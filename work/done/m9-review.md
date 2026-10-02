# m9-review

**Objective.** The author knows, clause by clause, whether M9's paragraph holds in the hands of a reader of the prologue and chapter 25, in both editions, and every clause that fails is a `[ ]` line in M9 under this review; and the book's own process, docs/05, runs milestone reviews the way the book teaches them (focus-kit d333348).

**Decided by the author.**
1. This review follows the kit's rule, not the old §8 recipe, and brings docs/05 to that rule in the same delivery; `milestone-review-process` is absorbed by it and marked `[x]` with that note.
2. The person tests alone: no fresh session reads the chapters as a reader, no agent proposes findings. The agent prepares, records and writes the lines.

**Behaviour.**

* The author receives both PDFs (`make book`) and the table of clauses below, and tests each clause by reading the passage it names, in English and then in Portuguese.
* For each clause the author answers, in the conversation, `C<n>: holds` or `C<n>: fails, <what the reader does not get>`; there is nothing to confirm or reject afterwards: a clause that fails in the author's hands is a finding.
* Each finding becomes one `[ ]` line in M9, under `m9-review`, saying what will be true, never how to fix it; written by the agent from the author's words, shown to the author before it is staged. No M9.1.
* No finding: M9 closes with this delivery; the page says so.
* No chapter, no note and no record of `ask-for-more-*` is edited by this delivery.
* docs/05 says, in §4, §7 and §8, what the kit's SETUP.md says at d333348, in this book's words; a reader of docs/05 alone finds no `.1`, no confirmed or rejected finding, no code review and no headless review recipe.

**Contract.**

