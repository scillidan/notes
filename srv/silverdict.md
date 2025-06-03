### [SilverDict](https://github.com/Crissium/SilverDict)

````{tab} Ubuntu 22 ARM
```sh
git clone --depth=1 https://github.com/Crissium/SilverDict
cd client
yarn install
yarn build
mv build ../server/
cd ..
uv venv
.venv/bin/activate
uv pip install -r server/requirements.txt
python server/server.py 0.0.0.0
```

```sh
sudo vim /etc/systemd/system/silverdict.service
```

```
[Unit]
Description=SilverDict
After=syslog.target network.target

[Service]
User=root
Group=root
WorkingDirectory=/home/<username>/SilverDict
ExecStart=/home/<username>/SilverDict/.venv/bin/python server/server.py 0.0.0.0

Restart=always
RestartSec=120

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl enable --now silverdict
```
````

````{tab} PM2 (Cache)
```sh
pm2 start server.py --name silverdict --interpreter "<path_to>/SilverDict/.venv/Scripts/python.exe" --cwd "<path_to>/SilverDict/server" 
```
````

````{tab} Docker compose (Cache)
```sh
mkdir silverdict
cd silverdict
touch docker-compose.yml
```

Copy form [here](https://github.com/Crissium/SilverDict/issues/20).

Or:

```sh
git clone --depth=1 https://github.com/Crissium/SilverDict
cd SilverDict
```

Then edit `docker-compose.yml` to add volumes:

```yaml
    volumes:
      - ./dictionaries/:/root/.silverdict/
      - ./cache/:/root/.cache/SilverDict/
      - /mnt/nvme/share/<your_dicts>:/<your_dicts>
```

```sh
sudo docker compose up -d
```
````

#### Usage

I did not test how to migrate dictionary data at present. So I import the dictionaries after enabling the service.

1. SilverDict → Setting → Library
	1. Dictionaries → Add
		 ```
		 Name `ecdict`
		 Filename `<path_to_dicts>/stardict-ecdict-2.4.2/stardict-ecdict-2.4.2.ifo`
		 Type `StarDict (.ifo)`
		 ```
		 ```
		 Name `汉语大词典(简体精排).mdx`
		 Filename `<path_to_dicts>/汉语大词典/汉语大词典(简体精排).mdx`
		 Type `MDict (.mdx)`
		 ```
	2. Do nothing until the import is complete
	3. Groups → Add:
		 ```
		 Group name `zh`
		 Group language(s) `zh`
		 ```
		1. `zh` → Edit dictionaries → `汉语大词典` (On)
		2. `Default Group` → Edit dictionaries → `汉语大词典` (Off)
	4. The `Sources` tab is used for batch import, I don't recommend using it at present.
2. Settings → Create n-gram index

#### Reference

- [Notes](https://github.com/Crissium/SilverDict/wiki/server#notes)
- [Enabling additional features](https://github.com/Crissium/SilverDict/wiki/general-notes#enabling-additional-features)
- [Running the server](https://github.com/Crissium/SilverDict/wiki/nginx#running-the-server)

#### Cross-reference

- [calibre.md](https://scillidan.github.io/notes/srv/calibre.html)