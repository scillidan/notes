### [Fish Speech](https://github.com/fishaudio/fish-speech) (Cache)

````{tab} From source
```sh
uv venv
.venv\Scripts\activate.bat
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
uv pip install https://github.com/AnyaCoder/fish-speech/releases/download/v0.1.0/triton_windows-0.1.0-py3-none-any.whl
uv pip install -e .
uv pip install hf_transfer
start.bat
```
````

If serve port used, edit `API_FLAGS.txt`.