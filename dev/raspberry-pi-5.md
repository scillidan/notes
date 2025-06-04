# [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5)

1. Get `balenaEtcher-win32-x64-*.zip` from [Etcher - Releases](https://github.com/balena-io/etcher/releases)
2. Decompress it to `balenaEtcher\`
3. Get [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
4. Raspberry Pi Imager
	1. Raspberry Pi Device → Raspberry Pi 5
	2. 请选择需要写入的操作系统 → Other general-purpose OS → Ubuntu → Ubuntu Desktop 24.10 (64-bit)
	3. 储存卡 → SD card
	4. Next
5. Install SD card in Pi5 and do user settings
	1. Enable WiFi
	2. Enable SSH [^1]:
	```
	sudo apt install ssh
	sudo systemctl enable ssh
	sudo ufw allow ssh
	sudo ufw enable
	sudo shutdown
	```
6. Put SD card into card reader. Add new line `dtparam=pciex1_gen3` into `SD card\config.txt` [^2]
7. balenaEtcher → clone `SD card` to `NVMe driver`
8. Install NVMe driver in Pi5, power on
9. You can log in to it via SSH

[^1]: [Quick Guide to Enabling SSH on Ubuntu 24.04](https://linuxconfig.org/quick-guide-to-enabling-ssh-on-ubuntu-24-04)
[^2]: [Ubuntu 24.04 LTS Raspberry Pi 5. NVMe install Fix](https://www.youtube.com/watch?v=2qkqCB8x2nM)