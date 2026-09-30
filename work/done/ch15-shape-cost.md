# ch15-shape-cost

**Objective.** A reader of chapter 15 can apply one rule for when a piece is written, the one the section shows: a piece is written when its job gives more than it costs, alone or through one shape a delivery chose for every hook, as the clinic keeps `healthEvents.ts`.

**Behaviour.**

* The reader can say, from key point 2 alone, why the clinic keeps `healthEvents.ts` although it costs more than it gives: the gain counted is the one shape across hooks that `orchestrator-tests` chose, not the piece alone.
* The reader can say that a shape counts as a gain only when a delivery chose it, as `orchestrator-tests` chose "*Every event moves*", and not because a piece of the same kind exists elsewhere.
* Key point 2 and the section's verdict ("Alone, `healthEvents.ts` costs more than it gives." and the sentence after it) no longer give two rules: the key point states the one the section applies.
* Both editions say the same.
* Finding F12 of the M4.1 review is settled (`work/done/m4.1-review-run/findings.md:67`, confirmed narrowed in `work/done/m4.1-review-run/decisions.md:65`).

**Contract.**

Sentences are found by their quoted text. The other ch15-* lines of M4.2 (`ch15-brief-printed`, `ch15-uncaught-pieces`, `ch15-view-rule`) may be in flight on chapter 15 and move its lines. The line numbers below are from commit `cad46ef`.

* `book/en/15-four-pieces.md`, section "When the pieces pay their way" (en:439, pt:440): unchanged. It already says what the key point will say: "Alone, `healthEvents.ts` costs more than it gives." and "The clinic keeps it because [...] chose "*Every event moves*", so every hook has one shape: that shape is what the clinic pays for, not the piece." (en:454-455, pt:455-456). The closing sentence "a piece is written when a delivery needs its job, and not before" (en:460, pt:461) stays; it agrees with the new key point.
* Key point 2 (en:465 "A piece is written when it has a job and that job gives more than it costs; the "Forbids" column keeps it to that job."; pt:466 "Uma peça é escrita quando tem um trabalho e esse trabalho dá mais do que custa; a coluna "Proíbe" a mantém nesse trabalho.") becomes, as a proposal for `/apply` to tighten:
  * English: "A piece is written when its job gives more than it costs, alone or through one shape a delivery chose for every hook, as the clinic keeps `healthEvents.ts`; the "Forbids" column keeps it to that job."
  * Portuguese: "Uma peça é escrita quando o trabalho dela dá mais do que custa, sozinho ou por uma só forma que uma entrega escolheu para todo hook, como a clínica mantém `healthEvents.ts`; a coluna "Proíbe" a mantém nesse trabalho."
  * "has a job" may be dropped from the English: "its job" still requires one, and the section's first sentence, "A piece can exist only when it has a job.", keeps the necessary condition.
* Terms of docs/03: none new, none changed. "shape" is used as the section already uses it, not as a term.
* Sources: none new; the section already links `healthEvents.ts` and `orchestrator-tests`.
* Cases: none. Ninjobs is not used. Exercises: unchanged.

**Out of scope.**

* The section's paragraphs: they already say the shape is what the clinic pays for; only the key point missed it.
* The clinic's code and `healthEvents.ts`: the book changes, not the guided project.
* Key points 1, 3, 4 and 5: no finding on them.
* The printed brief, the uncaught pieces and the view's rule: `ch15-brief-printed`, `ch15-uncaught-pieces`, `ch15-view-rule`.
* When a uniform shape stops paying (how many hooks, which ones): the section weighs one case and its contrast, as `ch15-piece-cost` decided.

**Done when.**

* [x] Both editions changed with the same meaning. Chapter 15 still opens with its value, with no filler and nothing useful cut.
* [x] Key point 2 in both editions names the job's weighing and the shape a delivery chose; the section is unchanged.
* [x] No "and that job gives more than it costs" or "e esse trabalho dá mais do que custa" left in `book/`.
* [x] No em dash in the changed lines.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author. Left unticked on purpose: in this batch the driver runs `make book` once at the end of the loop.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Revalidated against `main` at `60fc7d7`: `ch15-uncaught-pieces`, `ch15-brief-printed` and `ch15-view-rule` had moved the section to en:469 and pt:470, the verdict to en:484-485 and pt:485-486, the closing sentence to en:490 and pt:491, and key point 2 to en:495 and pt:496; the text was as the page quotes it, so the page held.
* Key point 2 now reads, in English, "A piece is written when its job gives more than it costs, alone or through one shape a delivery chose for every hook, as the clinic keeps `healthEvents.ts`; the "Forbids" column keeps it to that job.", and in Portuguese as the page proposed.
* Taken alone, since the batch ran without conversation: the page's proposal was kept word for word rather than tightened; each clause carries one behaviour item ("a delivery chose" for the second, "as the clinic keeps `healthEvents.ts`" for the first), and "has a job" was dropped as the page allowed.
* The section was not touched.
* F12 is settled by this delivery; `findings.md` is a run record and is not edited, as done for F9 to F11.
* No document changed: no new term, rule or decision.
