# [Jackett Search Cli](https://github.com/rodrigo-sys/jsc) (Cache)

````{tab} Termux
```sh
pkg install jq fzf
git clone --depth=1 https://github.com/rodrigo-sys/jsc
cd jsc
cp jsc jsc.bak
```

1. Run `jackett`.
2. `http://<your_host>:9117` → API Key → Copy.

```sh
vim jsc
```

```
api_key='<api_key>'
```

```sh
chmod +x jsc
jsc -t nyaa-si -s "chainsaw man"
jsc -t nyaa-si -s "chainsaw man" | xargs -n 1 -r aria2
```
````

## Cross-reference

- [jackett.md](https://scillidan.github.io/notes/srv/jackett.html)