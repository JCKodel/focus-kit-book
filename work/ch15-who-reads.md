# ch15-who-reads

**Objective.** After chapter 15 a reader can say who reads a milestone's code, as docs/05's Milestone review slot chooses it: the host's deep review, which the person launches once over the range the review's page names, when the host has a review that takes the whole range; or the kit's readers, one read-only agent per area of the slot; or none; with one checker marking every candidate either way; and can name the base of a review where no earlier review exists, a commit the page names with its reason; both editions.

**Behaviour.**

* Asked who reads a milestone's code, the reader answers: the Milestone review slot says, the host's deep review over the range or the kit's readers by area, or none, and the hand test runs in all three.
* The reader can say what the host's deep review is: the host's own review command, launched by the person, once, over `<base>..<review-head>` from the two commits the review's page records, reading the range whole by its own split and reporting candidates by file and line; and when a slot names it: when the host has such a review that takes the whole range.
* The reader can say how it differs from the kit's readers: the readers split the range by the slot's areas, one per area, each listing the paths it read, and the page checks that list against the range; the deep review takes the range whole in one launch.
* Either way, the reader knows one checker, an agent or the review's session, opens each candidate's file and marks it seen, latent or weak before the person sees it, and that a candidate the person confirms is a finding like the others.
* Edge, the base: for a project whose earlier milestones closed with no review line, so no previous review's commit exists and the milestone is not a first one, the reader knows the review's page names a commit as the base and says why it chose it; the range still excludes that commit, as it excludes a first commit.
* Edge, none: a slot that says none launches no deep review and no readers; the hand test and the slow tests still run (the chapter's existing sentence, kept).
* Fails if: the chapter names the code reading only by areas, sends the deep review's candidates to the person unchecked, has the session launch the deep review itself, names a host's command, a model or a cloud, tells how the kit chose before, or narrates a run of this repository.

**Contract.**

Chapter `book/en/15-closing-a-milestone.md` and `book/pt/15-closing-a-milestone.md`, same passages in both:

* Opening, second sentence: "split by areas with one read-only agent each and a checker before the person sees a candidate" becomes: read by whoever docs/05's Milestone review slot names, the host's deep review or one read-only agent per area, and a checker either way before the person sees a candidate. The first and third sentences stay.
* §The review is a delivery:
  * the base sentence ("Its page names as the base the commit of the previous milestone's review, or, for a first milestone, the project's first commit, ...") gains the third case of docs/05 §8: where no earlier review exists, the commit the page names and why; its listing clause, "lists, by the areas docs/05's Milestone review slot names, the paths that range changed", keeps the areas only for the kit's readers;
  * "each area gets a reader of its own, which reads it with the whole repository open" becomes: who reads is the slot's, the host's deep review or a reader per area (§Read the code since the base says how);
  * the first-commit exclusion sentence gains, in one clause, that a base the page names is likewise outside its own range. Every other sentence of the section stays.
* §Read the code since the base, by areas: the title becomes `## Read the code since the base` (pt `## Leia o código desde a base`); no link points to its anchor. Changes inside it:
  * "docs/05's Milestone review slot says how the range is split: ..." becomes the slot's three answers: the host's deep review the person launches over the range, when the host has one that takes the whole range; the kit's readers, by areas, one reader each, on the model the slot names or the session's; or none.
  * A new short paragraph, after that one: what the host's deep review is (the host's own command that reads a whole range in one launch and reports candidates by file and line), that the person launches it, once, over `<base>..<review-head>` from the page, never over `HEAD`, and that it splits the range its own way, so the slot names no areas for it.
  * The lending library slot block and the area paragraph stay, introduced as the readers' form of the slot.
  * "The reading runs in any host." paragraph: said of the kit's readers.
  * The paths-read paragraph: said of the readers' lists.
  * "One checker, an agent or the review's session itself, ..." gains "either way", over the readers' candidates or the deep review's.
  * The three-candidate block, its following paragraph, "The readers and the checker fix nothing" (gains the deep review) and the none sentence stay.
* What the team gains: unchanged unless the checker sentence needs "either way"; /apply decides, defaulting to no change.
* Key points 2 and 3: key point 2's base gains "or, where no earlier review exists, the commit the page names and why"; key point 3's "by the slot's areas, one read-only agent each, all on those two recorded commits, listing the paths it read" becomes: read by the host's deep review or by the slot's areas, one read-only agent each listing the paths it read, all on those two recorded commits.

