# [TTS](https://github.com/coqui-ai/TTS) [^1]

```sh
scoop install espeak-ng
```

````{tab} From source
```sh
git clone --depth=1 https://github.com/coqui-ai/TTS
uv venv
.venv\Scripts\activate.bat
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
uv pip install -e .
```
````

## Usage

```sh
tts --list_models
tts --model_name "tts_models/multilingual/multi-dataset/xtts_v2" --list_speaker_idxs
tts --model_name "tts_models/multilingual/multi-dataset/xtts_v2" --list_language_idxs
```

```sh
tts --device cuda --model_name "tts_models/multilingual/multi-dataset/xtts_v2" --speaker_idx "Claribel Dervla" --language_idx "en" --text "<text>" --out_path temp.wav
```

## Sample files

- [file_tts](https://github.com/scillidan/file_tts)

[^1]: [How can I run Mozilla TTS/Coqui TTS training with CUDA on a Windows system?](https://stackoverflow.com/questions/66726331/how-can-i-run-mozilla-tts-coqui-tts-training-with-cuda-on-a-windows-system)