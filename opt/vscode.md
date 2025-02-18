### [VS Code](https://code.visualstudio.com)

Settings → Features → Terminal → Edit in settings.json:

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
        },
    }
}
```