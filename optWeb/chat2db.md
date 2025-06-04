# [Chat2DB](https://github.com/CodePhiliaX/Chat2DB)

![](https://img.shields.io/github/license/CodePhiliaX/Chat2DB?style=flat-square)

````{tab} Docker compose
```sh
mkdir Chat2DB
cd Chat2DB
vim docker-compose.yml
```

```yaml
version: '3.8'

services:
  chat2db:
    image: chat2db/chat2db:latest
    container_name: chat2db
    ports:
      - "10824:10824"
    volumes:
      - ~/.chat2db-docker:/root/.chat2db
    tty: true
```

```sh
sudo docker compose up -d
```
````

Visit `<your_host>:10824`, login with user `chat2db`, password `chat2db`.