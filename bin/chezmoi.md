### [chezmoi](https://www.chezmoi.io) [^1]

````{tab} Ubuntu 22 ARM
```sh
1. Get `chezmoi_*_linux_arm64.deb` from [chezmoi - Releases](https://github.com/twpayne/chezmoi).
2. `sudo dpkg -i chezmoi_*_linux_arm64.deb`
```
````

```sh
chezmoi init
vim ~/.local/share/chezmoi/.chezmoiignore
```

```
# example
lazy-lock.json
```

```sh
chezmoi add <files>
chezmoi diff
chezmoi apply -v
chezmoi cd
```

```sh
git remote add origin https://github.com/<user>/dotfiles
git branch -M main
git add .
git commit -m "<commit>"
git push -u origin main
```

On another PC:

```sh
chezmoi init https://github.com/<user>/<dotfiles>
chezmoi diff
chezmoi apply -v
# chezmoi edit <file>
# chezmoi merge <file>
# chezmoi update -v
```

[^1]: [Dotfiles with Chezmoi](https://blog.lazkani.io/posts/dotfiles-with-chezmoi/)
[^2]: [Chezmoi: ignore files and subdirectories](https://stackoverflow.com/questions/75519055/chezmoi-ignore-files-and-subdirectories)