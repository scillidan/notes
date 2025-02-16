### [dict-ecdict](https://github.com/tuberry/dict-ecdict)

````{tab} Ubuntu 22 ARM [^1]
```sh
sudo apt install unzip p7zip-full dictfmt dictzip python-is-python3
git clone --depth=1 --single-branch -b master https://github.com/tuberry/dict-ecdict
cd ./dict-ecdict
make && sudo make install
```

```sh
sudo mkdir -p /etc/dict 
sudo vim /var/lib/dictd/db.list
```

```
database ecdict {
	data /usr/share/dictd/ecdict.dict.dz
	index /usr/share/dictd/ecdict.index
}
```

```sh
sudo systemctl restart dictd.service
```
````

[^1]: [How can I uncompress a \*.7z file?](https://askubuntu.com/questions/219392/how-can-i-uncompress-a-7z-file)