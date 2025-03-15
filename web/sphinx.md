### [Sphinx](https://www.sphinx-doc.org/en/master/) [^1][^2]

```sh
mkdir <site>
cd <site>
uv venv
.venv\Scripts\activate.bat
uv pip install furo myst-parser sphinx-copybutton sphinx-inline-tabs sphinx-external-toc sphinx-datatables sphinxcontrib.asciinema
sphinx-quickstart sphinx-autobuild
# uv pip install sphinxcontrib-mermaid
# make clean
make html
# sphinx-autobuild . _bulid
```

#### Reference

- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

#### [Resource](https://scillidan-datasette.vercel.app/resource/sphinx)

[^1]: [Furo](https://github.com/pradyunsg/furo)
[^2]: [Markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html)