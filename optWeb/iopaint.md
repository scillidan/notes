### [IOPaint](https://github.com/Sanster/IOPaint) (Bug)

![](https://img.shields.io/github/license/Sanster/IOPaint?style=flat-square)

````{tab} From source
```sh
git clone --depth=1 https://github.com/Sanster/IOPaint
cd IOPaint
cd web_app
# nvm use 22.14.0
npm install
npm run build
cp -r dist/ ../iopaint/web_app
npm run dev
```
````

```sh
cd ..
uv venv
.venv\Scripts\activate.bat
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
uv pip install -e .
iopaint start --model=lama --port=8080
# iopaint start --model=lama --device=cpu --port=8080
```

#### Optional

With [Interactive Segmentation](https://www.iopaint.com/plugins/interactive_seg):

```sh
iopaint start --model=lama --port=8080 --enable-interactive-seg --interactive-seg-device=cuda
```

With [GFPGAN](https://www.iopaint.com/plugins/GFPGAN):

```sh
uv pip install gfpgan
iopaint start --model=lama --port=8080 --enable-gfpgan --gfpgan-device cuda
```

With [RealESRGAN](https://www.iopaint.com/plugins/RealESRGAN):

```sh
uv pip install realesrgan
iopaint start --model=lama --port=8080 --enable-realesrgan --realesrgan-model RealESRGAN_x4plus --realesrgan-device cuda
```

With [Remove Background](https://www.iopaint.com/plugins/rembg):

```sh
uv pip install rembg
iopaint start --model=lama --port=8080 --enable-remove-bg
```

With [RestoreFormer](https://www.iopaint.com/plugins/RestoreFormer):

```sh
uv pip install realesrgan
iopaint start --model=lama --port=8080 --enable-restoreformer --restoreformer-device cuda
```

With [Anime Segmentation](https://www.iopaint.com/plugins/anime_seg):

```sh
iopaint start --model=lama --port=8080 --enable-anime-seg
```