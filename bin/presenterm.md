### [presenterm](https://github.com/mfontanini/presenterm)

````{tab} ArchWSL
```sh
sudo pacman -S presenterm
```
````

#### Usage

```sh
git clone --depth=1 https://github.com/mfontanini/presenterm
cd presenterm
presenterm --theme dark examples/demo.md
# pipx install presenterm-export
presenterm --export-pdf --theme light examples/demo.md
```