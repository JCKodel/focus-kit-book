# ch11-unticked-item

**Objective.** The reader of chapter 11 knows why the skeleton page was committed with its `npm run dev` item unticked, and that on their own page an item is ticked, with how it was checked, before the commit.

**Behaviour.**

* Right after the review's diff, before "Then I committed", the chapter says that the review left one thing uncorrected: the Done when item "`npm run dev` leaves client and server running locally" is still unticked in the committed page, although the author had checked it by hand after the run.
* It says this was a lapse: the author should have asked the agent, in the same session, to tick the item and to write on the page how it was checked; the author did not, and the published tag does not move.
* It tells the reader what to do on theirs: before committing, ask for that tick and that line, so the answer to "Is every Done when item ticked, and is each one true?" is yes.
* The review question itself and the rest of the chapter stay as they are.
* The Portuguese says the same in the same place.
* Finding F15 of the M3 review is settled.

**Contract.**

* Files: `book/en/11-apply.md`, between line 342 ("Nothing in the code changed…") and line 343 ("Then I committed…") today; `book/pt/11-apply.md`, between lines 349 and 350 today.
* A few sentences, no new section, list or code block. Line 234 ("The item … was mine, not the run's") is not repeated: the new text only adds why the tick is missing and what the reader does instead.
* Fact it rests on: `work/done/skeleton.md` at the clinic's tag `book-v1/apply` shows `* [x] npm run dev leaves client and server running locally`; the tag is already linked at line 235.
* Sources: the existing `[^apply-run]` note, if a citation is needed; no new note. Terms of docs/03, cases, exercises: unchanged.

**Out of scope.**

* Ticking the item in the clinic: `book-v1/apply` is published and a published tag never moves (docs/05).
* Changing the review question to allow an unticked item: the kit says to tick every item, and the lapse is the author's, not the rule's.
* An exercise about it: Exercise 11.2 already has the reader review and commit.

**Done when.**

* [x] Both editions say, after the diff, that the item stayed unticked, that it was a lapse, and what the reader asks for instead.
* [x] Line 234 and the review question unchanged in both editions.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Built as planned: three sentences after "Nothing in the code changed…" in both editions, no new section, list, code block or note. Line 234 and the review question are untouched.
* Nothing diverged and nothing was dropped. No note was cited: the tag is linked two paragraphs above, and the new text only states a fact of the committed page.
* Proof: `make verify` green; `make book` built both PDFs.
* Finding F15 of the M3 review is settled. No document other than the chapter and docs/06 changed; no ADR.
