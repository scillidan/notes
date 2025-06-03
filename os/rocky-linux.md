### [Rocky Linux](https://rockylinux.org)

#### PM2 [^1][^2] (Cache)

Take [Excalith Start Page](https://github.com/excalith/excalith-start-page) as an example:

```sh
pm2 start npm --name "excalith-start-page" --watch -- start
```

Used `rsync` to update:

```sh
rsync -r "/cygdrive/c/your_path/excalith-start-page/" "root@your_host:/var/www/excalith-start-page" --include={'.*'} --exclude={'.github','.next/','build/','node_modules/','.git'}
```

Create a new VirtualHost configuration with subdomain names:

```sh
sudo vim /etc/httpd/conf.d/sub.domain.com.conf
```

```sh
<VirtualHost *:80>
  ServerName www.sub.domain.com
  ServerAlias sub.domain.com

  ErrorLog /var/log/httpd/sub.domain.com-error.log
  CustomLog /var/log/httpd/sub.domain.com-access.log combined
  ProxyPreserveHost On
  ProxyPass / http://localhost:3000/
  ProxyPassReverse / http://localhost:3000/
</VirtualHost>
```

#### VNC [^3][^4] (Cache)

```sh
sudo dnf update -y
sudo dnf install -y epel-release
sudo dnf groupinstall -y "Xfce" "base-x"
sudo systemctl set-default graphical
sudo reboot
```

```sh
sudo dnf install tigervnc-server
sudo adduser vncuser
sudo passwd vncuser
sudo su - vncuser
```

```sh
sudo dnf install firewalld -y
sudo systemctl enable firewalld
sudo systemctl start firewalld
sudo firewall-cmd --state
firewall-cmd --zone=public --permanent --add-service=vnc-server
firewall-cmd --reload
```

```sh
su vncuser
vim ~/.vnc/config
```

```
session=xfce
geometry=1280x800
# localhost
# alwaysshared
```

```sh
sudo systemctl start firewalld
```

If you need to kill the process:

```sh
pf -fu vncuser
kill -9 vncuser
```

On PC [^5]:

```sh
scoop install tightvnc
tvnviewer <your_host>::5901 -password=<vncuser_password>
```

#### Cross-reference

- [excalith-start-page](https://scillidan.github.io/notes/optweb/excalith-start-page.html)

[^1]: [How to specify a port number for pm2](https://stackoverflow.com/questions/31502351/how-to-specify-a-port-number-for-pm2)
[^2]: [How to change the port in nextjs?](https://medium.com/frontendweb/how-to-change-port-in-nextjs-1b99930bb81f)
[^3]: [Install and Configure VNC Server on Rocky Linux 8](https://techviewleo.com/install-and-configure-vnc-server-on-rocky-linux)
[^4]: [How To Set Up a Firewall Using firewalld on Rocky Linux 8](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-on-rocky-linux-8)
[^5]: [How to Install VNC Server on Rocky Linux](https://www.howtoforge.com/how-to-install-vnc-server-on-rocky-linux/)