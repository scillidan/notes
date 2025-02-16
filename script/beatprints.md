### [BeatPrints](https://github.com/TrueMyst/BeatPrints)

1. Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create app `BeatPrints`, add `http://localhost` on `Redirect URIs (required)`.
3. Go `Settings`, get `Client ID`, `Client secret`.
4. Add `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET` into PATH.

```sh
git clone --depth=1 https://github.com/TrueMyst/BeatPrints
cd BeatPrints
uv.exe venv --python cpython-3.10.11-windows-x86_64-none
.venv\Scripts\activate.bat
uv pip install -e .
# uv pip install python-dotenv
```

```sh
beatprints
```

Optional [^1]:

```sh
mkdir C:\Users\User\AppData\Roaming\BeatPrints
subl C:\Users\User\AppData\Roaming\BeatPrints\config.toml
```

```toml
[general]
search_limit = 7
output_directory = "C:\\Users\\User\\Downloads"

[credentials]
client_id = "SPOTIFY_CLIENT_ID"
client_secret = "SPOTIFY_CLIENT_SECRET"
```

[^1]: [CLI Setup](https://beatprints.readthedocs.io/en/latest/guidebook/cli.html)