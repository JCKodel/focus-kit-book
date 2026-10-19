# ch07-slots-and-decided

**Objective.** After chapter 7 the reader can also add a slot of the project's own to docs/05 §5 that `/propose` or `/apply` follows with no edit to a command file, say that the queue's rules are written once, in docs/05 §4, with docs/06 pointing there, and ask the agent what a delivery decided or why, knowing it answers from that delivery's page and the ADRs it names.

**Behaviour.**

* Opening: the chapter's "After this chapter you can..." lines name the new capability in one clause each edition: adding a slot of the project's own that the commands follow. The rest of the opening stays.
* A reader asked "your team wants every mark change pushed to its board; where does that go?" answers: a slot the project adds to docs/05 §5, saying what and the command and naming the command that follows it, not an edit to `/propose` or `/apply`; and says why: the command files are the kit's, written by its installation, while the slot is the project's fact, in the document the commands already read.
* The reader can say which command follows a project slot: the one the slot names; a slot that names neither `/propose` nor `/apply` is a fact the commands read like any other, and the shape rule holds for it too (what and the command, a few lines, steps in a manual).
* The chapter shows one project slot, from the lending library's docs/05, written for this chapter and said so: a `Board` slot of two or three lines naming the command that pushes docs/06 to the team's board, that `/propose` and `/apply` run it whenever they change a mark, and that they say so when it fails. English identifiers in the English edition; in the Portuguese edition the slot's prose in Portuguese and its command name in Portuguese, as the library's other Portuguese examples are (docs/04).
* A reader asked "where are the marks and the `· after` suffix defined?" answers docs/05 §4, written once there; docs/06's header points to it and the queue holds milestones and lines, not its own rules; and ties it to the chapter's opening problem: two copies of a rule drift.
* A reader asked "how does an agent answer why `lend-book` refuses a member with an overdue copy?" says: `AGENTS.md`'s how-to-work section tells it to answer from the delivery's page, `work/done/<slug>.md`, and the ADRs that page names, not from memory or the commit message.
* Edge: the "ten slots" count of docs/05 stays ten, since a project slot is not one of the kit's; the sentence that adds project slots says they come in addition to the ten.
* Edge: `AGENTS.md` still holds no rule of its own; the new line points at the page and the ADRs, which hold the answer, consistent with the three rules the chapter already gives.
* Fails: no sentence says the kit "now" allows project slots, that `/propose` once marked first, that the docs/06 header once repeated the rules, or gives a version, date or number for these kit changes (AGENTS.md, memory "book is the kit today"). No sentence narrates the reinstall of `kit-2026-10-19`. No pointer to a later chapter outside `## What the team gains` (docs/04, `early-no-forward-links`); in particular no "chapter 20" next to the Board example.
* Both editions say the same, paragraph for paragraph; `make verify`'s parity check passes.

**Contract.** Files: `book/en/07-the-documents.md` and `book/pt/07-the-documents.md`, only these sections:

* Opening (lines 3 to 4 en, 3 to 4 pt): one clause for adding a project slot.
* `## The seven documents` / `## Os sete documentos`, the **docs/05** paragraph: after "The commands read these facts here, so no command file holds any of them." (pt "Os comandos leem esses fatos aqui, então nenhum arquivo de comando guarda algum deles."), two to four sentences: the project may add slots of its own beside the ten; a slot that names `/propose` or `/apply` is followed by that command with no edit to its file; the command files are the kit's and the installation writes them; then the lending library's `Board` slot as a short quoted block, written for this chapter. Wording source: docs/05 §5 intro ("The project may add slots of its own; a slot that names /propose or /apply is followed by that command, with no edit to the skill.") and the kit template in `.claude/skills/brainstorm/references/documents.md`.
* Same section, the **docs/06** paragraph: one sentence that the queue's rules, the marks, the suffixes, the order and what may run at the same time, are written once, in docs/05 §4, and docs/06's header points there. Source: `documents.md`'s docs/06 paragraph ("written once there") and this repository's docs/06 header.
* `## AGENTS.md`: one or two sentences after "It has four short sections...": the how-to-work section tells the agent, asked where things stand, to answer from docs/06 and `work/`, and asked what a delivery decided or why, from its page and the ADRs it names; one line of the lending library as the example (`lend-book`). Source: AGENTS.md template in `documents.md` and this repository's AGENTS.md.
* `## What the team gains` / `## O que o time ganha`: one sentence: a team's own step, such as refreshing its board, lives in its own docs/05 and survives every update of the kit's commands, since the update replaces only the kit's files and stops on a command file it does not recognize. Source: SETUP.md §1 of focus-kit 2026.10.19 (step 1 recognizes, a custom edit is shown as a diff and stops the run), as `work/done/kit-2026-10-19.md` records. No number.
* `## Key points` / `## Pontos-chave`: the first or fourth bullet gains a clause each for project slots and the queue's rules in docs/05 §4; the AGENTS.md clause of the fourth bullet gains "and answers what a delivery decided from its page and ADRs".

