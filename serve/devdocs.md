### [DevDocs](https://github.com/freeCodeCamp/devdocs)

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

1. Get `curl-*-win64-mingw.zip` from [curl for Windows](https://curl.se/windows/).
2. Decompress it to `curl\`.
3. `cp curl\bin\libcurl-x64.dll <RBENV_ROOT>\3.3.4-1\bin\libcurl.dll` [^1]. 


1. Get `Binaries` from [Gzip for Windows](https://gnuwin32.sourceforge.net/packages/gzip.htm).
2. Decompress it to `gzip\`.
3. Add `gzip\bin` into `PATH`.
4. `mklink gzip\bin\gunzip.exe gzip\bin\gzip.exe` [^2].

```pwsh
bundle exec thor docs:download bash
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