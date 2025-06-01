### [Sphinx](https://www.sphinx-doc.org/en/master/) [^1][^2]

```sh
mkdir <site>
cd <site>
uv venv
.venv\Scripts\activate.bat
uv pip install furo myst-parser
sphinx-quickstart
# make clean
make html
```

Or:

```sh
uv pip install sphinx-autobuild
sphinx-autobuild . _bulid
```

#### Reference

- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

#### [Resource](https://www.dolthub.com/repositories/scillidan/resource/data/main/sphinx)

[^1]: [Furo](https://github.com/pradyunsg/furo)
[^2]: [Markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html)