### [ComfyUI](https://github.com/comfyanonymous/ComfyUI) (Wait)

````{tab} From source
```sh
git clone --depth=1 https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
uv venv
.venv\Scripts\activate.bat
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
uv pip install -r requirements.txt
python main.py
```
````

#### Plugin

#### [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)

```sh
git clone --depth=1 https://github.com/ltdrdata/ComfyUI-Manager custom_nodes\comfyui-manager
uv pip install -r custom_nodes\comfyui-manager\requirements.txt
```

Usage:

- ComfyUI → Manager
	- Custom Nodes Manager → Search → Install
	- Install Missing Custom Nodes

#### Workflow

##### [Change product background with the image of your choice using Style Transfer.](https://civitai.com/models/413803/change-product-background-with-the-image-of-your-choice-using-style-transfer) [^1]

````{tab} From source
```sh
git clone --depth=1 https://github.com/cubiq/ComfyUI_IPAdapter_plus custom_nodes\comfyui_ipadapter_plus
git clone --depth=1 https://github.com/cubiq/ComfyUI_essentials custom_nodes\comfyui_essentials
uv pip install -r custom_nodes\comfyui_essentials\requirements.txt
git clone --depth=1 https://github.com/Fannovel16/comfyui_controlnet_aux custom_nodes\comfyui_controlnet_aux
uv pip install -r custom_nodes\comfyui_controlnet_aux\requirements.txt
uv pip install onnxruntime-gpu
```
````

##### [Workflow ComfyUi - Modify clothes at full resolution](https://civitai.com/models/304986/workflow-comfyui-modify-clothes-at-full-resolution)

````{tab} From source
```sh
git clone --depth=1 https://github.com/jags111/efficiency-nodes-comfyui custom_nodes\efficiency-nodes-comfyui
uv pip install -r custom_nodes\efficiency-nodes-comfyui\requirements.txt
git clone --depth=1 https://github.com/WASasquatch/was-node-suite-comfyui custom_nodes\was-node-suite-comfyui
uv pip install -r custom_nodes\was-node-suite-comfyui\requirements.txt
git clone --depth=1 https://github.com/BadCafeCode/masquerade-nodes-comfyui custom_nodes\masquerade-nodes-comfyui
git clone --depth=1 https://github.com/ltdrdata/ComfyUI-Impact-Pack custom_nodes\comfyui-impact-pack
uv pip install -r custom_nodes\comfyui-impact-pack\requirements.txt
git clone --depth=1 https://github.com/rgthree/rgthree-comfy custom_nodes\rgthree-comfy
git clone --depth=1 https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes comfyui_comfyroll_customnodes
```
````

##### [ComfyUI — Tell the Difference](https://civitai.com/models/533218/comfyui-tell-the-difference)

````{tab} From source
```sh
git clone --depth=1 https://github.com/chrisgoringe/cg-use-everywhere custom_nodes\cg-use-everywhere
git clone --depth=1 https://github.com/Smirnov75/ComfyUI-mxToolkit custom_nodes\comfyui-mxtoolkit
git clone --depth=1 https://github.com/chflame163/ComfyUI_LayerStyle custom_nodes\comfyui_layerstyle
uv pip install -r custom_nodes\comfyui_layerstyle\requirements.txt
```
````

#### Optional

Settings → Comfy → Locale → Change language

[^1]: [Error occurred when executing DepthAnythingPreprocessor:](https://github.com/Fannovel16/comfyui_controlnet_aux/issues/338)