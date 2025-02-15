### Repository mirror

```sh
mkdir -p /etc/apt/sources.list.d
sudo cp /etc/apt/sources.list.d/ubuntu.sources /etc/apt/sources.list.d/ubuntu.sources.bak
sudo vim /etc/apt/sources.list.d/ubuntu.sources
```

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

### Disable WiFi

```sh
sudo ifconfig eth0 up
sudo ifconfig wlan0 down
```

But it don't work.

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

↪ [Configure a Static IP address for WIFI using Netplan in Ubuntu Server 22.04 on a HP Pavillion Desktop 510-p051a](https://stackoverflow.com/questions/77637274/configure-a-static-ip-address-for-wifi-using-netplan-in-ubuntu-server-22-04-on-a)  
↪ [No internet connection after ubuntu server 20.04 install, ifconfig not available](https://askubuntu.com/questions/1233934/no-internet-connection-after-ubuntu-server-20-04-install-ifconfig-not-available)

### Samba

```sh
sudo apt install samba
sudo systemctl status smbd
sudo mkdir -p /mnt/nvme/sambashare
sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak
sudo vim /etc/samba/smb.conf
```

```
workgroup = SAMBAGROUP
...
[sambashare1]
comment = Samba Share
path = /mnt/nvme/sambashare
read only = no
browsable = yes
writable = yes
guest ok = no
# path = /data/smb/share1
# create mask = 0700
# directory mask = 0700
```

↪ [Installing and Configuring Samba on Ubuntu 22](https://reintech.io/blog/installing-configuring-samba-ubuntu-22)

```sh
sudo groupadd -r sambausers
sudo useradd -m sambauser
sudo usermod -aG sambausers sambauser
sudo smbpasswd -a sambauser
sudo systemctl restart smbd
# sudo chown -R :sambausers /mnt/nvme/sambashare
# sudo chmod 1770 /mnt/nvme/sambashare
# sudo systemctl enable --now smb
# sudo systemctl enable --now nmb
# testparm
```

### chezmoi

1. Get `chezmoi_*_linux_arm64.deb` from [chezmoi - Releases](https://github.com/twpayne/chezmoi).
2. `sudo dpkg -i chezmoi_*_linux_arm64.deb`