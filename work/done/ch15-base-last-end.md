# ch15-base-last-end

Defined by /propose on 2026-11-14 and built before the author read it, on the author's word for this run ("Vamos rodá-la de ponta a ponta automaticamente, sem pausas para concluir o milestone."): every question /propose would ask is answered by its recommendation, and each such answer below says the agent chose it (docs/05 §4). The author corrects it in the review.

**Objective.** After chapter 15 the reader can name a milestone review's base as the end the page of the last review that ran names, the commit that review's reading started at and not its own commit, say why: a delivery committed while a review reads falls in the next range instead of in neither, and name the base after a cancelled review; and say what the page of a review whose slot says none still names.

**Behaviour.** What the reader can do or explain afterwards:

* Name a review's base: the end, `<review-head>`, named by the page of the last review that ran; the project's first commit for a first milestone; where no earlier review ran, a commit the page names and why.
* Say what the range from that end holds: what was committed while the last review read, that review's own commit, which is a page, the fixes of its findings and the next milestone's deliveries.
* Say where a delivery committed while a review reads falls: after that review's end and before its own commit, outside that review's range and inside the next one's.
* Say the error a base at the last review's own commit makes: such a delivery is in neither range, so no review copies its notes or reads its code; this book noted that gap on a delivery's page on 2026-11-14, before any delivery had fallen into it.
* Name the base after a cancelled review: the end named by the last review that ran, so with `m2-review` cancelled, `m3-review`'s range starts at `m1-review`'s end and milestone 2's deliveries are read with milestone 3's.
* Say what a review whose Milestone review slot says none still does: its page names the range, its end the commit `HEAD` was when the review started, and the person tests each clause.
* Read the chapter's sentences on `after all` and a cancelled line with no line held by `after` told as waiting.
* Find all of this in chapter 15 in both editions; in Portuguese with docs/03's terms (revisão de marco, base, fim, intervalo, cancelada, `<head-da-revisao>`).

**Contract.** Two chapter files. Line numbers are en and pt at `6a91138`, HEAD; chapter 15 is unchanged in the working tree. Each change quotes the passage it replaces so a drift is found. pt follows en sentence for sentence. The text is the agent's within these changes.

* **ch15** (`book/en/15-closing-a-milestone.md`, `book/pt/15-closing-a-milestone.md`)
  * C1, the base (en :23, "Its page names as the base the commit of the previous milestone's review, or, for a first milestone,"; pt :23, "A página dela cita como base o commit da revisão do marco anterior,"): the base is the end named by the page of the last review that ran, the commit its reading started at and not that review's own commit; the first commit for a first milestone; "where no earlier review exists" becomes "where no earlier review ran", since a cancelled review exists and did not run.
  * C2, the range and the gap (en :25-26, "The range from the previous review's commit holds" to "is outside the range from it."; pt :25-26): four sentences. (1) The range from that end holds what was committed while the last review read, that review's own commit, a page, the fixes of its findings and the next milestone's deliveries. (2) A free line of the next milestone does not come after the review (chapter 14), so a delivery can be committed while a review reads, after its end and before its own commit, outside that review's range and inside the next, which starts at that end. (3) The error, in the present and dated as a finding of this book, with no version named (docs/04 "The kit as it is"; ch14 :200 and :235 as models): a base at the last review's own commit would leave such a delivery in neither range, its notes copied and its code read by no review; on 2026-11-14 a delivery of this book noted that gap on its page, before any delivery had fallen into it. (4) The base after a cancelled review, written for this chapter: with `m2-review` cancelled, `m3-review` names as its base the end `m1-review`'s page names.
  * C3, a slot that says none (en :112, "A project whose Milestone review slot says none has no code reading, and the hand test still runs."; pt :115): the page still names the range, its end the commit `HEAD` was when the review started, because the notes it copies come from the pages that range delivered and the next review's base is that end.
  * C4, no second review (en :189, "the next milestone's review names this review's commit as its base, so on the lending library `m2-review`'s range starts at `m1-review`'s commit"; pt :193): the next review's base is this review's `<review-head>`; `m2-review`'s range starts at `m1-review`'s `<review-head>`.
  * C5, key point 2 (en :215, "its page names as the base the commit of the previous milestone's review, ... or, where no earlier review exists,"; pt :219): the base is the `<review-head>` of the last review that ran, never that review's own commit; "exists" becomes "ran".
  * C6, a line held by `after` told as waiting (en :3, "so a line the person cancelled never keeps it waiting"; en :18, "a line whose `after` names a cancelled one waits, and the review with it,"; pt :3 and :18): the review is never held back by a cancelled line, and a line whose `after` names a cancelled one stays held by it, and the review with it, until the person re-decides it. Decided by the agent: these are chapter 15's own sentences against M40's clause that no sentence tells a line held by `after` as waiting, and no other M40 line touches chapter 15.
