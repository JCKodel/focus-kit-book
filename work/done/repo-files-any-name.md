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

* [x] In a scratch clone, the four Behaviour cases with a non-ASCII or special name print the findings above, and the same files give no finding before the change; both outputs are recorded on the page.
* [x] `make verify` green in the repository, and `python3 scripts/check_disclosure.py` still prints nothing on the clean tree.
* [x] docs/01 line 39 updated.
* [x] No output shows a term of the real list.

**Decisions in the review.**

* `-z` and a strict UTF-8 decode, not `-c core.quotePath=false`: the quotePath switch still quotes a name with a quote, tab or newline, and `scan_staged` already uses `-z`, so the two listings read names one way (docs/01, `.githooks/pre-commit` row; recommendation of this session).
* A non-UTF-8 name is out of scope instead of decoded with surrogate escapes: printing such a name would raise instead of printing `file:line: rule: message` (docs/01).
* No test file: docs/04 §Tests; the proof lives on the page after `/apply`, as in `commit-hooks`.

## What happened

**The error it catches** (docs/05 §7): `git ls-files` without `-z` quotes a name with a non-ASCII character, a double quote, a tab or a newline, so `repo_files()` looked for a file named `"caf\303\251.md"`, found none and dropped it; every check then skipped that file in silence.

**Built.** `scripts/repo_files.py` runs `git ls-files -z --cached --others --exclude-standard` with `capture_output=True` and `check=True`, decodes the bytes as UTF-8, splits on `\0` and drops the empty tail; a name is kept when `(ROOT / name).is_file()`. The signature and the result type are unchanged, and no check that imports it changed.
docs/01, the `scripts/repo_files.py` row, ends "whatever the characters of the name".
No abstraction: the NUL split already exists in `scan_staged` (the first occurrence), but the two read different listings (`git diff --cached -z` there), so nothing is shared yet.

**Diverged from the contract.** Nothing.

**Proof.** A scratch clone of this repository at the commit before this delivery, `core.hooksPath` set, the test list `FKB_DENYLIST=$S/testlist.txt` holding `# test list` and `zzqtestterm` (entry 2). `$S` is the session's scratch directory. In the clone:

* tracked and committed: `café.md` holding the test term; `a"b.md`, `a<TAB>b.md`, `a<LF>b.md`, `a b.md` and `chapter.md`, each one line holding the test term and an em dash;
* untracked: `日本.md` holding an em dash;
* ignored through `.git/info/exclude`: `ignoré.md` holding the test term;
* tracked, then deleted from the disk and not staged: `gone.md`.

The test term also appears in this repository's own pages under `work/` (this one included), so each check's output is filtered with `grep -v ^work/`; the exit code is the check's own. Section 3 calls `repo_files()` and says, for each name, whether it is listed.

Before the change (the clone's own `scripts/repo_files.py`):

```
== 1 tracked café.md holding the test term
$ python3 scripts/check_disclosure.py | grep -v ^work/
a b.md:1: disclosure: matches list entry 2
chapter.md:1: disclosure: matches list entry 2
[exit 1]
== 2 untracked 日本.md holding an em dash
$ python3 scripts/check_em_dash.py | grep -v ^work/
a b.md:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
chapter.md:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
[exit 1]
== 3 names with a double quote, a tab, a newline, a space, ASCII only: repo_files()
'café.md' absent
'日本.md' absent
'a"b.md' absent
'a\tb.md' absent
'a\nb.md' absent
'a b.md' listed
'chapter.md' listed
'ignoré.md' absent
'gone.md' absent
quoted names: []
```

After the change (this delivery's `scripts/repo_files.py` copied into the clone):

```
== 1 tracked café.md holding the test term
$ python3 scripts/check_disclosure.py | grep -v ^work/
a	b.md:1: disclosure: matches list entry 2
a
b.md:1: disclosure: matches list entry 2
a b.md:1: disclosure: matches list entry 2
a"b.md:1: disclosure: matches list entry 2
café.md:1: disclosure: matches list entry 2
chapter.md:1: disclosure: matches list entry 2
[exit 1]
== 2 untracked 日本.md holding an em dash
$ python3 scripts/check_em_dash.py | grep -v ^work/
日本.md:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
a	b.md:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
a
b.md:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
a b.md:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
a"b.md:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
chapter.md:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
[exit 1]
== 3 names with a double quote, a tab, a newline, a space, ASCII only: repo_files()
'café.md' listed
'日本.md' listed
'a"b.md' listed
'a\tb.md' listed
'a\nb.md' listed
'a b.md' listed
'chapter.md' listed
'ignoré.md' absent
'gone.md' absent
quoted names: []
```

Every special name is listed and read after the change and none before; `a b.md` and `chapter.md` give the same findings in both; the ignored and the deleted files stay out.
In this repository, the old and the new `repo_files()` return the same 759 paths in the same order, so git's order and the relative paths are unchanged.
`make verify` is green, and `python3 scripts/check_disclosure.py` with the real list prints nothing and exits 0. No output above or in the session showed a term of the real list.

**Noted, not fixed.** A name holding a newline prints its finding over two lines (`a` and `b.md:1: ...`), since each check prints the name as it is. What a check prints for the files it receives is out of this page's scope, no file of the book has such a name, and the author's filesystem allows one only by intent.

**Dropped.** Nothing.

**Decisions.**

* No screenshot: docs/05 §5 asks one of a toolchain delivery's rendered site, and this one changes nothing the site renders; the proof is the scratch clone, as the page says.
* The proof output is filtered to leave out the repository's own `work/` pages, which quote the test term; the exit code shown is the check's, taken before the filter.
* No queue line for the newline case above: the page puts what a check prints out of scope and names no such file.
* No ADR: the change applies docs/01's listing rule to every name and changes no decision.

```commit
fix(repo-files-any-name): list every file whatever its name holds

- repo_files reads git ls-files -z, decoded as UTF-8
- a name with an accent, a quote, a tab or a newline is checked again
- docs/01: the repo_files row says so

work/done/repo-files-any-name.md
```
