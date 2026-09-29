# milestone-1-bridge

**Objective.** After chapter 11, a reader following the guided project knows to build the rest of the clinic's milestone 1 with `/propose` and `/apply`, one line at a time, what to expect on the way, and which tag to compare the result against, so chapter 12 reviews a milestone the reader has.

This settles finding F17 of the M3 review (`work/done/m3-review-run/findings.md`): chapter 11 ends with `skeleton`, chapter 12 opens with the milestone closed, and nothing between them tells the reader to build the six deliveries in between, gives a tag to compare, or says where `npm run setup` comes from.

**Behaviour.**

* A reader who finishes chapter 11 reads that the rest of milestone 1 is built the same way as `skeleton`: `/propose`, read and correct the page, `/apply` in a fresh session, review the staged change, commit; one line at a time, in the queue's order, each committed before the next starts, with no tag.
* The reader can name the lines left after `skeleton`, in order: `clinic-setup`, `professionals`, `weekly-hours`, `book-appointment`, `cancel-appointment`.
* The reader knows a line may enter the milestone while it is being built, and why: `/apply weekly-hours` found a sign-in failing about once in 300 Playwright tests, and at the author's request it became the line `e2e-database-busy`, inside milestone 1, built before `book-appointment`. So the author's milestone has seven commits, and the reader's queue may differ.
* The reader knows `clinic-setup` adds `npm run setup`, which creates the clinic and its owner, so chapter 12's "run `npm run setup` and `npm run dev`" is not new.
* The reader knows what the author's build met, to expect the same: two of the six pages corrected before `/apply`, four with no correction; corrections to the staged change in three deliveries; 25 calls denied by the permission mode, none retried another way; twice a suggested commit message with a `Co-Authored-By` trailer, corrected by request before the commit.
* The reader can compare their milestone 1 with the tag `book-v1/closing-a-milestone`, and knows its code is milestone 1 as built, and that its one later commit, from chapter 12, only adds lines to the clinic's docs/06.
* Exercise 11.4 asks the reader to do all of that; exercise 12.1 starts from it.

**Contract.**

*Opening.* Chapter 11's opening gains a third sentence, so it promises the new section: you can then build the rest of a milestone the same way, one line at a time. Its two sentences today stay as they are.

*Sections.* Chapter 11 (`book/<edition>/11-apply.md`) gains one section, `## The rest of milestone 1` / `## O resto do marco 1`, after "Review before you commit" and before "Key points". Order inside it: the loop to repeat and the lines in order; `npm run setup`; the line that entered in the middle; what the build met; the tag to compare. Key points stay as they are (five already, and the section repeats a loop they already state).

*Exercises.*

* New `### Exercise 11.4` / `### Exercício 11.4`: build the rest of your milestone 1, from `clinic-setup` to `cancel-appointment`, one delivery at a time with `/propose` and `/apply`, committing each; then compare your code with [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone).
* Chapter 12, exercise 12.1: "With your milestone 1 built" becomes "After exercise 11.4", or its Portuguese equivalent; the rest unchanged.

*Terms of docs/03.* None new. Used: delivery, page, queue, milestone, fresh session, permission mode, stage, chapter tag.

*Sources.* The numbers come from `work/done/clinic-milestone-1-run/README.md`: six deliveries after `skeleton`; page reviews, two with corrections and four with none; staged corrections in `clinic-setup`, `weekly-hours` and `e2e-database-busy`; denied calls 5 + 4 + 5 + 4 + 5 + 2 = 25; the trailer twice. "About once in 300" comes from `work/done/clinic-milestone-1.md`, What happened. Chapter 11 gains the note `[^clinic-milestone-1-run]` with the same key and text as chapter 12's, printed once in this chapter; a key shared by two chapters already exists (`ninjobs`, `closing-a-milestone-run`). The tag's content is checked against the clinic: `book-v1/closing-a-milestone` is `c54d011`, whose only change over `f16f83b` is `docs/06-Queue.md`.

*Cases.* The guided project only. No Ninjobs, no Case A or B.

*Editions.* Both, same delivery, same headings and note keys; Portuguese uses docs/03's terms (marco, entrega, página, fila, stage).

**Out of scope.**

* A new tag on `f16f83b`: `book-v1/closing-a-milestone` already holds the code, and only chapters tag (docs/05 §5).
* A new chapter between 11 and 12: one section carries it, and renumbering 12 to 25 costs more than it gives.
* Changing chapter 12's opening or "Check the paragraph": they read right once chapter 11 has said this.
* Retelling each delivery's corrections or denied calls one by one: the record behind the note holds them.
* Any change to the clinic's repository: nothing is built or tagged there.
* The other M3.1 lines (`ch12-numbered-findings`, `ch13-unmet-terms`): their own pages.

**Done when.**

* [x] Both editions have the opening's third sentence, the section and exercise 11.4 in chapter 11 and the new start of exercise 12.1 in chapter 12.
* [x] Every Behaviour line can be checked in the text of both editions.
* [x] No filler and nothing useful cut; no em dash.
* [x] Every number traced to the record, and the note in chapter 11.
* [x] The tag link opens (link check).
* [x] docs/06: `milestone-1-bridge` is `[x]`.
* [x] `make verify` green, the disclosure scan included.
* [x] `make book`, and the paths of both PDFs given to the author.
* [x] Page in `work/done/`, staged, commit message suggested.

## What happened

**Built.** Chapter 11, both editions: the opening's third sentence, the section "The rest of milestone 1" / "O resto do marco 1" between "Review before you commit" and "Key points", exercise 11.4 and the note `[^clinic-milestone-1-run]`, same key and text as chapter 12's. Chapter 12, both editions: exercise 12.1 starts "After exercise 11.4" / "Depois do exercício 11.4".

**Diverged from the plan, and why.**

* The tag's later commit is described as changing only the clinic's docs/06, where it queues what chapter 12's review found, not as "only adds lines": `git diff f16f83b c54d011` shows 16 lines added and one changed, the old milestone 2 heading, renamed to milestone 3.
* "None retried another way" became what the record says: the agent took an allowed way each time (reading files one by one, `mv` for `git mv`) and nothing was run for it from outside its session. The record's "none was retried by another route" means from outside the clinic's session; inside it, the agent did use other allowed commands.
* `e2e-database-busy`: the author asked for the flaky sign-in to become a line, and the agent chose where; the text says "at my request ... the agent made it the line ... and put it inside milestone 1", as the record has it. The cause (an earlier test writing to the test database, no busy timeout on the server's connection) is from the staged review request of `weekly-hours`, in the record.
* The 25 refused calls are placed in "my headless runs", since a reader in an interactive session meets them as permission questions, not refusals.

**Dropped.** Nothing from Behaviour or Contract.

**What the proof found.** `make verify` green, the link check opening the tag URL and the disclosure scan included. `make book` built both PDFs and EPUBs; its only warning is the PDF renderer ignoring `user-select: none`, from the stylesheet, which this delivery did not touch. The tag checked against the clinic: `book-v1/closing-a-milestone` is `c54d011`, whose one change over `f16f83b` is `docs/06-Queue.md`; `package.json` of the clinic has `"setup"`.

**Decisions.** None beyond the page; no ADR, no new term in docs/03.
