# [SubPlease-ZH](https://github.com/BorisNA/SubPlease-ZH) (Cache)

````{tab} From source
```sh
git clone --depth=1 https://github.com/BorisNA/SubPlease-ZH
cd SubPlease-ZH
pyenv install 3.9.9
pyenv shell 3.9.9
pip install -r requirements.txt
```
````

## Usage

1. Create folder liked `your_book\`.
2. Put `your_book.m4b`, `your_book.epub` into `your_book\`.
3. Check [here](https://github.com/kanjieater/SubPlz#sync) to get the supported file format.

```sh
python run.py -d your_book
python gen.py -d your_book
```