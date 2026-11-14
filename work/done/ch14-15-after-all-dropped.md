# ch14-15-after-all-dropped

Decided before the author read it: the author's word for this run, relayed by the driver session on 2026-11-13, is "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão", so every question the documents leave open is answered by the agent's recommendation, marked "decided by the agent, the author corrects it in the review" (docs/05 §4, a command that says to decide alone). The page is built before the author reads it.

**Objective.** After chapters 14 and 15 the reader, developer or not, knows that a milestone review's `· after all` leaves out the lines the person cancelled, so a review never waits on a delivery the person cancelled, which it could neither drop nor rewrite to clear, while a line whose own `after` names a cancelled one is still the person's to re-decide, and the review waits with it until the person does.

**Behaviour.** What the reader can do or explain afterwards:

* Say the rule: `· after all` is every line above the review in its milestone but the cancelled ones, the `[x]` lines ending `· dropped:`; the review's `/propose` starts when every one of those is defined and its `/apply` when every one is integrated.
* Say why, as the error the rule prevents, in the present: a line whose `after` names a cancelled one waits for the person to re-decide it, to drop it too or rewrite it on what exists; a review that named the cancelled line would wait the same way, and a review is neither dropped nor rewritten on something else, so nothing the person could write would clear it; on 2026-10-26, in one project, a Milestone 1 review waited on a line the person had dropped, the queue script answered `after <slug>, dropped: re-decide`, and the review's `after all` was replaced by a list of the other 27 slugs.
* Edge, the review and the cancelled line: asked "`print-card` is `[x] · dropped: no printer driver` and every other line of milestone 1 is integrated; may `/apply m1-review` start?", answer yes: `after all` leaves `print-card` out.
* Edge, a line built on the cancelled one: asked the same with `reprint-card ... · after print-card` still `[ ]` in the milestone, answer no: `reprint-card` is not cancelled, so `after all` counts it, and it waits for the person to re-decide it (the queue tree prints `waits: after print-card, dropped: re-decide` beside it); once the person drops it too, the review starts, and once the person rewrites it on what exists, the review waits for it like any other line.
* Failure: asked "my review waits on a cancelled line; should I replace `after all` with the list of the other slugs?", answer no: `after all` already leaves the cancelled line out; a review that still waits is waiting on a line that names the cancelled one, which is the person's to re-decide, and re-deciding that line is what frees the review.
* Find in chapter 14 the rule, the error and the contrast with a line whose `after` names a cancelled one; in chapter 15 that the review line is `· after all`, when its two commands start, and that a cancelled line never holds it.
* In the Portuguese edition, the same, with docs/03's Portuguese terms: "revisão de marco", "linha da fila", "dependência", "cancelada" for a dropped line, as chapter 14 already writes it, and "redecidir".

**Contract.** Four chapter files; line numbers en at HEAD `2673874`, quoted beside each so a drift is found; pt follows en sentence for sentence. The text is the agent's within these changes. docs/03 does not change (Decisions).

* **ch14** (`book/en/14-queue-states.md`, `book/pt/14-queue-states.md`)
  * Already there, unchanged: :92 "A milestone's review line is written `· after all`: every line above it in its milestone but the cancelled ones" (pt :93), and key point 2 :268 "the review line's `· after all` names every line above it in its milestone but the cancelled ones, and a line whose `after` names a cancelled one is the person's to re-decide" (pt :270). Still five key points.
  * C1, opening (:5, "And you can resume a line whose session ended, and record a delivery the person cancels so that it never reads as built"; pt :5): one clause, nor holds the milestone's review. Still three sentences.
  * C2, owner of the reason, a new paragraph in `## A session that ended, a delivery cancelled` after "So a line whose `after` names a cancelled delivery is the person's to re-decide: drop it too, as `reprint-card` would be, or rewrite it on what does exist." (:220; pt :222) and before `## The queue as a kanban board`: the problem, chained from :220: a review that named every line above it would name the cancelled one and so wait, as `reprint-card` does, for the person to re-decide it, and a review can be neither dropped nor rewritten on what exists, so nothing the person could write would clear it; the error of 2026-10-26, told "in one project" as :71 and :80 tell theirs, saying nothing of whether it is either of their projects: a Milestone 1 review waited on a line the person had dropped, the queue script answered `after <slug>, dropped: re-decide`, and the review's `after all` was replaced by a list of the other 27 slugs; the rule, `after all` names no cancelled line and leaves it out; the contrast, set on the two lines of :213-214 supposed above milestone 1's `m1-review`, said in the text to be written for the chapter as the two lines are: `print-card` is left out, `reprint-card` is not cancelled, so `after all` counts it, the queue tree prints it with `waits: after print-card, dropped: re-decide` (the form of `queue.sh` :145 inside its `waits: ` at :155; pt keeps the output in English, with `imprimir-cartao`, as commands and their output stay, docs/04), and the review waits with it until the person re-decides it. Told in the present, never as what the script used to do, and naming no changelog (docs/04 :30).
  * C3, the team gain (:260, "and the kit writes such a closure as `[x]` with `· dropped:`"; pt :262): one clause, no number: and a line closed that way holds no review.
