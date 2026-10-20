# ch10-12-run-manual

**Objective.** After chapters 7, 9 and 10 a reader knows that running the product from a fresh clone is a manual always owed: the Manuals slot of docs/05 names it from `/brainstorm` on, the first delivery after which a person can run the product writes it, from installing what it needs to the first screen or call, every delivery that changes a step updates it, and `/analyze` writes it first on a repository with code; as focus-kit 2026.10.19.2 says.

**Behaviour.**

* A reader asked "which manual does every project owe?" answers from chapter 7's "Manuals": the manual of running the product from a fresh clone, from installing what it needs to the first screen or call; the others exist only when the project has something done by hand or a proof on another machine.
* A reader who runs `/brainstorm` on the empty lending library repository expects docs/05's Manuals slot to name `docs/manuals/run-the-app-from-a-clone.md` (pt `docs/manuals/rodar-o-app-de-um-clone.md`) as owed by the first delivery after which a person can run the app, the rest "none yet", and no `docs/manuals/` folder yet (chapter 9).
* A reader who follows the library's first milestone knows that `skeleton` (pt `esqueleto`, chapter 11's first line) is the first delivery after which a person can run the app, so its page's Done when includes writing that manual; a later delivery that adds a step, such as a database started before the server, updates it in the same delivery.
* Failure: a milestone closes with the app's install, its environment and its serve command added by three deliveries and no manual of running it. The reader knows from chapter 7 that the Manuals slot named it owed from the start, that `/apply`'s next steps for using a delivery live only in its conversation, and asks for the manual as a line in docs/06.
* Failure: a reader reviewing `/brainstorm`'s docs/05 finds the Manuals slot saying only "none yet". From chapter 9's "Review before you commit" they ask the agent, in the same session, to name the manual of running it as owed.
* A reader running `/analyze` on a repository whose README gives install and run steps expects the manual of running it from a fresh clone written first, then one for each thing a person already does by hand (a Makefile target, a deploy script), and checks in the review that a person who read nothing else can follow it and every command it gives exists (chapters 9 and 10).
* Edge: a product nobody can run yet, a new project before its skeleton, has no manual and no folder; the slot says the manual is owed and by which delivery, as "created by the first delivery" says of what does not exist yet (chapter 9, "A default with every question").
* Edge: a delivery that changes no step of running the product, such as a new refusal in `lend-book`, leaves the manual untouched.
* A reader asked "where do I look to run this project from a clone?" answers: `docs/manuals/`, which `AGENTS.md` points to for running it and for what a person does by hand.

**Contract.**

* **Chapter 7, `book/en/07-the-documents.md` and `book/pt/07-the-documents.md`; headings unchanged.**
  1. "One place per fact": the folder of manuals is "one per action of more than one command: running the product from a fresh clone, one done by hand outside a delivery, or a proof `/apply` runs on another machine".
  2. "Manuals": "of two kinds" becomes three; the new first kind, running the product from a fresh clone, from installing what it needs to the first screen or call, always owed: the Manuals slot names it from the start, the first delivery after which a person can run the product writes it, and every delivery that changes a step updates it. The library's example, written for the chapter: `skeleton`, chapter 11's first line, writes `docs/manuals/run-the-app-from-a-clone.md` (pt `docs/manuals/rodar-o-app-de-um-clone.md`, and `esqueleto`). The "who writes" sentence: `/analyze` writes the manual of running it first, then those of what the repository already does by hand; `/apply` writes or updates one when a delivery adds or changes it; `/brainstorm` writes none and names the one of running it as owed in the slot. `AGENTS.md` points to the folder for running it and for what is done by hand. The six parts, the slot pointing to the manual, the single command needing none, the proof and publish examples stay.
  3. "Where a new fact goes", question 7: "Is it how to run the product from a fresh clone, the steps a person follows by hand outside a delivery (...), or those of a proof `/apply` runs on another machine?"; the answer unchanged.
  4. "What the team gains": one sentence of the reason, as the kit gives it and with no history: running a product is assembled over several deliveries, each adding a step, and `/apply`'s next steps live only in its conversation, so the manual owed from the start is what lets a person run what the milestone built without that conversation. No date, no count, no changelog story (decided alone, below).
  5. Key points: the manuals point (the third) names running it from a fresh clone as the manual every project owes, written by the first delivery after which a person can run it; still five bullets (docs/04).
