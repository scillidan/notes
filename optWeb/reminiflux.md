### [reminiflux](https://github.com/reminiflux/reminiflux)

![](https://img.shields.io/github/license/reminiflux/reminiflux?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/reminiflux/main?label=last%20commit%20(fork)&style=flat-square) ![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

````{tab} From source
```sh
git clone --depth=1 https://github.com/reminiflux/reminiflux
cd reminiflux
subl package.json
```

```json
  "scripts": {
    "build": "set GENERATE_SOURCEMAP=false && react-scripts build",
```

```sh
npm install
npm run build
serve -s build -p 4321
```
````

````{tab} PM2
```sh
pm2 serve build 4321 --name reminiflux --spa
```
````

#### Usage

1. Miniflux → Settings → API Keys → Create a new API key → `reminiflux` → Copy the Token
2. Visit `localhost:4321`
  ```
  Host `<your_host>:<port>`
  API key `<token>`
  ```