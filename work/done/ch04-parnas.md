# ch04-parnas

**Objective.** A reader of chapter 4 §Vertical slices meets David Parnas before the book leans on him: in 1972 he showed that splitting a program by the steps of its processing spreads one change over every module, and proposed hiding each decision likely to change in one module, with his own words and the paper to open, so the reader knows why a slice hides its feature's decisions and a folder per layer does not, in both editions. Found by `m15-review` (work/done/m15-review.md, A4: "en 4:58, pt 4:59: Parnas named with no introduction and no note. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. Introduce Parnas with his source, rather than cut the sentence. The queue line offers both. The sentence's "too" and "Parnas's criterion" point to an introduction that no longer exists: the rewrite planned Parnas 1972 as a source of this chapter (work/done/rewrite.md, the `06 features-not-layers` row and its sources list), and the then-chapter 4 introduced him, with `[^parnas-1972]`, in its DRY section until `simplicity-and-results` cut that paragraph (work/done/simplicity-and-results.md, "Cut: ... Parnas"), leaving this sentence orphaned. Cutting was not taken: Parnas gives the reason behind the slice that neither Martin's dependency rule nor Bogard's coupling rule gives, why a folder per layer makes one change touch five folders, which is §The problem's complaint. Source: docs/04 §Teach, do not only show ("a study ... is introduced in a few words the first time it is named") and §Source notes ("a note only where the reader gains something to open": a paper is one).
2. The introduction teaches the paper's comparison, not only its rule: two decompositions of one program, one by the steps of the processing and one by information hiding, and what one change to how the data was stored cost in each. That comparison is what lets the reader map Parnas onto layers and slices; the rule alone would be a quotation with no reason. Source: docs/04 §Teach, do not report (why the practice exists and how it solves the reader's problem).
3. The application to slices and to layers is the book's, and the text says it as the book's: Parnas wrote about modules of one program in 1972, not about features, folders or layers. The quoted words are his, verified against the paper (below). Source: docs/04 §Source notes ("every quoted claim ... carries `[^<key>]` at the claim"), AGENTS.md (every quoted artifact is real).
4. The note keeps the venue, `Communications of the ACM 15(12)`, between the title and the year: the batch asked for that exact reference, and it is the note the book carried before `simplicity-and-results` (`2d56d6e^:book/en/04-simplicity.md:159`). It adds the venue to docs/04's `<Author>, "<Title>", <year>. <URL>` shape the way a journal paper needs; no docs/04 change. The URL is the DOI, which resolves to the ACM Digital Library's page of the paper. Source: docs/04 §Source notes.
5. Placement: the paragraph where the sentence already is, the last of §Vertical slices, after "removing loans from the product removes one folder", because it closes the argument that a change touches one folder; not in §The dependency rule, which is Martin's. Source: chapter 4 as it stands.
6. No docs/03 term: "information hiding" is the paper's phrase and the chapter does not need to name it; `vertical slice` exists (docs/03, its row). No new queue line, no split: two files, one paragraph. Source: docs/03, docs/05 §1.

**Verified against the paper.** D. L. Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules", Communications of the ACM, Volume 15, Number 12, December 1972, pages 1053 to 1058 (read from the paper's scan, 2026-10-17):

* The first decomposition: "*the criterion used was to make each major step in the processing a module*"
* The second: "*made using 'information hiding' [4] as a criterion*"; "*Every module in the second decomposition is characterized by its knowledge of a design decision which it hides from all others.*"
* Changeability: of five likely changes, the second (all lines stored in core) and third (packing four characters to a word) "*would result in changes in every module*" of the first decomposition, while in the second "*Any change in the manner of storage can be confined to that module!*"
* Conclusion: "*We propose instead that one begins with a list of difficult design decisions or design decisions which are likely to change. Each module is then designed to hide such a decision from the others.*"

**Behaviour.**

* A reader of chapter 4 §Vertical slices, after "The top folder screams the library ... removing loans from the product removes one folder.", reads three sentences in place of "Parnas's criterion of 1972 works at this size too: the slice hides its feature's decisions from the rest of the program." (pt in parentheses, in place of "O critério de Parnas de 1972 funciona também neste tamanho: a fatia esconde as decisões da sua feature do resto do programa."):
  * "In 1972 David Parnas compared two ways of splitting one program into modules: split by the steps of the processing, a change to how the data was stored touched every module; split by the decisions likely to change, it touched one." ("Em 1972, David Parnas comparou duas maneiras de dividir um mesmo programa em módulos: dividido pelos passos do processamento, uma mudança em como os dados eram guardados mexia em todos os módulos; dividido pelas decisões que provavelmente vão mudar, mexia em um só.")
  * "He proposed to begin "*with a list of difficult design decisions or design decisions which are likely to change*", so that "*each module is then designed to hide such a decision from the others*".[^parnas-1972]" ("Ele propôs começar "*com uma lista de decisões de projeto difíceis ou de decisões de projeto que provavelmente vão mudar*", de modo que "*cada módulo seja então projetado para esconder tal decisão dos outros*".[^parnas-1972]")
  * "A folder per layer splits code by the steps a request goes through; a slice applies Parnas's criterion at the size of a feature, and hides its feature's decisions, such as how a loan is decided and stored, from the rest of the program." ("Uma pasta por camada divide o código pelos passos por que passa uma requisição; uma fatia aplica o critério de Parnas no tamanho de uma feature, e esconde do resto do programa as decisões da sua feature, como a forma de decidir e de guardar um empréstimo.")
  /apply may polish within these limits: three sentences at most; the English quotations are the paper's words exactly as in §Verified (lowercase first letter allowed), in quotation marks and italic; the Portuguese gives only their translation, with no English word inside the quotation (docs/04 §Source notes); `[^parnas-1972]` at the quoted claim; the comparison says "every module" and "one", as the paper does; the last sentence reads as the book's application, never as Parnas's claim about folders, layers or features; no em dash.
