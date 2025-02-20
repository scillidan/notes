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

### Samba

<!-- --8<-- [start:arch-linux] -->
```sh
sudo pacman -S samba
sudo pacman -Qi samba
sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak
sudo vim /etc/samba/smb.conf
```

```
[global]
    workgroup = WORKGROUP
    server string = Samba Server %v
    netbios name = archlinux
    security = user
    map to guest = bad user
    dns proxy = no

[Shared]
    path = /srv/samba/shared
    writable = yes
    guest ok = yes
    read only = no
    force user = nobody
```

```sh
sudo mkdir -p /srv/samba/shared
sudo chmod 0777 /srv/samba/shared
sudo systemctl start smb.service
sudo systemctl start nmb.service
sudo systemctl enable smb.service
sudo systemctl enable nmb.service
```

<!-- ```sh
sudo mkdir /home/sambauser/server
sudo chown -R sambauser /home/sambauser/server
sudo mount -t cifs //<ip>/sambashare /home/sambauser/server -o username=sambauser,password=YourPassword,workgroup=SAMBAGROUP
sudo systemctl daemon-reload
sudo mount
``` -->

↪ [How to Install and Configure SAMBA on Arch Linux](https://linuxways.net/arch/install-configure-samba-arch-linux/)  
↪ [Samba error code 22](https://forum.manjaro.org/t/samba-error-code-22/106741/1)
<!-- ↪ [How to Set Up a Samba Share on a Linux Server](https://chuck.is/samba/) -->

If `mount error: cifs filesystem not supported by the system`:

```sh
sudo reboot
sudo mount -t cifs //<ip>/sambashare /home/sambauser/server -o username=sambauser,password=YourPassword,workgroup=ARCHGROUP
```

↪ [Mounting a NAS using systemd - mount error: cifs filesystem not supported by the system](https://forum.manjaro.org/t/mounting-a-nas-using-systemd-mount-error-cifs-filesystem-not-supported-by-the-system/119153)

```sh
sudo vim /etc/ufw/applications.d/samba
```

```
[Samba]
title=LanManager-like file and printer server for Unix
description=The Samba software suite is a collection of programs that implements the SMB/CIF$
ports=137,138/udp|139,445/tcp
```

```sh
sudo ufw allow samba
sudo ufw status
```

Finally. If not work, try:

```sh
sudo systemctl status smb.service
sudo systemctl status nmb.service
sudo mkdir -p /usr/local/samba/var
sudo systemctl restart nmb.service
sudo systemctl status nmb.service
sudo systemctl restart smb.service
sudo systemctl status smb.service
sudo mount
sudo umount server/
sudo mount -t cifs //YourIP/sambashare /home/sambauser/server -o username=sambauser,password=YourPassword,workgroup=ARCHGROUP
sudo systemctl daemon-reload
sudo mount
```

↪ [missing_ufw_samba.md](https://gist.github.com/ammgws/1dbd8b3bb38b588c1bb8b3f70dd4fd2c)  
↪ [UFW firewall still blocking SMB despite adding rules](https://askubuntu.com/questions/36608/ufw-firewall-still-blocking-smb-despite-adding-rules)  
↪ [nemo SMB not working](https://www.linuxquestions.org/questions/linux-networking-3/nemo-smb-not-working-4175717802/)  
↪ [Cinnamon Nemo File Manager not open Network shares](https://forum.endeavouros.com/t/cinnamon-nemo-file-manager-not-open-network-shares/12404)
<!-- --8<-- [end:arch-linux] -->

<!-- --8<-- [start:windows10] -->
1. PC → 计算机管理 → 本地用户和组 → 用户 → 右键 → 新用户:
  ```
  用户名 `sambauser`
  用户不能更改密码 On 
  密码永不过期 On
  ```
2. 本地用户和组 → 组 → 右键 → 新建组 → 组名 `SAMBAGROUP` → 添加 → 输入对象名称来选择 `sambauser` → 确认 → 创建
3. 资源管理器 → 此电脑 → 右键 → 添加一个网络位置 → 指定网站的位置 → `\\<your_host>\sambashare` → 请键入该网络位置的名称 `sambashare`
4. 网络位置 → `sambashare` → 右键 → 映射网络驱动器 → 登录时重新连接 On → 完成
<!-- --8<-- [end:windows10] -->

