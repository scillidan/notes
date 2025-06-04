# [Whisper-WebUI](https://github.com/jhj0517/Whisper-WebUI)

![](https://img.shields.io/github/license/jhj0517/Whisper-WebUI?style=flat-square)

````{tab} From source
```sh
git clone --depth=1 https://github.com/jhj0517/Whisper-WebUI
cd Whisper-WebUI
uv venv
.venv\Scripts\activate.bat
uv pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
uv pip install -r requirements.txt
uv pip install hf_transfer
user-start-webui.bat
```
````