# [Local Deep Researcher](https://github.com/langchain-ai/local-deep-researcher) (Cache)

```sh
git clone --depth=1 https://github.com/langchain-ai/local-deep-researcher
cd local-deep-researcher
uv venv --python 3.11
.venv\Scripts\activate.bat
uv pip install -e .
uv pip install -U "langgraph-cli[inmem]"
cp .env.example .env
```

Edit `.env`.

```sh
langgraph dev
```