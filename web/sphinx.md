### [Sphinx](https://www.sphinx-doc.org/en/master/)

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

- [Furo](https://github.com/pradyunsg/furo)
- [Markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html)
- [Sphinx Inline Tabs](https://github.com/pradyunsg/sphinx-inline-tabs)
- [sphinx-autobuild](https://github.com/sphinx-doc/sphinx-autobuild)
- [sphinx-copybutton](https://github.com/executablebooks/sphinx-copybutton)
- [sphinx-external-toc](https://github.com/executablebooks/sphinx-external-toc)
- [Sphinx DataTables](https://sharm294.github.io/sphinx-datatables/)
- [sphinxcontrib-asciinema](https://github.com/divi255/sphinxcontrib.asciinema)

#### Resource

- [autoclasstoc](https://autoclasstoc.readthedocs.io/en/latest/)
- [Read the Docs Sphinx Theme](https://github.com/readthedocs/sphinx_rtd_theme)
- [Sphinx Comments](https://github.com/executablebooks/sphinx-comments)
- [Sphinx Sitemap Generator Extension](https://github.com/jdillard/sphinx-sitemap)
- [sphinx-mdinclude](https://github.com/omnilib/sphinx-mdinclude)
- [sphinx-needs](https://github.com/useblocks/sphinx-needs)
- [sphinxcontrib-constdata](https://documatt.gitlab.io/sphinxcontrib-constdata/table.html)
- [sphinxcontrib-fulltoc](https://github.com/sphinx-contrib/fulltoc)
- [sphinxcontrib-mermaid](https://github.com/mgaitan/sphinxcontrib-mermaid)
- [sphinxcontrib-programoutput](https://github.com/OpenNTI/sphinxcontrib-programoutput)
- [sphinxcontrib.autoprogram](https://pythonhosted.org/sphinxcontrib-autoprogram/)

#### Note

```
# Heading in reStructuredText
H1 =
H2 -
H3 ~
H4 ^
H5 "
```