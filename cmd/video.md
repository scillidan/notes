### Video

```sh
# ass to srt
ass2srt $1.ass
```

```sh
# encode
av1an -i $1 -v "--cpu-used=3 --end-usage=q --cq-level=30 --threads=8" -w 10 --target-quality 95 -a "-c:a libopus -b:a 192k -ac 2" -l _.log -o _.mp4
```

```sh
# encode
handbrakecli --preset-import-file <preset.json> --input $1 --output _.mp4
```

```sh
# match film name
mnamer -b .
```

```sh
# rename subtitle files
sub-batch rename --subarea ".+"
```

```sh
# rename subtitle files and synchronize subtitles to videos
sub-batch alass
```

```sh
# rename subtitle files and synchronize subtitles with mpv
sub-batch time-mpv
```

```sh
# srt to vtt
srt-vtt $1
```

```sh
# subtitle ocr
rapid_videocr -vsf "C:\Users\User\Usr\Opt\VideoSubFinder\Release_x64\VideoSubFinderWXW.exe" -video_dir $1
```

```sh
# sup to srt
dotnet PgsToSrt.dll --input $1.sup --output _.srt --tesseractlanguage <language> --tesseractdata "C:\Users\User\Usr\Data\tessdata_fast"
```

```sh
# take thumbnail
mt -n 16 -c 4 --disable-timestamps --header=false $1
```

```sh
# take thumbnail
mtn -c 4 -r 4 -g 3 -k 000000 -w 1920 -i -t -D 4 -P -o _mtn.png $1
```

```sh
# take thumbnail
vcsi -w 1920 --metadata-position hidden $1
```

```sh
# take animated video contact sheets
vimg vcs -c4 -n16 -H270 --avif-fps=20 $1
```

```sh
# vtt to srt
vtt_to_srt $1
```

```sh
# with kamite
mpv --input-ipc-server=/./pipe/kamite-mpvsocket --sub-file=$2 --sid=2 --secondary-sid=1 --secondary-sub-visibility=no --save-position-on-quit $1
```