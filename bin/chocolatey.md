# [Chocolatey](https://docs.chocolatey.org/en-us/) [^1]

As Administrator:

```pwsh
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

[^1]: [Installing Chocolatey CLI](https://docs.chocolatey.org/en-us/choco/setup/#installing-chocolatey-cli)