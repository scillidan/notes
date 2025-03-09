### [recoded](https://github.com/siddharthroy12/recoded)

![](https://img.shields.io/github/license/siddharthroy12/recoded)
[![](https://img.shields.io/github/last-commit/scillidan//mainrecoded)](https://github.com/scillidan/recoded)
![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

````{tab} From source
```sh
git clone --depth=1 https://github.com/siddharthroy12/recoded
cd recoded
npm install --legacy-peer-deps
npm run build
serve -s build -p 4321
```
````

````{tab} PM2
```sh
pm2 serve build 4321 --name recoded --spa
```
````