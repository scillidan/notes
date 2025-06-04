# [Manga-Colorizer](https://github.com/BinitDOX/Manga-Colorizer) (Cache)

![](https://img.shields.io/github/license/BinitDOX/Manga-Colorizer?style=flat-square)

````{tab} Froms source
```sh
git clone --depth=1 https://github.com/BinitDOX/Manga-Colorizer
cd Manga-Colorizer/Backend
uv venv
.venv\Scripts\activate.bat
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
uv pip install -r Backend/requirements.txt
uv pip install einops
python app-stream.py
```
````