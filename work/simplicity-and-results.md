# simplicity-and-results

**Objective.** After this chapter a reader can refuse accidental complexity with KISS, YAGNI and DRY, write a business rule as a pure function that returns a `Result`, tell an exception from a refusal from an error, and rely on the compiler to refuse a forgotten case, in one chapter that opens with what went wrong on Ninjobs instead of two that open with definitions.

**Behaviour.**

* A reader opens the chapter on Ninjobs: 29 checks that never caught an error, a decision in six places, eight files to show one field; then meets the three principles as the names of what was lost. The pain comes before the rule.
* A reader finds each principle in one section of at most a screen: KISS with the due date example, YAGNI with the loan periods example, DRY with the two kinds of "non-empty" and the second-occurrence discipline; each with one source.
* A reader then finds the pure function, `Result`, the trio exception, refusal, error, and the exhaustive `switch`, in that order, with the code examples of chapter 5 kept where they teach (the `mayBorrow` rule, the `Result` type, the boundary `catch`, the `Record` over the refusals).
* Failure: a reader looking for the U-2 and the SR-71, Fowler's four numbered costs, Parnas, Lippert's four kinds, Spolsky, the ASP.NET and Framework Design Guidelines quotations, the Next.js and .NET cancellation paragraph, or the TDD section with its Vitest test, does not find them here; the TDD cycle is taught once, in chapter 8.
* A reader finds Toub's benchmark as a story, not a number: a throw costs the time of a thrown and caught exception on every refusal, and most of what a program handles is a refusal; the one number kept is the ratio ("more than four times a return on .NET 8") with its note.
* A reader finds the process paragraph ("The same three principles in a process") reduced to the Caution box, which already tells the story of the review spiral, and the sentence that chapter 18 turns the rule into a question.
* Edge: the Clean Architecture comparison (use case with injected repositories) is one sentence with a pointer to the FOCUS chapter, which teaches the orchestrator.
* Edge: the Go, Rust and F# sentence is one sentence: the field calls it "errors as values"; this book says "exceptions as values", and the trio section says why.
* Edge: the gain section is one, with one number, Ninjobs's 29 checks, and the key points are five for the whole chapter.

**Contract.**

