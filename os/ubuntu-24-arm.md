### Ubuntu 24 ARM

```sh
sudo apt update && sudo apt upgrade -y
sudo apt-get clean && sudo apt-get autoremove
# timedatectl set-timezone Asia/Shanghai
sudo cp /etc/apt/sources.list.d/ubuntu.sources /etc/apt/sources.list.d/ubuntu.sources.bak
sudo vim /etc/apt/sources.list.d/ubuntu.sources
```

```
Types: deb
URIs: https://mirrors.ustc.edu.cn/ubuntu-ports
Suites: noble noble-updates noble-backports
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

Types: deb
URIs: https://mirrors.ustc.edu.cn/ubuntu-ports
Suites: noble-security
Components: main universe restricted multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```

```sh
sudo apt update
```

- [USTC Mirror Help - Ubuntu Ports](https://mirrors.ustc.edu.cn/help/ubuntu-ports.html)

#### Enable WiFi:

```sh
sudo apt install network-manager
nmcli d
sudo nmcli r wifi on
nmcli d wifi list
sudo nmcli d wifi connect <ssid> password <password>
```

- [Establish a Wireless Connection](https://ubuntu.com/core/docs/networkmanager/configure-wifi-connections)

#### Troubleshoot

- [How to fix "Failed to fetch <sources.list links> 404 Not Found [IP: <some_ip>]"](https://askubuntu.com/questions/1348375/how-to-fix-failed-to-fetch-sources-list-links-404-not-found-ip-some-ip)