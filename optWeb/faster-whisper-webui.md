### [faster-whisper-webui](https://huggingface.co/spaces/aadnk/faster-whisper-webui) (Cache)

![](https://img.shields.io/github/license/aadnk/faster-whisper-webui?style=flat-square)

````{tab} From source [^1][^2][^3][^4]
```sh
git clone https://huggingface.co/spaces/aadnk/faster-whisper-webui
cd faster-whisper-webui
uv venv
.venv\Scripts\activate.bat
set "CUDA_PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8"
echo %CUDA_PATH%
uv pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
uv pip install -r requirements.txt
uv pip install -r requirements-fasterWhisper.txt
uv pip install hf_transfer
cp config.json5 config.json5.bak
```
````

Edit `config.json5` liked:

```json
"models": [
  {
    "name": "medium",
    "url": "Simple_Speech_Recognition/modelsCache/faster-whisper-medium",
    "type": "filesystem"
  },
  {
    "name": "large-v2",
    "url": "Simple_Speech_Recognition/modelsCache/faster-whisper-large-v2",
    "type": "filesystem"
  },
  {
    "name": "large-v3",
    "url": "Simple_Speech_Recognition/modelsCache/faster-whisper-large-v3",
    "type": "filesystem"
  },
]
"input_audio_max_duration": -1,
"server_port": 7830,
"whisper_implementation": "faster-whisper",
"default_model_name": "medium",
"vad_parallel_devices": 0,
"auto_parallel": true,
"output_dir": "<output_dir>",
"language": "Chinese",
```

#### Usage

As CLI:

```sh
python cli.py --whisper_implementation "faster-whisper" --vad "silero-vad-skip-gaps" --auto_parallel true --vad_parallel_devices 0 --model "large-v2" --language "Chinese" --initial_prompt="对于普通话句子，以中文简体输出" --diarization_num_speakers 1 --auth_token <hf_token> --output_dir "C:/Users/User/Downloads" <input>
```

As Web UI:

```sh
python.exe app.py --input_audio_max_duration -1 --server_name 127.0.0.1 --server_port 7830 --whisper_implementation "faster-whisper" --default_model_name "large-v2" --vad_parallel_devices 0 --auto_parallel true --auth_token <hf_token> --output_dir "C:/Users/User/Downloads"
```

#### Reference

- [what diff_silero-vad, silero-vad-skip-gaps, silero-vad-expan d-into-gaps, periodic-vad_02.md](https://github.com/scillidan/gpt_share/blob/main/what%20diff_silero-vad%2C%20silero-vad-skip-gaps%2C%20silero-vad-expan%20d-into-gaps%2C%20periodic-vad_02.md)

[^1]: [Running Locally](https://huggingface.co/spaces/aadnk/faster-whisper-webui/blob/main/README.md#running-locally)
[^2]: [Enabling custom Japanese model](https://huggingface.co/spaces/aadnk/faster-whisper-webui/discussions/5)
[^3]: [services.py](https://github.com/usoonees/logseq-whisper-subtitles-server/blob/main/logseq_whisper_subtitles_server/services.py)
[^4]: [Segmentation Fault when loading pyannote/speaker-diarization-3.0 in rockylinux9/python3 environment](https://github.com/pyannote/pyannote-audio/issues/1499)