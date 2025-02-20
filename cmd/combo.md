### Combo

```sh
# print linkding bookmarks
linkding --url "<linkding_serve>" --token "<token>" bookmarks all -q $* | jq ".results[]" | ramda -c -o csv | xsv select id,tag_names,url,website_description | tidy-viewer -u 50
```

```sh
# print markdown table
curl -k https://raw.githubusercontent.com/scillidan/WALLPAP-ENG-resource/main/table.md | sd "\[\d{10}\]\(" "" | sd "(\)\|\S+subsc)" "|![](//img.shields.io/steam/subsc" | mdtable2csv | sd "//steamc" "https://steamc" | xsv select source,version,urlid | csview
```

```sh
# print colors
curl -k --remote-name-all -o - https://raw.githubusercontent.com/scillidan/color/main/data/{chinese-traditional-colors.md,china-tradition-color-monokuro.md,zhongguose.md,china-tradition-color-320.md,nipponcolors.md} | mdtable2csv | xsv select hex,spelling,name | tidy-viewer -D -a -e | coloro | less -R
```

```sh
# linkding-cli
# Need jq linkding-cli ramda-cli tidy-viewer xsv
linkding --url "http://127.0.0.1:8002" --token "<token>" bookmarks all -q $1 | jq ".results[]" | ramda -c -o csv | xsv select tag_names,url,website_title | tidy-viewer -u 45
```