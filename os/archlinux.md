### [Arch Linux](https://archlinux.org/)

#### Init

##### Login

After boot, login with [^1]:

```
username: root
password: root
```

##### Wireless configure [^2] (Optional):

```sh
ip link
systemctl status iwd
systemctl restart iwd
systemctl status iwd
iwctl
device list
station wlan0 scan
station wlan0 get-networks
station wlan0 connect "<ssid>"
ping archlinux.org
```

##### [Pacman](https://pacman.archlinux.page/) [^3][^4]

Use repository mirror:

```sh
sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
sudo vim /etc/pacman.d/mirrorlist
```

```
Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch
```

Refreshes the package database and upgrades all installed packages:

```sh
pacman -Syyu
```

Additional tools for `pacman`:

```sh
sudo pacman -S pacman-contrib
```

Removes older versions of packages from the cache, keeping only the two most recent versions for each one.

```sh
sudo paccache -rk 2
```

##### [Users and groups](https://wiki.archlinux.org/title/Users_and_groups)

````{tab} useradd
```sh
sudo useradd -m <user>
sudo vim /etc/sudoers
```

```
<user> ALL=(ALL:ALL) ALL
```
````

````{tab} addgroup
```sh
sudo addgroup sudousers
sudo usermod -aG sudousers <user>
sudo vim /etc/sudoers
```

```
sudousers ALL=(ALL)ALL
```
````

```sh
reboot
```

##### [Localization](https://wiki.archlinux.org/title/Localization) [^5]

```sh
sudo vim /etc/locale.gen
```

```
en_US.UTF-8 UTF-8
zh_CN.UTF-8 UTF-8
```

```sh
sudo locale-gen
```

```sh
sudo vim /etc/locale.conf
```

```
LANG=en_US.UTF-8
```

##### [System time](https://wiki.archlinux.org/title/System_time)

```sh
timedatectl set-timezone Asia/Shanghai
```

##### [Set the hostname](https://wiki.archlinux.org/title/Network_configuration#Set_the_hostname)

```sh
sudo vim /etc/hostname
```

```
<hostname>
```

```sh
sudo systemctl restart systemd-hostnamed
```

##### [Domain name resolution](https://wiki.archlinux.org/title/Domain_name_resolution) [^6]

```sh
sudo vim /etc/hosts
```

```
<ip> github.com
<ip> raw.githubusercontent.com
<ip> mirror.archlinuxarm.org
```

```sh
sudo systemctl restart systemd-resolved
```

##### [NetworkManager](https://wiki.archlinux.org/title/NetworkManager)

```sh
sudo pacman -S networkmanager
sudo systemctl stop netctl
sudo systemctl disable netctl
sudo systemctl enable --now networkmanager
```

Enable system tray:

```sh
sudo pacman -S network-manager-applet
```

#### Setup

##### [yay](https://github.com/Jguer/yay)

````{tab} pacman
```sh
sudo pacman -Syu yay
```
````

````{tab} From source
```sh
gh auth login
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg
sudo pacman -U yay-bin*.pkg.tar.xz
yay
```
````

##### [Paru](https://github.com/Morganamilo/paru) (Optional)

```sh
yay -S paru
```

##### [Flatpak](https://github.com/flatpak/flatpak) [^7] (Optional)

