# [Jackett](https://github.com/Jackett/Jackett)

````{tab} Ubuntu ARM [^1]
```sh
sudo apt install mono-devel
wget https://github.com/Jackett/Jackett/releases/download/<version>/Jackett.Binaries.LinuxARM64.tar.gz
tar -xvzf Jackett.Binaries.LinuxARM64.tar.gz
cd Jackett
./jackett
```

```sh
sudo ./install_service_systemd.sh
```

```sh
sudo systemctl status jackett.service
```
````

````{tab} Termux [^3]
```sh
proot-distro login archlinux
pacman -S mono
wget https://github.com/Jackett/Jackett/releases/download/<version>/Jackett.Binaries.Mono.tar.gz
tar -xvzf Jackett.Binaries.Mono.tar.gz
cd Jackett
mono --debug JackettConsole.exe
```
````

## Cross-reference

- [jsc.md](https://scillidan.github.io/notes/bin/jsc.html)

[^1]: [How to Install Jackett on Ubuntu 20.04](https://varhowto.com/install-jackett-ubuntu-20-04/)
[^2]: [Security Risk: Your instance has external access enabled without using an admin password.](https://github.com/Jackett/Jackett/wiki/Troubleshooting#security-risk-your-instance-has-external-access-enabled-without-using-an-admin-password)
[^3]: [[Package]: Jackett](https://github.com/termux/termux-packages/issues/9757)