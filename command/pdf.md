### PDF

```sh
# analysis
python pdf_pdfalyzer.py $1
```

```sh
# html to epub
paperoni $1 --export epub
```

```sh
# html to epub
percollate epub $1 -o _.epub
```

```sh
# html to pdf
percollate pdf $1 -o _.pdf --css ":root { --main-font: 'Beholden Medium';  --code-font: 'Beholden Medium'; --alt-font: 'Beholden Medium'; }"
```

```sh
# signature
java -jar batchpdfsign-portable.jar -k <file.pfx> -p <password> -i $1 -o _sig.pdf
```

```sh
# signature
java -jar open-pdf-sign.jar --input $1 --output _sig.pdf --certificate <file.crt> --key <file.pem> --passphrase <password> --page -1 --locale zh-CN
```

```sh
# toc
pdf-toc -t _pdf -d _toc.txt $1
```

```sh
# watermark
markpdf $1 mark.png --opacity=0.3
```