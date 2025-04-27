### [uv](https://docs.astral.sh/uv/)

````{tab} Arch
```sh
uv python list
uv python install 3.10.*
uv python pin 3.10.*
cd ~
uv venv .venv
# deactivate
```
````

`````{tab} Ubuntu 24 ARM [^1]
````{tab} install.sh
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
````

````{tab} Download
```sh
wget $(curl -s https://api.github.com/repos/astral-sh/uv/releases/latest | grep 'browser_download_url.*uv-aarch64-unknown-linux-gnu.tar.gz' | cut -d '"' -f 4)
sha256sum -c uv-aarch64-unknown-linux-gnu.tar.gz.sha256
tar -xzf uv-aarch64-unknown-linux-gnu.tar.gz -C uv
chmod +x uv-aarch64-unknown-linux-gnu
mv uv-aarch64-unknown-linux-gnu/* .local/bin/
```
````
`````

[^1]: [Installing uv](https://docs.astral.sh/uv/getting-started/installation/)