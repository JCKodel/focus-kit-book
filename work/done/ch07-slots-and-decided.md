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
* /apply, the author absent (driver session): the Portuguese Board slot is named `Quadro` and its command `npm run quadro`, as the page says. A project's own slot is the project's text, not the kit's, so it takes the documentation language, as the library's manuals do (`publicar-o-app.md`); the script name is one the library invents, so docs/04's rule on Portuguese names applies. Chapter 13's `npm run verify` and `npm run migrate` stay as they are: not this line.
* /apply: the opening's new clause goes on the first sentence ("including a step of the team's own, which becomes a slot of docs/05 that the commands follow"), so the second sentence's "that" still refers to changing documents by talking to the agent.
* /apply: the Key points' fourth bullet says `AGENTS.md` "tells the agent to answer" what a delivery decided, not "answers", since the file does not answer; the meaning of the Contract's clause is kept.
* /apply: the gain sentence says what the kit's SETUP does, as `work/done/kit-2026-10-19.md` records it: an update writes only the kit's files and stops, writing nothing, on one holding an edit it does not recognize.

**Implementation.** `book/en/07-the-documents.md` and `book/pt/07-the-documents.md`: the opening's first sentence; the docs/05 paragraph gains four sentences and the lending library's `Board` slot (`Quadro` in pt) as a fenced block, written for this chapter; the docs/06 paragraph gains one sentence on the queue's rules in docs/05 §4, with a gloss of `· after`, which no earlier chapter explains; `## AGENTS.md` gains two sentences and the `lend-book` (`emprestar-livro`) example; the gain section one sentence; Key points the first and fourth bullets. Nothing else in the chapter changed. No shared file touched.

**Proof.** `make verify` green after the last edit (the first run failed only on `book/pt/08-install-and-hosts.md`'s parity, another lane's file in flight, untouched here; every other check passed on chapter 7 then, and the whole verify passed on the final run). `make book` is the driver's, run once at the end of the batch.

**Delivery review.** A read-only general-purpose agent on Opus read `git diff HEAD` of both chapter files, this page, docs/04, AGENTS.md, docs/05 §§4 and 5, the docs/06 header, the kit's `documents.md` and `work/done/kit-2026-10-19.md`, and ran the check scripts. No must-fix; seven optional findings:

1. Key points first bullet: the queue-rules clause blurred docs/05's item into docs/06's. Fixed: moved to docs/06's item, "whose rules are written once in docs/05 §4".
2. Key points fourth bullet: "so the agent answers" claimed a false cause. Fixed: "and tells the agent to answer".
3. Gain sentence: "stops on a command file it does not recognize" was loose against the source. Fixed: "writes only the kit's files and stops, writing nothing, on one that holds an edit it does not recognize".
4. The project-slot sentence repeated the shape rule two lines above. Fixed: "keeps the shape above".
5. `· after` appeared unexplained. Fixed: "which holds a line until another is done".
6. The Board slot says "change a mark" five lines before marks are introduced. Left: the docs/06 paragraph right below defines it, and the slot is quoted as the library wrote it.
7. pt: "quando perguntam" and the ambiguous "ela". Fixed: "quando lhe perguntam", "essa página".

Verify ran again after the fixes: green.

**Divergences.** None from Behaviour or Contract beyond the wording decisions above and the `· after` gloss the review asked for.

**Done when.**

* [x] Both editions written, same file name, each Behaviour line checkable in the text.
* [x] Opens with its value; no filler and nothing useful cut; the chapter keeps everything else it says.
* [x] No number added; the example is the lending library's, written for this chapter and said so.
* [x] No em dash; no pointer forward outside the gain section; no before/after of the kit.
* [x] `make verify` green after the last edit; `make book` builds both editions and both PDF paths are given to the author (the driver runs `make book` once for the batch and gives the paths).
* [x] Delivery review as docs/05 §5 says; no private case used, so OD-3 approval is inapplicable; only this delivery's paths staged (docs/05 §6) and the commit message suggested (staging is the driver's).

```commit
docs(ch07-slots-and-decided): project slots, queue rules, decided

- chapter 7 shows a project slot the commands follow, the library's Board
- docs/06's rules are written once in docs/05 §4, its header points there
- AGENTS.md sends "what did a delivery decide" to its page and ADRs
- a team's own step survives kit updates; key points updated

work/done/ch07-slots-and-decided.md
```
