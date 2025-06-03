### [talking-head-anime-4-demo](https://github.com/pkhungurn/talking-head-anime-4-demo)

````{tab} From source
```sh
git clone --depth=1 https://github.com/pkhungurn/talking-head-anime-4-demo
cd talking-head-anime-4-demo
uv venv
.venv\Scripts\activate.bat
uv pip install poetry
cd poetry
poetry install
cd ..
python src\tha4\app\character_model_ifacialmocap_puppeteer.py
```
````