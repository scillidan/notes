# [ttyd](https://github.com/tsl0922/ttyd) (Cache)

````{tab} Ubuntu 22 ARM [^1]
```sh
sudo apt-get update
sudo apt-get install -y build-essential cmake git libjson-c-dev libwebsockets-dev
git clone --depth=1 https://github.com/tsl0922/ttyd
cd ttyd && mkdir build && cd build
cmake ..
make
sudo make install
```

```sh
sudo vim /etc/systemd/system/ttyd.service
```

```
[Unit]
Description=ttyd service
After=network.target

[Service]
Type=simple
User=<username>
Group=<username>
ExecStart=/usr/local/bin/ttyd --cwd /home/<username> --writable zsh
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl enable --now ttyd
```
````

[^1]: [ttyd - Basic Usage](https://github.com/tsl0922/ttyd/wiki/Example-Usage)