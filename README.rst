======
PySwot
======

.. image:: https://img.shields.io/pypi/v/pyswot.svg
        :target: https://pypi.python.org/pypi/pyswot

.. image:: https://github.com/DIAGNijmegen/rse-pyswot/workflows/CI/badge.svg
   :target: https://github.com/DIAGNijmegen/rse-pyswot/actions?query=workflow%3ACI+branch%3Amaster
   :alt: Build Status

.. image:: https://codecov.io/gh/DIAGNijmegen/rse-pyswot/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/DIAGNijmegen/rse-pyswot
   :alt: Code Coverage Status

Python wrapper for `JetBrains/swot`_.

* Free software: Apache Software License 2.0
* Documentation: https://pyswot.readthedocs.io.


Features
--------

This library is a wrapper around `JetBrains/swot`_ and provides two methods:

.. code-block:: python

    >>> from pyswot import is_academic
    >>> is_academic("user@ox.ac.uk")
    True
    >>> is_academic("user@gmail.com")
    False

.. code-block:: python

    >>> from pyswot import find_school_names
    >>> find_school_names("user@ox.ac.uk")
    ['University of Oxford']
    >>> find_school_names("user@gmail.com")
    []

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _`JetBrains/swot`: https://github.com/JetBrains/swot
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
