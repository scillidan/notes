### [Docker](https://www.docker.com/)

````{tab} Ubuntu 22/24 ARM [^1]
```sh
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
sudo apt-get update
sudo apt-get install ca-certificates wget
sudo install -m 0755 -d /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/docker.asc https://download.docker.com/linux/ubuntu/gpg
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
````

````{tab} Arch
```sh
sudo pacman -S docker
sudo systemctl enable --now docker.service
```
````

Change repository mirrors [^2][^6]:

```sh 
sudo mkdir -p /etc/docker
sudo vim /etc/docker/daemon.json
```

```
{
  "dns": ["8.8.8.8", "8.8.4.4"],
  "registry-mirrors": [
    "https://docker.1panel.top",
    "https://docker.1panel.live",
    "https://proxy.1panel.live",
    "https://dockerproxy.1panel.live"
  ],
  "experimental": true,
  "default-runtime": "nvidia",
  "runtimes": {
    "nvidia": {
      "path": "/usr/bin/nvidia-container-runtime",
      "runtimeArgs": []
    }
  }
}
```
````

```sh
sudo mkdir -p /etc/containers/registries.conf.d
sudo vim /etc/containers/registries.conf.d/docker.conf
```

```
unqualified-search-registries = ["docker.io"]

[[registry]]
location = "docker.io"

[[registry.mirror]]
location = "docker.1panel.top"
```

```sh
sudo systemctl daemon-reload
sudo systemctl restart docker
```

Just test [^4]:

```sh
sudo docker run -p 8080:80 --rm nginx
# sudo ufw allow 8080
```

Visit `http://<your_host>/8080`.

Test [^5]:

```sh
sudo docker run --gpus all nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
```

Some command to clear:

```sh
sudo docker image prune -a -f
sudo docker container prune -f
sudo docker volume prune -f
sudo docker network prune -f
sudo docker system prune -a --volumes -f
```

[^1]: [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
[^2]: [Docker / Podman 安装与换源](https://wcbing.top/linux/containers/install/)
[^3]: [How to Change Docker’s Default Data Directory](https://linuxiac.com/how-to-change-docker-data-directory/)
[^4]: [Docker Hub - Quickstart](https://docs.docker.com/docker-hub/quickstart/)
[^5]: [Container Runtime Initialization Errors](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#container-runtime-initialization-errors)
[^6]: [Using the NVIDIA Container Runtime for Docker](https://docs.nvidia.com/dgx/nvidia-container-runtime-upgrade/index.html#using-nv-container-runtime)