# try-before-commit

**Objective.** A reader of chapter 13 uses what a delivery built, as its user would, before committing it, and knows where each thing found goes: what the page asked and the build got wrong is corrected in the same session while the delivery is open, and what the page did not ask becomes the queue's next line, with a draft written while the person still remembers it. Both editions. From the author's reading of the book on 2026-10-18: "Nowhere does the book advise using the software being built before committing each page. On Ninjobs this was essential to find UI/UX and performance problems, or simply to improve what the agent made. Small things were fixed in conversation, because the delivery was still open; more complex ones became new pages at the next position in the queue, using the fresh memory of whoever tested."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *Chapter 13's §Review the staged change is the place, and the only one.* That section is where the person stands between `/apply`'s end and the commit, the moment the draft names. Chapter 6 tells how Ninjobs was born and names the failure each rule answers; using a delivery is a habit of the person, not a rule of the kit, so it has no failure to list there. Chapter 11 owns how a line enters the queue and is not repeated (decision 4). Chapter 15's "Test each clause by hand" runs the whole milestone paragraph end to end when the milestone closes; this is one delivery, while it is open, and the new text says that difference in one clause with no second pointer (chapter 13 already points to chapter 15 at en 13:76). Source: docs/04 §Writing the book, **Say it where the doubt is born** and **Chapter pointers**; en 06:53-66; en 15:28-45.
2. *Page scope, not size, decides between a correction and a line.* The draft says small things were fixed in conversation and complex ones became pages. The book's criterion is the page: what the page asked and the build got wrong or left rough (a button out of place, a label that does not fit, a screen slower than a user waits for) is a correction of this delivery, fixed in the same session, with verify run again and the change recorded on the page; what the page did not ask, however small, becomes a `[ ]` line, and so does a problem that needs a definition of its own. The draft's "improve what the agent made" falls on the first side when the page asked for the thing improved. Source: en 13:71-72 ("A candidate that breaks the page ... is fixed in this session ... Anything else ... becomes a `[ ]` line ..., because the page is the scope"); en 11:151 (an edit made anyway "is reverted"); docs/05 §2 and §3 ("a wrong screen is fixed in a session").
3. *"The next position in the queue" is the person's priority, said as chapter 11 teaches it.* The line is added by conversation, in the same session, which may add a line as any session may; the person asks for it right below this delivery's line, so it is the next free line, because the order is the priority; what the line cannot hold goes into a draft `work/<slug>.md` now, which is where "the fresh memory of whoever tested" lives, so the next `/propose` starts from it. It carries no `· after`, no `[?]`, and does not go above this delivery: the delivery does not need it done first, and a fix the delivery needs first is a correction under decision 2. Source: en 11:74-76, 91, 94-102, 151, 155-156; docs/05 §2 and §4; en 13:43.
4. *Chapter 11 is not touched; `ch11-queue-grows` owns the consequence there.* That page adds to chapter 11 that a problem the person finds trying the product becomes a line by conversation; this delivery owns when and how to try a delivery and where each finding goes, and tells no Ninjobs story in chapter 11. Source: work/ch11-queue-grows.md decision 2; docs/04 §Writing the book, one source per point.
5. *Speed is said as a user feels it.* Chapter 15 says the hand test does not see "a call that takes hundreds of milliseconds"; the author found performance problems by using Ninjobs. The new text names slowness a user waits for, a screen that takes seconds, so chapter 13 does not contradict chapter 15. Source: en 15:42-43; the draft.
6. *The Ninjobs account is the author's, in the first person, with no number.* One or two sentences: I used each delivery before committing it; that is where I found problems of the interface, of how it was to use and of speed that tests and reviews had not shown, and where I improved what the agent made; the small ones fixed in the same conversation, the larger ones written as the next lines of the queue. No count (the author counted none, and docs/04's Evidence rule forbids an uncounted number), no screen, feature, user, server or host named. Source: docs/04 §Writing the book, **Voice** and **Evidence**; docs/03 §Entities and invariants (Ninjobs only through its process artifacts, paraphrased); docs/00 §Cases.
7. *The author's advice, not a step of `/apply`.* The kit's file for `/apply` lists the next steps as reviewing the staged diff, committing and taking the next line; it does not tell the person to use the product. The book says this as the person's practice, in the person's review, and does not add it to the next steps of en 13:92 or 13:134-138. A kit change is out of scope. Source: `.claude/skills/apply/SKILL.md` lines 58-59; docs/04 §Writing the book, **The kit as it is**.
8. *Where the person uses it: the environment `/apply` named.* The text points to the last sentence of `/apply`, which says which environment holds the delivery, so the person tries the version that has it; the Ninjobs sentence at en 13:142, a version reviewed without the delivery, stays as it is and now has a second reason to be read. Source: en 13:92, 140-142.
9. *Opening and key point amended in place, gain unchanged.* Chapter 13's opening has three sentences and its key points five, the limits docs/04 sets, so the opening's second sentence and the fifth key point take the practice in a clause each; no new sentence or bullet. `## What the team gains` stays as it is: one gain, said once. Source: docs/04 §Chapter shape (opening "at most three sentences", key points "at most five bullets"); docs/04 §Writing the book, **One gain**.
10. No new docs/03 term, no new source note, no new queue line, no split.

**Behaviour.**

