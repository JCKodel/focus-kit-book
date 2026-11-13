# ch12-14-mark-refused

Decided before the author read it: the author's word for this run, relayed by the driver session on 2026-11-13, is "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão", so every question the documents leave open is answered by the agent's recommendation, marked "decided by the agent, the author corrects it in the review" (docs/05 §4, a command that says to decide alone). The page is built before the author reads it.

**Objective.** After chapters 12, 13 and 14 the reader, developer or not, knows that the kit's mark script puts a `[~]` only on a `[ ]` line and a `[*]` only on a `[>]` one and refuses any other, writing nothing and saying the line is another session's, resumed only on the person's word, so two sessions that start one line cannot both mark it and build it twice.

**Behaviour.** What the reader can do or explain afterwards:

* Say the rule: the mark script sets `[~]` only on a line that is `[ ]` and `[*]` only on a line that is `[>]`; on any other line it refuses before it writes anything, and its message says a `[~]` or `[*]` is another session's, resumed only on the person's word. The other four marks are not checked this way.
* Say why, as the error the rule prevents, in the present: two sessions that start one line both read it free until one marks it, so the check has to be made where the mark is set, against what the line holds at that moment, or both mark it and both build; on 2026-10-26, in one project, `/apply` of one slug was typed in two sessions six seconds apart, in one folder on trunk, and the second read the line `[>]`, marked it `[*]` and built it too.
* Edge, two `/apply`: asked "you typed `/apply return-book` in two terminals a few seconds apart; what happens?", answer: the first marks the line `[*]` and builds; the second's mark is refused, because the line is no longer `[>]`, and it stops without building, saying the line is another session's.
* Edge, two `/propose`: asked the same of `/propose reservations`, answer: the second's `[~]` is refused, the line being no longer `[ ]`.
* Edge, a line not defined: asked "may `/apply` mark `[*]` on a `[ ]` line?", answer no: the script refuses a `[*]` on any line that is not `[>]`, as `/apply` already refuses a page not completely defined.
* Edge, a session that ended: asked "`lend-book` stayed `[*]` when its build lost the connection; you say so and run `/apply lend-book` again; is its mark refused?", answer: the line keeps its `[*]` and nothing marks it again, so nothing is refused, and the command goes on from what is built; the refusal stops a session that did not know the line was taken, not one the person sent back to it.
* Failure: asked "the script refused my `[*]`; may I change the byte by hand and go on?", answer no: the refusal says another session holds the line; only the person, who knows that session ended, resumes it, and the resumed command keeps the mark as it is.
* Find in chapter 14 the rule, the error and the resumed line's mark; in chapter 12 that `[~]` goes only on a `[ ]` line; in chapter 13 that `[*]` goes only on a `[>]` line, so a second `/apply` of the slug stops there.
* In the Portuguese edition, the same, with docs/03's Portuguese terms: "script de marca", "linha da fila", "retomada", "a palavra da pessoa" as the kit's Portuguese changelog says it.

**Contract.** Six chapter files and one document; line numbers en at HEAD `28a607a`, quoted beside each so a drift is found; pt follows en sentence for sentence, at the same lines in ch12 and ch13 and, in ch14, at pt :3, :78, :203, :260 and :264 for C1 to C5. The text is the agent's within these changes.

* **ch14** (`book/en/14-queue-states.md`, `book/pt/14-queue-states.md`)
  * C1, opening (:3, "how, one byte through the kit's mark script while every other edit of the queue changes only its own lines, since a program that writes the whole queue can empty it"): one clause more, the reader also says why the script refuses a second start of one line. Still three sentences.
  * C2, owner of the rule, a new paragraph in `## How a mark changes` after "With `stage` at the end, it changes the same line in the index and nothing else there" (:77) and before "Every other edit to docs/06 is the host's own file edit" (:79): the problem, two sessions that start one line both see it free until one marks it; the rule, `[~]` only on `[ ]`, `[*]` only on `[>]`, any other refused before anything is written, the message saying the line is another session's, resumed only on the person's word; the error of 2026-10-26, two `/apply` of one slug six seconds apart in one folder on trunk, the second reading `[>]`, marking `[*]` and building too, told "in one project", as :71 tells its error, never naming the changelog (docs/04 :30), and saying nothing of whether it is the project of the emptied queue told at :71; the reason in the present is that both sessions read the line free, so the check is made where the mark is set, never a description of an earlier script.
  * C3, `## A session that ended, a delivery cancelled`, after "the line stays `[*]`, never put back to `[>]` or `[ ]` as if nothing had been done" (:201): one clause, the resumed line keeps its mark and nothing marks it again, and a second `[~]` or `[*]` on it would be refused by the mark script. No pointer: C2 is a few paragraphs above.
  * C4, the team gain (:258, "And no session marking its line can leave the queue empty under the board and the other sessions"): one sentence or clause, no number: nor can two sessions that start one line both build it.
  * C5, key point 1 (:262, "every mark changes through the kit's mark script, one byte"): a clause, `[~]` only on a `[ ]` line and `[*]` only on a `[>]` one. Still five key points.
