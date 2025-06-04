# [Kokoro TTS](https://github.com/nazdridoy/kokoro-tts)

````{tab} From source
```sh
git clone --depth=1 https://github.com/nazdridoy/kokoro-tts
cd kokoro-tts
uv venv --python 3.12
.venv\Scripts\activate.bat
uv pip install -r requirements.txt
wget https://github.com/nazdridoy/kokoro-tts/releases/download/v1.0.0/voices-v1.0.bin
wget https://github.com/nazdridoy/kokoro-tts/releases/download/v1.0.0/kokoro-v1.0.onnx
```
````

## [Usage](https://github.com/nazdridoy/kokoro-tts#usage)

```sh
python kokoro-tts input.txt output.wav --speed 1.2 --lang en-us --voice af_alloy
python kokoro-tts input.txt output.wav --speed 1 --lang en-us --voice af_sarah
```