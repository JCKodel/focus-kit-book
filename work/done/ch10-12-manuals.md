# ch10-12-manuals

**Objective.** After chapters 10 and 12 a reader knows that what a person does by hand outside a delivery (publish, roll back, rotate a secret, set up a service) has a manual in `docs/manuals/`, one file each, named after what it does and readable by someone who has read nothing else; that the docs/05 slot naming such a command points to its manual instead of holding the steps; and that `/analyze` writes the manuals for what the repository already runs by hand, `/apply` writes or updates one when a delivery adds or changes it, and `/brainstorm` writes none, as focus-kit 2026.10.13 says.

**Behaviour.**

* A reader who must publish the library's app for the first time opens `docs/manuals/publish-the-app.md` by its name and finds, in order: what it does and when, what must be in place, the commands, how to tell it worked, how to undo it, and what breaks if a step is skipped.
* A reader asked "where do the steps to publish go?" answers from chapter 10's "Where a new fact goes": a manual in `docs/manuals/`; the Environments slot of docs/05 keeps the command and points to the manual.
* Failure: a reader who finds the publish steps written as a sub-item of the Environments slot knows from chapter 10 that a person looking for how to publish does not look there, and asks the agent to move them into a manual, the slot keeping the command and the pointer.
* Failure: a reader who finds `AGENTS.md` holding the steps knows it only points, at `docs/manuals/`, in its "Read before acting".
* A reader running `/analyze` on a repository with a Makefile target `deploy`, a deploy script, or setup steps in its README expects one manual for each thing a person does by hand there, and checks each in the review of chapter 12: a person who read nothing else can follow it, and each command it gives exists in the repository.
* Edge: a reader whose `/brainstorm` ends with no `docs/manuals/` knows that is right: the folder is created with the first manual, and there is no empty folder.
* Edge: a reader whose delivery changes the publish command expects `/apply` to update `publish-the-app.md` in the same delivery (chapter 15's "Green is not done"); a delivery that adds a new thing done by hand, such as restoring a backup, adds its manual.
* A reader asked "is a manual for the agent?" answers: no, for a person; the agent follows the slots, and a person follows the manual.

**Contract.**

* **Chapter 10, both editions, file name and title kept; same headings in both.**
  1. Opening: "the seven project documents, the ADRs and `AGENTS.md`" gains the manuals.
  2. "One place per fact": the list of places gains `docs/manuals/`, a folder of manuals, one per thing a person does by hand outside a delivery.
  3. A new section "Manuals" between "ADRs" and "`AGENTS.md`": what a manual is, the six things it holds (kit's docs/05 §5 Manuals slot), named after what it does in the documentation language, the slot points to it instead of holding the steps, the folder created with the first manual; the library's example: the Environments slot names the publish command and points to `docs/manuals/publish-the-app.md`, written for the chapter (pt: `docs/manuals/publicar-o-app.md`); who writes them: `/analyze` for what the repository already does by hand, `/apply` when a delivery adds or changes one (chapter 15), `/brainstorm` none; `AGENTS.md` points to the folder.
  4. "Where a new fact goes": a new question after the slot question, "Is it the steps a person follows by hand outside a delivery: publish, roll back, rotate a secret, set up a service? A manual in `docs/manuals/`, the slot keeping the command and pointing to it"; "Is it work to do?" becomes question 8. The slot question's text stays.
  5. "What the team gains": the kit's changelog, entry 2026.10.13, paraphrased, no note (docs/04): a user went to republish a project's site and found no instructions; the steps existed, as a sub-item of the Environments slot written for the agent, where a person looking for how to publish does not look. The Ninjobs paragraph kept.
  6. Key points: the first point's list gains `docs/manuals/`; a new point on manuals, who writes them and the slot pointing to them.
* **Chapter 12, both editions:**
  1. `/analyze`: a sentence on what it writes, the same documents as `/brainstorm` plus a manual for each thing a person already does by hand there (a Makefile target, a deploy script, steps in a README), as the kit's file for the command says.
  2. `/brainstorm`'s "What it writes" says it writes no manual: the folder is created with the first one, by the delivery that adds something done by hand.
  3. "Review before you commit": a bullet, on an existing project, every manual can be followed by a person who read nothing else, and every command it gives exists.
  4. Key points: the `/analyze` point mentions the manuals.
* **Chapter 15, both editions:** one bullet in "Green is not done": when the delivery adds or changes something a person does by hand, it writes or updates its manual. "Done is that whole list" stays, since its "the documents updated" covers it. Nothing else in chapter 15.
* **Terms:** page, slot, delivery, as docs/03 has them. manual, as docs/03 already has it (added by `kit-2026-10-13`); docs/03 unchanged.
* **Sources:** the kit's `SETUP.md`, the description of the documents and docs/05 §5's Manuals slot, the file of `/analyze` and of `/apply`, and the CHANGELOG entry 2026.10.13, named in plain words, no note (docs/04).
* **Cases:** Ninjobs's paragraph unchanged; no new private passage; no Case A or B.
* **Code examples:** none; the manual's name and the slot's pointer are written for the chapter on the lending library, said so; Portuguese names in the Portuguese edition.
* **Queue:** the line gains `· after ch15-apply-ends` (author's choice), since that delivery was building chapter 15's "Green is not done" while this page was written; it is `[x]` now, so the line is free.

**Out of scope.**

* Chapter 10's "docs/04 ... the format of a commit message": `ch11-update-migrations` (decided in `ch15-apply-ends`).
* Updating reports the Manuals slot as a migration: `ch11-update-migrations`.
* This book's own manuals as evidence: the changelog entry is the evidence (ADR-0017), and the repository's manuals are its own business.
* A manual's full text in the chapter: the six parts named, not a sample manual; the chapter teaches where it goes and who writes it.

**Done when.**

* [x] Chapters 10 and 12 changed in both editions, chapter 15 by one bullet in both, same headings; each opens with its value; no filler and nothing useful cut.
* [x] No sentence in the book lists the project's places without `docs/manuals/`, or says `/brainstorm` writes a manual.
* [x] The changelog entry and the kit's files named in plain words, no note to focus-kit's repository; every number and quote sourced.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* `/brainstorm` writes no manual: the kit's description of the documents ("Created with the first one; there is no empty folder").
* The question order in "Where a new fact goes" puts manuals right after slots, since the slot points to the manual (kit's docs/05 §5).
* Chapter 15 gets one bullet, after `ch15-apply-ends` (asked; author chose).
* The library's example is publishing the app (asked; author chose).

**What happened.**

* Chapter 10, both editions: the opening names the manuals; "One place per fact" lists `docs/manuals/`; a new section "Manuals" / "Manuais" between "ADRs" and "AGENTS.md", with the six parts, the slot pointing to the manual, the library's `docs/manuals/publish-the-app.md` (pt: `docs/manuals/publicar-o-app.md`) said to be written for the chapter, who writes manuals and the folder created with the first one; "Where a new fact goes" gains question 7, work to do becomes 8; "What the team gains" paraphrases the kit's changelog entry 2026.10.13 after the Ninjobs paragraph, kept.
* Chapter 12, both editions: `/brainstorm` writes no manual; `/analyze` writes the same documents plus a manual per thing done by hand (Makefile target, deploy script, README steps); a review bullet for manuals on an existing project; the `/analyze` key point mentions the manuals.
* Chapter 15, both editions: one bullet in "Green is not done"; "Done is that whole list" unchanged.

**Divergences.**

* Chapter 10's key points: docs/04 caps them at five, and the chapter had five. To add the manuals point as its own bullet, the first two (the places, and what each numbered document holds) became one bullet; nothing in them was cut.

**Proof.** `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review. A search of both editions found no other sentence listing the project's places, and none saying `/brainstorm` writes a manual.

**Decisions.**

* The kit's changelog, its description of the documents, docs/05 §5's Manuals slot and the file of `/analyze` are named in plain words, with no note (docs/04).
* docs/03 unchanged: "manual" was already there. No document owns a behaviour this delivery changed; no manual of this repository added or changed.

```commit
docs(ch10-12-manuals): teach docs/manuals/ and who writes each manual

- ch 10: a Manuals section, question 7 of where a fact goes, the gain
- ch 12: /analyze writes manuals, /brainstorm none, a review bullet
- ch 15: /apply writes or updates the manual of what it changes
- both editions

work/done/ch10-12-manuals.md
```
