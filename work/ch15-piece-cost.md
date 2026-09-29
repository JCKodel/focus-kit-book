# ch15-piece-cost

**Objective.** A reader of chapter 15 can weigh a piece that has a job: what it costs in files and lines against what it gives that nothing else gives. They can see this on a real case, the health slice's client orchestrator, which costs more than it gives, set against the booking slice's, which pays.

**Behaviour.**

* The reader can say why having a job is needed but is not enough. A piece is written when its job gives more than it costs.
* The reader can weigh `healthEvents.ts` from its numbers. It has a job, because the check event leads to a new state. It costs two files and 34 lines: 20 lines in one file at `book-v1/closing-a-milestone`, 54 lines in three files at `book-v1/four-pieces`. Its two Vitest cases, ok and unreachable, prove what `HealthView.e2e.ts`'s four Playwright tests already prove.
* The reader can say why the same piece pays in the booking slice. `bookingEvents.test.ts` proves that a name typed while the booking is in flight survives a `SlotTaken` answer, and no Playwright test at the tag proves that.
* The reader can say why the clinic kept `healthEvents.ts`. The delivery that wrote it chose "Every event moves", so all eight hooks have one shape. Alone, the piece costs more than it gives; the clinic pays for it to keep that shape. The decision against a piece comes from KISS and YAGNI, which are part of FOCUS. FOCUS is never presented as the cost.
* Key point 2 no longer says, or implies, that a job is enough.
* Both editions say the same.
* Finding F12 of the M4 review is settled (`work/done/m4-review-run/findings.md:67`).

**Contract.**

Sentences are found by their quoted text. `ch15-event-delivery`, `ch15-submit-event`, `slice-imports`, `ch15-route-io` and `ch15-injection-rule` are in flight on chapter 15 and move its lines. The line numbers below are from commit `6d41f5c`.

* `book/en/15-four-pieces.md`, section "When the pieces pay their way" (heading and anchor unchanged):
  * "A piece exists when it has a job." (en:418; pt:419 "Uma peça existe quando tem um trabalho.") becomes the necessary condition. English proposal for `/apply` to tighten: "A piece can exist only when it has a job." Portuguese: "Uma peça só pode existir quando tem um trabalho." The next two sentences (health has no `rules.ts`, and the job of each piece) stay.
  * The ADR-0002 paragraph and its Context sentence (en:421-422, pt:422-423) stay. The ADR's "a file appears only when it pays its way" leads into the new paragraph.
  * A new paragraph goes after it and before "Where the code already has its own shape". It weighs the health check, the section's own example, in this order:
    1. The job: `check`, in [`healthEvents.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/health/healthEvents.ts), turns the server's answer into `ok` or `unreachable`.
    2. The cost, with the tags named in the text: at `book-v1/closing-a-milestone` the health slice's client orchestrator was one file, `useHealth.ts`, of 20 lines. At `book-v1/four-pieces` it is three files: `useHealth.ts` (21), `healthEvents.ts` (16) and `healthEvents.test.ts` (17), 54 lines, counted with `wc -l` at the two tags. It is also an update function that ignores the current state, and a `repositories` parameter that only the test uses.
    3. The gain: the two cases of `healthEvents.test.ts` ("gives ok", "gives unreachable") assert what [`HealthView.e2e.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/health/HealthView.e2e.ts) already asserts. Its four Playwright tests show "Server: ok" and show "Server: unreachable" twice, on a 500 and on no answer.
    4. The contrast: the same piece pays in `bookingEvents.ts`, which step 2 of the chapter already shows (the first occurrence; not shown again). Its test "keeps a name typed in flight through a taken slot" proves something no Playwright test at the tag proves.
    5. The verdict and why the clinic kept it: alone, `healthEvents.ts` costs more than it gives. The clinic's delivery that wrote it, [`orchestrator-tests`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/work/done/orchestrator-tests.md), chose "*Every event moves*" so that every hook has one shape. That shape is the gain the clinic pays for, not the piece.
  * The Portuguese paragraph says the same, keeps "fatia `health`" as `pt-health-slice` decided, and quotes the clinic's English with the book's own translation in the text, as the chapter already does for ADR-0002.
  * "Where the code already has its own shape, the pieces can cost more than they give." and the three sentences after it (en:425-428, pt:426-429) stay, as the whole-architecture counterpart.
  * The paragraph gives no definition of a unit test or an end-to-end test. It names the files and what each test asserts.
* Key point 2 (en:433 "A piece is written when it has a job, and the "Forbids" column keeps it to that job."; pt:434) becomes, as a proposal for `/apply` to tighten: "A piece is written when it has a job and that job gives more than it costs; the "Forbids" column keeps it to that job." Portuguese: "Uma peça é escrita quando tem um trabalho e esse trabalho dá mais do que custa; a coluna "Proíbe" a mantém nesse trabalho."
* Terms of docs/03: none new, none changed.
* Sources: the clinic at `book-v1/closing-a-milestone` (`src/features/health/useHealth.ts`, 20 lines) and at `book-v1/four-pieces`, commit `e6653b5` (the files above, and `work/done/orchestrator-tests.md:193` for "Every event moves"). Counted by `wc -l` on `git show <tag>:<path>`. The files are linked in the text; no new note.
* Cases: none. Ninjobs is not used. Exercises: unchanged.

**Out of scope.**

* The clinic's code, its docs/01 and its tag: the person chose the book only. `healthEvents.ts` stays, and so does `clinic-update-type`'s count of seven files.
* Key point 1 and the route's I/O: `ch15-route-io`, in flight. Key point 5 and "Nowhere else is anything passed": `ch15-injection-rule`, in flight.
* What a unit test is, compared with the route test: the later line `ch16-unit-test`.
* The weekly hours hook's forwarding and the repeated update type: the later clinic lines `clinic-hours-report` and `clinic-update-type`.
* Weighing all eight hooks, `clinicEvents.ts` included: one case and its contrast are enough to weigh a piece.
* The chapter's opening sentence and Exercise 15.3: they already ask which pieces pay their way.

**Done when.**

* [ ] Both editions changed with the same meaning. Chapter 15 still opens with its value, with no filler and nothing useful cut.
* [ ] Every count in the new paragraph names its tag, and the method (`wc -l`) is in the text.
* [ ] No "A piece exists when it has a job" or "Uma peça existe quando tem um trabalho" left in `book/`. Key point 2 in both editions names the job and the weighing.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
