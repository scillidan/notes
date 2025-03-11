### [BeatPrints](https://github.com/TrueMyst/BeatPrints)

1. Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create app `BeatPrints`, add `http://localhost` on `Redirect URIs (required)`.
3. Go `Settings`, get `Client ID`, `Client secret`.
4. Add `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET` into PATH.

```sh
git clone --depth=1 https://github.com/TrueMyst/BeatPrints
cd BeatPrints
uv venv
.venv\Scripts\activate.bat
uv pip install -e .
uv pip install python-dotenv
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

#### Resource

- [Add new themes to BeatPrints](https://github.com/TrueMyst/BeatPrints/issues/25)
- [beatprints_from_csv.py](https://gist.github.com/scillidan/203fd0ce69800709e4c3057404f813be)

[^1]: [CLI Setup](https://beatprints.readthedocs.io/en/latest/guidebook/cli.html)