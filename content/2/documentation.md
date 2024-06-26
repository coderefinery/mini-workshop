# Code documentation

:::{objectives}
- Improve the README of our example project.
- Add [Sphinx](https://www.sphinx-doc.org/) documentation to the project.
- Deploy the result to [GitHub Pages](https://pages.github.com/).
:::


## Why? &#128151;&#9993;&#65039; to your future self

- You will probably use your code in the future and may forget details.
- You may want others to use your code (almost impossible without documentation).
- You may want others to contribute to the code.
- Time is limited - let the documentation answer FAQs.


## In-code documentation

Not very useful (more commentary than comment):
```python
# now we check if temperature is below -50
if temperature < -50:
    print("ERROR: temperature is too low")
```

More useful (explaining **why**):
```python
# we regard temperatures below -50 degrees as measurement errors
if temperature < -50:
    print("ERROR: temperature is too low")
```

Keeping zombie code "just in case" (rather use version control):
```python
# do not run this code!
# if temperature > 0:
#     print("It is warm")
```

Emulating version control:
```python
# John Doe: threshold changed from 0 to 15 on August 5, 2013
if temperature > 15:
    print("It is warm")
```


## Many languages allow "docstrings"

Example (Python):
```python
def kelvin_to_celsius(temp_k: float) -> float:
    """
    Converts temperature in Kelvin to Celsius.

    Parameters
    ----------
    temp_k : float
        temperature in Kelvin

    Returns
    -------
    temp_c : float
        temperature in Celsius
    """
    assert temp_k >= 0.0, "ERROR: negative T_K"

    temp_c = temp_k - 273.15

    return temp_c
```


## Often a README is enough - checklist

- **Purpose**
- Installation instructions
- Requirements
- **Copy-paste-able example to get started**
- Tutorials covering key functionality
- Reference documentation (e.g. API) covering all functionality
- Authors and **recommended citation**
- License
- Contribution guide

See also the
[JOSS review checklist](https://joss.readthedocs.io/en/latest/review_checklist.html).


## What if you need more than a README?

- Write documentation in
  [Markdown (.md)](https://en.wikipedia.org/wiki/Markdown)
  or
  [reStructuredText (.rst)](https://en.wikipedia.org/wiki/ReStructuredText)
  or
  [R Markdown (.Rmd)](https://rmarkdown.rstudio.com/)

- In the **same repository** as the code -> version control and **reproducibility**

- Use one of many tools to build HTML out of md/rst/Rmd:
  [Sphinx](https://sphinx-doc.org),
  [Zola](https://www.getzola.org/), [Jekyll](https://jekyllrb.com/),
  [Hugo](https://gohugo.io/), RStudio, [knitr](https://yihui.org/knitr/),
  [bookdown](https://bookdown.org/),
  [blogdown](https://bookdown.org/yihui/blogdown/), ...

- Deploy the generated HTML to [GitHub Pages](https://pages.github.com/) or
  [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/)


## Exercise/demo

:::{exercise}
- Open an issue and send a pull request (referencing the issue) which
  improves the README of the example project.
- We will together open a pull request from [a branch that adds Sphinx
  documentation](https://github.com/coderefinery/imgfilters/tree/radovan/documentation)
  and review it.
- We will verify that from there on documentation is built automatically by
  sending another pull request with a small change.
:::


## More resources

- [Documentation lesson material](https://coderefinery.github.io/documentation/)
- [Talk material "Documenting code" by S. Wittke](https://github.com/samumantha/documentation_example)
- Inside Sphinx we can add tables, images, equations, code snippets, ... ([more information](https://coderefinery.github.io/documentation/sphinx/#exercise-adding-more-sphinx-content).


## Optional: How to auto-generate documentation from docstrings in Python

Add the following highlighted lines to `conf.py`:
```{code-block} python
---
emphasize-lines: 6-10, 27-28
---
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

Instead of one command to build the documentation we now need two:
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
