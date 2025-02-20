### [LM Studio](https://lmstudio.ai/)

Discover → Select the LLM → Choose a download option → Check `Full GPU Offload Possible` → Download

#### Usage

- Chat → Select a model to load → Select the LLM
- Developer → Enable CORS (On) → Serve on Local Network (on) → Select a model to load → Start Server

#### Troubleshoot

1. Install LM Studio.
2. Go to `C:\Users\User\AppData\Local\LM-Studio\app-*\resources\app\.webpack\main`.
3. Find in folder, replace `huggingface.co` to `hf-mirror.com`.

[^1]: [LM Studio有魔法加持依然无法连网的解决办法](https://juejin.cn/post/7373961220585603124)