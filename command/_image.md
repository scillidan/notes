### Image

```sh
# cast to git
agg --theme 1F1F28,FFFFFF,1F1F28,D55FFF,A6E22E,F4BF75,66D9EF,AE81FF,A1EFE4,F8F8F2,75715E,D55FFF,A6E22E,F4BF75,66D9EF,AE81FF,A1EFE4,F9F8F5 --speed 1.5 --font-family "JetBrainsMono Nerd Font Mono" --font-size 14 --fps-cap 30 $1 _.gif
```

```sh
# cast to git
agg --theme asciinema --speed 1.5 --font-family "JetBrainsMono Nerd Font Mono" --font-size 14 --fps-cap 30 $1 _.gif
```

```sh
# color
paletter -colors <num> $1
```

```sh
# colorscheme
color-matcher -s $1 -r $2
```

```sh
# colorscheme
java -jar imagetheming/build/libs/ImageTheming.jar $1 -t=<theme>
```

```sh
# colorscheme
pyxelate $1 <output> --factor 9 --upscale 5 --palette 10 --nosvd
```

```sh
# crop
autocrop $1 _crop_$1 0.1
```

```sh
# crop face
autocrop -i pics -o crop -w 400 -H 400 -e png
```

```sh
# generate code block image
silicon --from-clipboard --language $1 --theme "tokyonight_moon" --font "'MonaspiceNe NFP + Sarasa Gothic SC + WFM Sans SC'=16" --no-window-controls --pad-horiz 0 --pad-vert 0 --background "#222436" --tab-width 2 --line-offset 0 --line-pad 4 --output _.png
```

```sh
# generate code block image
silicon --from-clipboard --language "Text" --font "'MonaspiceNe NFP + Sarasa Gothic SC + WFM Sans SC'=16" --no-window-controls --pad-horiz 0 --pad-vert 0 --background "#fffff8" --tab-width 2 --line-offset 0 --line-pad 4 --output _.png
```

```sh
# to ascii
ascii-image-converter $1 -C -b --dither -d 100,35
```

```sh
# to ascii
ascii-silhouettify --input $1
```

```sh
# to svg
magick convert $1 -define bmp:format=bmp3 _.bmp && autotrace -output-file _.svg -input-format bmp -despeckle-level <level> -color-count <num> _.bmp
```

```sh
# gif optimize
gifski -o _.gif $1
```

```sh
# gif optimize
gifski --width 600 --height 600 --fps 10 -o _.gif $1
```

```sh
# gif optimize
gifsicle -O3 --lossy=80 --resize-width 600 $1 -o _.gif
```

```sh
# gif optimize
gifsicle --lossy=80 -k 128 -O2 --keep-empty $1 -o _.gif
```

```sh
# png optimize
oxipng -o 4 -i 1 --strip safe *.png
```

```sh
# png to favicon
faviator --size 512 --text $1 --font-size 12 --font-family "Pridi" --font-color #000 --font-weight 400 --background-color #fff --border-width 0 --border-color 0 --border-radius 0 -o favicon.png
```

```sh
# png to favicon
favocon $1 -o ./favicon
```

```sh
# generate
node ./fishdraw/fishdraw.js --seed $1 --format smil --speed 2 > _.svg
```

```sh
# generate
node ./legumes/legc --format svg --stem-length 3 --title-text-size 28 --page-margin-x 120 $1 > _.svg
```

```sh
# png to ico
png-to-ico $1 > _.ico
```

```sh
# png to svg
png2svg -v -l -o $1 _.png
```

```sh
# remove background
rembg i -a -ae 15 $1 _.png
```

```sh
# svg to png
svg2png $1 -w <width>
```

```sh
# to svg
vtracer -i $1 -o _.svg
```

```sh
# video to ascii
video-to-ascii -f $1 --strategy ascii-color
```

```sh
# yoga image --resize 1920 $1 _.png
yoga image $1 _.png2
```