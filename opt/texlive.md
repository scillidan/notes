### [TeX Live](https://www.tug.org/texlive)

````{tab} Arch [^1][^2]
```sh
sudo /opt/texlive-installer/install-tl
sudo /usr/local/texlive/2024/bin/x86_64-linux/tlmgr option repository https://mirrors.cernet.edu.cn/CTAN/systems/texlive/tlnet
tlmgr update --list
sudo /usr/local/texlive/2024/bin/x86_64-linux/tlmgr update --all
```
````

[^1]: [TeX Live](https://wiki.archlinux.org/title/TeX_Live)
[^2]: [tlmgr](https://tug.org/texlive/doc/tlmgr.html)