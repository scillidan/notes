# [DeepLX](https://github.com/OwO-Network/DeepLX) (Cache)

````{tab} Windows 10
Download from releases:

1. Get `deeplx_windows_amd64.exe` from [DeepLX - Releases](https://github.com/OwO-Network/DeepLX/releases).
2. Run `deeplx_windows_amd64.exe`.

Or build from source [^1]:

```sh
git clone --depth=1 https://github.com/OwO-Network/DeepLX
cd DeepLX
go mod tidy
go build .
```
````

````{tab} Ubuntu 22 ARM
Get `deeplx_linux_arm64` from [DeepLX - Releases](https://github.com/OwO-Network/DeepLX/releases).

```sh
chmod +x deeplx_linux_arm64
mv deeplx_linux_arm64 /usr/bin/deeplx
sudo mkdir -p /opt/deeplx
sudo vim /etc/systemd/system/deeplx.service
```

```
[Unit]
Description=DeepLX Service
After=network.target

[Service]
User=root
Group=root
ExecStart=/usr/bin/deeplx
WorkingDirectory=/opt/deeplx
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl enable --now deeplx.service
```
````

[^1]: [请求添加对树莓派ARM的二进制程序](https://github.com/OwO-Network/DeepLX/issues/111)