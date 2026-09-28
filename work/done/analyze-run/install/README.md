# analyze run: the install

The install of focus-kit on the brownfield project, before chapter 8's `/analyze` run, done the way chapter 5 did it on the guided project.

* Date: 2026-09-28.
* Host: Claude Code, `claude --version` printed `2.1.283 (Claude Code)`.
* Repository: `JCKodel/clahub`, branch `book` created from `book-v1` (`9d1e666e1d30f271aea9640393229a7cbfbd1b62`), a clean tree.
* Kit: `JCKodel/focus-kit` `main` at `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b`, the commit chapter 5 installed in the guided project, whose `SETUP.md` the sentence fetched.

## The command

Run from the root of the fork, the same as chapter 5's third attempt:

```
claude -p "Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md and do what it says." --permission-mode bypassPermissions --setting-sources project --strict-mcp-config --no-session-persistence
```

Chapter 5's two attempts in `acceptEdits` showed that the install cannot finish in it, so this run went straight to the mode that worked. It exited with status 1 after printing its report, as chapter 5's attempts did.

## Files

```
output.txt               the agent's report, whole
git-status.txt           git status --short right after the run, as it prints (untracked folders collapse)
git-status-staged.txt    git status --short after git add -A: the 36 files, one per line
```

The report is kept byte for byte, but for the terminal control sequences and the line `stty: stdin isn't a terminal` that Claude Code printed after the text when it exited, which are removed. It holds no absolute path.

## The check

Every written file was compared with its block in section 3 of `SETUP.md` at the SHA above: the lines between the block's four-backtick fences plus a final newline, with `<name>` filled for 3.6 to 3.9, each file of 3.1 to 3.5 in `.claude/skills/`, `.agents/skills/` and `.windsurf/skills/`. All 36 matched, none missing, none extra. No file of the project was changed: the repository had no `.claude/`, `.agents/`, `.cursor/`, `.gemini/`, `.windsurf/`, `.github/prompts/` or `GEMINI.md` before.

The author committed it on `book` with `git commit -m "Install focus-kit"`, so `/analyze` ran on a clean tree.
