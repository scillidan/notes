### [yt-dlp](https://github.com/yt-dlp/yt-dlp)

````{tab} scoop
```sh
scoop install yt-dlp
```
````

````{tab} pacman
```sh
sudo pacman -S yt-dlp
```
````

#### Install plugins[^1] (Optional)

````{tab} Windows 10
1. Get `yt-dlp-ChromeCookieUnlock.zip` from [release](https://github.com/seproDev/yt-dlp-ChromeCookieUnlock)
2. Decompress it to `yt-dlp-ChromeCookieUnlock\`
3. Move `yt-dlp-ChromeCookieUnlock\` into `C:\Users\User\AppData\Roaming\yt-dlg\plugins\`
````

#### Usage

```sh
yt-dlp -F <url_1>
yt-dlp -f <video_id>+<audio_id> <url_1>
yt-dlp -f bestvideo+bestaudio <url_1>
```

#### Record

```{eval-rst}
.. asciinema :: Z9w9zQTrS7IJ6wfbGZxrlN8pR
```

[^1]: [Installing Plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins)