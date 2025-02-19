### [Calibre-Web](https://github.com/janeczku/calibre-web) (Cache)

#### Selfhost

````{tab} From source

```sh
git clone --depth=1 https://github.com/janeczku/calibre-web
cd calibre-web
uv venv
.venv\Scripts\activate.bat
uv pip install calibreweb[metadata]
cps
```
````

1. Visit `localhost:8083`. If your want to shotdown the process, `Ctrl+C` and refresh the web-page.
2. Login with default Username `admin` and Password `admin123`.
  1. If you want to edit account: admin → Edit `Username`, `Email`, `Password`.
3. Calibre → Add books. You should get `Calibre Library\` now.
4. Calibre-Web → Admin → Edit Cabibre Database Configuration → Select folder contains the `metadata.db`.

````{tab} Docker compose [^1]
```sh
mkdir calibre-web
cd calibre-web
vim docker-compose.yml
```

Copy from [here](https://docs.linuxserver.io/images/docker-calibre-web/#docker-compose-recommended-click-here-for-more-info). And add volumes as books storage liked:

```sh
mkdir -p /mnt/nvme/share/calibre/library
vim docker-compose.yml
```

```yaml
    volumes:
      - ./data:/config
      - /mnt/nvme/share/calibre/library:/books
```

```sh
sudo docker compose up -d
```
````

[^1]: [linuxserver/calibre-web](https://docs.linuxserver.io/images/docker-calibre-web)