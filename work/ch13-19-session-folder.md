# ch13-19-session-folder

Draft: what the person asked outside /apply and the queue line cannot hold. Not a completed proposal; /propose defines it.

**Objective.** The reader who uses a worktree per delivery knows which folder to open the host in for each command, and why, and never opens it in the container.

**What was asked.** A person using the kit with worktrees asked whether the agent session runs in the container folder (`library/`) or in `main/`, especially when a delivery's /propose is done in its worktree and /apply must start in a fresh session.

**The answer to teach.**

* Never in the container. It is not a checkout: it holds `main/` and the hidden folder with the bare repository and the worktrees, but no AGENTS.md, no documents and no skills, so a session there has none of what the kit reads.
* /propose in `main/`: it creates or reuses the worktree `<hidden>/worktrees/<slug>/` on `<prefix>/<slug>` and writes the page and the marks there.
* /apply in a fresh session opened inside `<hidden>/worktrees/<slug>/`, e.g. `cd library/.focus-kit/worktrees/return-book` and then the host's command, then `/apply return-book`.
* Why: the complete page and the `[>]` mark live on the delivery's branch; `main/`'s queue shows the line as it was until the merge (chapter 19, "Worktrees in the kit"), so an /apply opened in `main/` reads the wrong queue and page. The index /apply stages into is the worktree's own, and the host treats the folder it opens in as the session's root.
* `git worktree list` from `main/` prints the folder to open.

**Already in the book.** Chapter 19 says `/apply <slug>` "runs in a fresh session opened in that folder" and "open one session per folder: one in `main/` for each `/propose`, one in each worktree for its `/apply`". Missing: the container as a wrong place, the concrete path, the reason, and chapter 13 saying where /apply's fresh session opens off trunk.

**Kit 2026.10.20.2.** The kit now teaches this: /propose ends giving the worktree's path for /apply, /apply opened outside the worktree stops before any edit and gives that path, and the container's manual lets a session in `main/` edit the worktrees (in Claude Code, `"permissions": {"additionalDirectories": ["../<hidden>/worktrees"]}` in `.claude/settings.json`, file access only, no second copy of the skills). The line is in M26, after `kit-2026-10-20-2`.

**Open for /propose.** Whether chapter 10 (quick guide) or chapter 8 (hosts) also needs a sentence.
