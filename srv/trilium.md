### [Trilium Notes](https://github.com/zadam/trilium) (Cache)

````{tab} Ubuntu 24 ARM [^1][^2]
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
export TRILIUM_DATA_DIR=/home/<user>/data/trilium
sudo systemctl enable --now trilium
```
````

[^1]: [Server installation](https://github.com/zadam/trilium/wiki/Server-installation)
[^2]: [Manual server installation](https://github.com/zadam/trilium/wiki/Manual-server-installation)