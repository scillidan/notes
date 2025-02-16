### [uv](https://docs.astral.sh/uv/)

````{tab} Arch
```sh
uv python list
uv python install cpython-3.10.16-linux--x86_64-gnu
uv python pin cpython-3.10.16-linux-x86_64-gnu
cd ~
uv venv .venv
```
````

````{tab} Ubuntu 24 ARM [^1]
```sh
wget $(curl -s https://api.github.com/repos/astral-sh/uv/releases/latest | grep 'browser_download_url.*uv-aarch64-unknown-linux-gnu.tar.gz' | cut -d '"' -f 4)
sha256sum -c uv-aarch64-unknown-linux-gnu.tar.gz.sha256
tar -xzf uv-aarch64-unknown-linux-gnu.tar.gz -C uv
chmod +x uv-aarch64-unknown-linux-gnu
mv uv-aarch64-unknown-linux-gnu/* .local/bin/
```
````

[^1]: [Installing uv](https://docs.astral.sh/uv/getting-started/installation/)