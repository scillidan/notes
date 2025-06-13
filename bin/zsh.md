# [Zsh](https://www.zsh.org/)

````{tab} Ubuntu 22 ARM
```sh
sudo apt install zsh
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
cd ~
wget https://gist.githubusercontent.com/scillidan/b49eabe3a90e7e7499b5155af7f36480/raw/1ad03938633a16651b311e4a6108ed40152110f8/.zshrc_mini -O .zshrc
source .zshrc
```
````

## Plugin

```{include} bin/zsh/minimal.md
```
```{include} bin/zsh/zenquotes.md
```
```{include} bin/zsh/zsh-abbr.md
```
```{include} bin/zsh/zsh-help.md
```
```{include} bin/zsh/zsh-nvm-auto-use.md
```
```{include} bin/zsh/zsh-nvm-pnpm-auto-switch.md
```
```{include} bin/zsh/zsh-proxy.md
```
```{include} bin/zsh/zsh-smart-files.md
```
```{include} bin/zsh/zsh-ssh.md
```