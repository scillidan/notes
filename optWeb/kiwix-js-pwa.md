### [Kiwix JS](https://github.com/kiwix/kiwix-js-pwa)

![](https://img.shields.io/github/license/kiwix/kiwix-js-pwa?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/kiwix-js-pwa/main?label=last%20commit%20(fork)&style=flat-square) ![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

````{tab} From source
```sh
git clone --depth=1 https://github.com/kiwix/kiwix-js-pwa
cd kiwix-js-pwa
npm install
npm run build
npm run serve
```
````

````{tab} PM2
```sh
pm2 serve dist 5173 --name kiwix-js-pwa --spa --env production
```
````

#### Usage

1. Visit `http://localhost:5173`
2. Setting → Use Private File System → Add file(s) → Add to OPFS → Select your `.zim` → Wait for it to complete
3. (Optional) Install PWA
4. If you clean up the cache of browser, you need to do it again