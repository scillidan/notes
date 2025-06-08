# [Scoop](https://scoop.sh/)

## Install [^1][^2][^3]

```pwsh
Set-ExecutionPolicy ByPass -Scope Process -Force
$env:SCOOP='C:\Users\User\Scoop'
$env:SCOOP_GLOBAL='C:\Users\User\Scoop'
[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')
iex "& {$(irm get.scoop.sh)} -RunAsAdmin"
```

## Update scoop

````{tab} scoop
```sh
scoop update scoop
```
````

````{tab} git [^4]
```sh
cd C:\Users\User\Scoop\apps\scoop\current
git fetch
git pull
```
````

## Add bucket

````{tab} scoop
```sh
scoop bucket add extras
scoop bucket add nonportable
scoop bucket add nirsoft
scoop bucket add versions
scoop bucket add java
scoop bucket add games
```
````

````{tab} git
```sh
cd C:\Users\User\Scoop\buckets
# git clone --depth=1 https://github.com/ScoopInstaller/Main
git clone --depth=1 https://github.com/ScoopInstaller/Extras
git clone --depth=1 https://github.com/ScoopInstaller/Nonportable
git clone --depth=1 https://github.com/kodybrown/scoop-nirsoft
git clone --depth=1 https://github.com/ScoopInstaller/Versions
git clone --depth=1 https://github.com/ScoopInstaller/Java
git clone --depth=1 https://github.com/Calinou/scoop-games
```
````

## Cteate your bucket

- [CONTRIBUTING.md](https://github.com/ScoopInstaller/.github/blob/main/.github/CONTRIBUTING.md)
	- [App Manifests](https://github.com/ScoopInstaller/Scoop/wiki/App-Manifests)
	- [App Manifest Autoupdate](https://github.com/ScoopInstaller/Scoop/wiki/App-Manifest-Autoupdate)
- [Scoop Bucket Template](https://github.com/ScoopInstaller/BucketTemplate)
- References
	- [7zip.json](https://github.com/ScoopInstaller/Main/blob/master/bucket/7zip.json)
	- [alacritty.json](https://github.com/ScoopInstaller/Extras/blob/master/bucket/alacritty.json)
	- [calibre.json](https://github.com/ScoopInstaller/Extras/blob/master/bucket/calibre.json)
	- [handbrake.json](https://github.com/ScoopInstaller/Extras/blob/master/bucket/handbrake.json)
	- [mpv.json](https://github.com/ScoopInstaller/Extras/blob/master/bucket/mpv.json)
	- [neovim.json](https://github.com/ScoopInstaller/Main/blob/master/bucket/neovim.json)
	- [sumatrapdf-installer.json](https://github.com/ScoopInstaller/Versions/blob/master/bucket/sumatrapdf-installer.json)

## Install package

For example:

```sh
scoop install scoop-search
```

[^1]: [Scoop (un)installer](https://github.com/ScoopInstaller/Install#advanced-installation)
[^2]: [CMD.exe wrapper](https://github.com/shilangyu/scoop-search#cmdexe-wrapper)
[^3]: [About the Download Directory](https://github.com/ScoopInstaller/Scoop/issues/3666)
[^4]: [scoop update fails to connect to GitHub](https://github.com/ScoopInstaller/Scoop/issues/3124)