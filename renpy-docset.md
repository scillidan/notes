## Environment

Windows10

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
doc2dash --name RenPy_Engine -f ./build/html
// then put `icon.png`, icon@2x.png` into `RenPy_Engine.docsets`
tar --exclude='.DS_Store' -cvzf RenPy_Engine.tgz RenPy_Engine.docset
trash RenPy_Engine.docset // scoop install trash
```

## Feed

dash-feed://http%3A%2F%2Fraw.githubusercontent.com%2Fscillidan%2Fgh-cos%2Fmain%2FRenPy_Engine.xml