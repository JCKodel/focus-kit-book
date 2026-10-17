# venv-failed-install

**Objective.** After a `make` whose install of the site's packages failed, the next `make serve`, `make build` or `make verify` installs again instead of running on a half-built `.venv`.

**Behaviour.** A manual check in a scratch directory with a copy of the Makefile and a `requirements.txt` naming a package that does not exist (docs/04 §Tests: the checks are the tests, and none reads the Makefile).

* Start with no `.venv`. `make build` creates the venv, `pip install` fails, `make` prints pip's error and exits non-zero. Today the second `make build` finds `.venv` newer than `requirements.txt` and skips the install: it runs `scripts/build.py` on a venv without mkdocs. After this delivery the second `make build` runs `python3 -m venv .venv` and `pip install` again and fails the same way, every time, until the install succeeds.
* Edge: the install succeeds. `make build` leaves `.venv/.installed`; a second `make build` runs no install; a `requirements.txt` edited afterwards (newer than the stamp) installs again, as docs/01 says today.
* Edge: a clone with a `.venv` from before this delivery has no stamp. The first `make` installs once more over the existing venv, which `python3 -m venv` and `pip` accept, and leaves the stamp. Nothing else asks the person to delete `.venv`.
* Edge: `make scan`, `make hooks`, `make book` and `make release` do not depend on `.venv` and are unchanged.
* The finding named `touch .venv` after a failed install. Re-checked: make stops at the failing line, so `touch` never runs. The cause is that `python3 -m venv .venv` sets the directory's own modification time, which is newer than `requirements.txt`, and a directory is the target. The result the finding reports holds, reproduced in the scratch directory; the page fixes the cause, not `touch`.

**Contract.** `Makefile`, these lines replacing its first block, the rest unchanged:

```
.venv/.installed: requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	touch .venv/.installed

serve: .venv/.installed
	.venv/bin/mkdocs serve

build: .venv/.installed
	.venv/bin/python scripts/build.py
```

`verify` keeps `build` as its prerequisite. docs/01 follows in the same delivery: the `.venv` row of the target table reads `.venv/.installed`, "`python3 -m venv .venv` and `pip install -r requirements.txt`, then the stamp; rebuilt when `requirements.txt` is newer than the stamp or an install failed"; the tree line `.venv/` gains "`.venv/.installed` marks a finished install". `.gitignore` already ignores `.venv/`. No script, test or workflow changes (Actions does not use the target: `grep venv .github` finds nothing).

**Out of scope.**

* Retrying or hiding pip's error: the failure stays loud, one failed command, as the Makefile lets it.
* Pinning more packages or a Python version: `requirements.txt` is unchanged.
* A script that tests the Makefile: no check in docs/04 reads it, and one stamp rule does not earn a harness (abstraction on the second occurrence).
* docs/01's tree, other lines (`context/`, `.DS_Store`): `docs01-retired-projects`. Both deliveries edit docs/01 near the tree's `.venv/` line, in different lines; stage by hunk (docs/05 §6).

**Done when.**

* [x] The three checks above run in a scratch directory and their outcome is recorded on the page.
* [x] `make serve`, `make build` and `make verify` run from the repository: the first `make` after the change installs once and leaves `.venv/.installed`, the next installs nothing.
* [x] docs/01's target row and tree line updated.
* [x] `make verify` green; page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* A stamp file rather than `rm -rf .venv` on failure: the failure leaves the person's partial venv to inspect, and a rerun repairs it; docs/01 already says the venv is "rebuilt when `requirements.txt` changes", which the stamp keeps.
* Manual check, not a script: docs/04 §Tests, "the checks are the tests", and no check reads the Makefile.

**Decisions in the review.**

