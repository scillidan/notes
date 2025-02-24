### [MinerU](https://github.com/opendatalab/MinerU)

````{tab} Conda [^1]
```sh
conda create -n MinerU python=3.10
conda activate MinerU
pip install -U magic-pdf[full] --extra-index-url https://wheels.myhloli.com
pip install modelscope
wget https://gcore.jsdelivr.net/gh/opendatalab/MinerU@master/scripts/download_models.py -O download_models.py
python download_models.py
```
````

````{tab} Docker compose [^2]
```sh
sudo pacman -S nvidia nvidia-utils nvidia-container-toolkit
docker pull quincyqiang/mineru
sudo docker run --rm -it --gpus=all -v /mnt/c/Users/<username>/Downloads:/data quincyqiang/mineru:0.1-models /bin/bash -c "echo 'source /opt/mineru_venv/bin/activate' >> ~/.bashrc && exec bash"
magic-pdf --help
```
````

[^1]: [Windows10/11](https://github.com/opendatalab/MinerU/blob/master/docs/README_Windows_CUDA_Acceleration_zh_CN.md)
[^2]: [quincyqiang/mineru](https://hub.docker.com/r/quincyqiang/mineru)