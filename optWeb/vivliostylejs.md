# [Vivliostyle Viewer](https://github.com/vivliostyle/vivliostyle.js)

![](https://img.shields.io/github/license/vivliostyle/vivliostyle.js?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/vivliostyle.js/main?label=last%20commit%20(fork)&style=flat-square)

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

## Deploy with Github Pages

1. Github → Project → Settings → Pages → Build and deployment → Branch → gh-pages.
2. After deploy, visit `https://<username>.github.io/vivliostyle.js/viewer/vivliostyle-viewer.html`.

## Reference

- [[Support Guide] Handling CORS on Netlify](https://answers.netlify.com/t/support-guide-handling-cors-on-netlify/107739)