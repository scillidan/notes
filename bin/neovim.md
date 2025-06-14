# [Neovim](https://neovim.io/)

## Install

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

## Configure

- [How do I change my language in my init.lua? - neovim](https://vi.stackexchange.com/questions/36426/how-do-i-change-my-language-in-my-init-lua-neovim)
- [Install a Nerd Font](https://www.lunarvim.org/docs/installation/post-install#install-a-nerd-font)
- [Only just discovered 'set signcolumn=number', I like it](https://www.reddit.com/r/neovim/comments/neaeej/only_just_discovered_set_signcolumnnumber_i_like/)

## Configure Neovide

- [Neovide - Configuration](https://neovide.dev/configuration.html)
- [Run Neovide on remote SSH system](https://github.com/neovide/neovide/discussions/2853)

## Configure LSP

- [Configuring Language Server Protocol (LSP) in Neovim](https://linovox.com/configuring-language-server-protocol-lsp-in-neovim/)

## Configure cmp

- [How to Install and Use nvim cmp Autocompletion](https://linovox.com/install-and-use-nvim-cmp/)
- [Autocomplete with nvim-cmp](https://www.jonashietala.se/blog/2024/05/26/autocomplete_with_nvim-cmp/)

## Reference

- [Copy all the lines to clipboard](https://ctan.org/tex-archive/macros/latex/contrib/gitinfo2)
- [优化neovim启动速度](https://www.bilibili.com/video/BV1ohWqeSETr)
- [neovim的LSP配置这一块](https://www.bilibili.com/video/BV1iG7rzTEaz)

## Resource

```{include} bin/neovim/lazy.nvim.md
```
```{include} bin/neovim/packer.nvim.md
```
```{include} bin/neovim/nvim-treesitter.md
```
```{include} bin/neovim/mason.nvim.md
```
```{include} bin/neovim/blink.cmp.md
```
```{include} bin/neovim/cmp-lsp-rimels.md
```
```{include} bin/neovim/telescope.nvim.md
```
```{include} bin/neovim/nvim-dap.md
```
```{include} bin/neovim/nvim-devdocs.md
```
```{include} bin/neovim/latex.md
```

## Troubleshoot

````{tab} Windows 10
- [nvim-treesitter doesn't seem to work in windows.](https://github.com/nvim-treesitter/nvim-treesitter/issues/2135)
````

[^1]: [install JDK and Android SDK on Linux Ubuntu](https://gist.github.com/EmadAdly/dfd18bf1ed7380fb9754ef798d23ec3b)