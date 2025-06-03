### [Dify](https://github.com/langgenius/dify)

![](https://img.shields.io/github/license/langgenius/dify?style=flat-square)

````{tab} Docker compose [^1]
```sh
git clone --depth=1 https://github.com/langgenius/dify
cd dify/docker
cp .env.example .env
docker compose up -d
```

```sh
# Update
cd dify/docker
docker compose down
git pull origin main
docker compose pull
docker compose up -d
```
````

#### Create chatbot and knowledge bases [^2]

1. Dify → `<user>` → Settings → Model Provider
2. Ollama → Setup
    ```
    Model Name `llama3.1:8b`
    Base URL   `http://<host>:11434`
    ```
3. Ollama → Add Model
    ```
    Model Type `Text Embedding`
    Model Name `mxbai-embed-large:latest`
    Base URL   `http://<host>:11434`
    ```
    ```
    Model Type `Text Embedding`
    Model Name `jina/jina-embeddings-v2-base-en`
    Base URL   `http://<host>:11434`
    ```
4. OpenAI → Setup
    ```
    API Key  `<api_key>`
    API base `https://api.openai.com`
    ```
5. OpenAI → Show Models
6. Dify → Studio → Chatbot → Create from Blank
    ```
    APP icon & name `llama 3.1`
    ```
7. Studio → llama 3.1 → `<model>` CHAT → `llama3.1:8b`
8. Dify → Knowledge → Create Knowledge → Upload files → Save & Process → Go to Documents
    ```
    Index mode `Economical`
    ```
9. Studio → llama 3.1 → Context → Add → `<knowledge>`

#### Asset

- [Content Editing](https://dify101.com/market/claude-thinking-Content-Editing)
- [E-commerce Specialist](https://dify101.com/market/claude-thinking-E-commerce-Specialist)
- [ai-stemm-writing-supervisor](https://dify101.com/market/ai-stemm-writing-supervisor)
- [Data Analyst](https://dify101.com/market/claude-thinking-Data-Analyst)
- [Technical Support](https://dify101.com/market/claude-thinking-Technical-Support)
- [Translator](https://dify101.com/market/claude-thinking-Translator)
- [Educator](https://dify101.com/market/claude-thinking-Educator)
- [Child Psychotherapist](https://dify101.com/market/claude-thinking-Child-Psychotherapist)
- [Legal Assistant](https://dify101.com/market/claude-thinking-Legal-Assistant)
- [Insurance Claims Specialist](https://dify101.com/market/claude-thinking-Insurance-Claims-Specialist)
- [Cross-Platform Copywriting with Dify](https://dify101.com/market/url-to-cross-platform-copywriting-with-dify)
- [Wordplay](https://dify101.com/market/wordplay)
- [Claude Prompt: 汉语新解](https://dify101.com/market/hanyuxinjie)
- [Ancient Script Scholar](https://dify101.com/market/claude-thinking-Ancient-Script-Scholar)

[^1]: [Deploy with Docker Compose](https://docs.dify.ai/getting-started/install-self-hosted/docker-compose)
[^2]: [本地部署Dify基于Llama 3.1和OpenAI创建聊天机器人与知识库](https://dify101.com/market/marketing-copy-clone-machine)