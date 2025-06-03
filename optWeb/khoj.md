### [Khoj](https://github.com/khoj-ai/khoj) (Cache)

![](https://img.shields.io/github/license/khoj-ai/khoj?style=flat-square)

````{tab} ArchWSL
```sh
uv venv
.venv\Scripts\activate.bat
set CMAKE_ARGS="-DGGML_CUDA=on"
uv pip pip install "khoj[local]"
set USE_EMBEDDED_DB="true"
khoj --anonymous-modes
```
````

````{tab} Docker compose [^1]
```sh
mkdir khoj
cd khoj
wget https://raw.githubusercontent.com/khoj-ai/khoj/master/docker-compose.yml
sudo docker compose up -d
```
````

[^1]: [Khoj - Self-Host](https://docs.khoj.dev/get-started/setup/?server=docker&os=linux)