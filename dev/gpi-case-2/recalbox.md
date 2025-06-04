# [Recalbox](https://www.recalbox.com/)

## Enable SSH

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

## Update games lists

Menu → UI Settings → Update Games Lists

## [Add a Bluetooth controller](https://wiki.recalbox.com/en/basic-usage/first-use-and-configuration):

Menu → Controller settings → Pair a bluetooth controller

## [Add themes into frontend](https://wiki.recalbox.com/en/tutorials/frontend-customization/add-themes-into-emulationstation):

`share\themes`

## Hide preinstalled games

Menu → UI Settings → Game Filters → Hide Preinstalled Games

## Transferring Roms

WinSCP → Synchronize:

```
Local directory `roms\`
Remote directory `/recalbox/share/roms`
Direction/Target directory `Remote`
Mode `Synchronize files`
Synchronize options `Preview changes`
Caomparion criteria `Modification time`
```

## [Cave Story MD](https://github.com/andwn/cave-story-md)

1. Get `doukutsu-zh.bin.zip` from [Cave Story MD - Releases](https://github.com/andwn/cave-story-md/releases)
2. Copy it to `/recalbox/share/roms/megadrive/`

## Reference

- [Gamelists](https://github.com/recalbox/recalbox-emulationstation/blob/master/GAMELISTS.md)
- [Netplay (online games)](https://wiki.recalbox.com/en/basic-usage/features/netplay-online-games)