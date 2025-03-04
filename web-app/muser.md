### [Muser](https://github.com/jonshamir/muser) (Wait)

![](https://img.shields.io/github/license/jonshamir/muser?label=&style=flat-square) [![](https://img.shields.io/github/last-commit/scillidan/muser/master?label=&style=flat-square)](https://github.com/scillidan/muser) ![](https://img.shields.io/badge/GitHub%20Pages-121013?logo=github&logoColor=white)

````{tab} Arch [^1]
```sh
git clone --depth=1 https://github.com/jordipons/musicnn
cd musicnn
uv python install 3.7.9
uv venv --python 3.7.9
source .venv\Scripts\activate.bat
uv pip install -e .
uv pip install matplotlib
yay -S libxcrypt-compat
uv run --with jupyter jupyter lab
```
````

```sh
git clone --depth=1 https://github.com/jonshamir/muser
cd muser
npm install
npm install --save-dev cross-env
npm run start
# set NODE_ENV=development && node tools/bundler.js
```

[^1]: [Using uv with Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/)