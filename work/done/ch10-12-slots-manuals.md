# ch10-12-slots-manuals

**Objective.** After chapters 10 and 12 a reader writes a docs/05 slot as what and the command, in a few lines, because `/apply` reads it every time, with the steps in a manual and what a command prints left in its help; and knows that a manual in `docs/manuals/` is one action of more than one command, readable alone by whoever runs it: what a person does by hand outside a delivery, or a proof `/apply` runs on another machine. Both as focus-kit 2026.10.16 says.

**Behaviour.**

* A reader writing the library's Proof of a screen slot, when the proof publishes a preview to the test server and runs the end-to-end tests there, writes the command and a pointer to `docs/manuals/prove-on-the-test-server.md` (pt `provar-no-servidor-de-teste.md`), in a line or two; the steps (connect, publish the preview, run the tests, read the result, take the preview down) go in the manual.
* Failure: a slot that runs twenty lines, listing those steps and pasting what the test command prints. The reader knows from chapter 10 that `/apply` reads that slot on every delivery, that a person looking for how the proof runs does not look there, and asks the agent to shrink it to what and the command, the steps to a manual and the output left to the command's help.
* Failure: a slot that says which delivery created the command, or how it used to work. The reader knows it is more than what and the command, so it leaves the slot: history belongs on the page in `work/done/` and in the ADR. (The chapter says this follows from "what and the command", not as a sentence of the kit.)
* Edge: a single command needs no manual: `make verify` stays in the Verify slot as what and the command. A manual starts at an action of more than one command.
* A reader asked "who reads a manual?" answers: whoever runs it, having read nothing else; a person for publishing the app, and `/apply` for the proof on the test server. The slot points to it either way.
* A reader asked "where does the proof on another machine go?" answers from "Where a new fact goes": a manual in `docs/manuals/`, the slot keeping the command and pointing to it.
* A reader reviewing what `/brainstorm` or `/analyze` wrote (chapter 12) checks that every slot of docs/05 is what and the command, with no steps and no pasted output, and that each such action has its manual.
* Edge: a reader whose `/brainstorm` ends with no `docs/manuals/` still knows that is right: the folder comes with the first manual, whether it is something done by hand or a proof on another machine.

**Contract.**

* **Chapter 10, both editions, file name, title and headings kept.**
  1. "One place per fact": `docs/manuals/`, "one per thing a person does by hand outside a delivery" becomes one per action of more than one command, by hand outside a delivery or a proof `/apply` runs on another machine.
  2. "The seven documents", docs/05's paragraph, after the slots' list: a slot says what and the command, in a few lines, because `/apply` reads it every time; steps go in a manual, and what a command prints stays in its help. "The commands read these facts here" stays.
  3. "Manuals": the opening names both kinds, the second with the library's example, written for this chapter: the Proof of a screen slot names the command and points to `docs/manuals/prove-on-the-test-server.md` (pt `docs/manuals/provar-no-servidor-de-teste.md`), where `/apply` finds the steps to publish a preview there and run the end-to-end tests. "Stands alone for a person who has read nothing else" becomes "for whoever runs it". "The agent follows the slots of docs/05; a person follows the manual" becomes: the slot says what and the command, and the manual holds the steps for whoever runs them. The `publish-the-app.md` example, who writes manuals, the empty folder and `AGENTS.md` stay.
  4. "Where a new fact goes": question 6's answer gains "what and the command, in a few lines"; question 7 gains "or a proof `/apply` runs on another machine". Numbering kept.
  5. "What the team gains", after the 2026.10.13 sentences: the kit's changelog, entry 2026.10.16, paraphrased, no note, no number: in one project the steps of a proof `/apply` ran on another machine had nowhere to go but a slot, and every `/apply` read them before its first edit; now the slot holds what and the command, and the steps have a manual found by its name.
  6. Key points, still five: the first point's "docs/05 the process with the project's slots" gains "each what and the command"; the manuals point says one action of more than one command, by hand or a proof on another machine, for whoever runs it.
* **Chapter 12, both editions:**
  1. After `/brainstorm`'s list of six subjects, which the chapter attributes to the kit's file for the command (whose fifth subject does not say it), one clause of its own: each slot is written as what and the command, as chapter 10 says, citing docs/05, not the command's file.
  2. "What it writes": the folder is created by the delivery that adds the first manual, by hand or a proof on another machine, instead of "something a person does by hand".
  3. "Review before you commit": one bullet: every slot of docs/05 says what and the command, with no steps and no pasted output; the steps are in a manual. The existing manuals bullet stays.
  4. `/analyze`'s sentence on manuals for what a person already does by hand stays: it is what the kit's file for the command says.
* **Terms:** slot, manual, page, delivery, as docs/03 has them (both rows updated by `kit-2026-10-16`); docs/03 unchanged. Portuguese: "slot", "manual", "o que e o comando"; slot names in English with a gloss, as chapter 10 already writes `slot Environments (ambientes)`: `slot Proof of a screen (prova de uma tela)`.
* **Sources:** the kit's description of the documents and docs/05 §5 template (the slot rule and the Manuals slot), and the CHANGELOG entry 2026.10.16, named in plain words, no note (docs/04, the 2026.10.13 precedent in the same section).
* **Cases:** none. Ninjobs's paragraph unchanged.
* **Code examples:** none; the manual names and the slot's pointer are written for the chapter on the lending library and said so; Portuguese names in the Portuguese edition.

