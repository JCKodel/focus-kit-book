# ch17-23-git-slot-word

**Objective.** After chapters 17, 18, 19 and 23 the reader can say who takes each commit and merge: by default a person, who reviews and then commits or merges, or asks the agent to; when the Git slot's word lets the agent commit and merge, the agent takes that step and the person reviews the commit or the merge once it lands, as chapter 20 says.

**Behaviour.** What the reader can do or explain after the four chapters:

* Read chapter 17's queue change by a manager and say who commits it: by default a person, after reviewing it, or the agent when asked; by the Git slot's word, the agent, and the person reviews the commit.
* Read chapter 18's branch per delivery and say who merges it into `main`: by default the person, or the agent when asked; by the Git slot's word, the agent, and the person reviews the merge after it lands.
* Read chapter 19's work inside a worktree and say the same of its commit.
* Read chapter 23's roles and key points and say that the Git slot's word may give the agent the merge as well as the commit, and that the person then reviews either once it lands.
* Edge: no passage of the four reads as if a person always commits or merges by hand, nor as if the agent ever commits or merges on its own, with no asking and no slot's word.
* Edge: the sentences that already say it (chapter 18 :190 and :203, chapter 19 :194 and :351, chapter 23 :63's first sentence) stay as they are, and the four chapters agree with chapters 13 and 20.

**Contract.** Four chapters, same changes in both editions, against the files as they are today (en and pt line numbers match). One sentence per line, as the chapters are laid out; nothing else in the four chapters changes.

* `book/en/17-project-as-assistant.md` and `book/pt/17-project-as-assistant.md`, the manager's change (:137):
  * en: "and a person reviews and commits it." becomes "and a person reviews it and commits it, by default, or asks the agent to; when the Git slot's word lets the agent commit, the person reviews the commit once it lands."
  * pt: "e uma pessoa revisa e faz o commit." becomes "e uma pessoa a revisa e faz o commit, por padrão, ou pede ao agente que o faça; quando a palavra do slot Git deixa o agente fazer o commit, a pessoa revisa o commit depois que ele entra."
  * The start of the sentence stays.
* `book/en/18-git-essentials.md` and `book/pt/18-git-essentials.md`, the kit's branch per delivery (:25), then one new line after it:
  * en :25: "and the person merges page and build into `main` in one merge, here a merge commit," becomes "and by default the person merges page and build into `main`, or asks the agent to, in one merge, here a merge commit,". The rest of the sentence stays, the closing "the unit of work one `git revert -m 1 <merge>` takes back" included.
  * pt :25: "e a pessoa faz o merge da página e da construção no `main` em um merge, aqui um commit de merge," becomes "e por padrão a pessoa faz o merge da página e da construção no `main`, ou pede ao agente que o faça, em um merge, aqui um commit de merge,". The rest stays.
  * New line after :25, en: "When the Git slot's word lets the agent merge, the agent takes that step and the person reviews the merge once it lands (chapter 20)."
  * New line after :25, pt: "Quando a palavra do slot Git deixa o agente fazer o merge, o agente dá esse passo e a pessoa revisa o merge depois que ele entra (capítulo 20)."
  * :26 and the code block under it stay: they walk through the default path (Decisions taken alone).
* `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`, working inside the folder (:145):
  * en: "you use what it built, review and commit there." becomes "you use what it built, review it and, by default, commit there, or ask the agent to; by the Git slot's word the agent commits there and you review the commit."
  * pt: "você usa o que ele construiu, revisa e faz o commit ali." becomes "você usa o que ele construiu, revisa e, por padrão, faz o commit ali, ou pede ao agente que o faça; pela palavra do slot Git o agente faz o commit ali e você revisa o commit."
* `book/en/23-adoption.md` and `book/pt/23-adoption.md`, "Who decides each commit and merge" (:64) and the key points (:112):
  * en :64: "by the Git slot's word, the agent commits and the person uses the delivery and reviews the commit:" becomes "by the Git slot's word, the agent commits, and merges, and the person uses the delivery and reviews the commit or the merge:". The rest stays.
  * pt :64: "pela palavra do slot Git, o agente faz o commit e a pessoa usa a entrega e revisa o commit:" becomes "pela palavra do slot Git, o agente faz o commit, e o merge, e a pessoa usa a entrega e revisa o commit ou o merge:". The rest stays.
  * en :112: "then reviewing each commit after it lands," becomes "then reviewing each commit and merge after it lands,".
  * pt :112: "revisando depois cada commit que entra," becomes "revisando depois cada commit e cada merge que entra,".
* Terms of docs/03: Git slot, trunk, branch, worktree, the person's review. No new term; no docs/03 row.
* Sources: chapter 20 :8, :35, :85 and :86 (the reviewer by default and by the Git slot's word, the merge included), chapter 13 :169, docs/05 §5's Git slot and AGENTS.md ("The agent stages and suggests the commit message. It never commits or merges on its own"). No footnote: the reader gains nothing to open.
* Cases: none. No number.
* Neighbouring lines on the same files, applied after this one in queue order, which find these sentences as this delivery leaves them: `ch17-next-free-line` (M23, chapter 17 :124 to :128, not :137); M24's `ch12-14-17-20-branch-claim` (chapter 17); M25's `ch13-19-session-folder` (chapter 19); M27's `ch12-14-18-several-slugs` (chapter 18); M28's `ch13-19-claim-script` (chapter 19). None of them edits these sentences today.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Sentences that already carry the default and the slot's word: chapter 18 :190 and :203, chapter 19 :194 and :351, chapter 23 :63's first sentence, chapter 13 :169, :216, :219, :265 and :276; they are the rule these four lag.
* Chapter 20: the source of the wording, not a target.
* Chapter 13 :169's "the person then reviews the commit" for a slot that gives the merge too: no finding names it; not widened.
* D3 and D5, summaries pointing to chapters 14 and 17: dropped weak by the review.
* D7, chapter 17's next free line: `ch17-next-free-line`.
* Any version, date or history of the kit's rule.

**Decisions from the documents.**

* By default the agent stages and stops; the person commits or merges, or asks the agent to take that one step: AGENTS.md, docs/05 §5's Git slot, chapter 13 :169 and :216.
* A Git slot may say the agent commits, and merges, by its word, which counts as the asking, and the person then reviews what landed: chapter 13 :169, chapter 18 :190, chapter 20 :35 and :86.
* Finding ids D2 and D6, seen, low: `work/done/m23-review.md`.
* Taught as the kit is today, with no version or "now": AGENTS.md and the M21 rule.

**Decisions taken alone.**

* Chapter 18 :26 and its code block stay: "the last two are yours" describes the default path the example walks, and the new line just above says when the slot changes it.
* The slot's case in chapter 18 is a new line, not a clause of :25, which already carries the branch, the page, the marks, the board pointer and the revert.
* Chapter 17 names only the commit: the manager's change is a commit, whatever the strategy; the merge of a branch is chapter 18's and 23's.
* The Portuguese reuses the book's phrases: "por padrão", "pela palavra do slot Git", "pede ao agente que o faça", "revisa o commit depois que ele entra" (chapter 13 pt :265, chapter 20 pt :35, chapter 23 pt :64).
* The queue line keeps its wording.

**Done when.**

* [x] Both editions changed in the sentences the Contract names, chapter 18's one new line included, and nowhere else in chapters 17, 18, 19 and 23.
* [x] No passage of the four reads as if a person always commits or merges by hand, nor as if the agent commits or merges with no asking and no slot's word.
* [x] Each chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [x] No version, date, before/after or narration of a run in the text; no em dash; no number added, no private case used.
* [x] `make verify` green after the last edit, its result recorded in this page's Proof.
* [x] `make book` built both PDFs, its run and both PDF paths recorded in this page's Proof; when a batch's driver runs it instead, this item is ticked only on that run as the Proof records it.
* [x] The Delivery review as docs/05 §5 says, recorded on this page with who read what.

**Proof.**

`git diff HEAD -- book/` shows the eight chapter files only, 12 insertions and 10 deletions: ten edited lines and chapter 18's new line in each edition.
Chapter 18's new line moves the sentences that stay: chapter 18 :190 and :203 are now :191 and :204; chapter 19 :194 and :351 and chapter 23 :63 have not moved.

`make verify` green after the last edit. `make book` is run by the driver once for the batch.

**Divergences.**

* pt 23 :112 ends "que entra", singular, not the Contract's "que entram": with "cada" before each subject the verb stays singular, as the English "after it lands"; the Contract line is corrected to match (Delivery review finding 1).

**Decisions.**

* The four review findings outside the page go to the queue as lines of their own, not widened here.

**Delivery review.** One read-only Opus agent over this delivery's paths (`git diff HEAD` of the eight chapter files, word diff, and this page), against the page, AGENTS.md, docs/04, docs/05 §5, chapter 20 en/pt :8, :35, :85, :86, chapter 13 en/pt :169, :216, :265, and the neighbouring lines of chapters 18 and 19; it did not read docs/03, since the page adds no term. Verdict: passes; every Contract string in place word for word in both editions, nothing else changed in the four chapters, one sentence per line kept, the wording agrees with chapters 13 and 20, no em dash, number, private case, version, date or run narration added.
Findings:
1. Text written, minor: pt 23 :112 "que entram" reads better singular after "cada ... e cada ...". Fixed: "que entra", the Contract corrected.
2. Outside the page: chapter 19 :103 (both editions), "When a delivery is done, you bring it into `main` from `main/` with a merge commit", says who merges with no "by default" or slot's word. A queue line.
3. Outside the page: chapter 18 :25 (both editions), "or by hand" after "or asks the agent to" now also reads as a contrast with the agent; "or on the command line" would keep it the pull request's contrast. A queue line.
4. Outside the page, already named in Out of scope: chapter 13 :169 and chapter 19 :194 and :351 say the person reviews "the commit" where the slot may give the merge too. A queue line.
5. Outside the page, low: chapter 23 :64's default half names only the commit under a heading on each commit and merge; "then commits or merges, or asks the agent to take that one step". A queue line.

**Noted, not fixed.** Findings 2 to 5, queue lines of their own.

**Dropped.** Nothing.

```commit
docs(ch17-23-git-slot-word): say who commits and merges in 17-23

- ch17 and ch19: a person commits by default, or asks the agent to
- ch18: the person merges by default; a new line gives the slot's case
- ch23: the Git slot's word may give the agent the merge as well
- both editions

work/done/ch17-23-git-slot-word.md
```
