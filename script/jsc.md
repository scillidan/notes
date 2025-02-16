### [Jackett Search Cli](https://github.com/rodrigo-sys/jsc)

````{tab} Ubuntu
```sh
sudo apt install jq fzf
git clone depth=1 https://github.com/rodrigo-sys/jsc
cd jsc
chmod +x jsc
```

1. jackett → Open Web UI → Copy API Key.
2. Edit `jsc`.

```
api_key='<api_key>'
url="http://<jackett_host>:9117/api/v2.0/indexers/all/results?apikey=$api_key"
```

```sh
jsc -t nyaa-si -s "chainsaw man"
jsc -t nyaa-si -s "chainsaw man" | xargs -n 1 -r aria2
```
````