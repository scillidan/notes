# [FocusTide](https://github.com/Hanziness/FocusTide)

![](https://img.shields.io/github/license/Hanziness/FocusTide?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/FocusTide/main?label=last%20commit%20(fork)&style=flat-square)

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