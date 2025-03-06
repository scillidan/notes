### [Rust](https://www.rust-lang.org/)

````{tab} Ubuntu 22 ARM [^1]
```sh
sudo apt install rustc cargo
```
````

````{tab} Ubuntu 24 ARM
```sh
sudo apt install rustup
rustup default stable
```
````

#### Update

````{tab} Windows 10
```sh
set RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
set RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup
rustup update
```
````

[^1]: [How to Install Rust on Ubuntu](https://phoenixnap.com/kb/install-rust-ubuntu)
[^2]: [[已解决]请问安装或升级rust都出错怎么解决？](https://rustcc.cn/article?id=8e7ce61d-50c3-4a45-9652-b0cf01e5d640)