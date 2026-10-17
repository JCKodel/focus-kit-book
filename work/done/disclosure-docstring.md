# disclosure-docstring

**Objective.** A person who opens `scripts/check_disclosure.py` reads in its docstring every case in which the run fails or is skipped, with the same conditions docs/01 gives for `make scan` and `make hooks`. Finding build-4 of `m15-review` (work/done/m15-review.md), seen.

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. Whether to fix only the hooks clause or the whole failure paragraph: the whole paragraph of the no-argument run, because the line says "when the run fails as docs/01 does" and docs/01:69 gives three conditions the docstring leaves out (the list present, `CI` unset, and no list at all, skipped locally and failing in Actions). Source: docs/06 line, docs/01:69.
2. Whether to name the empty list: yes, as "missing or has no entry", the code's own message (`check_disclosure.py:133` and `:137`). docs/01:67 says "missing"; an empty list is the same refusal and the docstring describes the code, so naming it removes a second reading without contradicting docs/01. docs/01 is not edited.
3. Whether to change the code: no. The code already does what docs/01 says (`main`, lines 127-150); the finding is the docstring alone (m15-review, build-4).
4. Whether to fix build-3 (text detection on NUL or invalid UTF-8) in the same delivery: no, it is a separate latent finding with its own behaviour change, not this line's sentence (m15-review, candidates table).
5. Proof: the docstring is read against the code's branches, and the two `CI` cases are run with a missing list; the hooks-off case is run with a git setting from the environment so the shared tree's `core.hooksPath` is never touched (docs/05 §4, two sessions in one tree).
6. docs/03 and docs/06: no new term (the docstring uses "disclosure list" only as docs/03:121 has it) and no split.

**Behaviour.**

* The docstring says that with no argument the run scans the files and every commit message, and that it fails while the hooks are off only when a list exists and `CI` is unset. Held: `main` checks `hooks_off()` inside the branch with a list and under `not os.environ.get("CI")` (line 146); docs/01:69 says the same.
* The docstring says that with no argument and no list the run is skipped locally, with a note on standard error and exit 0, and fails when `CI` is set. Held: lines 130-132; docs/01:69 "Without a list it is skipped locally and fails in Actions (`CI` set)".
* The docstring keeps that `--staged` and `--message <file>` fail when the list is missing or has no entry, whatever `CI` says. Held: line 130 skips only when `args` is empty; docs/01:67.
* The first paragraph (what it checks, where the list lives, the output format, exit 1 when anything is printed, the masked path) is unchanged.
* Fails: a docstring that still says, with no condition, that the run "fails when the hooks are off", or that leaves out the skip without a list.
* Edge: `FKB_DENYLIST=/nonexistent CI= python3 scripts/check_disclosure.py` prints `disclosure: skipped, no list` on standard error and exits 0; with `CI=1` it prints `/nonexistent:1: disclosure: list is missing or has no entry` and exits 1. The docstring agrees with both.
* Edge: with a list, `CI` unset and `GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.hooksPath GIT_CONFIG_VALUE_0=off` in the environment, the run prints `Makefile:1: disclosure: hooks are off; run make hooks` and exits 1; with `CI=1` added, that line is not printed. The docstring agrees with both.

**Contract.** None. The module docstring of `scripts/check_disclosure.py`, lines 2-13; no function, message, exit code or command changes. The wording, for /apply to adjust only for line length:

    With no argument it scans the files and every commit message. Without a list it is skipped
    locally (a note on standard error, exit 0) and fails when `CI` is set; with a list and without
    `CI` it also fails while the hooks are off.
    `--staged` scans the staged files (the pre-commit hook); `--message <file>` scans a commit message
    (the commit-msg hook). Both fail when the list is missing or has no entry.

**Out of scope.**

* The code of `check_disclosure.py`: it already matches docs/01.
* build-3, text detection on the first 8000 bytes: its own finding, not queued under this line.
* docs/01:67 and :69: they are the reference here, and correct.
* `docs/manuals/set-up-the-disclosure-list.md`: it states no condition this docstring changes.
* Any chapter: no chapter quotes the docstring, so neither edition changes.

**Done when.**

* [x] `grep -n "and fails when the hooks are off" scripts/check_disclosure.py` finds nothing; the docstring holds the conditions of the Behaviour.
* [x] The two `CI` edge runs and the two hooks-off edge runs print and exit as the Behaviour says, with the tree's git config unchanged (`git config core.hooksPath` still prints `.githooks`).
* [x] `make verify` green.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and only this line's hunk of docs/06; commit message in a `commit` block.

**In flight.** `work/batch-propose.md` is another draft and touches no script. The other M15 finding lines edit docs/03, docs/05, ADR-0017 and chapters, never `scripts/check_disclosure.py`, so this line runs in parallel with any of them (docs/05 §4).

**Divergences.** The docstring differs from the Contract's wording in one clause: "Without a list" became "Without a list file", and "a list file with no entry fails" was added. The Delivery review found that an existing but empty list fails the no-argument run even locally (lines 136-137), so the Contract's wording let a reader expect a skip; the Objective asks for every case. docs/01:69 has the same gap and is out of scope here: it became the queue line `docs01-empty-list`.

**Proof.** Run on the delivered docstring, with the tree's `core.hooksPath` unchanged (`.githooks` before and after):

* `grep -n "and fails when the hooks are off" scripts/check_disclosure.py`: nothing.
* `FKB_DENYLIST=/nonexistent CI=`: `disclosure: skipped, no list` on standard error, exit 0. With `CI=1`: `/nonexistent:1: disclosure: list is missing or has no entry`, exit 1.
* With the list, `CI` unset and `core.hooksPath=off` given through `GIT_CONFIG_COUNT`: `Makefile:1: disclosure: hooks are off; run make hooks`, exit 1. With `CI=1` added: no such line, exit 0.
* An empty list file, `CI` unset: `<path>:1: disclosure: list is missing or has no entry`, exit 1.
* `make verify`: green.

**Review.** A read-only Opus agent read this delivery's diff against the page and docs/04.

1. An empty list file was not covered by the no-argument paragraph. Fixed in the docstring (see Divergences); docs/01's same gap became `docs01-empty-list`.
2. The page cited line numbers from before the docstring grew. Fixed.
3. Not a finding: the usage error and an invalid pattern are covered by "exits 1 when anything is printed".

```commit
docs(disclosure-docstring): say when check_disclosure.py fails or skips

- No argument: skipped locally without a list file, fails with CI set
- An empty list file fails; hooks off fails only with a list and no CI
- --staged and --message fail when the list is missing or has no entry
- work/done/disclosure-docstring.md
```
