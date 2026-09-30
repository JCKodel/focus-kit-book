# The M4.1 review, recorded

The review of milestone M4.1, run on 2026-09-30 as docs/05 §8, "The recipe of a milestone review", says: the third review of a milestone of chapters, after m3-review and m4-review, and the first to follow the recipe from a page that only names it.

* Host: Claude Code 2.1.285 (`claude --version`).
* Model: `claude-opus-5-5`, on both turns.
* The book's commit: `001daa9`, with only this delivery's `/propose` changes uncommitted (`work/m4.1-review.md`, and docs/06 marking `m4.1-review` and adding `m4.1-code-review`); `make verify` green before turn 1.
* Chapters: `00-` to `16-`, in both editions.

## Turn 1, the review

Run from the root of this repository, detached with `nohup`:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p "<the request of decisions.md, turn 1>" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode default --permission-prompts none --output-format stream-json --verbose --allowedTools "Read" "Glob" "Grep"
```

* The session read docs/00, docs/04 and the chapters `00-` to `16-` in order, English then Portuguese, each file once: 37 calls, 36 `Read` and one `Bash` that listed the chapters and counted their lines (`ls` and `wc`), which the host allowed as a read-only command though the list did not name it, as in m4-review. It read nothing from `work/` or `scripts/`. No call was denied and nothing changed.
* The findings, as reported, are `findings.md`; the turn is `turn-1.txt`.

## The paragraph check

M4.1's paragraph was quoted whole. Its clause on the clinic's client orchestrators ("the clinic's client orchestrators publish every in-flight state as an update of the current state, send the weekly hours editor's reports through one tested event, declare each repeated type once, and take only the event shapes its docs/01 describes") is the guided project's code, which no chapter teaches, so the request routed it to `m4.1-code-review` and asked for no finding on it. This is the first milestone paragraph that holds a clause about the guided project's code; §8 changes only on the second.

As the review reported it, one line per clause:

* every confirmed finding of the M4 review is settled: FINDING F1, F3, F5, F6, F7, F9, F11, F13
* chapter 3's key points say what its run showed: FINDING F3
* Part III says what makes one feature: FINDING F6
* and whether a slice may use another slice's code: ch14 §Vertical slices · book-v1/closing-a-milestone
* its definitions of a refusal fit the clinic's code it shows: ch14 §Exception, refusal, error · book-v1/closing-a-milestone
* its definition of an error fits the clinic's code it shows: FINDING F7
* its definition of a unit test fits the clinic's code it shows: FINDING F13
* its definition of injection fits the clinic's code it shows: ch15 §What the clinic injects · book-v1/four-pieces
* chapter 14 tells an error from an exception in any language: ch14 §Exception, refusal, error · book-v1/closing-a-milestone
* says why a throw must not steer the flow: ch14 §Why not throw · book-v1/closing-a-milestone
* and keeps a library's exceptions out of the domain: ch14 §The boundary · book-v1/closing-a-milestone
* it shows a piece that has a job and still costs more than it gives: ch15 §When the pieces pay their way · book-v1/four-pieces
* every excerpt can be followed from its text: FINDING F4, F11
* a reader following the guided project is told to build the code that chapter 15's tag holds: FINDING F9
* the clinic's client orchestrators …: m4.1-code-review
* and the Portuguese edition means what the English means: FINDING F1, F5

The first line takes the paragraph's opening clause as a clause of its own and answers it with the findings on subjects M4 raised. F2 and F14, both rejected, point at no clause.

## The decisions

The book's `/apply` session read each finding against the text and gave the author its assessment: twelve hold, six of them narrowed, and two are weak. F7: the chapter says how `query` swallows a bug, but not what the reader does about it. F8: the repository is the I/O piece, so SQLite's text there fits; only the routes carrying `DatabaseSync`'s type do not square. F10: `request` and `remembered.ts` are client repositories; `openDatabase` and `migrate` sit in no piece. F11: only `tooLateToCancel`. F12: the section names the shape as what the clinic pays for, the key point does not. F13: the next sentence already names fake repositories. F2 and F14 were assessed as weak: F2's paragraph credits the file with surviving a fresh session, not with its position; F14's text says "where", not "how much", and `ch16-reading-count` settled its count. The author accepted the assessment whole, and the request of turn 2 as drafted. It is in `decisions.md`.

* Read: 14. Confirmed: 12. Rejected: 2 (F2, F14). Already queued: 0.

## Turn 2, the decisions and the lines

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p --resume <the review's session> "<the request of decisions.md, turn 2>" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose --allowedTools "Read" "Edit" "Bash(git add docs/06-Queue.md)" "Bash(git diff *)" "Bash(git status *)"
```

* The session read docs/06, added `## M4.2. What the review of M4.1 found` between M4.1 and M5 with its paragraph, 12 `[ ]` lines and `m4.2-review` last, one edit, and staged the file. The diff is `queue.diff`, docs/06 just before turn 2 and after it.
* It judged that no existing line covered a finding: F6, F7, F10, F12 and F13 return to subjects of M4.1 lines already `[x]` (`ch14-feature-boundary`, `ch14-catch-all`, `ch15-route-io`, `ch15-piece-cost`, `ch16-unit-test`), and each new line says what is still wrong after that delivery.
* Two calls were `Bash` chains outside the allowlist's exact forms (`git diff` with `git diff --cached --stat`; `grep -c` for em dashes with `git add` and `git diff --cached`), which the host allowed as read-only or allowlisted commands. No call was denied.
* The turn is `turn-2.txt`. No correction was needed, so there is no turn 3.

## Notes of the host

Auto-memory was off on both turns. The host's memory folder for this repository held the same files, with the same dates, before the run and after it: no note to delete.

## What diverged

* The book's `/apply` ran in the same session as its `/propose`, not a fresh one; the review's turns were fresh headless sessions as §8 says, so the reader knew nothing of either.
* Turn 2 staged the whole of docs/06, so the `/propose` changes (`m4.1-review` `[>]` and the `m4.1-code-review` line) are staged with the lines, as this delivery's own.
* Nothing else from §8 as written.

## Files

```
README.md     this file
turn-1.txt    the review's turn, text byte for byte, calls one line each
turn-2.txt    the decisions' turn, the same way
findings.md   the findings and the paragraph check, as reported
decisions.md  each request sent, word for word
queue.diff    docs/06 before and after the M4.2 lines
```
