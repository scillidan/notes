### [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) [^1] (Cache)

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
cd <project>
pyenv local <venv>
```

[^1]: [ubuntu에서 pyenv 설치하기](https://jinmay.github.io/2019/03/16/linux/ubuntu-install-pyenv-1/)