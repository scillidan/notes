# [Easy Webpage Summarizer](https://github.com/cobanov/easy-web-summarizer)

![](https://img.shields.io/github/license/cobanov/easy-web-summarizer?style=flat-square)

```sh
git clone --depth=1 https://github.com/cobanov/easy-web-summarizer
cd easy-web-summarizer
uv venv
.venv\Scripts\activate.bat
uv pip install -r requirements.txt
ollama pull llama3:instruct
```

## Usage

As CLI:

```sh
python app/webui.py -u <url>
```

As GUI:

```sh
python app/webui.py
```