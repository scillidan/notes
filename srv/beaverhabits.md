# [beaverhabits](https://github.com/daya0576/beaverhabits) (Cache)

````{tab} Docker 22 ARM
```sh
mkdir beaverhabits
cd beaverhabits
vim docker-compose.yml
```

```yaml
version: '3.8'

services:
  beaverhabits:
    image: daya0576/beaverhabits:latest
    container_name: beaverhabits
    environment:
      - FIRST_DAY_OF_WEEK=0
      - HABITS_STORAGE=USER_DISK
      - MAX_USER_COUNT=1
    volumes:
      - ./beaverhabits:/app/.user/
    ports:
      - "8070:8080"
    restart: unless-stopped
```

```sh
sudo docker compose up -d
```
````

Beaver Habit Tracker → More → Add