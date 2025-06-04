# [immich](https://immich.app/)

````{tab} Docker compose [^1]
```sh
mkdir immich-app
cd immich-app
wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
sudo docker compose up -d
```
````

[^1]: [Docker Compose [Recommended]](https://immich.app/docs/install/docker-compose)