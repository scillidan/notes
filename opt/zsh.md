### [Zsh](https://www.zsh.org/)

````{tab} Ubuntu 22 ARM
```sh
sudo apt install zsh
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
cd ~
wget https://gist.githubusercontent.com/scillidan/b49eabe3a90e7e7499b5155af7f36480/raw/1ad03938633a16651b311e4a6108ed40152110f8/.zshrc_mini -O .zshrc
source .zshrc
```
````

#### Resource

##### [zsh-abbr](https://github.com/olets/zsh-abbr)

- [abbr c does not clear abbreviations created with the pattern abbr x=y](https://github.com/olets/zsh-abbr/issues/88)

##### [zsh-proxy](https://github.com/SukkaW/zsh-proxy)

```sh
init_proxy
config_proxy
proxy
# noproxy
```

##### [zsh-ssh](https://github.com/sunlei/zsh-ssh)

- [Using the SSH Config File](https://linuxize.com/post/using-the-ssh-config-file/)