```sh
sudo pacman -S flatpak
reboot
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

You can find apps on [Flathub](https://flathub.org/).

##### [Uncomplicated Firewall](https://wiki.archlinux.org/title/Uncomplicated_Firewall)

```sh
sudo pacman -S ufw
sudo ufw status
sudo systemctl enable --now ufw
sudo ufw status
```

##### SSH [^8]

```sh
sudo pacman -S openssh
sudo systemctl enable --now sshd
sudo ufw allow 22/tcp
ip addr show
```

Get your `ip` of `inet`. On client machine:

```sh
ssh <user>@<ip>
```

##### [Xfce](https://wiki.archlinux.org/title/Xfce) [^9]

```sh
sudo pacman -S xorg
sudo pacman -S xfce4 xfce4-goodies
```

##### i3 [^10] (Optional)

```sh
sudo pacman -S i3
```

##### [Hyprland](https://hyprland.org/) (Cache)

##### [Sway](https://swaywm.org/) [^11] (Cache)

##### [Thunar]

- Thunar → View → Show Hidden Files
- Thunar → View → Configure Toolbar
	```
	New Tab
	Split View
	View Switcher
	```

##### [Nemo](https://wiki.archlinux.org/title/Nemo) [^12] (Optional)

```sh
sudo pacman -S nemo
```

##### [LightDM](https://wiki.archlinux.org/title/LightDM) [^13][^14]

```sh
sudo pacman -S lightdm lightdm-webkit2-greeter
```

```sh
git clone --depth=1 https://github.com/TheTerrior/lightdm-minimal
cd lightdm-minimal
chmod +x ./risky_installer.sh
sudo ./risky_installer.sh
sudo vim /etc/lightdm/lightdm.conf
```

```
[Seat:*]
greeter-session=lightdm-webkit2-greeter
```

```sh
sudo vim /etc/lightdm/lightdm-webkit2-greeter.conf
```

```
webkit_theme = minimal
```

```sh
sudo systemctl enable --now lightdm
```

##### [xfce-tile](https://github.com/dodophoenix/xfce-tile) (Optional)

```sh
git clone --depth=1 https://github.com/dodophoenix/xfce-tile
cd xfce-tile
cp xfce-setup-shortcuts.sh xfce-setup-shortcuts.sh.bak
vim xfce-setup-shortcuts.sh
chmod +x ./xfce-setup-shortcuts.sh
./xfce-setup-shortcuts.sh
```

##### Console font [^15][^16] (Optional)

```sh
showconsolefont
ls /user/share/kbd/showconsolefont
sudo pacman -S terminus-font
setfont drdos8x14 -m 8859-2
```

##### Bluetooth [^17][^18]

```sh
sudo pacman -S bluez bluez-utils blueman
sudo systemctl enable --now bluetooth
systemctl status bluetooth
sudo vim /etc/bluetooth/main.conf
```

```
AutoEnable=true
```

If return `Bluetooth service was skipped because of an unmet condition check ...` [^19]:

```sh
sudo modprobe bluetooth
sudo systemctl restart bluetooth
systemctl status bluetooth
```

##### Audio

````{tab} pulseaudio
```sh
sudo pacman -S pulseaudio
```
````

````{tab} pipewire
```sh
sudo pacman -R pulseaudio
yay -S pipewire-pulse
sudo systemctl enable --now pipewire
```
````

##### USB drive [^20]

```sh
sudo pacman -S udisks2
```

```sh
sudo fdisk -l
udisksctl mount -b /dev/sda1
udisksctl unmount -b /dev/sda1
udisksctl power-off -b /dev/sda
```

##### [auto-cpufreq](https://github.com/AdnanHodzic/auto-cpufreq) [^3]

```sh
git clone --depth=1 https://github.com/AdnanHodzic/auto-cpufreq.git
cd auto-cpufreq
sudo ./auto-cpufreq-installer
sudo auto-cpufreq --install
sudo systemctl status auto-cpufreq
sudo auto-cpufreq --stats
```

##### [preload](http://sourceforge.net/projects/preload) [^3]

```sh
yay -S preload
sudo systemctl enable --now preload
sudo systemctl status preload
```

```sh
sudo systemctl stop preload && sudo systemctl disable preload
sudo reboot
```

##### [Timeshift](https://github.com/teejee2008/timeshift) [^3]

```sh
yay -S timeshift
```

```sh
sudo timeshift --list
sudo timeshift --restore --snapshot '20XX-XX-XX_XX-XX-XX' --skip-grub
```

##### [restic](https://restic.net/) (Cache)

##### Application Autostart

Settings → Session and Startup → Application Autostart → Add:

```
Name `<name>`
Command `<command>`
```

##### Configure Desktop

###### [Materia](https://github.com/nana-4/materia-theme)

```sh
sudo pacman -S materia-gtk-theme
```

Settings → Appearance → Style → Materia-dark-compact.

###### [Papirus](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)

```sh
sudo pacman -S papirus-icon-theme
```

Settings → Appearance → Icons → `Papirus-Dark`.

###### [SIF](https://github.com/BlueManCZ/SIF) (Optional)

##### Configure Cursor

```sh
mkdir ~/.icons
cd ~/.icons
```

1. Get `Bibata-Rainbow-*.tar.gz` from [Bibata Cursor Rainbow - Releases](https://github.com/ful1e5/Bibata_Cursor_Rainbow/releases).  
2. Get `Chroma-*.tar.xz` from [Chroma Cursors for Linux](https://www.gnome-look.org/p/2045954).

```sh
tar -xvf Bibata-Rainbow-Modern.tar.gz
tar -xvf Bibata-Rainbow-Original.tar.gz
tar -xvf Chroma-Black-M.tar.xz
tar -xvf Chroma-Black-S.tar.xz
```

Settings → Mouse and Touchpad → Theme → `<theme>`

##### Configure applications menu

- Settings → Panel → Appearance
	- Style → Solid color
	- Color → `black`
- Settings → Panel → Items
	1. Separator → Edit
		- Style → Transparent
		- Expand (Off)
	2. Applications Menu → Edit
		- Show button title (Off)
		- Icon → Select icon from → Image Files → `100x100.png`
	3. Separator → Expand (Off)
	4. Workspace Switcher → Edit
		- Appearance → Buttons
		- Workspace Settings → General → Names
			```
			# Workspace Name
			1 1
			2 2
			3 3
			4 4
			```
	5. Separator → Expand (On)
	6. Windows Buttons → Edit
		- Show button labels (Off)
		- Show handle (Off)
	7. Separator → Expand (On)
	8. Status Tray Plugin → Edit
		- Adjust size automatically (On)
		- Arrange items in a single row (On)
	9. Wavelan → Edit
		- Show signal bar (Off)
	10. Batter Monitor → Edit
		- Display icon (On)
		- Display bar (Off)
	11. Separator → Expand (Off)
	12. Clock → Edit
		- Timezone → Asia/Shanghai
		- Layout → Time Only
	13. Separator → Expand (Off)

##### Configure wallpaper

````{tab} Thunar
```sh
mkdir -p ~/Pictures/wallpaper
```

1. Put wallpaper images into `~/Pictures/wallpaper`.
2. Thunar → Choice image → Context menu → Set as wallpaper
````

````{tab} nitrogen
```sh
sudo pacman -S nitrogen
```

nitrogen → Preferences → Add → `~/Pictures/wallpaper` → OK → Apply.
````

##### Fonts

```sh
sudo pacman -S adobe-source-han-serif-cn-fonts \
	noto-fonts-cjk \
	noto-fonts-emoji \
	noto-fonts-extra
