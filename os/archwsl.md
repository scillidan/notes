# [ArchWSL](https://github.com/yuk7/ArchWSL) [^1][^2][^3]

```pwsh
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```

```sh
wsl --set-default-version 2
wsl --update --web-download
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

Use repository mirror [^4]:

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

## Install Opts

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
	ast-grep \
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
	fd \
	fzf \
	git \
	github-cli \
	harper \
	less \
	neovim \
	newsboat \
	nvm \
	openssh \
	pandoc-cli \
	pnpm \
	presenterm \
	python-pipx \
	rbenv \
	ripgrep \
	rust \
	sdcv \
	starship \
	tere \
	tldr \
	texlab \
	tmux \
	tmuxinator \
	translate-shell \
	tree-sitter \
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
pyenv global 3.10
hererocks lua51 -l5.1 -rlatest
source lua51/bin/activate
luarocks install luacheck
# curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain none -y
# rustup default nightly
```

```sh
pipx install deep-translator pip_search
pip install codespell isort
sudo /home/<username>/.pyenv/shims/pip install hererocks
cargo install autocast grex pipe-rename tidy-viewer trashy
pnpm add -g clean-css html-minifier js-beautify prettier svgo terser
pnpm add -g degit echo-cli npms-cli markserv open-cli png-to-ico serve
```

## Remove Windows 10's PATH [^5][^6]

```sh
sudo vim /etc/wsl.config
```

```
[interop]
appendWindowsPath = false
```

## Install fonts

```sh
mkdir -p ~/.local/share/fonts
mv <font> ~/.local/share/fonts/
fc-cache -fv
```

## D-Bus [^7]

```sh
# sudo pacman -S dbus
sudo mkdir /run/dbus -p
sudo dbus-daemon --system
```

## systemd/systemctl [^7]

```sh
vim /etc/wsl.conf
```

```
[boot]
systemd=true
```

## [WSLg](https://github.com/microsoft/wslg)

````{tab} Turn on [^8]
```sh
ln -s /mnt/wslg/runtime-dir/wayland-0* /run/user/1000/
```
````

````{tab} Turn off [^9]
On Windows:

Edit `~/.wslconfig`

```
[wsl2]
guiApplications=false
```
````

## Cross-reference

- [arch-linux.md](https://scillidan.github.io/notes/os/arch-linux.html)

[^1]: [Install Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/Install-Hyper-V?pivots=windows)
[^2]: [How to install Arch Linux for WSL](https://dev.to/jrcharney/how-to-install-arch-linux-for-wsl-184a)
[^3]: [WSL --update fails with unknown error code (0x80240066)](https://github.com/microsoft/WSL/issues/9039)
[^4]: [Arch Linux 中文社区仓库](https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/)
[^5]: [How to remove the Win10's PATH from WSL](https://stackoverflow.com/questions/51336147/how-to-remove-the-win10s-path-from-wsl)
[^6]: [[Question] How to remove Windows pathes from WSL PATH?](https://github.com/microsoft/WSL/issues/1493#issuecomment-266480323)
[^7]: [Known issues](https://wsldl-pg.github.io/ArchW-docs/Known-issues/)
[^8]: [GUI Applications will no longer launch in Wayland after updating](https://github.com/microsoft/wslg/issues/1032)
[^9]: [Disable WSLg permanently](https://github.com/microsoft/wslg/discussions/523)