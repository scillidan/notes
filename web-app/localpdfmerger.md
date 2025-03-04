### [Localpdf.tech](https://github.com/julianfbeck/localpdfmerger)

![](https://img.shields.io/github/license/julianfbeck/localpdfmerger?label=&style=flat-square) [![](https://img.shields.io/github/last-commit/scillidan/localpdfmerger/main?label=&style=flat-square)](https://github.com/scillidan/localpdfmerger) ![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

````{tab} From source
```sh
git clone --depth=1 https://github.com/julianfbeck/localpdfmerger
cd localpdfmerger
yarn
yarn build
yarn start
```
````

If you need to change port, edit `package.json`:

```json
  "scripts": {
    "start": "next start -p 4321"
}
```