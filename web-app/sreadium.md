### [sreadium](https://github.com/suisuyy/sreadium)

![](https://img.shields.io/github/license/suisuyy/sreadium?label=&style=flat-square) [![](https://img.shields.io/github/last-commit/scillidan/sreadium/main?label=&style=flat-square)](https://github.com/scillidan/sreadium) ![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white) ![](https://img.shields.io/badge/GitHub%20Pages-121013?logo=github&logoColor=white)

````{tab} From source
```sh
git clone --depth=1 https://github.com/suisuyy/sreadium
cd sreadium
```

Put `*.epub` into `epub_content/`.

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