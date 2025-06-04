# [Flatpak](https://flatpak.org/) [^1][^2]

```sh
sudo add-apt-repository ppa:flatpak/stable
sudo apt update
sudo apt install flatpak
sudo apt install gnome-software-plugin-flatpak
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
reboot
```

```sh
export GIO_MODULE_DIR=/usr/lib/x86_64-linux-gnu/gio/modules/
flatpak install flathub
```

[^1]: [Ubuntu Quick Setup](https://flatpak.org/setup/Ubuntu)
[^2]: [TLS support is not available](https://github.com/flatpak/flatpak/issues/1207)