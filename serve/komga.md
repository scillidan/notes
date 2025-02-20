### [Komga](https://github.com/gotson/komga)

````{tab} Ubuntu 22 ARM [^1][^2][^3]
```sh
sudo apt install openjdk-21-jdk postgresql postgresql-contrib -y
```

```sh
sudo su postgres
createuser komgauser --pwprompt
createdb -O komgauser komga
exit
```

```sh
sudo mkdir /opt/komga
```

```sh
sudo wget https://github.com/gotson/komga/releases/download/1.12.1/komga-1.12.1.jar -P /opt/komga/
```

```sh
sudo vim /etc/systemd/system/komga.service
```

```
[Unit]
Description=Komga Service
After=network.target

[Service]
User=root
Group=root
ExecStart=/usr/bin/java -Xms128M -Xmx256M -jar /opt/komga/komga-1.21.1.jar --server.servlet.context-path=/komga --server.port=8090
WorkingDirectory=/opt/komga
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl daemon-reload
sudo systemctl enable --now komga
```
````

````{tab} Windows 10
```batchfile
@echo off

java -jar "komga.jar" --komga.config-dir="config"

pause
```
````

[^1]: [How to Install Komga on Ubuntu Server Latest](https://ipv6.rs/tutorial/Ubuntu_Server_Latest/Komga/)
[^2]: [Komga - Breaking changes](https://komga.org/blog/prepare-v1/#breaking-changes)
[^3]: [Configuration options](https://komga.org/docs/installation/configuration)