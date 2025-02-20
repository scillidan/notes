### [Perplexica](https://github.com/ItzCrazyKns/Perplexica)

````{tab} From source [^1]
```sh
git clone --depth=1 https://github.com/ItzCrazyKns/Perplexica
cd Perplexica/ui
cp .env.example .env
npm install
npm run build
cd ..
cp sample.config.toml config.toml
npm install
npm run build
```
````

You can edit `config.toml` to fill some fields liked:

```
[API_ENDPOINTS]
OLLAMA = "http://127.0.0.1:11434"
```

````{tab} Docker compose [^2]
```sh
git clone --depth=1 https://github.com/ItzCrazyKns/Perplexica
cd Perplexica
cp sample.config.toml config.toml
sudo docker compose up -d
```
````

[^1]: [How to Contribute to Perplexica](https://github.com/ItzCrazyKns/Perplexica/blob/master/CONTRIBUTING.md)
[^2]: [Getting Started with Docker (Recommended)](https://github.com/ItzCrazyKns/Perplexica#getting-started-with-docker-recommended)