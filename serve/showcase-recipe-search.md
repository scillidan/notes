### [Instant Recipe Search](https://github.com/typesense/showcase-recipe-search) (Cache)

````{tab} Windows 10 (Cache)
```sh
git clone --depth=1 https://github.com/typesense/showcase-recipe-search
cd showcase-recipe-search
rbenv install 2.7.2
rbenv shell 2.7.2
gem install bundler -v 2.4.22
bundle install
corepack enable
cp yarn.lock yarn.lock.bk
rm yarn.lock
yarn install
yarn run typesenseServer
```

```sh
cp .env.development .env
set BATCH_SIZE=1000
yarn run indexer:transformDataset
yarn run indexer:importToTypesense
yarn start
```
````

````{tab} Arch
```sh
sudo pacman -S rbenv
rbenv init
```
````