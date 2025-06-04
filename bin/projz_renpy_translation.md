# [Projz - RenyPy Translation Toolkit](https://github.com/abse4411/projz_renpy_translation) (Later)

````{tab} From source
```sh
git clone --depth=1 https://github.com/abse4411/projz_renpy_translation
cd projz_renpy_translation
uv venv
.venv\Scripts\activate.bat
cp requirements_full.txt requirements_full.txt.bat
```

Edit `requirements_full.txt`:

```
# torch==2.0.1+cu117
# torchaudio==2.0.2+cu117
# torchvision==0.15.2+cu117
```

```sh
uv pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
uv pip install -r requirements_full.txt
python main.py
n <game_dir> -n <game_name>
i <game_name> -l schinese
t <game_name> -t ai -n {model_name} -l schinese -b 4
17 22
```
````