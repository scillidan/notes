## Dependence

```
scoop install make
pip install sphinx sphinx-rtd-theme sphinx-rtd-dark-mode
pip install doc2dash
```

## Start

```cmd
git clone https://github.com/renpy/renpy
cd renpy
git pull #sync to upstream
cd sphinx
make html
doc2dash -f ./build/html
mv "Ren'Py Visual Novel Engine.docset" "RenPy_Engine.docset"
tar --exclude='.DS_Store' -cvzf RenPy_Engine.tgz RenPy_Engine.docset
```