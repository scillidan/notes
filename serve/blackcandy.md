### [Black Candy](https://github.com/blackcandy-org/blackcandy)

````{tab} Docker compose [^1]
```sh
mkdir blackcandy
cd blackcandy
vim docker-compose.yml
```

```yaml
version: '3.8'

services:
  blackcandy:
    image: ghcr.io/blackcandy-org/blackcandy:latest
    ports:
      - "3000:3000"
    volumes:
      - <music_dir>:/media_data
    environment:
      MEDIA_PATH: /media_data
    deploy:
      restart_policy:
        condition: any
```
````

1. Visit `http://<your_host>:3000`
2. User → Settings → Library → Sync

[^1]: [Media Files Mounts](https://github.com/blackcandy-org/blackcandy#media-files-mounts)