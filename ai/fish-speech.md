### [Fish Speech](https://github.com/fishaudio/fish-speech) (Cache)

Edit `API_FLAGS.txt`:

```
--listen 0.0.0.0:<port> \
```

```sh
uv venv
.venv\Scripts\activate.bat
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
uv pip install https://github.com/AnyaCoder/fish-speech/releases/download/v0.1.0/triton_windows-0.1.0-py3-none-any.whl
uv pip install -e .
uv pip install hf_transfer
start.bat
```