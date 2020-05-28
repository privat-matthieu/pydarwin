[Details](https://packaging.python.org/tutorials/packaging-projects/)

# Generating distribution archives

```bash
pip install --upgrade setuptools wheel
```

```bash
python setup.py sdist bdist_wheel
```

# Uploading

This requires a configured `~/.pypirc` file:

```
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
username = __token__
password = pypi-TOKEN_FROM_PYPI_WEBSITE
```

```bash
pip install --upgrade twine
```

```bash
python -m twine upload --repository pypi dist/*
```

# Next release

```bash
python setup.py sdist bdist_wheel
```

```bash
python -m twine upload --repository pypi dist/*
```