# [DevDocs](https://github.com/freeCodeCamp/devdocs)

````{tab} Windows 10
```sh
git clone --depth=1 https://github.com/freeCodeCamp/devdocs
cd devdocs
cp Gemfile Gemfile.bak
subl Gemfile
```

```
ruby '3.3.4'
```

```pwsh
rbenv install 3.3.4
rbenv shell 3.3.4
gem install bundler
bundle install
```

```sh
scoop install curl gzip
cd ...\Scoop\shims
cp gzip.exe gunzip.exe
cp gzip.shim gunzip.shim
```

```pwsh
bunder exec thor docs:list
bundle exec thor docs:download html
bundle exec rackup
```

Check `public\docs`.
````

````{tab} Docker compose [^3]
```sh
mkdir devdocs
cd devdocs
vim docker-compose.yml
```

```yaml
version: '3.8'

services:
  devdocs:
    image: ghcr.io/freecodecamp/devdocs:latest
    container_name: devdocs
    ports:
      - "9292:9292"
    restart: always
```

```sh
sudo docker compose up -d
```
````

[^1]: [Any pod command fails for lack of libcurl.dll on a Windows machine.](https://github.com/CocoaPods/CocoaPods/issues/9955)
[^2]: [Not installable on Windows](https://github.com/freeCodeCamp/devdocs/issues/1152)
[^3]: [Using Docker (Recommended)](https://github.com/freeCodeCamp/devdocs#using-docker-recommended)