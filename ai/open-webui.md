### [Open WebUI](https://github.com/open-webui/open-webui)

````{tab} uv
```sh
uv venv python=3.11
.venv\Scripts\activate.bat
uv pip install open-webui
uv pip install hf_transfer
open-webui serve
```
````

````{tab} Docker compose
```sh
mkdir open-webui
cd open-webui
vim docker-compose.yml
```

```yaml
version: '3.8'

services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    ports:
      - "3000:8080"
    environment:
      OLLAMA_BASE_URL: http://<your_host>:11434
    volumes:
      - .data:/app/backend/data
    restart: always
```

```sh
sudo docker compose up -d
```
````

#### Reference

- [Tutorial: Configuring RAG with Open WebUI Documentation](https://docs.openwebui.com/tutorials/tips/rag-tutorial/)