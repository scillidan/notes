# [PDF Narrator](https://github.com/mateogon/pdf-narrator)

![](https://img.shields.io/github/license/mateogon/pdf-narrator?style=flat-square)

```sh
git clone --depth=1 https://github.com/mateogon/pdf-narrator
cd pdf-narrator
uv venv --python 3.12
.venv\Scripts\activate.bat
uv pip install torch==2.6.0 torchaudio==2.6.0 torchvision==0.21.0 --index-url https://download.pytorch.org/whl/cu124
```

```sh
uv pip install deepspeed-0.11.2+cuda124-cp312-cp312-win_amd64.whl
uv pip install lxml-5.3.0-cp312-cp312-win_amd64.whl
uv pip install -r requirements.txt
uv pip install hf_transfer
python main.py
```