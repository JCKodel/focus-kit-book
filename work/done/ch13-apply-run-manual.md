# ch13-apply-run-manual

**Objective.** After chapter 13 a reader can say that `/apply`'s next steps, using the delivery as its user would first, belong to the conversation and end with it, and that what lets anyone run the product again, from a fresh clone, is the manual of running it: written by the first delivery after which a person can run the product and updated by every delivery that changes a step; both editions.

**Behaviour.**

* Reading chapter 13's "Green is not done", the reader learns that before the review `/apply` also writes the manual of running the product, from a fresh clone to its first screen or call, when its delivery is the first after which a person can run it, and updates it when its delivery changes a step; and that the next steps it ends with are said in the conversation and end with it, so the manual is what is still there for the next person, or for you when another agent ran the session on your behalf and its steps never reached you.
* Reading chapter 13's `lend-book` example, the reader learns where the library's manual of running it is (`docs/manuals/run-the-app-from-a-clone.md`), that `skeleton` wrote it, being the first delivery after which a person could run the app, and that `lend-book` leaves it as it is, since its migration runs with the command the manual already gives; and what a delivery that adds a step, a service to start or a variable to set, would do instead.
* Reading chapter 13's checklist of the staged change, the reader finds one question on it: if the delivery is the first after which the product runs, or changed a step of running it, does the manual of running it say so.
* Reading chapter 13's Key points, the reader finds the same in one clause beside the next steps.
* Following the pointer to chapter 7 from the manuals bullet, the reader finds the manual of running it among chapter 7's kinds of manual, as `ch10-12-run-manual` leaves that chapter.
* Fails if: chapter 13 says the next steps are written anywhere but the conversation, or that the manual replaces them (using the delivery stays the first next step); it says the manual is owed by `/brainstorm` or by every delivery; `lend-book` is said to write or change the manual; a passage says the rule is new, names a version, a date, "no longer", or tells the kit's changelog case (the project whose milestone closed unrunnable); a passage narrates a run or names a host's command beyond what the chapter already names; the title changes; a file other than chapter 13 is touched.

**Contract.**

The same passages in both editions, `book/en/13-apply.md` and `book/pt/13-apply.md`; Portuguese line numbers equal the English ones. Wording is /apply's within the sense below.

* Terms: "the manual of running it" when the product was just named, else "the manual of running the product"; Portuguese "o manual de rodá-lo" and "o manual de rodar o produto", as the kit's README.pt.md says. `ch10-12-run-manual` uses the English phrase and fixes no Portuguese one; this page fixes it, for the driver to pass on.
* The lending library's file, as `ch10-12-run-manual` names it for chapter 7: `docs/manuals/run-the-app-from-a-clone.md`, Portuguese `docs/manuals/rodar-o-app-de-um-clone.md`, written by `skeleton` (pt `esqueleto`), chapter 11's first line.
* Source: focus-kit 2026.10.19.2 (`git -C ~/Projects/focus-kit show 44132c4:SETUP.md`, the Manuals slot and the `/apply` file; the `/apply` file's next steps are unchanged since 2026.10.19.1); no source note, since the chapter quotes nothing new.

Passages:

* "Green is not done", line 101, the manuals bullet: stays, its pointer to chapter 7 included, and gains one sentence (or a bullet of its own right after it): when the delivery is the first after which a person can run the product, it writes the manual of running it, from a fresh clone to the first screen or call, and every later delivery that changes a step updates it.
* Same list, line 108, the next steps bullet: stays whole, and gains at its end, before "The last thing it says", one sentence: these steps are said in the conversation and end with it, and when another agent runs the session on your behalf they may never reach you; what still holds them for the next person is the manual of running it, from the bullet above.
* "`lend-book`, built", after line 161 (the Ninjobs sentence on the environments), one new paragraph of two or three sentences: those next steps are this conversation's; a colleague with a fresh clone next month runs the library from `docs/manuals/run-the-app-from-a-clone.md`, which `skeleton` wrote, being the first delivery after which a person could run the app; `lend-book` changes no step of it, since its migration runs with the `npm run migrate` the manual already gives, so the manual stays as it is, where a delivery that added a step, a service to start or a variable to set, would update it before the review.
* "Review the staged change", after line 186 ("Did the documents the delivery changed get updated, and only those?"), one new question: if this delivery is the first after which the product runs, or changed a step of running it, does the manual of running it say so, so that someone with a fresh clone and nothing else can run it.
* Key points, line 270: after "its last words are your next steps, using what it built first, each command written out," a clause: steps the conversation holds, while the manual of running it, written by the first delivery after which the product runs and updated by each that changes a step, is what lasts.
* Stays: the title, the opening (lines 1 to 5, whose "the documents updated" covers the manuals, as line 68 already says "the documents and manuals"), line 21 and the "fresh session" of line 108, the four numbered next steps (lines 154 to 157), the environment sentence (line 159), "What the team gains", every other sentence.

No docs/03 edit (see the report). No code example: the library's file and commands are written for the chapter, on the lending library.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapters 7, 9, 10 and 12, and the kinds of manual, the Manuals slot and `/analyze`: `ch10-12-run-manual`, which this line follows, so chapter 13's pointer lands on chapter 7 as that delivery leaves it.
* Chapter 8: `ch08-update-2026-10-19-2`. README.md and README.pt.md: `readme-run-manual`.
* Where `/apply`'s fresh session opens with a worktree per delivery: `ch13-19-session-folder` (M25), which also edits chapter 13; this page leaves line 21 and the "fresh session" of line 108 as they are, but adds a sentence to line 108, which that delivery edits on top of.
* Chapter 15's hand test and chapter 19's container manual (line 132): true as they are.
* "What the team gains" in chapter 13: one gain per chapter (docs/04 **One gain**); the manual is a reason said where the doubt is born.
* The kit's changelog case: the book is the kit today, with no before and after (docs/04 **The kit as it is**).

**Decisions from the documents.**

* The rule's wording comes from the kit's Manuals slot and `/apply` file at 2026.10.19.2 (SETUP.md at 44132c4); the `/apply` file's next steps ("use what the delivery changed, as its user would") are unchanged, so chapter 13's numbered steps stay.
* `skeleton` is the library's first line after which a person can run it (chapter 11's queue: "empty app and server, npm run verify, first screenshot"), as `ch10-12-run-manual` also says.
* `npm run migrate` is already the library's command (chapter 13's environment sentence names `npm run migrate -- staging`), so `lend-book` adds no step.
* The manual's name and the scope of chapter 13 only: the driver's decision, aligning with `ch10-12-run-manual`.
* No source note: docs/04 puts a note only where the reader gains something to open.

