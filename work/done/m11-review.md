# m11-review

**Objective.** The author knows, clause by clause, whether M11's paragraph holds in the hands of a reader of the book, in both editions; every clause that fails is a `[ ]` line in M11 under this review.

**Decided by the author.**
1. As in `m9-review` and `m10-review`, and as docs/05 §8 says: the person tests alone; no fresh session reads the chapters as a reader and no agent proposes findings. The agent prepares, records and writes the lines.

**Behaviour.**

* The author receives both PDFs (`make book`), the page where each passage below starts in each PDF, and the clause table, and tests each clause by reading the passages it names, in English and then in Portuguese.
* For each clause the author answers, in the conversation, `C<n>: holds` or `C<n>: fails, <what the reader does not get>`; a clause that fails in the author's hands is a finding, with nothing to confirm or reject afterwards.
* Each finding becomes one `[ ]` line in M11, under `m11-review`, saying what will be true, never how to fix it; written by the agent from the author's words, shown to the author before it is staged. No M11.1.
* A defect the author finds outside the clause table (as the two PDF defects in `m10-review`) becomes a line the same way, when the author asks for it.
* No finding: M11 closes with this delivery; the page says so.
* No file under `book/` and no document but docs/06 and this page is edited by this delivery.

**Contract.**

The clause table, what the author tests (M11's paragraph, quoted: "When this milestone closes, a reader who hears that the page needs the whole answer before the work starts, that the method needs FOCUS, or that a person who commits after nine good deliveries stops reading finds the book's answer where the doubt arises: exploring is a conversation with the agent before any page, the method works with any of the three architectures, and the review of chapter 15 is the defence against automation bias."):

| | Clause | Answered by | Passage (en and pt, same lines) | How the author tests it |
|---|---|---|---|---|
| C1 | the page needs the whole answer before the work starts → exploring is a conversation with the agent before any page | critique-fixes | 14, opening (lines 3 and 4); §When you do not know yet (lines 118 to 125); Key points | A reader who does not know yet what the delivery is: can they say what to do (talk to the agent, in any session, before any page), the three ways it ends (a queue line, a decision written where it belongs, `/propose` in the same session), and why no mark, command or kind of delivery is added? Is the answer met where the doubt arises, at the end of §When it does not fit? |
| C2 | the method needs FOCUS → it works with any of the three architectures | critique-fixes | 10 §The two choices (lines 43 to 60, the sentences at 49 to 51); Key points | A reader whose project will not use FOCUS: can they say what still works (the page, the queue, the documents, verify, the commit) and what FOCUS adds, and does that match what chapters 6 and 8 say? |
| C3 | a person who commits after nine good deliveries stops reading → the review of chapter 15 is the defence against automation bias | critique-fixes | 15 §Review the staged change (lines 85 to 106, the paragraph at 101); Key points (line 157); 26 §Why the first answer feels final (line 31), where the bias is defined | Can a reader say what automation bias is, that chapter 26 defines and measures it, and how each of the four parts of the review counters it? Does chapter 15 add no number that chapter 26 does not hold? |

Line numbers are those of `book/<edition>/NN-*.md` at the start of this delivery; the PDF pages are given by /apply from `make book`.

The finding line, in docs/06 under M11:

```
[x] m11-review               the review of M11 as docs/05 §8 says
[ ] <slug>                   <what will be true>
```

docs/06: `m11-review` `[>]` now, `[*]` when /apply starts, `[x]` by /apply; its description stays.

docs/03, docs/05: no change.

**Out of scope.**

* Fixing any finding: each is its own line.
* Chapters other than 10, 14 and 15, save chapter 26's definition that C3 reads: M11 changed only those three.
* The rest of chapters 10, 14 and 15: `critique-fixes` changed nothing beyond its Contract; a finding only if the author says a clause fails on it.
* An agent's reading as support: decision 1.

**Done when.**

* [x] `make book` run; both PDF paths given to the author with the clause table and the page where each passage starts in each edition.
* [x] C1 to C3 each answered by the author, recorded under What happened in the author's words.
* [x] Each failed clause a `[ ]` line in M11 under `m11-review`, approved by the author; or the page says there was none.
* [x] No file under `book/` changed.
* [x] `make verify` green, disclosure scan included.
* [x] Page in `work/done/`, `m11-review` `[x]`, staged, commit message suggested.

**What happened.**

* `make book` run; the author got both PDFs, the clause table and the page where each passage starts in each edition (chapter 14 at p. 96 in English and p. 100 in Portuguese; chapter 10's §The two choices at p. 73 and p. 77; chapter 15's §Review the staged change at p. 107 and p. 112; chapter 26's §Why the first answer feels final at p. 175 and p. 184).
* The author's answer, in their words: "All holds".
  * C1: holds. C2: holds. C3: holds.
* No clause failed and the author named no defect outside the clause table: no finding, no line added. M11 closes with this delivery; no M11.1.
* Nothing diverged from the plan. No file under `book/` changed; no ADR.
