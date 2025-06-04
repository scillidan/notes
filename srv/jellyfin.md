# [Jellyfin](https://jellyfin.org/)

````{tab} Ubuntu 22 ARM [^1]
```sh
sudo dpkg -i jellyfin-server_10.9.11+ubu2204_arm64.deb jellyfin-web_10.9.11+ubu2204_all.deb
sudo dpkg -i jellyfin-ffmpeg6_6.0.1-8-jammy_arm64.deb
sudo systemctl enable --now jellyfin
systemctl status jellyfin
```
````

````{tab} Windows 10
```batchfile
@echo off

start jellyfin.exe --service
rem timeout 20
rem start jellyfin-mpv-shim\run.exe

pause
```
````

## Reference

- [Media - Movies](https://jellyfin.org/docs/general/server/media/movies/)
- [Plugins](https://jellyfin.org/docs/general/server/plugins/)

[^1]: [Installation - Linux](https://jellyfin.org/docs/general/installation/linux#linux-generic-amd64)