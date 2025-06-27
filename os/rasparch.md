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
sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay-git.git
cd yay-git
makepkg -si
yay --version
```

```sh
# sudo pacman -S --needed git base-devel
sudo pacman -S \
	asciinema \
	aspell \
	aspell-en \
	atuin \
	bat \
	chafa \
	chezmoi \
	cmus \
	cronie \
	curl \
	dictd \
	difftastic \
	eza \
	fastfetch \
	fd \
	ffmpegthumbnailer \
	fzf \
	git \
	github-cli \
	glow \
	gnupg \
	harper \
	lazygit \
	less \
	neovim \
	newsboat \
	nvm \
	imagemagick \
	openssh \
	pass \
	pnpm \
	presenterm \
	python-pipx \
	ripgrep \
	sdcv \
	starship \
	tailscale \
	tldr \
	tmux \
	translate-shell \
	uv \
	wget \
	xsel \
	yq \
	zoxide \
	zsh
	# ast-grep \
	# cargo \
	# docker \
	# docker-compose \
	# rbenv \
	# rust \
```

```sh
wget http://mirror.archlinuxarm.org/aarch64/core/libssh2-1.11.1-1-aarch64.pkg.tar.xz
mkdir libssh2
tar -xvf libssh2-1.11.1-1-x86_64.pkg.tar.zst -C libssh2
cd libssh2/usr/lib
sudo cp libssh2.so.1.0.1 /usr/lib
sudo pacman -Syyu
```

- [[SOLVED] pacman 7 - landlock is not supported by the kernel!](https://bbs.archlinux.org/viewtopic.php?id=299402)
- [Arch Linux ARM](https://mirrors.ustc.edu.cn/help/archlinuxarm.html)

## Troubleshoot

- [Pacman and NetworkManager are not working](https://forum.manjaro.org/t/pacman-and-networkmanager-are-not-working/174998/10)