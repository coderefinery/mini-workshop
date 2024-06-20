# Motivation for version control


## Git is all about keeping track of changes

Below are screenshots of **tracked changes with Git**
(from this [example repository](https://github.com/bast/runtest/commits/main/runtest/run.py)):
:::{figure} img/git-log-github.png
:alt: Screenshot of a git log on GitHub
:width: 80%
:class: with-border

Web browser, GitHub view
:::

:::{figure} img/git-log-terminal.png
:alt: Screenshot of a git log in terminal
:width: 80%

The same as above, but the terminal view
:::


## Why do we need to keep track of versions?

Version control is an answer to the following questions (do you recognize some
of them?):

- "It broke ... hopefully I have a working version somewhere?"

- "Can you please send me the latest version?"

- "Where is the latest version?"

- "Which version are you using?"

- "Which version have the authors used in the paper I am trying to reproduce?"

- "Found a bug! Since when was it there?"

- "I am sure it used to work. When did it change?"

- "My laptop is gone. Is my thesis now gone?"


## Features: roll-back, branching, merging, collaboration

- **Roll-back**: you can always go back to a previous version and compare

- **Branching and merging**:
  - Work on different ideas at the same time
  - Different people can work on the same code/project without interfering
  - You can experiment with an idea and discard it if it turns out to be a bad idea

:::{figure} img/gophers.png
:alt: Branching explained with a gopher
:width: 100%

Image created using <https://gopherize.me/>
([inspiration](https://twitter.com/jay_gee/status/703360688618536960)).
:::

- **Collaboration**: review, compare, share, discuss

- [Example network graph](https://github.com/coderefinery/git-intro/network)


## Reproducibility

- **Someone asks you about your results from 5 years ago. Can
  you get the same results now?**
- How do you indicate which version of your code you have used in your paper?
- When you find a bug, how do you know **when precisely** this bug was introduced
  (Are published results affected? Do you need to inform collaborators or users of your code?).

With version control we can "annotate" code
([browse this example online](https://github.com/networkx/networkx/blame/main/networkx/algorithms/boundary.py)):

:::{figure} img/git-annotate.png
:alt: Example of a git-annotated code with code and history side-by-side
:width: 100%
:class: with-border

Example of a git-annotated code with code and history side-by-side.
:::


## Talking about code

**You want to show someone a few lines from one of your projects.** Which of
these two is more practical?
- "Clone the code, go to the file 'src/util.rs', and search for 'time_iso8601'".
  Oh! But make sure you use the version from August 2023."
- Or I can send you a [permalink](https://github.com/NordicHPC/sonar/blob/75daafc86582feb06299d6a47c82112f39888152/src/util.rs#L40-L44):

:::{figure} img/code-portion.png
:alt: Screen-shot of a code portion
:width: 100%
:class: with-border

Permalink that points to a code portion.
:::


## What we typically like to snapshot

- Software (this is how it started but Git/GitHub can track a lot more)
- Scripts
- Notebooks
- Documents (plain text files much better suitable than Word documents)
- Manuscripts (Git is great for collaborating/sharing LaTeX or [Quarto](https://quarto.org/) manuscripts)
- Configuration files
- Website sources
- Data
