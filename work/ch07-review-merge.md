# ch07-review-merge

**Objective.** After chapter 7 the reader can say what the person reviews when the Git slot gives the agent the commit and the merge: the commit or the merge, whichever landed, as chapter 13 :169 says citing chapter 7.

**Behaviour.** What the reader can do or explain after the chapter:

* Read chapter 7's git strategy and say that by default the agent stages and never commits or merges on its own, and that asked, it takes the step the person names.
* Read the next sentence and say that when the Git slot says the agent commits, and merges, by its word, the person reviews the commit or the merge once it lands.
* Follow chapter 13 :169's link to chapter 7 and find the same review there: "the commit or the merge" in both chapters, in both editions.
* Edge: no sentence of chapter 7 reads as if the person reviews only the commit while the agent also merges.
* Edge: chapter 7 keeps agreeing with chapters 13, 19 and 23 as ch13-23-merge-default left them.

**Contract.** One chapter, same change in both editions, against the files as they are today. One sentence per line, as the chapter is laid out; nothing else in chapter 7 changes, and no line is added or removed.

* `book/en/07-the-documents.md` :82: "which counts as the asking; the person then reviews the commit." becomes "which counts as the asking; the person then reviews the commit or the merge.".
* `book/pt/07-the-documents.md` :83: "que vale como o pedido; a pessoa revisa o commit." becomes "que vale como o pedido; a pessoa então revisa o commit ou o merge.".
* Terms of docs/03: Git slot, the person's review. No new term; no docs/03 row.
* Sources: chapter 13 en/pt :169 and chapter 19 en/pt :194 ("reviews the commit or the merge", "revisa o commit ou o merge"), chapter 23 en/pt :64, AGENTS.md ("It never commits or merges on its own"). No footnote: the reader gains nothing to open.
* Cases: none. No number.
* Neighbouring lines on the same files: none. The lines proposed beside this one, ch08-23-fetch-taken (chapters 8, 13, 14, 17 and 23) and ch18-19-fetch-resume (chapters 18 and 19), do not touch chapter 7; no other open line in docs/06 names it.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 7 :81, the default sentence: it already names the commit and the merge.
* Chapters 13, 17, 19 and 23: already carry the review of the commit or the merge (ch13-23-merge-default, ch17-23-git-slot-word).
* The record page `work/done/m24-review.md`: it names D1 as this line already; no edit.

**Decisions from the documents.**

* Finding D1 of `work/done/m24-review.md`: chapter 7 :82 (pt :83) says the person "reviews the commit" after the slot lets the agent merge; chapter 13 :169, citing chapter 7, says "the commit or the merge".
* The wording is chapter 13 :169's and ch13-23-merge-default's: "the person then reviews the commit or the merge", "a pessoa então revisa o commit ou o merge".
* Taught as the kit is today, with no version or "now": AGENTS.md.

**Decisions taken alone.**

* The pt sentence also takes "então", which chapter 13 pt :169 has and en :82 already carries as "then"; the two editions then say the same.
* No sibling sentence widens the scope: chapter 7 has no other sentence on the slot's review.
* The queue line keeps its wording.

**Done when.**

* [ ] Both editions changed in the sentence the Contract names, and nowhere else in chapter 7.
* [ ] No sentence of chapter 7 reads as if the person reviews only the commit while the agent also merges.
* [ ] The chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [ ] No version, date, before/after or narration of a run in the text; no em dash; no number added, no private case used.
* [ ] `make verify` green after the last edit, its result recorded in this page's Proof.
* [ ] `make book` built both PDFs, its run and both PDF paths recorded in this page's Proof; when a batch's driver runs it instead, this item is ticked only on that run as the Proof records it.
* [ ] The Delivery review as docs/05 §5 says, recorded on this page with who read what.

**Proof.**

**Divergences.**

**Delivery review.**

```commit
docs(ch07-review-merge): the person reviews the commit or the merge in 7

- ch07: under the Git slot's word, the review names the merge too
- both editions

work/done/ch07-review-merge.md
```
