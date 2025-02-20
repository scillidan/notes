### [audiobookshelf](https://github.com/advplyr/audiobookshelf) (Cache)

````{tab} Docker compose
```sh
mkdir audiobookshelf
cd audiobookshelf
vim docker-compose.yml
```

```yaml
version: '3.8'

services:
  audiobookshelf:
    image: <docker_image_proxy>/advplyr/audiobookshelf:latest
    container_name: audiobookshelf
    ports:
      - "13378:80"
    volumes:
      - <audiobook_dir>:/mnt/nvme/audiobook
      - ./audiobooks:/audiobooks
      - ./podcasts:/podcasts
      - ./metadata:/metadata
      - ./config:/config
    restart: unless-stopped
```

```sh
sudo docker compose up -d
```
````

[^1]: [Docker Compose](https://www.audiobookshelf.org/docs/#docker-compose-install)