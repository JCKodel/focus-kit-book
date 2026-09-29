# m4-review run

The review of this book's milestone M4, for chapter 23: a fresh session reads the Prologue to chapter 16 in both editions against the product questions of docs/00 and M4's paragraph, the author decides each finding, and the confirmed ones become the milestone M4.1 in docs/06. It is the first run of the recipe in docs/05 §8, written by this delivery; the delivery that planned and recorded it is `../m4-review.md`.

* Host: Claude Code, `claude --version` printed `2.1.284 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Date: 2026-09-29.
* The book before the run: on `main` at `077f74a`, with this delivery's changes not yet committed: the `[>] m4-review` and `[ ] m4-code-review` lines of docs/06, `work/m4-review.md`, and the recipe added to docs/05 §8 before turn 1. None of them is among what the review reads. `make verify` green.

## Turn 1, the review

Run from the root of this repository, detached with `nohup`:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p "<the request of decisions.md, turn 1>" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode default --permission-prompts none --output-format stream-json --verbose --allowedTools "Read" "Glob" "Grep"
```

* The session read docs/00, docs/04 and the chapters `00-` to `16-` in order, English then Portuguese, each file once: 38 calls, 36 `Read`, one `Grep` in `book/pt` for the Portuguese words of two findings, and one `Bash` that listed the chapters and counted their lines (`ls` and `wc`), which the host allowed as a read-only command though the list did not name it. No call was denied and nothing changed.
* It reported 15 findings and the paragraph check. They are `findings.md`, byte for byte.

## The paragraph check

M4's paragraph: "When this milestone closes, a reader can organize code by feature with exceptions as values, and knows when the four pieces pay their way and when they do not." As the review reported it, one line per clause:

* a reader can organize code by feature: chapter 14 §Vertical slices · `book-v1/closing-a-milestone`
* with exceptions as values: chapter 14 §Exceptions as values in the clinic · `book-v1/closing-a-milestone`
* and knows when the four pieces pay their way: chapter 15 §When the pieces pay their way · `book-v1/four-pieces`
* and when they do not: chapter 15 §When the pieces pay their way · `book-v1/four-pieces`

No clause is a finding of its own, though three findings weaken what the lines point to: F3 (what makes one feature), F7 (the tag of chapter 15 holds a delivery the reader never built) and F12 (no case of a piece that does not pay).

## The decisions

The book's `/apply` session read each finding against the text and gave the author its assessment: all 15 stand, three narrowed. F4: chapter 14 does say an exception can become a refusal, but its definition and key point still contradict `SlotTaken`. F12: the section does name a cost (ADR-0002, the brownfield project), but no piece that has a job and still does not pay. F15: the text explains the 33 of 77; the key point's 20 of 95 has no baseline. The author accepted the assessment whole, and the request of turn 2 as drafted. It is in `decisions.md`.

* Read: 15. Confirmed: 15. Rejected: 0. Already queued: 0.

Turn 2, the decisions and the lines:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p --resume <the review's session> "<the request of decisions.md, turn 2>" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose --allowedTools "Read" "Edit" "Bash(git add docs/06-Queue.md)" "Bash(git diff *)" "Bash(git status *)"
```

* The session read docs/06, added `## M4.1. What the review of M4 found` between M4 and M5 with its paragraph and 15 `[ ]` lines, one edit, and staged the file. The diff is `queue.diff`, docs/06 just before turn 2 and after it.
* `git add docs/06-Queue.md` staged the whole file, so the M4 lines already uncommitted went with it: this delivery's `m4-review` and `m4-code-review`, and `kit-milestone-review`, a line the author added in another session while turn 1 ran. The session said so.
* No call was denied. No correction was needed, so there is no turn 3.

## Notes of the host

Auto-memory was off on both turns. The host's memory folder for this repository held the same files, with the same dates, before the run and after it: no note to delete.

## What diverged

* Nothing from §8 as written. The one call outside the allowlist of turn 1, the `ls` and `wc`, was allowed by the host as read-only, as `grep` was in m3-review.

## Files

```
README.md     this file
turn-N.txt    every turn, in order: text blocks byte for byte, tool calls as [tool <name>] <relative path or command>, a denied call as [denied]
findings.md   the 15 findings and the paragraph check, as the run reported them
decisions.md  each request sent, word for word
queue.diff    docs/06 before and after the M4.1 lines
```

The turn files are derived from each turn's stream by a one-off script outside the repository. Absolute paths are removed, so paths are relative to this repository's root. Session ids are left out.
