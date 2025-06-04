# [LuaJIT](https://luajit.org/) [^1]

```sh
git clone --depth=1 https://luajit.org/git/luajit.git
cd luagit
git checkout v2.1
```

```sh
# msys2
pacman -S mingw-w64-x86_64-gcc mingw-w64-x86_64-make
make CFLAGS=-DLUAJIT_ENABLE_LUA52COMPAT TARGET_LDFLAGS=-mwindows
```

[^1]: [How to build windowless LuaJIT for Windows](https://gist.github.com/Egor-Skriptunoff/22bf55c1abe44d7825605e132e48c084)