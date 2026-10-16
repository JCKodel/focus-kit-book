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

* [ ] In a scratch clone, each Behaviour line gives the result above, the outputs recorded on this page with the made-up list.
* [ ] `make verify` green with the hooks on; no output shows a term of the real list.
* [ ] docs/01's `.githooks/commit-msg` row updated.

**Decisions in the review.**

* Scan every line before the scissors line instead of trying to recognise git's template: the hook gets only a file path, and a hook weaker than the history scan is the error this line exists for (docs/04 §Tests: a message once carried a term).
* A term in git's own comment lines (branch, untracked paths) is refused with the message file's line number: accepted cost of the previous decision; the same term in a path already fails `make scan` (docs/05 §5 Disclosure).
* The scissors line stays the one place the hook stops, as `commit-hooks` decided in `/apply`.
