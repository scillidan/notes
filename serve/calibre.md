### [Calibre](https://calibre-ebook.com/)

#### Selfhost

````{tab} Windows 10
1. Calibre → Preferences → Sharing → Sharing over ht net → The port on which to listen for connections `<port>`
2. Calibre → Connect → share → Start Content server

PS: I can't add books with `calibredb add <Book> --with-library <calibre_data>` when `calibre-server.exe --port <port> <calibre_data>` running.
````

````{tab} Docker compose [^1]
```sh
mkdir calibre
cd calibre
vim docker-compose.yml
```

Copy from [here](https://docs.linuxserver.io/images/docker-calibre/#docker-compose-recommended-click-here-for-more-info). And add volumes as books storage liked:

```sh
vim docker-compose.yml
```

```yaml
    volumes:
      - ./config:/config
      - /mnt/nvme/book:/book
      - /mnt/nvme/sambashare/audioebook:/audioebook
```

```sh
sudo docker compose up -d
```
````

1. Cabibre → Preferences → Sharing → Sharing over the net → Run server automatically when calibre starts (On) → Start server.
2. The opds serve is on `http://<your_host>:8081/opds`.

[^1]: [linuxserver/calibre](https://docs.linuxserver.io/images/docker-calibre)
[^2]: [How To Install Calibre Server & Calibre Web On Ubuntu 22.04](https://kenfavors.com/code/how-to-install-calibre-server-calibre-web-on-ubuntu-22-04/)