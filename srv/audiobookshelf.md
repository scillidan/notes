# [audiobookshelf](https://github.com/advplyr/audiobookshelf)

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
    image: advplyr/audiobookshelf:latest
    container_name: audiobookshelf
    ports:
      - "13378:80"
    volumes:
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

## Reference

- [Directory Structure](https://www.audiobookshelf.org/docs/#book-directory-structure)

[^1]: [Docker Compose](https://www.audiobookshelf.org/docs/#docker-compose-install)