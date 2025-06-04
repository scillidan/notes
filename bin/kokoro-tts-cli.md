# [kokoro-tts-cli](https://github.com/cheuerde/kokoro-tts-cli) (Cacel)

```sh
git clone --depth=1 https://github.com/cheuerde/kokoro-tts-cli
cd kokoro-tts-cli
uv venv
.venv\Scripts\activate.bat
uv pip install torch --index-url https://download.pytorch.org/whl/cu121
uv pip install tqdm sounddevice scipy numpy phonemizer transformers
uv pip install windows-curses
python setup.py install
set KOKORO_PATH="<path_to>\Kokoro-TTS-Local"
echo 'Hello! How are you today?' | kokoro-tts
```

- [Processing Modes](https://github.com/cheuerde/kokoro-tts-cli?tab=readme-ov-file#processing-modes)