Terms of docs/03 used: `slot` (its row already says a project may add one that /propose or /apply follows), `queue`, `queue line`, `mark`, `free line`, `page`. No new docs/03 row. Sources cited: none new; no footnote to a kit file (docs/04, kit named in prose). Cases: none private; the lending library only. No data, schema or API.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.**

* The ten-slot list's wording of the Milestone review slot ("the areas ... and the model its readers and checker run on"), which the kit now words as who reads, the host's deep review or the kit's readers: not in this line; reported to the driver as a gap no M21 line names.
* "The git strategy" paragraph's "the agent never commits or merges on its own": the kit's Git slot may now say the agent commits by the slot's word; not in this line, reported to the driver likewise (ch20-one-person-assumed is about who commits on a team, not this sentence).
* Case A's board mirror and its story: ch20-one-person-assumed.
* Where a board sees a mark: ch14-where-a-board-sees.
* `/propose`'s order, branch then mark: ch12-branch-then-mark.
* The pt-only paragraph on folder names (pt line 17): unchanged.
* docs/03, docs/05, docs/06, AGENTS.md: already say all this since kit-2026-10-19; no edit.

**Decisions from the documents.**

* The example slot is a `Board` slot of the lending library: it is the kit's own motivating case (focus-kit CHANGELOG 2026.10.19) and the shape docs/05 §5 describes, and the lending library is the book's example project (docs/04). It is written for this chapter and said so (AGENTS.md non-negotiables).
* The count stays "ten slots": the kit template still has ten (`documents.md` §5); a project slot is added beside them.
* No pointer to chapter 20 from the Board example: docs/04's rule for chapters 0 to 7 (`work/done/early-no-forward-links.md`).
* No before/after, version or date in the text (AGENTS.md; `work/done/kit-as-it-is.md`).
* The Portuguese edition keeps "slot" as the term (`work/done/pt-slot-term.md`) and Portuguese names in the library's example (docs/04).

**Decisions taken alone.**

* The three changes go into the existing docs/05, docs/06 and AGENTS.md paragraphs, not a new section: each is one fact about a document the chapter already describes.
* The AGENTS.md example question is about `lend-book`, the library's delivery of chapter 12, named without a pointer.
* The gain sentence states the mechanism (the update replaces only the kit's files and stops on an unrecognized edit), not the kit's story of a project that redid its edit on every update, which would be a before/after and an unnamed project's history.
* The two stale sentences (Milestone review slot wording, Git paragraph) are left as they are and reported, since the line's scope does not name them.

**Done when.**

* [ ] Both editions written, same file name, each Behaviour line checkable in the text.
* [ ] Opens with its value; no filler and nothing useful cut; the chapter keeps everything else it says.
* [ ] No number added; the example is the lending library's, written for this chapter and said so.
* [ ] No em dash; no pointer forward outside the gain section; no before/after of the kit.
* [ ] `make verify` green after the last edit; `make book` builds both editions and both PDF paths are given to the author.
* [ ] Delivery review as docs/05 §5 says; no private case used, so OD-3 approval is inapplicable; only this delivery's paths staged (docs/05 §6) and the commit message suggested.
