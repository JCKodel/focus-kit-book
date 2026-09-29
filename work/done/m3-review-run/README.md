# m3-review run

The review of this book's milestone M3, for chapter 23: a fresh session reads the Prologue to chapter 13 in both editions against the product questions of docs/00 and M3's paragraph, the author decides each finding, and the confirmed ones become the milestone M3.1 in docs/06. The delivery that planned and recorded it is `../m3-review.md`.

* Host: Claude Code, `claude --version` printed `2.1.284 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Date: 2026-09-29.
* The book before the run: on `main` at `88492f0`, with two changes of this delivery's `/propose` not yet committed, the `[>]` line of `m3-review` in docs/06 and `work/m3-review.md`; neither is among what the review reads. `make verify` green, once the author had committed and pushed the guided project's `closing-a-milestone` commit and tag, whose link had answered 404.

## Turn 1, the review

Run from the root of this repository, detached with `nohup`:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p "<the request of decisions.md, turn 1>" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode default --permission-prompts none --output-format stream-json --verbose --allowedTools "Read" "Glob" "Grep"
```

* `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` is not in the page: the author approved it before the run, so that the session does not load the host's notes about this project, which a reader of the book does not have, and writes none.
* The page names "docs/04 §Voice"; docs/04 has no such section, Voice is a bullet of "Writing the book", so the request names that section.
* The session read docs/00, the two sections of docs/04, and the chapters `00-` to `13-` in order, English then Portuguese, and nothing else: 32 calls, `Read`, one `Grep` for docs/04's headings and one `Glob` for the chapter files. No call was denied and nothing changed.
* It reported 19 findings and the paragraph check. They are `findings.md`, byte for byte.

## The paragraph check

M3's paragraph: "When this milestone closes, a reader can install the kit, document a new or an existing project, and deliver a milestone with `/propose` and `/apply`, following the guided project." As the review reported it, one line per clause:

* a reader can install the kit: chapter 5 §Install · `book-v1/install-and-hosts`
* document a new project: chapter 7 §The run on the clinic · `book-v1/brainstorm`
* document an existing project: chapter 8 §The run on CLAHub · `book-v1-analyze` (the brownfield project)
* with `/propose`: chapter 10 §The run on the clinic · no tag
* and `/apply`: chapter 11 §The run on the clinic · `book-v1/apply`
* deliver a milestone, following the guided project: finding F17, nothing tells the reader to build the rest of milestone 1 between chapters 11 and 12

## The decisions

The book's `/apply` session read each finding against the text and gave the author its assessment: all 19 stand, F14 narrowed (the chapters do name the second agent; what they miss is that the runs are headless, what `--continue` does, and what the reader does in an interactive session). The author accepted the assessment whole and approved the request word for word before it was sent. It is in `decisions.md`.

* Read: 19. Confirmed: 19. Rejected: 0.
* Already queued: none. The closest, F16 against `git-essentials` (chapter 17), stays a line of its own: chapter 11 promises the reader will commit and must show the command itself.

Turn 2, the decisions and the lines:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p --resume <the review's session> "<the request of decisions.md, turn 2>" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose --allowedTools "Read" "Edit" "Bash(git add docs/06-Queue.md)" "Bash(git diff *)" "Bash(git status *)"
```

* The first send used `--continue`, as the page says. `--continue` takes the most recent conversation of the directory, and that was the book's own `/apply` session, running in the same repository, not the review. The process was stopped within seconds, before any call or any text; docs/06 was unchanged. The same request was sent again with `--resume` and the review's session, with the author's approval.
* The session read docs/06, added `## M3.1. What the review of M3 found` between M3 and M4 with its paragraph and 19 `[ ]` lines, one edit, and staged the file. The diff is `queue.diff`, docs/06 before and after the lines only: the `[>]` line of `m3-review`, staged with it, is this delivery's own change.
* It also ran `grep` for em dashes in docs/06 in the same command as `git add`; the host allowed it, as a read-only command, though the list did not name it. No call was denied.
* It suggested a commit message for the queue alone; it is not used, since the lines are committed with this delivery.
* No correction was needed, so there is no turn 3.

## Notes of the host

Auto-memory was off on both turns. The host's memory folder for this repository held the same files, with the same dates, before the run and after every turn: no note to delete.

## What diverged

* The auto-memory flag and the docs/04 section name, as above.
* The two uncommitted changes of `/propose` against "clean `main`": the author chose to run with them.
* The first send of turn 2 reached the wrong session through `--continue` and was stopped; `--resume` sent it to the review.

## Files

```
README.md     this file
turn-N.txt    every turn, in order: text blocks byte for byte, tool calls as [tool <name>] <relative path or command>, a denied call as [denied]
findings.md   the 19 findings and the paragraph check, as the run reported them
decisions.md  each request sent, word for word
queue.diff    docs/06 before and after the M3.1 lines
```

The turn files are derived from each turn's stream by a one-off script outside the repository. Absolute paths are removed, so paths are relative to this repository's root. Session ids are left out. The stopped send of turn 2 wrote no text and made no call, so it has no turn file.
