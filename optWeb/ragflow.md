### [RAGFlow](https://github.com/infiniflow/ragflow) (Cache)

![](https://img.shields.io/github/license/infiniflow/ragflow?style=flat-square)

````{tab} Docker compose
```sh
sysctl vm.max_map_count
sudo sysctl -w vm.max_map_count=262144
git clone --depth=1 https://github.com/infiniflow/ragflow
cd ragflow
sudo docker compose -f docker/docker-compose.yml up -d
docker logs -f ragflow-server
```
````