```

#### Install Opts

##### [picom](https://github.com/yshui/picom)

```sh
sudo pacman -S picom
```

##### [dunst](https://github.com/dunst-project/dunst)

```sh
sudo pacman -S dunst
```

##### [Alacritty](https://alacritty.org/)

```sh
sudo pacman -R xfce4-terminal
sudo pacman -S alacritty
```

##### [Rime](https://rime.im/)

```sh
sudo pacman -S fcitx5-im
```

```
sudo vim /etc/environment
```

```
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=fcitx
SDL_IM_MODULE=fcitx
```

##### [Brave](https://brave.com)

```sh
yay -S brave-bin
```

##### [qutebrowser](https://qutebrowser.org/) (Optional)

```sh
pacman -S qutebrowser
```

##### [mpv](https://mpv.io/)

```sh
sudo pacman -S mpv
cp -r /usr/share/doc/mpv/ ~/.config/
```

##### [ClamAV](https://www.clamav.net/)

```sh
sudo pacman -S clamav
```

```sh
clamd
clamscan <file>
```

If return `ERROR: Can't create freshclam.dat in /usr/local/share/clamav` [^21]:

```sh
sudo chown -R <user> /usr/local/share/clamav
```

##### Clipboard

```sh
sudo pacman -R xfce4-clipman-plugin
sudo pacman -S copyq
```

