# ADR-0003: copyleft everywhere: AGPL-3.0 for code, CC BY-SA 4.0 for text

**Date:** 2026-09-24

## Context

The repository is public, and its content must stay open: no one may take it and close it.
focus-kit is AGPL-3.0-only, and the command files it installs here stay under the AGPL.
The AGPL is written for software: its terms speak of source code, object code and network interaction, and do not map cleanly onto prose, figures or a printed PDF.
The closest license for text is Creative Commons Attribution-ShareAlike 4.0: anyone may copy, adapt and even sell it, but every derivative must carry the same license, so it can never become closed.
CC BY-SA 4.0 is also declared one-way compatible with GPLv3 by Creative Commons, so its text can flow into GPL-family works.

## Decision

* Code, scripts and configuration written for this repository (build, checks, workflows): AGPL-3.0-only, as focus-kit.
* The book's text and figures, in both editions: CC BY-SA 4.0.
* focus-kit's installed command files: AGPL-3.0-only, under focus-kit's own terms.

`license-and-readme` replaces the `LICENSE` file with the AGPL text plus a `LICENSE-TEXT` with CC BY-SA 4.0, and the README says which covers what.

## Consequences

Everything in the repository is copyleft.
Instructors and companies can use and adapt the book, including in paid workshops, but what they derive stays open under the same license.

## Amendment, 2026-09-24

* The project documents (`docs/`, `work/`) and the READMEs are CC BY-SA 4.0 too: they are prose, and the book quotes them as artifacts.
* `book/assets/site.css` is code, AGPL-3.0-only, although it lives in `book/`.

`README.md` and `README.pt.md` hold the table of which license covers what; `LICENSE` is the AGPL-3.0 text and `LICENSE-TEXT` the CC BY-SA 4.0 legal code.
