### [goenv](https://github.com/go-nv/goenv)

```sh
git clone --depth=1 https://github.com/go-nv/goenv ~/.goenv
sudo vim ~/.zshrc
```

```
export GOENV_ROOT="$HOME/.goenv"
export PATH="$GOENV_ROOT/bin:$PATH"
eval "$(goenv init -)"
```

```sh
source ~/.zshrc
```

#### Usage

```sh
# wget https://go.dev/dl/go1.22.0.linux-arm64.tar.gz
# mkdir -p ~/.goenv/cache
# mv go1.22.0.linux-arm64.tar.gz ~/.goenv/cache/
goenv install 1.22.0
go version
```