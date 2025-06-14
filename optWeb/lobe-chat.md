# [Lobe Chat](https://github.com/lobehub/lobe-chat)

![](https://img.shields.io/github/license/lobehub/lobe-chat?style=flat-square)

````{tab} From source [^1]
```sh
git clone --depth=1 https://github.com/lobehub/lobe-chat
cd lobe-chat
pnpm install
# pnpm add next@latest
# pnpm dev
set NODE_OPTIONS=--max-old-space-size=4096
pnpm build
pnpm start
# pm2 start pnpm --name lobe-chat -- run start
```
````

````{tab} Docker compose [^2]
```sh
mkdir lobe-chat
cd lobe-chat
vim docker-compose.yml
```

Copy from [here](https://lobehub.com/docs/self-hosting/platform/docker-compose#run-docker-compose-deployment-command).

```sh
sudo docker compose up -d
```
````

## Deploy with Vercel

- [Deploy LobeChat with Vercel](https://lobehub.com/docs/self-hosting/platform/vercel)

## Reference

- [Crontab Automatic Update Script (Optional)](https://lobehub.com/docs/self-hosting/platform/docker-compose#crontab-automatic-update-script-optional)
- [[Bug] Ollama service is unavailable](https://github.com/lobehub/lobe-chat/issues/2337)  
- [Hitting a Wall Trying to get Ollama to work with LobeChat or any other app (works fine in CLI in the container)](https://www.reddit.com/r/unRAID/comments/1ccxqu6/hitting_a_wall_trying_to_get_ollama_to_work_with/)

[^1]: [Project Setup](https://github.com/lobehub/lobe-chat/wiki/Setup-Development)
[^2]: [Docker Compose Deployment Guide](https://lobehub.com/zh/docs/self-hosting/platform/docker-compose)