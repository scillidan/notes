### [Dolt](https://www.dolthub.com/)

1. Get `dolt-windows-amd64.zip` from [Dolt - Releases](https://github.com/dolthub/dolt/releases).
2. Decompress it to `dolt\`.

````{tab} Ubuntu 22 ARM
Get `dolt-linux-arm64.tar.gz` from [Dolt - Releases](https://github.com/dolthub/dolt/releases).

```sh
tar -xzvf dolt-linux-arm64.tar.gz
chmod +x dolt-linux-arm64/bin/dolt
ln -s ~/dolt-linux-arm64/bin/dolt ~/.local/bin/dolt
```
````

```sh
dolt config --global --add user.email "user@example.com"
dolt config --global --add user.name "username"
dolt login
```

```sh
mkdir database_1
cd database_1
dolt init
dolt remote add origin scillidan/database_1
dolt table import --create-table --pk column_1 table_1 table_1.csv
dolt add table_1
dolt commit -m "add table_1"
# dolt status
# dolt pull origin main
dolt push origin main
```