* At the end of each file, among the source notes, after `[^seemann-composition-root]`: `[^parnas-1972]: D. L. Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules", Communications of the ACM 15(12), 1972. <https://doi.org/10.1145/361598.361623>`, the same line in both editions (the title stays in English, docs/04).
* Checked, both editions, on `book/en/04-focus.md` and `book/pt/04-focus.md`: `grep -c "\[\^parnas-1972\]"` gives 2 (the citation and the note); `grep -n "Parnas"` finds three lines, the first and third sentences above (one sentence per line, docs/04) and the note, and none before §Vertical slices; `grep -n "In 1972\|Em 1972"` finds one line, the comparison sentence; `grep -n -i "works at this size too\|funciona também neste tamanho"` finds nothing.
* The rest of chapter 4 is unchanged: its opening, §The problem, §The dependency rule, the folder tree and the paragraph that explains its files (pt's `features/` sentence included), every later section, the gain and the key points.
* Fails: one edition changed and not the other; a quotation that differs from the paper's words in English, or keeps English words in Portuguese; Parnas named before he is introduced, or with no note; the note without the DOI or with a different title, venue or year; the text saying Parnas wrote about slices, features, folders or layers; "too" or "também" left pointing to an earlier mention; any other line of chapter 4 changed; an em dash.

**Contract.**

* Files: `book/en/04-focus.md`, `book/pt/04-focus.md`; no other file.
* Sections and lines: §Vertical slices / §Fatias verticais, its last paragraph, the sentence that names Parnas (en line 58, pt line 60 in the working tree of 2026-10-17, after `pt-placeholders`; the text is the locator, the numbers a courtesy); the source notes at the end of each file.
* Terms of docs/03: none new. Sources: `[^parnas-1972]` added, both editions, cited once each. Cases: none; no Case A, Case B or Ninjobs passage. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same chapters.**

* `pt-placeholders`: appears applied in the tree; its chapter 4 edit, the sentence on `features/` that closes the paragraph explaining the files of `src/features/emprestimos/`, is not touched by this page.
* `ch03-opening` (being applied, page in `work/done/`): chapter 3 only; it keeps the eight files that chapter 4's §When a piece pays its way points to. No file in common.

**Out of scope.**

* Parnas anywhere else in the book, such as back in chapter 3's DRY section: the finding is the orphaned sentence in chapter 4, and chapter 3's cut was decided by `simplicity-and-results`.
* "Information hiding" as a docs/03 term: the chapter does not name it.
* §The dependency rule and Martin's "Screaming Architecture" sentence: not the finding.
* A diagram of the two decompositions: three sentences carry it.

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapter 4 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every quotation matches the paper (§Verified); `make verify` green, edition parity with the new note cited once per edition, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, the change draws on no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Built.** The three sentences of Behaviour replace the orphaned one in §Vertical slices (en line 58 to 60, pt line 60 to 62), worded exactly as the page gives them, and `[^parnas-1972]` follows `[^seemann-composition-root]` in both editions. No other line of either file changed.

**Proof.** Behaviour's greps, both editions: `[^parnas-1972]` counted 2; "Parnas" on three lines (the comparison, the slice sentence, the note), none before §Vertical slices; "In 1972" / "Em 1972" on one line; "works at this size too" / "funciona também neste tamanho" on none. `make verify` green (build, parity, em dash, prose, width, links with the DOI resolving, disclosure). `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.** None.

**Omissions.** None.

**Review.** A read-only Opus agent read this delivery's staged diff, its docs/06 hunk, the page, docs/04 and a scan of the paper: no findings. It confirmed both quotations word for word, the first decomposition by "*each major step in the processing*", the storage changes touching "*every module*" in the first and "*that module*" in the second, the note's title, venue, year and DOI, the Portuguese meaning the same as the English, and the last sentence reading as the book's application. It noted, as style and not a rule, that the note sits after the closing period; docs/04 fixes neither form, so it stays.

```commit
docs(ch04-parnas): introduce Parnas's criterion with his 1972 paper

- Chapter 4 §Vertical slices says what Parnas compared and proposed
- His two phrases quoted from the paper, translated in pt
- The slice as the book's application of his criterion
- [^parnas-1972] note with the paper's DOI, both editions

work/done/ch04-parnas.md
```
