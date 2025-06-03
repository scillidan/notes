### [changedetection.io](https://github.com/dgtlmoon/changedetection.io)

![](https://img.shields.io/github/license/dgtlmoon/changedetection.io)

````{tab} From source
```sh
git clone --depth=1 https://github.com/dgtlmoon/changedetection.io
cd changedetection.io
uv venv
.venv\Scripts\activate.bat
uv pip install -e .
python changedetection.py
```
````

````{tab} PM2
```sh
pm2 start changedetection.py --name changedetection --interpreter ".venv/Scripts/python.exe" --cwd "changedetection.io"
```
````