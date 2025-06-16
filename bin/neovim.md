# [Neovim](https://neovim.io/)

````{tab} Ubuntu 22 ARM [^1][^2][^3]
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
````

## Usage

### nvim_headless.service (Cancel)

P.S. I suspect it once broke my RPI-5 system. I don't know how to fix it and have to reinstall the system.

On Ubuntu 24 ARM:

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

On Windows10:

```sh
C:\Users\User\Scoop\apps\git\current\usr\bin\ssh.exe <username>@<your_host> -L 1234:0.0.0.0:1234 -- /home/<your_host>/.local/bin/nvim --headless --listen 0.0.0.0:1234
neovide --server <your_host>:1234
```

## Reference

- [How do I change my language in my init.lua? - neovim](https://vi.stackexchange.com/questions/36426/how-do-i-change-my-language-in-my-init-lua-neovim)
- [Install a Nerd Font](https://www.lunarvim.org/docs/installation/post-install#install-a-nerd-font)
- [Only just discovered 'set signcolumn=number', I like it](https://www.reddit.com/r/neovim/comments/neaeej/only_just_discovered_set_signcolumnnumber_i_like/)
- [Copy all the lines to clipboard](https://ctan.org/tex-archive/macros/latex/contrib/gitinfo2)
- [优化neovim启动速度](https://www.bilibili.com/video/BV1ohWqeSETr)
- (Windows 10) [Neovim configuration on Windows 10](https://jdhao.github.io/2018/11/15/neovim_configuration_windows/)

### Configure LSP

- [Configuring Language Server Protocol (LSP) in Neovim](https://linovox.com/configuring-language-server-protocol-lsp-in-neovim/) (Cache)
- [neovim的LSP配置这一块](https://www.bilibili.com/video/BV1iG7rzTEaz)

### Configure CMP

- [How to Install and Use nvim cmp Autocompletion](https://linovox.com/install-and-use-nvim-cmp/) (Cache)
- [Autocomplete with nvim-cmp](https://www.jonashietala.se/blog/2024/05/26/autocomplete_with_nvim-cmp/) (Cache)

### As LaTex Editor

```{include} neovim/latex.md
```

## Resource

```{include} neovide.md
```
```{include} neovim/lazy.nvim.md
```
```{include} neovim/packer.nvim.md
```
```{include} neovim/nvim-treesitter.md
```
```{include} neovim/mason.nvim.md
```
```{include} neovim/blink.cmp.md
```
```{include} neovim/cmp-lsp-rimels.md
```
```{include} neovim/telescope.nvim.md
```
```{include} neovim/nvim-dap.md
```
```{include} neovim/nvim-devdocs.md
```

[^1]: [PPA not working with lazy.nvim](https://www.reddit.com/r/neovim/comments/166fpfb/ppa_not_working_with_lazynvim/)
[^2]: [Neovim - Build prerequisites](https://github.com/neovim/neovim/blob/master/BUILD.md#build-prerequisites)
[^3]: [Install from source](https://github.com/neovim/neovim/blob/master/INSTALL.md#install-from-source)