# [LunarVim](https://www.lunarvim.org/) [^1]

````{tab} Windows 10
Add to `cmder_mini\config\user_profile.cmd`:

```sh
set "XDG_CACHE_HOME=C:\Users\User\AppData\Local\Temp%XDG_CACHE_HOME%"
set "XDG_RUNTIME_DIR=C:\Users\User\AppData\Local\Temp%XDG_RUNTIME_DIR%"
set "LUNARVIM_BASE_DIR=C:\Users\User\AppData\Roaming\lunarvim\lvim%LUNARVIM_BASE_DIR%"
set "LUNARVIM_CACHE_DIR=C:\Users\User\AppData\Local\Temp\lvim%LUNARVIM_CACHE_DIR%"
set "LUNARVIM_CONFIG_DIR=C:\Users\User\AppData\Local\lvim%LUNARVIM_CONFIG_DIR%"
set "LUNARVIM_RUNTIME_DIR=C:\Users\User\AppData\Roaming\lunarvim%LUNARVIM_RUNTIME_DIR%"
```

```sh
lvim
```
````

[^1]: [Installation](https://www.lunarvim.org/docs/installation)
[^2]: [No C compiler found](https://github.com/LunarVim/Neovim-from-scratch/issues/274#issuecomment-1364584526)