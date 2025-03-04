### [Image/Manga Translator](https://github.com/zyddnys/manga-image-translator)

![](https://img.shields.io/github/license/zyddnys/manga-image-translator)[![](https://img.shields.io/github/last-commit/scillidan/manga-image-translator/main)](https://github.com/scillidan/manga-image-translator)

````{tab} From source
```sh
git clone --depth=1 https://github.com/zyddnys/manga-image-translator
python -m venv venv
venv\Scripts\activate.bat
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```
````

If you need change api port, create `.env` liked:

```
SAKURA_API_BASE=http://127.0.0.1:5000
```

```sh
python -m manga_translator -v --mode web --use-gpu
```