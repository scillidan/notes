### [ImageMagick](https://www.imagemagick.org/)

```sh
# annotate
magick convert $1 -undercolor #00000075 -fill #FFFFFF -gravity NorthWest -font "C:\Users\User\Git\_\Nerd-Sarasa-Merge\MonaspiceNeNFP-SarasaGothicSC-WFMSansSC.ttf" -pointsize 20 -interline-spacing 2 -annotate +10+10 $2 _.png
```

```sh
# border
magick convert $1 -bordercolor #000 -border 1 $2
```

```sh
# bmp to png
magick mogrify -format png $1
```

```sh
# charcoal
magick convert $1 -charcoal 2 $2
```

```sh
# complementary color
magick convert $1.png -channel RGB -negate _.png
```

```sh
# crop
magick convert $1.png -crop x1500 _%d.png
```

```sh
# dither
magick convert $1 -ordered-dither h4x4o -colors 8 $2
```

```sh
# dither
magick convert $1 -colorspace Gray -ordered-dither o2x2 $2
```

```sh
# montage tile 1x
magick montage $1 -resize 750x -geometry +0+0 -tile 1x _.png
```

```sh
# montage tile x1
magick montage $1 -density 300 -tile x1 -geometry +1+1 -background #000 _.png && magick convert -border 1 -bordercolor #000 -strip -interlace Plane -quality 0.85 _.png _.jpg
```

```sh
# paint
magick convert $1 -paint 3 $2
```

```sh
# preview
magick convert -size $2 -background #000000 -fill #fffff8 -font "C:\Users\User\Git\_\Nerd-Sarasa-Merge\MonaspiceNeNFP-SarasaGothicSC-WFMSansSC.ttf" -gravity Center -pointsize 20 -interline-spacing 2 caption:$3 $1.png
```

```sh
# resize
magick convert $1 -resize x1600 -quality 100 _.jpg
```

```sh
# sketch
magick convert $1 -colorspace gray -sketch 0x10+120 $2
```

```sh
# to pdf
magick convert "*.{png,jpeg}" -quality 100 _.pdf
```