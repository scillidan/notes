# [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)

````{tab} From source [^1]
```sh
git clone --depth=1 https://github.com/LibreTranslate/LibreTranslate
cd LibreTranslate
pipx install hatch
hatch run dev --debug
```
````
````{tab} Ubuntu 22 ARM [^2] (Cache)
```sh
uv venv .LibreTranslate
source .LibreTranslate/bin/activate
uv pip install libretranslate
```
````

````{tab} Docker compose [^3] (Cache)
```sh
git clone https://github.com/LibreTranslate/LibreTranslate
cd LibreTranslate
cp docker-compose.yml docker-compose.yml.bak
vim docker-compose.yml
```

```yamlservices:
version: '3.8'

services:
  libretranslate:
    container_name: libretranslate
    # image: libretranslate/libretranslate
    build:
      context: .
      dockerfile: ./docker/Dockerfile
    restart: unless-stopped
    ports:
      - "5000:5000"
    healthcheck:
      test: ['CMD-SHELL', './venv/bin/python scripts/healthcheck.py']
    environment:
      LT_HOST: 0.0.0.0
      LT_UPDATE_MODELS: 'true'
      LT_LOAD_ONLY: en,zh
    volumes:
    	- /mnt/nvme/share/argos-translate/packages:/home/libretranslate/.local:rw
```

```sh
sudo docker compose up -d
```
````

[^1]: [Contributing.md](https://github.com/LibreTranslate/LibreTranslate/blob/main/CONTRIBUTING.md)
[^2]: [Can I run it as a systemd (default pip/python installed one)?](https://github.com/LibreTranslate/LibreTranslate?tab=readme-ov-file#can-i-run-it-as-a-systemd-default-pippython-installed-one)
[^3]: [Where are the language models saved?](https://github.com/LibreTranslate/LibreTranslate?tab=readme-ov-file#where-are-the-language-models-saved)