Terms of docs/03 used: milestone review, checker, candidate, finding, slot, milestone; "host's deep review" is the wording of docs/05 §5, §8 and docs/03's `milestone review` and `checker` rows, in Portuguese "revisão profunda do host". No new docs/03 row. Sources: docs/05 §5 (Milestone review) and §8 as installed by `kit-2026-10-19` (`work/done/kit-2026-10-19.md`), which take the kit template's text; the installed `.claude/skills/analyze/references/documents.md` slot template. No number, no footnote, no private case; the lending library slot block exists already.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* The Ninjobs section, "A line, and not a fix", "No second review", "Test each clause by hand" and "The problem": untouched.
* This repository's own choice of the kit's readers (`work/done/review-slot-models.md`) and why: a run of this repository (ADR-0017); chapter 15 teaches the choice, not this project's answer.
* m21-review's base: its own page names it.
* Chapters 11 and 23, which say the session has the code read "by the areas docs/05 names, when it names areas": they stay true for a slot of readers and are not this line's; chapter 7's slot list is `ch07-review-git-slots`, and chapter 9's question is `ch09-second-pair-of-eyes`, which points here for what the deep review is.
* docs/03, docs/05, docs/06: no change; `kit-2026-10-19` already wrote them.

**Decisions from the documents.**

* Who reads is one of three answers of the slot, the host's deep review, the kit's readers, or none: docs/05 §8 and the slot template in `.claude/skills/analyze/references/documents.md`.
* The deep review is launched by the person, over the range the page names: docs/05 §8 ("which the person launches over that range"); the session still says when it is time and starts nothing without the person's word.
* The checker runs either way: docs/05 §8 ("Either way, one checker") and docs/03's `checker` row.
* The base where no earlier review exists is a commit the page names and why: docs/05 §8 and docs/03's `milestone review` row.
* The deep review fits when the host has one that takes the whole range: the slot template ("when the host has one that takes the whole range").
* The book teaches the kit as it is: no before/after, no version, no account of why the kit added the option (docs/04 "The kit as it is", ADR-0017).

**Decisions taken alone.**

* No host command is named: chapters 8, 9 and 13 name none (`work/done/ch08-09-review-slot.md` decision 5, `work/done/ch15-review-by-areas.md` decision 10, `work/done/ch09-second-pair-of-eyes.md`), and the slot template's "named with its command" is said as "the slot names the command the person launches". Alternative the author may prefer: Claude Code's `/code-review ultra` as one example, which the chapter named before; left out to keep chapters 8, 9, 13 and 15 consistent.
* The deep review's form of the slot is said in prose, not as a second code block: one block of the readers' form already shows the slot, and a block with a placeholder command teaches nothing a sentence does not.
* The paths-read check and the `[?]` wait are taught as the readers' (docs/05 §8 puts the paths read in the readers' branch); the chapter does not claim the deep review lists the paths it read.
* The base where no earlier review exists gets one example reason, in the present: a project whose earlier milestones closed with no review line names, for instance, the commit that closed the last of them, because nothing after it was read as a whole; written for the chapter and said so, no lending library number.
* The section title drops ", by areas", since the section now teaches both readers; nothing links to its anchor.
* Portuguese: "revisão profunda do host", as the edition says "do host" elsewhere (chapters 1, 7, 8, 13).
* The gain section defaults to no change.

**Done when.**

* [ ] Both editions written, the same passages changed in each, Portuguese read as Portuguese.
* [ ] The chapter still opens with what the reader can do after it, now naming who reads as the slot's choice; no filler and nothing useful cut.
* [ ] The three answers of the slot, the person launching the deep review over the recorded range, the checker either way, and the base where no earlier review exists are each said once in the body and agree with docs/05 §8.
* [ ] `grep -n -i -E "code-review|ultra|opus|fable|advisor|cloud|no longer|2026\.10" book/en/15-closing-a-milestone.md` and `grep -n -i -E "code-review|ultra|opus|fable|advisor|nuvem|não mais|2026\.10" book/pt/15-closing-a-milestone.md` find nothing; no before/after, no narrated run, no em dash.
* [ ] Every link resolves; no number added, so none to source.
* [ ] Delivery review as docs/05 §5 says.
* [ ] `make verify` green; `make book` builds both editions, and the two PDF paths are reported.
* [ ] Only this delivery's paths and its hunks of docs/06 staged; the page moved to `work/done/` and its commit message suggested.
