# [Flood](https://github.com/jesec/flood)

````{tab} From source
```sh
git clone --depth=1 https://github.com/jesec/flood
cd flood
npm install
npm run build
# npm run start
vim package.json
```

```json
  "script": {
    "start": "node --enable-source-maps --use_strict dist/index.js --host 0.0.0.0 --port 4321",
```

```sh
pm2 start npm --name "flood" -- run start
```
````

Some tips:

1. Here are some important fields:
	```
	User for Flood: <user>
	Password for Flood: <password>
	URL: http://0.0.0.0:8050
	User for qBittorrent: admin
	Password for qBittorrent: adminadmin
	```
2. Default Download Directory is on `/home/qbittorrent-nox/Downloads`.
3. If you forget `<user>` or `<password>`, delete `~/.local/shared/flood/`. Reload or re-create flood's PM2 serve.