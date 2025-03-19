### [syncabook](https://github.com/r4victor/syncabook) (Cache)

````{tab} Build docker image
```sh
git clone --depth=1 https://github.com/r4victor/syncabook
cd syncabook
sudo docker build -t <user>/syncabook -f Dockerfile .
sudo docker run --rm -it <user>/syncabook:latest -h
```
````

````{tab} WSL (Cache)
```sh
sudo apt update
sudo apt install -y build-essential libssl-dev libbz2-dev libreadline-dev libsqlite3-dev libgdbm-dev liblzma-dev zlib1g-dev libffi-dev
sudo apt install espeak ffmpeg
pyenv install 2.7.18
pyenv shell 2.7.18
```
````

````{tab} Windows 10 [^1] (Cache)
Get `aeneas-win64-setup-*.exe` from [Aeneas Tools - Releases](https://github.com/sillsdev/aeneas-installer/releases).
````

````{tab} ArchWSL (Cache)
```sh
sudo pacman -S espeak-ng ffmpeg
git clone --depth=1 https://github.com/r4victor/syncabook
cd syncabook
uv venv
source .venv/bin/activate
uv pip install numpy aeneas afaligner
```
````

```sh
pip install pytest epubcheck
python -m pytest -s tests/
```

#### Usage

```sh
syncabook download_files <the_url> <the_book>
```

```sh
syncabook split_text --mode opening --p <the_index> <the_book>\text.txt <the_book>\plaintext
syncabook split_text --mode delimeter --p <the_index> <the_book>\text.txt <the_book>\plaintext
syncabook split_text --mode equal --n 2 <the_book>\text.txt <the_book>\plaintext
```

```sh
syncabook to_xhtml <the_book>/plaintext/ <the_book>/sync_text/
syncabook sync <the_book>/
```

```sh
syncabook create <the_book>
```

```sh
cd _synclibrivox\books\_little_prince\ // Cache
syncabook.exe split_text --m opening --p 第一章 text.txt plaintext
iconv -f gbk -t utf-8 plaintext\1.txt > plaintext\_1.txt && trash plaintext\1.txt && move plaintext\_1.txt plaintext\1.txt
syncabook.exe to_xhtml plaintext sync_text\
iconv -f gbk -t utf-8 sync_text\1.xhtml > sync_text\_1.xhtml && trash sync_text\1.xhtml && move sync_text\_1.xhtml  sync_text\1.xhtml
syncabook sync _synclibrivox\books\_little_prince
syncabook create <the_book>
```

... calibre-web → Apphabetical Books → ALL → `The Black Cat` → Import (EPUB)
My Books → `The Black Cat` → ButtonOfPlayAudio


[^1]: [Installing and using Aeneas](https://lingtran.net/Installing-and-using-Aeneas)
[^2]: [Audio Ebook ID Inserter](https://github.com/Audun97/audio-ebook-id-inserter)