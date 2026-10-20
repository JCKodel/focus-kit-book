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

* [x] Chapters 7, 9 and 10 changed in both editions as the Contract says, same headings, chapter 12 untouched; each still opens with its value; no filler and nothing useful cut.
* [x] No sentence in the book lists the kinds of manual without running it from a fresh clone, says `/brainstorm`'s Manuals slot is "none yet" alone, or says `/analyze` writes manuals without the one of running it first (outside chapters 8 and 13, whose lines own them).
* [x] No numbers, no history of the kit's change, no run narrated; no em dash.
* [x] `make verify` green; `make book` built both editions: the batch's driver ran it after the last M23 build lane, at `31f510e` (exit 0), and `work/done/m23-review.md` records the build at `8a87b0c`, whose `book/` is the same and holds chapters 7, 9 and 10 as this delivery left them, with both PDF paths.
* [x] Page in `work/done/`, the commit suggested in a `commit` block; the line's `[x]` and the staging by paths and hunk were the batch driver's, from a temporary index at commit time.

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

**Decisions taken alone in /apply** (the batch's driver asked for recommended answers; correct them in the review).

* The phrase, picked by `ch13-apply-run-manual`'s /propose and passed by the batch's driver to this /apply so the book says it one way, here and in that delivery: "the manual of running it", or "the manual of running the product" where the product was not just named; pt "o manual de rodá-lo" / "o manual de rodar o produto", the kit's README.pt.md wording. The kind itself is "running the product from a fresh clone" (pt "rodar o produto a partir de um clone novo").
* The library's manual keeps the page's names: `docs/manuals/run-the-app-from-a-clone.md`, pt `docs/manuals/rodar-o-app-de-um-clone.md`, written by `skeleton`, pt `esqueleto`.
* Chapter 7 does not print "chapter 11's first line": docs/04's Chapter pointers allow no forward pointer outside the gain in chapters 0 to 7, so the text says what `skeleton` is, "the first delivery, which builds the empty app and server"; the Contract's words name the delivery for the page, not for the text.
* The reason is said where the manual is introduced too (docs/04, "Say it where the doubt is born"): chapter 7's Manuals paragraph gives it in one clause, and the gain sums it in one sentence.
* The two Behaviour edges (a database started before the server updates the manual; a new refusal in `lend-book` leaves it as it is) are carried by chapter 7's library example, the one place the Contract gives the example.
* In pt, the slot is "o slot Manuals (manuais)" at its first mention in each chapter, as chapter 7 names the other slots.

**Built.** Chapter 7: the folder's three kinds in "One place per fact"; "Manuals" with three kinds, the first owed from the start, the library's `skeleton` example, the who-writes sentence and `AGENTS.md`'s pointer; question 7; one gain sentence; the third key point (still five). Chapter 9: the fifth subject, "What it writes, and where it stops", `/analyze`'s write sentence, a review bullet, the `/analyze` key point. Chapter 10: new project step 6 and existing project step 3. Both editions; headings unchanged; chapters 11 and 12 untouched.

**Divergences.** Beyond the forward pointer above, one: Behaviour's second scenario expects chapter 9 to name `docs/manuals/run-the-app-from-a-clone.md` (pt `rodar-o-app-de-um-clone.md`); chapter 9 names the manual of running it and no file, which chapter 7 carries, as the Delivery review noted and left.

**Proof.** A search of both editions outside chapters 8 and 13 for "two kinds"/"dois tipos", "none yet"/"nenhum ainda", "writes the manuals"/"escreve os manuais" and "a manual ... for each"/"um manual ... para cada" finds only chapter 3's unrelated "two kinds of errors" and chapter 9's new fifth subject, which names the manual of running it before "the rest none yet". `make verify` green after the last edit, the page's move included; the batch's driver ran `make book` at `31f510e` (exit 0), and `work/done/m23-review.md` records the build at `8a87b0c`, the same `book/`, with both PDF paths.

**Delivery review.** A read-only agent on Opus, launched by this lane, read `git diff HEAD` of the six chapter files against this page, docs/04 and AGENTS.md, and searched both editions outside chapters 8 and 13 for stale sentences on manuals. No finding breaks the page or docs/04: no em dash, no forward pointer in chapter 7's body, five key points, headings unchanged, chapter 12 untouched, the editions agree. Its wording suggestions, all on text this delivery wrote, were applied: chapter 7 moves "from the start" before the slot so it does not read as "running it from the start" (both editions); chapter 10 step 6 says "the manual of running it", not "its manual"; pt chapter 9 says "a cargo da primeira entrega" for "owed by", and pt chapter 7 gains a comma before "para rodar o produto". It also noted that the library's file name is in chapter 7 and not in chapter 9; it is left there, since chapter 9 names the manual and chapter 7 carries the example.

```commit
docs(ch10-12-run-manual): name the manual of running it in ch 7, 9, 10

- ch 7: three kinds of manual, running it from a clone owed from start
- ch 7: library's skeleton writes run-the-app-from-a-clone.md
- ch 9: Manuals slot names it owed; /analyze writes it first; review
- ch 10: step 6 and existing step 3 show the manual of running it

work/done/ch10-12-run-manual.md
```
