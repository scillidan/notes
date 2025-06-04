# [Zellij](https://github.com/zellij-org/zellij)

````{tab} Ubuntu 22 ARM
Get `zellij-aarch64-unknown-linux-musl.tar.gz` from [Zellij - Releases](https://github.com/zellij-org/zellij/releases).

```sh
tar -xvzf zellij-aarch64-unknown-linux-musl.tar.gz
mv zellij ~/.local/bin/
```
````

Get `zjframes.wasm`, `zjstatus.wasm` from [zjstatus & zjframes - Releases](https://github.com/dj95/zjstatus/releases).

```sh
mv zjframes.wasm ~/.config/zellij/plugins
mv zjstatus.wasm ~/.config/zellij/plugins
```

## Reference

- [Configuration](https://zellij.dev/documentation/configuration)
- [Configuration - Options](https://zellij.dev/documentation/options)
- [Configuration - Tokyo Night Light](https://zellij.dev/documentation/theme-gallery#tokyo-night-light)
- [Layouts](https://zellij.dev/documentation/layouts)
- [default.kdl](https://github.com/zellij-org/zellij/blob/main/zellij-utils/assets/config/default.kdl)
- [Does zellij support changing tab's name according to pane file system path automatically?](https://www.reddit.com/r/zellij/comments/10skez0/does_zellij_support_changing_tabs_name_according/)