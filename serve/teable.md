### [Teable](https://github.com/teableio/teable) (Cache)

#### Selfhost

````{tab} Docker compose [^1][^2]

```sh
mkdir teable
cd teable
vim docker-compose.yml
vim .env
```

Copy from [Install Teable - Incloude Redis (Recommend)](https://help.teable.io/deployment/docker-compose#docker-compose).

```sh
sudo docker-compose pull
sudo docker compose up -d
```
````

[^1]: [Install Teable - Docker Compose](https://help.teable.io/deployment/docker-compose#docker-compose)
[^2]: [CORS error after Dockerizing? How to fix?](https://www.reddit.com/r/docker/comments/yk0x2l/cors_error_after_dockerizing_how_to_fix/)
<!-- --8<-- [end:docker-arm] -->