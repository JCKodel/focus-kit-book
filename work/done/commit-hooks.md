# commit-hooks

**Objective.** A commit whose message or staged files contain a term of the disclosure list is refused on the author's machine before it exists, and `make verify` finds any such message already in the history.

**Behaviour.**

* `make hooks`, run once in a clone, turns the repository's hooks on.
* A commit whose message matches a list entry is refused; the finding names the line and the entry's number, never the term.
* A commit whose staged files match a list entry, in a path or in the staged text, is refused the same way, even when `make verify` was not run.
* A commit made while the list is missing is refused, and the message says the list is missing.
* A clean commit goes through with no output.
* `make verify` and `make scan` also check the message of every commit in the history; a match fails them, locally and in Actions.
* On a machine that has the list, `make verify` fails while the hooks are off, and says to run `make hooks`.
* `git commit --no-verify` still goes through (git's own escape); the history check then finds the commit.

**Contract.**

Files:

```
.githooks/pre-commit     python3 scripts/check_disclosure.py --staged
.githooks/commit-msg     python3 scripts/check_disclosure.py --message "$1"
```

Both executable, POSIX `sh`, no dependency beyond `python3` and the standard library.

`scripts/check_disclosure.py` modes (the list is found as today: `FKB_DENYLIST`, else `~/.config/focus-kit-book/denylist.txt`):

| Invocation | Scans | Missing list |
|---|---|---|
| no argument (today) | tracked and untracked files, paths and text, then every commit message (`git log --format=%H%x00%B%x00`) | skipped locally, fails with `CI` set (unchanged) |
| `--staged` | each added, copied, modified or renamed staged path, and its staged text (`git show :<path>`) | always fails |
| `--message <file>` | the lines of `<file>`, skipping lines that start with `#` (git's comments) | always fails |

Findings, one per line, exit 1 when any is printed:

```
<path>:<line>: disclosure: matches list entry <n>                 files and staged files, as today
<path>:1: disclosure: file path matches list entry <n>            paths, as today; matched part masked as ***
<message file>:<line>: disclosure: matches list entry <n>         --message; <message file> as given
<sha, 12 chars>:<line>: disclosure: commit message matches list entry <n>   history; <line> counts from the subject, 1
<list path>:1: disclosure: list is missing or has no entry        as today
Makefile:1: disclosure: hooks are off; run make hooks             no argument, list present, core.hooksPath is not .githooks, CI not set
```

Makefile: new target `hooks`, which runs `git config core.hooksPath .githooks`.

`.github/workflows/verify.yml`: the `verify` job's checkout gets `fetch-depth: 0`, so the history check sees every commit.

**Out of scope.**

* Rewriting history: it holds no match today (checked on 2026-09-25), and a later match is fixed by hand.
* Pull request text: the project works on trunk (ADR-0010) and opens no pull requests.
* A server-side hook: GitHub.com does not run pre-receive hooks.
* Hooks for the guided project's repository: it has its own process.

**Done when.**

* [x] A test commit in a scratch clone proves each Behaviour line: message match refused, staged path match refused, staged text match refused, missing list refused, clean commit accepted, `--no-verify` accepted and then found by `make scan`; the outputs are recorded on this page with the terms replaced by a harmless test list (`FKB_DENYLIST`).
* [x] No output shows a term of the real list.
* [x] `make verify` green with the hooks on, and failing with the hooks off.
* [x] docs/01 (file list, the `hooks`, `scan` and `verify` rows), docs/05 §Disclosure, docs/04 (the checks) and both READMEs updated to say the hooks exist and how to turn them on.

## What happened

**The error it catches** (docs/05 §7): a commit message once carried a term of the list; the file scan cannot see a message, and Actions sees it only after the push.

**Built.** `scripts/check_disclosure.py` gains `--staged`, `--message <file>`, the history check and the hooks-off check; `.githooks/pre-commit` and `.githooks/commit-msg`; `make hooks`; `fetch-depth: 0` on the `verify` job.
The line loop (`scan_lines`) was factored on its second occurrence: the first was the file scan, the second the commit message; staged text and history reuse it.
The path-and-text scan (`scan_file`) is shared by the file scan and `--staged`.

**Diverged from the contract.**

* `--message` also stops at git's scissors line (`# ---...--- >8 ---...---`). With `git commit -v` the message file carries the staged diff below it, so a commit that removes a term would have been refused for the removed line; the staged text itself is checked by the pre-commit hook.
* The history check returns nothing in a repository with no commit yet, so the first commit of a fresh clone does not fail on `git log`.
* An unknown argument prints `Makefile:1: disclosure: usage: ...` and exits 1, in the convention of docs/01.

**Proof.** A scratch clone of this repository with the delivery's files, the test list `FKB_DENYLIST=$S/testlist.txt` holding `# test list` and `zzqtestterm` (entry 2), `make hooks` run there. `$S` is the session's scratch directory.

```
== 1 message match (staged file clean)
$ git commit -q -m "chore: note zzqtestterm"
.git/COMMIT_EDITMSG:1: disclosure: matches list entry 2
[exit 1]

== 2 staged path match
$ git commit -q -m "chore: add notes"
***-notes.txt:1: disclosure: file path matches list entry 2
[exit 1]

== 3 staged text match
$ git commit -q -m "chore: add notes"
notes.txt:2: disclosure: matches list entry 2
[exit 1]

== 4 missing list (FKB_DENYLIST=$S/nope.txt)
$ git commit -q -m "chore: add a"
$S/nope.txt:1: disclosure: list is missing or has no entry
[exit 1]

== 5 clean commit
$ git commit -q -m "chore: add a"
[exit 0]

== 6 --no-verify, then make scan
$ git commit -q --no-verify -m "chore: add b" -m "about zzqtestterm"
[exit 0]
$ make scan
python3 scripts/check_disclosure.py
b.txt:1: disclosure: matches list entry 2
72becbf3d29a:3: disclosure: commit message matches list entry 2
make: *** [scan] Error 1

== 7 hooks off (git config --unset core.hooksPath)
$ make scan
python3 scripts/check_disclosure.py
72becbf3d29a:3: disclosure: commit message matches list entry 2
Makefile:1: disclosure: hooks are off; run make hooks
make: *** [scan] Error 1

== 8 git commit -v removing a line that holds the term
[exit 0]   the message file held the term once, below the scissors line
```

In this repository, with the real list: `make scan` with the hooks off printed only `Makefile:1: disclosure: hooks are off; run make hooks`; after `make hooks`, `make verify` was green, so the history holds no match.
With `core.hooksPath` unset, `make verify` failed at the disclosure step with the same line; `make hooks` turned them back on.
No output above or in the session showed a term of the real list.

**Dropped.** Nothing.

**Decisions.** No ADR: the hooks apply ADR-0012 at one more moment and change none of its reasons.
The README says only the author turns the hooks on, since they refuse every commit without the list.

