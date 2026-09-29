# ch4-rule-failures

**Objective.** A reader of chapter 4 can say which failure each rule of focus-kit answers, as the chapter's opening promises, because every rule that names none today gains one clause that names it.

**Behaviour.**

* Every rule in §"Where it went" can be paired with a failure the chapter names; today "One page per delivery", "The documents hold the facts", "The governor" and the rule that came later already are, and they do not change.
* "Deciding and doing in separate sessions" gains a clause: the session that builds starts clean, with the written target and without the conversation that decided it, because a context that grows loses accuracy; it points to chapter 2, where context rot is explained. (Ninjobs' pivot review asked for "clean context, written target, without the conversation along", paraphrased.)
* "A queue" gains a clause: the outline, one of the six places, held each delivery's plan and its reasoning together, so reading the list meant reading everything; the queue keeps one line per delivery and the page keeps the reasoning.
* "The agent never commits" gains a clause: none of the 29 checks ever caught an error in the product, so the check that looks at the product is the person's review of each commit.
* No new number and no new note: the existing `[^ninjobs]` note already names ADR-0022, whose reviews and plan these clauses paraphrase; if `/apply` finds that a clause needs a source the note does not cover, it adds one sentence to that note, naming the ADR's reviews, not their files.
* Each rule stays a single bullet; the chapter still tells one story, with clauses, not new paragraphs.
* Both editions say the same.
* Finding F3 of the M3 review is settled.

**Contract.**

* Files: `book/en/04-birth-of-focus-kit.md` and `book/pt/04-birth-of-focus-kit.md`, lines 26, 28 and 29 today.
* Line 29 is also changed by `pt-stage-term` (the stage wording) and lines 9 and 37 by `ch4-adr-docs05`: whichever is applied later works on the tree the others leave, and keeps their changes.
* Untouched: the opening (lines 3 and 4), §"How it was", §"What went wrong", §"A lesson beyond the process" and the Key points.
* Terms of docs/03: fresh session, queue, page, delivery, governor (named in words). No new term.
* Sources: the `[^ninjobs]` note, unchanged unless the Behaviour line on sources applies. The pointer to chapter 2 is a relative link, `02-how-agents-see.md`.
* Cases: Ninjobs, through its process artifacts only: no file name, host or path from its pivot documents. Exercises: none; chapter 4 has none.

**Out of scope.**

* ADRs and docs/05 said in a few words: `ch4-adr-docs05`, its own delivery.
* The Portuguese term for stage: `pt-stage-term`, its own delivery.
* The size of the outline in words or tokens: the only count is a reviewer model's estimate, and today's Ninjobs queue is not smaller; the failure is where the reasoning lived, not size.
* A new failure in §"What went wrong": the outline is already one of its six places.

**Done when.**

* [x] Both editions changed, same meaning; each of the three bullets names its failure; nothing listed as untouched changed.
* [x] No number without a source; no private name, host or path (`make verify` disclosure scan green).
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* "Deciding and doing in separate sessions" ends with ": a context that grows loses accuracy ([chapter 2](02-how-agents-see.md)), so the build starts clean, from the written target, without the conversation that decided it." The Portuguese says the same with "um contexto que cresce perde precisão", the words chapter 2 uses.
* "A queue" gains: "The outline held each delivery's plan and its reasoning together, so reading the list meant reading everything; the queue keeps one line per delivery, and the page keeps the reasoning." The Portuguese keeps "roteiro", the word §"What went wrong" already uses for the outline.
* "The agent never commits" gains: "None of the 29 checks had ever caught an error in the product, so the check that looks at the product is the person's review of each commit." The 29 and the claim are the ones line 18 already sources to `[^ninjobs]`; ADR-0022 itself says every delivery goes through human review.
* The Behaviour line on sources applied: the ADR text holds the causes and the commit rule, but the outline that held each plan's reasoning and "clean context, written target, without the conversation along" are in the independent reviews the ADR cites, not in the ADR. The `[^ninjobs]` note gained one sentence naming those reviews, not their files, in both editions.
* The tree was the one the M3.1 deliveries before this left; `pt-stage-term` and `ch4-adr-docs05` are not applied yet, so they work on this tree and keep these changes.
* Nothing dropped. No document changed: docs/03 already holds every term used. Finding F3 of the M3 review is settled.
* Proof: `make verify` green; `make book` builds both editions, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