* **ch15** (`book/en/15-closing-a-milestone.md`, `book/pt/15-closing-a-milestone.md`)
  * C4, opening (:3, "plan its review as the milestone's last line"; pt :3, "planejar a sua revisão como a última linha do marco"): one clause, written `· after all`, so a line the person cancelled never holds it. Still three sentences.
  * C5, `## The review is a delivery`, one sentence after "A milestone is planned with its review as its last line, `<milestone>-review`, a delivery like the others: `/propose` writes its page, and `/apply` runs it." (:17; pt :17): the line ends `· after all`, every line above it in its milestone but the cancelled ones, so `/propose` writes its page when every one of those is defined and `/apply` runs it when every one is integrated; a line the person cancelled never holds it, and a line whose `after` names a cancelled one waits for the person to re-decide it, and the review with it. No chapter pointer: ch15 already points back to chapter 14 at :25 and :87, and the sentence stands alone (docs/04, Chapter pointers).
  * C6, key point 2 (:166, "A milestone is planned with its review as its last line, `<milestone>-review`, run with `/propose` and `/apply`"; pt :169): a clause, written `· after all`, which leaves out the cancelled lines. Still five key points.

Terms of docs/03: milestone review, dependency, queue line, mark, queue tree; none new. Sources: the installed `.agents/skills/propose/scripts/queue.sh` (:10-11, :128, the dropped lines left out of `all`, and :145, `after <slug>, dropped: re-decide`); the kit's `CHANGELOG.md` and `CHANGELOG.pt.md`, `## 2026.10.27.1`, for the error, its date and the 27 slugs; this repository's docs/05 §4 (:104-106 and :201-202, "`after all` names none and leaves it out") and §8 (:438-440). No source note: the kit is taught as it is, and no note points to a file of focus-kit's repository (docs/04). Cases: none; the project of the error stays unnamed, as the changelog leaves it.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content (prose, inline code); the Design slot says prototype, by choice (ADR-0019).

**Out of scope.**

* ch14 :92 and key point 2: they already hold the rule, since `ch11-14-after`; this delivery adds the reason and the error, not the rule again.
* docs/03: the `dependency` row (:120) already leaves out the dropped lines and says a line naming one waits for the person to re-decide it; the `milestone review` (:34), `mark` (:30) and `queue tree` (:123) rows say nothing wrong.
* ch15 :3, :115 and key point 4, "each finding becomes a `[ ]` line": `ch15-review-grades` (M38) teaches the grading.
* The `· from <slug>` suffix, notes and `findings:` in chapter 14: `ch14-queue-findings` (M38); `[?]` never on another line and `waits`: `ch14-after-never-waits` (M39); `queue.sh` drawing every open milestone: `ch14-queue-every-milestone` (M39).
* The kit's history behind the error (how the script read `after all` before): docs/04's "The kit as it is"; the error is told as the reason of the rule.
* The kit's test fixture (`tooltips` above `m2-review`): the kit's own test, nothing a reader of the book runs.

**Done when.**

* [x] C1 to C6 read as the Contract says in both editions; ch14 :92 and both key points 2 still say the rule.
* [x] Both editions written; each chapter opens with its value; no filler and nothing useful cut; the date, the queue script's answer and the 27 slugs from the kit's changelog; no em dash; no run narration; no code but what the chapters already show; the queue tree's words stay within 74 columns if set in a block.
* [x] The error told without naming or hinting at a project, nor tying it to the errors at ch14 :71 and :80: the disclosure scan green.
* [x] `make verify` green after the last edit, with its time.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: chapter 14 already states the rule (:92 and key point 2, in the text since `ch11-14-after`), against `work/done/kit-2026-10-27-1.md`'s "Chapters 14 and 15 still teach the old reading"; so chapter 14 gains the reason, the error and the contrast with a re-decided line, not the rule again, and chapter 15, which says nothing of `after all`, gains the rule as the review's start.
* Decided by the agent, the author corrects it in the review: chapter 14 owns the error, beside the cancelled line it explains and the re-decide rule it is set against; chapter 15 says the rule in one sentence and does not repeat the error (the author's preference: each thing once, in the chapter that owns it).
* Decided by the agent, the author corrects it in the review: the error is told as the changelog words it, with no project named, as the author's word for this run says ("Sim, como o changelog": the dated errors are told as the kit's changelog words them, with no project named, no place and no business detail); it is no Case A or Case B passage, so docs/05 §5's Case A and Case B slot asks nothing of this line. It is the third error of 2026-10-26 in chapter 14, and the text says nothing of whether the projects are the same.
* Decided by the agent, the author corrects it in the review: "27 slugs" is in the text, as the line asks, a figure of the error and not a measure before and after a kit change (docs/04 "The kit as it is"); the gain and the key points carry no number.
* Decided by the agent, the author corrects it in the review: the review waits with a line built on the cancelled one, read from `queue.sh` :128 (`after all` counts every line above but the dropped ones, so `reprint-card` is counted) and :145 (a line naming a dropped one shows `dropped: re-decide`).
* Decided by the agent, the author corrects it in the review: "cancelled" (pt "cancelada") for a dropped line, as chapter 14 already writes it, though the kit's Portuguese changelog says "descartada"; the suffix stays `· dropped:`.
* From the documents: the rule (docs/05 §4 and §8, installed `queue.sh`), docs/03 unchanged (its rows checked above), the five key points (docs/04), no source note to the kit's repository (docs/04), the scope kept off M38 and M39's lines on these chapters (docs/05 §4, other lines).

