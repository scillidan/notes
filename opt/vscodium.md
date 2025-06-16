# [VSCodium](https://vscodium.com/) / [VS Code](https://code.visualstudio.com)

Settings → Open Settings (JSON)

```sh
{
    "terminal.integrated.profiles.windows": {
        "Cmder": {
            "path": [
                "${env:windir}\\Sysnative\\cmd.exe",
                "${env:windir}\\System32\\cmd.exe"
            ],
            "args": [
                "/k C:\\Users\\User\\Usr\\Opt\\cmder_mini\\vendor\\init.bat"
            ]
        }
    },
    "terminal.integrated.defaultProfile.windows": "Cmder",
    "terminal.integrated.tabs.enableAnimation": false
}
```

## Reference

- [Extensions missing?](https://www.reddit.com/r/vscode/comments/kb0eb5/extensions_missing/)

## Cross-reference

- [godot-mcp](https://scillidan.github.io/notes/srv/godot-mcp.html)
- [mcp_godot_rag.md](https://scillidan.github.io/notes/srv/mcp_godot_rag.html)
- [n8n-mcp-server.md](https://scillidan.github.io/notes/srv/n8n-mcp-server.html)

## Resource

```{include} vscodium/ltex-ls-plus.md
```