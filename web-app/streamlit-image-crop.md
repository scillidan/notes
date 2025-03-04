### [Streamlit Image Crop](https://github.com/mitsuse/streamlit-image-crop)

![](https://img.shields.io/github/license/mitsuse/streamlit-image-crop?label=&style=flat-square)

````{tab} From source
```sh
git clone --depth=1 https://github.com/mitsuse/streamlit-image-crop
cd streamlit-image-crop
uv python install 3.8.20
uv venv --python 3.8.20
.venv\Scripts\activate.bat
uv pip install poetry
poetry install
```

```sh
cd streamlit_image_crop/frontend
nvm install 16.20.0
nvm use 16.20.0
npm install
npm run build
serve -s build -l 4321
```

Open a new terminal window [^1]:

```sh
uv pip install -U click==8
streamlit run example.py
````

[^1]: [click.get_os_args is deprecated on module 'click 8.1.0'](https://github.com/streamlit/streamlit/issues/4555)