* **One file, both editions:** `04-simplicity-and-results.md` (pt same name), H1 "4. Simplicity and results: KISS, YAGNI, DRY and exceptions as values" (pt: "4. Simplicidade e resultados: KISS, YAGNI, DRY e exceções como valores"); `05-rules-and-exceptions.md` removed with `git rm` in both editions. Chapter 4's sentence that the code examples are written for the book, in TypeScript, and in Portuguese names in the pt edition, stays at the first code block (docs/04 §Code).
* **Sections, in order:**
  1. Opening, three sentences: what the reader can do.
  2. `## What grew on Ninjobs`: the five sentences of today's chapter 4 gain section (29 checks, six places, eight files, the architecture not at fault, two checks kept), then Brooks's essential and accidental complexity in two sentences, `[^brooks-silver-bullet]`, and the sentence that an agent makes the wrong choice cheaper.
  3. `## KISS`, `## YAGNI`, `## DRY`: each the current section minus the cuts: KISS loses the U-2 account (one sentence credits Johnson and the field-repair rule); YAGNI loses the numbered list of four costs and keeps "even the right presumptive feature pays delay and carry", `[^beck-xp]` and `[^fowler-yagni]`; DRY loses the Parnas paragraph, keeps `[^pragmatic-programmer]`, the two-kinds-of-knowledge example and `[^metz-wrong-abstraction]`.
  4. `## Abstraction on the second occurrence`: today's "The discipline" section, unchanged.
  5. `## A pure function`: chapter 5's section with the Clean Architecture paragraph cut to one sentence and a pointer to the FOCUS chapter.
  6. `## Result`: chapter 5's section; the Go, Rust, F# paragraph becomes one sentence with `[^go-errors]` only.
  7. `## Exception, refusal, error`: chapter 5's section minus the Lippert paragraph; `[^dart-core]` stays if its claim stays.
  8. `## Why not throw`: three reasons in prose, not a numbered list: the exit the call site does not show (`[^spolsky-exceptions]` cut; the sentence is the book's), the signature that lies, the catch that hides bugs; then time as one sentence with the ratio and `[^toub-net9]`. `[^aspnet-best-practices]` and `[^fdg-exception-throwing]` removed.
  9. `## Where the catch lives`: chapter 5's section with the boundary code, `[^anti-corruption-layer]` kept; the "Two kinds of throw pass the boundary" paragraph reduced to its first and last sentences, `[^nextjs-redirect]` and `[^dotnet-exceptions]` removed.
  10. `## Every case handled`: unchanged.
  11. `## The same principles in a process`: the Caution box and the sentence on chapter 18 only; the three bullets removed (chapter 18 and chapter 9 teach them).
  12. `## What the team gains`: one paragraph: less to read, review and keep true; a rule has a test before it has a screen; a forgotten case is a compile error. One number at most.
  13. `## Key points`: five.
* **Cuts, by first words, both editions:** "Kelly Johnson... U-2 and the SR-71" to one sentence; "Fowler counted... four costs" list; "David Parnas gave the reason"; "Clean Architecture, as it is usually practised" to one sentence; "Go returns errors... Wlaschin" to one sentence; "Eric Lippert sorted"; the "Why not throw" list's quotations; "Two kinds of throw pass the boundary" middle; "The rule is born with its test" whole; the three process bullets; chapter 5's gain and key points merged into the chapter's.
* **Notes removed:** `[^parnas-1972]`, `[^rust-result]`, `[^wlaschin-rop]`, `[^lippert-vexing]`, `[^spolsky-exceptions]`, `[^aspnet-best-practices]`, `[^fdg-exception-throwing]`, `[^nextjs-redirect]`, `[^dotnet-exceptions]`, `[^beck-tdd]` (chapter 8 keeps its own). Same keys cited the same number of times in both editions.
* **Pointers:** every `](05-rules-and-exceptions.md)` and "chapter 5" in `book/`, docs/00 Contents and Audience, docs/03 and docs/04 resolves to chapter 4 or to the merged file; chapters 7 and 8 point to "chapter 4" for `Result` and the boundary; docs/04's "chapter 5's red and green cycle" example becomes chapter 8's. The list of mentions resolved goes on this page.
* **Terms:** pure function, Result, exception, refusal, error, as docs/03 has them; docs/03's rows that cite chapter 5 move to chapter 4.
* **Code:** chapter 5's blocks kept as they are, under 25 lines each, on the lending library; chapter 4's `dueDate` block stays as the first block of the book.
* **Cases:** Ninjobs, by name, in the opening section.

**Out of scope.**

* The TDD cycle: chapter 8 (`ch8-testing-trim` keeps it there).
* The orchestrator and dependency injection: `focus-and-slices`.
* Renumbering 6 to 26: `renumber-chapters`.
* The "no baseline" sentence: said once in the prologue (`prologue-and-why`).

**Done when.**

* [ ] One chapter in both editions, `05-rules-and-exceptions.md` gone from both, same headings; opens with Ninjobs; one source per point; no filler and nothing useful cut (every rule of the two chapters is in the merged one or named as cut above).
* [ ] No link to `05-rules-and-exceptions.md` and no "chapter 5"/"capítulo 5" left in `book/`, docs/00, docs/03 or docs/04 that means the old chapter; the list on this page.
* [ ] Every number sourced; parity of notes green; the Portuguese code keeps its Portuguese names.
* [ ] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Open with Ninjobs: docs/04 §Value first and §Say it where the doubt is born; the review found the chapter's only concrete pain at its end.
* One source per point: docs/04 §Source notes, a note only where the reader gains something to open; four guidelines for one rule is not four things to open.
* The TDD cycle leaves chapter 4 for chapter 8: docs/04 §Teach, do not only show and DRY; chapter 8's "Red and green" paragraph already points to it.
* The ratio stays and the milliseconds leave: docs/04 §Numbers that prove.

**Decisions in the review.**

* The gain's one number is Ninjobs's 29 checks, as recommended.
* The title stays "Simplicity and results" (pt "Simplicidade e resultados"), the author's choice; the Contract's H1 holds.
