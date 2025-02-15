### [Neovide](https://neovide.dev)

↪ [Installation](https://neovide.dev/installation.html).

`init.lua` part:

```lua
local alpha = function()
  return string.format("%x", math.floor(255 * vim.g.transparency or 0.75))
end

if vim.g.neovide then
    vim.g.neovide_padding_top = 0
    vim.g.neovide_padding_bottom = 0
    vim.g.neovide_padding_right = 0
    vim.g.neovide_padding_left = 0
    vim.g.neovide_transparency = 0.75
    vim.g.transparency = 0.75
    vim.g.neovide_background_color = "#0f1117" .. alpha()
    vim.g.neovide_floating_blur_amount_x = 1.0
    vim.g.neovide_floating_blur_amount_y = 1.0
    vim.g.neovide_cursor_animation_length = 0
    vim.g.neovide_cursor_trail_size = 0
    vim.g.neovide_remember_window_size = true
    vim.g.neovide_hide_mouse_when_typing = true
end
```

Create `nv.cmd`:

```sh
neovide.exe --size=1250x720 --frame none --no-tabs --neovim-bin nvim.exe -- -u "init.lua" %*
```

Create `lv.cmd`:

```sh
neovide.exe --neovim-bin nvim.exe --geometry 100x30 --notabs --frame none -- -u "%LUNARVIM_BASE_DIR%\init.lua" %*
```

#### `init.lua`

`init.lua`:

```lua
vim.api.nvim_command("language en_US.UTF-8")
vim.o.guifont = "MonaspiceAr NFP + Sarasa Gothic SC + WFM Sans SC:h9"
vim.o.number = true
vim.o.relativenumber = true
vim.o.tabstop = 2
vim.o.shiftwidth = 2
vim.o.timeout = true
vim.o.timeoutlen = 300
vim.o.signcolumn = "yes:1"
vim.o.cmdheight = 1
vim.g.mapleader = " "
```

↪ [How do I change my language in my init.lua? - neovim](https://vi.stackexchange.com/questions/36426/how-do-i-change-my-language-in-my-init-lua-neovim)  
↪ [Install a Nerd Font](https://www.lunarvim.org/docs/installation/post-install#install-a-nerd-font)  
↪ [Only just discovered 'set signcolumn=number', I like it](https://www.reddit.com/r/neovim/comments/neaeej/only_just_discovered_set_signcolumnnumber_i_like/)

#### LSP

↪ [Configuring Language Server Protocol (LSP) in Neovim](https://linovox.com/configuring-language-server-protocol-lsp-in-neovim/)

#### cmp

↪ [How to Install and Use nvim cmp Autocompletion](https://linovox.com/install-and-use-nvim-cmp/)
<!-- ↪ [Autocomplete with nvim-cmp](https://www.jonashietala.se/blog/2024/05/26/autocomplete_with_nvim-cmp/) -->