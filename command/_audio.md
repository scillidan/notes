### Audio

```sh
# download lyric
ZonyLrcTools.Cli.exe download -d "$1" -l -n 2
```

```sh
# download media from m3u8
m3u8 -u="$1" -o="_"
```

```sh
# generate waveform
audiowaveform -i $1 -o _.png -z auto -w 1920 -h 150 --background-color fffff8 --waveform-color 111111 --axis-label-color fffff8 --border-color fffff8
```

```sh
# mid to mp3
timidity $1 -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k _.mp3
```