# hook-hash-lines

**Objective.** The commit-msg hook refuses a commit whose message holds a term of the disclosure list on any line it will store, including a line that starts with `#`, so `git commit -m "# <term>"` no longer gets through.

**Behaviour.**

The proof uses a scratch clone with `make hooks` run and a made-up list (`FKB_DENYLIST` holding `# test list` and `zzqtestterm`, entry 2), as `commit-hooks` did.

* `git commit -m "# zzqtestterm"` (staged files clean): refused, `.git/COMMIT_EDITMSG:1: disclosure: matches list entry 2`, exit 1. Today it is accepted, because `git commit -m` stores every line, `#` lines included (cleanup is `whitespace` when the message is given with `-m` or `-F`), and the hook skips them.
* `git commit -m "chore: note" -m "# zzqtestterm"`: refused, at line 3 of the message file.
* `git commit -m "chore: note" -m "# a heading"` with no term: accepted, nothing printed.
* A commit made in the editor, whose message file starts with the author's text and then holds git's own `#` lines (the branch, the paths): a term in the author's text is refused as today. A term in git's own lines, such as a branch name that matches, is refused too: the hook cannot tell git's lines from the author's, and the same term in a path is a finding of `make scan` anyway. The finding names the line of the message file, never the term.
* `git commit -v`: the message file carries the staged diff below the scissors line (`# ------------------------ >8 ------------------------`); the hook still stops there, so a commit that removes a term is not refused for the removed line. The staged text itself is the pre-commit hook's.
* `git commit --no-verify` still skips the hook, and `make scan` still finds the message in the history, where it already reads every stored line.
* A clean message in any of these forms prints nothing and exits 0.

**Contract.**

`scripts/check_disclosure.py`, `scan_message(entries, name)`: reads the file, stops at the line equal to `SCISSORS`, and scans every other line, `#` lines included; line numbers are the message file's. Output and exit codes unchanged (`<file>:<line>: disclosure: matches list entry <N>`; the term is never shown).

Nothing else changes: `.githooks/commit-msg`, `--message <file>`, `--staged`, the history scan.

Documents, in the same delivery: docs/01, the `.githooks/commit-msg` row, now "the commit message, `#` lines included, without the diff below the scissors line of commit -v". docs/04 §Tests, docs/05 §5 Disclosure and the manual say "the message", which stays true.

**Out of scope.**

* Telling git's comment lines from the author's: there is no signal in the hook's argument, and the stricter reading costs only a refusal the author can read.
* A scissors line typed inside a `-m` message, which hides what follows it: nobody writes it by accident; the history scan still reads it.
* `core.commentChar` other than `#`: the hook no longer cares which character a line starts with.
* The history scan and the pre-commit hook: they already read every line.

**Done when.**

* [x] In a scratch clone, each Behaviour line gives the result above, the outputs recorded on this page with the made-up list.
* [x] `make verify` green with the hooks on; no output shows a term of the real list.
* [x] docs/01's `.githooks/commit-msg` row updated.

**Decisions in the review.**

* Scan every line before the scissors line instead of trying to recognise git's template: the hook gets only a file path, and a hook weaker than the history scan is the error this line exists for (docs/04 §Tests: a message once carried a term).
* A term in git's own comment lines (branch, untracked paths) is refused with the message file's line number: accepted cost of the previous decision; the same term in a path already fails `make scan` (docs/05 §5 Disclosure).
* The scissors line stays the one place the hook stops, as `commit-hooks` decided in `/apply`.

**The error it catches** (docs/05 §7): the commit-msg hook skipped every line starting with `#`, but `git commit -m` stores those lines (cleanup is `whitespace` for `-m` and `-F`), so `git commit -m "# <term>"` put a term of the list in the history with the hooks on, and only `make scan` found it afterwards.

**Built.** `scan_message` in `scripts/check_disclosure.py` no longer drops the lines starting with `#`: it reads the message file up to the line equal to `SCISSORS` and scans every line before it, with the file's line numbers. Output, exit codes, `.githooks/commit-msg`, `--staged` and the history scan are unchanged. docs/01's `.githooks/commit-msg` row says "the commit message, # lines included, without the diff below the scissors line of commit -v".

**Diverged from the contract.** Nothing.

**Proof.** Two scratch clones of this repository at HEAD (6665818), `make hooks` run in each, the test list `FKB_DENYLIST=$S/testlist.txt` holding `# test list` and `zzqtestterm` (entry 2); `$S` is the session's scratch directory. One clone keeps the old `check_disclosure.py` (before), the other gets this delivery's (after). Every commit stages a clean change to `proof.txt` first. The editor cases set `GIT_EDITOR` to a script that writes the author's text above git's own template, so the message file holds the author's text and then git's `#` lines.