The clause table, what the author tests (M9's paragraph, quoted: "When this milestone closes, a reader knows why an agent's first answer feels final, what an agent never proposes (the test of a limit it claimed, the reader's time, the cost, what nobody asked for), and how to ask for more with a challenge protocol, with a recorded experiment and published studies as the evidence; the prologue plants the idea and chapter 25 teaches it."):

| | Clause | Answered by | Passage (en and pt) | How the author tests it |
|---|---|---|---|---|
| C1 | why an agent's first answer feels final | ask-for-more-chapter | 25 §Why the first answer feels final | After reading it, without looking back: can you give three reasons a first answer is accepted, and whose finding each is? |
| C2 | what an agent never proposes (the four) | ask-for-more-chapter | 25 §What the agent does not propose | Can you name the four, and say for each why the agent leaves it out? |
| C3 | how to ask for more with a challenge protocol | ask-for-more-chapter | 25 §The challenge protocol | On one real task of your own, send the four turns from the book's list alone, with nothing else open: can you? Can you say why turn 2 asks for a test and not "Are you sure?", and when the protocol is not worth sending? |
| C4 | a recorded experiment and published studies as the evidence | ask-for-more-experiment, ask-for-more-chapter | 25 §What the protocol bought, and what it cost; its notes | Does every number lead, through its note, to something you can open, and are the experiment's limits said where its numbers are? |
| C5 | the prologue plants the idea | ask-for-more-chapter | Prologue §People (en and pt line 41), §What the team gains (line 65) | Reading only the prologue: does a reader know that validating an agent includes asking it for more, and where the book shows how? |
| C6 | chapter 25 teaches it | ask-for-more-chapter | 25 whole, opening to Key points | Does it open with what you can do after it, follow from the earlier chapters alone, say what the team gains, and does the Portuguese mean what the English means? |

The finding line, in docs/06 under M9:

```
[x] m9-review                the review of M9: ...
[ ] <slug>                   <what will be true>
```

docs/05, in this book's words, after the kit at d333348:

* §4: "Each milestone is planned with its review as the last line (§8)." replaces "The last line of each milestone is its review (§8)."
* §7: the list gains "no review of a review" after "no gate before implementation".
* §8, rewritten: the review is the milestone's last planned line, `<milestone>-review`, a delivery like the others; its page takes the paragraph clause by clause and writes which delivery answers each and how a person tests it; it reviews no code and fixes nothing; the person tests each clause by hand; a clause no delivery answers, or that fails in the person's hands, is a finding; each finding is a `[ ]` line in the same milestone under the review line, waiting for /propose; the milestone closes when those lines are `[x]`; they get no second review, each passing through its own page, its proof and the person's commit; a finding is never a fix in the middle of the next milestone. For a milestone of chapters, testing by hand is the author reading, in the PDF of both editions, the passages the page names, and answering the test the page wrote. One sentence of history replaces both the recipe and the closing paragraph on the guided project's code review: M3 and M4 were reviewed by a headless session whose findings opened `.1` milestones, with a code review of the guided project beside them, and both recipes are in the history of this file at the commit before `m9-review`.

docs/06:

* `milestone-review-process` `[x]`, its line ending "; absorbed by m9-review".
* `m7-review`: "each confirmed finding becomes a line in a new milestone M7.1" becomes "each clause tested by hand, each finding a line in M7 under the review".
* `m9-review` `[>]` now, `[x]` by /apply.

docs/03: no change; its rows for milestone review and finding already say this.

**Out of scope.**

* Fixing any finding: each is its own line.
* Product questions 1 to 7 as a checklist: each was asked when its delivery was done; this review tests the paragraph, as the kit says. A product question that fails while testing a clause is part of that clause's answer.
* Any chapter but the prologue and 25: Parts I to IV are `m8-review`'s.
* An agent's reading as support: decision 2.
* `m8-review`'s line: it is already the author reading, with no review of its own.
* focus-kit itself, and the records of m3, m4 and m4.1 reviews: a record says what happened.
* M3.1, M4.1 and M4.2 in docs/06: they stay as history, since a line never leaves the queue.

**Done when.**

* [x] docs/05 §4, §7, §8 as Contract; `grep -n -E '\.1|confirmed|code review|headless' docs/05-Process.md` prints only the history sentence of §8.
* [x] docs/06: `milestone-review-process` `[x]`, `m7-review` adjusted.
* [x] `make book` run; both PDF paths given to the author with the clause table.
* [x] C1 to C6 each answered by the author, recorded under What happened in the author's words.
* [x] Each failed clause a `[ ]` line in M9 under `m9-review`, approved by the author; or the page says there was none.
* [x] No file under `book/` changed.
* [x] `make verify` green, disclosure scan included.
* [x] Page in `work/done/`, `m9-review` `[x]`, staged, commit message suggested.

**What happened.**

* docs/05 §4, §7 and §8 rewritten after focus-kit d333348; the recipe of a headless review and the paragraph on the guided project's code review gave way to one history sentence. The grep of Done when prints only that sentence (two lines of it).
* docs/06: `milestone-review-process` `[x]`, absorbed by this delivery; `m7-review` adjusted; `m9-review` `[x]`.
* `make book` run; the author got both PDFs and the clause table, with the pages where the prologue and chapter 25 start.
* The author's answers, in their words (given in Portuguese, rendered here): "The only correction is about the protocol: it is not entirely clear to me what it is or where it is written, and the USD values say nothing to me, who pays a fixed subscription (and a session costing USD 8 is something scary for this context)."
  * C1: holds. C2: holds. C5: holds. C6: holds.
  * C3: fails, the reader is not sure what the challenge protocol is or where it is written.
  * C4: fails, the cost in USD says nothing to a reader on a fixed subscription, and a session priced at USD 8 reads as frightening.
* Two findings, two `[ ]` lines in M9 under `m9-review`, shown to and approved by the author: `ch25-protocol-findable` (C3) and `ch25-cost-for-subscribers` (C4). M9 closes when both are `[x]`; no M9.1.
* Nothing diverged from the plan; no file under `book/` changed; no ADR (the rule is the kit's, carried into docs/05).
