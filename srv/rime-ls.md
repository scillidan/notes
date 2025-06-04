# [rime-ls](https://github.com/wlh320/rime-ls) (Cache)

```sh
git clone --depth=1 https://github.com/wlh320/rime-ls
cd rime-ls
git fetch --tags
git checkout v0.4.1
```

````{tab} Windows 10
```sh
cargo build --release
```
````

````{tab} ArchWSL (Cache)
```sh
sudo pacman -S rustup
rustup default stable
cargo build --release
```
````

````{tab} Ubuntu 24 [^1] (Cache)
```sh
sudo apt install build-essential librime-dev rustup
rustup default stable
rustup target add aarch64-unknown-linux-gnu
cargo build --target aarch64-unknown-linux-gnu --release
```
````

````{tab} Ubuntu 24 ARM (Cache)
```sh
sudo apt install build-essential libclang-dev librime-dev rustup
rustup default stable
rustup target add aarch64-unknown-linux-gnu
cargo build --target aarch64-unknown-linux-gnu --release
```
````

````{tab} Termux (Cache)
On Windows 10:

```sh
subl cargo.toml
```

```toml
[dependencies]
librime-sys = { git = "https://github.com/lotem/librime-sys" }
```

```sh
cargo install cargo-ndk
rustup target add aarch64-linux-android
# rustup target add armv7-linux-androideabi x86_64-linux-android i686-linux-android
cargo ndk -t aarch64-linux-android build --release
```
````

```sh
ln ~/.cargo/tmp/release/rime_ls ~/.local/bin/rime_ls
```

## Cross-reference

- [cmp-lsp-rimels.md](https://scillidan.github.io/notes/opt/neovim/cmp-lsp-rimels.html)