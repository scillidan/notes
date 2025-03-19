### [mpv](https://mpv.io/)

````{tab} From source (Cache)
```sh
git clone --depth=1 https://github.com/mpv-player/mpv
cd mpv
git fetch --tags
git checkout v0.38.0
```
````

#### Note

- `mpv.exe` → 新建快捷方式 → 属性 → 快捷方式:
	```
	目标 `mpv.exe`
	起始位置 `mpv_config_dir_for_stream\`
	```

#### Reference

- [How to toggle second subtitles visibility?](https://www.reddit.com/r/mpv/comments/p2brpk/how_to_toggle_second_subtitles_visibility/)
- [Is it possible to make delete_file script remove file to recycle bin instead of permanently deleting the file?](https://github.com/zenyd/mpv-scripts/issues/29)
- [--sub-fonts-dir](https://mpv.io/manual/master/#subtitles)
- [mpv.conf](https://iamscum.wordpress.com/guides/videoplayback-guide/mpv-conf/)
- [ytdl_hook.lua should set http headers from yt-dlp when format_info is "youtube-dl (separate)"](https://github.com/mpv-player/mpv/issues/9978)
- [Support SOCKS5 proxies](https://github.com/mpv-player/mpv/issues/3373)