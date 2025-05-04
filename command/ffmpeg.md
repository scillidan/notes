### [FFmpeg](https://www.ffmpeg.org/)

```sh
# export subtilte
ffmpeg -i $1 -map 0:s:0 _.srt
```

```sh
# export subtilte
ffmpeg -i $1 -map 0:s:0 -c:s copy _.sup
```

```sh
# gif to mp4
ffmpeg -i $1.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" _.mp4
```

```sh
# image to video
ffmpeg -framerate 1 -i $04d.png -c:v libx264 -r 30 -pix_fmt yuv420p _.mp4
```

```sh
# image to video
ffmpeg -framerate 30 -i $04d.png -c:v libx264 -pix_fmt yuv420p _.mp4
```

```sh
# image to video
ffmpeg -loop 1 -i $1.jpg -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -t 1 -pix_fmt yuv420p _.mp4
```

```sh
# m4a to mp3
ffmpeg -i $1 -c:a libmp3lame -q:a 8 _.mp3
```

```sh
# m4a to mp3
ffmpeg -i $1 -vn -c:a libmp3lame -b:a 224K -ac 2 _.mp3
```

```sh
# creat poster from video
ffmpeg -i $1.mp4 -vframes 1 _poster.jpg
``

```sh
# aac to mp3
ffmpeg -i $1 -codec:a libmp3lame -qscale:a 1 _.mp3
```

```sh
# to mp3
ffmpeg -i $1 -map 0:a:0 -c:a copy _.mp3
```

```sh
# to mp4
ffmpeg -i $1 -map 0 -c:v copy -c:a ac3 -b:a 256K -ac 2 -c:s copy _.mp4
```

```sh
# to ogg
ffmpeg -i $1 -map_metadata -1 -c:a libvorbis -b:a 64k -compression_level 10 -vn _.ogg
```