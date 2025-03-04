### [image-editor](https://github.com/andrepv/image-editor)

![](https://img.shields.io/github/license/andrepv/image-editor?label=&style=flat-square) [![](https://img.shields.io/github/last-commit/scillidan/image-editor/master?label=&style=flat-square)](https://github.com/scillidan/image-editor)

````{tab} From source
```sh
git clone --depth=1 https://github.com/andrepv/image-editor
cd image-editor
nvm install 16.20.0
nvm use 16.20.0
npm install
npm run build
serve -s build -l 4321
```
````

````{tab} PM2
```sh
pm2 serve build 4321 --name image-editor --watch --spa
```
````