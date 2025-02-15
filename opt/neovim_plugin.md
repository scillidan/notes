### [lazy.nvim](https://github.com/folke/lazy.nvim)

<!-- 
### [packer.nvim](https://github.com/wbthomason/packer.nvim)

↪ [How to Install and Use Packer in Neovim/Nvim](https://linovox.com/install-and-use-packer-in-neovim/)
-->

### [nvim-devdocs](https://github.com/luckasRanarison/nvim-devdocs)

```sh
:DevdocFetch
:DevdocInstall html
:DevdocInstall css
:DevdocInstall javascript
:DevdocInstall http
:DevdocInstall latex
:DevdocInstall bash
```

### [mason.nvim](https://github.com/williamboman/mason.nvim)

```sh
:MasonUpdate
:MasonInstall python-lsp-server
:MasonInstall lua-language-server
:MasonInstall luacheck
:MasonInstall luaformatter
:MasonInstall ltex-ls
:MasonInstall harper-ls
```

### [rime-ls](https://github.com/wlh320/rime-ls)

```sh
sudo pacman -S librime
git clone https://github.com/wlh320/rime-ls
cd rime-ls
git fetch --tags
git checkout v0.4.1
cargo build --release
ln ~/.cargo/tmp/release/rime_ls ~/.local/bin/rime_ls
```

<!-- ubuntu-24-arm 
```sh
sudo apt install librime-dev
rustup target add aarch64-unknown-linux-gnu
cargo build --target aarch64-unknown-linux-gnu --release
```
-->

### [cmp-lsp-rimels](https://github.com/liubianshi/cmp-lsp-rimels)

↪ [莫名奇妙的参数类型错误](https://github.com/liubianshi/cmp-lsp-rimels/issues/1)

### [telescope.nvim](https://github.com/nvim-telescope/telescope.nvim)

↪ [How to change telescope theme](https://github.com/LazyVim/LazyVim/discussions/1127)

### [nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter)

```sh
:TSInstall html
```

<!-- windows 
1. Install [MinGW GCC G++ Compiler](https://techdecodetutorials.com/download/)
2. Install [zig](https://ziglang.org/)

↪ [nvim-treesitter doesn't seem to work in windows.](https://github.com/nvim-treesitter/nvim-treesitter/issues/2135)
-->