**Decisions taken alone.**

* The Portuguese phrase "o manual de rodá-lo" / "o manual de rodar o produto", from the kit's README.pt.md, since `ch10-12-run-manual` fixes none.
* Chapter 13's opening stays: line 3's "the documents updated" already covers the manuals, as line 68 does.
* "When another agent runs the session on your behalf" is said as a reason, without the kit's case behind it: the book is the kit today.
* The checklist gains one question, not a rewrite of "Did the documents the delivery changed get updated": running it is the manual a reader most needs and the one no test checks.
* No gain sentence: chapter 13 keeps its one gain.

**Done when.**

* [x] Both editions written, the same passages changed in each, Portuguese read as Portuguese; the chapter opens as it did, no filler and nothing useful cut.
* [x] Every passage the Contract names says what it says; every passage it lists as staying is unchanged.
* [x] `grep -n "run-the-app-from-a-clone" book/en/13-apply.md` and `grep -n "rodar-o-app-de-um-clone" book/pt/13-apply.md` find the file; `grep -c "07-the-documents"` on chapter 13 is unchanged in both editions.
* [x] `git diff --stat` touches no book file but the two chapter 13 files.
* [x] `grep -n -i -E "no longer|now |2026\.10|changelog"` on the added en lines and `grep -n -i -E "não mais|agora |2026\.10|changelog"` on the added pt lines find nothing; no em dash; no narrated run.
* [x] Delivery review by one read-only Opus agent this lane launched, over the two chapter files (Delivery review): narrower than docs/05 §5, which also has it read this page, against the page and docs/04, and keep the session's advisor, which this page does not record.
* [x] `make verify` green after the last edit; `make book` built both editions: the batch's driver ran it after this lane, at `31f510e`, this delivery's commit (exit 0), and `work/done/m23-review.md` records the build at `8a87b0c`, the same `book/`, with both PDF paths.
* [x] Only this delivery's paths and its hunk of docs/06 staged, by the batch's driver from a temporary index at commit time; the page moved to `work/done/` and its commit message suggested.

**What happened.**

* Built as the Contract says, in both editions, at the same lines: line 101 gained the sentence inside the manuals bullet (no bullet of its own); line 108 gained its sentence before "The last thing it says"; a three-sentence paragraph follows the Ninjobs sentence at line 161 (new lines 163 to 165); the checklist gained one question (line 191); Key points gained the clause (line 275). Both editions go from 273 to 278 lines.
* Divergence from the Contract's wording, from the delivery review: line 108 says the manual holds "how to run the product", not "them", since "them" would be the next steps and the manual does not replace those; the `lend-book` paragraph adds "and later deliveries kept current", since `skeleton`'s manual of an empty app could not already give `npm run migrate` alone.
* Checks: both greps find the file at line 164; `07-the-documents` counts 2 in both editions, before and after; `git diff --stat` touches only the two chapter 13 files among book files; the forbidden-words grep on the added lines and the em dash grep find nothing.

**Delivery review.** One read-only Opus agent, launched by this lane, over the two chapter files. Five candidates, all fixed: line 108 antecedent (the manual seemed to hold the next steps), Key points clause in en and pt (a run-on, and "it"/"ele" could read as `/apply`; now "said in the conversation and gone with it" / "ditos na conversa e que acabam com ela", "the product runs" / "o produto roda"), pt checklist question (three "rodá-lo"; now "um passo para rodá-lo" and "rodar o produto"), and the manual's history in the `lend-book` paragraph (`skeleton` wrote it, later deliveries kept it current). No new queue line. `make verify` green after the fixes.

```commit
docs(ch13-apply-run-manual): name the manual of running it in ch 13

- Green is not done: the first runnable delivery writes the manual
  of running it, every step change updates it; next steps end with
  the conversation
- lend-book: the library's manual, written by skeleton, stays as it is
- checklist question and Key points clause on the manual, both editions

work/done/ch13-apply-run-manual.md
```
