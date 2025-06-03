### [FastKokoro](https://github.com/remsky/Kokoro-FastAPI)

`````{tab} From source [^1]
```sh
git clone --depth=1 https://github.com/remsky/Kokoro-FastAPI
cd Kokoro-FastAPI
```

````{tab} Windows 10
```sh
scoop install espeak-ng
```

```sh
uv venv
.venv\Scripts\activate.bat
set PHONEMIZER_ESPEAK_LIBRARY="C:\Users\User\Scoop\apps\espeak-ng\current\eSpeak NG\libespeak-ng.dll"
set PYTHONUTF8=1
set PROJECT_ROOT=%cd%
set USE_GPU=true
set USE_ONNX=false
set PYTHONPATH=%PROJECT_ROOT%;%PROJECT_ROOT%\api
set MODEL_DIR=src\models
set VOICES_DIR=src\voices\v1_0
set WEB_PLAYER_PATH=%PROJECT_ROOT%\web
uv pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cu124
uv pip install -e ".[gpu]"
```
````

````{tab} Ubuntu 24 ARM (Cache)
```sh
sudo apt install ffmpeg espeak-ng
```

```sh
uv venv
source .venv/Scripts/activate
export PYTHONUTF8=1
export PROJECT_ROOT=%cd%
export USE_GPU=false
export USE_ONNX=false
export PYTHONPATH=%PROJECT_ROOT%;%PROJECT_ROOT%/api
export MODEL_DIR=src/models
export VOICES_DIR=src/voices/v1_0
export WEB_PLAYER_PATH=%PROJECT_ROOT%/web
uv pip install -e .
```
````

```sh
uv run --no-sync python docker/scripts/download_model.py --output api/src/models/v1_0
uv run --no-sync uvicorn api.src.main:app --host 127.0.0.1 --port 8880
# uv run --no-sync uvicorn api.src.main:app --host 0.0.0.0 --port 8880
```
`````

[^1]: [start-gpu.ps1](https://github.com/remsky/Kokoro-FastAPI/blob/master/start-gpu.ps1)