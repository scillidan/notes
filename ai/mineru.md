### [MinerU](https://github.com/opendatalab/MinerU)

#### Selfhost

````{tab} Docker compose [^1]
```sh
sudo pacman -S nvidia nvidia-utils nvidia-container-toolkit
docker pull quincyqiang/mineru
sudo docker run --rm -it --gpus=all -v /mnt/c/Users/<username>/Downloads:/data quincyqiang/mineru:0.1-models /bin/bash -c "echo 'source /opt/mineru_venv/bin/activate' >> ~/.bashrc && exec bash"
magic-pdf --help
```
````

[^1]: [quincyqiang/mineru](https://hub.docker.com/r/quincyqiang/mineru)