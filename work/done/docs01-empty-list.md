# docs01-empty-list

**Objective.** A person who reads docs/01's `make scan` row learns that a list file with no entry fails the run everywhere, locally included, as `scripts/check_disclosure.py` does, and is no longer led to expect the local skip that only a missing list file gets. Found by the Delivery review of `disclosure-docstring` (work/done/disclosure-docstring.md, Divergences and Review 1).

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. Whether the `make hooks` row, which says "Both refuse every commit when the list is missing", changes too: yes, to "missing or has no entry", the code's own message (`check_disclosure.py:133` and `:137`). It is the same gap in the same table of the same document, one clause long, and a reader of that row would otherwise ask whether an empty list lets commits through. Source: docs/06 line, docs/01:67, the docstring delivered by disclosure-docstring.
2. What "no entry" means in the text: a list file whose lines are all comments or empty, the words docs/01:69 and `docs/manuals/set-up-the-disclosure-list.md:20` already use for the list's format. `load` returns no entry for such a file (lines 136-137). Source: docs/01:69, the code.
3. Whether to change the code: no. The behaviour is deliberate (an empty list would scan nothing and pass, which hides a private term) and the docstring already states it; docs/01 is the only document behind the code. Source: ADR-0012, the docstring.
4. Whether `README.md:23` and the manual change: no. README's sentence is about why only the author turns the hooks on, and "missing" is true there; the manual's line 42 describes a machine with no list, a case that stays as it is. Neither leads a reader to a wrong expectation about an empty file. Source: docs/05 §2 (one delivery, one page).
5. Both editions: none applies; docs/01 is a process document in English (AGENTS.md, docs/05 §5), and no chapter states this rule (`grep` of `book/` for the skip finds nothing).
6. docs/03 and docs/06: no new term ("disclosure list" as docs/03:121 has it) and no split.

**Behaviour.**

* Reading docs/01's `make scan` row, a person finds three cases for the list, each with its result: no list file, skipped locally with a note and failing in Actions (`CI` set); a list file with no entry, failing everywhere with `<list>:1: disclosure: list is missing or has no entry`; a list with entries, scanned, and failing locally while the hooks are off.
* Reading docs/01's `make hooks` row, a person finds that both hooks refuse every commit when the list is missing or has no entry.
* Every other clause of the two rows (the finding formats, where the list lives, its format, the masked path, `--no-verify`) reads as before.
* Fails: a `make scan` row that still says only "Without a list it is skipped locally", leaving an empty list file unnamed.
* Edge: with `FKB_DENYLIST` pointing to an empty file and `CI` unset, `python3 scripts/check_disclosure.py` prints `<path>:1: disclosure: list is missing or has no entry` and exits 1; a file holding only a `#` comment and an empty line does the same. The row agrees with both.
* Edge: with `FKB_DENYLIST=/nonexistent` and `CI` unset, the run prints `disclosure: skipped, no list` on standard error and exits 0; with `CI=1`, `/nonexistent:1: disclosure: list is missing or has no entry` and exit 1. The row agrees with both.
* Edge: with an empty list file, `python3 scripts/check_disclosure.py --staged` exits 1 with the same line. The `make hooks` row agrees.

**Contract.** None: no code, message, exit code or command changes. Two sentences of docs/01's Makefile table; the wording, for /apply to adjust only to fit the row:

* `make hooks` row, replacing "Both refuse every commit when the list is missing.":

      Both refuse every commit when the list is missing or has no entry.

* `make scan` row, replacing "Without a list it is skipped locally and fails in Actions (`CI` set).":

      Without a list file it is skipped locally and fails in Actions (`CI` set); a list file with no entry, only comments and empty lines, fails everywhere (`<list>:1: disclosure: list is missing or has no entry`).

**Out of scope.**

* `scripts/check_disclosure.py`: code and docstring already say this (disclosure-docstring).
* `README.md:23` and `docs/manuals/set-up-the-disclosure-list.md`: true as written, see decision 4.
* The `make verify` row: it points to `make scan` and states no list case of its own.
* Any chapter: none states the rule, so neither edition changes.

**Done when.**

* [x] `grep -n "Without a list it is skipped" docs/01-Architecture.md` finds nothing; the `make scan` row holds the three list cases of the Behaviour, and the `make hooks` row says "missing or has no entry".
* [x] The empty-file, comments-only, missing-list and `--staged` edge runs print and exit as the Behaviour says, with `FKB_DENYLIST` set per run and the tree's git config unchanged (`git config core.hooksPath` still prints `.githooks`).
* [x] No em dash added; `make verify` green.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and only this line's hunk of docs/06; commit message in a `commit` block.

**In flight.** `work/batch-propose.md` is a draft about the method's chapters and touches no row of docs/01's Makefile table, so this line runs in parallel with it (docs/05 §4).

**Divergences.** None: both sentences read as the Contract gives them.

**Proof.** Run on the delivered docs/01, with `FKB_DENYLIST` set per run and the tree's `core.hooksPath` unchanged (`.githooks` before and after):

* `grep -n "Without a list it is skipped" docs/01-Architecture.md`: nothing.
* An empty list file, `CI` unset: `<path>:1: disclosure: list is missing or has no entry`, exit 1. A file holding only a `#` comment and an empty line: the same.
* `FKB_DENYLIST=/nonexistent`, `CI` unset: `disclosure: skipped, no list` on standard error, exit 0. With `CI=1`: `/nonexistent:1: disclosure: list is missing or has no entry`, exit 1.
* An empty list file with `--staged`: the same line, exit 1.
* `make verify`: green.

**Review.** A read-only Opus agent read this delivery's diff against the page and docs/04 and found nothing that breaks either. It noted, as no defect, that a list whose only lines are invalid regular expressions fails with `invalid regular expression` rather than the no-entry message; the row claims only the comments-and-empty-lines case, so it stays accurate and nothing changed.

```commit
docs(docs01-empty-list): say an empty disclosure list fails everywhere

- make scan row: a list file with no entry fails locally and in Actions
- make hooks row: both hooks refuse commits when the list has no entry
work/done/docs01-empty-list.md
```
