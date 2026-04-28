"""
scripts/train_model.py
───────────────────────
Trains a MobileNetV2 transfer learning model on PlantVillage dataset.
CPU-friendly: ~2-4 hours for 20 epochs on a standard laptop.

Usage:
    python scripts/train_model.py
    python scripts/train_model.py --epochs 20 --batch_size 16
    python scripts/train_model.py --architecture resnet18 --epochs 25

Press Ctrl+C at any time to stop — the best model so far is always saved.
"""

import os
import sys
import json
import time
import argparse

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms, models

import numpy as np
import matplotlib
matplotlib.use("Agg")          # non-interactive backend (safe for all OS)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from tqdm import tqdm


# ── Paths ──────────────────────────────────────────────────────────────────────
ROOT         = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH   = os.path.join(ROOT, "models", "crop_disease_model.pth")
METRICS_PATH = os.path.join(ROOT, "models", "training_metrics.json")
CURVES_PATH  = os.path.join(ROOT, "models", "training_curves.png")
CM_PATH      = os.path.join(ROOT, "models", "confusion_matrix.png")

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


# ── Transforms ────────────────────────────────────────────────────────────────
def get_transforms():
    """
    Train transform  → augmentation + normalization
    Val/Test transform → resize + normalization only
    """
    mean = [0.485, 0.456, 0.406]   # ImageNet statistics
    std  = [0.229, 0.224, 0.225]

    train_tf = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.2),
        transforms.RandomRotation(degrees=30),
        transforms.ColorJitter(brightness=0.3, contrast=0.3,
                               saturation=0.3, hue=0.1),
        transforms.RandomGrayscale(p=0.05),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])

    val_tf = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])

    return train_tf, val_tf


# ── Model ─────────────────────────────────────────────────────────────────────
def build_model(num_classes: int, architecture: str = "mobilenet") -> nn.Module:
    """
    Build a pretrained model with a custom classification head.

    architecture options:
      mobilenet  — fastest on CPU (~2-4 hrs / 20 epochs)
      resnet18   — good balance (~4-6 hrs)
      resnet50   — highest accuracy (~8-12 hrs)
    """
    print(f"  Architecture : {architecture}")
    print(f"  Classes      : {num_classes}")
    print(f"  Device       : {DEVICE}")
    print()

    if architecture == "mobilenet":
        model = models.mobilenet_v2(weights="IMAGENET1K_V1")
        for p in list(model.parameters())[:-20]:    # freeze early layers
            p.requires_grad = False
        model.classifier = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(model.last_channel, 512),
            nn.ReLU(inplace=True),
            nn.Dropout(0.2),
            nn.Linear(512, num_classes),
        )

    elif architecture == "resnet18":
        model = models.resnet18(weights="IMAGENET1K_V1")
        for p in list(model.parameters())[:-10]:
            p.requires_grad = False
        model.fc = nn.Sequential(
            nn.Linear(512, 256),
            nn.ReLU(inplace=True),
            nn.Dropout(0.3),
            nn.Linear(256, num_classes),
        )

    elif architecture == "resnet50":
        model = models.resnet50(weights="IMAGENET1K_V1")
        for p in list(model.parameters())[:-15]:
            p.requires_grad = False
        model.fc = nn.Sequential(
            nn.Linear(2048, 512),
            nn.ReLU(inplace=True),
            nn.Dropout(0.3),
            nn.Linear(512, num_classes),
        )

    else:
        raise ValueError(f"Unknown architecture: {architecture}")

    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total     = sum(p.numel() for p in model.parameters())
    print(f"  Parameters   : {total:,} total  |  {trainable:,} trainable")
    print()

    return model.to(DEVICE)


