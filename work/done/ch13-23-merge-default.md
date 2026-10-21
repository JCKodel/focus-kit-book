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
* Neighbouring lines on the same files, all later in queue order, which find these sentences as this delivery leaves them: M25's `ch12-14-parallel-token` (chapter 13); and later deliveries of the queue's plan, on where each session opens (chapters 13 and 19), a command typed with several slugs (chapters 13 and 18) and the claim script (chapters 13 and 19). None of them edits these sentences today.

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

* [x] Both editions changed in the sentences the Contract names, and nowhere else in chapters 13, 18, 19 and 23.
* [x] No passage of the four reads as if a person always merges by hand, nor as if the agent commits or merges with no asking and no slot's word.
* [x] Each chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [x] No version, date, before/after or narration of a run in the text; no em dash; no number added, no private case used.
* [x] `make verify` green after the last edit, its result recorded in this page's Proof.
* [x] `make book` built both PDFs: the batch's driver ran it after this lane, at `16fdca6`, this delivery's commit (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapters 18 and 19 (Proof).
* [x] Delivery review by one read-only Opus agent this lane launched, over this delivery's paths (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.

**Proof.**

`git diff HEAD -- book/` shows the eight chapter files only, 12 insertions and 12 deletions: the twelve lines the Contract names, six in each edition; no line added or removed, so no line moved.

`make verify` green after the last edit. The batch's driver ran `make book` at `16fdca6`, this delivery's commit (exit 0); `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapters 18 and 19.

**Divergences.** None.

**Delivery review.** One read-only Opus agent, launched by this lane, over this delivery's paths (`git diff HEAD` of the eight chapter files and this page), against the page, AGENTS.md and docs/04, with the surrounding paragraphs of the four chapters in both editions and chapters 17 :132, 18 :26, 20 :35, 20 :86, 23 :63 and 23 :112. Verdict: no defects; every Contract string in place word for word in both editions, nothing else changed in the four chapters, "by hand" no longer near the merge, one sentence per line kept, no em dash, version, date or run narration added, "pela linha de comando" the book's term.
Notes, outside the Contract, both called wording preferences by the review:
1. Chapter 13 :108 (both editions): the reader's next steps say "commit (and merge, on a delivery branch)" with no "or ask the agent"; the reader's default steps, with no "by hand".
2. Chapter 19 :185 (both editions): "By default, you use the delivery, review and commit on the branch, merge into `main`" has no "or ask the agent to"; it already says "By default", and :145 and :194 give the other ways.
3. Chapter 13 :216, :219, :265 and :276, which Out of scope cites, say what the page claims; :220 and :234 also carry the default for the merge.

**Noted, not fixed.** Notes 1 and 2, wording preferences in the last fix of the milestone's fix round: no queue line.

**Dropped.** Nothing.

```commit
docs(ch13-23-merge-default): say who merges and who reviews in 13-23

- ch13 and ch19: the person reviews the commit or the merge that landed
- ch18: the merge goes through the pull request or the command line
- ch19: by default you merge into main, or ask the agent to
- ch23: by default the person commits or merges, or asks the agent
- both editions

work/done/ch13-23-merge-default.md
```
