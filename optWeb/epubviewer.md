# [ePubViewer](https://github.com/pgaskin/ePubViewer)

![](https://img.shields.io/github/license/pgaskin/ePubViewer?style=flat-square) ![](https://img.shields.io/github/last-commit/pgaskin/ePubViewer/main?label=last%20commit%20(fork)&style=flat-square) ![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

````{tab} From source
```sh
serve -s . -p 4321
```
````

````{tab} PM2
```sh
pm2 serve . 4321 --name epubvidewer --spa
```
````

1. Visit `http://localhost:4000` or `http://localhost:4000#book.epub`.
2. If app take up `4321` port, open `chrome://serviceworker-internals/?devtools` and unregister it.