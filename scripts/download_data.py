"""
scripts/download_data.py
─────────────────────────
Downloads the PlantVillage dataset from Kaggle.

Usage:
    python scripts/download_data.py

Requirements:
    pip install kaggle
    Place kaggle.json in C:/Users/YourName/.kaggle/  (Windows)
                     or ~/.kaggle/                   (Mac/Linux)
"""

import os
import sys
import zipfile


def check_kaggle_setup():
    """Check if kaggle API is configured."""
    kaggle_dir = os.path.join(os.path.expanduser("~"), ".kaggle")
    kaggle_json = os.path.join(kaggle_dir, "kaggle.json")

    if not os.path.exists(kaggle_json):
        print("=" * 55)
        print("  Kaggle API key not found!")
        print("=" * 55)
        print()
        print("Steps to set it up:")
        print("  1. Go to https://www.kaggle.com")
        print("  2. Click your profile picture → Settings")
        print("  3. Scroll to 'API' section")
        print("  4. Click 'Create New Token'")
        print("  5. This downloads kaggle.json")
        print()
        print("  Windows: Move kaggle.json to:")
        print(f"    {kaggle_dir}\\")
        print()
        print("  Mac/Linux: Move kaggle.json to:")
        print("    ~/.kaggle/")
        print()
        return False
    return True


def download_plantvillage():
    """Download PlantVillage dataset from Kaggle."""
    print("=" * 55)
    print("  CropGuard AI — Dataset Download")
    print("=" * 55)
    print()

    # Check kaggle setup
    if not check_kaggle_setup():
        sys.exit(1)

    try:
        import kaggle
    except ImportError:
        print("Kaggle package not installed. Installing now...")
        os.system(f"{sys.executable} -m pip install kaggle")
        import kaggle

    # Create data directory
    os.makedirs("data", exist_ok=True)

    print("Downloading PlantVillage dataset (~1.5 GB)...")
    print("This may take 5-15 minutes depending on your internet speed.")
    print()

    try:
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(
            "abdallahalidev/plantvillage-dataset",
            path="data/",
            unzip=False,
        )

        # Find the downloaded zip
        zip_path = "data/plantvillage-dataset.zip"
        if not os.path.exists(zip_path):
            # Try alternate name
            for f in os.listdir("data/"):
                if f.endswith(".zip"):
                    zip_path = os.path.join("data", f)
                    break

        print(f"Extracting {zip_path}...")
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall("data/")

        print()
        print("Verifying dataset...")
        verify_dataset()

    except Exception as e:
        print(f"Download failed: {e}")
        print()
        print("Manual download steps:")
        print("  1. Visit: https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset")
        print("  2. Click Download")
        print("  3. Extract and place in: data/plantvillage/")
        sys.exit(1)


def verify_dataset(data_dir="data/plantvillage"):
    """Verify dataset structure and count images."""
    if not os.path.exists(data_dir):
        # Check for alternate extraction paths
        for entry in os.listdir("data/"):
            full_path = os.path.join("data", entry)
            if os.path.isdir(full_path) and len(os.listdir(full_path)) > 10:
                data_dir = full_path
                break

    if not os.path.exists(data_dir):
        print(f"Dataset not found at {data_dir}")
        return False

    classes = [
        d for d in os.listdir(data_dir)
        if os.path.isdir(os.path.join(data_dir, d))
    ]

    if not classes:
        print(f"No class folders found in {data_dir}")
        return False

    total = 0
    for cls in classes:
        cls_path = os.path.join(data_dir, cls)
        imgs = [
            f for f in os.listdir(cls_path)
            if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ]
        total += len(imgs)

    print(f"  Classes  : {len(classes)}")
    print(f"  Images   : {total:,}")
    print(f"  Location : {data_dir}")
    print()
    print("Dataset is ready for training!")
    return True


if __name__ == "__main__":
    download_plantvillage()
