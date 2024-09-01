# Copy and browse an existing project

:::{objectives}
- We will fork the [example project](https://github.com/coderefinery/imgfilters).
- We will find a point in history when a code default changed (using `git annotate`).
- We will create a branch and a commit with a new file added to `exercise`
  directory.
:::


## Repositories and branches

What is a **Git repository**?
- Git repository contains a bunch of files and tracks their changes over time.
- Git repositories typically reside on GitHub or GitLab or on your computer or on some server.
- Git repositories track changes using commits.

What are **branches**?
- Commits form a history of changes and the history can be visualized as a tree which contains branches.
- Each repository has a default branch. It is often called `main` or `master`.
- Branches are like parallel universes where you can experiment with changes without affecting the default branch.
- Browse the network of branches in our example repository
  ("Insights" -> "Network"): <https://github.com/coderefinery/imgfilters/network>


## Annotated history

:::{exercise} Let us try the annotation feature ("git blame")
- The function [gaussian_smoothing](https://github.com/coderefinery/imgfilters/blob/8aefed153328230092df31775dcd2388721bb862/imgfilters/filters.py#L16-L22) has a default value for sigma. But this default used to be different.
- Find out **when** this default value was changed (which commit).
- Would you be able to do this archaeology work with your project?
- Is the commit message informative about **why** this was changed?
:::


## What is a fork? Let's create and browse it!

- A fork is a full copy of a repository.
- You have then write permissions to your copy.
- Once a fork is created, you decide when to sync changes from the original
  repository - it does not happen automatically.

:::{figure} img/create-fork.png
:alt: Creating a fork on GitHub
:width: 100%
:class: with-border

Creating a fork on GitHub
:::

:::{figure} img/verify-fork.png
:alt: Verify that you are on your fork
:width: 100%
:class: with-border

Verify that you are on your fork
:::


## Exercise/demo: creating a new branch and a new commit

You can try this or you watch the instructor doing it.

:::{exercise} Creating a new branch and a new commit
- Create a new branch in your fork and give it a descriptive name.
- Add a new file in the `exercise` directory to the new branch.
- In this file we will try to answer: "What do you know now about programming
  that you wish you knew when you started?".
- The new branch and new file now only exist on the fork, not yet in the
  original repository.
:::


## How does this relate to your own work?

:::{admonition} Summary
- Forking is useful if you want to modify a repository that you do not have
  write access to or if you want to allow others to experiment with your
  repository.
- Within your research project you probably want to give all project members
  write access and then you can work within the same repository.
- If you are more than 1 person working on a project, it can be useful
  to make the `main` branch protected and to always create a new branch for each
  new feature or bug-fix or idea.
- In the next episode ({ref}`code-review`) we will discuss how to suggest
  changes from a fork or within the same repository.
:::


## More resources

In this short workshop we focus on **what is possible** and **what are good
practices** but we cannot focus on **how to do these in detail**
across the many user interfaces (GitHub web, GitLab web, command line, VS Code, other editors).

- Here we go through those in detail: [Introduction to version control with Git](https://coderefinery.github.io/git-intro/)
