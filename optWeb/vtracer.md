# [Vtracer Web App](https://github.com/visioncortex/vtracer)

![](https://img.shields.io/github/license/visioncortex/vtracer?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/vtracer/master?label=last%20commit%20(fork)&style=flat-square)

````{tab} From source
```sh
git clone --depth=1 https://github.com/visioncortex/vtracer
cd vtracer
nvm install 16.20.0
nvm use 16.20.0
cd webapp/app
npm install
cargo install wasm-pack
wasm-pack build
npm run build
serve -s . -p 4321
```
````