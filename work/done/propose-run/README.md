# propose run

`/propose skeleton` on the guided project, answered from `brief.md`, and the author's review of the page it wrote, that chapter 10 shows. The delivery that planned and recorded it is `../propose.md`.

* Date: 2026-09-28.
* Host: Claude Code, `claude --version` printed `2.1.283 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64. The run headless (`claude -p`); the review interactive, in a fresh session.
* Model: `claude-opus-5-5`, given with `--model` on every headless turn; the review session reported the same model.
* Repository: `JCKodel/focus-kit-clinic` at `3f0b47c1868e69970eefadb4f4a34bdcbada67b2` on `main`, "Update focus-kit to e7607c5": `book-v1/brainstorm` plus the kit updated to focus-kit `e7607c58ad38e70e3496518a58d4237612e21ebc` in a commit of its own, on a clean tree.
* Sessions: the run is one session of two turns, the second reporting the same session id as the first; the review is a second session.

## The commands

Run from the root of the clinic. The first turn:

```
claude -p "/propose skeleton" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose
```

The answer, turn 2, the brief's rule word for word:

```
claude -p --continue "Your call. Say what you chose and why." --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose
```

The review, turn 3: the author ran `claude` in the clinic, in `acceptEdits`, and typed `/propose skeleton`, a blank line, and the request of `review.md`.

* `--setting-sources project` and `--strict-mcp-config` keep the author's own settings, plugins, hooks and MCP servers out of the run, as in chapters 5, 7 and 8. The review session was opened with no flags.
* `--permission-mode acceptEdits` was enough for the run to finish: it reads and writes files, and the read-only shell commands it ran (listings, `cat`, `grep`, `node --version`, `git log`, `git status`) needed no approval. No call was denied in any turn.
* Each headless turn exited with status 1 after its last event, as in chapters 5, 7 and 8, with a result of `success`.
* The plan was to send the review to the same headless session with `--continue`. It ran as a fresh interactive session of `/propose skeleton` instead, which reads the page already in `work/` and works on it; `review.md` says how it went.

## Files

```
brief.md                 the brief, given word for word
usage.txt                the author's /usage output of 2026-09-28, terminal escapes removed, the source of the cost shares of chapter 10
questions.md             the round of questions, the answer given, and the agent's reply that ends with the page to read
turn-1.txt, turn-2.txt   the full output of each headless turn: the agent's text and its tool calls
skeleton-first.md        work/skeleton.md as turn 2 wrote it, byte for byte
review.md                the author's request, the agent's two questions and the author's answers, and its reply
turn-3.txt               the full output of the review: the agent's text, its tool calls, the question form and its answers
skeleton.diff            skeleton-first.md against the clinic's work/skeleton.md after the review
queue.diff               git diff of the clinic's docs/06-Queue.md after the review: the mark of turn 2 and the line of turn 3
git-status.txt           git status --short of the clinic after the review
```

The turn files are derived from the stream of the headless turns and from the session file of the review: the text blocks byte for byte, each tool call as `[tool <name>] <path or command>`, the question form as its input in JSON, and its answers as the host returned them. The content a `Write` or `Edit` call carried is in the clinic's working tree, which the two diffs show. The results of other tool calls (the files the agent read) are not kept, nor are the raw streams and the session file. Every absolute path, the clinic's folder on the author's machine, was removed, so paths are relative to the clinic's root.

## What happened

* Turn 1 read docs/00 to 06, the ADRs, the README and `work/`, and asked four questions, each with its recommendation first, then listed the choices it would make on its own and a gap it noticed outside the delivery (`absences` in the queue and not in docs/00).
* Turn 2 got the brief's rule, kept every recommendation, wrote `work/skeleton.md`, marked `skeleton` `[>]` in docs/06, said what it chose and why, and ended by asking the person to read and question the page before `/apply`, the kit's ending since focus-kit `e7607c5`. Its `grep` for em dashes found none.
* The review sent four holes. The agent asked the author about the manifest and the screenshot and took the recommended option in each; it removed the import check, took the manifest out and added the queue line `install` for it, replaced the screenshot baseline with a proof file, and wrote the migration runner's signature and error into the Contract. On its own it moved `Result` to `src/lib/result.ts` in this delivery, as its second use, and said so.
* The clinic was left with `work/skeleton.md` and docs/06 changed, unstaged and uncommitted, and no tag: chapter 11 builds the page and commits both.

## Repeating it

Check out `book-v1/brainstorm` on a branch of your own, update the kit as chapter 5 shows, commit it, run the first command, and answer with the brief's rule with `--continue`. Then read the page and ask for each correction in the same conversation. You will get the same kind of page, not the same bytes: the agent is not deterministic, so its questions, choices and wording will move.
