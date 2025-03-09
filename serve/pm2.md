### [PM2](https://pm2.keymetrics.io/)

````{tab} Ubuntu 22 ARM [^1]
```sh
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source .bashrc
nvm install --lts
nvm use --lts
npm install -g pm2
# npm install pnpm -g
# pnpm setup
# source .bashrc
# pnpm add -g pm2
pm2 dump
pm2 startup
# pm2 unstartup
```
````

[^1]: [Persistent applications](https://pm2.keymetrics.io/docs/usage/startup/)

#### Reference

- [Vue packages version mismatch](https://github.com/nuxt/nuxt/issues/10305)
- [how to modify nuxt server start port ,default port is 3000](https://github.com/nuxt/nuxt/issues/490)

#### Cross-reference

- [pm2-installer](https://scillidan.github.io/notes/script/pm2-installer.html)