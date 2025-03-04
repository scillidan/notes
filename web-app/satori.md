### [Satori](https://github.com/vercel/satori)

![](https://img.shields.io/github/license/vercel/satori?label=&style=flat-square) [![](https://img.shields.io/github/last-commit/scillidan/satori/main?label=&style=flat-square)](https://github.com/scillidan/satori)

````{tab} From source
```sh
git clone --depth=1 https://github.com/vercel/satori
cd satori
nvm install 16.20.0
nvm use 16.20.0
pnpm install
pnpm dev:playground -- -p 4321
```
````

````{tab} PM2
```sh
set PORT=4321
pm2 start -n "satori" --cwd "./" "./node_modules/turbo/bin/turbo" -- dev --filter=satori-playground...
```
````