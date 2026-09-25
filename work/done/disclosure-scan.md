# disclosure-scan

**Objective.** The author runs `make scan`, or `make verify`, and it fails when any term of the disclosure list appears in a file name or a text file of the repository, locally and in GitHub Actions on every push, and it never shows the term it found.

**Behaviour.**

* With the list at `~/.config/focus-kit-book/denylist.txt`, or at the path in `FKB_DENYLIST`, `make scan` on the clean tree is green and exits 0.
* A listed term written in any tracked or untracked, not ignored, text file makes `make scan` print `file:line: disclosure: matches list entry N` and exit 1, so the author catches it before staging.
* A listed term in a file path (any file, images included) gives the same finding at line 1, with the matched part of the path shown as `***`.
* The finding names the file, the line and the entry's line number in the list; it never prints the term or the matched text, because Actions logs of a public repository are public.
* A plain entry matches regardless of case, and does not match inside a longer word: the entry `acme` finds `Acme` and `ACME Ltd` but not `acmeology`; the entry `10.0.0.` finds `10.0.0.7`.
* An entry `re:<pattern>` matches as a Python regular expression, regardless of case: `re:ref-\d{3}` finds `REF-123`.
* Blank lines and lines starting with `#` in the list are ignored.
* Without a list, locally, `make scan` prints `disclosure: skipped, no list` on stderr and exits 0, so a contributor still runs every other check (ADR-0012).
* In Actions (`CI` set), a missing list, or a list with no entry, is a finding and exits 1, so a missing secret never passes in silence.
* A list that exists but has no entry fails locally too; an invalid `re:` entry is a finding at its line in the list.
* `make verify` runs, in order, build, parity, em dash, disclosure, and stops at the first failing group.
* Every push to GitHub runs `make verify` with the list taken from the secret `DISCLOSURE_DENYLIST`.

**Contract.**

Files:

```
scripts/check_disclosure.py    rule "disclosure"; Python 3 standard library only
scripts/repo_files.py          the file listing, shared with check_em_dash.py (added in /apply)
Makefile                       target scan; verify runs it after em dash
.github/workflows/verify.yml   make verify on every push, with the list from the secret
docs/01-Architecture.md        tree, targets and Environments updated
README.md, README.pt.md        one line: the scan needs a list only the author has; without it, it is skipped
```

`scripts/check_disclosure.py`:

* List path: `FKB_DENYLIST` when set and not empty, else `~/.config/focus-kit-book/denylist.txt`. UTF-8.
* Entry: each line, stripped of surrounding whitespace; skipped when empty or starting with `#`.
  Its number is its line number in the list file.
* Plain entry: `re.escape(entry)`, compiled with `re.IGNORECASE`; `(?<!\w)` in front when its first character is a word character, `(?!\w)` after when its last character is.
* `re:` entry: the rest of the line compiled as is, with `re.IGNORECASE`.
* Files: `git ls-files --cached --others --exclude-standard`, as `check_em_dash.py`.
  Every path is matched against every entry.
  Content is matched line by line for every file that decodes as UTF-8 and has no NUL byte; other files are skipped.
* Output, one line per finding, on stdout:

```
<file>:<line>: disclosure: matches list entry <N>
<file>:1: disclosure: file path matches list entry <N>
<list>:<N>: disclosure: invalid regular expression
<list>:1: disclosure: list is missing or has no entry
```

* `<file>` is printed with every part that matches an entry replaced by `***`, so a path finding does not show the term either (decided in /apply).
* Exit: 0 when there is no finding, or when there is no list and `CI` is not set (stderr: `disclosure: skipped, no list`); 1 otherwise.

`Makefile`:

```
scan:
	python3 scripts/check_disclosure.py
```

`verify` gains the line `python3 scripts/check_disclosure.py` after the em dash check; `scan` joins `.PHONY`.

`.github/workflows/verify.yml`:

* `name: verify`; `on: push` (every branch); `permissions: contents: read`; one job on `ubuntu-latest`.
* Steps: checkout; set up Python 3; write the secret `DISCLOSURE_DENYLIST`, passed through `env`, to `$RUNNER_TEMP/denylist.txt` with `printf '%s'`, never echoed; `make verify` with `FKB_DENYLIST=$RUNNER_TEMP/denylist.txt`.
* `pages-and-release` extends this file with the Pages deploy and the Release; it does not create a second verify.

Author steps, outside the repository (the agent never writes these terms in the repository, a page or a commit message):

* Write `~/.config/focus-kit-book/denylist.txt` with the private terms; `/apply` may create it from the author's seed, with the author's go-ahead.
* Add its content as the repository secret `DISCLOSURE_DENYLIST` (`gh secret set DISCLOSURE_DENYLIST < ~/.config/focus-kit-book/denylist.txt`), then push.

Examples on this page and in the proof use made-up entries only (`acme`, `10.0.0.`, `re:ref-\d{3}`).

