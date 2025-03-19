### [Reference](https://github.com/Fechin/reference)

![](https://img.shields.io/github/license/Fechin/reference?style=flat-square)<br />
[![](https://img.shields.io/github/last-commit/scillidan/reference/main?label=last%20commit%20(fork)&style=flat-square)](https://github.com/scillidan/reference)<br />
![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

````{tab} From source
```sh
git clone --depth=1 https://github.com/Fechin/reference
cd reference
npm install
npm run build
npm run dev
```
````

````{tab} PM2 [^1]
```sh
hexo g
pm2 serve public 4321 --name reference --watch --spa
# watchexec -w source\_posts -- hexo g
```
````

If you need to change port, edit `_config.yml`:

```yaml
url: http://localhost
```

[^1]: [Watchexec](https://github.com/watchexec/watchexec)