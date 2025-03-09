### [Ollama](https://ollama.com/)

````{tab} Ubuntu 22 ARM [^1][^2]
Get `ollama-linux-arm64.tgz` from [Ollama - Releases](https://github.com/ollama/ollama/releases).

```sh
tar -xvzf ollama-linux-arm64.tgz -C ollama
chmod +x ollama/bin/ollama
mv ollama/bin/ollama ~/.local/bin 
ollama serve
```

In new session:

```sh
ollama pull tinyllama
ollama run tinyllama
```
````

````{tab} Windows 10
```sh
scoop install ollama-full
ollama pull codellama 
ollama pull starcoder2:3b
# ollama pull starcoder2:7b
ollama pull nomic-embed-text
# ollama pull mxbai-embed-large
# ollama pull jina/jina-embeddings-v2-base-en
ollama pull qwen2.5:7b
ollama pull deepseek-r1:8b
ollama pull deepseek-coder:6.7b
ollama list
```
````

If you used on local network, add these into PATH [^3]:

```
OLLAMA_HOST=0.0.0.0
OLLAMA_ORIGINS=*
```

#### Cross-reference

- [Continue](https://scillidan.github.io/notes/ai/continue.html)
- [Immersive Translate](https://scillidan.github.io/notes/opt/immersive-translate.html)

[^1]: [Running Ollama on the Raspberry Pi](https://pimylifeup.com/raspberry-pi-ollama)  
[^2]: [Run LLMs Locally on Raspberry Pi Using Ollama AI](https://itsfoss.com/raspberry-pi-ollama-ai-setup/)
[^3]: [Ollama Connection issues FAQ help](https://github.com/Mintplex-Labs/anything-llm/issues/1640)