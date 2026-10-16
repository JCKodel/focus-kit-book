# ch15-24-apply-reads

**Objective.** After chapters 15 and 24 the reader can say what `/apply` reads in docs/06, only the lines naming its slug and their milestone heading, and why the queue is the one document it does not read whole.

**Behaviour.**

* A reader of chapter 15, "What it reads", can list what `/apply` reads: the page, `AGENTS.md`, docs/01, docs/04, docs/05, and in docs/06 only the lines naming the slug and their milestone heading; then it marks its line `[*]`.
* The same reader can say why the queue is the exception: it gains a line with every delivery and holds every other delivery's state, while the build needs only its own line; the other documents say how the project is now.
* A reader of chapter 24, "Why the page and the documents keep sessions small", can say why that matters for the bill: what `/apply` reads at the start rides along on every call of the session, so reading only its own lines keeps the context the size of the delivery however long the queue gets.
* Chapter 24's key point on cache reads, or a new one, says `/apply` reads its own queue lines, not the queue.
* Must fail: any sentence in either chapter that says or implies `/apply` reads the whole queue; any number, measurement, or before-and-after comparison about this change (the book describes the kit as it is today, not what it was: the person, in this conversation); any changelog entry cited for it; Case A or Case B drawn on for it; a change in one edition and not the other.
* Edge: chapter 16 or another chapter that says `/apply` reads docs/06 whole is corrected in this delivery, in both editions, and named on the page; a chapter that only says `/apply` marks its line stays as it is.

**Contract.**

* **Chapters, both editions.** `book/en/15-apply.md` and `book/pt/15-apply.md`: "What it reads" / "O que ele lê" gains the docs/06 clause and its reason, in two or three sentences. `book/en/24-cost-and-where.md` and `book/pt/24-cost-and-where.md`: "Why the page and the documents keep sessions small" / "Por que a página e os documentos mantêm as sessões pequenas" gains one or two sentences; "Key points" / "Pontos-chave" one clause or bullet. No new section; "What the team gains" in either chapter does not change, since this adds no new gain to prove.
* **Source of the rule.** The kit's `/apply` file at 2026.10.16, as planted in this repository: "in docs/06 (queue) only the lines naming the slug and their milestone heading". Paraphrased, or quoted in that one line as chapter 15 already quotes the kit's file.
* **Other chapters.** /apply searches both editions for any claim that `/apply` reads the whole queue and corrects only those sentences.
* **docs/03 terms.** None new: `queue`, `queue line`, `milestone`, `context window`, `fresh session` exist.
* **Cases.** None. **Code examples.** None.
* **docs/06.** This line's sentence drops "with Case A's measured context before and after", now out of scope.

**Out of scope.**

* Numbers, Case A's or the kit changelog's, and any before and after: the book is a portrait of the kit today (the person, in this conversation).
* A queue line as one sentence, and a request that continues as /propose: `ch13-short-lines`.
* Slots as what and the command, and manuals for a proof on another machine: `ch10-12-slots-manuals`.
* The update example at 2026.10.16: `ch11-update-2026-10-16`.
* A worktree per delivery in a container folder: `ch21-container`.

**Done when.**

* [x] Both editions of chapters 15 and 24 read as Behaviour says, Portuguese terms from docs/03.
* [x] No other chapter, in either edition, says `/apply` reads the whole queue.
* [x] Each chapter still opens with its value; no filler and nothing useful cut; no new number.
* [x] `make verify` green; `make book` builds, and the delivery ends with the paths of both PDFs.
* [x] Page moved to `work/done/`, the line `[x]`, only this delivery staged, the `commit` block suggested.

**Record.**

* Chapter 15, "What it reads" / "O que ele lê": two sentences after the docs/05 slots, the docs/06 clause and why the queue is the one document read in part; the `[*]` sentence stays.
* Chapter 24, "Why the page and the documents keep sessions small": one sentence after the page's, that `/apply` reads only its queue lines because what it reads at the start rides on every call, so the build's context does not grow with the queue; the third key point names `/apply` reading its own queue lines, not the queue. "What the team gains" unchanged in both.
* Other chapters: both editions searched for a claim that `/apply` reads docs/06 or the queue whole ("whole queue", "reads the queue", "reads docs/06", "fila inteira", "lê a fila", "lê o docs/06"), and every `/apply` sentence naming the queue read; none found, so none corrected. Chapter 16 and chapter 15's `[x]` bullet only say `/apply` marks its line, and stay.
* Source: the kit's `/apply` file at 2026.10.16, paraphrased; no note, as docs/04 says for a rule of the kit.
* No number, no case, no changelog entry, no new term. Divergences: none.
* Proof: `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(ch15-24-apply-reads): teach that /apply reads only its queue lines

- ch 15: /apply reads only its slug's lines and milestone heading
- ch 15: why the queue is the one document not read whole
- ch 24: its own queue lines keep the build's context small
- both editions

work/done/ch15-24-apply-reads.md
```
