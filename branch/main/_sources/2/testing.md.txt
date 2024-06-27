# Automated testing: from unit tests to end-to-end tests

:::{objectives}
- Get an overview of possibilities for automated testing.
- Add a unit test to a function.
- Add an end-to-end test or discuss how it could look.
- Make the testing part of code review.
- Discuss where to start in your own project.
:::


## Technical possibilities

Any programming language has tools/libraries to perform:

- **Unit tests**: test a function or a module and
  compare function result to a reference.
- **End-to-end test**: run the whole code and compare result to a reference.
- **Coverage analysis**: Give overview of which parts of the code are tested.
- The test (set) can be run **automatically** on [GitHub
  Actions](https://github.com/features/actions) or [GitLab
  CI](https://docs.gitlab.com/ee/ci/) after every Git commit.


## Motivation

- **Less scary to change code**: tests will tell you whether something broke.
- Unit tests can **guide towards better structured code**: complicated code is more difficult to test.
- **Easier for new people** to join.
- Easier for somebody to **revive an old code**.


## How testing is often taught

```python
def add(a, b):
    return a + b


def test_add():
    assert add(1, 2) == 3
```

How this feels:
:::{figure} img/owl.png
:alt: Instruction on how to draw an owl
:width: 50%
:class: with-border

[Citation needed]
:::

Instead, we will look at and **discuss a real example** where we test components
from our image processing project.


## Exercise/demo

:::{exercise}
- We will together open a pull request from [a branch that implements testing](https://github.com/coderefinery/imgfilters/tree/radovan/testing)
  and review it.
- We will verify that from there on tests are run automatically.
- We will try to open another pull request later which would break tests (and not merge it).
:::

:::{discussion}
- We will discuss the potential but also limitations of the code changes.
- Do we need this for a simple Notebook?
:::


## Where to start

- A simple script or notebook probably does not need an automated test.

**If you have nothing yet**:
- Start with an end-to-end test.
- Describe in words how *you* check whether the code still works.
- Translate the words into a script.
- Run the script automatically on every code change.

**If you want to start with unit-testing**:
- You want to rewrite a function? Start adding a unit test right there first.


## Recommendations for Notebooks

- Automated testing is often too much for notebooks.
- Instead you can test modules that you import in the notebook.
- What is often more useful is to provide an example input
  and show how the result should look like.
  Good example: [scikit-image](https://scikit-image.org/docs/stable/auto_examples/index.html)


## More resources

- [Software testing lesson material](https://coderefinery.github.io/testing/)
