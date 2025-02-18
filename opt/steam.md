### [Steam](https://store.steampowered.com/) (Cache)

````{tab} Ubuntu 24 ARM
```sh
sudo dpkg --add-architecture armhf
sudo apt-get update && sudo apt-get upgrade
sudo apt install gcc-arm-linux-gnueabihf -y
sudo apt-get install git -y
sudo apt install cmake -y
git clone --depth=1 https://github.com/ptitSeb/box64
cd box64
mkdir build; cd build; cmake .. -D RPI5ARM64=1 -D CMAKE_BUILD_TYPE=RelWithDebInfo
make -j4
sudo make install
sudo systemctl restart systemd-binfmt
```

```sh
cd ~
git clone --depth=1 https://github.com/ptitSeb/box86
cd box86
mkdir build; cd build; cmake .. -D RPI4ARM64=1 -D CMAKE_BUILD_TYPE=RelWithDebInfo
make -j4
sudo make install
sudo systemctl restart systemd-binfmt
```

```sh
sudo apt install libgdm1:armhf libudev1:armhf libgl1-mesa-dri:armhf libglapi-mesa:armhf libglu1-mesa:armhf libglx-mesa0:armhf mesa-va-drivers:armhf mesa-vdpau-drivers:armhf mesa-vulkan-drivers:armhf libsdl1.2debian:armhf libegl-mesa0:armhf
sudo apt-get install libc6:armhf -y
sudo apt install libcurl3t64-gnutls:armhf libcurl4t64:armhf
sudo apt install mesa-vulkan-drivers -y
```

- [How to install Steam on Raspberry Pi](https://www.xda-developers.com/install-steam-on-raspberry-pi/)
- [What is the best operating system for a Raspberry Pi to play games and do other heavy graphics tasks?](https://www.quora.com/What-is-the-best-operating-system-for-a-Raspberry-Pi-to-play-games-and-do-other-heavy-graphics-tasks)
- [Upgrade your Raspberry Pi 5 with a powerful graphics card](https://www.geeky-gadgets.com/add-a-graphics-card-to-raspberry-pi/)
- [Use an External GPU on Raspberry Pi 5 for 4K Gaming](https://www.jeffgeerling.com/blog/2024/use-external-gpu-on-raspberry-pi-5-4k-gaming)
- [Raspberry Pilink](https://www.renpy.org/doc/html/raspi.html)
````