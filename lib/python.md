### [Python](https://www.python.org/)

````{tab} Ubuntu 22 ARM
- [How to Install Python 3.9 on Ubuntu 22.04](https://vegastack.com/tutorials/how-to-install-python-3-9-on-ubuntu-22-04/)
````

#### Publish python package [^1]

```sh
python -m pip install -e .
python -m pip install build twine
python setup.py sdist bdist_wheel
python -m build
```

[^1]: [How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/)