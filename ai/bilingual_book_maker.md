### [bilingual_book_maker](https://github.com/yihong0618/bilingual_book_maker)

```sh
git clone --depth=1 https://github.com/yihong0618/bilingual_book_maker
cd bilingual_book_maker
uv venv
.venv\Scripts\activate.bat
uv pip install -r requirements.txt
python make_book.py --book_name file.epub --ollama_model llama3.1
```