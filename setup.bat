@echo off
echo ============================================
echo   CropGuard AI - One Click Setup (Windows)
echo ============================================
echo.

:: Step 1 - Create virtual environment
echo [1/5] Creating virtual environment...
python -m venv venv
echo Done!
echo.

:: Step 2 - Activate it
echo [2/5] Activating virtual environment...
call venv\Scripts\activate
echo Done!
echo.

:: Step 3 - Upgrade pip
echo [3/5] Upgrading pip...
python -m pip install --upgrade pip
echo Done!
echo.

:: Step 4 - Install PyTorch CPU version
echo [4/5] Installing PyTorch (CPU version)...
echo This may take 5-10 minutes depending on your internet...
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
echo Done!
echo.

:: Step 5 - Install other dependencies
echo [5/5] Installing other dependencies...
pip install numpy Pillow matplotlib seaborn pandas scikit-learn tqdm opencv-python jupyter ipykernel
echo Done!
echo.

:: Verify
echo ============================================
echo   Verifying Installation...
echo ============================================
python -c "import torch; print('PyTorch:', torch.__version__)"
python -c "import torchvision; print('Torchvision:', torchvision.__version__)"
python -c "import numpy; print('NumPy:', numpy.__version__)"
python -c "import PIL; print('Pillow: OK')"
python -c "import sklearn; print('Scikit-learn: OK')"
echo.
echo ============================================
echo   Setup Complete! 
echo ============================================
echo.
echo Next steps:
echo   1. Get dataset:  python scripts/download_data.py
echo   2. Train model:  python scripts/train_model.py --data_dir data/plantvillage --epochs 20 --batch_size 16
echo   3. Web app:      python app/server.py   then open http://localhost:8080
echo   4. Predict:      python scripts/predict.py --image data/sample_images/test_leaf.jpg
echo.
pause
