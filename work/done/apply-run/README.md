# apply run

`/apply skeleton` on the guided project, and the author's review of the staged change it left, that chapter 11 shows. The delivery that planned and recorded it is `../apply.md`.

* Date: 2026-09-28.
* Host: Claude Code, `claude --version` printed `2.1.284 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64; Node 26.10.0 and npm 11.19.1 on the machine.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Repository: `JCKodel/focus-kit-clinic` at `3f0b47c1868e69970eefadb4f4a34bdcbada67b2` on `main`, with the reviewed `work/skeleton.md` and docs/06 (`skeleton` at `[>]`) uncommitted, as chapter 10 left them.
* Session: one session of three turns: the run, then two review turns sent with `--continue`, each reporting the same session id.

## The commands

Run from the root of the clinic. The run, turn 1:

```
claude -p "/apply skeleton" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose --disallowedTools "Bash(npm run dev*)" --allowedTools "Bash(npm *)" "Bash(npx *)" "Bash(node *)" "Bash(mkdir *)" "Bash(cp *)" "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"
```

The review, turns 2 and 3: the same flags, with `-p --continue "<request>"` in place of `-p "/apply skeleton"`. Each request is in `review.md`, as sent.

* The allowlist is the one above, exactly, in the space-wildcard form `claude --help` shows in 2.1.284. `git commit`, `git push` and `git tag` are not on it, so a commit would have been denied as well as being against the kit's instruction.
* `--disallowedTools "Bash(npm run dev*)"` was added before the run, by the author's decision, beyond the delivery's list: `Bash(npm *)` permits `npm run dev`, and the clinic's page lists it in Done when, so the agent would have tried to start a server that a headless turn could hold. It tried once, and it was denied.
* `--setting-sources project` and `--strict-mcp-config` keep the author's own settings, plugins, hooks and MCP servers out of the run, as in chapters 5, 7, 8 and 10.
* `acceptEdits` also let through, with no approval, the shell commands that move or delete files inside the project: the agent's `mv` of the page and its `rm` of the temporary migration file. Read-only commands, such as `ls`, needed no approval either.
* Each turn exited with status 1 after its last event, as in the earlier runs, with a result of `success`.

### Denied calls

Five, all in turn 1:

1. A shell loop that printed docs/01 to 05, the ADRs, the README and `.gitignore` in one command; the agent read the files one by one instead.
2. `node --version; npm --version; ls -a work/done .github .claude; git -C . ls-files`; the agent ran the two version commands alone.
3. `DATABASE_PATH=/tmp/fkc-check/clinic.sqlite PORT=3200 node src/server/main.server.ts; echo "exit=$?"`, the variable prefix is not on the allowlist; the agent ran `npm run server` instead.
4. `npm run dev`, denied by `--disallowedTools`.
5. `git mv -f work/skeleton.md work/done/skeleton.md`; the agent used `mv`, the page being untracked.

## After the run

* The agent never ran `npm run dev`. After the run the author started it in the clinic, opened the page and `GET /api/health`, confirmed both answered, and kept it running through the review. The clinic's page leaves that Done when item unticked, with the reason in its What happened: the item is the person's.
* In turn 2 the agent saved two notes in Claude Code's auto-memory folder for the clinic, outside the repository; `--setting-sources project` does not turn auto-memory off. They would have shaped the book's later runs on the clinic and a reader's run would not have them, so the author had them deleted after turn 3. Their paths are replaced by `<host memory folder of the clinic>` in `turn-2.txt`.

## Files

```
turn-1.txt, turn-2.txt, turn-3.txt   the full output of each turn: the agent's text and its tool calls
verify.txt               the output of the run's last npm run verify, the green one
skeleton-390x844.png     the proof screenshot, copied from the clinic's work/done/
skeleton-done.md         work/done/skeleton.md as turn 1 left it, byte for byte
review.md                the author's two requests, as sent, and the agent's reply to each
review.diff              the staged files that the review changed, before and after it
git-status-staged.txt    git status --short of the clinic after the review, everything staged
commit-message.txt       the commit message turn 1 suggested; the review left it unchanged
duration.txt             each turn's result event: duration, number of turns, denied calls
```

The turn files are derived from the stream of each turn: the text blocks byte for byte, each tool call as `[tool <name>] <path or command>`. The content a `Write` or `Edit` call carried is in the clinic's commit. The results of the tool calls are not kept, except the last `npm run verify` in `verify.txt`; nor are the raw streams. Every absolute path, the clinic's folder on the author's machine, was removed, so paths are relative to the clinic's root; in `verify.txt` the folder Vitest prints became `.`.

`review.diff` compares the staged tree before turn 2 with the staged tree after turn 3, file by file, made with `diff -u`; only `docs/05-Process.md` and `work/done/skeleton.md` changed. Request 1 was sent from a file, through the shell, which dropped its final newline.

## What happened

* Turn 1 read the page, `AGENTS.md`, docs/01 to 05 and the ADRs; installed the dependencies and Chromium for Playwright; wrote the code, the config and the tests; ran `npm run verify`, green; checked a failing migration by hand with a temporary file; took the screenshot with a one-off line in a Playwright test; updated docs/01, 02, 04, 05 and 06; wrote What happened and moved the page to `work/done/`; ran verify, red on Biome's formatting where it had removed the screenshot line; fixed it and ran verify green; staged with `git add -A`; and ended with the commit message and the environments.
* The author's review found five things, listed in `review.md`, and sent them as one request. The agent fixed the page and docs/05, said it should have asked before adding `@hono/node-server`, and asked whether to keep it. The author answered "Keep it", and turn 3 recorded the approval on the page.
* The clinic was left with everything staged and nothing committed; the author committed it with the suggested message, tagged it `book-v1/apply` and pushed both.

## Repeating it

Check out `book-v1/brainstorm` on a branch of your own, follow chapter 10's exercises to a reviewed `work/skeleton.md`, and run `/apply skeleton` in a fresh session. Review the staged change with chapter 11's questions, ask for each correction in the same conversation, and commit it yourself. You will get the same kind of build, not the same bytes: the agent is not deterministic, and npm installs the versions current on your day.
