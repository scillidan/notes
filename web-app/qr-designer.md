### [QR code designer](https://github.com/kochrt/qr-designer)

![](https://img.shields.io/github/license/kochrt/qr-designer?label=&style=flat-square) [![](https://img.shields.io/github/last-commit/scillidan/qr-designer/main?label=&style=flat-square)](https://github.com/scillidan/qr-designer) ![](https://img.shields.io/badge/GitHub%20Pages-121013?logo=github&logoColor=white)

````{tab} From source
```sh
git clone --depth=1 https://github.com/kochrt/qr-designer
cd qr-designer
nvm install 16.20.0
nvm use 16.20.0
npm install
npm run generate
npm run start
```
````

````{tab} PM2
```sh
pm2 start npm --name "qr-designer" -- run start
```
````

If you need to change port, edit `nuxt.config.js`:

```json
  server: {
    host: "localhost",
    port: 3003
  },
```