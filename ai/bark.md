### [Bark](https://github.com/suno-ai/bark)

```sh
git lfs install
git clone https://huggingface.co/spaces/suno/bark
cd bark
uv venv
.venv\Scripts\activate.bat
uv pip install torch --index-url https://download.pytorch.org/whl/cu121
uv pip install -e .
uv pip install hf_transfer
python -m bark --text "<text>" --output_filename "temp.wav"
ffplay -autoexit temp.wav
```