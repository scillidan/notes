# [QR code designer](https://github.com/kochrt/qr-designer)

![](https://img.shields.io/github/license/kochrt/qr-designer?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/qr-designer/main?label=last%20commit%20(fork)&style=flat-square)

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