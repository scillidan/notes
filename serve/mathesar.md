### [Mathesar](https://github.com/mathesar-foundation/mathesar) (Wait)

#### Selfhost

```sh
mkdir mathesar
cd mathesar
wget https://github.com/mathesar-foundation/mathesar/raw/0.2.0/docker-compose.yml
echo $(cat /dev/urandom | LC_CTYPE=C tr -dc 'a-zA-Z0-9' | head -c 50)
vim .env
```

```
SECRET_KEY=<secret_key>
```