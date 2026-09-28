# brainstorm run

`/brainstorm` on the guided project, answered from `brief.md`, that chapter 7 shows. The delivery that planned and recorded it is `../brainstorm.md`.

* Date: 2026-09-28.
* Host: Claude Code, `claude --version` printed `2.1.283 (Claude Code)`; headless (`claude -p`), macOS 26 (Darwin 25.6.0), arm64.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Repository: `JCKodel/focus-kit-clinic` at `book-v1/install-and-hosts` (`a5ac6fd39f19dcfa9161f59cd68cbd979d134e52`), with the kit of `JCKodel/focus-kit` at `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b`.
* Session: one; every turn after the first reported the same session id as the first.

## The commands

Run from the root of the clinic. The first turn:

```
claude -p "/brainstorm" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose
```

Each answer, turns 2 to 6, with `<answer>` the text of the round's answer in `questions.md`:

```
claude -p --continue "<answer>" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose
```

* `--setting-sources project` and `--strict-mcp-config` keep the author's own settings, plugins, hooks and MCP servers out, as in chapter 5's run.
* There is no `--no-session-persistence`: `--continue` resumes the saved session.
* `--permission-mode acceptEdits` was enough, the least mode the command needs, since it only reads and writes files. It denied two shell commands of turn 5, the agent's own check for em dashes and its `git status`; the agent wrote `CLAUDE.md` and `work/done/.gitkeep` with its file tool instead and said the check had not run. A read-only listing in turn 1 ran without approval.
* `--output-format stream-json --verbose` records every tool call, so a question asked through a question form would not be lost. The agent used none: headless mode lists no question tool, and it asked in text.

## Files

```
brief.md                 the brief, given word for word
questions.md             each round of questions and the answer given, in order
turn-1.txt ... turn-6.txt  the full output of each turn: the agent's text, its tool calls, and the tool errors it received
turn-6.diff              the one change of turn 6, to docs/06-Queue.md
git-status.txt           git status --short after turn 5, as it prints (untracked folders collapse)
git-status-staged.txt    git status --short after turn 6 and git add -A: the 15 files, one per line
```

The turn files are derived from the stream: the text blocks byte for byte, each tool call as `[tool <name>] <path or command>`, and each tool error whole. The content a `Write` call carried is the file in the clinic; the files are unchanged since, except `docs/06-Queue.md`, which `turn-6.diff` changes. The results of successful tool calls (the files the agent read) are not kept. The raw streams stayed outside the repository.

Every absolute path, the clinic's folder on the author's machine, was removed from the tool calls, so paths are relative to the clinic's root. The host's denial message in `turn-5.txt` holds an em dash, which is why the em dash check skips `work/done/*-run/`.

## What happened

* Turns 1 to 4 were four rounds of questions: the product, then its gaps with the vocabulary, then how it is built with FOCUS and git, then the conventions and the process slots. Each was answered by the rule of `brief.md`.
* Turn 5 wrote docs/00 to 06, five ADRs, `AGENTS.md`, `CLAUDE.md` and `work/done/.gitkeep`, and showed the queue. It never asked about the first milestone, so the brief's section First milestone was not given, and milestone 1 held the owner's view of the day, which the brief puts in the second.
* The author reviewed the documents and chose the fix: turn 6 gave that section word for word, in the same session. The agent rewrote milestone 1's paragraph with the brief's sentence and added milestone 2 with `absences`, `owner-schedule` and `deploy`; `deploy` moved there on its own reasoning, which the author accepted.
* No generated document holds an em dash: a search of `docs/`, `AGENTS.md` and `CLAUDE.md` after turn 6 finds none.
* Nothing was committed by the agent; the author commits and tags `book-v1/brainstorm`.

## Repeating it

Check out `book-v1/install-and-hosts`, run the first command, and answer each round by the rule at the end of `brief.md` with `--continue`. You will get the same kind of documents, not the same bytes: the agent is not deterministic, so its questions, defaults and file names will move.
