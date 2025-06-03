### [linkding](https://github.com/sissbruecker/linkding)

````{tab} From source [^1]
```sh
git clone --depth=1 https://github.com/sissbruecker/linkding
cd linkding
nvm install 18.*
nvm use 18.*
npm install
npm run build
```

```sh
uv venv
.venv\Scripts\activate.bat
uv python -m pip install -r requirements.txt
uv python -m pip install -r requirements.prod.txt
uv pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --username=<user> --email=<email>
```

Just test:

```sh
npm run dev
```

```sh
# Open a new terminial window
python manage.py runserver 8002
```

Visit `http://localhost:8002`.
````

````{tab} Windows 10 [^2]
How to autorun when Windows 10 startup?

1. Create `start_linkding.bat`:
  ```batchfile
  @echo off

  cd linkding
  set LD_SUPERUSER_NAME=<user>
  set LD_SUPERUSER_PASSWORD=<password>
  start npm run dev
  timeout 5
  start .venv\Scripts\python.exe manage.py runserver 8002

  pause
  ```
2. Create `start_linkding.vbs`:
  ```vbs
  Set WshShell = CreateObject("WScript.Shell")
    WshShell.Run chr(34) & "start_linkding.cmd" & Chr(34), 0
  Set WshShell = Nothing
  ```
3. Create shortcut of `start_linkding.vbs`.
4. Put the shortcut into `C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`.
````

````{tab} Ubuntu 22 ARM [^3]
```sh
npm install -g concurrently
cp requirements.dev.txt requirements.dev.txt.bak
vim requirements.dev.txt
```

```
rcssmin
```

```sh
vim package.json
```

```json
{
  "scripts": {
    "start": "concurrently \"rollup -c -w\" \"python manage.py runserver 0.0.0.0:8060\""
```

```sh
pm2 start npm --name "linkding" -- run start
pm2 save
```
````

### Browser Extension

Visit `127.0.0.1:8002` → Settings → Integrations → Integrations → REST API → Copy this

- [linkding extension](https://github.com/sissbruecker/linkding-extension) → Configuration
  ```
  Base URL `http://127.0.0.1:8002`
  API Authentication Token `<token>`
  ```
- [linkding injector](https://github.com/fivefold/linkding-injector)

[^1]: [Development](https://github.com/sissbruecker/linkding#development)
[^2]: [linkding - Setup](https://github.com/sissbruecker/linkding/blob/master/README.md#setup)
[^3]: [ModuleNotFoundError: No module named 'ruamel'](https://github.com/fair-workflows/nanopub/issues/106)