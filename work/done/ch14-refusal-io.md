# ch14-refusal-io

**Objective.** A reader of chapter 14 can tell a refusal from an exception even when the database gives it. A refusal is a rule saying no, checked in code or by a database constraint, and nothing failed. So `SlotTaken`, returned by the repository when the unique index refuses an insert, fits the definition and the key point.

**Behaviour.**

* The definition of a refusal in §"Exception, refusal, error" says the rule may be checked in code or by a database constraint, such as a unique index. Either way nothing failed: the database answered. It replaces "a rule saying no, returned as a value, with no I/O involved." (en/14:84) and "uma regra dizendo não, devolvida como valor, sem I/O envolvido." (pt/14:84).
* "No I/O failed, and no code is wrong; the rule did its job." (en/14:79, pt/14:79) is unchanged, because it stays true for the index.
* Near "the repository returns that as the refusal `SlotTaken`" (en/14:167, pt/14:167), one sentence says this is the same rule checked twice. The use case `book` refuses a time that is not free first, as chapter 15 shows. The index is the last guard when two clients book at once. The code is not quoted again in chapter 14.
* The third key point reads "An exception is I/O that failed, a refusal is a rule saying no, in code or in a database constraint, and neither is thrown." Portuguese: "Uma exceção é um I/O que falhou, uma recusa é uma regra dizendo não, no código ou em uma restrição do banco de dados, e nenhuma das duas é lançada." It replaces the key point at en/14:248 and pt/14:248. Chapter 14 keeps five key points.
* These stay unchanged: "An exception can also become a refusal." (line 129), "A refusal from a rule involves no I/O at all." (line 169, now the contrast with the index), and the chapter's opening (lines 3 and 4).
* Both editions say the same.
* Finding F4 of the M4 review is settled.

**Contract.**

* Files:
  * `book/en/14-errors-and-slices.md`: lines 84, 167 (one sentence added after it) and 248.
  * `book/pt/14-errors-and-slices.md`: the same lines, 84, 167 and 248.
  * `docs/03-Domain.md:50`, the refusal row. Its identifier becomes "`E` of a use case's or repository's `Result<T, E>`". Its meaning says the rule is held in code or in a database constraint, such as a unique index refusing a write. "It travels in a Result like an exception but is not one, since no I/O failed." stays.
  * Line numbers are from before `ch14-feature-boundary`, which replaces line 53 and the first key point (line 246) and moves the lines below. The quoted sentences are the reference.
* Terms of docs/03: none new. The "refusal" row changes as above.
* Sources: the clinic at `book-v1/closing-a-milestone`. `rules.ts:137` returns `SlotTaken` when the time is not in `freeSlots(input)`. `repository.server.ts:34` calls the index `appointment_booked_slot` "the last guard against a double booking", and line 57 returns `SlotTaken`. The pointer goes to chapter 15's `book` (en/15:360, pt/15:361), with a link to its section in each edition.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* That `query` catches every thrown value, so a bug inside it becomes `DatabaseFailed`, and the Error definition (lines 85 and 127, key point 249): that is the later line `ch14-catch-all`.
* The route that reads the request body, and "Where a repository's SQLite exception becomes a Result" (lines 115 and 116, 208 and 209): that is the later line `ch15-route-io`.
* The first key point and the slice text: they belong to `ch14-feature-boundary`, which is in flight.
* The clinic repository: it is not touched. Its docs/03 already calls `SlotTaken` a refusal.

**Done when.**

* [x] Both editions changed with the same meaning. Chapter 14 opens with its value, with no filler and nothing useful cut.
* [x] No "with no I/O involved", "sem I/O envolvido", "a refusal only in a rule" or "uma recusa só em uma regra" is left in `book/`.
* [x] The refusal row of docs/03 updated.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author: run once at the end of the M4.1 loop by the driver, on 2026-09-30, both PDFs built
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* The definition of a refusal now says the rule is checked in code or by a database constraint such as a unique index, and ends "even when the database answers, nothing failed", which holds for both places the rule lives.
* After the sentence on `SlotTaken` from the index, one sentence says it is the same rule checked twice, pointing to the use case `book` in chapter 15's §"One event, one new state" (Portuguese: §"Um evento, um novo estado"). Checked against the clinic at `book-v1/closing-a-milestone`: `repository.server.ts` calls `appointment_booked_slot` the last guard and returns `SlotTaken`.
* The third key point reads as the page gave it; chapter 14 keeps five key points. The refusal row of docs/03 names a repository's `Result` and a database constraint.
* The Portuguese calls the index "a última barreira".
* Nothing diverged from the page. Finding F4 of the M4 review is settled.
