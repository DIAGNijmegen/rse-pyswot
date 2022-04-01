# PySwot

[![CI](https://github.com/DIAGNijmegen/rse-pyswot/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/DIAGNijmegen/rse-pyswot/actions/workflows/ci.yml?query=branch%3Amain)
[![PyPI](https://img.shields.io/pypi/v/pyswot)](https://pypi.org/project/pyswot/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyswot)](https://pypi.org/project/pyswot/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python wrapper for [JetBrains/swot](https://github.com/JetBrains/swot).

  - Free software: Apache Software License 2.0

## Features

This library is a wrapper around
[JetBrains/swot](https://github.com/JetBrains/swot) and provides two
methods:

```python
>>> from pyswot import is_academic
>>> is_academic("user@ox.ac.uk")
True
>>> is_academic("user@gmail.com")
False
```

```python
>>> from pyswot import find_school_names
>>> find_school_names("user@ox.ac.uk")
['University of Oxford']
>>> find_school_names("user@gmail.com")
[]
```
