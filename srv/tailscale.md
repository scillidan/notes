# [Tailscale](https://tailscale.com)

````{tab} Ubuntu 22 ARM
```sh
curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/noble.noarmor.gpg | sudo tee /usr/share/keyrings/tailscale-archive-keyring.gpg >/dev/null
curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/noble.tailscale-keyring.list | sudo tee /etc/apt/sources.list.d/tailscale.list
sudo apt-get update
sudo apt-get install tailscale
sudo tailscale up
```
````

````{tab} ArchWSL / RaspArch
```sh
sudo pacman -S tailscale
sudo systemctl enable --now tailscaled
```
````

```sh
sudo tailscale login
```