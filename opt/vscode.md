### [VS Code](https://code.visualstudio.com)

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