Before:

```
== 1
$ git commit -q -m "# zzqtestterm"
[exit 0]
== 2
$ git commit -q -m "chore: note" -m "# zzqtestterm"
[exit 0]
== 3
$ git commit -q -m "chore: note" -m "# a heading"
[exit 0]
== 4a editor, term in the author's text
$ git commit -q
.git/COMMIT_EDITMSG:1: disclosure: matches list entry 2
[exit 1]
== 4b editor, clean text, branch zzqtestterm
$ git commit -q
[exit 0]
== 4c editor, clean text
$ git commit -q
[exit 0]
== 5 commit -v removing the term (added first with --no-verify)
$ git commit -q -v
[exit 0]
```

After:

```
== 1
$ git commit -q -m "# zzqtestterm"
.git/COMMIT_EDITMSG:1: disclosure: matches list entry 2
[exit 1]
== 2
$ git commit -q -m "chore: note" -m "# zzqtestterm"
.git/COMMIT_EDITMSG:3: disclosure: matches list entry 2
[exit 1]
== 3
$ git commit -q -m "chore: note" -m "# a heading"
[exit 0]
== 4a editor, term in the author's text
$ git commit -q
.git/COMMIT_EDITMSG:1: disclosure: matches list entry 2
[exit 1]
== 4b editor, clean text, branch zzqtestterm
$ git commit -q
.git/COMMIT_EDITMSG:6: disclosure: matches list entry 2
[exit 1]
== 4c editor, clean text
$ git commit -q
[exit 0]
== 5 commit -v removing the term (added first with --no-verify)
$ git commit -q -v
[exit 0]
== 6 --no-verify, then make scan
$ git commit -q --no-verify -m "# zzqtestterm"
[exit 0]
$ make scan
python3 scripts/check_disclosure.py
work/done/commit-hooks.md:78: disclosure: matches list entry 2
work/done/commit-hooks.md:82: disclosure: matches list entry 2
work/done/commit-hooks.md:106: disclosure: matches list entry 2
work/done/repo-files-any-name.md:7: disclosure: matches list entry 2
work/done/repo-files-any-name.md:9: disclosure: matches list entry 2
work/done/repo-files-any-name.md:57: disclosure: matches list entry 2
work/hook-hash-lines.md:7: disclosure: matches list entry 2
work/hook-hash-lines.md:9: disclosure: matches list entry 2
work/hook-hash-lines.md:10: disclosure: matches list entry 2
55cbf9dac0c6:1: disclosure: commit message matches list entry 2
make: *** [scan] Error 1
[exit 2]
```

Cases 1 and 2 were accepted before and are refused after, at the message file's line; case 4b, a branch named after the term with clean author text, is refused at line 6, git's `# On branch` line, as the Behaviour accepts. In case 5 a copy of the message file showed the scissors line at line 15 and the removed `-zzqtestterm` at line 24, below it: accepted. In case 6 the file findings are this repository's own proof pages, which name the made-up test term; the one commit finding is the `--no-verify` commit, so the history scan reads the `#` line. In the before clone, `make scan` also listed the commits of cases 1 and 2, which the old hook had let through.
In this repository, with the real list and the hooks on, `make verify` is green, and the suggested commit message below passes `python3 scripts/check_disclosure.py --message`. No output above or in the session showed a term of the real list.

**Dropped.** Nothing.

**Decisions.**

* docs/01's row stands inside the fenced tree, where backticks print as they are, so it reads "# lines included" without them, as its old text wrote "git's # lines" (decided in this session, not asked).
* No screenshot: docs/05 §5 asks one of a toolchain delivery's rendered site, and this one changes nothing the site renders; the proof is the scratch clone, as the page says.
* The editor cases use a `GIT_EDITOR` script that writes the author's text above git's own template, so the hook sees the file git really writes in an editor commit.
* docs/04 §Tests, docs/05 §5 Disclosure and `docs/manuals/set-up-the-disclosure-list.md` say "the message" and stay as they are; no ADR, since ADR-0012's decision does not change.
* No queue line depends on this one.

```commit
fix(hook-hash-lines): scan the message's # lines in the commit-msg hook

- check_disclosure --message scans every line before the scissors line
- git commit -m "# <term>" is refused, at the message file's line
- docs/01's commit-msg row says # lines are included

work/done/hook-hash-lines.md
```
