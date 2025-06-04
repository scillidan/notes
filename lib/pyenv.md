# [pyenv](https://github.com/pyenv/pyenv) (Cache)

````{tab} Ubuntu 22 ARM [^1][^2]
```sh
sudo apt update
sudo apt-get install -y build-essential curl libbz2-dev libffi-dev liblzma-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libssl-dev libxml2-dev libxmlsec1-dev llvm make tk-dev wget xz-utils zlib1g-dev
```

```sh
git clone --depth=1 https://github.com/pyenv/pyenv.git ~/.pyenv
vim ~/.zshrc
```

```
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

```sh
source ~/.zshrc
```
````

## [pyenv for Windows](https://github.com/pyenv-win/pyenv-win) [^3][^4]

```sh
git clone --depth=1 https://github.com/pyenv-win/pyenv-win ~/.pyenv
pyenv install -l | findstr 3.7
pyenv install -l | findstr 3.11
pyenv install 3.7.9-win32
pyenv install 3.11.9
pyenv shell <version>
```

## Usage

```sh
# mkdir ~/.pyenv/cache
# cd ~/.pyenv/cache
# wget https://www.python.org/ftp/python/3.10.11/Python-3.10.11.tar.xz
pyenv install 3.10.11
pyenv global 3.10.11
# pyenv local 3.10.11
```

[^1]: [ubuntu에서 pyenv 설치하기](https://jinmay.github.io/2019/03/16/linux/ubuntu-install-pyenv-1/)
[^2]: [pyenv install: 3.x BUILD FAILED (Ubuntu 20.04 using python-build 20180424)](https://stackoverflow.com/questions/67807596/pyenv-install-3-x-build-failed-ubuntu-20-04-using-python-build-20180424)
[^3]: [Installation](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#git-commands)
[^4]: [Add System Settings](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#add-system-settings)
[^5]: [Build older python package - 3.9](https://github.com/termux/termux-packages/discussions/9498)