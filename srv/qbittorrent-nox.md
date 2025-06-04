# qbittorrent-nox

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

## Cross-reference

- [flood.md](https://scillidan.github.io/notes/optWeb/flood.html)

[^1]: `Running qBittorrent without X server (WebUI only, systemd service set up, Ubuntu 15.04 or newer)` on [qBittorrent - Wiki](https://github.com/qbittorrent/qBittorrent/wiki)
[^2]: [How to Install qBittorrent-NoX, a headless and web UI Torrent Client](https://saputra.org/threads/how-to-install-qbittorrent-nox-a-headless-and-web-ui-torrent-client.1099/)