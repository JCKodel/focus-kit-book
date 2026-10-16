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

* [ ] The three checks above run in a scratch directory and their outcome is recorded on the page.
* [ ] `make serve`, `make build` and `make verify` run from the repository: the first `make` after the change installs once and leaves `.venv/.installed`, the next installs nothing.
* [ ] docs/01's target row and tree line updated.
* [ ] `make verify` green; page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* A stamp file rather than `rm -rf .venv` on failure: the failure leaves the person's partial venv to inspect, and a rerun repairs it; docs/01 already says the venv is "rebuilt when `requirements.txt` changes", which the stamp keeps.
* Manual check, not a script: docs/04 §Tests, "the checks are the tests", and no check reads the Makefile.

**Decisions in the review.**

* The fix is a stamp `.venv/.installed`, not a `|| rm -rf .venv` after the install: chosen alone, since the documents say only that the next make rebuilds.
* The page corrects the finding's mechanism (the directory's mtime, not `touch`), chosen alone after reproducing it.
* No overlap with any page in flight (M15's pages change `book/`, docs/00, 03, 04 and ADRs); the one shared file is docs/01 with `docs01-retired-projects`, different lines.
