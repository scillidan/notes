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

#### On client

1. Windows 10 → 计算机管理 → 本地用户和组 → 用户 → 右键 → 新用户:
  ```
  用户名 `sambauser`
  用户不能更改密码 On 
  密码永不过期 On
  ```
2. 本地用户和组 → 组 → 右键 → 新建组 → 组名 `SAMBAGROUP` → 添加 → 输入对象名称来选择 `sambauser` → 确认 → 创建
3. 资源管理器 → 此电脑 → 右键 → 添加一个网络位置 → 指定网站的位置 → `\\<your_host>\sambashare` → 请键入该网络位置的名称 `sambashare`
4. 网络位置 → `sambashare` → 右键 → 映射网络驱动器 → 登录时重新连接 On → 完成

[^1]: [Installing and Configuring Samba on Ubuntu 22](https://reintech.io/blog/installing-configuring-samba-ubuntu-22)

