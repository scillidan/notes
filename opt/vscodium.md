### [VSCodium](https://vscodium.com/) / [VS Code](https://code.visualstudio.com)

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

#### Extension

##### [LTEX+](https://github.com/ltex-plus/ltex-ls-plus) [^1]

1. VSCodium → Extension → Search and install `LTeX+`
2. Get `ltex-ls-plus-*-windows-x64.zip` from [releases](https://github.com/ltex-plus/ltex-ls-plus/releases)
3. Decompress it to `ltex-ls-plus\`
4. VSCodium → Settings → Open Settings (JSON) → Add:
    ```
        "ltex.ltex-ls.path": "C:\\<full_path>\\ltex-ls-plus",
        "ltex.java.path": "C:\\<full_path>\\ltex-ls-plus\\jdk-21.0.5+11",
    ```
5. Restart VSCodium

[^1]: [First Alternative: Download the Offline Version of LTEX+](https://ltex-plus.github.io/ltex-plus/vscode-ltex-plus/installation-usage-vscode-ltex-plus.html#first-alternative-download-the-offline-version-of-ltex)

#### Cross-reference

- [Godot MCP](https://scillidan.github.io/notes/serve/godot-mcp.html)
- [A MCP server for Godot RAG](https://scillidan.github.io/notes/serve/mcp_godot_rag.html)
- [n8n MCP Server](https://scillidan.github.io/notes/serve/n8n-mcp-server.html)

#### Reference

- [Extensions missing?](https://www.reddit.com/r/vscode/comments/kb0eb5/extensions_missing/)