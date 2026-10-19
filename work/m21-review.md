# m21-review

**Objective.** The author can decide whether each promise of M21 holds in both editions and in the installed process, with every confirmed failure recorded as a new finding under this review.

**Behaviour.**

* With every line M21's review names `[x]`, the author receives both PDFs built at the end commit and the clause checks below, each with its chapter sections and their start pages in both editions; each answer is recorded as holds, or fails with what the author saw.
* The review compares the installed commands and the active documents with focus-kit 2026.10.19 as `work/done/kit-2026-10-19.md` records it (SETUP.md at the kit's `fd1aa75`), then checks the book's explanations against those rules.
* On the author's word, read-only area readers read one fixed range, `git diff <base>..<end>`; one checker tests each candidate against that same snapshot and labels it seen, latent or weak before the author decides which become findings.
* A clause with no answer, a required reader that cannot run, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8); a partial reading that found nothing never closes it.
* A commit made during the reading does not move the end commit; what it changed is named as outside this reading. Each confirmed candidate becomes a `[ ]` line under this review, with no fix made here.

**Contract.** Clause checks from docs/06's M21 paragraph, each against the named deliveries' pages in `work/done/` and the cited chapter sections in both PDFs (`output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`):

| Clause | Deliveries and passages | Author's question |
|---|---|---|
| The book teaches focus-kit 2026.10.19 and the repository runs on it | `kit-2026-10-19`, `ch08-update-2026-10-19`; installed skills, docs/05, AGENTS.md; chapter 8, "What the install never touches, and how to update", "What an update reports", "How each host finds the commands" | Does the update example in chapter 8 match what this repository's update to 2026.10.19 did: a custom edit shown against the kit file it was made on, the prior version checked in the kit's history or taken on the person's word, the next command named for a documented project, and Copilot's order for a skill found in both folders? |
| /propose branching before it marks `[~]` | `ch12-branch-then-mark`; chapter 12, "What `/propose` does", "Key points" | Can a reader say where `/propose` starts on trunk, on a branch per delivery and on a worktree per delivery, and that the `[~]` mark is its first edit there? |
| Where a board sees a mark | `ch14-where-a-board-sees`, `ch18-19-one-index`; chapter 14, "At the moment the work changes"; chapter 19, "Worktrees in the kit" | On trunk, when does a board see a line turn `[~]`; with a branch or worktree per delivery, when? |
| The commands following every slot of docs/05 §5, the project's own included | `ch07-slots-and-decided`, `ch07-review-git-slots`, `ch13-apply-reads-00-03`, `ch13-19-commit-by-slot`; chapter 7, "The seven documents", "The two choices", "AGENTS.md"; chapter 13, "What it reads", "Why it stops at the stage", "The commit is the human review"; chapter 18, "Commits and the history", "Choosing"; chapter 19, "Worktrees in the kit"; chapter 23, "Roles in a team" | Can a reader add a slot of their own to docs/05 §5 and say that `/propose` and `/apply` follow it with no edit to a skill; and, under a Git slot that lets the agent commit by its word, say who still decides each commit and why every "you commit" sentence still holds? |
| The Milestone review slot choosing the host's deep review or the kit's readers | `ch15-who-reads`, `ch11-23-who-reads`, `ch07-review-git-slots`, `ch09-second-pair-of-eyes`, `docs03-review-reads`; chapter 9, "`/brainstorm`: a new project", "What it asks"; chapter 11, "The review, and its findings"; chapter 15, "The review is a delivery", "Read the code since the base"; chapter 23, "Roles in a team"; docs/03's `milestone review` row | Given a project whose host has a deep review and one whose host has none, can a reader say who reads the milestone's code in each, what the checker does either way, and which base a review names where no earlier review exists? |
| /apply reading docs/00 and docs/03 | `ch13-apply-reads-00-03`; chapter 13, "What it reads", "`lend-book`, built", "Key points" | Which five documents does `/apply` read, and what does it take from docs/00 and from docs/03 in the `lend-book` example? |
| The one index of a working tree | `ch18-19-one-index`; chapter 18, "One delivery, one step to undo", "Commits and the history"; chapter 19, "Two sessions in one folder", "What a worktree is and when it pays" | Two sessions in one folder, and the second finds the first's change staged: what does it run, and why does the index hold one delivery when the person commits? |
| The queue's rules written once in docs/05 §4 | `kit-2026-10-19` (docs/06's header), `ch07-slots-and-decided`; chapter 7, "The seven documents", "AGENTS.md" | Where does a reader look for what a mark means and when it changes, and what does AGENTS.md answer about what a page decided? |
| SETUP.md §1's step 4 as a list | `ch08-update-2026-10-19`; chapter 8, "What an update reports" | Can a reader read the report's step 4 as a list by section of the documents and say what each item asks them to change by hand? |
| What the kit assumes of one person, a team and a reader who does not read code | `ch20-one-person-assumed`, `ch20-reader-no-code`; chapter 20, "The problem", "The pull request as the team's review", "Boards" | Who does the kit assume proposes, uses, reviews and commits; on a team, who is the reviewer; what a Board slot replaces; and what part a person who does not read code takes in `/propose`, in using the delivery and in asking where things stand? |
| No clause as written | `ch06-kit-after-ninjobs` (chapter 6, "Where it went"); `ch16-ceiling-moves` (chapter 16, "It works both ways", "A ceiling, and where the words go") | Does chapter 6 say Ninjobs' 91 deliveries ran on its own two commands and the kit arrived after the opening; does chapter 16 say where the words go when a command is full, with the kit's three ceilings? |

