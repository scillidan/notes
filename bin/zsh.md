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

```{include} zsh/minimal.md
```
```{include} zsh/zenquotes.md
```
```{include} zsh/zsh-abbr.md
```
```{include} zsh/zsh-chezmoi.md
```
```{include} zsh/zsh-help.md
```
```{include} zsh/zsh-nvm-auto-use.md
```
```{include} zsh/zsh-nvm-pnpm-auto-switch.md
```
```{include} zsh/zsh-proxy.md
```
```{include} zsh/zsh-smart-files.md
```
```{include} zsh/zsh-ssh.md
```