# Lobe Chat Server Database

![](https://img.shields.io/github/license/lobehub/lobe-chat?style=flat-square)

## Deploy with docker compose [^1]

```sh
mkdir lobe-chat-database
cd lobe-chat-database
# sudo rm -rf data
# sudo rm -rf s3_data
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

You can remember them.

```sh
vim docker-compose.yml
```

```sh
cp .env .env.bak
# sed -i -e 's/3210/3310/g' -e 's/9000/9100/g' -e 's/9001/9101/g' -e 's/8000/8100/g' .env
sed -i 's/localhos/<your_ip>/g' .env
```

```sh
sudo docker compose up -d
```

1. Visit `http://<your_ip>:8000`, login with `admin` and `<password>`
2. Casdorr → Identity → Applications → LobeChat → Edit
3. Redirect URLs → Add → `http://<your_ip>:3210/api/auth/callback/casdoor` → Save & Exit

## Build docker image [^4] (Cache)

```sh
git clone --depth=1 https://github.com/lobehub/lobe-chat
cd lobe-chat
```

Edit `Dockerfile.database` line `75`:

```
ENV NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY="pk_live_***" \
    CLERK_SECRET_KEY="sk_live_***" \
    CLERK_WEBHOOK_SECRET="whsec_****"
```

````{tab} ArchWSL
```sh
sudo docker build --memory=16g -t <user>/lobe-chat-database -f Dockerfile.database .
sudo docker save -o lobe-chat-database.tar <user>/lobe-chat-database:latest
```

Build image for Arm platform:

```sh
sudo pacman -S docker-buildx
# sudo docker buildx rm lobe-chat-database
sudo docker buildx create --name lobe-chat-database --use
sudo docker buildx inspect lobe-chat-database --bootstrap
sudo docker buildx build --platform linux/arm64 --memory=16g -t <user>/lobe-chat-database-arm:latest -f Dockerfile.database .
```
````

````{tab} Ubuntu 24 ARM
```sh
sudo docker build --memory=8g -t <user>/lobe-chat-database -f Dockerfile.database .
sudo docker save -o lobe-chat-database-arm.tar <user>/lobe-chat-database:latest
sudo chmod 644 lobe-chat-database-arm.tar
```

Move `lobe-chat-database-arm.tar` to server pc.

```sh
sudo docker load -i lobe-chat-database-arm.tar
```

```sh
mkdir lobe-chat-database
cd lobe-chat-database
bash <(curl -fsSL https://lobe.li/setup.sh) -l en
```

Remember the `username` and `password` displayed on the terminal.
````

## Deploy with Vercel

- [Deploying Server Database Version on Vercel](https://lobehub.com/docs/self-hosting/server-database/vercel)

## Troubleshoot [^1] (Cache)

1. Visit `http://<your_host>:8000/login`. Login with `Username`, `Password`
2. Casdorr → Identity → Applications → LobeChat → Edit
3. Redirect URLs → Add → `http://<your_host>:3210/api/auth/callback/casdoor` → Save & Exit
4. Visit `http://<your_host>:3210` → User ># Login / Sign up → Admin (Admin)
5. Visit `http://<your_host>:9000`. Login with `YOUR_MINIO_USER`, `YOUR_MINIO_PASSWORD`
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
    Endpoint `http://<your_host>:9000`
    Bucket `casdoor`
    Path prefix `casdoor`
    Domain `http://<your_host>:9000`
    Provider URL `http://<your_host>:9000`
    ```
10. Casdoor → Identity → Applications → LobeChat → Edit → Providers → Add → Select `minio` → Save & Exit

[^1]: [Deploying LobeChat Server Database Version with Docker Compose](https://lobehub.com/docs/self-hosting/server-database/docker-compose)
[^2]: [Unable to Log In Properly](https://lobehub.com/docs/self-hosting/server-database/docker-compose#unable-to-log-in-properly)
[^3]: [[Bug] 向量化失败](https://github.com/lobehub/lobe-chat/issues/4111)
[^4]: [[Bug] 使用clerk生产环境，预览知识库文件报错 Error: Clerk: auth() was called but Clerk can't detect usage of clerkMiddleware()](https://github.com/lobehub/lobe-chat/issues/6762)