### Termux

```sh
pkg update
pkg upgrade
pkg install asciinema \
  atuin \
  bat \
  chezmoi \
  curl \
  eza \
  fzf \
  gh \
  git \
  libandroid-stub \
  neovim \
  newsboat \
  nodejs-lts \
  sdcv \
  starship \
  tere \
  tealdeer \
  tmux \
  translate-shell \
  uv \
  vim \
  wget \
  yq \
  zsh
```

```sh
python -m pip install pipx
pipx install deep-translator
```

```sh
tldr --update
```

#### About Username

- [Termux is single-user](https://wiki.termux.com/wiki/Differences_from_Linux#Termux_is_single-user)

#### Use [SSH](https://wiki.termux.com/wiki/Remote_Access#SSH)

```sh
pkg install openssh
passwd
sshd
```

On PC:

```sh
ssh -p 8022 <any_username>@<your_host>
```

#### [Termux-setup-storage](https://wiki.termux.com/wiki/Termux-setup-storage)

```sh
termux-setup-storage
```

#### Enable Linux file system [^1][^2]

```sh
pkg install proot
termux-chroot
ls /usr
```

#### Install [Nerd Font](https://www.nerdfonts.com/font-downloads) [^3]

```sh
wget https://raw.githubusercontent.com/scillidan/Nerd-Sarasa-Merge/main/MonaspiceArNFP-SarasaGothicSC-WFMSansSC.ttf -O ~/.termux/font.ttf
termux-reload-settings
```

#### Configure Keyboard [^4][^5]

```sh
cp .termux/termux.properties .termux/termux.properties.bak
vim .termux/termux.properties
```

```
extra-keys = [[ \
  {key: TAB, popup: KEYBOARD}, \
  {key: ESC, popup: '<'}, \
  {key: CTRL, popup: '['}, \
  {key: ALT, popup: '\{'}, \
  {key: 'BACKSLASH', popup: '|'}, \
  {key: '_', popup: '='}, \
  {key: UP, popup: PGUP}, \
  {key: DOWN, popup: PGDN}, \
  {key: LEFT, popup: HOME}, \
  {key: RIGHT, popup: END} \
]]
```

#### Input Method

- [copy and paste using Ctrl-C Ctrl-V or right click menu](https://github.com/termux/termux-app/issues/1891)
- [Text Input View](https://wiki.termux.com/wiki/Touch_Keyboard#Text_Input_View)

#### About Desktop Environment

- [Graphical Environment](https://wiki.termux.com/wiki/Graphical_Environment)  
- [Termux Desktop](https://github.com/adi1090x/termux-desktop)  
- [termux-desktop-xfce](https://github.com/Yisus7u7/termux-desktop-xfce)

#### LLM

```sh
pkg install ollama
ollama pull tinyllama
```

#### [PRoot Distro](https://github.com/termux/proot-distro)

```sh
proot-distro install debian
proot-distro list
proot-distro install archlinux
proot-distro login archlinux
```

```sh
pacman -Syyu
```

#### Troubleshoot

- [apt-get update fails to fetch files, “Temporary failure resolving …” error](https://askubuntu.com/questions/91543/apt-get-update-fails-to-fetch-files-temporary-failure-resolving-error)
- [cargo install: specify a /tmp substitute?](https://stackoverflow.com/questions/64572901/cargo-install-specify-a-tmp-substitute/64616981#64616981)
- [Can not install on android - target 'aarch64-linux-android' not found in channel.](https://github.com/rust-lang/rustup/issues/2872)

[^1]: [Termux is not FHS compliant](https://wiki.termux.com/wiki/Differences_from_Linux#Termux_is_not_FHS_compliant)
[^2]: [Access Termux from a file manager](https://wiki.termux.com/wiki/Internal_and_external_storage)
[^3]: [[Info] How to setup nerd font in order to work lsd properly in Termux(Android)](https://github.com/lsd-rs/lsd/issues/423)
[^4]: [Can I hide this keyboard? I have a physical one attached](https://www.reddit.com/r/termux/comments/qaenv5/can_i_hide_this_keyboard_i_have_a_physical_one/)
[^5]: [Disabling the up-arrow key rebinding?](https://github.com/atuinsh/atuin/issues/51#issuecomment-1641211422)
