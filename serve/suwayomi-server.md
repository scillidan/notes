### [Suwayomi-Server](https://github.com/Suwayomi/Suwayomi-Server)

````{tab} Ubuntu 22 ARM
Get `Suwayomi-Server-v*-debian-all.deb` from [Suwayomi-Server - Releases](https://github.com/Suwayomi/Suwayomi-Server/releases).

```sh
sudo dpkg -i Suwayomi-Server-v*-debian-all.deb
sudo apt --fix-broken install
sudo vim /etc/systemd/system/suwayomi-server.service
```

```
[Unit]
Description=Suwayomi Server
After=network.target

[Service]
User=root
Group=root
ExecStart=suwayomi-server
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl enable --now suwayomi-server
sudo systemctl status suwayomi-server
```
````

#### Setting

1. Visit `http://<your_host>:4567`.
2. The service may take several minutes to start until you can see it.
3. Suwayomi → Settings → Brower settings → Extension repositories → Add repository:

```
https://raw.githubusercontent.com/ThePBone/tachiyomi-extensions-revived/repo/index.min.json
```

[^1]: [can you make it easier to install on ubuntu , and tutorial need to update](https://github.com/Suwayomi/Suwayomi-Server/issues/896)
[^2]: [Tachiyomi Extensions Revived](https://github.com/timschneeb/tachiyomi-extensions-revived)