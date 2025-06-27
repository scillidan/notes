# [Local RAG Chatbot](https://github.com/datvodinh/rag-chatbot) (Cache)

![](https://img.shields.io/github/license/datvodinh/rag-chatbot?style=flat-square)

````{tab} From source
```sh
# scoop install ollama ngrok
git clone --depth=1 https://github.com/datvodinh/rag-chatbot
cd rag-chatbot
uv venv
.venv\Scripts\activate.bat
uv pip install -e .
uv pip install hf_transfer
python -m rag_chatbot --host localhost & ngrok http 4321
```
````