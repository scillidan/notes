# [StarVector](https://github.com/joanrod/star-vector) (Cache)

![](https://img.shields.io/github/license/joanrod/star-vector?style=flat-square)

```sh
git clone --depth=1 https://github.com/joanrod/star-vector
cd star-vector
conda create -n starvector python=3.11.3 -y
conda activate starvector
pip install --upgrade pip
pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu121
pip install -e ".[train]"
```

```sh
python -m starvector.serve.controller --host 0.0.0.0 --port 10000
python -m starvector.serve.gradio_web_server --controller http://localhost:10000 --model-list-mode reload --port 7000
# pip install -U "huggingface_hub[cli]"
# huggingface-cli login
# pip install hf_transfer deepspeed
python -m starvector.serve.model_worker --host 0.0.0.0 --controller http://localhost:10000 --port 40000 --worker http://localhost:40000 --model-path joanrodai/starvector-1.4b
```