##### [qView](https://interversehq.com/qview/) (Optional)

```sh
yay -S qview
```

##### [Flameshot](https://flameshot.org/) (Optional)

##### [Snipaste](https://www.snipaste.com/)

```sh
yay -S snipaste
```

##### [eSearch](https://github.com/xushengfeng/eSearch) (Optional)

```sh
git clone --depth=1 https://aur.archlinux.org/e-search-bin.git
```

Download `eSearch-*-linux-x64.deb` from [releases](https://github.com/xushengfeng/eSearch/releases).

```sh
mv eSearch-*-linux-x64.deb e-search-*.deb
mv e-search-*.deb e-search-bin/
cd e-search-bin
makepkg
sudo pacman -U e-search-bin-*-1-x86_64.pkg.tar.zst
```

##### [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR)

````{tab} yay
```sh
yay -S umi-ocr-bin
```
````

````{tab} From releases
Get `Umi-OCR_Linux_Paddle_*.tar.xz` from [Umi-OCR - Releases](https://github.com/hiroi-sora/Umi-OCR/releases).

```sh
tar -xf Umi-OCR_Linux_Paddle_*.tar.xz
mv Umi-OCR_Linux_Paddle_* Umi-OCR_Linux_Paddle
./umi-ocr.sh
```
````

##### [Goldendict](https://github.com/goldendict/goldendict)

````{tab} pacman
```sh
sudo pacman -S goldendict-git
```
````

````{tab} From releases
Download `goldendict-1_1.5.0-3-x86_64.pkg.tar.zst`, `qt5-webkit-5.212.0alpha4-22-x86_64.pkg.tar.zst` from https://sourceforge.net/projects/fabiololix-os-archive/files/Packages/

```sh
sudo pacman -U qt5-webkit-5.212.0alpha4-22-x86_64.pkg.tar.zst
sudo pacman -U goldendict-1_1.5.0-3-x86_64.pkg.tar.zst
yay -Ql goldendict
```
````

##### [Rofi](https://github.com/davatorium/rofi)

```sh
sudo pacman -S rofi
```

###### [rofi-shortcuts](https://github.com/Zeioth/rofi-shortcuts) (Optional)

````{tab} From source
```sh
git clone --depth=1 https://github.com/Zeioth/rofi-shortcuts
cd rofi-shortcuts
mkdir -p ~/.config/rofi/rofi-shortcuts/
mkdir -p ~/.local/share/rofi/rofi-shortcuts/
cp ./rofi-shortcuts.conf ~/.config/rofi/rofi-shortcuts/rofi-shortcuts.conf
cp ./rofi-shortcuts.sh ~/.local/share/rofi/rofi-shortcuts/rofi-shortcuts.sh
chmod u+x ~/.local/share/rofi/rofi-shortcuts/rofi-shortcuts.sh
ln -sf ~/.local/share/rofi/rofi-shortcuts/rofi-shortcuts.sh ~/.local/bin/rofi-shortcuts
```
````

```sh
rofi-shortcuts
```

###### [rofi-calc](https://github.com/svenstaro/rofi-calc) (Optional)

```sh
sudo pacman -S rofi-calc
rofi -show calc -modi calc -no-show-match -no-sort
```

###### [Rofimoji](https://github.com/fdw/rofimoji)

```sh
sudo pacman -S rofimoji
```

###### [rofi-copyq](https://github.com/cjbassi/rofi-copyq)

```sh
git clone --depth=1 https://github.com/cjbassi/rofi-copyq
cd rofi-copyq
./rofi-copyq
```

##### [AHK_X11](https://github.com/phil294/AHK_X11) (Cache)

```sh
yay -S ahk_x11-bin
```

##### [keymapper](https://github.com/houmain/keymapper) (Wait)

```sh
yay -S keymapper
sudo systemctl enable --now keymapperd
```

##### [Input Leap](https://github.com/input-leap/input-leap) (Optional)

```sh
yay -S input-leap-git
input-leap
```

On Client PC, install [Barrier](https://github.com/debauchee/barrier).

##### [WeChat](https://flathub.org/apps/com.tencent.WeChat)

```sh
flatpak install flathub com.tencent.WeChat
```

##### Photoshop CC (Cache)

- [Photoshop CC v19 installer for Linux](https://github.com/Gictorbit/photoshopCClinux)
- [error: sorry something went wrong during download photoshopCC-V19.1.6-2018x64.tgz](https://github.com/Gictorbit/photoshopCClinux/issues/175)
- [Dropbox link to download photoshopCC-V19.1.6-2018x64.tgz is broken](https://github.com/Gictorbit/photoshopCClinux/issues/40)

#### Reference

- [Desktop entries](https://wiki.archlinux.org/title/desktop_entries)

[^1]: [alarm login?](https://github.com/altreact/archbk/issues/9)
[^2]: [Network configuration/Wireless](https://wiki.archlinux.org/title/Network_configuration/Wireless)
[^3]: [10 Things You MUST DO After Installing Arch Linux (2023)](https://www.youtube.com/watch?v=odgD_RdJjCU)
[^4]: [USTC Mirror Help - Arch Linux](https://mirrors.ustc.edu.cn/help/archlinux.html)
[^5]: [Localization/Simplified Chinese](https://wiki.archlinux.org/title/Localization/Simplified_Chinese)
[^6]: [hosts](https://man.archlinux.org/man/hosts.5)
[^7]: [[Bug]: "SSL peer certificate or SSH remote key was not OK" during extra-data download, only on Ubuntu-based distros](https://github.com/flatpak/flatpak/issues/5253)
[^8]: [enable SSH on Arch Linux](https://medium.com/@pythonaugust/enable-ssh-on-arch-linux-8f1ede0d9c88)
[^9]: [Install XFCE Desktop on Arch Linux](https://linuxopsys.com/topics/install-xfce-desktop-on-arch-linux)
[^10]: [How to Use i3 with XFCE](https://www.youtube.com/watch?v=nZTBxJ_gr8w)
[^11]: [Sway on Arch Linux: 2023 Edition (From Scratch)](https://www.youtube.com/watch?v=QAmTUkzpIiM)
[^12]: [Set dark theme on dolphin in cinnamon](https://forum.manjaro.org/t/set-dark-theme-on-dolphin-in-cinnamon/122034/7)
[^13]: [Arch linux install lightdm (Light Display Manager)](https://gist.github.com/miguelmota/5087fb8d92599efc4748c134846c8daf)
[^14]: [A minimal LightDM WebKit2 theme](https://github.com/TheTerrior/lightdm-minimal)
[^15]: [How to Change Linux Console Fonts on Arch Linux](https://www.youtube.com/watch?v=nxUTnZVdS64)
[^16]: [Linux console - Fonts](https://wiki.archlinux.org/title/Linux_console#Fonts)
[^17]: [Bluetooth headset connection occasionally fails: br-connection-page-timeout](https://www.reddit.com/r/archlinux/comments/qnffce/bluetooth_headset_connection_occasionally_fails/)
[^18]: [How to Set up Bluetooth in Arch Linux](https://www.jeremymorgan.com/tutorials/linux/how-to-bluetooth-arch-linux/)
[^19]: [Bluetooth not working on computer](https://www.linuxquestions.org/questions/linux-hardware-18/bluetooth-not-working-on-computer-4175724971/)
[^20]: [Using USB drives on Arch](https://ejmastnak.com/tutorials/arch/usb/)
[^21]: [Can't create freshclam.dat in /usr/local/share/clamav](https://docs.clamav.net/faq/faq-freshclam.html#cant-create-freshclamdat-in-usrlocalshareclamav)