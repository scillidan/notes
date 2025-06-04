# [Stable Diffusion web UI for AMDGPUs](https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu)

````{tab} From source
```sh
git clone --depth=1 https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu
cd stable-diffusion-webui-amdgpu
python -m venv venv
venv\Scripts\activate.bat
subl webui-user.bat
```

```bat
set COMMANDLINE_ARGS="--use-directml"
```

```sh
pip install hf_transfer
webui-user.bat
```
````