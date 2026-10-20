# ch13-23-merge-default

**Objective.** After chapters 13, 18, 19 and 23 the reader can say who brings a delivery into `main` and who reviews what landed: by default a person, who merges or asks the agent to, through a pull request or on the command line; by the Git slot's word the agent, and the person then reviews the commit or the merge, whichever the slot gave it.

**Behaviour.** What the reader can do or explain after the four chapters:

* Read chapter 19's "When a delivery is done" and say who merges it into `main`: by default the reader, or the agent when asked, as chapter 18 :25 says.
* Read chapter 18's branch per delivery and tell the merge's two ways, the pull request or the command line, apart from who takes it, the person or the agent.
* Read chapter 13 :169 and chapter 19 :194 and say that when the Git slot gives the agent the commit and the merge, the person reviews the commit or the merge once it lands.
* Read chapter 19's parallel key point (:351) and say that each commit or merge is reviewed after it lands.
* Read chapter 23's "Who decides each commit and merge" and say that by default the person commits or merges, or asks the agent to take that one step.
* Edge: no passage of the four reads as if a person always merges by hand, nor as if the agent merges with no asking and no slot's word; "by hand" no longer sits beside "asks the agent to" where it could read as the contrast with the agent.
* Edge: the four chapters keep agreeing with chapters 17, 18, 20 and 23 as ch17-23-git-slot-word left them.

**Contract.** Four chapters, same changes in both editions, against the files as they are today (en and pt line numbers match). One sentence per line, as the chapters are laid out; nothing else in the four chapters changes, and no line is added or removed.

* `book/en/13-apply.md` and `book/pt/13-apply.md`, :169:
  * en: "and the person then reviews the commit ([chapter 7]" becomes "and the person then reviews the commit or the merge ([chapter 7]".
  * pt: "e a pessoa então revisa o commit ([capítulo 7]" becomes "e a pessoa então revisa o commit ou o merge ([capítulo 7]".
* `book/en/18-git-essentials.md` and `book/pt/18-git-essentials.md`, :25:
  * en: "through its pull request (chapter 20) or by hand:" becomes "through its pull request (chapter 20) or on the command line:".
  * pt: "pelo pull request do branch (capítulo 20) ou à mão:" becomes "pelo pull request do branch (capítulo 20) ou pela linha de comando:".
* `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`, :103, :194 and :351:
  * en :103: "When a delivery is done, you bring it into `main` from `main/` with a merge commit," becomes "When a delivery is done, by default you bring it into `main` from `main/`, or ask the agent to, with a merge commit,". The rest stays.
  * pt :103: "Quando uma entrega está pronta, você a traz para o `main` a partir de `main/` com um commit de merge," becomes "Quando uma entrega está pronta, por padrão você a traz para o `main` a partir de `main/`, ou pede ao agente que o faça, com um commit de merge,". The rest stays.
  * en :194: "and you then review the commit ([chapter 7]" becomes "and you then review the commit or the merge ([chapter 7]".
  * pt :194: "e você então revisa o commit ([capítulo 7]" becomes "e você então revisa o commit ou o merge ([capítulo 7]".
  * en :351: "with each commit reviewed after it lands." becomes "with each commit or merge reviewed after it lands.".
  * pt :351: "com cada commit revisado depois que entra." becomes "com cada commit ou merge revisado depois que entra.".
* `book/en/23-adoption.md` and `book/pt/23-adoption.md`, :64:
  * en: "then commits or asks the agent to take that one step," becomes "then commits or merges, or asks the agent to take that one step,". The rest stays.
  * pt: "depois faz o commit ou pede ao agente que dê esse único passo," becomes "depois faz o commit ou o merge, ou pede ao agente que dê esse único passo,". The rest stays.
* Terms of docs/03: Git slot, trunk, branch, worktree, the person's review. No new term; no docs/03 row.
* Sources: chapter 18 :25 and :26 (the default merge, asked of the agent), chapter 20 :35 and :86 (the slot's word, the merge included), chapter 23 :64's second half and :112 (the commit or the merge reviewed), docs/05 §5's Git slot and AGENTS.md ("It never commits or merges on its own"). No footnote: the reader gains nothing to open.
* Cases: none. No number.
* Neighbouring lines on the same files, all later in queue order, which find these sentences as this delivery leaves them: M24's `ch12-14-parallel-token` (chapter 13); M25's `ch13-19-session-folder` (chapters 13 and 19); M27's `ch12-14-18-several-slugs` (chapters 13 and 18); M28's `ch13-19-claim-script` (chapters 13 and 19). None of them edits these sentences today.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 19 :99, "the commit you make there": an example inside a list, not a finding; :145 and :194 already give the default and the slot's word.
* Chapter 18 :26 and its code block: the default path, kept by ch17-23-git-slot-word.
* Chapter 13 :216, :219, :265 and :276, chapter 17, chapter 20 and chapter 23 :63 and :112: already carry the default and the slot's word.
* Any version, date or history of the kit's rule.

**Decisions from the documents.**

* By default the agent stages and stops; the person commits or merges, or asks the agent to take that one step: AGENTS.md, docs/05 §5's Git slot, chapter 18 :25.
* A Git slot may give the agent the commit and the merge by its word, which counts as the asking, and the person reviews what landed: chapter 13 :169, chapter 20 :35 and :86, chapter 23 :64.
* Findings 2 to 5 of the Delivery review in `work/done/ch17-23-git-slot-word.md`, each named "a queue line" there; this delivery is that line.
* The wording follows ch17-23-git-slot-word's: "by default", "or asks the agent to", "reviews the commit or the merge", "por padrão", "ou pede ao agente que o faça", "revisa o commit ou o merge" (chapter 18 en/pt :25, chapter 23 en/pt :64).
* Taught as the kit is today, with no version or "now": AGENTS.md and the M21 rule.

**Decisions taken alone.**

* Chapter 19 :103 takes "or ask the agent to" with "by default", as chapter 18 :25 and chapter 19 :145 do; the slot's word stays in :194, later in the same chapter, so :103 does not repeat it.
* Chapter 19 :351 keeps "every commit stays your decision" and only widens the review clause to "each commit or merge": the line names the review, and the sentence's subject is the batch's commits.
* "On the command line" in Portuguese is "pela linha de comando", the book's term (chapter 4 pt :125, chapter 19 pt :60).
* Chapter 23 :64 reads "commits or merges, or asks", the review's own suggestion (finding 5).
* No record page is edited: the findings come from ch17-23-git-slot-word's Delivery review, not from `work/done/m23-review.md`, and that record already names them as queue lines.
* The queue line keeps its wording.

**Done when.**

* [ ] Both editions changed in the sentences the Contract names, and nowhere else in chapters 13, 18, 19 and 23.
* [ ] No passage of the four reads as if a person always merges by hand, nor as if the agent commits or merges with no asking and no slot's word.
* [ ] Each chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [ ] No version, date, before/after or narration of a run in the text; no em dash; no number added, no private case used.
* [ ] `make verify` green after the last edit, its result recorded in this page's Proof.
* [ ] `make book` built both PDFs, its run and both PDF paths recorded in this page's Proof; when a batch's driver runs it instead, this item is ticked only on that run as the Proof records it.
* [ ] The Delivery review as docs/05 §5 says, recorded on this page with who read what.
