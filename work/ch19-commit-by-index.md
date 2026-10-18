# ch19-commit-by-index

**Objective.** After chapters 13 and 19 the reader can commit one delivery from the index while preserving another session's changes, and distinguish a shared diff hunk from a conflict.

**Behaviour.**
* Given two deliveries staged together, the reader postpones the commit until the index contains only the reviewed delivery; the agent reports and preserves pre-existing entries instead of removing them itself.
* Given two adjacent queue lines in one diff hunk, each session stages its own line; sharing that hunk is not a conflict. If both edited the same line, or one requires a file the other is changing, the session stops and reports it.
* Given a shared file with another delivery's unstaged line, the reader uses a plain `git commit` after checking the staged diff, never `git commit -- <paths>` as a way to select a delivery: the latter takes the named file's working-tree content.
* Given a staged summary that lists only expected filenames but a shared queue file, the reader inspects the actual staged diff; filenames alone do not establish ownership of its lines.

**Contract.** Files: `book/en/13-apply.md`, `book/pt/13-apply.md`, `book/en/19-worktrees.md`, `book/pt/19-worktrees.md`; commit instructions, shared-tree conflict wording and affected key points. Terms: index, stage, conflict and unit of work from docs/03; no new term or API. Source: focus-kit SETUP.md 2026.10.18.1, template docs/05 §§4 and 6, the source pinned in `work/kit-2026-10-18-1.md`; retain chapter 19's Git commit/add/apply documentation references where useful. docs/05 §6 alignment is owned exclusively by that migration, despite this queue line naming it. This delivery checks the resulting rule and changes only chapter prose.

**States.** Inapplicable: no new screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** No commits, index manipulation demonstration in this repository, new Git helper, or batch proposal staging change (`ch19-batch-staging` owns that). No private-case changes.

**Decisions.** The user authorized definition before prerequisites finish, using their contracts; `after kit-2026-10-18-1` still gates apply. Existing partial staging instructions are retained where correct; the proof is a manual reading of the scenarios, not a new test suite or a narrated run.

**Done when.**
* [ ] The migration is `[x]` and its owning rules match this Contract before apply starts.
* [ ] Both editions answer every Behaviour scenario; all relevant commit instructions require an index holding one delivery and all conflict statements use lines rather than hunks.
* [ ] Both chapters open with their value, retain evidenced team gains, contain no filler or useful omissions, and keep every number and artifact sourced; docs/03 terms agree.
* [ ] `make verify` is green after the final covered edit and `make book` builds both editions; the proof records both PDF paths for author review, with delivery review and archival per docs/05.
