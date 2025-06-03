### [visionmagic](https://github.com/visioncortex/visionmagic)

![](https://img.shields.io/github/license/visioncortex/visionmagic?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/visionmagic/master?label=last%20commit%20(fork)&style=flat-square) ![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

````{tab} From source
```sh
git clone --depth=1 https://github.com/visioncortex/visionmagic
cd visionmagic
nvm install 16.20.0
nvm use 16.20.0
cd webapp/app
npm install
cargo install wasm-pack
wasm-pack build
npm start
```
````