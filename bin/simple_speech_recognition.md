# [Simple_Speech_Recognition](https://github.com/Temmie-Flakes/Simple_Speech_Recognition)

```sh
git clone --depth=1 https://github.com/Temmie-Flakes/Simple_Speech_Recognition
cd Simple_Speech_Recognition
uv venv
.venv\Scripts\activate.bat
uv pip install torch --index-url https://download.pytorch.org/whl/cu121
uv pip install -r requirements.txt
uv pip install hf_transfer
```

1. Read `RunBaseModel.bat`.
2. Create other `.bat` you need liked `RunMediumModel.bat`.
3. Run `.bat`.