# ch13-short-lines

**Objective.** After chapter 13 a reader writes a queue line as the mark, the slug, one sentence and its suffixes, knows that what happened goes on the page because `/propose` reads the whole queue, and knows that a change asked outside `/apply` may continue as `/propose <slug>` in the same session when they want it defined now, so what was said becomes the page instead of growing the line. Both as focus-kit 2026.10.16 says.

**Behaviour.**

* (The reader's own line, not printed in the chapter.) A reader writing the line for "a member can renew a loan once, for 21 more days" writes `[ ] renew-loan   a member renews a loan once · after lend-book`: one sentence after the slug, the suffix kept. From chapter 13 they know the 21 days, the refusal when the copy is reserved, and why, go on the page.
* Failure: a line that reads "a member renews a loan once; we chose 21 days because the librarian asked, and a reserved copy is refused, see the meeting" is two sentences and carries decisions. The reader knows from chapter 13 that it is a page's content in the wrong place, and that every `/propose` reads it.
* Failure: after `return-book` is `[x]`, a reader who appends "done, the fine rule was dropped" to its line knows that what happened goes on the page in `work/done/`, and the line only changes mark.
* Edge: a line shortened until it no longer says which chapter, screen or file it touches is too short: the sentence keeps what the delivery gives (chapter 13 keeps the existing example lines as models).
* Edge: `· after <slug>` and, from chapter 16, `· resume:` and `· blocked:` are suffixes, not a second sentence; the rule leaves them.
* A reader asks the agent, in an ordinary session, for the due date as day/month/year and adds "and I want it defined now". From chapter 13 they expect the agent to add `[ ] due-date-format`, say so, and continue as `/propose due-date-format` in the same session: the line becomes `[~]`, and what was said becomes the page, with no file of the app changed.
* Without "now", the answer is the one chapter 13 already teaches: the line, and the answer stops there.
* Failure: an agent that, asked to define it now, writes the format rules, the screens and the edge cases into the queue line instead of a page. The reader knows the detail had nowhere to go but the line only before this rule, and asks for the page.
* A reader of chapter 19 who reads that a code change asked by the manager becomes a line finds the same choice: the answer stops there, or continues as `/propose` when they want it defined now.

**Contract.**

* **Chapter 13, both editions, file name, title and headings kept.**
  1. Opening, second sentence: the reader can also write a line as one sentence with its suffixes, and continue a request as `/propose` in the same session.
  2. "The line": "A line has three parts, a mark, a slug and what the delivery gives, in one line" becomes the mark, the slug, one sentence of what it gives, and its suffixes, such as `· after <slug>`; the template block reads `<what it delivers, one sentence>`. "The kit asks for one line, and the reasoning goes on the page" becomes one sentence, with what happened on the page, because `/propose` reads the whole queue: every word on a line is read by every definition. The Ninjobs sentence and the "decision in the wrong place" sentence stay.
  3. "The marks", the paragraph after "A line never leaves the queue": it changes mark and keeps its sentence; what happened is on the page behind `[x]`.
  4. "Changing the queue", after the `due-date-format` block and its first sentence: when you want the change defined now, say so, and the conversation continues as `/propose due-date-format` in the same session, the line goes `[~]`, and what was said becomes the page (chapter 14 in plain text: "The line" already links it). The paragraph's later sentences stay.
  5. "What the team gains", after the 2026.10.06.1 sentences: the kit's changelog, entry 2026.10.16, paraphrased, no note: in one project the request lines grew to 4.7 KB, because the detail of a request had nowhere to go but the line, and every session read them; since then the line holds one sentence and the detail goes to a page, in the same session if the person wants. Then this book's own queue: when it moved to 2026.10.16, 61 of its 150 lines were over 200 characters and the longest 639; after, 12 and 223. Note `[^short-lines]`, pointing to `work/done/kit-2026-10-16.md` in the book's repository, where the count is recorded.
  6. Key points: the docs/06 point reads "a mark, a slug, one sentence and its suffixes; what happened goes on the page"; the last point gains "or continues as `/propose` in the same session when you want it defined now".
* **Chapter 19, both editions:** the sentence "A change to the code, however small, becomes a line as well (chapter 13), and the answer stops there." gains ", or continues as `/propose` in the same session when the manager wants it defined now". Nothing else in chapter 19 changes.
* **Portuguese:** `due-date-format` stays `formato-devolucao` as chapters 13 and 19 already have it; "uma frase" for one sentence, "sufixos" for suffixes; `· after`, `· resume:` and `· blocked:` stay in English (chapter 13 already says so).
* **Terms:** queue line, mark, suffix, page, free line, as docs/03 has them (`queue line` added by `kit-2026-10-16`); docs/03 unchanged.
* **Sources:** the kit's CHANGELOG, entry 2026.10.16, paraphrased with no note (docs/04, the 2026.10.08.3 and 2026.10.06.1 paragraphs beside it); this book's `work/done/kit-2026-10-16.md` for the before and after counts, with a note, since the reader can open it (docs/04, the `[^queue-m12]` precedent).
* **Cases:** none new. Case A is not counted here: its measured context belongs to `ch15-24-apply-reads`.
* **Code examples:** the template line and the `due-date-format` line already in the chapter, written for it on the lending library; no transcript of the continuation, which is told in prose (ADR-0017).

**Out of scope.**

* `/apply` reading only its queue lines, and Case A's 180 KB: `ch15-24-apply-reads`.
* Slots and manuals: `ch10-12-slots-manuals`.
* Chapter 14's own account of `/propose`: the continuation starts `/propose` as chapter 14 already teaches it; chapter 13 points there.
* Chapter 16's suffixes and marks: unchanged; they are already suffixes.
* docs/05, docs/03, AGENTS.md: `kit-2026-10-16` already holds both rules.
* A new count or run: the changelog and the recorded count are the evidence (ADR-0017).

**Done when.**

* [x] Chapters 13 and 19 changed in both editions, same headings; chapter 13 still opens with its value; no filler and nothing useful cut.
* [x] No sentence in the book says a line holds more than one sentence plus suffixes, or that a code change asked outside `/apply` can only stop at the line.
* [x] Changelog entry 2026.10.16 paraphrased and checked against the kit's CHANGELOG; the counts checked against `work/done/kit-2026-10-16.md` and docs/06 at the commits before and at `kit-2026-10-16`.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Trunk, no branch: docs/05 §5 Git.
* The rule's wording, "the mark, the slug, one sentence and its suffixes; what happened goes on the page, because /propose reads the whole queue": docs/05 §4 and docs/03's `queue line` row.
* The continuation's wording, "when the person wants it defined now, the conversation continues as /propose <slug> in the same session, and what was said becomes the page": docs/05 §2.
* Changelog paraphrased with no note, the book's own count with one: docs/04 and the precedents in chapter 13.
* Evidence, the changelog plus this book's queue before and after (asked; the author chose).
* Chapter 19's sentence adjusted here so no chapter contradicts chapter 13 (asked; the author chose).
* The 4.7 KB lines are the kit's evidence, "one project", with no attribution: the changelog does not name it, and naming a project's own measurement is `ch15-24-apply-reads`'s, for Case A.
* Other chapters checked: chapters 9, 10, 12 and 19 say "one line per delivery", still true; chapters 2, 11, 14 and 15 put `/apply` in a fresh session and say nothing that keeps `/propose` from continuing a session. None changes.

**What happened.**

* Chapter 13, both editions: the opening's second sentence gains writing a line as one sentence with its suffixes and continuing a request as `/propose`; "The line" says the mark, the slug, one sentence and its suffixes, the template reads `<what it delivers, one sentence>`, and "The kit asks for one sentence" gives the reason, `/propose` reading the whole queue; "The marks" keeps the sentence on the line and what happened on the page; "Changing the queue" gains the continuation as `/propose due-date-format` (pt `formato-devolucao`); the gain gains entry 2026.10.16 and the book's own count with `[^short-lines]`; both key points changed as the contract says.
* Chapter 19, both editions: the one sentence gains the continuation; nothing else changed.
* Divergence: in the gain, the existing sentence "This book's own queue shows `· after` at work" now opens "The same queue shows", since the sentence before it already names the book's queue. Its content is unchanged.
* Changelog checked: the kit's CHANGELOG entry 2026.10.16 says the request lines grew to 4.7KB "because the detail of a request had nowhere to go but the line", and that the conversation continues as `/propose <slug>` in the same session when the person wants it defined now. It also gives the project's 180KB read by every `/apply`, left to `ch15-24-apply-reads` as the page says.
* Counts checked: `work/done/kit-2026-10-16.md` records 150 queue lines, 61 over 200 characters, the longest 639, before; 12 and 223 after. docs/06 at the commit before `kit-2026-10-16` has 143 lines, 61 over 200, the longest 639: the seven M13 lines its /propose added were in the tree and not yet committed, all under 200. At `kit-2026-10-16`, 150 lines, 12 over 200, the longest 223 (counted in characters; a byte count gives 224, since `·` is two bytes). The chapter uses the recorded 150, the queue as it moved.
* Other chapters searched for "one line" and "the answer stops there": no other sentence says a line holds more than one sentence or that a request can only stop at the line.
* Proof: `make verify` is red at links only: the note's URL, `work/done/kit-2026-10-16.md` on GitHub, answers 404 in both editions, since `main` is three commits ahead of `origin/main` and the commit of `kit-2026-10-16` is not pushed. The author chose to push; at the end of this session the push had not arrived. `make book` built both editions' PDF and EPUB.
* Blocked: `resume: apply`. After the push, a fresh `/apply ch13-short-lines` runs `make verify`, ticks the last two Done when items, moves the page to `work/done/`, marks the line `[x]` and stages.

* Resumed after the push: `main` matches `origin/main`, the note's URL answers, and `make verify` is green, links included. `make book` built both editions' PDF and EPUB again. The blocked suffixes are removed and the line is `[x]`.

```commit
docs(ch13-short-lines): teach one-sentence queue lines

- Chapter 13: a line is mark, slug, one sentence and suffixes
- Chapter 13: a request may continue as /propose in the same session
- Chapter 13: changelog 2026.10.16 and the book's queue counts
- Chapter 19: the code-change sentence gains the continuation

work/done/ch13-short-lines.md
```
