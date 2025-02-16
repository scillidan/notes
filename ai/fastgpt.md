### [FastGPT](https://github.com/labring/FastGPT) (Cache)

````{tab} Docker compose [^1]
```sh
mkdir fastgpt
cd fastgpt
curl -O https://raw.githubusercontent.com/labring/FastGPT/main/projects/app/data/config.json
curl -o docker-compose.yml https://raw.githubusercontent.com/labring/FastGPT/main/files/docker/docker-compose-pgvector.yml
sudo docker compose up -d
```
````

[^1]: [Docker Compose 快速部署](https://doc.tryfastgpt.ai/docs/development/docker/)