**Base.** `a50474bc4debd01a933641ca5c509fa7e9d1c956`, the commit of m19-review. M20 has no review of its own: `m20-review` was dropped because m19-review's reading, "review M19 and M20 code", already covered M20's range. So no review of the previous milestone exists, and this page names the last review's commit, as docs/05 §8 asks where no earlier review exists. The range therefore also holds the fixes of M19's seven findings (`docs05-blocked-trunk`, `adr0010-commit-asked`, `readme-release`, `pt-blocked-term`, `kit-proposals-ninjobs-phases`, `ch16-two-checks-stayed`, `ch13-next-milestone`), which get no second review (docs/05 §8), and the release commit of v1.2.4 (`VERSION`): the clause checks above are M21's alone, while the readers read the whole range, as m19-review did with M20's.

**End.** The commit HEAD is when the reading starts; /apply records it before launching any reader, and nothing it records later moves it.

**Areas.** The paths `git diff --stat a50474b..HEAD` shows today, at `234fbd7` (76 paths, 2780 insertions, 506 deletions), by the areas of docs/05 §5's Milestone review slot. /apply recomputes them at its end commit and splits an area too large for one careful reading:

* **Build:** `VERSION`, `README.md`, `README.pt.md`.
* **Chapters**, split in two:
  * chapters 06 to 13, both editions: `book/{en,pt}/06-birth-of-focus-kit.md`, `07-the-documents.md`, `08-install-and-hosts.md`, `09-starting-a-project.md`, `11-queue-and-milestones.md`, `12-propose.md`, `13-apply.md` (14 files);
  * chapters 14 to 23, both editions: `book/{en,pt}/14-queue-states.md`, `15-closing-a-milestone.md`, `16-the-governor.md`, `18-git-essentials.md`, `19-worktrees.md`, `20-team-tools.md`, `23-adoption.md`, and `book/pt/17-project-as-assistant.md` (15 files).
