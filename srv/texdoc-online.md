# [TeXdoc online](https://gitlab.com/islandoftex/images/texdoc-online)

````{tab} Docker compose [^1]
```sh
git clone --depth=1 https://gitlab.com/islandoftex/images/texdoc-online
cd texdoc-online
cp docker-compose.yml docker-compose.yml.bak
vim docker-compose.yml
```

```yaml
version: '3.8'

services:
  texdoconline:
    container_name: texdoconline
    build: .
    ports:
      - "8010:80"
    restart: always
```

```sh
sudo docker compose up -d
```
````

[^1]: [Deploying your instance of TeXdoc online](https://gitlab.com/islandoftex/images/texdoc-online/-/wikis/Deploying-your-instance-of-TeXdoc-online)