### Uncategorized

```sh
# decompress
7z x $1 -p"<password>"
```

```sh
# font to webfont
webify --no-eot --no-svg $1 && cat $1 | ttf2woff2 > $1.woff2
```

```sh
# font latin subset
pyftsubset $1.ttf --output-file=$2.woff2 --flavor=woff2 --layout-features=* --unicodes="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
```

```sh
# komga-cover-extractor
cd C:\Users\User\Usr\Script\komga-cover-extractor && .venv\Scripts\python.exe komga_cover_extractor.py" $1
```

```
# PostgreSQL Query
SELECT * FROM <table> WHERE <row_1> LIKE '%<string>%' OR <row_2> LIKE '%<string>%' OR <row_3> LIKE '%<string>%';
```