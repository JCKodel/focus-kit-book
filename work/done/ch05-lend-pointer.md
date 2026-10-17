# ch05-lend-pointer

**Objective.** A reader of chapter 5 §One rule through its tests who wants to see the use case `lend` before reading its tests is sent to chapter 4, where `lend` decides between a `Loan` due 21 days later and the refusal `HasOverdueBooks`, the two results the tests check, and not to chapter 3, which names `lend` only for its signature and its place in `rules.ts`; both editions. Found by `m15-review` (work/done/m15-review.md, A1: "5:56: the use case `lend` pointed to chapter 3; it is chapter 4's. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The pointer moves to chapter 4; the sentence is not reworded around chapter 3. Chapter 3 shows the rule as `mayBorrow` (§A pure function) and names `lend` only for its signature and as `Result`'s first use (§Abstraction on the second occurrence, §Why not throw); chapter 4 §One event, one new state is where `lend` is the use case: step 4 says what it returns, "a `Loan` due 21 days later, or the refusal `HasOverdueBooks` or `MemberSuspended`", and `lendRequested` calls it. Chapter 5's tests check exactly those results. Chapter 4 §Vertical slices says "`rules.ts` holds the rules of chapter 3, such as `lend`" (en line 51, pt 52): true of the rules, since chapter 3 teaches the pure rule and `Result`, but it does not change the choice, because the queue line asks for the chapter where `lend` is shown as the use case, and chapter 4 is the only one that says what it returns and calls it. Source: the finding A1 and chapters 3 and 4 as they stand.
2. The pointer stays, and is not cut. docs/04 §Chapter pointers keeps a pointer back "where it names a term of chapters 3 to 5 for the reader who skipped them"; "use case" is chapter 4's term (docs/03, its row), and the sentence names it.
3. The link targets the chapter, with no section anchor. docs/04 §Chapter pointers: "A chapter is found by the number in its title"; no chapter of the book links a section today.
4. Only the one sentence changes. Chapter 5's first section says "what chapter 3 asks of any step" (en and pt line 11), which is right: chapter 3 §The same principles in a process asks it. Its two links to chapter 4 (§The problem and the orchestrator's test) stay as they are; a third link to the same chapter is how this chapter already points. Source: chapter 5 as it stands, docs/04 §Chapter pointers.
5. No docs/03 term, no new queue line, no split: two files, one sentence each. Source: docs/03, docs/05 §1.

**Behaviour.**

* A reader of chapter 5 §One rule through its tests reads, after "The rule: a member with an overdue book cannot borrow another.":
  * en: "It lives in the use case `lend` of [chapter 4](04-focus.md), and each piece it crosses has a test." in place of the same sentence with "[chapter 3](03-simplicity-and-results.md)".
  * pt, §Uma regra pelos testes dela, after "A regra: um membro com um livro atrasado não pode pegar outro emprestado.": "Ela mora no caso de uso `emprestar` do [capítulo 4](04-focus.md), e cada peça que ela atravessa tem um teste." in place of the same sentence with "[capítulo 3](03-simplicity-and-results.md)".
* Following the link, the reader lands on chapter 4, whose §One event, one new state shows what `lend` (`emprestar`) returns and the orchestrator that calls it.
* Checked, both editions, on `book/en/05-testing-each-piece.md` and `book/pt/05-testing-each-piece.md`: `grep -c "03-simplicity-and-results.md"` gives 0; `grep -c "04-focus.md"` gives 3; `grep -n "use case \`lend\` of \[chapter 4\]"` (pt: `grep -n "caso de uso \`emprestar\` do \[capítulo 4\]"`) finds one line.
* The rest of chapter 5 is unchanged, line 11's "chapter 3" included.
* Fails: one edition changed and not the other; the link still on chapter 3, or on a section anchor; any other line of chapter 5 changed; any other file changed but this page and the line's marks in docs/06; an em dash.

**Contract.**

* Files: `book/en/05-testing-each-piece.md`, `book/pt/05-testing-each-piece.md`; no other file.
* Section and line: §One rule through its tests / §Uma regra pelos testes dela, its second sentence (line 56 in both editions in the working tree of 2026-10-17; the text is the locator, the number a courtesy).
* Terms of docs/03: none new ("use case", "caso de uso", already there). Sources: none added or removed. Cases: none; no Case A, Case B or Ninjobs passage. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on nearby chapters.**

* `ch03-opening` (being applied): chapter 3 only. This page links away from chapter 3 and depends on nothing in it.
* `ch04-parnas`: chapter 4 §Vertical slices only. This page links to chapter 4 as a whole and depends on nothing in that section. No file in common with either.

**Out of scope.**

* How chapter 3 and chapter 4 present `lend` and `mayBorrow`: the finding is the pointer, not the chapters it points to.
* A section anchor in the book's links: no chapter uses one (decision 3).
* Other pointers of chapter 5: right as they stand (decision 4).
* Chapter 4's sentence that calls `lend` one of "the rules of chapter 3" (§Vertical slices, the paragraph explaining the files, not the last paragraph that `ch04-parnas` edits): not this finding; rewording it would be a new line.

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapter 5 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: links, edition parity, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, the change draws on no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Built.** The second sentence of §One rule through its tests (en) and §Uma regra pelos testes dela (pt), line 56 in both editions, now links the use case `lend` (`emprestar`) to [chapter 4](04-focus.md) instead of chapter 3, worded exactly as Behaviour gives it. No other line of either file changed; line 11's "chapter 3" stays.

**Proof.** Behaviour's greps, both editions: `03-simplicity-and-results.md` counted 0; `04-focus.md` counted 3; the new sentence found once, on line 56. `make verify` green (build, parity, em dash, prose, width, links, disclosure). `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.** None.

**Omissions.** None.

**Review.** A read-only Opus agent read this delivery's staged diff, its docs/06 hunk, the page and docs/04: no findings. It confirmed only line 56 changed in each edition, the greps, chapter 4 §One event, one new state saying what `lend` (`emprestar`) returns and `lendRequested` calling it, the pt sentence meaning the same as the en one, and the link to the chapter with no anchor as docs/04 §Chapter pointers asks. It noted chapter 4 §Vertical slices still calling `lend` one of "the rules of chapter 3"; the page leaves that out of scope (decision 1), so it is not a finding.

```commit
docs(ch05-lend-pointer): point chapter 5's use case lend to chapter 4

- Chapter 5 §One rule through its tests links lend to chapter 4
- Same change in the pt edition, for emprestar

work/done/ch05-lend-pointer.md
```
