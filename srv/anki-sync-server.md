# [Anki Sync Server](https://docs.ankiweb.net/sync-server.html)

````{tab} Ubuntu 22 ARM [^1]
```sh
uv venv .anki-sync-server
source .anki-sync-server/bin/activate
uv pip install anki
export SYNC_HOST=0.0.0.0
export SYNC_PORT=8060
SYNC_USER1=<username>:<password> python -m anki.syncserver
```

Close it.

```sh
sudo vim /etc/systemd/system/anki-sync-server.service
```

```
[Unit]
Description=Anki Sync Server
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/path/to/.anki-sync-server
Environment="SYNC_USER1=<username>:<password>"
Environment="SYNC_USER1=SYNC_HOST=0.0.0.0"
Environment="SYNC_USER1=SYNC_PORT=8060"
ExecStart=/path/to/.anki-sync-server/bin/python -m anki.syncserver
Restart=always

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl enable --now anki-sync-server
```
````

## Cross-reference

- [anki.md](https://scillidan.github.io/notes/opt/anki.html)
- [ankidroid.md](https://scillidan.github.io/notes/opt/ankidroid.html)

[^1]: [With pip](https://docs.ankiweb.net/sync-server.html#with-pip)