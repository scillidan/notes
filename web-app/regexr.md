### [RegExr](https://github.com/gskinner/regexr)

![](https://img.shields.io/github/license/gskinner/regexr)
[![](https://img.shields.io/github/last-commit/scillidan/regexr/master?label=last%20commit%20(fork))](https://github.com/scillidan/regexr)

````{tab} From source
```sh
git clone --depth=1 https://github.com/gskinner/regexr
cd regexr
nvm install 10.21.0
nvm use 10.21.0
npm install
gulp
```
````

````{tab} PM2
```sh
pm2 start "...\gulp-cli\bin\gulp.js" --interpreter "...\.nvm\v10.21.0\node.exe" -n regexr
```
````

````{tab} Docker compose
```sh
mkdir regexr
cd regexr
vim docker-compose.yml
```

```yaml
version: '3.8'

services:
  regexr:
    image: gufertum/regexr
```

```sh
sudo docker compose up -d
```
````

If you need change port, edit `gulpfile.babel.js`:

````{tab} Windows 10
```js
gulp.task("serve", () => {
  browser({
    server: { baseDir: "./deploy/" },
    port: 4321,
  });
});
```
````