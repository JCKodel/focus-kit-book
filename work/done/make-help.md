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

* [x] The Makefile is the Contract's: `make` and `make help` print the eight lines byte for byte and exit 0, in the repository.
* [x] Every name in `.PHONY` appears in `make help`'s output (checked by hand).
* [x] A scratch copy of the Makefile with no `.venv`: `make` prints the lines and creates nothing; `make -f` from another directory prints them too.
* [x] `make -n` of the seven other targets prints the same commands as at HEAD.
* [x] docs/01's tree line and target row, and both READMEs' bullet, written.
* [x] No screenshot: docs/05 §5's proof of a screen is the rendered site, which this delivery does not change; the proof is the runs above, recorded on the page.
* [x] `make verify` green; page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

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

**Built.** The Makefile is the Contract's: `.PHONY` gains `help`, `.DEFAULT_GOAL := help` follows it, the rule `help` comes after `BUMP ?= patch` and before `.venv/.installed`, and the seven public rule lines end in their `## ` description; every recipe line is unchanged. docs/01: the tree line `Makefile` reads "the targets below; `make` alone is `make help`" (inside the fenced tree, with backticks as its `VERSION` and `context/` lines have), and the target table's first row is `make help`, worded as the Contract says. README.md and README.pt.md: the first bullet under "Build locally" and "Gerar localmente".

**Diverged from the contract.** Nothing.

**Proof.** GNU Make 3.81, macOS. `$S` is the session's scratch directory; `expected.txt` there holds the Contract's eight lines.

In the repository:

```
== make
exit 0
identical            (cmp with expected.txt)
== make help
exit 0
identical
== make -n
awk -F ':.*## ' '/^[a-z]+:.*## /{printf "make %-8s %s\n", $1, $2}'  Makefile
```

`make -n` prints the awk command alone: nothing else runs. Every name in `.PHONY` (help, serve, build, verify, scan, hooks, book, release) is in the output, checked by a loop over the `.PHONY` line.

`make -n` of each of the seven other targets, saved at HEAD before the edit and again after, compared with `cmp`: serve, build, verify, scan, hooks, book and release the same.

A scratch directory `$S/fresh` holding only a copy of the Makefile, `requirements.txt` and an empty `sub/`:

```
== make
exit 0
identical
ls -A: Makefile requirements.txt sub        (no .venv)
== cd sub; make -f ../Makefile
exit 0
identical
== cd /; make -f $S/fresh/Makefile
identical
```

In the same scratch directory, `make -n build` prints `python3 -m venv .venv` and `.venv/bin/pip install -r requirements.txt` first, as the Makefile at HEAD does there; `make -n serve` and `make -n verify` start with `python3 -m venv .venv` too: they still install `.venv` when it is missing.

Edges, in the scratch copy with two rules appended, `nodesc:` with no `## ` and `with-hyphen: ## hy`: `make` prints the same eight lines and exits 0; neither is listed.

Failure as before: `make nosuch` prints `make: *** No rule to make target `nosuch'.  Stop.` and exits 2.

`make verify` green in the repository.

**Noted, not fixed.** Nothing.

**Dropped.** Nothing.

**Review.** A read-only agent on Opus read `git diff HEAD` of the Makefile, both READMEs, docs/01 and this line of docs/06, and this page, against the page and docs/04, and ran the checks in a scratch copy: no findings. It confirmed the Contract character for character, tabs on every recipe line, the eight lines byte for byte, the fresh copy creating nothing, `make -f` from `/`, the seven `make -n` unchanged, `make nosuch` exit 2, and the docs/01 and README wording word for word, the table row ending in a period as the other rows do.

**Decisions.**

* No screenshot: the site renders nothing new; the proof is the runs above, as the page says.
* No ADR and no manual: no ADR's decision changes, and nothing a person does by hand changes beyond `make` alone, which README and docs/01 now say.
* The page's "Decisions made alone" stand as written: the driver ran this /apply with recommended answers, so no question was asked.
* The `make -n` comparison is against `make -n` run at HEAD in the repository before the first edit, so `.venv/.installed` is up to date in both and only the targets' own commands differ, if any.
* The other lane building `kit-2026-10-19-1` in the same tree was not touched: of docs/06 only this line's mark changed.

```commit
feat(make-help): `make` alone lists the targets, one line each

- .DEFAULT_GOAL is help: awk lists every rule line ending in "## "
- the seven public targets carry their one-line description
- docs/01's tree line and table row, both READMEs' first bullet

work/done/make-help.md
```
