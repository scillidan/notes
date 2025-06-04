# [Bukubrow](https://github.com/samhh/bukubrow-webext) (Cache)

Install `Bukubrow` browser extension.

Host Bukuserver [^1]:

```sh
pipx install "buku[server]"
bukuserver run --host 127.0.0.1 --port 5001
```

```sh
git clone --depth=1 https://github.com/samhh/bukubrow-host
cd bukubrow-host
cargo build --release
./target/release/bukubrow --install-chrome
```

[^1]: [Bukuserver](https://github.com/jarun/buku/tree/master/bukuserver)