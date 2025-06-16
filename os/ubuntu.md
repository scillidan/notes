# [Ubuntu](https://ubuntu.com/)

```sh
sudo apt update && sudo apt upgrade -y
# sudo apt-get clean && sudo apt-get autoremove
# timedatectl set-timezone Asia/Shanghai
# mkdir -p /etc/apt/sources.list.d
```

## Use repository mirror [^1]

```sh
sudo cp /etc/apt/sources.list.d/ubuntu.sources /etc/apt/sources.list.d/ubuntu.sources.bak
sudo vim /etc/apt/sources.list.d/ubuntu.sources
```

````{tab} Ubuntu 24
```
Types: deb
URIs: https://mirrors.ustc.edu.cn/ubuntu
Suites: noble noble-updates noble-backports
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

Types: deb
URIs: https://mirrors.ustc.edu.cn/ubuntu
Suites: noble-security
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```
````

````{tab} Ubuntu 24 ARM
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
````

````{tab} Ubuntu 22 ARM
```
Types: deb
URIs: https://mirrors.ustc.edu.cn/ubuntu-ports
Suites: jammy jammy-updates jammy-backports
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

Types: deb
URIs: https://mirrors.ustc.edu.cn/ubuntu-ports
Suites: jammy-security
Components: main universe restricted multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```
````

```sh
sudo apt update
```

## Ubuntu 24

```{include} ubuntu/flatpak.md
```

## Ubuntu 24 ARM (Cache)

### Enable WiFi [^2]

```sh
sudo apt install network-manager
nmcli d
sudo nmcli r wifi on
nmcli d wifi list
sudo nmcli d wifi connect <ssid> password <password>
```

### Troubleshoot

- [How to fix "Failed to fetch <sources.list links> 404 Not Found [IP: <some_ip>]"](https://askubuntu.com/questions/1348375/how-to-fix-failed-to-fetch-sources-list-links-404-not-found-ip-some-ip)

## Ubuntu 22 ARM

### Disable WiFi [^3][^4]

```sh
sudo ifconfig eth0 up
sudo ifconfig wlan0 down
```

But it seems don't work.

```sh
sudo rm /etc/netplan/50-cloud-init.yaml
sudo vim /etc/netplan/00-installer-config.yaml
```

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: true
      optional: true
  wifis:
    wlan0:
      dhcp4: true
      optional: false
      access-points:
        "<ssid>":
          password: "<password>"
          hidden: true
```

```sh
sudo chmod 600 /etc/netplan/00-installer-config.yaml
sudo netplan generate
sudo netplan --debug apply
sudo reboot
```

```sh
ip a
sudo ifconfig wlan0 down
```

### Install [Nerd Font](http://nerdfonts.com/) [^5] (Cache)

```sh
sudo vim /etc/fonts/conf.d/50-enable-fixed.conf
```

```
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <selectfont>
    <acceptfont>
      <pattern>
        <patelt name="<font_family>"><string>fixed</string></patelt>
      </pattern>
    </acceptfont>
  </selectfont>
</fontconfig>
```

```sh
sudo dpkg-reconfigure fontconfig
```

```sh
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/JetBrainsMono.tar.xz
tar -xJvf JetBrainsMono.tar.xz
rm README.md
rm OFL.txt
mv JetBrains** ~/.local/share/fonts
```

[^1]: [USTC Mirror Help - Ubuntu](https://mirrors.ustc.edu.cn/help/ubuntu.html)
[^2]: [Establish a Wireless Connection](https://ubuntu.com/core/docs/networkmanager/configure-wifi-connections)
[^3]: [Configure a Static IP address for WIFI using Netplan in Ubuntu Server 22.04 on a HP Pavillion Desktop 510-p051a](https://stackoverflow.com/questions/77637274/configure-a-static-ip-address-for-wifi-using-netplan-in-ubuntu-server-22-04-on-a)
[^4]: [No internet connection after ubuntu server 20.04 install, ifconfig not available](https://askubuntu.com/questions/1233934/no-internet-connection-after-ubuntu-server-20-04-install-ifconfig-not-available)
[^5]: [ubuntu wiki - Fonts](https://wiki.ubuntu.com/Fonts)