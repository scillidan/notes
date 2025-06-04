# [postgresql](https://www.postgresql.org/) [^1]

````{tab} Ubuntu ARM
```sh
sudo apt install postgresql
sudo systemctl enable --now postgresql
sudo systemctl status postgresql
sudo vim /etc/postgresql/17/main/postgresql.conf
```

```
listen_addresses = '0.0.0.0'
```

```sh
sudo systemctl restart postgresql
sudo su postgres
```
````

[^1]: [Install and configure PostgreSQL](https://ubuntu.com/server/docs/install-and-configure-postgresql)