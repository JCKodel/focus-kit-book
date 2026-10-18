# ch16-review-agents

**Objective.** After chapter 16 a reader can say why the process admits one kind of specialized subagent and no other: the read-only readers of the two reviews (the delivery review's reader of chapter 13, the milestone review's readers by area of chapter 15) and their checker, which read and report candidates and fix and decide nothing; and can name the error that happened behind each, as the governor asks; both editions.

**Decided without the author.**

1. *An error that happened, in a chapter where the kit is taught as it is today.* The chapter names the errors that let the readers and the checker in, because the governor's answer is an error that happened (docs/05 §7) and the queue line asks for them; the chapter already answers it this way for Ninjobs' duplicate index and Case A's `[?]`. Named as the governor's answer, an error is not a changelog citation, a kit version, a before-and-after measure or a narrated run (docs/04 "The kit as it is", ADR-0017). So: no count of rework, no build-file tally, no host command, no cloud review, no cancellation or cost, no model or advisor name, no kit date, no commit hash, no "since" or "no longer". `ch15-review-by-areas` decision 9 keeps the same account out of chapter 15, where each error is its rule's reason in the present; the bare commit stays there, as the range's reason, not the subagent's.
2. *Which errors.* Four, each from this book's repository, which is public, and each tied to what it let in (work/done/m14-review.md B1 and L8, its C8 scope line; work/done/m15-review.md, its revision note; work/done/repo-files-any-name.md):
   * the readers: a reader of the build, with the whole repository open, found that the function listing the repository's files dropped a file whose name holds a non-ASCII letter, such as `café.md`, so every check, the disclosure scan included, skipped it; no check could see it, since the checks were what was broken;
   * the delivery review's reader: that fault sat in the file from the delivery that wrote it, read before the commit only by the agent that wrote it and the person who committed it, and found at a milestone's review it became a line of its own instead of a fix in that delivery;
   * the paths read: one review's reader of the chapters read some of them, and the review closed as if it had read them all;
   * the checker: a reader said a number in one chapter had no row in the table it came from; opened, the table gave it, from two of its rows. The chapter number is not given: the book was renumbered after that review.
