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
ollama pull llama3.1
# ollama pull gemma3
ollama pull qwen2.5-coder:3b
ollama pull qwen2.5-coder:7b
ollama pull nomic-embed-text
ollama list
```
````

If you used on local network, add these into PATH [^3]:

```
OLLAMA_HOST=0.0.0.0
OLLAMA_ORIGINS=*
```

#### Cross-reference

- [continue.md](https://scillidan.github.io/notes/opt/continue.html)
- [immersive-translate.md](https://scillidan.github.io/notes/opt/brave/immersive-translate.html)

[^1]: [Running Ollama on the Raspberry Pi](https://pimylifeup.com/raspberry-pi-ollama)  
[^2]: [Run LLMs Locally on Raspberry Pi Using Ollama AI](https://itsfoss.com/raspberry-pi-ollama-ai-setup/)
[^3]: [Ollama Connection issues FAQ help](https://github.com/Mintplex-Labs/anything-llm/issues/1640)