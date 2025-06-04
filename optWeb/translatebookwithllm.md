# [TBL](https://github.com/hydropix/TranslateBookWithLLM) (Cache)

![](https://img.shields.io/github/license/hydropix/TranslateBookWithLLM?style=flat-square)

```sh
git clone --depth=1 https://github.com/hydropix/TranslateBookWithLLM
cd TranslateBookWithLLM
uv venv --python 3.9
.venv\Scripts\activate.bat
uv pip install flask flask-cors flask-socketio python-socketio requests tqdm aiohttp lxml ebooklib
python translation_api.py
```