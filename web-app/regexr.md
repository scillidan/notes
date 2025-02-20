### [RegExr](https://github.com/gskinner/regexr)

```sh
mkdir regexr
cd regexr
vim docker-compose.yml
```

```yaml
version: '3.8'

services:
  regexr:
    image: gufertum/regexr
```

```sh
sudo docker compose up -d
```