### [Material for MkDocs](https://github.com/squidfunk/mkdocs-material)

```sh
mkdir <site>
cd <site>
uv venv
.venv\Scripts\activate.bat
uv pip install mkdocs-material
mkdocs new .
subl config.yaml
```

```yaml
theme:
  name: material
```

#### Reference

- [Pymdown extensions dependency issue](https://github.com/squidfunk/mkdocs-material/issues/5526)
- [Changing the logo and icons](https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/)
- [Embedding external files](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#embedding-external-files)
- [mkdocs-table-reader-plugin](https://timvink.github.io/mkdocs-table-reader-plugin/)