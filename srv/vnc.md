# VNC

````{tab} Arch [^1][^2][^3]
```sh
sudo pacman -S tigervnc
vncpasswd
sudo useradd -m vncuser
sudo passwd vncuser
sudo groupadd -r vncusers
sudo usermod -aG vncusers vncuser
sudo vim /etc/tigervnc/vncserver.users
```

```
:1=vncuser
```

For example, used [Xfce](https://www.xfce.org/) as desktop:

```sh
sudo pacman -S xfce4 xfce4-goodies
# rm -rf ~/.vnc
# mkdir ~/.vnc
vim ~/.vnc/config
```

```
session=xfce
geometry=1280x720
# localhost
alwaysshared
```

```sh
vncserver :1
# sudo systemctl enable --now vncserver@:1
```
````

````{tab} ArchWSL [^4]
```sh
vim ~/vncstart.sh
```

```bash
#!/bin/bash
vncserver -kill :1 > /dev/null 2>&1
rm -f /tmp/.X1-lock
rm -f /tmp/.X11-unix/X1
vncserver :1
```

```sh
chmod u+x ~/vncstart.sh
```

```sh
vncstart
```
````

````{tab} Ubuntu 22 ARM [^5] (Cache)
```sh
sudo apt install xfce4 xfce4-goodies
sudo apt install tightvncserver
vncserver
vncserver -kill :1
mv ~/.vnc/xstartup ~/.vnc/xstartup.bak
chmod +x ~/.vnc/xstartup
vim ~/.vnc/xstartup
```

```bash
#!/bin/bash
xrdb $HOME/.Xresources
startxfce4 &
```

```sh
vncserver
```

Create service:

```sh
sudo vim /etc/systemd/system/vncserver@.service
```

```
[Unit]
Description=Start TightVNC server at startup
After=syslog.target network.target

[Service]
Type=forking
User=<username>
Group=<username>
WorkingDirectory=/home/<username>

PIDFile=/home/<username>/.vnc/%H:%i.pid
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1280x860 -localhost :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl daemon-reload
sudo systemctl enable --now vncserver@1.service
sudo systemctl status vncserver@1
```
````

On client liked Windows 10, used [TightVNC](https://www.tightvnc.com/download.php):

```sh
tvnviewer <host>::5901 -password=<vncpasswd>
```

[^1]: [Setting up tigervncserver on arch linux (raspberry-pi)](https://rushichaudhari.github.io/posts/2020-10-29-setting-up-tigervncserver-on-arch-linux-raspberry-pi/)
[^2]: [TigerVNC Server in Manjaro (Arch Linux) - Headless Guide 2021!](https://www.youtube.com/watch?v=w1HS_xVnFFo)
[^3]: [How to Install & Configure VNC Server on Ubuntu 22.04](https://bytexd.com/how-to-install-configure-vnc-server-on-ubuntu/)
[^4]: [Using Graphical User Interface in WSL](https://hackmd.io/@heymosbrother/ryQS8PWa9)
[^5]: [How to Install and Configure VNC on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-22-04)