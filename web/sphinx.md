### [Sphinx](https://www.sphinx-doc.org/en/master/) [^1][^2]

```sh
mkdir <site>
cd <site>
uv venv
.venv\Scripts\activate.bat
uv pip install furo myst-parser sphinx-copybutton sphinx-inline-tabs sphinx-external-toc sphinx-datatables sphinxcontrib.asciinema sphinxext-photofinish sphinxcontrib-video sphinx-quickstart sphinx-autobuild
# make clean
make html
# sphinx-autobuild . _bulid
```

#### Reference

- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

#### [Resource](https://www.dolthub.com/repositories/scillidan/resource/data/main/sphinx)

[^1]: [Furo](https://github.com/pradyunsg/furo)
[^2]: [Markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html)