* **ch12** (`12-propose.md`, both editions)
  * C6 (:31, "through the kit's mark script, `propose/scripts/mark.sh`, which changes that one mark and nothing else of the file"): a clause, and which sets `[~]` only on a `[ ]` line, so a second `/propose` of the slug is refused. No key point changes: the chapter already has six (a note of `ch12-14-mark`).
* **ch13** (`13-apply.md`, both editions)
  * C7 (:52, "does it mark the line `[*]` in docs/06, through the mark script, as its first edit, so the queue shows the build under way"): one sentence after it, the script sets `[*]` only on a `[>]` line, so a second `/apply` of the slug, typed in another session, is refused there and stops without building, the line being another session's.
  * C8, key point 2 (:293, "It marks the line, through the kit's mark script, `[*]` with its first edit"): a clause, `[*]` only on a `[>]` line. Still five key points.
* **docs/03** (`docs/03-Domain.md`), the `mark script` row (:31, "and refuses unless the result keeps its size and differs in at most that byte"): one clause, a `[~]` only on a `[ ]` line and a `[*]` only on a `[>]` one, any other refused with nothing written, so two sessions that start one line cannot both mark it, as two `/apply` of one slug six seconds apart did on 2026-10-26; the row's closing parenthesis gains "the refusal of a second start since 2026.10.27".

Terms of docs/03: mark, mark script, queue line, resume suffix, claim; none new. Sources: the installed `.agents/skills/propose/scripts/mark.sh` (:10 to :12, and its refusal "a [~] or [*] is another session's, resumed only on the person's word; nothing written"); the kit's `CHANGELOG.md` and `CHANGELOG.pt.md`, `## 2026.10.27`, for the error and its date; this repository's docs/05 §4 (:215-216, "`mark.sh` refusing a second start of one line is that of 2026.10.27"). No source note: the kit is taught as it is, and no note points to a file of focus-kit's repository (docs/04). Cases: none; the project of the error stays unnamed, as the changelog leaves it.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content (prose, inline code); the Design slot says prototype, by choice (ADR-0019).

**Out of scope.**

* The kit's history behind the error (the host's edit from `[>]` before the script, the script that changed the byte whatever the line held): docs/04's "The kit as it is" keeps a kit change's history out; the error is told as the reason of the rule.
* That the check is not a lock (two runs within the same instant): the kit claims only that the second is refused, and the book says no more than the kit.
* Chapter 19's two sessions in one folder: they run different lines, which the refusal does not touch; nothing there is wrong.
* Chapters 7, 11 and 18: `m34-fixes`, defined at the same time by another session.
* Chapter 12's six key points: a note of `ch12-14-mark` for the review, older than this delivery.

**Done when.**

* [x] C1 to C8 read as the Contract says in both editions, with the docs/03 clause.
* [x] Both editions written; each chapter opens with its value; no filler and nothing useful cut; the date and the six seconds from the kit's changelog; no em dash; no run narration; no code but what the chapters already show.
* [x] The error told without naming or hinting at a project, nor tying it to the error at ch14 :71: the disclosure scan green.
* [x] `make verify` green after the last edit, with its time.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.
* [x] The Outcome says `m34-review`'s candidate R3-8, "the refusal of a second start untaught", is answered here.

**Decisions.**

* Decided by the agent, the author corrects it in the review: docs/03's `mark script` row does not hold the refusal (it says only "refuses unless the result keeps its size and differs in at most that byte"), against the brief that said it did and with `m34-review` R3-8 citing the same row; the row gains the clause in this delivery, as AGENTS.md says a delivery that changes behaviour updates the document that owns it.
* Decided by the agent, the author corrects it in the review: chapter 14 owns the rule and the error, in `## How a mark changes`, beside the script's other refusal; the session-ended section gets one clause on the resumed line's mark; chapters 12 and 13 say only which start the script refuses, with no new pointer, as `ch12-14-mark` placed the script.
* Decided by the agent, the author corrects it in the review: a resumed line keeps its mark and nothing marks it again; read from docs/05 §4 ("A `[~]` or `[*]` line whose session ended ... keeps its mark; its command resumes it on the person's word") and from `mark.sh`, which has no word to resume and would refuse.
* Decided by the agent, the author corrects it in the review: the error is told as the changelog words it, with no project named, as the author's word for this run says ("Sim, como o changelog": the dated errors are told as the kit's changelog words them, with no project named, no place and no business detail); it is no Case A or Case B passage, so docs/05 §5's Case A and Case B slot asks nothing of this line.
* Decided by the agent, the author corrects it in the review: "six seconds" is in the text, as the line asks, a figure of the error and not a measure before and after a kit change (docs/04 "The kit as it is"); the gain and the key points carry no number.
* From the documents: the rule (installed `mark.sh`, docs/05 §4), the no-key-point-added limit (docs/04, five bullets), the scope kept off `m34-fixes`'s chapters (docs/05 §4, another session's work).

