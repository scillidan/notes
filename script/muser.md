### [muser](https://github.com/jordipons/musicnn) [^1][^2] (Cache)

```sh
git clone --depth=1 https://github.com/jonshamir/muser
git clone --depth=1 https://github.com/jordipons/musicnn muser/musicnn
cd muser
uv venv
.venv\Scripts\activate.bat
uv pip install --force-reinstall msgpack==1.0.4 cffi==1.15.1 llvmlite==0.39.1 pycparser==2.21 soxr==0.3.3 soundfile==0.12.1 numpy==1.23.5 pooch==1.6.0 scipy==1.10.1 setuptools==67.4.0 urllib3==1.26.14 idna==3.4 librosa==0.10.0
# uv pip install --force-reinstall msgpack-1.0.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl cffi-1.15.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl llvmlite-0.39.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl pycparser-2.21-py2.py3-none-any.whl soxr-0.3.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl  soundfile-0.12.1-py2.py3-none-manylinux_2_31_x86_64.whl numpy-1.23.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl pooch-1.6.0-py3-none-any.whl scipy-1.10.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl setuptools-67.4.0-py3-none-any.whl urllib3-1.26.14-py2.py3-none-any.whl idna-3.4-py3-none-any.whl librosa-0.10.0-py3-none-any.whl
cd musicnn
python setup.py install
cd ..
uv pip install --force-reinstall filetype==1.2.0 coverage==5.5 toml==0.10.2 eyed3==0.9.7
# uv pip install --force-reinstall filetype-1.2.0-py2.py3-none-any.whl coverage-5.5-cp310-cp310-manylinux1_x86_64.whl toml-0.10.2-py2.py3-none-any.whl eyed3-0.9.7-py3-none-any.whl
uv run --with jupyter jupyter lab
```

```sh
npm install
npm install --save-dev cross-env
npm run start
```

[^1]: [musicnn](https://github.com/jordipons/musicnn)
[^2]: [Using uv with Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/)