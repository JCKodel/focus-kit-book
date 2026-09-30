# m4.1-code-review run

The code review of this book's milestone M4.1, for chapter 23: `/code-review high` reviews the clinic's code that M4.1 changed, the author decides each finding, and the confirmed ones become lines in the book's M4.2. It is the third occurrence of a milestone's code review, after chapter 12's (`../closing-a-milestone-run/`) and M4's (`../m4-code-review-run/`), and the first whose range ends at a commit with no chapter tag. The delivery that planned and recorded it is `../m4.1-code-review.md`.

* Host: Claude Code, `claude --version` printed `2.1.285 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Date: 2026-09-30.
* The book before the run: on `main` at `1f25343`, with this delivery's changes not yet committed: the `[>] m4.1-code-review` line of docs/06, `work/m4.1-code-review.md`, and steps 1 and 5 of docs/05 §8's code-review recipe, edited before turn 1. `make verify` green.
* The clinic before the run: on `main`, clean, at `6edc9ad`, equal to `origin/main`.

## The range and the target form

`a3e2470...6edc9ad`. `6edc9ad` ("Name every event shape in docs/01 (event-shapes)") is M4.1's last clinic run and has no chapter tag, so the range ends at that commit, by its short hash, as docs/05 §8 step 1 now says.

The commit left out is `a3e2470` ("Update focus-kit to bff8414"), the one right after `book-v1/four-pieces` (`e6653b5`), made by `kit-milestone-review`: 14 files, the kit's, `docs/05` and `docs/06`, none in `src/`. The range starts on it, so it is not reviewed: it is not the clinic's code.

The range holds five commits, one per M4.1 clinic line, in order: `8e4de46` `clinic-booking-submit`, `13dd9c0` `clinic-hours-save`, `9f625cb` `clinic-hours-report`, `181286f` `clinic-update-type`, `6edc9ad` `clinic-event-shapes`. 22 files, 1272 insertions, 144 deletions, 15 of the files in `src/` (`git diff --stat`). No commit of M4.1 lies past its end.

The target form is the ref range with three dots, as `../m4-code-review-run/README.md` quotes from Claude Code's documentation. `a3e2470` is an ancestor of `6edc9ad`, so the merge base is `a3e2470` and the diff is the five commits.

## The `--add-dir` check

Not checked again: `claude --version` printed the same `2.1.285` as the m4-code-review run, which checked it from Claude Code's documentation and whose turn 2 used it (`../m4-code-review-run/README.md`, "The `--add-dir` check"). This run's turn 2 used it too: the fallback was not needed.

## Turn 1, the review

Run from the clinic's root, detached with `nohup`:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p "/code-review high a3e2470...6edc9ad" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode default --permission-prompts none --output-format stream-json --verbose --allowedTools "Bash(git diff *)" "Bash(git log *)" "Bash(git show *)" "Bash(git status *)" "Bash(npm *)" "Bash(npx *)"
```

* The review took about two minutes. As in M4's run, its stream holds no tool call of the session itself: only the final response, one paragraph and a JSON block of seven findings, each with `file`, `line`, `summary` and `failure_scenario`. That block is `findings.md`, one block per finding. Its result was `success`.
* No call was denied. Nothing in the clinic changed.

## The decisions

The book's `/apply` session read each finding against the clinic's code at `6edc9ad`, the code at `e6653b5` and the clinic's docs/01, and gave the author its assessment: 1, 2 and 4 stand; 3, 5, 6 and 7 do not.

* 1 and 2 share a root: the weekly hours' time inputs and the booking's name and phone have no `disabled={busy}`, while the buttons beside them do, so what is typed during a call is shown and not sent. M4.1 touched both paths and its tests keep a name typed in flight on purpose. One change settles both.
* 4: `clinic-hours-report` added `"saving"` to `WeeklyHoursReport`, which `WeeklyHoursAnswer.report` also uses.
* 3 is real, but at `e6653b5` `hoursRefused` already ran `reloadGone` on the same path: code M4 added, which M4.1 did not change, so out of the page's scope.
* 5 is what docs/01's shape 4 describes, and no click reaches it. 6 would move the branch, not remove it, against the M4.1 line's "one tested professionals event". 7: docs/01 names `retryOf` under shape 5.

The author accepted the assessment whole, chose one line for 1 and 2, and approved the request of turn 2 as drafted. It is in `decisions.md`.

* Read: 7. Confirmed: 3 (1, 2, 4). Rejected: 4 (3, 5, 6, 7). Already queued: 0, in the book's M4.2 and in the clinic's milestone 1.1, whose open lines (`time-zone-names`, `slot-taken-retry`, `routes-table`, `route-errors`, `minutes-of`) cover none of them.

Turn 2, the decisions and the lines, from the clinic's root:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p --resume <turn 1's session> "<the request of decisions.md, turn 2>" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose --add-dir ../focus-kit-book --allowedTools "Read" "Edit" "Bash(git -C ../focus-kit-book add docs/06-Queue.md)" "Bash(git -C ../focus-kit-book diff *)" "Bash(git -C ../focus-kit-book status *)"
```

* The session read the book's docs/06 and the clinic's, looked at the view inputs and the report types, added two `[ ]` lines to M4.2 before `m4.2-review` (`clinic-busy-fields` for findings 1 and 2, `clinic-hours-answer` for finding 4) and one clause to M4.2's paragraph, two edits, and staged the file. The diff is `queue.diff`, the book's docs/06 just before turn 2 and after turn 3.
* One call denied: `cd ../focus-kit-book && git status --short && grep …` on docs/06, outside the allowlist, the same call M4's turn 2 tried. The session did not retry it by another route; it read the file with `Read`.
* One Bash call ran outside the allowlist without a denial: a `grep` on the clinic's `src/` for the view inputs and the report types (`turn-2.txt`, line 5). Claude Code let it through as a read-only command; it changed nothing.
* `git -C ../focus-kit-book add docs/06-Queue.md` staged the whole file, so this delivery's `[>] m4.1-code-review` went with it. The session said so.
* The `/apply` session found that `clinic-hours-answer` said "load and save answer only "saved", "failed" or a refusal", while `load` answers only a refusal or nothing. The author asked for a correction.

Turn 3, the correction, from the clinic's root, flags as turn 2, with the request of `decisions.md`, turn 3:

* The session edited that line once, staged the file again and checked it. No call was denied. The author kept both lines as they now stand. Nothing in the clinic changed.
* Turn 3 ran in the foreground, without `nohup`, so the terminal's reset sequence landed at the end of its stream and `claude` exited 1 on `stty`; the stream's result is `success`, and `turn-3.txt` is derived from its JSON lines only.

## Notes of the host

Auto-memory was off on every turn. The clinic's memory folder was empty before the run and after it; the book's held the same files, with the same dates: no note to delete.

## What diverged

* §8 as written, which this delivery had edited before turn 1 (step 1 for the untagged end and the kit commit left out, step 5 for findings that share one line, here 1 with 2), was followed; a correction turn is what step 5 allows.
* Turn 3 was not detached with `nohup`, unlike turns 1 and 2; see above.

## Files

```
README.md     this file
turn-N.txt    every turn, in order: text blocks byte for byte, tool calls as [tool <name>] <relative path or command>, a denied call as [denied]
findings.md   the seven findings as the run reported them, one block each
decisions.md  each request sent, word for word
queue.diff    the book's docs/06 before and after the M4.2 lines
```

The turn files are derived from each turn's stream by a one-off script outside the repository. Absolute paths are removed, so paths are relative to the clinic's root and the book is `../focus-kit-book`. Session ids are left out.
