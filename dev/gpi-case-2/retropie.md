# [RetroPie](https://retropie.org.uk/)

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

## Set Up WiFi

1. Configuration → WiFi → ... → Localisation Options → Set WiFi country → Save and exit
2. After reboot, connect to WiFi

## Install safe-shutdown script [^1]

1. Configuration → File Manager → Edit `/etc/hosts`:
	```
	<ip>	github.com
	<ip>	raw.githubusercontent.com
	```
2. Reboot.
3. Configuration → File Manager → Run `/boot/gpi.sh`.

## Enable SSH [^2][^3]

1. Configuration → Raspi-config → Interface Options → SSH → Yes
2. Connect with:
	```
	host `retropie` (or ip-address)
	port `22`
	username `pi`
	password `raspberry`
	```

## Refresh the game listing

Menu → Quit → Restart EmulationStation

## [Transferring Roms](https://retropie.org.uk/docs/Transferring-Roms/)

## Enable Pegasus Frontend [^4]

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

[^1]: [Retro Gaming With RetroPie, GPi CASE 2, and a Raspberry Pi](https://navendu.me/posts/retropie-gpi-case-2-setup/)
[^2]: [RetroPie - SSH](https://retropie.org.uk/docs/SSH/)
[^3]: [RetroPie - SFTP](https://retropie.org.uk/docs/Transferring-Roms/#sftp)
[^4]: [Pegasus Docs - Platform Notes: Raspberry](https://pegasus-frontend.org/docs/user-guide/platform-raspberry/#retropie)