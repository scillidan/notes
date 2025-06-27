# [RaspArch](https://raspex.exton.se/category/rasparch/)

```sh
sudo -s
passwd
```

```sh
sudo nano /etc/sudoers.d/wheel
```

```
%wheel ALL=(ALL) ALL
```

```sh
sudo useradd -m -G wheel -s /bin/bash <username>
sudo passwd <username>
su <username>
```

```sh
sudo nano /etc/pacman.conf
```

```
DisableSandbox
[archlinuxcn]
Server = https://repo.archlinuxcn.org/$arch
```

```sh
sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
sudo vim /etc/pacman.d/mirrorlist
```

```
# Add on top
Server = https://mirrors.ustc.edu.cn/archlinuxarm/$repo/os/$arch
```

## Setup

```sh
pacman -S tailscale
```

- [[SOLVED] pacman 7 - landlock is not supported by the kernel!](https://bbs.archlinux.org/viewtopic.php?id=299402)
- [Arch Linux ARM](https://mirrors.ustc.edu.cn/help/archlinuxarm.html)