# ch21-one-tree

**Objective.** After chapter 21 a reader can run two agents at once in one folder on trunk, on free lines whose files do not meet, tell what is and is not a conflict there, commit each delivery alone, and say when a worktree per delivery still pays; chapters 20 and 10 choose git the same way.

**Behaviour.**

* A reader with two free lines, `return-book` (touches `src/loans/`) and `overdue-list` (touches `src/reports/`), both marking docs/06, says from chapter 21 that they can run in one folder at once, and why: their files do not meet, and their queue marks are different lines of one file.
* A reader whose second session sees `[~]` become `[*]` on the other line, or the other delivery's page appear in `work/`, or the other's entries already staged, says it is not a conflict and the session goes on (docs/05 §4; the kit's changelog story of the second session that stopped on a changed docs/06).
* A reader whose two deliveries both edit the same lines of `src/loans/loan.ts`, or whose page needs `src/loans/` while the other delivery is changing it, says it is a conflict: the session stops and reports, and the person orders the two lines (`· after`) or gives one a worktree.
* A reader about to commit `return-book` runs `git diff --cached --stat`, sees only that delivery's paths and its hunk of docs/06, and commits with plain `git commit`; seeing the other delivery's entries staged too, they know a plain commit takes both.
* A reader who commits with `git commit -- docs/06-Queue.md <paths>` knows git takes each named file whole from the folder, so the other line's mark rides into this commit (git-commit documentation, `--only`; checked on a scratch repository during /propose); the chapter gives the way out: commit each delivery as its session ends, before the other stages, or unstage the other's entries first and let its session stage again.
* A reader asked "one folder or worktrees?" answers from chapter 20 and 21 alike: trunk for one person, alone or with several sessions on free lines that touch different files; a branch per delivery for sequential work reviewed by pull request; a worktree per delivery for several people, or for one person whose deliveries touch the same files (kit SETUP.md Git text at `96c0930`).
* A reader of chapter 21's worktree sections finds them as today (what a worktree is, its life, in the kit, the conflict, the markers, when parallel stops paying), now framed as the second answer, with no sentence left saying that two agents in one folder always mix their deliveries.
* A reader of chapter 10's git strategy paragraph reads the same three answers as chapter 20, the trunk one with several sessions on free lines.
* Edge: a reader whose two sessions share one folder knows they also share its ports, its test database and its build output, so two test runs can collide there as in worktrees, and that one folder costs no second install.

**Contract.**

* **Chapter 21, both editions, file name kept** (`21-worktrees.md`, links stay). Title kept, "Worktrees and parallel agents" / "Worktrees e agentes em paralelo", so docs/00's contents do not change. Sections:
  1. Opening "After this chapter" rewritten to the Objective.
  2. "The problem: one folder, two jobs" rewritten: waiting on one agent; what goes wrong in one folder only when the files meet or one commit takes both.
  3. New "Two sessions in one folder": free line in one sentence, pointing to chapter 16; each session marks only its line, stages only its paths and its hunk of the queue; the person commits one at a time; `git diff --cached --stat`; the `git commit -- <paths>` trap and its way out.
  4. New "What is and is not a conflict there": the three not-conflicts and the two conflicts of docs/05 §4; the kit changelog's story, paraphrased.
  5. New "When a worktree still pays": the deliveries' files meet, or several people; then the existing sections from "What a worktree is" to "The trap", unchanged except line 93's "one session per folder" read against the new section.
  6. "When parallel stops paying": the checks for both forms (the queue conflicts only across worktrees; ports and databases shared in one folder too; dependencies only per worktree; you); the closing sentence says this book is on trunk and its docs/05 lets two sessions work in one tree.
  7. "What the team gains": the worktree run's numbers kept as they are; one folder removes the folder, the install (155 MB per worktree in that run), the merge and the queue's conflict, with no new number, said so; the changelog story as the error the rule removes.
  8. Key points rewritten to match.
* **Sources:** existing notes kept; new: focus-kit CHANGELOG, entry 2026.10.08.3 (public repository), and git-commit documentation for `--only`, accessed on the day written. No new run.
* **Chapter 20, both editions:** "Choosing" bullets for trunk and a branch per delivery, and the key point on trunk, follow the kit's Git text; a worktree per delivery named there, pointing to chapter 21.
* **Chapter 10, both editions:** line 56's three answers follow the same text.
* **Chapter 25, both editions:** line 63, "several at once in worktrees" becomes "several at once, in one folder or in worktrees" (the line asks for every chapter where git is chosen).
* **docs/03:** `trunk` row: "one person, alone or with several sessions on free lines that touch different files; not for two people"; `conflict` row gains: between two sessions in one folder, the same hunk edited by both, or a file one page needs that the other delivery is changing.
* **docs/05 §6** (the book differs from the template, as kit-2026-10-13 allowed): "the person commits one delivery at a time, naming its paths" becomes "the person commits one delivery at a time, from the index once `git diff --cached` holds only it; naming paths takes each file whole from the working tree, the other delivery's hunk of a shared file included."
* **ADR-0010:** a dated amendment: since `kit-2026-10-13`, two sessions may work in one tree on free lines that touch different files.
* **Cases:** none. Case A and Case B are not used.
* **Code examples:** none new; the lending library's slugs and paths are illustrations written for the chapter, said so.

**Out of scope.**

* The queue's order, `· after` and which lines run together as a lesson: `ch13-16-queue-order`; chapter 21 only points to chapter 16.
* /apply staging only its delivery as a lesson: `ch15-apply-ends`.
* A new parallel run in one folder: the changelog is M12's evidence, and runs are not the chapter's thread (ADR-0017).
* Renaming the chapter or its file: would change docs/00's contents and every link for no reader gain.
* Telling the kit that its §6 sentence takes the other hunk: a note for the author, not this repository.

**Done when.**

* [x] Chapters 21, 20, 10 and 25 changed in both editions, same headings; chapter 21 opens with its value; no filler and nothing useful cut.
* [x] Every number and quote sourced; the `--only` behaviour checked on a scratch repository again in /apply and the documentation's words quoted exactly.
* [x] No sentence in the book says two agents in one folder always mix deliveries, or that trunk is only one delivery at a time.
* [x] docs/03, docs/05 §6 and ADR-0010 read as the Contract says.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths, the commit suggested in a `commit` block.

## What happened

* **Tree before editing.** `docs/06-Queue.md` modified (this line `[ ]` to `[>]`, by /propose) and `work/ch21-one-tree.md` untracked: both this delivery's; index empty; on `main`, no worktree.
* **The CHANGELOG has no note.** The Contract listed the kit's CHANGELOG under Sources, but docs/04 §Chapter shape says no note points to a file of focus-kit's repository. Asked in the conversation; the author chose docs/04 as written: chapter 21 names "the kit's changelog, at entry 2026.10.08.3" in plain words and paraphrases the story. The one new note is `[^git-commit]`.
* **`--only` checked again** on a scratch repository (git 2.56.0): a shared file with two hunks, only the first staged, plus one file wholly owned. `git commit -- <shared> <owned>` committed both hunks of the shared file; a plain `git commit` committed only the staged hunk. `git restore --staged -p` unstaged the second hunk alone. Quoted from the git-commit documentation, option `--only`, accessed 2026-10-13: "Make a commit by taking the updated working tree contents of the paths specified on the command line, disregarding any contents that have been staged for other paths." The chapter quotes it from "by taking".
* **Divergence: "How it solves the problem"** in chapter 21 now says the two example deliveries both need `src/loans/` (pt `src/emprestimos/`), so the worktree example does not contradict the new section that puts the same pair in one folder. The Contract asked those sections unchanged except line 93.
* **Divergence: the old problem's argument moved.** The branch-in-one-folder and second-clone paragraphs, which led to "That is a worktree", moved from "The problem" to "When a worktree still pays", where they now argue for it.
* **Beyond the Contract's named lines, for Done when 3:** chapter 20's "Trunk, and trunk-based development" sentence ("one person committing on `main`, one delivery at a time") and its opening (now naming a worktree per delivery among the choices), both editions.
* **Free line.** Chapter 16 does not define it yet (`ch13-16-queue-order` will); chapter 21 defines it in one sentence and points to chapter 16 for the marks; chapters 20 and 10 gloss it in place ("queue lines ready to build", "deliveries ready to build").
* **No new number.** One folder's saving is said without a number, as the Contract asked; the 155 MB is the worktree run's.
* **Proof.** `make verify` green (build, parity, em dash, prose, links, disclosure); `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` with their EPUBs.
* **Environments.** Local builds; GitHub Pages and Release unchanged until the author pushes and tags (docs/05 §5).
* **Dependent lines.** None names `ch21-one-tree` in `· after`.

```commit
docs(ch21-one-tree): teach two sessions in one folder before worktrees

- chapter 21: one folder on free lines, what is and is not a conflict
- chapter 21: commit from the index; naming paths takes the whole file
- chapters 20, 10, 25: trunk with several sessions; worktree per delivery
- docs/03 trunk and conflict, docs/05 §6, ADR-0010 amendment

work/done/ch21-one-tree.md
```
