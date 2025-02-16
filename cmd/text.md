### Text

```sh
# create serialized folders
cook volume $1-$2 | sd volume "\55 chapter" > _.md && mkdirs _.md && trash _.md
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
# to llm prompt
code2prompt $1.md --tokens --filter lua --output $1.md
```