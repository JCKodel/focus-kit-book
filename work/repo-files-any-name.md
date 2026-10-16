# repo-files-any-name

**Objective.** Every check of `make verify` reads every tracked or untracked, not ignored file of the repository, whatever characters its name has, so a file named `café.md` is no longer skipped by the disclosure scan, the em dash check or the others.

**Behaviour.**

The proof uses a scratch clone and a made-up list (`FKB_DENYLIST` holding `zzqtestterm`), as `commit-hooks` did.

* A tracked file `café.md` whose text holds `zzqtestterm`: `python3 scripts/check_disclosure.py` prints `café.md:1: disclosure: matches list entry 1` and exits 1. Today it prints nothing, because `git ls-files` returns `"caf\303\251.md"` in quotes, no such file exists, and the name is dropped.
* An untracked `日本.md` holding an em dash: `python3 scripts/check_em_dash.py` prints `日本.md:1: em-dash: ...` and exits 1.
* A file whose name holds a double quote, a tab or a newline (`a"b.md`, `a<TAB>b.md`, `a<LF>b.md`) is listed with its real name and read, the same way.
* A name with a space or only ASCII (`a b.md`, `chapter.md`) lists as before: nothing changes for them.
* An ignored file (`.gitignore`) with a non-ASCII name stays out of the list; a tracked file deleted from the disk and not yet staged stays out (it is not a file).
* The listing is in git's order, as today, with paths relative to the repository root.
* A name that is not valid UTF-8 is not handled: `scan_staged` has the same limit, and the filesystem of the author (macOS) cannot hold one.

**Contract.**

`scripts/repo_files.py`, `repo_files() -> list[Path]`, signature and result unchanged.

* The command becomes `git ls-files -z --cached --others --exclude-standard`, run with `capture_output=True` and `check=True` as now, its bytes decoded as UTF-8 and split on `\0`, the empty tail dropped.
* A name is kept when `(ROOT / name).is_file()`, as now.
* No other script changes: `check_disclosure.py`, `check_em_dash.py`, `check_prose.py` and `check_links.py` import this function and need nothing.

Documents, in the same delivery: docs/01 line 39, the `scripts/repo_files.py` row, ends "whatever the characters of the name". docs/04 §Tests is unchanged (the checks are the tests).

**Out of scope.**

* A name that is not valid UTF-8: no file of the book has one.
* A new test directory or test runner: docs/04 §Tests says the checks are the tests, and docs/05 §7 asks for the error a new check would have caught; the proof is the scratch clone.
* What each check does with the files it receives (`em-dash-every-text`, `links-url-bounds` and the others are their own lines).
* `scan_staged` and the pre-commit hook: they already use `-z`.

**Done when.**

* [ ] In a scratch clone, the four Behaviour cases with a non-ASCII or special name print the findings above, and the same files give no finding before the change; both outputs are recorded on the page.
* [ ] `make verify` green in the repository, and `python3 scripts/check_disclosure.py` still prints nothing on the clean tree.
* [ ] docs/01 line 39 updated.
* [ ] No output shows a term of the real list.

**Decisions in the review.**

* `-z` and a strict UTF-8 decode, not `-c core.quotePath=false`: the quotePath switch still quotes a name with a quote, tab or newline, and `scan_staged` already uses `-z`, so the two listings read names one way (docs/01, `.githooks/pre-commit` row; recommendation of this session).
* A non-UTF-8 name is out of scope instead of decoded with surrogate escapes: printing such a name would raise instead of printing `file:line: rule: message` (docs/01).
* No test file: docs/04 §Tests; the proof lives on the page after `/apply`, as in `commit-hooks`.
