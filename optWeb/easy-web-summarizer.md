### [Easy Webpage Summarizer](https://github.com/cobanov/easy-web-summarizer)

![](https://img.shields.io/github/license/cobanov/easy-web-summarizer?style=flat-square)

````{tab} From source
```sh
git clone --depth=1 https://github.com/cobanov/easy-web-summarizer
cd easy-web-summarizer
uv venv
.venv\Scripts\activate.bat
uv pip install -r requirements.txt
ollama run llama3:instruct
python app/webui.py
```
````