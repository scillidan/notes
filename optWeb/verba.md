# [Verba](https://github.com/weaviate/Verba) (Cache)

![](https://img.shields.io/github/license/weaviate/Verba?style=flat-square)

````{tab} Docker compose
```sh
git clone --depth=1 https://github.com/weaviate/Verba
cd Verba
vim .env
```

```
OLLAMA_URL=http://<ollama_host>:11434
OLLAMA_MODEL=llama3.1
OLLAMA_EMBED_MODEL=mxbai-embed-large
```

```sh
sudo docker compose --env-file .env up -d --build
```
````