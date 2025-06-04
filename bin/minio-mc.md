# [MinIO Client](https://min.io/docs/minio/linux/reference/minio-mc.html)

````{tab} Ubuntu 22 ARM
```sh
wget https://dl.min.io/client/mc/release/linux-arm64/mc
chmod +x mc
mv mc ~/.local/bin/
```

```sh
mkdir -p ~/minio_recursive
mc alias set <database_name> http://<your_host>:9000 <MINIO_ROOT_USER> <MINIO_ROOT_PASSWORD>
mc list <database_name>
mc cp --recursive <database_name>/ ~/minio_recursive/
```
````