* Terms: no new term of docs/03; its `milestone review` row already says the new base (`kit-2026-11-14`).
* Sources: docs/05 §8 and §4; no new number; the date 2026-11-14 is `ch15-review-grades`' note, `work/done/ch15-review-grades.md` `## For the review`, which the text does not cite (a note only where the reader gains something to open, docs/04).
* Cases: none.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: the Design slot says prototype, no reference, by choice (ADR-0019); no new kind of content.

**Out of scope.**

* Chapters 12 and 19, `/propose` reading pages on branches: `ch12-pages-on-branches`, another lane.
* docs/03, docs/05, ADR-0018: migrated by `kit-2026-11-14`.
* Chapters 8, 11, 13 and 23, which say "the milestone's base" with no definition of it: they read right with the new base.
* The 2026-10-19 milestone that followed a dropped review, the changelog's error for that clause: the queue line asks only for the base after a dropped review, and the rule needs no story to be taught.
* :163 and :181 ("waiting for `/propose`", "waits its turn"): a line's turn in the queue's order, not a line held by `after`.
* `make book`: the driver of this run builds once.

**Done when.**

* [x] C1 to C6 read as the Contract says in both editions; still three opening sentences and five key points.
* [x] Both editions written; the chapter opens with its value; no filler and nothing useful cut; no new number; no version named as a date; no em dash; no run narration.
* [x] `make verify` green after the last edit, with its time.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent: the dated error is one sentence in the present, "a base at the last review's own commit would leave", and "on 2026-11-14 a delivery of this book noted that gap", with no version and no "until then", since docs/04 forbids naming a version as a date and the gap never happened.
* Decided by the agent: the dropped review is taught with the chapter's word, cancelled, and a lending library example, `m2-review` cancelled.
* Decided by the agent: C3, the slot that says none, is in scope: it is chapter 15's sentence on the same range, M40's paragraph names it, and no other line teaches it.
* Decided by the agent: C6, chapter 15's two sentences that tell a line held by `after` as waiting, is in scope for the same reason.
* Decided by the agent: the reasons C3 gives (the notes come from the range, the next base is its end) follow from §8 and are not the kit's words.
* From the documents: the base, the range, the slot that says none (docs/05 §8), `after` never waiting (docs/05 §4), the kit as it is today (docs/04), three opening sentences and five key points (docs/04 §Chapter shape).

## Outcome

Built by /apply on 2026-11-14, before the author read the page, on the author's word for this run quoted above. The driver of this run stages and commits; this session staged nothing.

* C1 to C6 in both editions, as the Contract says; every passage was found by its quoted sentence at `6a91138`. Still three opening sentences and five key points.
* Delivery review, one read-only Opus agent, as docs/05 §5 says: no blocking candidate; eight wording candidates fixed in this delivery: "its page" in C3 made "the review's page" (pt "a página da revisão", where "dela" had no feminine noun); "the range from that end" made "from that base ... up to the review's own end"; "the last review that ran is also the base" made "the end of the last review that ran"; "its reading" in C1 and "its end ... its own commit" in C2 made "that review's"; "which is a page" made "which adds its page"; pt "antes de alguma entrega cair nela" made "antes que alguma entrega tivesse caído nela"; pt C6 "nunca a segura" made "nunca a prende", the pair of "fica presa a ela". A ninth, that a review whose slot says none has no reading for `<review-head>` to start at, is fixed in C3 by naming its end `<review-head>`, the commit `HEAD` was when the review started.
* "Before any delivery had fallen into it" rests on the kit's changelog for 2026.11.14 ("It has not happened there"), which the chapter does not cite (docs/04).
* `make verify` green after the last edit, 13 seconds (41 seconds on the first run, the other lane's run beside it).
* Proof: verify green; `make book` and the PDF paths are the driver's, who builds once for this run.

```commit
docs(ch15-base-last-end): the base is the last review's recorded end

- base: the end the last review's page names, not its commit
- a delivery committed while a review reads falls in the next range
- the base after a cancelled review; a slot that says none
- no line held by after told as waiting
- work/done/ch15-base-last-end.md
```