# ── Train / Validate one epoch ─────────────────────────────────────────────────
def train_epoch(model, loader, optimizer, criterion):
    model.train()
    total_loss = correct = total = 0

    for imgs, labels in tqdm(loader, desc="  train", leave=False, ncols=70):
        imgs, labels = imgs.to(DEVICE), labels.to(DEVICE)

        optimizer.zero_grad()
        out  = model(imgs)
        loss = criterion(out, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        correct    += out.argmax(1).eq(labels).sum().item()
        total      += labels.size(0)

    return total_loss / len(loader), 100.0 * correct / total


def val_epoch(model, loader, criterion):
    model.eval()
    total_loss = correct = total = 0

    with torch.no_grad():
        for imgs, labels in tqdm(loader, desc="  val  ", leave=False, ncols=70):
            imgs, labels = imgs.to(DEVICE), labels.to(DEVICE)
            out  = model(imgs)
            loss = criterion(out, labels)

            total_loss += loss.item()
            correct    += out.argmax(1).eq(labels).sum().item()
            total      += labels.size(0)

    return total_loss / len(loader), 100.0 * correct / total


# ── Plots ──────────────────────────────────────────────────────────────────────
def save_curves(history):
    epochs = range(1, len(history["train_loss"]) + 1)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("Training History — CropGuard AI", fontsize=15, fontweight="bold")

    for ax, key, title in [
        (axes[0], "loss", "Loss"),
        (axes[1], "acc",  "Accuracy (%)"),
    ]:
        ax.plot(epochs, history[f"train_{key}"], "b-o", lw=2, ms=4, label="Train")
        ax.plot(epochs, history[f"val_{key}"],   "r-o", lw=2, ms=4, label="Val")
        ax.fill_between(epochs, history[f"train_{key}"], alpha=0.08, color="blue")
        ax.fill_between(epochs, history[f"val_{key}"],   alpha=0.08, color="red")
        ax.set_title(title); ax.set_xlabel("Epoch")
        ax.legend(); ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(CURVES_PATH, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved curves → {CURVES_PATH}")


def save_confusion_matrix(y_true, y_pred, class_names):
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(22, 20))
    sns.heatmap(cm, annot=False, fmt="d", cmap="Greens",
                xticklabels=class_names, yticklabels=class_names, ax=ax)
    ax.set_title("Confusion Matrix", fontsize=16, fontweight="bold", pad=20)
    ax.set_xlabel("Predicted"); ax.set_ylabel("True")
    ax.tick_params(axis="x", rotation=90, labelsize=7)
    ax.tick_params(axis="y", rotation=0,  labelsize=7)
    plt.tight_layout()
    plt.savefig(CM_PATH, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved confusion matrix → {CM_PATH}")


# ── Main ───────────────────────────────────────────────────────────────────────
def train(data_dir: str, architecture: str, epochs: int, batch_size: int):
    os.makedirs(os.path.join(ROOT, "models"), exist_ok=True)

    print()
    print("=" * 55)
    print("  CropGuard AI — Model Training")
    print("=" * 55)

    # ── Dataset ──
    train_tf, val_tf = get_transforms()
    full_ds = datasets.ImageFolder(data_dir, transform=train_tf)
    class_names = full_ds.classes

    n       = len(full_ds)
    n_train = int(0.80 * n)
    n_val   = int(0.10 * n)
    n_test  = n - n_train - n_val

    train_ds, val_ds, test_ds = random_split(
        full_ds, [n_train, n_val, n_test],
        generator=torch.Generator().manual_seed(42),
    )
    val_ds.dataset.transform  = val_tf
    test_ds.dataset.transform = val_tf

    nw = 0 if DEVICE == "cpu" else 2      # num_workers
    train_loader = DataLoader(train_ds, batch_size, shuffle=True,  num_workers=nw, pin_memory=False)
    val_loader   = DataLoader(val_ds,   batch_size, shuffle=False, num_workers=nw, pin_memory=False)
    test_loader  = DataLoader(test_ds,  batch_size, shuffle=False, num_workers=nw, pin_memory=False)

    print(f"  Dataset      : {n:,} images  |  {len(class_names)} classes")
    print(f"  Train/Val/Test: {n_train:,} / {n_val:,} / {n_test:,}")
    print(f"  Batch size   : {batch_size}")
    print(f"  Epochs       : {epochs}")
    print()

    # ── Model / Loss / Optimizer ──
    model     = build_model(len(class_names), architecture)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(
        filter(lambda p: p.requires_grad, model.parameters()),
        lr=1e-3, weight_decay=1e-4,
    )
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)

    # ── Training loop ──
    history = {"train_loss": [], "train_acc": [], "val_loss": [], "val_acc": []}
    best_val_acc = 0.0

    for epoch in range(1, epochs + 1):
        print(f"Epoch [{epoch:02d}/{epochs}]")
        t0 = time.time()

        tr_loss, tr_acc = train_epoch(model, train_loader, optimizer, criterion)
        vl_loss, vl_acc = val_epoch(model, val_loader, criterion)
        scheduler.step()

        history["train_loss"].append(tr_loss)
        history["train_acc"].append(tr_acc)
        history["val_loss"].append(vl_loss)
        history["val_acc"].append(vl_acc)

        elapsed = time.time() - t0
        print(f"  Train  loss={tr_loss:.4f}  acc={tr_acc:.2f}%")
        print(f"  Val    loss={vl_loss:.4f}  acc={vl_acc:.2f}%   ({elapsed:.0f}s)")

        if vl_acc > best_val_acc:
            best_val_acc = vl_acc
            torch.save({
                "epoch":              epoch,
                "model_state_dict":   model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "val_acc":            vl_acc,
                "class_names":        class_names,
                "architecture":       architecture,
            }, MODEL_PATH)
            print(f"  ✓ Best model saved  (val_acc={vl_acc:.2f}%)")
        print()

    # ── Test evaluation ──
    print("=" * 55)
    print("  Evaluating on test set …")
    ckpt = torch.load(MODEL_PATH, map_location=DEVICE)
    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()

    all_preds, all_labels = [], []
    with torch.no_grad():
        for imgs, labels in tqdm(test_loader, desc="  test ", ncols=70):
            out = model(imgs.to(DEVICE))
            all_preds.extend(out.argmax(1).cpu().tolist())
            all_labels.extend(labels.tolist())

    test_acc = 100 * sum(p == l for p, l in zip(all_preds, all_labels)) / len(all_labels)
    print(f"\n  Test accuracy : {test_acc:.2f}%")
    print(f"  Best val acc  : {best_val_acc:.2f}%")
    print()
    print(classification_report(all_labels, all_preds, target_names=class_names))

    # ── Save metrics + plots ──
    metrics = {
        "best_val_accuracy": best_val_acc,
        "test_accuracy":     test_acc,
        "architecture":      architecture,
        "epochs":            epochs,
        "class_names":       class_names,
        "history":           history,
    }
    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=2)

    save_curves(history)
    save_confusion_matrix(all_labels, all_preds, class_names)

    print()
    print("=" * 55)
    print(f"  Training complete!  Best val acc = {best_val_acc:.2f}%")
    print(f"  Model saved → {MODEL_PATH}")
    print("=" * 55)


# ── CLI ────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Train CropGuard disease detection model")
    ap.add_argument("--data_dir",     default="data/plantvillage",
                    help="Path to PlantVillage dataset root")
    ap.add_argument("--architecture", default="mobilenet",
                    choices=["mobilenet", "resnet18", "resnet50"],
                    help="Model backbone (mobilenet is fastest on CPU)")
    ap.add_argument("--epochs",       type=int, default=20)
    ap.add_argument("--batch_size",   type=int, default=16,
                    help="Reduce to 8 if you run out of RAM")
    args = ap.parse_args()

    train(args.data_dir, args.architecture, args.epochs, args.batch_size)
