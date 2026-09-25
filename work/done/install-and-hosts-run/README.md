# install-and-hosts run

The install of focus-kit on the guided project that chapter 5 shows.

* Date: 2026-09-25.
* Host: Claude Code, `claude --version` printed `2.1.282 (Claude Code)`.
* Repository: `JCKodel/focus-kit-clinic` at `book-v1/start` (`31d950312581a9ebfd933deb13125ca6e192a920`): `README.md`, `LICENSE`, `LICENSE-TEXT`.
* Kit: `JCKodel/focus-kit` `main` at `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b`, whose `SETUP.md` the sentence fetched.

## The command

Run from the root of the clinic:

```
claude -p "Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md and do what it says." --permission-mode bypassPermissions --setting-sources project --strict-mcp-config --no-session-persistence
```

* `--setting-sources project` and `--strict-mcp-config` keep the author's own settings, plugins, hooks and MCP servers out of the session, so it sees what a reader's fresh install sees. A probe before the run confirmed it loaded no instruction file, no hook context and no MCP server.
* `--no-session-persistence` keeps the run out of the author's session history.
* `--permission-mode bypassPermissions` was the third attempt; the two before it stopped for lack of permission and are kept here (below).

## Attempts

1. `--permission-mode acceptEdits --allowedTools WebFetch`: the fetch tool returned a summary of `SETUP.md`, not its text, and the agent refused to write files it could not copy byte for byte; its request to download the file with `curl` was denied. Output: `attempt-1-output.txt`.
2. `--permission-mode acceptEdits --allowedTools WebFetch "Bash(curl:*)"`: the download worked, but Claude Code refuses writes into `.claude/` in accept-edits mode, and the agent's extraction script needed an approval it could not get. Output: `attempt-2-output.txt`.
3. `--permission-mode bypassPermissions`: the run. Output: `output.txt`.

Each attempt exited with status 1 after printing its report, a status the three share whatever the outcome. No attempt wrote, staged or committed a file other than the third's 36.

## Files

```
output.txt               the agent's report, whole
git-status.txt           git status --short right after the run, as it prints (untracked folders collapse)
git-status-staged.txt    git status --short after git add -A: the 36 files, one per line
attempt-1-output.txt     the first attempt's report
attempt-2-output.txt     the second attempt's report
```

The reports are kept byte for byte, but for the terminal control sequences Claude Code printed after the text when it exited, which are removed. They hold no absolute path.

## The check

Every written file was compared with its block in section 3 of `SETUP.md` at the SHA above: the lines between the block's four-backtick fences plus a final newline, with `<name>` filled for 3.6 to 3.9, each file of 3.1 to 3.5 in `.claude/skills/`, `.agents/skills/` and `.windsurf/skills/`. All 36 matched, none missing, none extra, which is the count of `SETUP.md` §4.
