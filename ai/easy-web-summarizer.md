### [Easy Webpage Summarizer](https://github.com/cobanov/easy-web-summarizer)

#### Selfhost

````{tab} From source
```sh
git clone --depth=1 https://github.com/cobanov/easy-web-summarizer
cd easy-web-summarizer
uv venv --python cpython-3.10.11-windows-x86_64-none
.venv\Scripts\activate.bat
uv pip install -r requirements.txt
ollama run llama3:instruct
python app/webui.py
```
````