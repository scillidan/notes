# [Continue](https://github.com/continuedev/continue) [^1]

## Setting

- VSCode/VSCodium → Sidebar → Continue → Configure Continue:
  ```sh
  {
    "models": [
      {
        "apiBase": "http://127.0.0.1:11434/",
        "model": "qwen2.5-coder:7b",
        "provider": "ollama",
        "title": "Qwen2.5 Coder"
      }
    ],
    "tabAutocompleteModel": [
      {
        "title": "qwen2.5-coder:3b",
        "provider": "ollama",
        "model": "Qwen2.5 Coder 3B"
      }
    ]
  }
  ```

## Reference

- [开源 AI 编程工具（一） Continue](https://www.rectcircle.cn/posts/open-source-ai-code-tool-1-continue/)

[^1]: [Configuring Ollama and Continue VS Code Extension for Local Coding Assistant](https://dev.to/manjushsh/configuring-ollama-and-continue-vs-code-extension-for-local-coding-assistant-48li)