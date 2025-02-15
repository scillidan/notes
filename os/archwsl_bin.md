### [asciinema](https://github.com/asciinema/asciinema)

↪ [CLI - Usage](https://docs.asciinema.org/manual/cli/usage/)  
↪ [agg - Usage](https://docs.asciinema.org/manual/agg/usage/)  
↪ [Recording & Sharing Terminal Sessions](https://weblog.masukomi.org/2022/10/11/recording_and_sharing_terminal_sessions/)

### [act](https://github.com/nektos/act)

```sh
act -l
act -n
act
```

### [broot](https://dystroy.org/broot)

↪ [edit a text file](https://dystroy.org/broot/file-operations/#edit-a-text-file)  
↪ [Launching movie playback via "am start"](https://stackoverflow.com/questions/8207548/launching-movie-playback-via-am-start)

### [cmus](https://cmus.github.io/)

```sh
cmus
:a <music_dir>
```

↪ [A command line music player.](https://nchrs.xyz/cmus.html)  
↪ [How can I create a playlist and add songs to it in cmus?](https://unix.stackexchange.com/questions/593727/how-can-i-create-a-playlist-and-add-songs-to-it-in-cmus)

### [Newsboat](https://github.com/newsboat/newsboat)

```sh
mkdir ~/.config/newsboat
vim ~/.config/newsboat/config
```

```
include /usr/share/doc/newsboat/contrib/colorschemes/plain
# include /data/data/com.termux/files/usr/share/doc/newsboat/contrib/colorschemes/plain
```

```sh
vim ~/.config/newsboat/urls
```

```
https://hnrss.org/newest
```

```sh
newsboat
```

↪ [ArchWiki - Newsboat](https://wiki.archlinux.org/title/Newsboat)

### [sdcv](https://github.com/Dushistov/sdcv)

<!--  
1. Get [ecdict-stardict-28.zip](https://github.com/skywind3000/ECDICT/releases) form [ECDICT](https://github.com/skywind3000/ECDICT).
2. Depress it into `files_sdcv/stardict-ecdct-2.4.2`

```sh
vim stardict-ecdict-2.4.2/stardict-ecdict-2.4.2.ifo
```

```
bookname=ecdict
```

```sh
sdcv <word>
```

↪ [A command line dictionary.](https://nchrs.xyz/stardict.html)
-->

### [dict-ecdict](https://github.com/tuberry/dict-ecdict)

<!-- --8<-- [start:ubuntu-server-arm-22] -->
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

↪ [How can I uncompress a \*.7z file?](https://askubuntu.com/questions/219392/how-can-i-uncompress-a-7z-file)
<!-- --8<-- [end:ubuntu-server-arm-22] -->

### [dict-wrapper](https://github.com/dekerser/dict-wrapper)

### [starfetch](https://github.com/Haruno19/starfetch)

```sh
git clone --depth=1 https://github.com/Haruno19/starfetch
```

Check `starfetch/res/constellations`.

```sh
git clone --depth=1 https://github.com/K1ngst0m/starfetch
cd starfetch
make
./starfetch.exe -r
```

Or:

Install and use MSYS2.

```sh
git clone --depth=1 https://github.com/CoderCharmander/starfetch
cargo build
cd target/debug
starfetch.exe -d
starfetch.exe -l
```