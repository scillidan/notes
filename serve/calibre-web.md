### [Calibre-Web](https://github.com/janeczku/calibre-web)

#### Selfhost

````{tab} Ubuntu 22 ARM
```sh
uv venv calibre-web-venv
source calibre-web-venv/bin/activate
uv pip install calibreweb
```

Install optional features:

```sh
vim calibre-web-venv/requirements.txt
```

```sh
# For example
# metadata extraction
rarfile>=3.2,<5.0
scholarly>=1.2.0,<1.8
markdown2>=2.0.0,<2.5.0
html2text>=2020.1.16,<2024.2.26
python-dateutil>=2.1,<2.10.0
beautifulsoup4>=4.0.1,<4.13.0
faust-cchardet>=2.1.18,<2.1.20
py7zr>=0.15.0,<0.21.0
mutagen>=1.40.0,<1.50.0
pycountry>=20.0.0,<25.0.0
```

```sh
cps
```

As a service:

```sh
sudo vim /lib/systemd/system/calibre-web.service
```

```
[Unit]
Description=Calibre-Web
After=network.target

[Service]
User=root
Group=root
ExecStart=/home/scillidan/calibre-web-venv/bin/cps
WorkingDirectory=/home/scillidan/calibre-web-venv
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl enable --now calibre-web
```
````

1. Visit `http://<your_host>:8083`
2. Login with `admin`, `admin123`
3. Calibre → Add books. You should get `Calibre Library\` now.
4. Calibre-Web → Admin → Edit Cabibre Database Configuration → Select folder contains the `metadata.db`.

````{tab} Docker compose [^1] (Cache)
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