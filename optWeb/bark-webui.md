### [Bark Web UI](https://github.com/makawy7/bark-webui)

![](https://img.shields.io/github/license/makawy7/bark-webui?style=flat-square)

````{tab} From source
```sh
git clone --depth=1 https://github.com/makawy7/bark-webui
cd bark-webui
uv venv
.venv\Scripts\activate.bat
uv pip install torch --index-url https://download.pytorch.org/whl/cu121
uv pip install .
uv pip install gradio
python webui.py
```
````