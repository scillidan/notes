### Combo

```sh
# curl, sd, mdtable2csv, xsv, csview
curl -k https://raw.githubusercontent.com/scillidan/WALLPAP-ENG-resource/main/table.md | sd "\[\d{10}\]\(" "" | sd "(\)\|\S+subsc)" "|![](//img.shields.io/steam/subsc" | mdtable2csv | sd "//steamc" "https://steamc" | xsv select source,version,urlid | csview
```

```sh
# curl, mdtable2csv, xsv, tidy-viewer, coloro, less
curl -k --remote-name-all -o - https://raw.githubusercontent.com/scillidan/color/main/data/{chinese-traditional-colors.md,china-tradition-color-monokuro.md,zhongguose.md,china-tradition-color-320.md,nipponcolors.md} | mdtable2csv | xsv select hex,spelling,name | tidy-viewer -D -a -e | coloro | less -R
```

```sh
# linkding-cli, jq, ramda-cli, xsv, tidy-viewer
linkding --url "http://127.0.0.1:8002" --token "<token>" bookmarks all -q $1 | jq ".results[]" | ramda -c -o csv | xsv select tag_names,url,website_title | tidy-viewer -u 45
```

```sh
# autocast, agg, ffmpeg
autocast $1.yaml $1.cast
agg --theme asciinema --speed 1.5 --font-family "JetBrainsMono Nerd Font Mono" --font-size 14 --fps-cap 30 $1.cast $1.gif
ffmpeg -i $1.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" $1.mp4
```