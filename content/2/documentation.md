# Code documentation

(work in progress)

```python
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# this is here so that the package can be imported by sphinx
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "imgfilters"
copyright = "2024, Authors"
author = "Authors"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

extensions = [
    "myst_parser",  # in order to use markdown
    "sphinx.ext.autodoc",  # to automatically document the code from docstrings
    "sphinx.ext.napoleon",  # to parse numpy-style docstrings
]

myst_enable_extensions = [
    "colon_fence",  # ::: can be used instead of ``` for better rendering
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
```

```console
$ sphinx-apidoc -o doc imgfilters
$ sphinx-build doc _build
```

Add to `index.md`:
```
:::{toctree}
:maxdepth: 2
:caption: API documentation

modules.rst
:::
```
