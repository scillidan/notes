### qbittorrent-nox

````{tab} Ubuntu 22 ARM [^1][^2]
```sh
sudo apt install qbittorrent-nox
sudo vim /etc/systemd/system/qbittorrent-nox.service
```

```
[Unit]
Description=qBittorrent-nox service
After=network.target

[Service]
Type=exec
User=qbittorrent-nox
Group=qbittorrent-nox
UMask=007
ExecStart=/usr/bin/qbittorrent-nox --webui-port=8060
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl daemon-reload
sudo adduser --system --group qbittorrent-nox
sudo adduser <user> qbittorrent-nox
sudo systemctl enable --now qbittorrent-nox
```

Visit `http://<your_host>:8050`, login with:

```
User: admin
Password: adminadmin
```
````

[^1]: `Running qBittorrent without X server (WebUI only, systemd service set up, Ubuntu 15.04 or newer)` on [qBittorrent - Wiki](https://github.com/qbittorrent/qBittorrent/wiki)
[^2]: [How to Install qBittorrent-NoX, a headless and web UI Torrent Client](https://saputra.org/threads/how-to-install-qbittorrent-nox-a-headless-and-web-ui-torrent-client.1099/)

#### [Flood](https://github.com/jesec/flood)

````{tab} From source
```sh
git clone --depth=1 https://github.com/jesec/flood
cd flood
npm install
npm run build
# npm run start
vim package.json
```

```json
  "script": {
    "start": "node --enable-source-maps --use_strict dist/index.js --host 0.0.0.0 --port 4321",
```

```sh
pm2 start npm --name "flood" -- run start
```
````

Some tips:

1. Here are some important fields:
	```
	User for Flood: <user>
	Password for Flood: <password>
	URL: http://0.0.0.0:8050
	User for qBittorrent: admin
	Password for qBittorrent: adminadmin
	```
2. Default Download Directory is on `/home/qbittorrent-nox/Downloads`.
3. If you forget `<user>` or `<password>`, delete `~/.local/shared/flood/`. Reload or re-create flood's PM2 serve.