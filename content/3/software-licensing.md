# Choosing a software license

:::{objectives}
- Knowing about what derivative work is and whether we can share it.
- Get familiar with terminology around licensing.
- We will add a license to our example project.
:::


## Copyright and derivative work: Sampling/remixing

:::{figure} img/ai/record-player.png
:alt: Generated image of a monk operating a record player
:width: 50%
:::
[Midjourney, CC-BY-NC 4.0]

:::{figure} img/ai/turntable.png
:alt: Generated image of a monk operating two record players
:width: 50%
:::
[Midjourney, CC-BY-NC 4.0]

- Copyright controls whether and how we can distribute
  the original work or the **derivative work**.
- In the **context of software** it is more about
  being able to change and **distribute changes**.
- Changing and distributing software is similar to changing and distributing
  music
- You can do almost anything if you don't distribute it

**Often we don't have the choice**:
- We are expected to publish software
- Sharing can be good insurance against being locked out

**Can we distribute our changes** with the research community or our future selves?


## Why software licenses matter

You find some great code that you want to reuse for your own publication.

- This is good for the original author - you will cite them. Maybe other people who cite you will cite them.

- You modify and remix the code.

- Two years later ... &#8987;

- Time to publish: You realize **there is no license to the original work** &#128561;

**Now we have a problem**:
- &#128556; "Best" case: You manage to publish the paper without the software/data.
  Others cannot build on your software and data.
- &#128561; Worst case: You cannot publish it at all.
  Journal requires that papers should come with data and software so that they are reproducible.


## Taxonomy of software licenses

:::{figure} img/license-models.png
:alt: "European Union Public Licence (EUPL): guidelines July 2021"

European Commission, Directorate-General for Informatics, Schmitz, P., European Union Public Licence (EUPL): guidelines July 2021, Publications Office, 2021, <https://data.europa.eu/doi/10.2799/77160>
:::

Comments:
- Arrows represent compatibility (A -> B: B can reuse A)
- Proprietary/custom: Derivative work typically not possible (no arrow goes from proprietary to open)
- Permissive: Derivative work does not have to be shared
- Copyleft/reciprocal: Derivative work must be made available under the same license terms
- NC (non-commercial) and ND (non-derivative) exist for data licenses but not really for software licenses

**Great resource for comparing software licenses**: [Joinup Licensing Assistant](https://joinup.ec.europa.eu/collection/eupl/solution/joinup-licensing-assistant/jla-find-and-compare-software-licenses)
- Provides comments on licenses
- Easy to compare licenses ([example](https://joinup.ec.europa.eu/licence/compare/BSD-3-Clause;Apache-2.0))
- [Joinup Licensing Assistant - Compatibility Checker](https://joinup.ec.europa.eu/collection/eupl/solution/joinup-licensing-assistant/jla-compatibility-checker)
- Not biased by some company agenda


## Exercise/demo

:::{exercise}
- Let us choose a license for our example project.
- We will add a LICENSE to the repository.
:::

:::{discussion}
- Our example code uses the libraries `scikit-image`, `scikit-learn`, `numpy`,
  and `matplotlib`. Do we need to look at their licenses? In other words, **is
  our project derivative work** of something else?
:::


## More resources

- Presentation slides "Practical software licensing" (R. Bast): <https://doi.org/10.5281/zenodo.11554001>
- [Social coding lesson material](https://coderefinery.github.io/social-coding/)
- [UiT research software licensing guide (draft)](https://research-software.uit.no/blog/2023-software-licensing-guide/)
- [Research institution policies to support research software (compiled by the Research Software Alliance)](https://www.researchsoft.org/software-policies/)
- More [reading material](https://coderefinery.github.io/social-coding/software-licensing/#great-resources)
