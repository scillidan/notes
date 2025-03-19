### [Gifsicle Wasm Browser](https://github.com/renzhezhilu/gifsicle-wasm-browser)

![](https://img.shields.io/github/license/renzhezhilu/gifsicle-wasm-browser?style=flat-square)<br />
[![](https://img.shields.io/github/last-commit/scillidan/gifsicle-wasm-browser/main?label=last%20commit%20(fork)&style=flat-square)](https://github.com/scillidan/gifsicle-wasm-browser)

````{tab} From source
```sh
git clone --depth=1 https://github.com/renzhezhilu/gifsicle-wasm-browser
cd gifsicle-wasm-browser
npm install
serve -s docs -p 4321
```
````

````{tab} PM2
```sh
pm2 serve docs 4321 --name gifsicle-wasm-browser --spa
```
````

If app take up `4321` port, open `chrome://serviceworker-internals/?devtools` and unregister it.