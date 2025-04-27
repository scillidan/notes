### [Kokoro TTS Local](https://github.com/PierrunoYT/Kokoro-TTS-Local)

````{tab} From source
```sh
git clone --depth=1 https://github.com/PierrunoYT/Kokoro-TTS-Local
cd Kokoro-TTS-Local
python -m venv venv
venv\Scripts\activate.bat
pip install torch --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
pip install hf_transfer
```
````

#### Usage

As CLI:

```sh
python tts_demo.py
```

As Web UI:

```sh
pip install ordered_set pypinyin cn2an jieba
python gradio_interface.py
```