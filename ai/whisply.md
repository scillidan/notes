### [whisply](https://github.com/tsmdt/whisply) (Cache)

```sh
git clone --depth=1 https://github.com/tsmdt/whisply
cd whisply
```

Edit `setup.py`:

```py
with open("README.md", "r") as fh:
    long_description = fh.read()
```

To:

```py
with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
```

```sh
uv venv
.venv\Scripts\activate.bat
uv pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
uv pip install .
# pip uninstall numpy
# pip install numpy==1.26.3
pip install hf_transfer
whisply --hf_token <token> --translate --subtitle --annotate --model large-v3 --lang zh --device gpu --files <input>
```

[^1]: [Incompatible with NumPy 2.0...](https://github.com/Vaibhavs10/insanely-fast-whisper/issues/233)