* **Chapter 9, `book/en/09-starting-a-project.md` and `book/pt/09-starting-a-project.md`; headings unchanged.**
  1. `/brainstorm`'s fifth subject: "the manuals (the one of running the product, owed by the first delivery after which a person can run it; the rest none yet, on a new project)".
  2. "What it writes, and where it stops": it still writes no manual and `docs/manuals/` is created with the first one; the slot names the manual of running it as owed by the first delivery after which a person can run the product, from installing what it needs to the first screen or call; the others come with the delivery that adds something done by hand or a proof on another machine.
  3. `/analyze`'s "What it asks" paragraph: "plus, in `docs/manuals/`, the manual of running the product from a fresh clone first, then one for each thing a person already does by hand there, such as a Makefile target, a deploy script or setup steps in a README".
  4. "Review before you commit": a bullet, the Manuals slot names the manual of running it, owed on a new project, written on an existing one; the existing-project manual bullet unchanged.
  5. Key points: the `/analyze` point says it writes the manual of running it first, then one for each thing done by hand.
* **Chapter 10, `book/en/10-quick-guide.md` and `book/pt/10-quick-guide.md`; headings unchanged.**
  1. An existing project, step 3's "You see": "the manual of running the product from a fresh clone and one for each thing a person already does by hand, in `docs/manuals/`".
  2. A new project, step 6's "You see" gains: when the delivery is the first after which a person can run the product, such as the skeleton, its manual of running it in `docs/manuals/`.
* **Chapter 12 (`12-propose.md`):** unchanged; it says nothing on manuals.
* **Terms:** manual, slot, delivery, milestone, as docs/03 has them; docs/03's `manual` already names running the book from a fresh clone, and the chapters use "the manual of running it" in its words. docs/03 unchanged.
* **Sources:** the kit's `SETUP.md` at 2026.10.19.2: docs/05 §5's Manuals slot in the description of the documents, `/brainstorm`'s process slots item, `/analyze`'s Write paragraph, the AGENTS.md template's manuals line; named in plain words, no note (docs/04).
* **Cases:** none; Ninjobs's paragraphs unchanged; no Case A or B.
* **Code examples:** none; the manual's name, `skeleton`'s role and the slot's wording are written for the chapter on the lending library, said so, with Portuguese names in the Portuguese edition.

**Out of scope.**

* Chapter 13's `/apply` next steps and its "writes or updates its manual" bullet: `ch13-apply-run-manual`.
* Chapter 8's update example and report: `ch08-update-2026-10-19-2`.
* README's "Build locally": `readme-run-manual`.
* Chapter 11's `skeleton` line and its sentence on what it creates: not stale, and chapter 7 carries the example.
* This book's own `build-the-book-from-a-clone.md` as an example: the repository's manuals are its own business, and the library is the book's example.
* A sample manual of running it: the six parts are already named; the chapter teaches who owes it and when.
* The changelog's story of the project that could not be run: the book describes the kit as it is today.

**Done when.**

* [ ] Chapters 7, 9 and 10 changed in both editions as the Contract says, same headings, chapter 12 untouched; each still opens with its value; no filler and nothing useful cut.
* [ ] No sentence in the book lists the kinds of manual without running it from a fresh clone, says `/brainstorm`'s Manuals slot is "none yet" alone, or says `/analyze` writes manuals without the one of running it first (outside chapters 8 and 13, whose lines own them).
* [ ] No numbers, no history of the kit's change, no run narrated; no em dash.
* [ ] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The manual is owed by the first delivery after which a person can run the product, from install to the first screen or call, and `/brainstorm` names it in the slot instead of "none yet": the kit's `SETUP.md` 2026.10.19.2, docs/05 §5 template and `/brainstorm`'s process slots item.
* `/analyze` writes it first: the kit's `/analyze` Write paragraph, "running it first".
* `/brainstorm` still writes no manual and the folder is created with the first one: the kit's description of docs/manuals/, unchanged.
* docs/03 needs no new term: its `manual` row already names running from a fresh clone (`kit-2026-10-19-2`).

**Decisions taken alone.**

* "Chapters 10 and 12" read as the numbers before the renumbering of 2026-10-16: the documents chapter, now `07-the-documents.md`, and the starting chapter, now `09-starting-a-project.md`, the files the earlier `ch10-12-*` pages changed (the commit of `work/done/ch10-12-all-slots.md` touched `10-the-documents.md` and `12-starting-a-project.md`). Today's chapter 10, the quick guide, is widened in for the sentences that go stale; today's chapter 12, `/propose`, says nothing on manuals and is untouched. The queue line's wording should say "chapters 7, 9 and 10"; the slug stays.
* The library's manual is `docs/manuals/run-the-app-from-a-clone.md` (pt `rodar-o-app-de-um-clone.md`), written by `skeleton`.
* The gain gives the kit's reason without the changelog's dated story, as the book describes the kit as it is today.
* Chapter 10's step 6 gains the manual for the first runnable delivery; step 7 and the next steps are left to `ch13-apply-run-manual`'s chapter.
* Chapter 11 is not changed.
* Chapter 9 gains a review bullet for the slot, since the kit's update checks a Manuals slot naming the manual of running it, owed or written.
