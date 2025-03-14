### [Neovim](https://neovim.io/)

#### Install

````{tab} Windows 10
- [Neovim configuration on Windows 10](https://jdhao.github.io/2018/11/15/neovim_configuration_windows/)
- [Nvim warning](https://github.com/LunarWatcher/auto-pairs#nvim-warning)
- [Why you switched from Neovim to Vim?](https://www.reddit.com/r/vim/comments/16cdbyd/why_you_switched_from_neovim_to_vim/)
````

````{tab} Ubuntu 22 ARM
```sh
sudo apt-get install ninja-build gettext cmake unzip curl
```

1. Get `Source code` from [Neovim - Releases](https://github.com/neovim/neovim/releases).
2. Decompress it to `neovim/`.

```sh
cd neovim
# rm -r build
make CMAKE_EXTRA_FLAGS="-DCMAKE_INSTALL_PREFIX=$HOME/neovim"
make install
ln -s ~/neovim/bin/nvim ~/.local/bin/
# rm -rf ~/.local/share/nvim/lazy/
nvim
```

- [PPA not working with lazy.nvim](https://www.reddit.com/r/neovim/comments/166fpfb/ppa_not_working_with_lazynvim/)
- [Neovim - Build prerequisites](https://github.com/neovim/neovim/blob/master/BUILD.md#build-prerequisites)
- [Install from source](https://github.com/neovim/neovim/blob/master/INSTALL.md#install-from-source)
- [Neovim: module 'lazy' not found](https://stackoverflow.com/questions/77510936/neovim-module-lazy-not-found/77825709)
````

````{tab} Ubuntu 24 ARM (Warning)
```sh
vim ~/.config/systemd/user/nvim_headless.service
```

```
[Unit]
Description=Start Neovim Headless Server

[Service]
ExecStart=nvim --headless --listen 0.0.0.0:1234
Restart=on-failure
User=<username>

[Install]
WantedBy=default.target
```

```sh
systemctl --user daemon-reload
systemctl --user enable --now nvim_headless
```

On PC:

```sh
C:\Users\User\Scoop\apps\git\current\usr\bin\ssh.exe <username>@<your_host> -L 1234:0.0.0.0:1234 -- /home/<your_host>/.local/bin/nvim --headless --listen 0.0.0.0:1234
neovide --server <your_host>:1234
```
````

#### Configure

- [How do I change my language in my init.lua? - neovim](https://vi.stackexchange.com/questions/36426/how-do-i-change-my-language-in-my-init-lua-neovim)
- [Install a Nerd Font](https://www.lunarvim.org/docs/installation/post-install#install-a-nerd-font)
- [Only just discovered 'set signcolumn=number', I like it](https://www.reddit.com/r/neovim/comments/neaeej/only_just_discovered_set_signcolumnnumber_i_like/)

#### Configure Neovide

- [Neovide - Configuration](https://neovide.dev/configuration.html)
- [Run Neovide on remote SSH system](https://github.com/neovide/neovide/discussions/2853)

#### Configure LSP

- [Configuring Language Server Protocol (LSP) in Neovim](https://linovox.com/configuring-language-server-protocol-lsp-in-neovim/)

#### Configure cmp

- [How to Install and Use nvim cmp Autocompletion](https://linovox.com/install-and-use-nvim-cmp/)
- [Autocomplete with nvim-cmp](https://www.jonashietala.se/blog/2024/05/26/autocomplete_with_nvim-cmp/)

#### [Resource](https://scillidan-database.vercel.app/resource/neovim)

##### [lazy.nvim](https://github.com/folke/lazy.nvim)

````{tab} Windows 10
```sh
git clone https://github.com/folke/lazy.nvim C:\Users\User\AppData\Local\nvim-data\lazy\lazy.nvim
```
````

##### [packer.nvim](https://github.com/wbthomason/packer.nvim) (Cache)

- [How to Install and Use Packer in Neovim/Nvim](https://linovox.com/install-and-use-packer-in-neovim/)

##### [mason.nvim](https://github.com/williamboman/mason.nvim)

```sh
:MasonUpdate
# :MasonInstall emmet-language-server
# :MasonInstall html-lsp
# :MasonInstall css-lsp
# :MasonInstall tailwindcss-language-server
# :MasonInstall nextls
# :MasonInstall typescript-language-server
# :MasonInstall eslint-lsp
:MasonInstall ltex-ls
:MasonInstall harper-ls
:MasonInstall python-lsp-server
:MasonInstall lua-language-server
:MasonInstall luacheck
:MasonInstall luaformatter
```

##### [nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter)

```sh
:TSInstall html
```

##### [nvim-devdocs](https://github.com/luckasRanarison/nvim-devdocs)

````{tab} Windows 10
```sh
mkdir C:\Users\User\AppData\Local\nvim-data\devdocs
```
````

```sh
:DevdocFetch
:DevdocInstall html
:DevdocInstall css
:DevdocInstall javascript
:DevdocInstall http
# :DevdocInstall tailwindcss
# :DevdocInstall nextjs
# :DevdocInstall typescript
# :DevdocInstall eslint
# :DevdocInstall electron
# :DevdocInstall react-18
:DevdocInstall bash
:DevdocInstall latex
```

##### [rime-ls](https://github.com/wlh320/rime-ls)

```sh
git clone --depth=1 https://github.com/wlh320/rime-ls
cd rime-ls
git fetch --tags
git checkout v0.4.1
```

````{tab} Windows 10
```sh
cargo build --release
```
````

````{tab} Ubuntu 24 [^1] (Cache)
```sh
sudo apt install build-essential librime-dev rustup
rustup default stable
rustup target add aarch64-unknown-linux-gnu
cargo build --target aarch64-unknown-linux-gnu --release
```
````

````{tab} Ubuntu 24 ARM (Cache)
```sh
sudo apt install build-essential libclang-dev librime-dev rustup
rustup default stable
rustup target add aarch64-unknown-linux-gnu
cargo build --target aarch64-unknown-linux-gnu --release
```
````

````{tab} Termux (Cache)
On Windows 10:

```sh
subl cargo.toml
```

```toml
[dependencies]
librime-sys = { git = "https://github.com/lotem/librime-sys" }
```

```sh
cargo install cargo-ndk
rustup target add aarch64-linux-android
# rustup target add armv7-linux-androideabi x86_64-linux-android i686-linux-android
cargo ndk -t aarch64-linux-android build --release
```
````

```sh
ln ~/.cargo/tmp/release/rime_ls ~/.local/bin/rime_ls
```

##### [cmp-lsp-rimels](https://github.com/liubianshi/cmp-lsp-rimels)

- [莫名奇妙的参数类型错误](https://github.com/liubianshi/cmp-lsp-rimels/issues/1)

##### Latex

````{tab} Arch
```sh
sudo pacman -S texlab zathura
```
````

- [opt/latex](opt/latex.html)
- [Neovim as a LaTex Development Environment](https://blog.epheme.re/software/nvim-latex.html)
- [使用 Neovim 和 vimtex 高效撰写 LaTeX 学术论文](https://sspai.com/post/64080)
- [opt/texlive](/opt/texlive.html)

##### [telescope.nvim](https://github.com/nvim-telescope/telescope.nvim)

- [How to change telescope theme](https://github.com/LazyVim/LazyVim/discussions/1127)

#### Troubleshoot

````{tab} Windows 10
- [nvim-treesitter doesn't seem to work in windows.](https://github.com/nvim-treesitter/nvim-treesitter/issues/2135)
````

[^1]: [install JDK and Android SDK on Linux Ubuntu](https://gist.github.com/EmadAdly/dfd18bf1ed7380fb9754ef798d23ec3b)