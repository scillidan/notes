### [Sage](https://github.com/Storia-AI/sage) (Cache)

````{tab} From source [^1]
```sh
git clone --depth=1 https://github.com/Storia-AI/sage
cd sage
uv venv --python cpython-3.10.16-linux-aarch64-gnu
source .venv/bin/activate
cp .sage-env .sage-env.bak
vim .sage-env
```

```
OLLAMA_BASE_URL=http://<your_host>:11434
```

```sh
uv pip install -e .
sage-index huggingface/transformers --mode=local
sage-chat huggingface/transformers --mode=local --llm-model llama3.1:8b
```
````

[^1]: [Get Started - Quickstart](https://sage-docs.storia.ai/quickstart)