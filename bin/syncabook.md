### [syncabook](https://github.com/r4victor/syncabook) (Cache)

Get `aeneas-win64-setup-*.exe` [Aeneas Tools - Releases](https://github.com/sillsdev/aeneas-installer/releases).

- [Installing and using Aeneas](https://lingtran.net/Installing-and-using-Aeneas)

```sh
mkdir syncabook
cd syncabook
pvthon -m venv venv
venv\Scripts\activate.bat
```

```sh
git clone --depth=1 https://github.com/r4victor/afaligner
cd afaligner
pip install -e .
edit setup.py
cd ..
```

```sh
git clone --depth=1 https://github.com/r4victor/syncabook
cd syncabook
pip install beautifulsoup4 lxml numpy aeneas
```

See [Check out this ShareGPT conversation](https://sharegpt.com/c/97thh2m)

```sh
pip install pytest epubcheck
python -m pytest -s tests/
```

```sh
syncabook download_files theurl thebook
```

```sh
syncabook split_text --mode opening --p theindex thebook\text.txt thebook\plaintext
syncabook split_text --mode delimeter --p theindex thebook\text.txt thebook\plaintext
syncabook split_text --mode equal --n 2 thebook\text.txt thebook\plaintext
```

```sh
syncabook to_xhtml thebook/plaintext/ thebook/sync_text/
syncabook sync thebook/
```

```sh
syncabook create thebook
```

```sh
cd _synclibrivox\books\_little_prince\ // Cache
syncabook.exe split_text --m opening --p 第一章 text.txt plaintext
iconv -f gbk -t utf-8 plaintext\1.txt > plaintext\_1.txt && trash plaintext\1.txt && move plaintext\_1.txt plaintext\1.txt
syncabook.exe to_xhtml plaintext sync_text\
iconv -f gbk -t utf-8 sync_text\1.xhtml > sync_text\_1.xhtml && trash sync_text\1.xhtml && move sync_text\_1.xhtml  sync_text\1.xhtml
syncabook sync _synclibrivox\books\_little_prince
syncabook create thebook
```

... calibre-web → Apphabetical Books → ALL → `The Black Cat` → Import (EPUB)
My Books → `The Black Cat` → ButtonOfPlayAudio

- [Audio Ebook ID Inserter](https://github.com/Audun97/audio-ebook-id-inserter)

#### syncabook-like (TBD)

- [Package aeneas - language](https://www.readbeyond.it/aeneas/docs/language.html)