* The fix is a stamp `.venv/.installed`, not a `|| rm -rf .venv` after the install: chosen alone, since the documents say only that the next make rebuilds.
* The page corrects the finding's mechanism (the directory's mtime, not `touch`), chosen alone after reproducing it.
* No overlap with any page in flight (M15's pages change `book/`, docs/00, 03, 04 and ADRs); the one shared file is docs/01 with `docs01-retired-projects`, different lines.

**The error it catches** (docs/05 §7): after a `make` whose `pip install` failed, the next `make build` skipped the install, because the target was the directory `.venv` and `python3 -m venv .venv` had already made it newer than `requirements.txt`; the build then ran on a venv without mkdocs.

**Built.** The Makefile's first block is the Contract's, word for word: the target `.venv/.installed`, touched only after `pip install` succeeds, and `serve` and `build` depend on it. `verify`, `scan`, `hooks`, `book` and `release` are unchanged. docs/01: the tree line `.venv/` reads "created by make from requirements.txt; .venv/.installed marks a finished install; ignored" (inside the fenced tree, so no backticks), and the target row is `.venv/.installed`, "`python3 -m venv .venv` and `pip install -r requirements.txt`, then the stamp; rebuilt when `requirements.txt` is newer than the stamp or an install failed".

**Diverged from the contract.** Nothing.

**Proof.** Scratch directories under the session's scratch directory, `$S`, each with a copy of a Makefile, a `requirements.txt` and a stub `scripts/build.py` that prints `build.py ran` and then imports mkdocs. Python 3.14.8.

Failed install, Makefile at HEAD (before), `requirements.txt` holding `zzq-no-such-package-xyz==1.0`:

```
== before: run 1
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
ERROR: No matching distribution found for zzq-no-such-package-xyz==1.0
make: *** [.venv] Error 1
== before: run 2
build.py ran
ModuleNotFoundError: No module named 'mkdocs'
make: *** [build] Error 1
```

The finding's result is reproduced: the second run installs nothing and runs the build on a venv without mkdocs.

Failed install, this delivery's Makefile (after), the same `requirements.txt`, three runs:

```
== after, failed install: run 1, 2 and 3, each
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
ERROR: No matching distribution found for zzq-no-such-package-xyz==1.0
make: *** [.venv/.installed] Error 1
[exit 2]
stamp: ls: .venv/.installed: No such file or directory
```

Edge, the install succeeds: in the same directory, the repository's `requirements.txt` copied in.

```
== requirements fixed (real requirements.txt)
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
Successfully installed babel-2.18.0 ...
build.py ran
[exit 0]
stamp: .venv/.installed
== second run
build.py ran
[exit 0]
== requirements.txt newer than the stamp   (touch requirements.txt)
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
build.py ran
[exit 0]
== again
build.py ran
[exit 0]
```

Edge, a venv from before this delivery: a fresh directory built with the Makefile at HEAD, then this delivery's Makefile copied over it.

```
== old Makefile, fresh clone
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
Successfully installed babel-2.18.0 ...
touch .venv
build.py ran
[exit 0]
stamp: ls: .venv/.installed: No such file or directory
== new Makefile over the old .venv
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
touch .venv/.installed
build.py ran
[exit 0]
== second run
build.py ran
[exit 0]
```

Edge, the targets that do not use `.venv`: `make -n` prints one command each, as before: `python3 scripts/check_disclosure.py` (scan), `git config core.hooksPath .githooks` (hooks), `python3 scripts/build_book.py` (book), `python3 scripts/release.py patch` (release).

In the repository, whose `.venv` predates this delivery and had no stamp: the first `make build` printed `python3 -m venv .venv`, `.venv/bin/pip install -r requirements.txt` (every requirement already satisfied), `touch .venv/.installed` and the build; the second `make build` printed only `.venv/bin/python scripts/build.py`; `make verify` printed only the build and the five checks, green; `make serve` printed only `.venv/bin/mkdocs serve` and answered 200 at `http://127.0.0.1:8000/focus-kit-book/`. The repository's `.venv` is working and stamped.

**Noted, not fixed.** Nothing.

**Dropped.** Nothing.

**Decisions.**

* No screenshot: docs/05 §5 asks one of a toolchain delivery's rendered site, and this one changes nothing the site renders; the proof is the scratch directories and the repository's runs, as the page says (decided in this session, not asked).
* The scratch `scripts/build.py` is a stub that imports mkdocs, not a copy of the real one, so the before case shows the build running on a venv without mkdocs without copying the repository's sources (decided in this session, not asked).
* The edge "a venv from before this delivery" is proved twice: in a scratch directory built by the Makefile at HEAD, and on the repository's own `.venv`.
* No ADR and no manual: no decision of an ADR changes, and nothing a person does by hand changes (the first `make` installs once by itself).
* No queue line depends on this one; `docs01-retired-projects` edits other lines of docs/01.

```commit
fix(venv-failed-install): reinstall after a failed pip install

- the Makefile's install target is the stamp .venv/.installed
- the stamp is written only after pip install succeeds
- docs/01's target row and tree line name the stamp

work/done/venv-failed-install.md
```
