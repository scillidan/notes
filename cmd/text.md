### Text

```sh
# create serialized folders
cook volume $1-$2 | sd volume "\55 chapter" > _.md && mkdirs _.md && trash _.md
```

```sh
# format json
prettier --write --paser json $1
```

```sh
# neovide
neovide --size=1250x720 --frame none --no-tabs -- -u "%LOCALAPPDATA%\nvim\init.lua" $*
```

```sh
# neovide with lunarvim
neovide --geometry 100x30 --notabs --frame none -- -u "%LUNARVIM_BASE_DIR%\init.lua" $*
```

```sh
# rst to markdown
pandoc $1 -f rst -t markdown -o _.md
```

```sh
# semantic grep
w2vgrep /C 2 /n /t 0.55 /m "C:\Users\User\Data\Model\googlenews-slim\GoogleNews-vectors-negative300-SLIM.bin" $1 /f $2
```

```sh
# to llm prompt
code2prompt $1.md --tokens --filter lua --output $1.md
```
