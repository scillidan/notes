### [syncabook](https://github.com/r4victor/syncabook) (Cache)

````{tab} Docker
```sh
git clone --depth=1 https://github.com/r4victor/syncabook
cd syncabook
sudo docker build -t <user>/syncabook -f Dockerfile .
sudo docker run --rm -it <user>/syncabook:latest -h
```
````

````{tab} Build docker image
```sh
mkdir syncabook
cd syncabook
git clone --depth=1 https://github.com/scillidan/syncabook
git clone --depth=1 https://github.com/scillidan/afaligner
vim Dockerfile
```

```
FROM python:3.9-slim

RUN apt update -q \
    && apt install --no-install-recommends -yq espeak \
    libespeak-dev \
    ffmpeg \
    && apt install -yq gcc

RUN pip install --upgrade pip
RUN pip install numpy==1.23.4
RUN pip install pytest==7.1.3

WORKDIR /syncabook

COPY afaligner ./afaligner
COPY syncabook ./syncabook

RUN pip install -e afaligner
RUN pip install -r syncabook/requirements/base.txt
RUN pip install -e syncabook

WORKDIR /
ENTRYPOINT ["syncabook"]
```

```sh
sudo docker build -t <user>/syncabook -f Dockerfile .
sudo docker run --rm -it <user>/syncabook:latest -h
```
````

````{tab} Windows 10 (Cache)
Get `aeneas-win64-setup-*.exe` from [Aeneas Tools - Releases](https://github.com/sillsdev/aeneas-installer/releases).
````

```sh
cd books
mkdir alice_in_wonderland
cd alice_in_wonderland
mkdir plaintext
```

1. For example, download "Alice in Wonderland, Retold in Words of One Syllable" by Carroll and Gorham, the `Plain Text UTF-8` format from [Project Gutenberg](https://www.gutenberg.org/ebooks/19551), rename to `text.txt`
2. Download the corresponding book's vocal reading audio files from [LibriVox](https://librivox.org/alice-in-wonderland-retold-in-words-of-one-syllable-by-jc-gorham/), rename to `audio.zip`, then decompress to `audio/`
3. In `plaintext/`, create a `001_title.txt`
4. Open `text.txt`, cut all content that above chapter strings liked `CHAPTER I`, `ACT I` into `001_title.txt`

```sh
# syncabook download_files <url> <book>
syncabook split_text --mode opening --p <book_index> <book>\text.txt <book>\plaintext
# syncabook split_text --mode delimeter --p <book_index> <book>\text.txt <book>\plaintext
# syncabook split_text --mode equal --n 2 <book>\text.txt <book>\plaintext
syncabook to_xhtml <book>/plaintext <book>/sync_text
syncabook sync <book>
syncabook create <book>
```

For example:

```sh
sudo docker run --rm -v ~/Git/_/synclibrivox/books:/books -it scillidan/syncabook:latest split_text --mode opening --p CHAPTER books/alice_in_wonderland/text.txt books/alice_in_wonderland/plaintext
sudo docker run --rm -v ~/Git/_/synclibrivox/books:/books -it scillidan/syncabook:latest to_xhtml books/alice_in_wonderland/plaintext books/alice_in_wonderland/sync_text
sudo docker run --rm -v ~/Git/_/synclibrivox/books:/books -it scillidan/syncabook:latest sync books/alice_in_wonderland
sudo docker run --rm -v ~/Git/_/synclibrivox/books:/books -it scillidan/syncabook:latest create books/alice_in_wonderland
```

[^1]: [Installing aeneas - Linux](https://github.com/readbeyond/aeneas/blob/master/wiki/INSTALL.md#linux)