# [NoteCalc](https://github.com/bbodi/notecalc3)

![](https://img.shields.io/github/license/bbodi/notecalc3) ![](https://img.shields.io/github/last-commit/scillidan/notecalc3/develop) ![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

````{tab} From source
```sh
git clone --depth=1 https://github.com/bbodi/notecalc3
cd notecalc3
# rustup override set nightly-2020-11-17
# cargo install wasm-pack
# wasm-pack build --release --target no-modules frontend-web
serve -s . -p 4321
```