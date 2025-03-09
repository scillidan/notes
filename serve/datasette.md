### [Datasette](https://datasette.io)

#### Selfhost [^1]

```sh
mkdir <dir>
cd <dir>
uv venv
.venv\Scripts\activate.bat
uv pip install datasette
uv pip install datasette-sitemap datasette-block-robots datasette-backup datasette-search-all datasette-render-images datasette-media datasette-render-markdown datasette-multiline-links datasette-external-links-new-tabs datasette-copyable datasette-publish-vercel
# uv pip install datasette-parquet 
# pipx install sqlite-utils
# sqlite-utils insert database.db table table.csv --csv
# sqlite-utils drop-table database.db table
# sqlite-utils enable-fts database.db table column_1 column_2
datasette serve database.db
datasette serve database_1.db database_2.db -m metadata.yml
```

#### Deploy to Vercel [^3]

Create `.github/workflows/vercel.yml`

```yaml
name: Deploy to Vercel
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18.x'
      - name: Install Vercel CLI
        run: npm i -g vercel
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install datasette datasette-sitemap datasette-block-robots datasette-backup datasette-search-all datasette-render-images datasette-media datasette-render-markdown datasette-multiline-links datasette-external-links-new-tabs datasette-copyable datasette-publish-vercel
      - name: Deploy Datasette using Vercel
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
        run: |-
          datasette publish vercel database_1.db database_2.db \
            --metadata metadata.yml \
            --token $VERCEL_TOKEN \
            --project database
```

Vercel → Project `database` → Settings → Build and Deployment → Node.js Version → 18.x

#### Resource

- [Datasette charcoal theme](https://github.com/julien040/charcoal-datasette-theme)
- [datasette-block-robots](https://github.com/simonw/datasette-block-robots)
- [datasette-sitemap](https://github.com/simonw/datasette-sitemap)
- [datasette-search-all](https://github.com/simonw/datasette-search-all)
- [Configuring FTS using sqlite-utils](https://docs.datasette.io/en/stable/full_text_search.html#configuring-fts-using-sqlite-utils)
- [datasette-render-markdown](https://github.com/simonw/datasette-render-markdown)
- [datasette-external-links-new-tabs](https://github.com/ocdtrekkie/datasette-external-links-new-tabs)
- [datasette-multiline-links](https://github.com/simonw/datasette-multiline-links)

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
[^3]: [datasette-publish-vercel](https://github.com/simonw/datasette-publish-vercel)