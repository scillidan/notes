### [rbenv for Windows](https://github.com/RubyMetric/rbenv-for-windows)

```pwsh
$env:HOME = "C:\Users\User"
$env:RBENV_ROOT = "$env:HOME\Usr\Lib\rbenv"
iwr -useb "https://github.com/RubyMetric/rbenv-for-windows/raw/main/tool/install.ps1" | iex
$env:RBENV_USE_MIRROR = "CN"
& "$ENV:RBENV_ROOT\rbenv\bin\rbenv.ps1" init
```

1. Set variable `RBENV_ROOT=C:\Users\User\Usr\Lib\rbenv`.
2. Add `%RBENV_ROOT%\rbenv\bin`, `%RBENV_ROOT%\shims` into `PATH`.