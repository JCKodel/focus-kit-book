# manual-pip-floor

**Objective.** A person on macOS whose `python3` carries a pip older than 23.0.1 follows the build manual's pypdf line and gets pypdf installed, instead of an unknown-option error the manual does not explain.

**Behaviour.**

The finding comes from the Delivery review recorded in `work/done/manual-pypdf-install.md` ("Outside the page" and "Noted, not fixed"): `--break-system-packages` exists from pip 23.0.1; an older pip, such as the stock pip of Apple's `/usr/bin/python3`, rejects it as an unknown option. It does not come from `work/done/m23-review.md`.

* pip's NEWS (`NEWS.rst` in pypa/pip, read at this page's writing): 23.0 (2023-01-30) implements the `EXTERNALLY-MANAGED` refusal of PEP 668; 23.0.1 (2023-02-17) implements `--break-system-packages`.
* With pip 23.0.1 or later, the manual's command `python3 -m pip install --user --break-system-packages pypdf` runs as today: past Homebrew's refusal, accepted and without effect where the Python is not externally managed.
* With a pip older than 23.0.1, the same command stops at `no such option: --break-system-packages` and installs nothing. The manual now says what that message means and what to run: the same command without the flag, `python3 -m pip install --user pypdf`, which such a pip accepts, since only 23.0 and later read `EXTERNALLY-MANAGED`.
* The reader does not need to run `pip --version` first: the sentence is keyed on pip's own message and still names the floor, 23.0.1.
* Edge, not covered: pip 23.0 exactly, on an externally managed Python, refuses the install and lacks the flag; no pip command gets past it (Decisions taken alone).
* Debian or Ubuntu: unchanged, apt installs `python3-pypdf`.

**Contract.**

One file, edited by its text:

```
docs/manuals/build-the-book-from-a-clone.md  "What must be in place", the macOS sub-item of "For `make book`" (:15)
```

* The sentence "macOS: `brew install pandoc weasyprint` and `python3 -m pip install --user --break-system-packages pypdf`, for the `python3` that `make book` runs; Homebrew's Python refuses a bare `pip install` and has no pypdf formula." keeps its words and gains, after its full stop, in the same bullet: "If pip answers `no such option: --break-system-packages`, it is older than 23.0.1: run the same command without that flag."
* Nothing else in the file changes: the summary (:7), the "For `make book`" item (:14), the Debian line (:16), "How to undo it" and the pypdf line under "What breaks" (:44) stay true.
* Not touched: `scripts/build_book.py`, `Makefile`, both READMEs, `docs/01-Architecture.md`, `release-the-book.md`, `.github/workflows/verify.yml` (its runner's pip is current).
* No new term in docs/03; no chapter names pypdf or pip's flag, so no edition changes. The manual is English only, as `README.pt.md` says.

Neighbouring lines on the same file: none open. `manual-link-pointers` and `manual-pypdf-install`, both `[x]`, edited it before; this delivery edits the file as they left it (grep of `work/*.md` and docs/06's open lines at this page's writing).

**Out of scope.**

* pip 23.0 on an externally managed Python: one release, and no pip flag passes it; a venv or an upgraded Python is the way, beyond this line.
* `work/done/manual-pypdf-install.md`'s Behaviour line ("the flag is accepted and changes nothing"): history, and its Delivery review already records the floor.
* Telling the reader to upgrade pip first: on an externally managed Python that upgrade is refused the same way, and on the others the command without the flag already works.

**Done when.**

* [x] In a scratchpad venv with pip pinned to 23.0, `pip install --dry-run --break-system-packages pypdf` prints `no such option: --break-system-packages`; with pip 23.0.1, the same command prints `Would install pypdf-...`; recorded. (`--dry-run` exists from pip 22.2; `--user` is dropped because a venv refuses it for its own reason; needs network.)
* [x] In the pip 23.0 venv, `pip install --dry-run pypdf` prints `Would install pypdf-...`, recorded.
* [x] The manual's macOS bullet reads as Contract says; `git diff` of the manual shows only that line changed, recorded.
* [x] `make verify` green.
* [x] The Delivery review as docs/05 §5 says.

**Decisions taken alone.**

* Keyed on pip's message, not on `pip --version`: the reader who hits the error reads it at the step, and the number 23.0.1 stays in the sentence as the queue line asks.
* "Without that flag", not a second full command: the smallest wording; the command the reader just ran is one line above.
* The 23.0 gap is left out of the manual and stated here from pip's NEWS (23.0 added the refusal, 23.0.1 the flag), with no claim about which Pythons shipped 23.0.
* The proof uses venvs with pinned pips in the scratchpad: it shows the floor exactly, 23.0 against 23.0.1, without changing this machine's `python3`.

**Proof.**

Two venvs in the session's scratchpad, made from Apple's `/usr/bin/python3` (Python 3.9.6), one with pip pinned to 23.0 and one to 23.0.1:

```
$ pip --version            # venv with pip 23.0
pip 23.0 from .../site-packages/pip (python 3.9)
$ pip install --dry-run --break-system-packages pypdf
no such option: --break-system-packages
$ pip install --dry-run pypdf
Would install pypdf-6.21.1 typing_extensions-4.16.0

$ pip --version            # venv with pip 23.0.1
pip 23.0.1 from .../site-packages/pip (python 3.9)
$ pip install --dry-run --break-system-packages pypdf
Would install pypdf-6.21.1 typing_extensions-4.16.0
```

After the proof, the machine's `python3 -m pip --version` still prints `pip 26.2.1` (Homebrew's Python 3.14) and `/usr/bin/python3 -m pip --version` still prints `pip 26.0.1`: neither changed.

`git diff HEAD -- docs/manuals/build-the-book-from-a-clone.md` shows one line changed, :15, which now reads:

```
  * macOS: `brew install pandoc weasyprint` and `python3 -m pip install --user --break-system-packages pypdf`, for the `python3` that `make book` runs; Homebrew's Python refuses a bare `pip install` and has no pypdf formula. If pip answers `no such option: --break-system-packages`, it is older than 23.0.1: run the same command without that flag.
```

`make verify` green. `make book` is run by the driver once for the batch; this delivery changes nothing it builds.

**Divergences.**

* Done when names "a scratchpad venv" without its Python. The first venvs, made from this machine's `python3` (3.14.8), could not run pip 23.0 or 23.0.1: both stop at `AttributeError: module 'pkgutil' has no attribute 'ImpImporter'`, since that attribute left Python in 3.12. The proof ran on venvs made from Apple's `/usr/bin/python3` 3.9.6 instead, the interpreter the finding names.

**Decisions.**

* The 3.14 failure changes nothing in the manual: it is about running an old pip on a new Python, not about the flag, and the 3.9 venvs show the floor exactly.

**Delivery review.** One read-only Opus agent over this delivery's paths (`git diff HEAD` of the manual and this page against its committed version): nothing breaks the page, docs/04 or the text written. It confirmed :15 matches the Contract word for word and is the only changed line, the rest of the manual stays true, and the Proof reproduces in the same venvs; Apple's `/usr/bin/python3` is not externally managed, so dropping the flag holds there. The Divergence and the Decision are sound and the commit block follows docs/05 §6. Outside the page: nothing. Stylistic notes, kept: the page has both "Decisions taken alone." and "Decisions.", an established pattern; the 26.0.1 pip of `/usr/bin/python3` lives in the user site, not Apple's stock install.

```commit
docs(manual-pip-floor): say what to run when pip lacks the flag

- macOS pypdf line: a pip older than 23.0.1 answers no such option
- the manual says to run the same command without the flag

work/done/manual-pip-floor.md
```
