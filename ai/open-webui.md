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
      - "8050:8080"
    environment:
      OLLAMA_BASE_URL: http://<your_host>:11434
    volumes:
      - .data:/app/backend/data
    restart: always
```

```sh
sudo docker compose up -d
```

Visit `http://<your_host>:8050`, wait a few minutes for it to complete initialization.
````

#### Reference

- [Tutorial: Configuring RAG with Open WebUI Documentation](https://docs.openwebui.com/tutorials/tips/rag-tutorial/)
- [Add Open WebUI as a Custom Search Engine](https://docs.openwebui.com/tutorials/integrations/browser-search-engine/#step-2-add-open-webui-as-a-custom-search-engine)