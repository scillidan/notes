### [RAGFlow](https://github.com/infiniflow/ragflow) (Cache)

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