**Out of scope.**

* The 120-line slot and the 180KB read: the book describes the kit as it is today, with no numbers for the change (the author, in this conversation).
* Chapter 11's update report, which lists slots that narrate steps: `ch11-update-2026-10-16`.
* Chapter 15's bullet on manuals: it says what the kit's `/apply` file says, and the Manuals slot's "a delivery that changes one updates its manual" adds nothing it contradicts.
* A sample manual's full text: the parts are named, as `ch10-12-manuals` decided.
* This book's own docs/05 and manuals: `kit-2026-10-16` already shrank the slots; no proof here runs on another machine.

**Done when.**

* [x] Chapters 10 and 12 changed in both editions, same headings; each opens with its value; no filler and nothing useful cut.
* [x] No sentence in the book says a manual is only for what a person does by hand, that a manual is read only by a person, or that a slot holds steps; except the sentences that say what the kit's `/analyze` and `/apply` files say (chapter 12's `/analyze`, chapter 15's "Green is not done").
* [x] The changelog entry 2026.10.16 paraphrased and checked against the kit's CHANGELOG at `029cee6`; no number from it in the text.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Trunk, no branch: docs/05 §5 Git.
* The slot rule's wording, "what and the command, in a few lines: /apply reads it every time; steps go in a manual, and what a command prints stays in its help": docs/05 §5 and docs/03's `slot` row.
* The manual's two kinds and "whoever runs it": docs/05 §5's Manuals slot and docs/03's `manual` row.
* A single command needs no manual: "one file per action that takes more than one command" (docs/05 §5).
* `/analyze` and chapter 15 unchanged: the kit's files for `/analyze` and `/apply` at 2026.10.16 still name only what a person does by hand.
* Evidence, the changelog's reason with no number (asked; the author chose), as the book describes the kit today.
* The library's example, the proof on the test server (asked; the author chose).

**What happened.**

* Chapter 10, both editions: "One place per fact" names the two kinds of manual; docs/05's paragraph gains the slot rule and, as its consequence, that a slot holds no history (page in `work/done/`, the ADR); "Manuals" opens with an action of more than one command, of two kinds, the second with the library's Proof of a screen slot pointing to `docs/manuals/prove-on-the-test-server.md` (pt `provar-no-servidor-de-teste.md`), "whoever runs it", the slot-and-manual sentence, and one sentence that a single command needs no manual; questions 6 and 7 extended, numbering kept; the gain paraphrases entry 2026.10.16 with no number; key points still five, the first and the third changed.
* Chapter 12, both editions: one sentence after the six subjects, attributed to docs/05 with the link to chapter 10; the folder sentence names both kinds, and its link to chapter 10 moved to that new, earlier sentence so the chapter links chapter 10 once; one review bullet before the two "on an existing project" bullets; `/analyze`'s sentence unchanged.
* Changelog checked against focus-kit's CHANGELOG at `029cee6`, entry 2026.10.16: its third bullet (a manual also holds a proof `/apply` runs on another machine; the proof steps had nowhere to go but the slot) and its first (a slot says what and the command; every `/apply` read the documents before its first edit). None of its numbers is in the text.

**Divergences and decisions.**

* The edge "`make verify` stays in the Verify slot": the lending library's verify command is `npm run verify` (chapter 12), not `make verify`, so chapter 10 says "a single command, such as the one that verifies a delivery, needs no manual: it stays in its slot", naming no command.
* pt: "testes de ponta a ponta" tripped the prose rule `inflated` ("de ponta"); written "testes ponta a ponta", as chapter 15 already writes "execução ponta a ponta".
* The changelog's "not only what a person does by hand" is written "by hand or a proof `/apply` runs on another machine" everywhere, which also keeps clear of the `not-but` rule.
* Book-wide check of the second Done when: the remaining sentences that tie a manual to what a person does by hand are chapter 12's `/analyze` and chapter 15's two (kit files, kept by this page), and chapter 11's update report to 2026.10.13, which quotes that version's migration wording; it is the scope of `ch11-update-2026-10-16`, not changed here.
* No owning document changes: docs/03's `slot` and `manual` rows and docs/05 §5 already say this (`kit-2026-10-16`); no manual of this book changes.

**Proof.**

* `make verify` in the shared tree: red only on chapter 13's link to `work/done/kit-2026-10-16.md` (HTTP 404 until `main` is pushed), which is `ch13-short-lines`'s edit, blocked for that reason; not this delivery's.
* `make verify` in a throwaway worktree at `HEAD` with this delivery's staged diff applied whole (chapters, page, queue line): green, exit 0; the worktree removed.
* `make book` builds; PDFs for the author: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, chapters 10 and 12.
* Environments: local builds; GitHub Pages and the Release unchanged until the author pushes and tags.
* Staging: docs/06's line for this slug is adjacent to `ch13-short-lines`'s, in one hunk; only this line was staged, with a crafted patch.

```commit
docs(ch10-12-slots-manuals): teach a slot as what and the command

- Ch 10: a slot says what and the command; steps go in a manual
- Ch 10: a manual also holds a proof /apply runs on another machine
- Ch 10: the library's proof on the test server; changelog 2026.10.16
- Ch 12: /brainstorm writes slots that way; review bullet for slots
- Both editions

work/done/ch10-12-slots-manuals.md
```
