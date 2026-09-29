# ch15-event-delivery

**Objective.** A reader following the clinic knows which delivery added the event functions after chapter 12. They add it to their queue and build it before reading the excerpts, so their code can match `book-v1/four-pieces`.

**Behaviour.**

* In §"The four pieces", en/15:9 and pt/15:9 name the delivery instead of calling it "the clinic's first delivery of milestone 1.1" ("a primeira entrega do marco 1.1 da clínica"). The name is the clinic's `orchestrator-tests`, linked to its page at the tag. The parenthesis on milestone 2 stays.
* A short paragraph right after line 9 does three things:
  * It says in one sentence why a line that is not a finding sits in milestone 1.1. The author added it because chapter 16 needed client orchestrators with tests.
  * It tells the reader to add the clinic's line as the first line of their milestone 1.1, the one exercise 12.3 wrote, and to add the clause "every client orchestrator has unit tests" to that milestone's paragraph.
  * It tells the reader to run `/propose orchestrator-tests`, answer its questions with the author's brief, which the note links, and then run `/apply orchestrator-tests`, before reading on.
* The line is printed in a code block, word for word as the clinic's queue has it, the same in both editions:

  ```
  [ ] orchestrator-tests   every use<Feature>.ts hook's events move to plain functions with repositories as a parameter, tested in Node
  ```

* Both editions say the same.
* Finding F7 of the M4 review is settled for chapter 15.

**Contract.**

* Files:
  * `book/en/15-four-pieces.md`: line 9 and a new paragraph after it. There is also one new note at the end.
  * `book/pt/15-four-pieces.md`: the same.
* Sources:
  * The clinic at `book-v1/four-pieces`, commit `e6653b5`, the only commit after `book-v1/closing-a-milestone`. Its `docs/06-Queue.md` holds the line and the paragraph clause. Its `work/done/orchestrator-tests.md` is the page the link opens.
  * The brief is in `work/done/clinic-orchestrator-tests-run/README.md:40-44`.
  * The note is `[^clinic-orchestrator-tests-run]`. Its first occurrence is chapter 16's note (en/16:384, pt/16:386). Chapter 15 repeats that text with the link going to the run's `README.md`, where the brief is.
* Terms of docs/03: none new.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* Chapter 16's "These turns ran before the event functions existed" (en/16:330). It reads correctly once chapter 15 names the delivery, and no queue line names chapter 16 for it.
* Chapter 14's 22-file listing. It quotes `book-v1/closing-a-milestone`, which comes before the event functions.
* The hook's `submitEvent`, `shown` and `latest`. That is the later line `ch15-submit-event`.
* The route's body read, the injection rule, and the cost of a piece. Those are the later lines `ch15-route-io`, `ch15-injection-rule` and `ch15-piece-cost`.
* Slice imports. That is the later line `slice-imports`.
* en/15:50 and pt/15:51. They belong to `ch14-feature-boundary`, which is in flight.
* The clinic. It is not touched, and no tag moves.

**Done when.**

* [ ] Both editions changed with the same meaning. Chapter 15 opens with its value, with no filler and nothing useful cut.
* [ ] The line in the code block matches the clinic's `docs/06-Queue.md` at `book-v1/four-pieces`, byte for byte.
* [ ] `make verify` green, the link to `orchestrator-tests.md` at the tag included.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
