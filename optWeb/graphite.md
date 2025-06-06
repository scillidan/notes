# [Graphite](https://github.com/GraphiteEditor/Graphite) (Cache)

![](https://img.shields.io/github/license/GraphiteEditor/Graphite?style=flat-square)

````{tab} Ubuntu 24 ARM [^1]
```sh
cargo install cargo-watch
cargo install wasm-pack
cargo install -f wasm-bindgen-cli@0.2.99
sudo apt install libgtk-3-dev libsoup2.4-dev libjavascriptcoregtk-4.0-dev libwebkit2gtk-4.0-dev
git clone --depth=1 https://github.com/GraphiteEditor/Graphite
cd Graphite/frontend
cargo install cargo-about
cargo install wasm-opt
npm install vite --save-dev
npm run build
pm2 serve dist 4321 --name graphite --spa
```
````

## Deploy with Vercel (Cache)

Settings → Build and Deployment → Output Directory → `website/other/dist`

[^1]: [Project setup](https://graphite.rs/volunteer/guide/project-setup/)