# [Flowchart Fun](https://github.com/tone-row/flowchart-fun)

![](https://img.shields.io/github/license/tone-row/flowchart-fun?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/flowchart-fun/main?label=last%20commit%20(fork)&style=flat-square)

````{tab} From source
```sh
git clone --depth=1 https://github.com/tone-row/flowchart-fun
cd flowchart-fun
pnpm install
pnpm build
serve -s app/build -p 4321
```
````

````{tab} PM2
```sh
pm2 serve app\build\ 4321 --name flowchart-fun --spa
```
````