# [Uconsole CM4](https://www.clockworkpi.com/uconsole) [^1][^2][^3] (Cache)

```sh
sudo wipefs --all /dev/sdc
sudo fdisk --list
sudo fdisk /dev/sdc
sudo mkfs.vfat /dev/sdc1
sudo mkfs.ext4 /dev/sdc2
```

```sh
sudo umount /mnt/boot
sudo umount /mnt
```

```sh
sudo fdisk --list
sudo mount /dev/sdc2 /mnt
sudo mkdir /mnt/boot
sudo mount /dev/sdc1 /mnt/boot
```

```sh
sudo pacman -Sy
sudo pacman -S qemu-user-static qemu-user-static-binfmt arch-install-scripts
```

```sh
sudo bsdtar -xpf ArchLinuxARM-aarch64-latest.tar.gz -C /mnt
ls -l /mnt
sudo genfstab -U /mnt | sudo tee -a /mnt/etc/fstab
```

```sh
sudo arch-chroot /mnt
pacman-key --init
pacman-key --populate archlinuxarm
pacman -Sy raspberrypi-bootloader firmware-raspberrypi
pacman -R linux-aarch64
```

````{tab} pacman
```sh
pacman -U --noconfirm linux-uconsole-cm3-rpi64*.pkg.zst
pacman -U --noconfirm ap6256-firmware*.pkg.tar
```
````

````{tab} From source
```sh
git clone --depth=1 https://github.com/PotatoMania/uconsole-cm3
# git clone --depth=1 https://github.com/systematiccaos/uconsole-cm3-cm4
cd uconsole-cm3/PKGBUILDs/linux-uconsole-cm3-rpi64
git clone --depth=1 -b rpi-6.1.y https://github.com/raspberrypi/linux.git
tar -czvf linux.tar.gz linux
cd linux
git status
git restore --source=HEAD :/
```

```sh
sudo pacman -S cpio pahole aarch64-linux-gnu-gcc make flex bison patch
makepkg
pacman -Syu
```

```sh
useradd -m auruser
passwd auruser
echo "auruser ALL=(ALL) ALL" > /etc/sudoers.d/auruser
chmod 440 /etc/sudoers.d/auruser
chmod u+w /home/auruser/ap6256-firmware
pacman -S fakeroot sudo
su - auruser
ls -l /home/auruser/ap6256-firmware
export PKGDEST=/tmp/my_package_destination
export SRCDEST=/tmp/my_source_directory
export BUILDDIR=/tmp/my_build_directory
makepkg
pacman -U /tmp/my_package_destination/ap6256-firmware-0.1.20231120-1-any.pkg.tar.xz
```
````

```sh
sudo vim /mnt/boot/config.txt
```

```
ignore_lcd=1
disable_fw_kms_setup=1
max_framebuffers=2
arm_boost=1

# setup headphone detect pin
gpio=10=ip,np

# boot kernel directly
kernel=Image.gz
arm_64bit=1
initramfs initramfs-linux.img followkernel

# overlays
dtoverlay=dwc2,dr_mode=host
dtoverlay=vc4-kms-v3d
dtoverlay=audremap,pins_12_13
dtparam=audio=on
dtoverlay=uconsole
```

```sh
pacman -S iwe
sudo vim /mnt/boot/config.txt
```

```
[all]
ignore_lcd=1
disable_fw_kms_setup=1
disable_audio_dither
pwm_sample_bits=20

# setup headphone detect pin
gpio=10=ip,np

# boot custom kernel
kernel=Image.gz
arm_64bit=1
initramfs initramfs-linux.img followkernel

dtoverlay=dwc2,dr_mode=host
dtoverlay=audremap,pins_12_13
dtparam=audio=on

[pi3]
dtoverlay=vc4-kms-v3d
dtoverlay=uconsole

[cm4]
arm_boost=1
max_framebuffers=2
dtoverlay=vc4-kms-v3d-pi4
dtoverlay=uconsole,cm4

[all]
# whatever you need
```

```sh
sudo umount /mnt/boot /mnt
```

## Reference

- [Create DevTerm CM4 OS image from scratch](https://github.com/clockworkpi/DevTerm/wiki/Create-DevTerm-CM4-OS-image-from-scratch)
- [How uConsole CM4 OS image made](https://github.com/clockworkpi/uConsole/wiki/How-uConsole-CM4-OS-image-made)

[^1]: [How to install ArchLinux on uConsole/CM3 from scratch](https://github.com/PotatoMania/uconsole-cm3)
[^2]: [uConsole CM3](https://github.com/PotatoMania/uconsole-cm3/blob/dev/doc/how-to-install-archlinux-from-scratch.md)
[^3]: [Wifi not working on CM4](https://github.com/PotatoMania/uconsole-cm3-arch-image-builder/issues/1)