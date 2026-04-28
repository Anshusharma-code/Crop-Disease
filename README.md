# 🌿 CropGuard AI — Crop Disease Detection

> Deep learning system to detect plant diseases from leaf images.
> CPU-friendly · MobileNetV2 · 38 diseases · 14 crops · ~96% accuracy

---

## 📁 Project Structure

```
cropguard/
│
├── .vscode/
│   ├── settings.json        ← VS Code auto-configured for this project
│   ├── launch.json          ← One-click Run buttons for Train / Predict / Server
│   └── extensions.json      ← Recommended extensions list
│
├── data/
│   └── sample_images/       ← Put test leaf images here
│
├── models/                  ← Trained model saved here after training
│
├── notebooks/
│   └── training_notebook.ipynb
│
├── scripts/
│   ├── download_data.py     ← Download PlantVillage dataset
│   ├── train_model.py       ← Train the model (run this first)
│   └── predict.py           ← Predict disease from a single image
│
├── utils/
│   ├── __init__.py
│   └── disease_db.py        ← Disease info, remedies, prevention (38 diseases)
│
├── app/
│   ├── index.html           ← Web interface
│   └── server.py            ← Local web server (opens browser automatically)
│
├── setup.bat                ← Windows one-click setup
├── setup.sh                 ← Mac/Linux one-click setup
├── requirements.txt
└── README.md
```

---

## 🚀 Setup in VS Code (Step by Step)

### Step 1 — Open the project in VS Code
```
File → Open Folder → select the cropguard folder
```

### Step 2 — Install recommended extensions
VS Code will show a popup: **"Do you want to install recommended extensions?"**
Click **Install All**. This installs Python, Jupyter, and Pylance.

### Step 3 — Run the setup script

Open the **VS Code Terminal** with `` Ctrl+` `` then run:

**Windows:**
```cmd
setup.bat
```

**Mac / Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

This automatically:
- Creates a virtual environment (`venv/`)
- Installs PyTorch (CPU version)
- Installs all other dependencies
- Verifies everything works

### Step 4 — Select Python interpreter
Press `Ctrl+Shift+P` → type **Python: Select Interpreter**
→ Choose the one that says `venv` (e.g. `./venv/Scripts/python.exe`)

---

## 📦 Getting the Dataset

### Option A — Kaggle (Free, Recommended)
1. Sign up at [kaggle.com](https://www.kaggle.com) (free)
2. Profile → Settings → API → **Create New Token** → downloads `kaggle.json`
3. Move `kaggle.json` to:
   - Windows: `C:\Users\YourName\.kaggle\`
   - Mac/Linux: `~/.kaggle/`
4. In VS Code terminal:
```cmd
python scripts/download_data.py
```

### Option B — Manual
1. Visit: https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset
2. Download zip → extract → place contents in `data/plantvillage/`

The folder should look like:
```
data/plantvillage/
    Apple___Apple_scab/       ← folder with .jpg images
    Apple___Black_rot/
    Tomato___Early_blight/
    ...38 folders total
```

---

## 🏋️ Training the Model

### From VS Code Terminal:
```cmd
python scripts/train_model.py --data_dir data/plantvillage --epochs 20 --batch_size 16
```

### From VS Code Run button:
Press `F5` → select **"Train Model"** from the dropdown.

| Setting | Value | Notes |
|---------|-------|-------|
| Architecture | mobilenet | Fastest on CPU |
| Epochs | 20 | ~2-4 hrs on CPU |
| Batch size | 16 | Reduce to 8 if RAM issues |

Progress shown live in terminal. Best model auto-saved to `models/`.

**Free GPU option:** Upload to [Google Colab](https://colab.research.google.com) → training takes ~30 mins instead.

---

## 🔮 Predicting from an Image

```cmd
python scripts/predict.py --image data/sample_images/leaf.jpg
```

Output:
```
  Prediction  : Tomato___Early_blight
  Confidence  : 94.30%
  Disease     : Early Blight
  Severity    : Medium
  Treatment:
    1. Apply chlorothalonil or mancozeb fungicides
    2. Stake plants to improve air circulation
    ...
```

---

## 🌐 Running the Web App

```cmd
python app/server.py
```

Browser opens automatically at `http://localhost:8080`.

Features:
- Drag & drop image upload
- Sample disease buttons (no training needed)
- Confidence score with visual bar
- Top 3 predictions
- Treatment recommendations
- AI deep analysis

---

## 📓 Opening the Notebook

```cmd
jupyter notebook
```

Navigate to `notebooks/training_notebook.ipynb`

Or in VS Code: just click the `.ipynb` file — it opens inline.

---

## ✅ VS Code Run Configurations (F5 Menu)

| Config Name | What it does |
|-------------|-------------|
| Train Model | Runs full training pipeline |
| Predict Disease | Predicts on a test image |
| Run Web App | Starts local server + opens browser |

---

## 🆘 Common Issues

| Problem | Fix |
|---------|-----|
| `ModuleNotFoundError: torch` | Run `venv\Scripts\activate` first |
| `CUDA not available` warning | Normal — CPU is used automatically |
| `Out of Memory` during training | Use `--batch_size 8` |
| Web app `401` error | Sample buttons work without API key |
| Dataset not found | Check path is `data/plantvillage/` with 38 subfolders |
| `python` not recognized | Add Python to PATH during install |
