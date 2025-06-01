### [yomichan-web-service](https://github.com/tetraset/yomichan-web-service) (Cache)

````{tab} ArchWSL
```sh
sudo pacman -S memcached
yay -S mongodb42-bin
nvm install hydrogen
```

```sh
git clone --depth=1 https://github.com/tetraset/yomichan-web-service
cd yomichan-web-service
npm install
node yomichan.js
```
````