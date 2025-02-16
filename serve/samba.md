### Samba [^1]

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

[^1]: [Installing and Configuring Samba on Ubuntu 22](https://reintech.io/blog/installing-configuring-samba-ubuntu-22)