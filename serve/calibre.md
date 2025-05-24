### [Calibre](https://calibre-ebook.com/)

#### Selfhost

````{tab} Windows 10
1. Calibre → Preferences → Sharing → Sharing over ht net → The port on which to listen for connections `<port>`
2. Calibre → Connect → share → Start Content server

PS: I can't add books with `calibredb add <Book> --with-library <calibre_data>` when `calibre-server.exe --port <port> <calibre_data>` running.
````

````{tab} Docker compose [^1]
```sh
mkdir calibre
cd calibre
vim docker-compose.yml
```

Copy from [here](https://docs.linuxserver.io/images/docker-calibre/#docker-compose-recommended-click-here-for-more-info). And add volumes as books storage liked:

```sh
vim docker-compose.yml
```

```yaml
    volumes:
      - ./config:/config
      - /mnt/nvme/book:/book
      - /mnt/nvme/sambashare/audioebook:/audioebook
```

```sh
sudo docker compose up -d
```
````

1. Cabibre → Preferences → Sharing → Sharing over the net → Run server automatically when calibre starts (On) → Start server.
2. The opds serve is on `http://<your_host>:8081/opds`.
3. Calibre → Control bar → Enable Audio

#### Setting [^3][^4]

1. Calibre → Select your book → View → View with calibre E-book viewer
2. Stay at the top of the reader → Show controls → Preferences
3. Miscellaneous → Show a toolbar with the most useful actions (On) → Customize toolbar → Put you want into `Current actions` liked `Read aloud`, `Lookup words` → OK
4. Read aloud → Configure Read aloud → Text-to-Speech engine → `The Piper Neural Engine`
  - Voices → English → `libritts (United States) [High quality]` → Download voice
5. Lookup words → Add sources → Add:
  ```
  Name `etymonline.com`
  URL `https://www.etymonline.com/search?q={word}`
  ```
  ```
  Name `sliverdict_en`
  URL `http://<your_host>:2628/api/query/en/{word}`
  ```
  ```
  Name `sliverdict_zh`
  URL `http://<your_host>:2628/api/query/zh/{word}`
  ```
  ```
  Name `open-webui_librarian_zh`
  URL `http://<your_host>:<port>/?models=librarian%3Alatest-clone&q={word}`
  ```

#### Usage

1. Calibre → Get books → Configure → `Project Gutenberg` (Enable)
2. Title → Entry `<book_name>` → Search
3. Select a book → Enter → Check book format → Download
4. Select book → View → View with calibre E-book viewer

#### [Resource](https://www.dolthub.com/repositories/scillidan/resource/data/main/calibre)

#### Cross-reference

- [SilverDict](https://scillidan.github.io/notes/serve/silverdict.html)

[^1]: [linuxserver/calibre](https://docs.linuxserver.io/images/docker-calibre)
[^2]: [How To Install Calibre Server & Calibre Web On Ubuntu 22.04](https://kenfavors.com/code/how-to-install-calibre-server-calibre-web-on-ubuntu-22-04/)
[^3]: [How To Enable Sidebar in Calibre Ebook Viewer](https://www.youtube.com/watch?v=rJfbcTlvujQ)
[^4]: [Adding Dictionary In Calibre Ebook](https://www.youtube.com/watch?v=_lN1N90c8zw)
