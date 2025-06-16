# [GPi CASE 2](https://retroflag.com/gpi_case_2.html)

## Flash OS to SD card

1. Get [SD Memory Card Formatter](https://www.sdcard.org/downloads/formatter/). Use it to format SD card.
2. Get [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
3. Raspberry Pi Imager:
	1. Raspberry Pi Device → Raspberry Pi 4
	2. 请选择需要写入的操作系统 → Emulation and game OS → Recalbox / RetroPie
	3. 储存卡 → SD card
	4. Next

RetroPie used [EmulationStation](https://gitlab.com/es-de/emulationstation-de) as default frontend. Recalbox used [Modern](https://gitlab.com/es-de/themes/modern-es-de) theme for [ES-DE](https://gitlab.com/es-de/emulationstation-de).

## Reference

- [Placing games and other resources on network shares](https://gitlab.com/es-de/emulationstation-de/-/blob/master/USERGUIDE.md#placing-games-and-other-resources-on-network-shares)
- [Arcade manager](https://github.com/cosmo0/arcade-manager)
- [RetroArch asset server](https://github.com/NickHeap2/retroarch-asset-server)
- [Renpy Documentation - Raspberry Pi](https://www.renpy.org/doc/html/raspi.html)
- [FAQ - How can I recover my RetroPie after enabling the desktop OpenGL driver?](https://retropie.org.uk/docs/FAQ/#how-can-i-recover-my-retropie-after-enabling-the-desktop-opengl-driver)

## OS

```{include} gpi-case-2/recalbox.md
```
```{include} gpi-case-2/retropie.md
```

## Emulator [Löve](https://love2d.org/) (Experimental) [^1][^2] (Cache)

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

[^1]: [RetroPie Docs - Love](https://retropie.org.uk/docs/Love/)
[^2]: [PyGame LÖVE (love2d) in RecalBox](https://forum.recalbox.com/topic/19222/pygame-l%C3%B6ve-love2d-in-recalbox)