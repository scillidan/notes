### [F5-TTS](https://github.com/SWivid/F5-TTS)

````{tab} From source
```sh
git clone --depth=1 https://github.com/SWivid/F5-TTS
cd F5-TTS
uv venv
.venv\Scripts\activate.bat
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
uv pip install -e .
uv pip install hf_transfer
f5-tts_infer-gradio
```
````