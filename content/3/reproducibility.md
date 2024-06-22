# Reproducible dependencies, environments, and workflows

:::{objectives}
- Learn how to document dependencies in Python.
- Discuss how to document dependencies in other languages.
- Each (non-trivial) Python project from now on should have a
  `requirements.txt` or `environment.yml` file.
:::


## Have you ever experienced the following?

1) You try to run a code or notebook and it cannot find a module?
```python
Traceback (most recent call last):
  File "/home/user/imgfilters/example.py", line 1, in <module>
    from imgfilters.filters import (
  File "/home/user/imgfilters/imgfilters/filters.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
```

2) You have installed the module but the code still does not work since it needs
   a different version of the module?

3) "It works on my machine &#129335;" but not on your machine?

:::{discussion}
- How do you install and use dependencies in your projects?
- How do you document them?
:::


## Tracking dependencies in Python

**There are two standard files to document dependencies in Python.**
Either use `requirements.txt` (together with pip) or `environment.yml` (Conda).

Let us study the [requirements.txt](https://github.com/coderefinery/imgfilters/blob/main/requirements.txt) from our project.
- How would we "pin" the versions?
- When should we "pin" the versions?

How would the corresponding `environment.yml` look like?
```yaml
name: imgfilters
channels:
  - conda-forge
dependencies:
  - python=3.12
  - numpy
  - scikit-image
  - scikit-learn
  - pywavelets
  - matplotlib
  - jupyterlab
```

**What if you don't remember which dependencies you have installed?**

Conda:
```bash
# list all dependencies and write them to file
$ conda env export > environment.yml

# omit detailed build information
$ conda env export --no-builds > environment.yml

# only list dependencies that were explicitly installed, not their dependencies
$ conda env export --from-history > environment.yml
```
pip:
```console
$ python -m pip freeze > requirements.txt
```

**My recommendation to install dependencies and document them at the same time:**
Document them first and then install from file:
```console
$ conda env create -f environment.yml
$ pip install -r requirements.txt
```


## What if I need to record the entire operating system?

(Here I will add an Apptainer example for our example project)


## Recording computational steps

We need a way to record and **communicate** computational steps:

- **README** (steps written out "in words")
- **Scripts** (typically shell scripts)
- **Notebooks** (Jupyter or R Markdown)
- **Workflows** (Snakemake, doit, ...)

:::{figure} img/kitchen/busy.png
:alt: Busy kitchen
:width: 50%
:::
[Midjourney, CC-BY-NC 4.0]


## More reading

- [Reproducible research](https://coderefinery.github.io/reproducible-research/)
- [The Turing Way: Guide for Reproducible Research](https://the-turing-way.netlify.app/reproducible-research/reproducible-research.html)
- [Ten simple rules for writing Dockerfiles for reproducible data science](https://doi.org/10.1371/journal.pcbi.1008316)
- [Computing environment reproducibility](https://doi.org/10.5281/zenodo.8089471)
