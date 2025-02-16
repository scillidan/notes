### [docTR](https://github.com/mindee/doctr)

#### Selfhost

````{tab} Form source
```sh
git clone --depth=1 https://github.com/mindee/doctr
cd doctr
uv venv
.venv\Scripts\activate.bat
# cat demo/pt-requirements.txt
uv pip install git+https://github.com/mindee/doctr.git#egg=python-doctr[torch,viz]
uv pip install streamlit>=1.0.0
set USE_TORCH=1
streamlit run demo/app.py
```
````