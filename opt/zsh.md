### [zsh-abbr](https://github.com/olets/zsh-abbr)

↪ [abbr c does not clear abbreviations created with the pattern abbr x=y](https://github.com/olets/zsh-abbr/issues/88)

### [zsh-proxy](https://github.com/SukkaW/zsh-proxy)

```sh
init_proxy
config_proxy
proxy
# noproxy
```

### [zsh-ssh](https://github.com/sunlei/zsh-ssh)

Read more on [Using the SSH Config File](https://linuxize.com/post/using-the-ssh-config-file/).

### [Translate Shell](https://github.com/soimort/translate-shell)

```sh
mkdir ~/.config/translate-shell
vim ~/.config/translate-shell/init.trans
```

```
{
	:translate-shell "0.9.0"
	:verbose         false
	:show-original   false
	:hl              "en"
	:tl              ["zh"]
	:engine          "bing"
}
```


### [nvm](https://github.com/nvm-sh/nvm)

```sh
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/refs/heads/master/install.sh | bash
vim .zshrc
```

```
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

```sh
source ~/.zshrc
nvm ls-remote
nvm install Gallium
nvm install Hydrogen
nvm use <version>
```

### [pyenv](https://github.com/pyenv/pyenv)

<!-- --8<-- [start:termux] -->
↪ [Build older python package - 3.9](https://github.com/termux/termux-packages/discussions/9498)
<!-- --8<-- [end:termux] -->

<!-- --8<-- [start:arch-linux] -->
```sh
sudo pacman -S pyenv
```
<!-- --8<-- [end:arch-linux] -->

<!-- --8<-- [start:ubuntu-22-arm] -->
```sh
sudo apt update
sudo apt-get install -y build-essential curl libbz2-dev libffi-dev liblzma-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libssl-dev libxml2-dev libxmlsec1-dev llvm make tk-dev wget xz-utils zlib1g-dev
```

↪ [ubuntu에서 pyenv 설치하기](https://jinmay.github.io/2019/03/16/linux/ubuntu-install-pyenv-1/)  
↪ [pyenv install: 3.x BUILD FAILED (Ubuntu 20.04 using python-build 20180424)](https://stackoverflow.com/questions/67807596/pyenv-install-3-x-build-failed-ubuntu-20-04-using-python-build-20180424)
<!-- --8<-- [end:ubuntu-22-arm] -->

<!-- --8<-- [start:ubuntu-24-arm] -->
```sh
sudo apt install -y build-essential libssl-dev libbz2-dev libreadline-dev libsqlite3-dev libffi-dev zlib1g-dev liblzma-dev tk-dev
```
<!-- --8<-- [end:ubuntu-24-arm] -->

```sh
git clone --depth=1 https://github.com/pyenv/pyenv.git ~/.pyenv
```

```sh
vim ~/.zshrc
```

```
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

```sh
source ~/.zshrc
pyenv install 3.10.11
```

Or install from files:

```sh
mkdir ~/.pyenv/cache
cd ~/.pyenv/cache
wget https://www.python.org/ftp/python/3.10.11/Python-3.10.11.tar.xz
pyenv install 3.10.11
```

```sh
pyenv global 3.10.11
pyenv local 3.10.11
```

### [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

```sh
git clone --depth=1 https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
vim ~/.zshrc
```

```
eval "$(pyenv virtualenv-init -)"
```

```sh
source ~/.zshrc
pyenv virtualenv 3.9.13 <venv>
cd <Project>
pyenv local <venv>
```

↪ [ubuntu에서 pyenv 설치하기](https://jinmay.github.io/2019/03/16/linux/ubuntu-install-pyenv-1/)

### [virtualenv](https://github.com/pypa/virtualenv)

```sh
pyenv exec pip install virtualenv
virtualenv <venv>
source <venv>/bin/activate
```