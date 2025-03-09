### [Datasette](https://datasette.io)

#### Selfhost [^1]

```sh
mkdir <dir>
cd <dir>
uv venv
.venv\Scripts\activate.bat
uv pip install datasette
uv pip install datasette-sitemap datasette-block-robots datasette-backup datasette-search-all datasette-render-images datasette-media datasette-render-markdown datasette-multiline-links datasette-external-links-new-tabs datasette-copyable
# uv pip install datasette-parquet 
# pipx install sqlite-utils
# sqlite-utils insert database.db table table.csv --csv
# sqlite-utils drop-table database.db table
# sqlite-utils enable-fts database.db table column_1 column_2
datasette serve database.db
datasette serve database_1.db database_2.db -m metadata.yml
```

#### Resource

- [Datasette charcoal theme](https://github.com/julien040/charcoal-datasette-theme)
- [datasette-block-robots](https://github.com/simonw/datasette-block-robots)
- [datasette-sitemap](https://github.com/simonw/datasette-sitemap)
- [datasette-search-all](https://github.com/simonw/datasette-search-all)
- [Configuring FTS using sqlite-utils](https://docs.datasette.io/en/stable/full_text_search.html#configuring-fts-using-sqlite-utils)
- [datasette-render-markdown](https://github.com/simonw/datasette-render-markdown)
- [datasette-external-links-new-tabs](https://github.com/ocdtrekkie/datasette-external-links-new-tabs)
- [datasette-multiline-links](https://github.com/simonw/datasette-multiline-links)
- [datasette-publish-vercel](https://github.com/simonw/datasette-publish-vercel)

#### Resource cache

- [datasette-parquet](https://github.com/cldellow/datasette-parquet)
- [datasette-atom](https://github.com/simonw/datasette-atom)
- [datasette-write-ui](https://github.com/datasette/datasette-write-ui)
- [datasette-upload-csvs](https://github.com/simonw/datasette-upload-csvs)
- [datasette-insert](https://github.com/simonw/datasette-insert)
- [datasette-export](https://github.com/simonw/datasette-export)
- [datasette-mutable-downloads](https://github.com/cldellow/datasette-mutable-downloads)

[^1]: [Metadata](https://docs.datasette.io/en/stable/metadata.html)
[^2]: [sqlite-utils](https://github.com/simonw/sqlite-utils)