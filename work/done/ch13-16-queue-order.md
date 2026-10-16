# ch13-16-queue-order

**Objective.** After chapters 13 and 16 a reader can order a milestone so that the order is the priority, write `· after <slug>` for an order known when a line is added, tell it from a `[?]` found on the way, name the next delivery as the first free line, say which free lines can run at the same time, and take a waiting line out by its resume suffix, as focus-kit 2026.10.13 says.

**Behaviour.**

* A reader adding `return-book` to the lending library's milestone, knowing a return needs a loan, writes `[ ] return-book ... · after lend-book` from chapter 13, and says the line keeps `[ ]`: an order, not a wait (docs/05 §4; docs/03 "dependency").
* A reader asked "which delivery matters most?" answers from chapter 13: the one higher in the queue; to change the priority they ask the agent to move the line, by conversation, and no priority field or label exists (docs/05 §4).
* A reader of chapter 16's example (`[*] lend-book`, `[>] return-book`, `[~] reservations`, `[ ] my-loans ... · after lend-book`, `[?] due-reminder ... · resume: propose · blocked: which provider?`) names the free lines: `return-book`, `reservations` (taken by a session) and not `my-loans` (its `after` is not `[x]`) nor `due-reminder` (`[?]`); a new session's next delivery is `return-book`, the first free line no session holds.
* A reader whose `lend-book` becomes `[x]` says `my-loans` is free from that moment, with nothing to clear and no mark changed: `· after` stays on the line as the record of the order.
* Failure: a reader who, adding `my-loans`, writes `[?] my-loans ... · blocked: after lend-book` knows from chapter 16 it is wrong: a dependency known when the line is written is `· after`, and a `[?]` there would show queued work as stuck on the board (docs/03 "blocked reason").
* A reader whose `/apply my-loans` finds that `lend-book` sets the due date a day early at a month's end writes `[ ] fix-due-date` above it and `[?] my-loans ... · resume: apply · blocked: after fix-due-date`: a wait found on the way, after work started.
* Failure: a reader who runs `/propose my-loans` while `lend-book` is `[*]` knows the command does not start it and says what it waits on, as it does for a `[?]` line (the kit's `/propose` and `/apply` files).
* A reader asked "what can run at the same time?" answers from the queue: the free lines, and among them those that touch different files, judged from their pages and docs/01; `return-book` and `reservations` (`src/loans/`, `src/reservations/`) can; `return-book` and `lend-book`, both in `src/loans/`, cannot in one folder; chapter 21 shows how two run in one folder.
* Leaving `[?]`: when the director names the provider, `due-reminder`'s `resume: propose` sends it back to `[ ]`, its draft kept for `/propose`; a `resume: apply` line goes back to `[>]` only if its page still answers every section, otherwise to `[ ]` with what `/propose` must settle (docs/05 §4). A page that merely exists is not enough.
* Board: on three columns `my-loans` sits in To Do with no blocked tag; only `due-reminder` carries one.
* Edge: a line with two orders, `· after lend-book, members`, is free only when both are `[x]`.
* A reader looking for the source finds `SETUP.md` at version 2026.10.13, its docs/05 §4, named in plain words; the six marks still date from 2026.10.05.

**Contract.**

* **Chapter 13, both editions, file name and title kept.**
  1. Opening: "size and order a milestone" becomes order as priority and `· after`.
  2. "The line": the line's shape gains the optional `· after <slug>` at its end.
  3. Example milestone: `return-book` gains `· after lend-book`; the reading sentence under it says so.
  4. "Size and order": the order is the priority; "each line after the lines it needs" is written as `· after <slug>` when the line is added, an order and not a block, pointing to chapter 16 for when a line is free.
  5. "Changing the queue": reordering is changing priority, by conversation.
  6. "What the team gains": the kit's changelog, entry 2026.10.08.3, paraphrased: the rule that order is priority always held and was written nowhere, so a user asked for a way to rank deliveries. This book's own docs/06: milestone M12's seven lines that end `· after kit-2026-10-13`, public in the repository.
  7. Key points follow.
* **Chapter 16, both editions, file name and title kept.**
  1. Opening gains: the next delivery, `· after` against `[?]`, which lines run together, the resume suffix.
  2. "The problem": the sentence "focus-kit answers both since its version 2026.10.05" stays for the marks.
  3. Table: the `[>]` row's "Set by" reads "when the page is complete" (docs/05 §4).
  4. Example: as in Behaviour; `my-loans` becomes `[ ] ... · after lend-book`, `due-reminder` gains `· resume: propose`; the reading sentence follows. Portuguese slugs as today (`meus-emprestimos`, `emprestar-livro`, `aviso-prazo`, `corrigir-vencimento`).
  5. New section "The next line, and which run together", after "At the moment the work changes": free line (docs/03), the first free line no session holds is next, a line whose `after` is not `[x]` is not started by `/propose` or `/apply`; what runs at the same time, judged from pages and docs/01; pointer to chapter 21.
  6. "Waiting": the third case says "found after work started"; a new paragraph tells `· after` from `· blocked: after`; the resume suffix before the reason; leaving `[?]` by the resume phase, replacing "It goes back to `[>]` when its page exists".
  7. Kanban: `my-loans` in To Do, untagged.
  8. "What the team gains": Case A's paragraph kept; the changelog's second story paraphrased (nothing said which lines could run together, so the person worked it out alone before opening two sessions).
  9. Key points follow.
  10. The note `[^setup]` leaves: docs/04 says no note points to a file of focus-kit's repository; the text names `SETUP.md`, version 2026.10.13, docs/05 §4.
* **Terms:** dependency, free line, resume suffix, waiting mark, blocked reason, as docs/03 has them (kit-2026-10-13); pt `dependência`, `linha livre`, `fase de retomada`; `· after` and `· resume:` stay in English in pt, as `· blocked:` does. docs/03 unchanged.
* **Sources:** the kit's CHANGELOG entry 2026.10.08.3 and `SETUP.md` 2026.10.13, named in plain words, no note; this book's docs/06. Toyota and Azure notes kept.
* **Cases:** Case A's existing passages in chapters 13 and 16, unchanged; no new private passage.
* **Code examples:** none; the lending library's lines and paths are written for the chapter, said so.

**Out of scope.**

* Chapter 14's "or on another line not yet done" sentence: `ch14-propose-decides` owns chapter 14.
* Chapter 22's board mirror: it says how `[?]` maps, and an `· after` line is a plain card there; no sentence is wrong.
* Running two sessions in one folder: chapter 21, done by `ch21-one-tree`.
* GitHub Spec Kit's `[P]` marker, which the changelog compares: the claim was not checked against Spec Kit, and chapter 3 does not need it.
* A new run or count: the changelog and the book's own queue are the evidence (ADR-0017).

**Done when.**

* [x] Chapters 13 and 16 changed in both editions, same headings; each opens with its value; no filler and nothing useful cut.
* [x] No sentence in the book says a line waiting on a known order is `[?]`, or that a `[?]` line goes back to `[>]` because its page exists.
* [x] Chapter 16 names `SETUP.md` 2026.10.13 in plain words and has no `[^setup]`; every other number and quote sourced.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Chapter 13 teaches the order when the queue is written; chapter 16 teaches it while the queue moves (next line, free, run together, waiting), so each says it once (docs/04, say each thing once).
* "The next delivery is the first free line" is read as the first free line no session holds, since a `[~]` or `[*]` line is free and already taken (docs/03 "free line"; docs/05 §4).
* The resume suffix is taught here: chapter 16's leaving-`[?]` sentence would contradict the version it cites (asked; author chose yes).
* Evidence: the changelog's two stories and this book's M12 (asked; author chose both).

**What /apply did.**

* Chapter 13: the opening names ordering as priority and `· after`; the line's shape ends with an optional `· after <slug>`; `return-book` gains `· after lend-book` and the reading sentence says why; "Size and order" says the order is the priority, with no field or label, and teaches `· after` as an order that keeps `[ ]`, with `lend-book` carrying none since its lines were `[x]`; "Changing the queue" says moving a line is changing its priority; "What the team gains" gains the changelog's first story and M12's seven lines; two key points added.
* Chapter 16: the opening gains the next delivery, which lines run together, `· after` against `[?]` and the resume suffix; the version sentence names `SETUP.md` 2026.10.13 and its docs/05 §4 in plain words and `[^setup]` is gone; the `[>]` row and "At the moment the work changes" read "when the page is complete"; new section "The next line, and which run together"; "Waiting" gains the resume suffix on every example, "found after work started", the `· after` against `· blocked: after` paragraph and leaving `[?]` by the resume phase; the board puts `my-loans` in To Do untagged; "What the team gains" gains the changelog's second story; key points rewritten for free lines, `· after` and the resume phase.
* The queue line until kit-2026-10-16 said: chapters 13 and 16: the order is the priority, the next delivery is the first free line, `· after <slug>` as a known order against `[?]` as a wait found on the way, which lines can run at the same time; the version cited in chapter 16; both editions.

**Divergences.**

* Chapter 16's free line `return-book` became `[>] search-catalog` (pt `buscar-catalogo`), in `src/catalog/` (pt `src/catalogo/`). Chapter 13's contract gives `return-book` a `· after lend-book`, so a `[>] return-book` beside `[*] lend-book` in chapter 16, the same library's milestone 1, would show a line defined before the line it comes after was done, which `/propose` refuses. Asked; the author chose to change chapter 16's line. So the line that runs beside `reservations` is `search-catalog`, and the example of two lines that cannot run together in one folder is `lend-book` and a line to renew a loan, both in `src/loans/`.
* Chapter 15's line 57, in both editions, said a `[?]` line goes back to `[>]` when it has a page, which Done when forbids anywhere in the book. Asked; the author chose to fix that one sentence here: it now goes back by its resume phase, pointing to chapter 16. The rest of chapter 15 stays with `ch15-apply-ends`.
* The M12 count has a source note, `[^queue-m12]`, to this book's docs/06: docs/04 lists a file of this book's repository among what a note may point to, and chapters 3, 18, 21 and 26 cite theirs so. The kit's changelog and `SETUP.md` have none, as docs/04 says.
* The example lines were shortened to fit the PDF's code width without wrapping: chapter 16's `due-reminder` reads "a reminder" (pt `aviso-prazo`, "um aviso"), chapter 13's pt `devolver-livro` reads "a bibliotecária registra a volta".
* Chapter 16 is now the first statement of "free line" in the book; chapter 21, which already defines it the same way and points to chapter 16, is the second and stays as it is.
* The Portuguese edition says once in each chapter that `· after`, `· resume:` and `· blocked:` stay in English, as the kit writes them.

**Proof.** `make verify` green (build, parity, em dash, prose, links, disclosure). `make book` builds both editions; in both PDFs every changed code line of chapters 13 and 16 fits on one line, checked in the text of each PDF and on the rendered page of chapter 16's example. Numbers: seven M12 lines end with `· after kit-2026-10-13`, counted in docs/06; the changelog's two stories read at focus-kit's entry 2026.10.08.3; `SETUP.md` reads `Version: 2026.10.13`.

**Cases.** No new passage of Case A or Case B; chapter 16's Case A passages are unchanged.

**Dependent lines.** None: no line names `ch13-16-queue-order` in an `after`.

```commit
docs(ch13-16-queue-order): teach queue order, free lines and resume

- chapter 13: the order is the priority; `· after <slug>` is an order
- chapter 16: the next free line, which lines run together, resume phase
- chapter 16 names SETUP.md 2026.10.13 in plain words, no note
- chapter 15: a [?] line leaves by its resume phase, not by its page
- both editions

work/done/ch13-16-queue-order.md
```
