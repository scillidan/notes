### Lobe Chat Server Database

#### Deploy with docker compose [^1]

```sh
mkdir lobe-chat-db
cd lobe-chat-db
bash <(curl -fsSL https://lobe.li/setup.sh) -l en
```

In terminal, you can see:

```
Security secret generation results are as follows:
LobeChat:
  - URL: http://localhost:3210
  - Username: user
  - Password: <password>
Casdoor:
  - URL: http://localhost:8000
  - Username: admin
  - Password: <password>

Minio:
  - URL: http://localhost:9000
  - Username: admin
  - Password: <password>
```

Remember them.

```sh
# cp .env .env.bak
# vim .env
# sed -i -e 's/3210/3310/g' -e 's/9000/9100/g' -e 's/9001/9101/g' -e 's/8000/8100/g' .env
# sed -i 's/localhost/<your_host>/g' .env
sudo docker compose up -d
```

````{tab} Ubuntu 22 ARM (Cache) [^2]
1. Visit `http://<your_host>:8100/login`. Login with `Username`, `Password`
2. Casdorr → Identity → Applications → LobeChat → Edit
3. Redirect URLs → Add → `http://<your_host>:3310/api/auth/callback/casdoor` → Save & Exit
4. Visit `http://<your_host>:3310` → User ># Login / Sign up → Admin (Admin)
5. Visit `http://<your_host>:9100`. Login with `YOUR_MINIO_USER`, `YOUR_MINIO_PASSWORD`
6. Minio → Buckets → Create Bucket → `casdoor`
7. `casdoor` bucket → Summary → Access Policy → Edit → Access Policy → Custom → Copy form [here](https://lobehub.com/docs/self-hosting/server-database/docker-compose#unable-to-log-in-properly) → Set
8. Minio → Access Keys → Create access key → Create → Download for import
9. Casdoor → Identity → Providers → Add:
    ```
    Name `minio`
    Display name `minio`
    Organization `admin (Shared)`
    Category `Storage`
    Type `MinIO`
    Client ID `<access_key>`
    Client secret `<secret_key>`
    Endpoint `http://<your_host>:9100`
    Bucket `casdoor`
    Path prefix `casdoor`
    Domain `http://<your_host>:9100`
    Provider URL `http://<your_host>:9100`
    ```
10. Casdoor → Identity → Applications → LobeChat → Edit → Providers → Add → Select `minio` → Save & Exit
````

#### Deploy with Vercel

- [Deploying Server Database Version on Vercel](https://lobehub.com/docs/self-hosting/server-database/vercel)

[^1]: [Deploying LobeChat Server Database Version with Docker Compose](https://lobehub.com/docs/self-hosting/server-database/docker-compose)
[^2]: [Unable to Log In Properly](https://lobehub.com/docs/self-hosting/server-database/docker-compose#unable-to-log-in-properly)
[^3]: [[Bug] 向量化失败](https://github.com/lobehub/lobe-chat/issues/4111)
[^4]: [[Bug] 使用clerk生产环境，预览知识库文件报错 Error: Clerk: auth() was called but Clerk can't detect usage of clerkMiddleware()](https://github.com/lobehub/lobe-chat/issues/6762)