3. *A source note.* Yes, one, `[^m14-review]`, the same key in both editions, on the first of these errors: the record of that review in the book's repository, which holds the file-name candidate, the scope of the chapters' reader and the candidate that did not hold, so the reader gains the whole list to open. Format as chapter 19's `[^parallel-run]` and chapter 24's `[^ask-for-more-run]` (docs/03 `source note`, "a record of the book's runs"; docs/04 "Source notes"). The partial reading is stated from that record's own scope line; work/done/m15-review.md, which noticed it, is not cited, one note per point.
4. *Where it goes.* A new section after "What the process does not have" and before "The error that earned a mark": `## The subagent it admits` (pt `## O subagente que ele admite`). It explains the one exception the list's seventh item now names, so it follows the list; "The error that earned a mark" keeps its place and story.
5. *The seventh item of the list.* Its bold text becomes §7's own words, "No specialized subagent beyond the reviews' readers and checker", the definition and `[^claude-code-subagents]` stay, and the job reads: one agent that reads the documents plans and builds; the reviews' readers and checker are the exception the next section explains. Still eight items, and "§7 of docs/05 lists eight things" stays (docs/05 §7).
6. *Connecting the terms.* The chapter says once that the read-only agent of chapters 13 and 15 is a specialized subagent in this chapter's sense, since chapter 13 points here for agents an agent launches (work/done/ch13-delivery-review.md decision 7 and its divergence); chapter 13 and chapter 15 are each pointed to once, and how the readers work is not retold (docs/04 "Chapter pointers").
7. *The boundary.* Said where the exception is admitted (docs/04 "Say it where the doubt is born"): they read, list the paths they read and report candidates; they fix nothing and decide nothing, `/apply` or the person does; the checker works inside the one review, before the person sees a candidate, so it is not a review of a review, since the person still decides what counts (docs/05 §§5, 7, 8). The exception opens nothing else: a planner, a builder or a fixer subagent still has to name its error, and until one does it stays out.
8. *Why a separate context.* One clause pointing to chapter 13's reason, that the agent that wrote a change rereads it with the reasoning that wrote it; chapter 13 owns the reason and its source (`ch13-delivery-review`).
9. *Models and hosts named.* None: the chapter teaches the rule, not this repository's slot answers, which belong to `ch08-09-review-slot` (ch13-delivery-review decision 3; ch15-review-by-areas decision 10).
10. *The gain.* `## What the team gains` keeps its three sentences and gains one, no number: the one exception carries the errors that justify it, so the team checks it the way it checks any step, and the readers stay on the job those errors gave them (docs/04 "One gain", "A gain per chapter").
11. *Opening and key points.* The opening's second sentence gains a clause; still at most three sentences. Key point 4 names the exception; a key point on the errors is added to key point 4, not a sixth: still five key points (docs/04 "One gain").
12. *Docs/03.* No new term: `governor`, `delivery review`, `milestone review` and `finding` hold; `candidate` is the row `ch15-review-by-areas` asks the driver for, used here as defined there.
13. *Order.* The chapter points to chapter 15's checker and marks and to chapter 13's reader, and uses `candidate`; applied before `ch15-review-by-areas`, those pointers would name text not yet written. So the Contract asks the driver for this line's suffix `· after kit-2026-10-17, ch13-delivery-review, ch15-review-by-areas` (docs/05 §4); `batch-propose` already waits on this line.
14. *Portuguese words.* As chapters 13 and 15 fix them (Contract), one rendering each (docs/04 "Languages").
15. *Trunk, nothing staged by this definition.* docs/05 §5 Git; the driver session sets the marks in docs/06 (this batch's instructions). Chapter 13's files and work/ch15-review-by-areas.md, changed in the tree by other sessions, are not this page's.

**Behaviour.**

* The opening's second sentence says the reader can list what the process does not have, say what does each of those jobs instead, and say why the reviews' read-only readers and checker are the one specialized subagent it admits; the opening stays at most three sentences, its first sentence unchanged.
* §What the process does not have: "§7 of docs/05 lists eight things" stays; the seventh item reads as decision 5, keeping the definition and `[^claude-code-subagents]`; the other seven items are unchanged.
* Reading §The subagent it admits, a reader can explain:
  * that the read-only agent of chapter 13 and the readers and checker of chapter 15 are specialized subagents in this chapter's sense: launched by the session for one narrow role, they read files and the changes and edit nothing;
  * that the governor admits them because each names an error that happened in this book's repository, the four of decision 2, each said in one sentence and tied to what it let in: the readers, the delivery review's reader, the paths read, the checker; `[^m14-review]` on the first;
  * why the reader is another context, in one clause, pointing to chapter 13;
  * the boundary of decision 7: they fix and decide nothing, the checker is inside the one review and is not a review of a review, and the exception opens no other subagent until it names its error.
* §The error that earned a mark: unchanged.
* §What the team gains: its three sentences stay and the sentence of decision 10 is added.
* Key point 4: each of the eight things has its job done by something the process has, the readers of the two reviews and their checker being the one specialized subagent it admits, each on an error that happened; still five key points, the others unchanged.
* Edge: nothing in either edition names a kit version, cites the changelog, compares the kit with an earlier one, counts rework, or names a host command, a cloud review, a model, an advisor or a commit hash (decisions 1, 9).
* Edge: the errors are said as errors and their consequence, with no brief, transcript, diff, `git status` or hash: no run is narrated (ADR-0017).
* Edge: no number is added; the existing Ninjobs numbers and date stay.
* Edge: docs/04's prose rules hold, `not-but` included, in the sentences on what the readers do not do.
* Failure: a passage saying the readers or the checker fix or decide anything, that the checker is a second review, that the exception admits a planner or any other subagent, or that the delivery review's reader would certainly have caught the file-name fault, contradicts docs/05 §§5, 7, 8 and this page.
* Failure: one edition changed and not the other, or the note's key differing between them.

**Contract.**

* **Files.** `book/en/16-the-governor.md` and `book/pt/16-the-governor.md`, same changes; no other file.
* **Sections touched** (found by text): the opening's second sentence ("You can also list what the process does not have" / "Você também consegue listar o que o processo não tem"); the item "**No specialized subagent**" / "**Nenhum subagente especializado**" of §What the process does not have; a new `## The subagent it admits` / `## O subagente que ele admite` before `## The error that earned a mark` / its pt heading; §What the team gains; key point 4 ("Each of the eight things" / its pt); a new note after `[^claude-code-subagents]`.
* **Terms of docs/03.** `governor`, `delivery review`, `milestone review`, `finding`, `slot`, used as defined; `candidate` as `ch15-review-by-areas` asks the driver to define it. No new row from this page.
* **Portuguese words.** specialized subagent: `subagente especializado`; read-only agent: `agente somente leitura`; reader: `leitor`; checker: `conferente`; candidate: `candidato`; delivery review: `revisão da entrega`; milestone review: `revisão de marco`; paths read: `caminhos lidos`; governor: `regulador`.
* **Sources.** One added, both editions, same key:
  `[^m14-review]: J.C. Ködel, "One Page at a Time", the record of the review of M14, 2026-10-16, in the book's repository. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/m14-review.md>`
  pt: `[^m14-review]: J.C. Ködel, "One Page at a Time", o registro da revisão do M14, 2026-10-16, no repositório do livro. <same URL>`, following how chapter 19's pt note writes its `[^parallel-run]`. `[^openspec-glossary]` and `[^claude-code-subagents]` stay.
* **Cases.** This book's repository, public (decision 2); no Case A or Case B passage added; the Ninjobs and Case A passages unchanged.
* **Numbers.** None added.
* **docs/06**, asked of the driver session: this line's marks, and its suffix becomes `· after kit-2026-10-17, ch13-delivery-review, ch15-review-by-areas` (decision 13). No new line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* How the delivery review runs and why a writer misses its own faults: `ch13-delivery-review`.
* The range, the areas, the paths read and the checker's three marks: `ch15-review-by-areas`.
* How a project answers the review slots, its areas and model: `ch08-09-review-slot`.
* Batches of proposes and parallel applies: `batch-propose`.
* The kit's account of why it changed, its counts and the cloud review: a history of a kit change (decision 1).
* Chapters 7, 11 and 23's sentences on the milestone review: the line `ch15-review-by-areas` asks the driver for.

**Done when.**

* [x] Both editions written, same sections, parity green; the new heading in both.
* [x] The chapter opens with its value, at most three sentences; no filler, nothing useful cut; the list still eight items; still five key points.
* [x] Every Behaviour line reads as written in both editions.
* [x] Each of the four errors matches its record (decision 2): `scripts/repo_files.py`'s fault and its line in work/done/m14-review.md B1, the chapters' reader's scope in its C8 line, the weak candidate L8.
* [x] `[^m14-review]` opens at its URL on the day of /apply and the record holds those three things; cited once per edition.
* [x] `grep -n -i -E "2026\.[0-9]|changelog|no longer|opus|fable|sonnet|advisor|code-review|ultra|cloud" book/en/16-the-governor.md` finds nothing; `grep -n -i -E "2026\.[0-9]|changelog|não mais|opus|fable|sonnet|advisor|code-review|ultra|nuvem" book/pt/16-the-governor.md` finds nothing.
* [x] The Portuguese uses the Contract's words and no synonym.
* [x] No number added; every number sourced.
* [x] No em dash; `make verify` green, disclosure scan included.
* [x] The Delivery review ran on this delivery's paths as docs/05 §5 says, and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage added.
* [x] `make book` builds, and the delivery ends giving the author both PDF paths to review.

**Decided in /apply, without the author** (batch, recommended options):

1. *Which agents are the "readers".* The chapter names the delivery review's read-only agent and the milestone's readers together as "the reviews' readers", and the checker as a specialized subagent only "when an agent does that job", since chapter 15 lets the review's session be the checker.
2. *The delivery review's agent, where the host has its own review.* Chapter 13 has the host's own review first; the sentence says the read-only agent runs "where the host has no review of its own", naming no host (decision 9).
3. *"No check could see it."* The record says the pre-commit hook, which lists files another way, would have caught the name; the chapter says every check of `make verify` skipped it and none of them could see it, which is what the record holds.
4. *The disclosure scan.* Chapter 16's reader has not met it (chapter 21 names it); the chapter says "the scan that keeps private names out of the book" (pt "a varredura que mantém nomes privados fora do livro"), as chapter 21 says "a scan against the disclosure list" / "uma varredura contra a lista de exposição".
5. *The four errors as a list.* One bullet each, bold label, one sentence; no numeral, so no number is added.
6. *The note's newline.* The English file had no final newline; the new note line keeps it so.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure). The Done when greps for forbidden words find nothing in either edition; `[^m14-review]` is cited once and defined once per edition. On 2026-10-17 the note's URL answered 200 and the record on `main` held B1 (`scripts/repo_files.py:11`, a non-ASCII name skipped by every check), the C8 scope line (chapters 10 to 19, 21, 24 and 25 read by the chapters' reader) and L8 (weak: the number is the table's All minus Cache read). `make book` builds both PDFs.

**Divergences.** None from the page.

**Delivery review** (docs/05 §5): a read-only agent on Opus read `git diff` and `git diff --cached` of this delivery's paths, of docs/06 only this line's hunk, against the page, docs/03, docs/04 and docs/05 §§5, 7, 8, and the four errors against their records. Nothing broke the page's decisions or docs/04's rules; the four errors match B1, C8 and L8. Its findings, and what became of them:

1. en, the delivery review's reader: "and found only at a milestone's review, it became" did not parse: fixed, "and, found only at a milestone's review, it became", as the pt already read.
2. en, the seventh item: "reads the documents plans and builds" read as one noun: fixed, "reads the documents, plans and builds", as the pt.
3. The pt called the milestone's reader an agent and the en did not, and both said the steps launch agents with no condition, where docs/05 §8 has one fresh session per area in a host that runs no agents: fixed in both, "can launch agents" and "one reader per area, a read-only agent where the host runs agents" (pt to match).
4. The opening, the seventh item and key point 4 name the readers and the checker as the subagent with no condition: kept, as /apply decision 1 says; the section gives the conditions where the exception is admitted, and the short forms name the role. No line.
5. pt "código da construção" read oddly: fixed in both, "the code that builds the book" / "o código que monta o livro".


```commit
docs(ch16-review-agents): admit the reviews' readers in chapter 16

- List item 7 says docs/05 §7: no subagent beyond the readers, checker
- New section: the subagent the governor admits, and its boundary
- Four errors from this repository let the readers and checker in
- Source note [^m14-review] on the record of the review of M14
- Gain and key point 4 name the one exception

work/done/ch16-review-agents.md
```
