### [PDF.js](https://github.com/mozilla/pdf.js)

![](https://img.shields.io/github/license/mozilla/pdf.js) [![](https://img.shields.io/github/last-commit/scillidan/pdf.js/main)](https://github.com/scillidan/pdf.js) ![](https://img.shields.io/badge/GitHub%20Pages-121013?logo=github&logoColor=white)

````{tab} From source [^1]
Install [GTK 2](https://github.com/Automattic/node-canvas/wiki/Installation:-Windows#2-installing-gtk-2).

```sh
pnpm install node-pre-gyp
git clone --depth=1 https://github.com/mozilla/pdf.js
cd pdf.js
npm install
npm install -g gulp-cli
gulp generic
dufs build/generic
```
````

````{tab} 
```sh
pm2 serve -s build/generic -p 4321 --name pdfjs --spa
```
````

Visit `localhost:<port>/web/viewer.html` or `localhost:<port>/web/viewer.html?file=<your_book>.pdf`.

[^1]: [Error on npm install](https://github.com/mozilla/pdf.js/issues/15112).