**Out of scope.**

* `pull_request` runs: pull requests from forks get no secrets, so the scan would always fail there.
* Scanning commit messages on every verify: a finding in history would stay red forever.
* A pre-commit hook: no error has asked for one yet (docs/05 §7).
* Text inside images (PNG screenshots): the author reviews each proof image.
* An allowlist for false positives: added when the first one happens.
* Rewriting history if the one-time audit finds a term: the author decides, and it becomes its own queue line.

**Done when.**

* [x] With a scratch list holding one made-up entry per kind (plain word, prefix ending in a dot, `re:`), a term planted in an untracked file and in a file name gives the findings above and exit 1; removed, the scan is green. Output recorded in the page, no real term in it.
* [x] Without a list: exit 0 with the stderr line; with `CI=true` and no list: exit 1; with an empty list: exit 1; with an invalid `re:` entry: exit 1.
* [x] No finding prints the term or the matched text.
* [x] One-time audit: every commit message and diff in `git log --all -p` scanned against the author's real list; recorded as "N commits scanned, M findings", with list entry numbers only.
* [x] `make verify` green locally with the real list, stopping at disclosure when a term is planted.
* [x] docs/01 and both READMEs updated; docs/06 line marked `[x]`.
* [x] Author, after the commit: secret set, push, the `verify` run green in Actions (run 36132817580, 2026-09-25).

**What happened.**

Diverged from the plan:

* A path finding would have printed the term inside the file name, against the Objective ("it never shows the term it found"). The author chose to mask it: every part of a printed path that matches an entry is shown as `***`. Behaviour and Contract above say so.
* `scripts/repo_files.py` is new: the `git ls-files --cached --others --exclude-standard` listing was the second concrete occurrence (the first is `check_em_dash.py`), so both checks now import it.
* The proof used the made-up entries `zorblat`, `172.31.254.` and `re:zq-\d{4}` instead of `acme`, `10.0.0.` and `re:ref-\d{3}`: this page is scanned too and holds those examples, so a scratch list with them could never be green. The page's own examples were checked directly against the entry compiler: `acme` finds `Acme` and `ACME Ltd`, not `acmeology`; `10.0.0.` finds `10.0.0.7`; `re:ref-\d{3}` finds `REF-123`.

Nothing dropped.

The proof found (scratch lists outside the repository, shown as `<scratch>`):

```
list: zorblat (entry 3), 172.31.254. (entry 4), re:zq-\d{4} (entry 5)

clean tree                       exit 0, no output
planted.md (3 lines) and notes-zorblat.png, both untracked:
notes-***.png:1: disclosure: file path matches list entry 3
planted.md:2: disclosure: matches list entry 3
planted.md:3: disclosure: matches list entry 4
planted.md:3: disclosure: matches list entry 5
                                 exit 1
both removed                     exit 0, no output

no list                          stderr "disclosure: skipped, no list", exit 0
CI=true, no list                 ~/.config/focus-kit-book/denylist.txt:1: disclosure: list is missing or has no entry, exit 1
list with only a comment         <scratch>/empty.txt:1: disclosure: list is missing or has no entry, exit 1
entry 2 is re:zq-(\d            <scratch>/bad.txt:2: disclosure: invalid regular expression, exit 1
```

* `planted.md` line 2 held `Zorblat`, `ZORBLAT Ltd` and `zorblatology`; a line with only `zorblatology` gives no finding.
* The real list was created by /apply from the author's seed, with the author's go-ahead, at `~/.config/focus-kit-book/denylist.txt`. Seed items that were descriptions became `re:` entries (org ids, requirement codes, a generic GUID pattern); an identifier prefix ending in `_` is a `re:` entry, because a plain entry gets a word boundary after its last word character and would not match inside an identifier. One seed item, a host name, stays out until the author gives its exact value.
* `make scan` and `make verify` green on the working tree with the real list. With list entry 5 planted in an untracked file, `make verify` ran build, parity and em dash, then stopped at `planted.md:1: disclosure: matches list entry 5`, exit 2 from make; removed, green.
* One-time audit, every commit message and patch of `git rev-list --all`: 5 commits scanned, 0 findings.
* A missing secret in Actions writes an empty file, which the "no entry" rule turns into a finding.
* No screen changes, so no screenshot: the proof is the runs above.
* While building, the `\u2014` escape in `check_em_dash.py` was written back as a literal em dash by the editor, and `make verify` caught it at that line; restored to the escape.
* Importing `repo_files.py` makes Python write `scripts/__pycache__/`; it is now in `.gitignore` and in the docs/01 tree.

Decisions: masking matched parts of a path (author, in /apply); no ADR, the rule lives in docs/01 and in this page.

Documents this delivery changed: `.gitignore`, docs/01 (tree, `make verify` and `make scan`, Automation, Environments), `README.md` and `README.pt.md` (one line under Build locally), docs/06.
