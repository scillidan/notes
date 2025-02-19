### [LinguaCafe](https://github.com/simjanos-dev/LinguaCafe) (Cache)

#### Selfhost

````{tab} Docker compose [^1]
```sh
mkdir linguacafe
cd linguacafe
wget https://raw.githubusercontent.com/simjanos-dev/LinguaCafe/refs/heads/main/docker-compose.yml
mkdir storage
sudo docker compose up -d
```

1. Visit `http://<your_host>:9191`
2. Create first/admin user, then login-in with it
3. Admin settings → Languages → Chinese → Install
````

[^1]: [Updating to the latest version](https://github.com/simjanos-dev/LinguaCafe#updating-to-the-latest-version)
[^2]: [Importing dictionaries](https://github.com/simjanos-dev/LinguaCafe/wiki/2.-Setup#importing-dictionaries)