### [MeloTTS](https://github.com/myshell-ai/MeloTTS)

````{tab} From source
```sh
git clone --depth=1 https://github.com/myshell-ai/MeloTTS
uv venv
.venv\Scripts\activate.bat
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
uv pip install -e .
uv pip install hf_transfer
python -m unidic download
```
````

#### Usage

```sh
melo "Hello" temp.wav --language EN
melo --device cuda --language EN "<text>" temp.wav && ffplay -autoexit temp.wav
```

With Web UI:

```sh
python melo/app.py
```

[^1]: [运行web_demo_gradio.py报gbk解码错误，cli和streamlit则可以正常运行](https://github.com/THUDM/ChatGLM3/discussions/1009)