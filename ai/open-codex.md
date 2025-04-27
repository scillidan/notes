### [Open Codex CLI](https://github.com/ymichael/open-codex)

````{tab} ArchWSL
```sh
pnpm i -g open-codex
```
````

#### Usage

```sh
git clone --depth=1 https://github.com/openai/openai-fm
cd openai-fm
open-codex --provider ollama --model qwen2.5-coder:7b
open-codex --provider ollama --full-context --model qwen2.5-coder:7b
```