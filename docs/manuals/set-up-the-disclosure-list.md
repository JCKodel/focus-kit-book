# Set up the disclosure list

## What it does and when

The disclosure list holds the terms that must never appear in this repository: names, places and paths of the book's private cases (ADR-0012).
It lives outside the repository, so it is never published.
`make scan`, part of `make verify`, fails when a file, a file path or a commit message matches it; the hooks refuse such a commit before it exists; Actions runs the same scan with the list from a secret.
Set it up once per machine (the file), once per clone (the hooks) and once per repository (the secret).
Ask the author for the list's contents; this manual never shows them.

## What must be in place

* The list's contents, from the author, through a private channel.
* Python 3, which `make verify` already needs.
* For the secret: admin rights on `JCKodel/focus-kit-book`.

## Steps

1. Write the list to `~/.config/focus-kit-book/denylist.txt`, or anywhere outside the repository with `FKB_DENYLIST` set to its path in your shell.
   One entry per line. A line starting with `#` is a comment; an empty line is ignored.
   A plain entry matches without regard to case and not inside a longer word, and its apostrophe, `'` or `’`, matches either; `re:<pattern>` is a regular expression, also without regard to case, that spells both apostrophes when it wants both, as `(’|')`.
2. In the clone, once: `make hooks`.
   It sets `core.hooksPath` to `.githooks`, whose pre-commit hook checks the staged paths and text and whose commit-msg hook checks the message.
3. Once per repository: Settings, Secrets and variables, Actions, a repository secret named `DISCLOSURE_DENYLIST` holding the whole list, the same text as the file.
   When the list changes, update the file and the secret together.

## How to tell it worked

`make scan` prints nothing and exits 0.
A finding names the file, the line and the entry's number in the list, never the term; a matched part of a path prints as `***`.
An invalid `re:` entry prints its line in the list as a finding.
In Actions, the job `verify` passes its disclosure step.

## How to undo it

* The hooks: `git config --unset core.hooksPath`.
* The list on this machine: delete the file, or unset `FKB_DENYLIST`.
* The secret: delete it in the repository's settings; the job `verify` then fails on every push.

## What breaks if a step is skipped

* No list on the machine: `make scan` is skipped locally, so a private term can be committed unseen, and the hooks refuse every commit.
* No `make hooks`: `make verify` fails with `Makefile:1: disclosure: hooks are off; run make hooks`.
* No secret: the job `verify` fails in Actions, so the site is not published and no Release is built.
* A secret older than the file: Actions passes a term the local scan refuses, or the other way round.
* `git commit --no-verify`: the hooks are skipped, and the next `make scan` finds the commit's message or files.