* **The kit's skills:** `.claude/skills/{analyze,apply,brainstorm,propose}/SKILL.md`, `.claude/skills/{analyze,brainstorm}/references/documents.md`, and the same six under `.agents/skills/` (12 files), each also compared byte for byte with SETUP.md §3 of 2026.10.19.
* **The documents**, split in two:
  * documents: `AGENTS.md`, `docs/03-Domain.md`, `docs/05-Process.md`, `docs/06-Queue.md`, `docs/adr/ADR-0010-trunk.md`, `docs/adr/ADR-0018-six-marks.md`, `work/kit-proposals.md`;
  * delivery records: the 24 pages added to `work/done/` (`adr0010-commit-asked`, `ch06-kit-after-ninjobs`, `ch07-review-git-slots`, `ch07-slots-and-decided`, `ch08-update-2026-10-19`, `ch09-second-pair-of-eyes`, `ch11-23-who-reads`, `ch12-branch-then-mark`, `ch13-19-commit-by-slot`, `ch13-apply-reads-00-03`, `ch13-next-milestone`, `ch14-where-a-board-sees`, `ch15-who-reads`, `ch16-ceiling-moves`, `ch16-two-checks-stayed`, `ch18-19-one-index`, `ch20-one-person-assumed`, `ch20-reader-no-code`, `docs03-review-reads`, `docs05-blocked-trunk`, `kit-2026-10-19`, `kit-proposals-ninjobs-phases`, `pt-blocked-term`, `readme-release`) and the move of `work/m20-review.md` to `work/done/m20-review.md`.

**Readers.** Six read-only readers on Opus, one per area above, each keeping the session's advisor, Fable, at most two at a time, then one read-only checker on Opus; no other model runs the review (docs/05 §5, Milestone review). Each reader lists the paths it read.

**Slow tests.** The Verify slot names none; none is invented for this review.

**Known candidates for the checker**, from the deliveries' own reports:

* Chapter 19, "Worktrees in the kit", line 196 (both editions): "Each step comes after your reading" should open with "By default" (pt "Por padrão") under the Git slot's commit form, as chapter 13 line 165 and chapter 23 line 64 now do; `ch13-19-commit-by-slot` left it on purpose, reading it as the asked steps, and proposed it as a line.
* docs/05 §8 names two answers for who reads, the host's deep review or the kit's readers, while docs/03's `milestone review` row and chapter 15 (line 63) name three, counting none. docs/05 §8 is the kit's template text: SETUP.md §8 names two, and its Milestone review slot template ends "or: none". If confirmed, likely a kit note rather than a line here (m19-review's B3 and E6); `docs03-review-reads` left the choice to the author.
* Chapter 7, "The two choices", line 145, sends the 21-day loan period to docs/03; chapter 12, lines 59 and 114, says it comes from docs/00 (`ch13-apply-reads-00-03`, Decisions). It answers no clause of M21: if confirmed, a line under the next milestone (docs/05 §4).

Only this page, its move to `work/done/` and its findings' lines change; no chapter, document or build change.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit; /apply records the start page of every chapter in both editions.

**Out of scope.**

* Fixing any finding: each becomes its own line (docs/05 §8).
* Re-testing M19's or M20's clauses: their reviews answered them.
* Changing the readers' model or the slot: docs/05 §5 owns it.
* Taking the approval of this page as the author's PDF reading or as the word that starts the readers: each is asked in the /apply session.

**Decisions.**

* The base is m19-review's commit, named with its reason, since M20's review was dropped as already read (docs/05 §8, docs/06's `m20-review` line).
* The range's M19 finding fixes and release commit are read by the area readers but have no clause here (docs/05 §8: findings get no second review; m19-review did the same with M20).
* `ch06-kit-after-ninjobs` and `ch16-ceiling-moves` answer no clause of M21's paragraph as written; they stay in M21 as the queue placed them, with their own row so their promise is still tested, and the author decides whether the paragraph should name them (docs/05 §4; m19-review's E4).
* Two chapter readers and two document readers, the build and the skills one each, as m19-review split its range (docs/05 §8: an area too large for one careful reading splits again).
* A confirmed candidate on a clause of M21 becomes a `[ ]` line under this review (docs/05 §8); one that answers no clause of M21, as the 21-day candidate, goes under the next milestone (docs/05 §4).
* The end commit and the final path inventory are inputs /apply fixes before reading, not open scope (docs/05 §8, `ch15-review-head`).

**Done when.**

* [ ] Every line in this review's `after` is `[x]`, and every clause above has the author's answer.
* [ ] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read and every checked candidate are recorded on this page.
* [ ] Every candidate the author confirms is its own `[ ]` line under this review, or under the next milestone as Decisions says; nothing is fixed here.
* [ ] `make verify` is green after the last edit, both PDFs were built at the end commit for the author's reading, and only this review's changes are staged, with its suggested commit message.
