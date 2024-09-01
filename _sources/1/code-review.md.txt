(code-review)=

# Collaboration and code review using issues and pull requests

:::{objectives}
- Using issues as a way to discuss and plan work.
- Using pull requests as a way to review and discuss code changes.
:::


## What is a pull request (GitHub) or merge request (GitLab)?

- Think of merge requests as **change proposals**.
- Conceptually, they are similar to "suggesting changes" in Google Docs:
  They can be commented on and accepted (merged).


## &#127803; Five nice things about pull requests which are often misunderstood

1) **Issues don't have to be only about bugs**: Open one to share an idea
before you start coding and collect feedback. Later cross-reference the issue
in the pull request.

2) **Reviewing code is mainly for <strike>quality assurance</strike>
collaborative learning**: It is mainly for knowledge transfer. Two persons
know about a change instead of one. Both have a chance to learn something
new.

3) **Modifying an open pull request** does not require closing and opening a
new one. Pull requests are from a source branch to a target branch. You can
add new commits to the source branch and the pull request will be updated
automatically. This also means: Always create a new branch for each new pull
request.

4) **Draft pull requests** are a nice way to inform about unfinished work and
to collect feedback early.

5) **Reviewing changes in Jupyter Notebooks** can be pleasant. Enable
  [Rich Jupyter Notebook Diffs](https://github.blog/changelog/2023-03-01-feature-preview-rich-jupyter-notebook-diffs/).


## Exercise/demo

The proof of the pudding is in the eating. Let's try the above
in two pull requests:

:::{exercise}
1) Open an issue, describe an idea, then open a pull request that
cross-references the issue, then improve the pull request based on feedback
(as an example, we can try to change one of the colors in the warhol_effect
filter).
2) Compare the following "diff" between two branches that modifies our
Notebook. View it with and without the [Rich Jupyter Notebook
Diffs](https://github.blog/changelog/2023-03-01-feature-preview-rich-jupyter-notebook-diffs/)
feature enabled (click on your avatar top-right on GitHub, then "Feature
preview"): <https://github.com/coderefinery/imgfilters/compare/8aefed1..4dbae92>
:::


## How to organize your own project

**How large should a commit be?**
- Better too small than too large (easier to combine than to split).
- Smaller sized commits may be easier to review for others than huge commits.
- Imperfect commits are better than no commits.

**Writing useful commit messages**:
  Useful commit messages summarize the change and provide context.

**What level of branching complexity is necessary?**
- Simple **personal projects**: Typically start with just the `main` branch.
  Use branches when you are not sure about a change.
- Projects with **few persons**: Create a new branch for each new feature or
  bug fix. Changes are reviewed by others. Consider to write-protect the
  `main` branch so that it can only be changed
  with pull requests or merge requests.


## More resources

- [CodeRefinery lesson on collaborative Git](https://coderefinery.github.io/git-collaborative/)
