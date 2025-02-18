### [Raspberry Pi OS](https://www.raspberrypi.com/documentation/computers/os.html) [^1]

```sh
sudo cp /etc/apt/sources.list.d/raspi.list /etc/apt/sources.list.d/raspi.list.bat
sudo vim /etc/apt/sources.list.d/raspi.list
```

```
deb https://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ bookworm main
```

```sh
sudo apt update && sudo apt upgrade
```

#### Enable SSH

Preferences → Raspberry Pi Configuration → Interfaces → SSH (On) [^2]

```sh
hostname -I
```

[^1]: [清华大学开源软件镜像站 - Raspbian 软件仓库](https://mirrors.tuna.tsinghua.edu.cn/help/raspberrypi/)
[^2]: [How to SSH into Raspberry Pi](https://www.onlogic.com/company/io-hub/how-to-ssh-into-raspberry-pi/)