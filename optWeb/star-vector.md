# [StarVector](https://github.com/joanrod/star-vector) [^1][^2] (Cache)

![](https://img.shields.io/github/license/joanrod/star-vector?style=flat-square)

```sh
git clone --depth=1 https://github.com/joanrod/star-vector
cd star-vector
conda create -n starvector python=3.11.3 -y
conda activate starvector
python -m pip install --upgrade pip wheel setuptools
set CUDA_PATH="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4"
pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu124
pip install -e .
# pip install -e ".[train]"
```

```sh
python -m starvector.serve.controller --host 127.0.0.1 --port 10000
```

And:

```sh
python -m starvector.serve.gradio_web_server --controller http://127.0.0.1:10000 --model-list-mode reload --port 7000
```

And:

```sh
pip install -U "huggingface_hub[cli]"
huggingface-cli login
# set HF_ENDPOINT=https://hf-mirror.com
python -m starvector.serve.model_worker --host 127.0.0.1 --controller http://127.0.0.1:10000 --port 40000 --worker http://127.0.0.1:40000 --model-path joanrodai/starvector-1.4b
```

[^1]: [Failed to Install flash-attn==2.7.4.post1 with ModuleNotFoundError: No module named 'torch' on Pre-Configured Image](https://github.com/huggingface/open-r1/issues/282)
[^2]: [Project installation is obscure and not working](https://github.com/joanrod/star-vector/issues/19)