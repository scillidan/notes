### [SilverDict](https://github.com/Crissium/SilverDict) (Cache)

```sh
git clone --depth=1 https://github.com/Crissium/SilverDict
cd client
yarn install
yarn build
mv build ../server/
```

```sh
cd ../server
uv venv
.venv\Scripts\activate.bat
uv pip install -r requirements.txt
uv pip install lxml
python server.py
# pm2 start server.py --name silverdict --interpreter "venv/Scripts/python.exe" --cwd "SilverDict/server" 
```

`localhost:2628` → Setting → Sources → add `your_path` then `Enter` → Wait for import.

In addition, some cache saved on `C:\Users\User\.silverdict` and `C:\Users\User\.cache\SilverDict`.