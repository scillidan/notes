### [ArchWSL](https://github.com/yuk7/ArchWSL)

```pwsh
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```

```sh
wsl --set-default-version 2
wsl --update
scoop install archwsl
arch
```

```sh
passwd
echo "%wheel ALL=(ALL) ALL" > /etc/sudoers.d/wheel
useradd -m -G wheel -s /bin/bash <username>
passwd <username>
exit
```

```sh
arch config --default-user <username>
arch
```

```sh
sudo vim /etc/pacman.conf
```

```
[archlinuxcn]
Server = https://repo.archlinuxcn.org/$arch
```

```sh
sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
sudo vim /etc/pacman.d/mirrorlist
```

```
Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch
```

- [Arch Linux 中文社区仓库](https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/)

```sh
# sudo pacman -Sy archlinux-keyring
# sudo pacman-key --init
# sudo pacman-key --populate archlinux
sudo pacman -Sy archlinuxcn-keyring
sudo pacman-key --init
sudo pacman-key --populate
sudo pacman -Syyu
sudo pacman -S --needed base-devel
```

- [How to install Arch Linux for WSL](https://dev.to/jrcharney/how-to-install-arch-linux-for-wsl-184a)

#### Install [Yay](https://github.com/Jguer/yay)

````{tab} pacman
```sh
sudo pacman -Syu yay
```
````

````{tab} From source
```sh
gh auth login
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg
sudo pacman -U yay-bin*.pkg.tar.xz
yay
```
````

#### Install Opts

```sh
sudo pacman -S \
	asciinema \
	atuin \
	bat \
	cargo \
	chezmoi \
	cmus \
	cronie \
	curl \
	docker \
	docker-compose \
	eza \
	fzf \
	git \
	github-cli \
	harper \
	neovim \
	newsboat \
	nvm \
	openssh \
	pnpm \
	rust \
	rbenv \
	sdcv \
	starship \
	tere \
	tldr \
	tmux \
	tmuxinator \
	translate-shell \
	uv \
	wget \
	yq \
	zsh
	# go
```

```sh
yay -S --noconfirm \
act \
gvm \
lazydocker-bin \
paru \
texlive-installer \
win32yank
```

```sh
uv pip install pipx
pipx install deep-translator pip_search
cargo install autocast grex pipe-rename tidy-viewer trashy
pnpm add -g clean-css html-minifier js-beautify prettier svgo terser
pnpm add -g degit echo-cli npms-cli markserv open-cli png-to-ico serve
```

#### Install fonts

```sh
mkdir -p ~/.local/share/fonts
mv <font> ~/.local/share/fonts/
fc-cache -fv
```

#### Reference

- [WSLg/WSL2 网络配置，终极解决方案 - 镜像网络](https://blog.gazer.win/essay/wsl2-mirrored-network.html)