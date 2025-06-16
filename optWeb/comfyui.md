# [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

![](https://img.shields.io/github/license/comfyanonymous/ComfyUI?style=flat-square)

Get and install [CUDA Toolkit 12.8](https://developer.nvidia.com/cuda-12-8-0-download-archive)

````{tab} From source
```sh
git clone --depth=1 https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
python -m venv .venv
.venv\Scripts\activate.bat
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
pip install -r requirements.txt
python main.py
```
````

````{tab} From source (AMD) [^1] (Cache)
```sh
git clone --depth=1 https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
pip install torch-directml
set HSA_OVERRIDE_GFX_VERSION=10.3.0
python main.py --directml
```
````

## Workflow

```{include} comfyui/comfyui-auto_installer.md
```
```{include} comfyui/comfyui-tell-the-difference.md
```

## Optional

Settings → Comfy → Locale → Change language

## Usage

- ComfyUI → Manager
	- Custom Nodes Manager → Search → Install
	- Install Missing Custom Nodes

[^1]: [Installing ComfyUI on Windows for AMD GPUs](https://atlassc.net/2025/01/15/installing-comfyui-on-windows-for-amd-gpus)