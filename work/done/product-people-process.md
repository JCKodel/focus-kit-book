# product-people-process

**Objective.** After the prologue the reader can name the three things any company that builds software depends on, product, people and process, say what each one teaches when the builders include coding agents, and say which part of the book answers each.

**Behaviour.**

* The reader can say where the idea comes from: the author heard it from Marcus Lemonis on television, and his site names three P's of business, people, process and product.
* Product: the reader can say that what is judged is the product, not the language, the framework or the code; the code is compiled and its users never see it. They can also say why the book still spends Part III on code: architecture is worth what it gives the product and the agent that maintains it, never an end in itself.
* People: the reader can say that people, and now agents, are the most important part and the most fragile, and name the three fragilities the prologue names: knowledge held by a few, opinion in place of evidence, and ego. They can say what the book does about each: documents take knowledge out of heads (chapter 6); every claim cites its source (the book's own rule, visible in every note); the person interprets, guides and validates, and never trusts blindly, whether the author is a colleague or an agent (chapter 2 for what an agent does not remember).
* Process: the reader can say why no software engineering survives without a shared process, and why a company's process is followed, not treated as a suggestion. They can also say the other half: a step is followed because it has a purpose, and a step that catches no concrete error is removed (the governor, chapter 13). Too much process fails too (chapter 1, chapter 4).
* The reader knows the book is also the material of an adoption program for a company that uses AI without a shared way to use it (Case B), and that the method is the same for one developer and for a company.

**Contract.**

Prologue, `book/en/00-product-people-process.md` and `book/pt/00-product-people-process.md`. The `00-` prefix only sorts it first: the site and the build number nothing (checked in `scripts/build_book.py`: `chapters()` sorts `[0-9][0-9]-*.md`, and no title carries a number), so no build change. It is not "chapter 0": the text calls it the prologue, and chapter 1 stays chapter 1.

* Title: "Product, people and process" / "Produto, pessoas e processo".
* Voice: the author in the first person for the two stories (the show, the LinkedIn exchange); "you" for the reader.
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. Where the idea comes from. First person: the author watched a reality show by Marcus Lemonis (*The Profit*), whose content does not matter here; one idea stayed: every company rests on three P's. Source note at the claim. His site orders them people, process, product; the prologue orders them product, people, process, and says in one sentence why: the product is what everything is judged by, so it comes first. The idea came from business, not software, and fits software well.
  3. Product. Many developers turn development itself into the product: the best solution, the best language, the best framework, and lose sight of what matters, the product being built. At the end of the day the code is compiled and nobody sees it; only the product exists, and everything is judged by it. One sentence against the misreading: this does not make code irrelevant; Part III organizes code because that serves the product and the agent that changes it. Point to docs/00 as where a project writes down its product (chapter 6), one sentence.
  4. People. People, and now agents, are the most important part and the most fragile. The three fragilities, one paragraph each or one list: knowledge held by a few (the answer: documents, chapter 6; an agent starts every session knowing nothing, chapter 2); opinion in place of evidence (the answer: every number and claim cites its source, as in this book); ego (the answer: the person interprets, guides and validates, the author of the code included, and trusts no one blindly, agent or colleague). No number, no study: this section frames, it does not argue with data.
  5. Process. No software engineering survives without a process; each person doing things their own way produces only chaos. The LinkedIn story, first person, paraphrased, no name, no date: someone asked me how I make sure everyone in a company follows the same standard; I was taken aback, and answered with a question: "Do you have a company of professionals, or a daycare full of children?" The meaning, one or two sentences: the process a company defines is not a suggestion, because it has a purpose. Then the other half, one or two sentences: the purpose is the test; a step that catches no concrete error leaves the process (chapter 13), and too much process fails too (chapter 1, chapter 4). The evidence for process is chapter 1's; the prologue points there and re-argues nothing.
  6. Why this book, and Case B. The book is also the material of an adoption program for a company (Case B) that uses AI without a shared way to use it. Proposed text, for the author to approve: "This book is also the material of an adoption program for a company, Case B, that already uses AI and has no shared way of using it: each person decides alone what to ask, where and at what cost." What the book gives such a company: a product written down, knowledge in documents instead of heads, one process that everyone follows because each step has a reason. One sentence on the map: Part I is why, Part II is the process, Part III the code, Part IV the team's git, Part V beyond code and adoption; cost and where AI pays is chapter 24.
  7. Key points, at most five.
  No exercises (Part I).
* Case B: only the sentence above, reworded by the author if needed. No name, sector, size, place, date, sales team or third party's assessment of the company; the company's situation is described only as what the book answers. The author approves the text in both editions (docs/00 OD-3).
* Numbers: three (P's), none else.
* docs/03 terms used: project documents, case, governor, fresh session. No new term.
* Sources (`[^key]`, same key in both editions):
  * `[^lemonis-3ps]` (new): `Marcus Lemonis Business Team, "3 Key To Business Success: People, Process & Product", accessed 2026-09-28. https://marcuslemonis.com/business/3ps-of-business` (pt: `acesso em 2026-09-28`). The page has no date and its byline is the team, not Lemonis. The live URL answers 403 to scripts; `check_links.py` counts 403 as passing. The wording was read in the Web Archive copy of 2025-08-11.
  * *The Profit* is named as where the author heard it, not cited: no note.
* Cases: Case B, one sentence. No Ninjobs number (chapter 1 carries it).
* Documents:
  * docs/00 §Contents gains the Prologue row, and Part V lists chapter 24 as cost and where AI pays, adoption as 25 (done by /propose, with the queue).
  * docs/04 §Chapter shape: "chapter 1 is the first to follow it" becomes "the prologue and every chapter, starting at chapter 1, follow it".
  * docs/04 §Files: one line saying the prologue is `00-<slug>.md`, sorted first and never called chapter 0.
  * docs/06: the line becomes `[x]`.

**Out of scope.**

* The evidence for process (METR, DORA): chapter 1 has it.
* AI cost, and where and how to use AI: chapter 24, `cost-and-where`, a delivery of its own.
* Adoption in a company, and Case B beyond one sentence: chapter 25, `adoption`.
* People, Process, Technology (Leavitt, 1964): the author chose to cite Lemonis only.
* Renumbering chapters: the prologue is outside the numbering.
* Any change to chapter 1: it stays as it is.

**Done when.**

* [x] Both editions written, same file name and heading structure, opening with the Objective in at most three sentences.
* [x] No filler and nothing useful cut; the only number (three) and every quoted claim carry a source; no draft marker.
* [x] The Case B sentence approved by the author in both editions; `make scan` green.
* [x] The site navigation and both PDFs show the prologue before chapter 1, with no number.
* [x] docs/04 updated as the Contract says.
* [x] `make verify` green.
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 line `[x]`, page in `work/done/`, staged, commit message suggested.

**What happened.**

* Both editions written as the Contract lists, sections in its order; Key points has five bullets; no exercises.
* The Case B sentence is the page's proposed text, word for word; the author approved it in both editions in this session.
* "Two or three heads" in the first draft became "a few heads", so three stays the only number.
* Diverged: in the Portuguese edition, "I was taken aback" became "A pergunta me pegou de surpresa", which keeps the first person without a gendered adjective.
* The show is named as where the idea came from, with nothing about its content; the note `[^lemonis-3ps]` sits at the three P's and at the site's order.
* Proof: `make verify` green (the link check passes the Lemonis URL); `make book` builds; the site navigation of both editions lists the prologue first after the home page, and the table of contents of both PDFs lists it before chapter 1, with no number. No build change, as the Contract said.
* No new term, no ADR.
