### [Trilium](https://github.com/zadam/trilium) (Cache)

````{tab} Ubuntu 24 ARM
Get `trilium-linux-x64-server-*.tar.xz` from [Trilium - Releases](https://github.com/zadam/trilium/releases).

```sh
tar -xvf trilium-linux-x64-server-*.tar.xz
sudo mv trilium-linux-x64-server /opt/trilium
sudo vim /etc/systemd/system/trilium.service
```

```
[Unit]
Description=Trilium Daemon
After=syslog.target network.target

[Service]
User=root
Group=root
Type=simple
ExecStart=/opt/trilium/trilium.sh
WorkingDirectory=/opt/trilium/

TimeoutStopSec=20
Restart=always

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl enable --now trilium
```
````