* The opening of chapter 13, in either edition, says in its second sentence that the reader can then use what `/apply` built, review the staged change against the page and commit it themself; the first and third sentences unchanged; still three sentences.
* In `## Review the staged change` (pt `## Revise a mudança em stage`), after the sentence "Read what happened too, and ask whether you would have decided any divergence otherwise." (en 13:164, pt 13:164) and before "Ask the agent for each correction, in the same session, never by hand." (en/pt 13:165), the reader reads new text, one sentence per line, that says:
  * before you commit, use what the delivery built as its user would, in the environment `/apply`'s last sentence names as holding the delivery, going through what the page changed;
  * why: the tests prove what the page wrote and the review reads the code, and only using it shows whether it looks right, is easy to use and answers without keeping the user waiting; this is one delivery while it is open, where the milestone's hand test runs the whole paragraph when the milestone closes (a clause, no link);
  * what the page asked and the build got wrong or left rough is a correction of this delivery, made while it is open: verify runs again and the page records it (decision 2, its examples); "in the same session" is left to the existing sentence en/pt 13:165, which follows, so it is not said twice;
  * what the page did not ask, however small, or a problem that needs a definition of its own, becomes a `[ ]` line by conversation, with a draft page for what the line cannot hold, and you ask for it right below this delivery's line, so it is the next free line and its `/propose` starts from what you saw while you still remember it (decision 3);
  * the Ninjobs account of decision 6, in the first person.
* The existing sentences en/pt 13:165-166 follow, so "each correction" covers what the review of the diff and the use of the product found.
* The fifth key point, in either edition, adds in a clause that you use what was built before reviewing and committing, and that what the page did not ask becomes the queue's next line; the rest of the key point, automation bias included, unchanged.
* The Portuguese edition says the same in the same places, with docs/03's terms ("entrega", "linha", "fila", "página", "sessão", "rascunho", "em stage"), and Ninjobs takes the article docs/03's `case` row gives when this line is applied.
* Checked at apply time:
  * `git diff book/` shows changes only in chapter 13 of both editions: the opening's second sentence, the new text in `## Review the staged change`, and the fifth key point.
  * The opening still has three sentences and `## Key points` five bullets, in both editions.
  * `grep -c "Ninjobs" book/en/13-apply.md` goes from 2 to 3, and the same in pt.
  * The new text holds no number about Ninjobs.
* Fails: a number about Ninjobs or any Ninjobs detail beyond the account (a screen, a feature, a user, a server); the practice presented as a step of `/apply` or of its next steps; a size rule ("small", "complex") in place of the page's scope; the new line placed above the delivery, marked `[?]` or given `· after`; a `not-but` pattern or another prose rule; a fourth opening sentence or a sixth key point; a change to en/pt 13:165-166, to `## What the team gains`, to chapters 6, 11 or 15; a run narrated; an em dash.

**Contract.**

* Files: `book/en/13-apply.md`, `book/pt/13-apply.md`: the opening's second sentence, new text in `## Review the staged change` (pt `## Revise a mudança em stage`) between lines 164 and 165, the fifth key point.
* Terms of docs/03: none new; `delivery`, `page`, `queue`, `line` as docs/03 has them. Sources: none added. Cases: Ninjobs, the author's own account, no number. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `ch13-teach-the-agent` (a draft at /propose) edits chapter 13's `## Review the staged change` around "Ask the agent for each correction, in the same session, never by hand." (en/pt 13:165-166), to ask for corrections by talking to the agent so it learns. This delivery inserts its text just before that sentence and does not edit it: adjacent hunks, not a conflict (docs/05 §4). Its new text leans on that sentence, so if `ch13-teach-the-agent` rewrites it, the one that lands second reads the other's section first and keeps the two in step: corrections found by use are corrections like the others. If that page also amends the fifth key point, the second to land adds its clause to the key point as the first left it.
* `ch11-queue-grows` edits chapter 11's `### Size and order`; this delivery leaves chapter 11 as it is (decision 4).
* `pt-ninjobs-masculine` changes Ninjobs's article in `book/pt/`, pt 13:142 and 13:222 included, and checks that the count of Ninjobs in `book/pt/` does not change in its own diff (39 at its /propose). This delivery adds one occurrence in pt 13: if it lands first, that page's count is 40 and its new sentence is fixed by that page's check over the whole edition; if it lands second, it writes the masculine that docs/03 then gives.
* `case-a-why-anonymous` and `ch07-talk-not-edit` name chapter 13 but do not edit it.

**Out of scope.**

* A kit change asking `/apply`'s next steps to tell the person to use the product: a suggestion for focus-kit's repository, which the person may add to work/kit-proposals.md; this delivery does not edit that file (decision 7).
* Chapters 6, 11 and 15: decisions 1 and 4.
* `## What the team gains` and key points other than the fifth: decision 9.
* A count of Ninjobs's corrections or lines found by use: none was counted.

**Done when.**

* [ ] Both editions written: the opening's second sentence, the new text and the fifth key point as Behaviour says.
* [ ] Chapter 13 still opens with its value in three sentences, keeps its gain said once and five key points, no filler and nothing useful cut.
* [ ] No new number; the Ninjobs account carries none.
* [ ] `make verify` green: edition parity, prose rules, width, links, disclosure scan, no em dash.
* [ ] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3); the Ninjobs account is the author's own and the author reads it in the review.
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.
