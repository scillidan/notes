### [dir2opds](https://github.com/dubyte/dir2opds)

#### Selfhost

````{tab} Ubuntu 22 ARM
```sh
mkdir dir2opds
cd dir2opds
wget https://github.com/dubyte/dir2opds/releases/download/v1.2.0/dir2opds_1.2.0_linux_arm64.tar.gz
tar xvf dir2opds_1.2.0_linux_arm64.tar.gz
sudo vim /etc/systemd/system/dir2opds.service
```

```
[Unit]
Description=dir2opds
Documentation=https://github.com/dubyte/dir2opds
After=network-online.target

[Service]
User=root
Group=root
Restart=on-failure
ExecStart=/home/<username>/dir2opds/dir2opds -dir /mnt/nvme/audioebook -port 8080

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl enable --now dir2opds.service
```
````