### [Ollama Deep Researcher](https://github.com/langchain-ai/ollama-deep-researcher) (Cache)

![](https://img.shields.io/github/license/langchain-ai/ollama-deep-researcher?style=flat-square)

````{tab} From source
```sh
git clone --depth=1 https://github.com/langchain-ai/ollama-deep-researcher
cd ollama-deep-researcher
cp .env.example .env
uv venv --python 3.11
.venv\Scripts\activate.bat
uv pip install -e .
uv pip install -U "langgraph-cli[inmem]"
langgraph dev
```
````