## Outcome

Built on 2026-11-13 by /apply in a fresh session, on trunk, before the author read the page, on the author's word for this run: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão". The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

What was built, by Contract item (pt at the same place, sentence for sentence):

* C1, ch14 opening: "and why the script refuses a second start of one line" (pt "e por que o script recusa um segundo começo de uma mesma linha"); the opening keeps its two sentences.
* C2, ch14 `## How a mark changes`, a new paragraph after the `stage` sentence: the problem (two sessions both read the line free until one marks it), the error of 2026-10-26 "in one project", six seconds apart, in one folder on trunk, the second reading `[>]`, marking `[*]` and building too, then the rule, checked where the mark is set, the refusal's message paraphrased, and "The other four marks are set without that check."
* C3, ch14 session-ended section: "neither resumed command marks its line again, and the mark script would refuse a second `[~]` or `[*]` on it."
* C4, ch14 gain: "nor can two sessions that start one line both build it", and "a start on a line already taken is refused"; no number.
* C5, ch14 key point 1: "`[~]` only on a `[ ]` line and `[*]` only on a `[>]` one"; still five key points.
* C6, ch12 :31: "and sets `[~]` only on a `[ ]` line, so a second `/propose` of the slug is refused there".
* C7, ch13 :53, a new sentence after :52: the script sets `[*]` only on a `[>]` line, so a second `/apply` of the slug typed in another session is refused there and stops without building.
* C8, ch13 key point 2: "only on a `[>]` line"; still five key points.
* docs/03, the `mark script` row: the clause on `[~]` and `[*]`, the error of 2026-10-26, and "the refusal of a second start since 2026.10.27" in its closing parenthesis.

`m34-review`'s candidate R3-8, "the refusal of a second start untaught", is answered here.

Divergences: none from the Contract. C2's order became problem, error, rule, the order of the section's earlier paragraphs (:69 to :74), on the review's suggestion, so the error is not read as the rule failing.

Proof: `make verify` green, 10 seconds after the last edit (14 s on the first run). `make book` built both editions under the run's lock: `/Volumes/Data/Projects/focus-kit-book/output/one-page-at-a-time.pdf` and `/Volumes/Data/Projects/focus-kit-book/output/uma-pagina-de-cada-vez.pdf`.

Delivery review: one read-only Opus agent read the diff of the seven paths, this line's hunk of docs/06, the page, docs/04, `mark.sh` and the changelog. No must-fix. Seven suggestions; taken: the C2 order (1), pt "numa mesma pasta, no trunk" for "numa pasta só no trunk" (4), pt "marcou-a como `[*]`" (5), pt "conseguem ambas construí-la" (6). Declined, decided by the agent, the author corrects it in the review: (2) the same date as :71's second error needs no change, the text ties nothing; (3) C6 and C7 hold where the mark script runs, and with a branch per delivery the claim of chapter 12 stops another clone first, which the chapters already say; (7) the opening's added clause stays a clause, as C1 asks. The reviewer also noted the docs/06 hunk holds `m35-review`'s line, another session's: only this line is staged, by `mark.sh` with `stage`.

Decisions taken alone (decided by the agent, the author corrects it in the review): the four other marks said to be set without the check, as `mark.sh` sets them; the refusal's message paraphrased, not quoted, so the Portuguese edition gives it in Portuguese; "taken" (pt "ocupada") for a line another session holds, as ch14 already says.

Environments: local builds the site and both PDF and EPUB; GitHub Pages and the Release are unchanged until the author pushes and tags.

```commit
docs(ch12-14-mark-refused): teach mark.sh refusing a second start

- ch14 owns the rule, the error of 2026-10-26 and the resumed mark
- ch12 and ch13 say which start the script refuses
- docs/03's mark script row gains the refusal
- both editions; answers m34-review's candidate R3-8

work/done/ch12-14-mark-refused.md
```
