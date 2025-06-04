# [sreadium](https://github.com/suisuyy/sreadium)

![](https://img.shields.io/github/license/suisuyy/sreadium?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/sreadium/main?label=last%20commit%20(fork)&style=flat-square) ![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white) ![](https://img.shields.io/badge/GitHub%20Pages-121013?logo=github&logoColor=white)

````{tab} From source
```sh
git clone --depth=1 https://github.com/suisuyy/sreadium
cd sreadium
```

1. Put `*.epub` into `epub_content/`.
2. Edit `epub_library.opds` by yourself.

```sh
serve -s . -p 4321
```
````

````{tab} PM2
```sh
pm2 serve . 4321 --name sreadium --spa
```
````

If app take up `4321` port, open `chrome://serviceworker-internals/?devtools` and unregister it.