### [ArchWSL](https://github.com/yuk7/ArchWSL) [^1][^2]

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

Use repository mirror [^3]:

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

#### Install Opts

````{tab} pacman
```sh
sudo pacman -S <pkg>
```
````

````{tab} yay
```sh
sudo pacman -Syu yay
yay -S <pkg>
```
````

````{tab} paru
```sh
yay -S paru
paru <pkg>
```
````

For example:

````{tab} pacman
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
	presenterm \
	python-pipx \
	rust \
	rbenv \
	sdcv \
	starship \
	tere \
	tldr \
	texlab \
	tmux \
	tmuxinator \
	translate-shell \
	uv \
	wget \
	yq \
	zsh
	# go
```
````

````{tab} yay
```sh
yay -S --noconfirm \
act \
gvm \
lazydocker-bin \
paru \
ruby-build \
texlive-installer \
win32yank
```
````

```sh
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

#### D-Bus [^4]

```sh
# sudo pacman -S dbus
sudo mkdir /run/dbus -p
sudo dbus-daemon --system
```

#### systemd/systemctl [^4]

```sh
vim /etc/wsl.conf
```

```
[boot]
systemd=true
```

#### [WSLg](https://github.com/microsoft/wslg)

````{tab} Turn on [^5]
```sh
ln -s /mnt/wslg/runtime-dir/wayland-0* /run/user/1000/
```
````

````{tab} Turn off [^6]
On Windows:

```sh
subl ~/.wslconfig
```

```
[wsl2]
guiApplications=false
```
````

#### Reference cache

- [WSLg/WSL2 网络配置，终极解决方案 - 镜像网络](https://blog.gazer.win/essay/wsl2-mirrored-network.html)
- [WSL2 with GUI using Xvnc](https://gist.github.com/tdcosta100/385636cbae39fc8cd0937139e87b1c74)

[^1]: [Install Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/Install-Hyper-V?pivots=windows)
[^2]: [How to install Arch Linux for WSL](https://dev.to/jrcharney/how-to-install-arch-linux-for-wsl-184a)
[^3]: [Arch Linux 中文社区仓库](https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/)
[^4]: [Known issues](https://wsldl-pg.github.io/ArchW-docs/Known-issues/)
[^5]: [GUI Applications will no longer launch in Wayland after updating](https://github.com/microsoft/wslg/issues/1032)
[^6]: [Disable WSLg permanently](https://github.com/microsoft/wslg/discussions/523)