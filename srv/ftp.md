# FTP (Cache)

````{tab} Ubuntu 22 ARM [^1]
```sh
sudo apt install vsftpd
# sudo adduser ftpuser
# sudo mkdir -p /home/ftpuser/ftp
# sudo chmod a-w /home/ftpuser/ftp
# sudo chown ftpuser:ftpuser /home/ftpuser/ftp
sudo vim /etc/vsftpd.conf
```

```
utf8_filesystem=YES
```

```sh
sudo systemctl enable --now vsftpd
```
````

[^1]: [Setting Up a Basic FTP Server on Ubuntu 22](https://reintech.io/blog/setting-up-basic-ftp-server-ubuntu-22)