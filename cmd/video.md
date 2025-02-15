### Video

```sh
# ass to srt
ass2srt $1.ass
```

```sh
# handbrake
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
# vtt to srt
vtt_to_srt $1
```