# CodeRefinery mini-workshop

:::{figure} index/astronaut.jpg
:alt: Series of images which come out of the image processing pipeline
:width: 100%

We will together create a simple image processing pipeline that is
reproducible, reusable, extensible, documented, and tested.  Celebrating
[Eileen Collins](https://en.wikipedia.org/wiki/Eileen_Collins), the first woman
to pilot the Space Shuttle and the first to command a Space Shuttle mission.
:::

- Example project: <https://github.com/coderefinery/imgfilters>
- Inspiration for this example: [scikit-image](https://scikit-image.org/docs/stable/auto_examples/index.html)
- This is a mini-version of the [CodeRefinery workshop](https://coderefinery.org/) (6 half-days) which we teach twice a year.


## Goals of this workshop

- We will together create a simple image processing pipeline that is reproducible, reusable, extensible, documented, and tested.
- We will start with something relatively simple and gradually add the missing pieces: all the way towards making it publishable.
- We will use a Python example but we will not need Python experience to follow and not
  focus on Python programming but rather on software development practices.

We will explore these in 3 sessions:
- Session 1: **Reproducible code changes**. Keep track of code changes and learn how we can collaborate on code using Git and GitHub.
- Session 2: Add **code documentation** and **testing**. Improve **structure**.
- Session 3: Document **dependencies** and prepare the code to be **shared**, reused, and published.

:::{discussion} Learner personas
- You write code for their own research: alone or in a small collaboration.
- You want to be able to contribute to open-source projects.
- You do data analysis and use (import) code written by others in a Jupyter Notebook (or similar) or a script.
- You neither write not use code but you want to better understand how
  reproducible research software is created and what matters to make it
  reusable.
:::

:::{prereq} Preparation (more details will follow)
- Access to exercise repository
- Enable rich diffs for Notebooks in GitHub
:::

---

```{toctree}
:maxdepth: 1
:caption: Session 1: Tracking changes

1/motivation.md
1/browse.md
1/code-review.md
1/sharing.md
```

```{toctree}
:maxdepth: 1
:caption: Session 2: Usability

2/documentation.md
2/testing.md
2/structure.md
```

```{toctree}
:maxdepth: 1
:caption: Session 3: Sharing

3/reproducibility.md
3/software-licensing.md
3/publishing.md
```

```{toctree}
:maxdepth: 1
:caption: Reference

guide.md
All lessons <https://coderefinery.org/lessons/core/>
CodeRefinery <https://coderefinery.org/>
Reusing <https://coderefinery.org/lessons/reusing/>
```
