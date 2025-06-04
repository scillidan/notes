# [n8n](https://n8n.io/)

````{tab} Docker compose [^1]
```sh
mkdir n8n
cd n8n
vim docker-compose.yml
```

Copy from [here](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/#5-create-docker-compose-file).And if serve port is already used, edit liked:

```yaml
services:
  traefik:
    command:
      - "--entrypoints.web.address=:8070"
      - "--entrypoints.websecure.address=:453"
    ports:
      - "8070:8070"
      - "453:453"
  n8n:
    images: n8nio/n8n
    ports:
      - "0.0.0.0:5678:5678"
    environment:
      - N8N_SECURE_COOKIE=false
```

```sh
sudo docker volume create n8n_data
sudo docker volume create traefik_data
sudo docker compose up -d
```
````

## Asset

- [Archive Spotify's discover weekly playlist](https://n8n.io/workflows/697-archive-spotifys-discover-weekly-playlist/)
- [Bulk Automated Google Drive Files Sharing and Direct Download Link Generation](https://n8n.io/workflows/2042-bulk-automated-google-drive-files-sharing-and-direct-download-link-generation/)
- [Create an RSS feed based on a website's content](https://n8n.io/workflows/1418-create-an-rss-feed-based-on-a-websites-content/)
- [Extract post titles from a blog](https://n8n.io/workflows/434-extract-post-titles-from-a-blog/)
- [Notion AI Assistant Generator](https://n8n.io/workflows/2415-notion-ai-assistant-generator/)
- [Scrape and summarize posts of a news site without RSS feed using AI and save them to a NocoDB](https://n8n.io/workflows/2180-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-them-to-a-nocodb/)
- [Backup workflows to GitHub](https://n8n.io/workflows/1222-backup-workflows-to-github/)
- [Backup your credentials to GitHub](https://n8n.io/workflows/2307-backup-your-credentials-to-github/)
- [Save your workflows into a Gitlab repository](https://n8n.io/workflows/2385-save-your-workflows-into-a-gitlab-repository/)
- [Monitor a file for changes and send an alert](https://n8n.io/workflows/967-monitor-a-file-for-changes-and-send-an-alert/)
- [Turn on a light to a specific color on any update in GitHub repository](https://n8n.io/workflows/1856-turn-on-a-light-to-a-specific-color-on-any-update-in-github-repository/)

[^1]: [Server setups - Docker-Compose](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/)