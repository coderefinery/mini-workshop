# How to structure the code as it grows

:::{objectives}
- Discuss the advantages of structuring code into functions and files.
- Add a command-line interface to the code and discuss its advantages.
:::


## From no functions to functions

- Many projects start with a single file and all code is in the global scope (meaning there are no functions).
- A bit later we often introduce functions into the code.

Motivation to structure code into functions:
- Less code repetition.
- Functions can make the overall code flow more readable and easier to follow.
  Example: <https://github.com/coderefinery/imgfilters/blob/main/example.py>
- They allow us to encapsulate details and complexity.
- We can make code reusable across projects and notebooks.
- Code becomes easier to test.
- Unintended side effects are less likely to occur.
- For languages with garbage collection, functions can help to manage memory.


## Prefer pure functions

These are functions without side-effects, meaning they do not modify any global
variables or have any other side-effects.

Functions without side-effects are easier to understand and to copy-paste into
other projects.

Examples for impure functions:
- Functions which modify global variables.
- Functions which modify input data.
- Functions which read from or write to files or databases.


## From one file to multiple files

Motivation to split code into multiple files:
- When the one file grows long and becomes hard to navigate.
- When we want to reuse some functions in other projects.
- We can browse <https://github.com/coderefinery/imgfilters/network> and find the point where that happened.


## Exercise/demo: Adding a command-line interface

Adding a command-line interface (CLI) to a script is an often undervalued "superpower" of programming.

:::{exercise}
- We will together add a command-line interface to our example code.
:::

:::{discussion}
- We will discuss the advantages of doing this:
  - **Easier to use**: Give the user the freedom to change data and settings without having to modify the code.
  - **Easier to parallelize**: Give the user the freedom to choose their parallelization strategy.
  - **Easier to automate**: As part of pipeline/workflow tools.
:::

Here is an example solution using [Argparse](https://docs.python.org/3/library/argparse.html):
```python
from imgfilters.filters import pixelate
from imgfilters.file_io import read_image, save_image

import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Pixelate image")
    parser.add_argument(
        "--input", type=str, required=True, help="Path to the input image"
    )
    parser.add_argument(
        "--output", type=str, required=True, help="Path to the output image"
    )
    parser.add_argument(
        "--scale", type=float, default=0.05, help="Scale for pixelation"
    )

    return parser.parse_args()


args = parse_arguments()


image = read_image(args.input)
image_pixelated = pixelate(image, scale=args.scale, num_colors=8)
save_image(image_pixelated, args.output)
```

Instead of Argparse, we could have used
[Click](https://click.palletsprojects.com) or
[docopt](http://docopt.org/) or ...
