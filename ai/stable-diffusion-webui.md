### [Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

#### Selfhost

````{tab} From source [^1]
```sh
git clone --depth=1 https://github.com/AUTOMATIC1111/stable-diffusion-webui
cd stable-diffusion-webui
python -m venv venv
venv\Scripts\activate.bat
pip install torch torchvision torchaudio xformers --index-url https://download.pytorch.org/whl/cu121
```
````

Edit `webui-user.bat` [^2][^3][^4]:

```sh
set COMMANDLINE_ARGS=--xformers --port <port>
set XFORMERS_MORE_DETAILS=1
```

Download type `Checkpoint *` and put file `*.safetensors` into `models/Stable-diffusion`. Liked [Earth Satellite Image Map Generator Mix](https://civitai.com/models/18022/earth-satellite-image-map-generator-mix).

```sh
pip install hf_transfer
webui-user.bat
```
#### Install extensions

1. Extensions → Available → Load from → Search and Install.
2. Extensions → Install from URL.
3. Extensions → Installed → Apply and restartUI.

#### Reference

- [How to make web-ui available on local network](https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/6589)
- [Choosing which GPU to use when running](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/1561)

[^1]: [Manual Installation](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPUs#manual-installation)
[^2]: [How on earth can I install xformers?](https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/9802#discussioncomment-5894895)
[^3]: [Installing xFormers](https://github.com/facebookresearch/xformers#installing-xformers)
[^4]: [Command Line Arguments and Settings](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings)