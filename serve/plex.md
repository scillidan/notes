### [Plex](https://www.plex.tv/) (Cache)

````{tab} Ubuntu 22 ARM [^1]
```sh
echo deb https://downloads.plex.tv/repo/deb public main | sudo tee /etc/apt/sources.list.d/plexmediaserver.list
curl https://downloads.plex.tv/plex-keys/PlexSign.key | sudo apt-key add -
sudo apt update
sudo apt install plexmediaserver
sudo systemctl status plexmediaserver
```

Visit `http://<your_host>:32400/web`.

[^1]: [Install of plex on Ubuntu server 22.04](https://www.reddit.com/r/PleX/comments/yp13yb/install_of_plex_on_ubuntu_server_2204/)
````