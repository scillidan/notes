# [Vivliostyle CLI](https://github.com/vivliostyle/vivliostyle-cli)

```sh
mkdir <dir>
cd <dir>
pnpm add -g @vivliostyle/cli
vivliostyle init
```

Edit `vivliostyle.config.js` by yourself.

```sh
vivliostyle preview
```

You can refer to `.css` files in [vivliostyle_doc/samples](https://github.com/vivliostyle/vivliostyle_doc/tree/gh-pages/samples) or [kaigainotabi1](https://github.com/MurakamiShinyu/kaigainotabi1) to create your `style.css`.

PS: I don't know why, but sometimes after you use "vivliostyle preview", you need to used `Task Manager` to find and stop the (multi-) `chromium` process.

Build `html`, `epub`, `pdf`:

```sh
vivliostyle build
vivliostyle build --format epub -o <file>.epub
```

## Github Action

Build with Github Action, host on Github Pages:

1. Repository → Settings → Pages → Build and deployment → Github Actions
2. Edit `./github/workflows/action.yml`:

```
name: vivliostyle_gh-page

on:
  push:
    branches: ["gh-page"]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18.x'
      - name: Install Vivliostyle CLI
        run: npm install -g @vivliostyle/cli
      - name: Build Project
        run: vivliostyle build
      - name: Setup Pages
        uses: actions/configure-pages@v3
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: ./
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

Visit [Vivliostyle Viewer](https://vivliostyle.org/viewer/). Enter your `gh-pages` URL liked `https://<User>.github.io/<Repository>`.

## Reference

- [Option to use a specific Vivliostyle Viewer version or its URL](https://github.com/vivliostyle/vivliostyle-cli/issues/232)