## Outcome

Built on 2026-11-14 by /apply in a subagent of the driver session, on trunk, before the author read the page; the author's word for this run: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão". The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

* **What was built.** C1 to C6 as the Contract says, in both editions, the Portuguese sentence for sentence.
  * ch14 opening (en :5, pt :5): "...so that it never reads as built nor keeps the milestone's review waiting."
  * ch14, a new paragraph of eight sentences after the re-decide sentence and before `## The queue as a kanban board` (en :222-229, pt :224-231): "A milestone's review would have no such way out." The reason (a review would wait on a line only the person's decision clears, and it is neither dropped nor rewritten), the error of 2026-10-26 "in one project" with `after <slug>, dropped: re-decide` and the 27 slugs, the rule, and the contrast on `print-card` and `reprint-card` supposed in milestone 1 above `m1-review`, with `waits: after print-card, dropped: re-decide` inline (pt `imprimir-cartao`), no new block.
  * ch14 gain (en :269, pt :271): "...and a line closed that way keeps no review waiting."
  * ch15 opening (:3 both): "(written `· after all`, so a line the person cancelled never keeps it waiting)".
  * ch15 `## The review is a delivery` (en :18, pt :18): "Its line ends `· after all`, every line above it in its milestone but the cancelled ones, ..."
  * ch15 key point 2 (en :167, pt :170): "written `· after all`, an `after` that leaves out the cancelled lines".
  * Unchanged, as the page says: ch14 :92 (pt :93) and key point 2 (en :277, pt :279); five key points and three-sentence openings in both chapters.
* **Divergence.** "Holds" became "keeps ... waiting" (pt "faz ... esperar", not "segura"): chapter 14 already uses "hold" for a session occupying a line (:97, :99, :203), so the page's "holds the review" would read as that. Decided by the agent, the author corrects it in the review.
* **Delivery review** (one read-only Opus agent, the four chapters' `git diff HEAD`, this line of docs/06, the page and docs/04): no high candidate; Contract, facts against `queue.sh` :128, :145, :155 and the changelog, docs/04 rules and Behaviour all hold. Fixed in this delivery:
  * medium, en :223 / pt :225 "for the person to re-decide it" read as re-deciding the cancelled line: now "on a line only the person's decision clears";
  * medium, "holds" in the chapter's other sense: replaced as above, in all six places;
  * low, "the only way out was to replace" said more than the changelog and repeated :223: now "nothing the person could write freed it, and the review's `after all` was replaced by a list of the other 27 slugs", and :223 ends "no re-decision of its own would clear it";
  * low, "cannot take that way out" for a rule that never needs it: now "would have no such way out";
  * low, ch15 key point 2's "which" could attach to the review: now "an `after` that leaves out".
  * Kept: the two "and" clauses at the gain (reads correctly); the failure question answered by inference from the contrast (the page puts it under Behaviour); the supposed lines not in the tree at :139-166 ("Suppose" makes it hypothetical).
* **Proof.** `make verify` green after the last edit, 11 seconds (12 before the review's fixes). `make book` green after the last edit, both PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` (EPUBs beside them).
* **Cases.** None: the error is told as the kit's changelog words it, no project named, so docs/05 §5's Case A and Case B slot asks nothing.
* **Environments.** local builds both; GitHub Pages and Release untouched until the author pushes and tags.

```commit
docs(ch14-15-after-all-dropped): teach after all leaving cancelled out

- ch14: why after all leaves a cancelled line out, the error of 2026-10-26
- ch14: reprint-card, naming a cancelled line, still re-decided
- ch14: opening and gain say a cancelled line keeps no review waiting
- ch15: the review line is after all, and when its commands start
- both editions; verify green; the book builds

work/done/ch14-15-after-all-dropped.md
```
