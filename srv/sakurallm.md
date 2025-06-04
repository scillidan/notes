# [SakuraLLM](https://github.com/SakuraLLM/SakuraLLM)

````{tab} From source [^1]
```sh
git clone --depth=1 https://github.com/SakuraLLM/SakuraLLM
cd SakuraLLM
uv pip install torch torchvision torchaudio xformers --index-url https://download.pytorch.org/whl/cu121
uv pip install -r requirements.llamacpp.txt
uv pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121
```
````

I used `q2k` of [Sakura-14B-Qwen2beta-v0.9.2-GGUF](https://huggingface.co/SakuraLLM/Sakura-14B-Qwen2beta-v0.9.2-GGUF). Put it into `models/`.

## Usage

As API [^2]:

```sh
python server.py --trust_remote_code --model_name_or_path models/sakura-13b-lnovel-v0.9b-Q2_K.gguf --model_version 0.9 --no-auth --llama_cpp --use_gpu --log debug
```

As CLI [^1]:

```sh
python translate_novel.py --trust_remote_code --model_name_or_path models/sakura-13b-lnovel-v0.9b-Q2_K.gguf --model_version 0.9 --no-auth --llama_cpp --use_gpu --log debug --text_length 512 --data_path <novel.txt> --output_path <novel_translated.txt>
```

```sh
python translate_epub.py --trust_remote_code --model_name_or_path models/sakura-13b-lnovel-v0.9b-Q2_K.gguf --model_version 0.9 --no-auth --llama_cpp --use_gpu --log debug --text_length 512 --data_path <novel.epub> --output_folder <novel_epub>
```

[^1]: [Sakura模型部署教程-本地运行-Transformers模型](https://github.com/SakuraLLM/tutorial/blob/main/tutorial-local-transformers.md)
[^2]: [各种推理引擎的使用说明](https://github.com/SakuraLLM/SakuraLLM/blob/main/usage.md)