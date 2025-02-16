### [MSYS2](https://www.msys2.org/) (Cache)

```sh
pacman -Syyu
pacman -S mingw-w64-ucrt-x86_64-gcc
pacman -S mingw-w64-x86_64-cargo-c mingw-w64-x86_64-protobuf
cargo install atuin
pacman -S mingw-w64-ucrt-x86_64-pkg-config
```

#### Reference

- [Install gcc compiler on Windows with MSYS2 for C/C++](https://www.devdungeon.com/content/install-gcc-compiler-windows-msys2-cc)
- [Using CMake in MSYS2](https://www.msys2.org/docs/cmake/)
- [How to Install GCC in Termux for C++ Programming](https://www.samgalope.dev/2024/09/03/how-to-install-gcc-in-termux-for-c-programming/)