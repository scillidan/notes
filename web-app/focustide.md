### [FocusTide](https://github.com/Hanziness/FocusTide)

![](https://img.shields.io/github/license/Hanziness/FocusTide) [![](https://img.shields.io/github/last-commit/scillidan/FocusTide/main)](https://github.com/scillidan/FocusTide) ![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

````{tab} From source
```sh
yarn install
yarn generate
serve dist -p 4321
```

If app take up `4321` port, open `chrome://serviceworker-internals/?devtools` and unregister it.
````

````{tab} PM2
```sh
pm2 serve dist 4321 --name focustide --spa
```
````