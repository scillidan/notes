# [Excalith Start Page](https://github.com/excalith/excalith-start-page)

![](https://img.shields.io/github/license/excalith/excalith-start-page?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/excalith-start-page/main?label=last%20commit%20(fork)&style=flat-square)![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

````{tab} PM2
```sh
git clone --depth=1 https://github.com/excalith/excalith-start-page
cd excalith-start-page
yarn
pm2 start yarn --watch --name "excalith-start-page" -- dev
```
````