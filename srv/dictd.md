### [dictd](https://linux.die.net/man/8/dictd)

````{tab} Ubuntu 22 ARM
```sh
sudo apt install dictd
# dict -d ecdict <word>
# pgrep dictd
# kill <pid>
```

For used serve on LAN:

```sh
sudo vim /etc/dictd/dictd.conf
```

```
global {
listen_to 0.0.0.0
}

access {
allow *
}
```

```sh
sudo vim /var/lib/dictd/db.list
```

For example [^1]:

```
database ecdict {
  data /mnt/nvme/share/dictd/ecdict.dict.dz
  index /mnt/nvme/share/dictd/ecdict.index
}
database 21th-en22zh {
  data /mnt/nvme/share/dictd/21shijishuangxiangcidian.dict.dz
  index /mnt/nvme/share/dictd/21shijishuangxiangcidian.index
}
database etymonline {
  data /mnt/nvme/share/dictd/etymonline.dict.dz
  index /mnt/nvme/share/dictd/etymonline.index
}
database gcide {
  data /mnt/nvme/share/dictd/gcide.dict.dz
  index /mnt/nvme/share/dictd/gcide.index
}
database dict-en-en {
  data /mnt/nvme/share/dictd/dict-en-en.dict.dz
  index /mnt/nvme/share/dictd/dict-en-en.index
}
database wikdict-en-zh {
  data /mnt/nvme/share/dictd/wikdict-en-zh.dict.dz
  index /mnt/nvme/share/dictd/wikdict-en-zh.index
}
# database wikdict-zh-en {
#   data /mnt/nvme/share/dictd/wikdict-zh-en.dict.dz
#   index /mnt/nvme/share/dictd/wikdict-zh-en.index
# }
# database chibigenc-sc {
#   data /mnt/nvme/share/dictd/chibigenc-sc.dict.dz
#   index /mnt/nvme/share/dictd/chibigenc-sc.index
# }
# database chibigenc {
#   data /mnt/nvme/share/dictd/chibigenc.dict.dz
#   index /mnt/nvme/share/dictd/chibigenc.index
# }
```

```sh
sudo systemctl enable --now dictd.service
```
````

#### Cross-reference

- [dict-ecdict.md](https://scillidan.github.io/notes/bin/dict-ecdict.html)

[^1]: [dictd.conf](https://gist.github.com/wind0204/d65c7d1b5d7794c4c7fa1a02d5151acc)