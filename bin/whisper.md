### [Whishper](https://github.com/openai/whisper)

````{tab} From source
```sh
git clone --depth=1 https://github.com/openai/whisper
cd whisper
uv venv
.venv\Scripts\activate.bat
uv pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
uv pip install -e .
whisper --model large-v3 --device cuda --language Chinese --output_format srt <input>
```
````