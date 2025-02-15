↪ [WSLg/WSL2 网络配置，终极解决方案 - 镜像网络](https://blog.gazer.win/essay/wsl2-mirrored-network.html)

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

↪ [Arch Linux 中文社区仓库](https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/)

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

↪ [How to install Arch Linux for WSL](https://dev.to/jrcharney/how-to-install-arch-linux-for-wsl-184a)

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
# zerotier-one
```

```sh
gh auth login
```

↪ [Github CLI](https://cli.github.com/)

<!-- 

```sh
sudo pacman -S go
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
# go env -w GOPROXY=
go env
```

↪ [Goproxy.cn](https://goproxy.cn/)

```sh
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg
sudo pacman -U yay-bin*.pkg.tar.xz
yay
``` -->

```sh
sudo pacman -Syu yay
yay -S --noconfirm \
act \
lazydocker-bin \
paru \
texlive-installer \
win32yank
```

↪ [How to Install and Use Yay on Arch Linux](https://www.makeuseof.com/install-and-use-yay-arch-linux/)

```sh
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
tmux
tmux source ~/.tmux.conf
```

↪ [Tmux Config: A Guide](https://builtin.com/articles/tmux-config)

```sh
uv python list
uv python install cpython-3.10.16-linux--x86_64-gnu
uv python pin cpython-3.10.16-linux-x86_64-gnu
cd ~
uv venv .venv
```

```sh
uv pip install pip_search pipx
cargo install autocast grex pipe-rename tidy-viewer trashy
pnpm add -g clean-css html-minifier js-beautify prettier svgo terser
pnpm add -g degit echo-cli npms-cli markserv open-cli png-to-ico serve
```

```sh
nvm install --lts
nvm use --lts
```

```sh
sudo /opt/texlive-installer/install-tl
sudo /usr/local/texlive/2024/bin/x86_64-linux/tlmgr option repository https://mirrors.cernet.edu.cn/CTAN/systems/texlive/tlnet
tlmgr update --list
sudo /usr/local/texlive/2024/bin/x86_64-linux/tlmgr update --all
```

↪ [TeX Live](https://wiki.archlinux.org/title/TeX_Live)  
↪ [tlmgr](https://tug.org/texlive/doc/tlmgr.html)

<!-- ```sh
hererocks lua53 -l5.3 -rlatest
source lua53/bin/activate
luarocks install luacheck
deactivate-lua
```

↪ [hererocks](https://github.com/mpeterv/hererocks) -->

<!-- ### [gvm](https://github.com/moovweb/gvm) 

```sh
yay -S gvm-git
gvm install 1.21.0
gvm use 1.21.0
```
-->

<!-- ### [goenv](https://github.com/go-nv/goenv)

```sh
git clone --depth=1 https://github.com/go-nv/goenv.git ~/.goenv
sudo vim ~/.zshrc
```

```
export GOENV_ROOT="$HOME/.goenv"
export PATH="$GOENV_ROOT/bin:$PATH"
eval "$(goenv init -)"
```

```sh
source ~/.zshrc
```

```sh
goenv install 1.22.0
```

Or:

```sh
wget https://go.dev/dl/go1.22.0.linux-arm64.tar.gz
mkdir -p ~/.goenv/cache
mv go1.22.0.linux-arm64.tar.gz ~/.goenv/cache/
goenv install 1.22.0
go version
```
-->

```sh
mkdir -p ~/.local/share/fonts
mv <font> ~/.local/share/fonts/
fc-cache -fv
```