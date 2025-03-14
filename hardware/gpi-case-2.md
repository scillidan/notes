### [GPi CASE 2](https://retroflag.com/gpi_case_2.html)

#### Flash OS to SD card

1. Get [SD Memory Card Formatter](https://www.sdcard.org/downloads/formatter/). Use it to format SD card.
2. Get [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
3. Raspberry Pi Imager:
	1. Raspberry Pi Device → Raspberry Pi 4
	2. 请选择需要写入的操作系统 → Emulation and game OS → Recalbox / RetroPie
	3. 储存卡 → SD card
	4. Next

RetroPie used [EmulationStation](https://gitlab.com/es-de/emulationstation-de) as default frontend. Recalbox used [Modern](https://gitlab.com/es-de/themes/modern-es-de) theme for [ES-DE](https://gitlab.com/es-de/emulationstation-de).

#### Reference

- [Placing games and other resources on network shares](https://gitlab.com/es-de/emulationstation-de/-/blob/master/USERGUIDE.md#placing-games-and-other-resources-on-network-shares)
- [Arcade manager](https://github.com/cosmo0/arcade-manager)
- [RetroArch asset server](https://github.com/NickHeap2/retroarch-asset-server)
- [Renpy Documentation - Raspberry Pi](https://www.renpy.org/doc/html/raspi.html)
- [FAQ - How can I recover my RetroPie after enabling the desktop OpenGL driver?](https://retropie.org.uk/docs/FAQ/#how-can-i-recover-my-retropie-after-enabling-the-desktop-opengl-driver)

#### Emulator [Löve](https://love2d.org/) (Experimental) [^1][^2] (Cache)

1. Config → RetroPie Setup → Manage packages → Manage optional packages → love-0.10.2, love
2. `mv <game>.love <path>/roms/love/``

Some games:

Get `CurseOfTheArrow-V1.8.3-universal.love` form [Curse of the Arrow](https://egordorichev.itch.io/curse-of-the-arrow).

```sh
unzip CurseOfTheArrow-V1.8.3-universal.love -d CurseOfTheArrow-V1.8.3-universal
cd CurseOfTheArrow-V1.8.3-universal
vim conf.lua
```

```
t.window.width = 96*5
t.window.height = 64*5
t.window.minwidth = 96
t.window.minheight = 64
```

```sh
7z a -tzip CurseOfTheArrow-V1.8.3-universal-640x480.love *
mv CurseOfTheArrow-V1.8.3-universal-640x480.love <RetroPie>/home/pi/RetroPie/roms/love/
```

Get `Source code (zip)` from [mari0 - Releases](https://github.com/Stabyourself/mari0/releases).

```sh
unzip mari0-1.6.2.zip -d mari0-1.6.2
cd mari0-1.6.2/mari0-1.6.2
7z a -tzip mari0-1.6.2.love *
mv mari0-1.6.2.love <RetroPie>/home/pi/RetroPie/roms/love/
```

#### [Recalbox](https://www.recalbox.com/)

##### Enable SSH

1. Menu → Network Name → Enable WiFi → On
2. Network Name → <SSID>
3. WiFi Password → <Password> → Start
4. Connect with:
	```
	host `recalbox` (or ip-address)
	port `22`
	username `root`
	password `recalboxroot`
	```

#####  Update games lists

Menu → UI Settings → Update Games Lists

##### [Add a Bluetooth controller](https://wiki.recalbox.com/en/basic-usage/first-use-and-configuration):

Menu → Controller settings → Pair a bluetooth controller

##### [Add themes into frontend](https://wiki.recalbox.com/en/tutorials/frontend-customization/add-themes-into-emulationstation):

`share\themes

##### Hide preinstalled games

Menu → UI Settings → Game Filters → Hide Preinstalled Games

##### Transferring Roms

WinSCP → Synchronize:

```
Local directory `roms\`
Remote directory `/recalbox/share/roms`
Direction/Target directory `Remote`
Mode `Synchronize files`
Synchronize options `Preview changes`
Caomparion criteria `Modification time`
```

##### [Cave Story MD](https://github.com/andwn/cave-story-md)

1. Get `doukutsu-zh.bin.zip` from [Cave Story MD - Releases](https://github.com/andwn/cave-story-md/releases)
2. Copy it to `/recalbox/share/roms/megadrive/`

##### Reference

- [Gamelists](https://github.com/recalbox/recalbox-emulationstation/blob/master/GAMELISTS.md)
- [Netplay (online games)](https://wiki.recalbox.com/en/basic-usage/features/netplay-online-games)

#### [RetroPie](https://retropie.org.uk/)

Install display patch and safe-shutdown script:

1. Get `GPi_Case2_patch.zip` from [GPiCase2-Script](https://github.com/RetroFlag/GPiCase2-Script).
2. Decompress it to `GPi_Case2_patch\`.
3. Copy all files under `GPi_Case2_patch_retropie` to `<SD card>\`.
4. Run `Install_patch.bat`.

Create `gpi.sh`:

```sh
wget -O - "https://raw.githubusercontent.com/RetroFlag/GPiCase2-Script/main/retropie_install_gpi2.sh" | sudo bash
```

First Boot

1. Insert SD card into GPi Case 2, turn it on.
2. After first boot, hold a button to configure keymap. ou can hold down the button until it is be skipped.

##### Set Up WiFi

1. Configuration → WiFi → ... → Localisation Options → Set WiFi country → Save and exit
2. After reboot, connect to WiFi

##### Install safe-shutdown script [^3]

1. Configuration → File Manager → Edit `/etc/hosts`:
	```
	<ip>	github.com
	<ip>	raw.githubusercontent.com
	```
2. Reboot.
3. Configuration → File Manager → Run `/boot/gpi.sh`.

##### Enable SSH [^4][^5]

1. Configuration → Raspi-config → Interface Options → SSH → Yes
2. Connect with:
	```
	host `retropie` (or ip-address)
	port `22`
	username `pi`
	password `raspberry`
	```

##### Refresh the game listing

Menu → Quit → Restart EmulationStation

##### [Transferring Roms](https://retropie.org.uk/docs/Transferring-Roms/)

##### Enable Pegasus Frontend [^6]

System Menu → RetroPie Setup → Manage packages → Manage experimental packages → pegasus-fe → Install from pre-compiled binary

```sh
nano /opt/retropie/configs/all/autostart.sh
```

```sh
pegasus-fe
```

Reboot.

If you use other controllers:

- [Xbox 360](https://retropie.org.uk/docs/Xbox-360-Controller/)
- [Setting up an 8bitdo Bluetooth controller](https://retropie.org.uk/docs/8Bitdo-Controller/)
- [Virtual Gamepad](https://retropie.org.uk/docs/Virtual-Gamepad/)
- [Mobile Gamepad](https://github.com/sbidolach/mobile-gamepad)

[^1]: [RetroPie Docs - Love](https://retropie.org.uk/docs/Love/)
[^2]: [PyGame LÖVE (love2d) in RecalBox](https://forum.recalbox.com/topic/19222/pygame-l%C3%B6ve-love2d-in-recalbox)
[^3]: [Retro Gaming With RetroPie, GPi CASE 2, and a Raspberry Pi](https://navendu.me/posts/retropie-gpi-case-2-setup/)
[^4]: [RetroPie - SSH](https://retropie.org.uk/docs/SSH/)
[^5]: [RetroPie - SFTP](https://retropie.org.uk/docs/Transferring-Roms/#sftp)
[^6]: [Pegasus Docs - Platform Notes: Raspberry](https://pegasus-frontend.org/docs/user-guide/platform-raspberry/#retropie)