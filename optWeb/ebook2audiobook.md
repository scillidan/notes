# [ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) (Cache)

![](https://img.shields.io/github/license/DrewThomasson/ebook2audiobook?style=flat-square)

````{tab} From source
```sh
git clone --depth=1 https://github.com/DrewThomasson/ebook2audiobook
cd ebook2audiobook
uv venv
.venv\Scripts\activate.bat
uv pip isntall -r requirements.txt
# uv pip install coqui-tts==0.24.2 pydub nltk beautifulsoup4 ebooklib tqdm gradio==4.44.0
uv python -m nltk.downloader punkt
uv python -m nltk.downloader punkt_tab
uv pip install mecab mecab-python3 unidic
python -m unidic download
```
```` 

## Usage

```sh
python app.py
```

```sh
python app.py --headless True --use_custom_model True --ebook <ebook_file_path> --voice <target_voice_file_path> --language <language> --custom_model <custom_model_path> --custom_config <custom_config_path> --custom_vocab <custom_vocab_path>
```