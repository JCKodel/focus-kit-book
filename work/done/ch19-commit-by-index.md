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
* [x] The migration is `[x]` and its owning rules match this Contract before apply starts.
* [x] Both editions answer every Behaviour scenario; all relevant commit instructions require an index holding one delivery and all conflict statements use lines rather than hunks.
* [x] Both chapters open with their value, retain evidenced team gains, contain no filler or useful omissions, and keep every number and artifact sourced; docs/03 terms agree.
* [x] `make verify` is green after the final covered edit and `make book` builds both editions; the proof records both PDF paths for author review, with delivery review and archival per docs/05.

**Build.** Chapter 19, both editions: hunks are defined as what `git add -p` offers, two neighbouring lines being one, and each session marks and stages its own line of docs/06, near or far; the staged check says `--stat` names files and not whose lines a shared file holds, so the queue's staged diff decides; with another delivery staged, the commit waits until the index holds only the reviewed one, the agent having reported and left those entries; the person may sort the index, `git restore --staged <its paths>` and, for neighbouring queue lines, the whole of docs/06 unstaged and this delivery's line staged again by its session, since `git restore --staged -p` splits with `s` only as `git add -p` does (new `git-restore` footnote); the path trap now says a plain commit leaves the other's unstaged line out and a commit with paths is never a way to choose a delivery, dropping the concession that it was safe for files one delivery alone changed; the not-a-conflict list adds two neighbouring queue lines in one hunk, a conflict is the same line edited by both; the batch's commit request, the queue check and the key points use lines and the shared-file diff. git's merge-conflict definition for two branches stays as is. Chapter 13, both editions: the review reads this line's change of docs/06, `/apply` stages that line, and the commit paragraph adds never naming paths on `git commit` and not committing while the staged diff holds another delivery's entries.

**Gate.** `kit-2026-10-18-1` is `[x]` in docs/06; docs/05 §4 (a conflict is a line edited by both; neighbouring lines in one hunk conflict in nothing) and §6 (commit from an index holding only the delivery, never by naming paths; report and do not unstage others' entries) already say what the Contract asks. No shared file changes.

**Proof.** Manual reading of the four scenarios against the final text of both editions: scenario 1, chapter 19 "Then do not commit yet" paragraph and chapter 13's commit paragraph; scenario 2, chapter 19's opening of the one-folder section, the not-a-conflict list and conflict list, and the batch section; scenario 3, chapter 19's path trap; scenario 4, chapter 19's staged check and key point. `make verify` green after the last chapter edit. `make book` and the PDF paths are the batch driver's, run once at the end: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Review.** One read-only Opus agent over the four chapter files and this page found nothing serious. Applied: Portuguese "dividir um hunk" became "compartilhar um hunk", since the chapter uses "dividir" for splitting; the queue "cannot be split with `s`", since a person could still edit the hunk; the bullet's `git add -p` note dropped, since it does not stage a neighbouring line alone; "Git stages a file in hunks" became what `git add -p` offers; "it never is" became "never a way to choose one". Declined: chapter 13's "paths and hunks" in the Green-is-not-done list stays, since it is docs/05 §6's and the kit's rule for mixed files. `make verify` green again after the fixes.

**Decisions taken alone.** The person, not a session, unstages the other's entries when both are staged, as docs/05 §6 forbids it only to the agent; the earlier `git restore --staged -p` recovery for the queue was replaced, since it cannot split neighbouring lines either; the in-folder rule says "line" while the merge section keeps git's "same lines, or lines next to each other".

```commit
docs(ch19-commit-by-index): commit from an index of one delivery

- Wait while another delivery is staged; the agent reports, never unstages
- Never choose a delivery by naming paths on git commit
- Neighbouring queue lines share a hunk, not a conflict; a conflict is a line
- A --stat listing names files; the shared file's staged diff shows lines
- Chapter 13 points the commit paragraph to these rules

work/done/ch19-commit-by-index.md
```
