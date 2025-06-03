### [Sourcebot](https://github.com/sourcebot-dev/sourcebot)

#### Selfhost

````{tab} Docker compose [^1]
```sh
mkdir sourcebot
cd sourcebot
vim docker-compose.yml
```

```yaml
version: '3.8'

services:
  sourcebot:
    image: ghcr.io/sourcebot-dev/sourcebot:latest
    ports:
      - "3100:3100"
    restart: unless-stopped
```

```sh
sudo docker compose up -d
```
````

[^1]: [Getting Started](https://github.com/sourcebot-dev/sourcebot#getting-started)