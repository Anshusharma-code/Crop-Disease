"""
scripts/predict.py
───────────────────
Run disease detection on a single leaf image using the trained model.

Usage:
    python scripts/predict.py --image data/sample_images/leaf.jpg
    python scripts/predict.py --image leaf.jpg --top_k 5
"""

import os
import sys
import argparse

import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from utils.disease_db import get_disease_info


# ── Load trained model ─────────────────────────────────────────────────────────
def load_model(model_path: str):
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model not found at {model_path}\n"
            "Run training first:  python scripts/train_model.py"
        )

    ckpt         = torch.load(model_path, map_location="cpu")
    architecture = ckpt.get("architecture", "mobilenet")
    class_names  = ckpt["class_names"]
    n            = len(class_names)

    if architecture == "mobilenet":
        model = models.mobilenet_v2(weights=None)
        model.classifier = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(model.last_channel, 512),
            nn.ReLU(inplace=True),
            nn.Dropout(0.2),
            nn.Linear(512, n),
        )
    elif architecture == "resnet18":
        model = models.resnet18(weights=None)
        model.fc = nn.Sequential(
            nn.Linear(512, 256), nn.ReLU(inplace=True),
            nn.Dropout(0.3), nn.Linear(256, n),
        )
    else:
        model = models.resnet50(weights=None)
        model.fc = nn.Sequential(
            nn.Linear(2048, 512), nn.ReLU(inplace=True),
            nn.Dropout(0.3), nn.Linear(512, n),
        )

    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()
    return model, class_names


# ── Preprocess image ───────────────────────────────────────────────────────────
def preprocess(image_path: str) -> torch.Tensor:
    tf = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225]),
    ])
    img = Image.open(image_path).convert("RGB")
    return tf(img).unsqueeze(0)


# ── Predict ────────────────────────────────────────────────────────────────────
def predict(image_path: str, model_path: str = None, top_k: int = 3) -> dict:
    if model_path is None:
        model_path = os.path.join(ROOT, "models", "crop_disease_model.pth")

    model, class_names = load_model(model_path)
    tensor = preprocess(image_path)

    with torch.no_grad():
        probs = torch.softmax(model(tensor), dim=1)

    top_p, top_i = torch.topk(probs, k=min(top_k, len(class_names)))
    top_p = top_p.squeeze().tolist()
    top_i = top_i.squeeze().tolist()

    if not isinstance(top_p, list):
        top_p, top_i = [top_p], [top_i]

    top_predictions = [
        {"disease": class_names[i], "confidence": round(p * 100, 2)}
        for i, p in zip(top_i, top_p)
    ]

    return {
        "prediction":      top_predictions[0]["disease"],
        "confidence":      top_predictions[0]["confidence"],
        "top_predictions": top_predictions,
        "disease_info":    get_disease_info(top_predictions[0]["disease"]),
    }


# ── Pretty print ───────────────────────────────────────────────────────────────
def print_result(result: dict):
    SEP = "=" * 58
    print(f"\n{SEP}")
    print("  CropGuard AI — Detection Result")
    print(SEP)

    pred = result["prediction"]
    conf = result["confidence"]
    info = result["disease_info"]

    print(f"\n  Prediction  : {pred}")
    print(f"  Confidence  : {conf:.2f}%")

    if info:
        print(f"\n  Disease     : {info['common_name']}")
        print(f"  Crop        : {info['crop']}")
        print(f"  Pathogen    : {info['pathogen']}")
        print(f"  Severity    : {info['severity']}")
        print(f"\n  Symptoms    : {info['symptoms']}")

    print(f"\n  Top {len(result['top_predictions'])} Predictions:")
    for i, p in enumerate(result["top_predictions"], 1):
        bar = "█" * int(p["confidence"] / 4)
        print(f"  {i}. {p['disease']:<48}  {p['confidence']:>6.2f}%  {bar}")

    if info and info.get("remedy"):
        print(f"\n  Recommended Treatment:")
        for j, r in enumerate(info["remedy"], 1):
            print(f"    {j}. {r}")

        print(f"\n  Prevention  : {info['prevention']}")

    print(f"\n{SEP}\n")


# ── CLI ────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Predict crop disease from a leaf image")
    ap.add_argument("--image",  required=True, help="Path to the leaf image")
    ap.add_argument("--model",  default=None,  help="Path to trained model (.pth)")
    ap.add_argument("--top_k", type=int, default=3, help="Number of top predictions")
    args = ap.parse_args()

    result = predict(args.image, args.model, args.top_k)
    print_result(result)
