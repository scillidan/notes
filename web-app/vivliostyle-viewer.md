### [Vivliostyle Viewer](https://github.com/vivliostyle/vivliostyle.js/tree/master/packages/viewer)

![](https://img.shields.io/github/license/vivliostyle/vivliostyle.js?label=&style=flat-square) [![](https://img.shields.io/github/last-commit/scillidan/vivliostyle.js/main?label=&style=flat-square)](https://github.com/scillidan/vivliostyle.js) ![](https://img.shields.io/badge/GitHub%20Pages-121013?logo=github&logoColor=white) ![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

````{tab} From source
1. Get `Stable release` from [Vivliostyle.js Releases](https://vivliostyle.github.io/).
2. Decompress it to `vivliostyle-viewer`.

```sh
cd vivliostyle-viewer
serve -s viewer -p 4321
```
````

````{tab} PM2
```sh
pm2 serve viewer 4321 --name vivliostyle-viewer --spa
```
````

#### Deploy with Github Pages

Visit `https://<username>.github.io/vivliostyle.js/viewer/vivliostyle-viewer.html`.