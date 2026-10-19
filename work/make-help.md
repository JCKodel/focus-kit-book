# make-help

**Objective.** A person who runs `make` with no target in the repository sees the targets it offers, one line each saying what it does, and nothing runs (M22's last clause, docs/06).

**Behaviour.** Manual checks, in the repository and in a scratch directory with a copy of the Makefile (docs/04 §Tests: the checks are the tests, and none reads the Makefile; as `venv-failed-install` did).

* `make` in the repository prints the eight lines of the Contract, in that order, and exits 0; no other command runs and nothing is echoed.
* `make help` prints the same eight lines and exits 0.
* `make` in a fresh clone, with no `.venv`: prints the eight lines, exits 0, and creates nothing. Today it builds `.venv`, because `.venv/.installed` is the Makefile's first rule (`make -n` at HEAD prints "`.venv/.installed' is up to date"); this is the one change a person sees. Nothing relies on it: `.github/workflows/verify.yml` runs `make verify`, `make build` and `make book`; the hooks call `scripts/check_disclosure.py`; `scripts/release.py` runs `make verify`; neither README, docs/01, docs/05 nor a manual tells anyone to run `make` alone. `make serve`, `make build` and `make verify` still install `.venv` when it is missing.
* `make -f <path>/Makefile` from another directory prints the same lines (the help reads `$(MAKEFILE_LIST)`, not a fixed name).
* `make -n serve`, `build`, `verify`, `scan`, `hooks`, `book` and `release` print the same commands as before: only `## ` comments are added to their rule lines.
* Edge: a public target added later without `## ` on its rule line is not listed, and nothing fails. That is the accepted failure, and also how a helper stays hidden: `.venv/.installed` is never listed, its name starting with `.`.
* Edge: a target whose name holds anything but `a` to `z` (a hyphen, a digit) is not listed by this pattern, even with `## `; no target has one today, and the delivery that adds one widens the pattern.
* Fails as before: `make nosuch` prints make's own "No rule to make target" and exits 2.

**Contract.** `Makefile`. The first lines become:

```
.PHONY: help serve build verify scan hooks book release
.DEFAULT_GOAL := help

BUMP ?= patch

help: ## this list
	@awk -F ':.*## ' '/^[a-z]+:.*## /{printf "make %-8s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
```

then the existing rules, in their order and unchanged but for a `## ` comment at the end of each public rule line:

```
serve: .venv/.installed ## serve the site at http://127.0.0.1:8000/
build: .venv/.installed ## build the site into site/, strict
verify: build ## build, then every check; green before anything is done
scan: ## the disclosure scan alone
hooks: ## turn on the git hooks, once per clone
book: ## the PDF and EPUB of both editions, in output/
release: ## publish the next version, author only (BUMP=minor|major)
```

`make` and `make help` print exactly, file order, `make `, the name left-aligned in 8 columns, a space, the description:

```
make help     this list
make serve    serve the site at http://127.0.0.1:8000/
make build    build the site into site/, strict
make verify   build, then every check; green before anything is done
make scan     the disclosure scan alone
make hooks    turn on the git hooks, once per clone
make book     the PDF and EPUB of both editions, in output/
make release  publish the next version, author only (BUMP=minor|major)
```

The output is English in both editions: commands and their output stay as they are (docs/04). Tools: make and awk only, both already needed; `.DEFAULT_GOAL` exists since GNU make 3.81, the version on macOS (prototype run on 3.81 in this session, the output above), and Actions' make is newer.

Documents in the same delivery:

* docs/01: the tree line `Makefile` reads "the targets below; `make` alone is `make help`"; the target table gains a first row, `make help`: "the default goal: each target whose rule line ends in `## <what it does>`, one line each, `make <name>` and the text, in the Makefile's order; a target without it, `.venv/.installed` included, is not listed".
* README.md, under "Build locally", a first bullet: "`make` lists these commands, one line each." README.pt.md, the same place: "`make` lista estes comandos, uma linha cada." Parity counts headings, not bullets.
* docs/05 §5 names targets without listing them: unchanged. docs/03: no new term (the page says "target"; docs/03's "command" is the kit's four).

**States.** No screen.

**Visual reference.** No screen.

**Out of scope.**

* A verify check that every public target has a description: no error it would have caught has happened (docs/04 §Tests, docs/05 §7), and `venv-failed-install` found one Makefile rule does not earn a harness; Done when checks it by hand.
* A Portuguese help: the output of a command stays as it is (docs/04).
* Describing `BUMP` or other variables beyond the release line's parenthesis: docs/01 and the release manual say it.
* Colours or a header line: plain text, nothing to strip in a terminal or a log.

**Done when.**

* [ ] The Makefile is the Contract's: `make` and `make help` print the eight lines byte for byte and exit 0, in the repository.
* [ ] Every name in `.PHONY` appears in `make help`'s output (checked by hand).
* [ ] A scratch copy of the Makefile with no `.venv`: `make` prints the lines and creates nothing; `make -f` from another directory prints them too.
* [ ] `make -n` of the seven other targets prints the same commands as at HEAD.
* [ ] docs/01's tree line and target row, and both READMEs' bullet, written.
* [ ] No screenshot: docs/05 §5's proof of a screen is the rendered site, which this delivery does not change; the proof is the runs above, recorded on the page.
* [ ] `make verify` green; page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* No check and no test: docs/04 §Tests and docs/05 §7, as `venv-failed-install` decided for the Makefile.
* No screenshot: docs/05 §5, as `venv-failed-install` decided.
* Output in English in both editions: docs/04, commands and their output stay as they are.

**Decisions made alone** (the author asked for recommended answers; correct them in the review):

* `.DEFAULT_GOAL := help`, not `help` as the first rule: it survives a rule added above it.
* `## ` on the rule line, parsed by awk from `$(MAKEFILE_LIST)`: the common idiom, no new file, script or dependency, and the description sits beside the rule it describes.
* `help` is listed, first, as the file's first rule; the rest keep the Makefile's order.
* `build` is listed: Actions runs it and docs/01 documents it, though the READMEs do not.
* The eight descriptions above, worded for this delivery from docs/01's rows.
* Target names `[a-z]+` only, the pattern kept simple until a name needs more.
