# m4-code-review run

The code review of this book's milestone M4, for chapter 23: `/code-review high` reviews the clinic's code that M4 added, the author decides each finding, and the confirmed ones become lines in the book's M4.1. It is the second occurrence of a milestone's code review, after chapter 12's (`../closing-a-milestone-run/`), and the first run of the recipe that this delivery wrote into docs/05 §8 before turn 1. The delivery that planned and recorded it is `../m4-code-review.md`.

* Host: Claude Code, `claude --version` printed `2.1.285 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Date: 2026-09-29.
* The book before the run: on `main` at `05244c6`, with this delivery's changes not yet committed: the `[>] m4-code-review` line of docs/06, `work/m4-code-review.md`, and the recipe added to docs/05 §8 before turn 1. `make verify` green.
* The clinic before the run: on `main`, clean, at `a3e2470`, equal to `origin/main`.

## The range and the target form

`c54d011...e6653b5`: `c54d011` is `book-v1/closing-a-milestone`, the last chapter tag of M3, and `e6653b5` is `book-v1/four-pieces`, the last chapter tag of M4 (chapter 16 has no tag). The range holds one commit, `clinic-orchestrator-tests` ("Move each client hook's events into tested plain functions"): 28 files, 2987 insertions, 697 deletions (`git diff --stat`).

The one commit of the milestone past the last tag is `a3e2470` ("Update focus-kit to bff8414"), made by `kit-milestone-review`: 14 files, the kit's, `docs/05` and `docs/06`, none in `src/`. It is not reviewed: it is not the clinic's code, and the tree the review read differs from `e6653b5` only there.

The target form is the ref range in the form of Claude Code's documentation, three dots, as chapter 12's run README explains: "To review something else, pass a target: a file path, a PR number, a branch name, or a ref range such as `main...my-feature`" (https://code.claude.com/docs/en/code-review#review-a-diff-locally). `c54d011` is an ancestor of `e6653b5`, so the merge base is `c54d011` and the diff is the one commit.

## The `--add-dir` check

Checked from Claude Code's documentation, without running a review, before turn 1:

* The CLI reference: `--add-dir` "Add[s] additional working directories for Claude to read and edit files" (https://code.claude.com/docs/en/cli-reference).
* The permissions page: "Files in additional directories follow the same permission rules as the original working directory: they become readable without prompts, and file editing permissions follow the current permission mode", and `acceptEdits` "Automatically accepts file edits … for paths in the working directory or `additionalDirectories`" (https://code.claude.com/docs/en/permissions).
* The same page: a Bash rule without a wildcard, such as `Bash(git -C ../focus-kit-book add docs/06-Queue.md)`, matches that command exactly, and a trailing ` *` matches any arguments.

So `Read` and `Edit` reach the book's docs/06 under `acceptEdits`, and the three `git -C` rules allow staging and checking it. The fallback was not needed: turn 2 wrote and staged the lines.

## Turn 1, the review

Run from the clinic's root, detached with `nohup`:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p "/code-review high c54d011...e6653b5" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode default --permission-prompts none --output-format stream-json --verbose --allowedTools "Bash(git diff *)" "Bash(git log *)" "Bash(git show *)" "Bash(git status *)" "Bash(npm *)" "Bash(npx *)"
```

* The review ran in the foreground of the session, as in chapter 12, in about two and a half minutes. Its stream holds no tool call of the session itself: only the final response, a JSON block of nine findings, each with `file`, `line`, `summary` and `failure_scenario`. That block is `findings.md`, one block per finding. Its result was `success`.
* No call was denied. Nothing in the clinic changed.

## The decisions

The book's `/apply` session read each finding against the clinic's code and documents and gave the author its assessment: 1 to 7 stand, 8 and 9 do not. For 1 and 2, the whole state overwrites only an update queued in the same tick, which React's flush between discrete events makes unreachable from a click today, but the code breaks the rule docs/01 and the delivery state. 6 is the same fix as 1, and 7 the same fix as 3. 8 was recorded on purpose by the delivery, and 9 asks the Orchestrator level, which docs/04 keeps without a DOM, to test the hook. The author accepted the assessment whole, chose one line for each pair (1 and 6, 3 and 7), and approved the request of turn 2 as drafted. It is in `decisions.md`.

* Read: 9. Confirmed: 7. Rejected: 2 (8, 9). Already queued: 0 in the book's M4.1. In the clinic's milestone 1.1, findings 3 and 7 fall under its `[x] orchestrator-tests` line, which promised that no logic stays in a hook untested; their M4.1 line names it and what it left. Finding 5 falls under the clause of the clinic's 1.1 paragraph "the code repeated across features has one shared copy", but under no line: `route-errors` and `minutes-of` cover other copies.

Turn 2, the decisions and the lines, from the clinic's root:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p --resume <turn 1's session> "<the request of decisions.md, turn 2>" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose --add-dir ../focus-kit-book --allowedTools "Read" "Edit" "Bash(git -C ../focus-kit-book add docs/06-Queue.md)" "Bash(git -C ../focus-kit-book diff *)" "Bash(git -C ../focus-kit-book status *)"
```

* The session read the book's docs/06 and the clinic's, added five `[ ]` lines to M4.1 before `m4.1-review` (`clinic-booking-submit`, `clinic-hours-save`, `clinic-hours-report`, `clinic-update-type`, `clinic-event-shapes`, in the order they can be built, the docs/01 line last) and one clause to M4.1's paragraph, two edits, and staged the file. The diff is `queue.diff`, the book's docs/06 just before turn 2 and after it.
* One call denied: `cd ../focus-kit-book && git status --short && grep …` on docs/06, outside the allowlist. The session did not retry it by another route; it read the file with `Read`.
* `git -C ../focus-kit-book add docs/06-Queue.md` staged the whole file, so this delivery's `[>] m4-code-review` went with it. The session said so.
* It raised one point for later: M4.1's `ch15-submit-event` asks chapter 15 to say what `shown` holds, and `clinic-booking-submit` removes `shown`. It left that line alone, as the request said; whoever builds the two lines settles their order.
* The author kept the lines as written, so there is no turn 3. Nothing in the clinic changed.

## Notes of the host

Auto-memory was off on both turns. The clinic has no memory folder, before or after; the book's held the same files, with the same dates, before the run and after it: no note to delete.

## What diverged

* The page asks for one M4.1 line per confirmed finding. The author chose one line for each pair of findings that one change settles, 1 with 6 and 3 with 7: seven confirmed findings, five lines.
* Nothing else from §8 as written.

## Files

```
README.md     this file
turn-N.txt    every turn, in order: text blocks byte for byte, tool calls as [tool <name>] <relative path or command>, a denied call as [denied]
findings.md   the nine findings as the run reported them, one block each
decisions.md  each request sent, word for word
queue.diff    the book's docs/06 before and after the M4.1 lines
```

The turn files are derived from each turn's stream by a one-off script outside the repository. Absolute paths are removed, so paths are relative to the clinic's root and the book is `../focus-kit-book`. Session ids are left out.
