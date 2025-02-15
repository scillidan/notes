### LobeChat Server Database

#### Docker Compose

```sh
mkdir Docker/lobe-chat-db
cd Docker/lobe-chat-db
bash <(curl -fsSL https://raw.githubusercontent.com/lobehub/lobe-chat/HEAD/docker-compose/local/setup.sh) -f
# echo 'MINIO_PORT=9002' > .env
sed -i 's/localhost/<your_host>/g' docker-compose.yml
sudo docker compose up -d
```

In terminal, you can see:

```
Casdoor:
    - Username: admin
    - Password: <password>
```

1. Visit `http://<your_host>:8000/login`. Login with `Username`, `Password`
2. Casdorr → Identity → Applications → LobeChat → Edit
3. Redirect URLs → Add → `http://<your_host>:3210/api/auth/callback/casdoor` → Save & Exit
4. Visit `http://<your_host>:3210` → User ># Login / Sign up → Admin (Admin)
5. Visit `http://<your_host>:9001`. Login with `YOUR_MINIO_USER`, `YOUR_MINIO_PASSWORD`
6. Casdoor → Administrator → Buckets → Create Bucket → `casdoor`
7. `casdoor` bucket → Summary → Access Policy → Edit → Access Policy → Custom → Copy form [here](https://lobehub.com/docs/self-hosting/server-database/docker-compose#configuring-min-io-s-3) → Set
8. Casdoor → Access Keys → Create access key → Create → Download for import
9. Visit `http://<your_host>:8000` → Identity → Providers → Add:
    ```
    Name `minio`
    Display name `minio`
    Organization `admin (Shared)`
    Category `Storage`
    Type `MinIO`
    Client ID `access_key`
    Client secret `secret_key`
    Endpoint `http://<your_host>:<minio_port>`
    Bucket `casdoor`
    Path prefix `casdoor`
    Domain `http://<your_host>:<minio_port>`
    Provider URL `http://<your_host>:<minio_port>`
    ```
10. Casdoor → Identity → Applications → LobeChat → Edit → Providers → Add → Select `minio` → Save & Exit

↪ [Deploying LobeChat Server Database Version with Docker Compose](https://lobehub.com/docs/self-hosting/server-database/docker-compose)  
↪ [[Bug] 无法使用管理员账号登录casdoor](https://github.com/lobehub/lobe-chat/issues/5098)