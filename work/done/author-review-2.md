# author-review-2

**Objective.** A reader finds a chapter by its number, and from chapter 7 to chapter 22 meets each explanation where the doubt is born, not several sections later.

**Behaviour.**

* Every H1 carries the chapter's number, `# 7. FOCUS: the four pieces`; the prologue is `# Prologue: ...`.
* Chapter 7 says, at the letter C, that the orchestrator is the correction: the glue that fetches, validates, decides through use cases, saves and shapes the result, so use cases stay pure, and that its test knows which repositories were called. At U it says that one event to one state is the test of a behaviour, and names MVI. Use cases hold decisions, validations and formats; the view formats nothing and is any output, a screen, a JSON answer, a printed line. A subsection explains drivers, third-party and written, and services. MVVM, MVC and the Mediator are named, with the author's view on a mediator beside MVC controllers.
* Chapter 8 says that agents made writing tests cheap and too many tests a risk, that red before green is how a test earns trust, and that a green suite does not prove working software.
* Chapter 10 says the queue is the document touched most, the kanban the agent reads, and spells ADR out before defining it.
* Chapters 12 and 18 say that every new document goes into the context folder and is brought into the project by the agent, so the agent can say why a thing is as it is.
* Chapter 18's work record fits the PDF's page; no text or Markdown block has a row over 74 columns.
* Case A's platform is named, Microsoft Power Apps with Copilot Studio, in chapters 13 and 22.
* Chapter pointers: 65 of 179 cut in each edition; chapter links print in the text's color in the PDF and the EPUB.

**Contract.**

* docs/04: H1 shape, "Say it where the doubt is born", the chapter-pointer rule, the 74-column rule.
* docs/03: view, driver, service (new), Case A's technology in the invariants.
* `pandoc/pdf.css`, `pandoc/epub.css`: `a[href^="#chapter-"]` and `a[href*="#chapter-"]` in the text's color.
* docs/06: this line; the launch line names the site and the Release links for focus-kit's README.

**Out of scope.**

* Publishing: the agent never pushes or tags; the site updates on the author's push to `main`, the Release on the author's `v*` tag.
* focus-kit's README: its own repository, after this review, by the launch line.
* Long TypeScript lines: code may wrap in the PDF.

**Done when.**

* [x] Both editions changed together; `make verify` green.
* [x] `make book` writes four files; the table of chapter 18 and the numbered titles checked in the PDF.
* [x] The author has both PDF paths to review.

## What happened

* The author's ten points, sent by conversation on 2026-09-30, are this page's Behaviour. Two questions were asked: the number format (`7. Title`, chosen) and what to do with chapter pointers (numbered titles, text color in print, and a sweep, all three chosen).
* The sweep's rule is now in docs/04. Kept: forward pointers to a term not yet taught, once per chapter and target; back pointers to a specific detail, to a term of chapters 4 to 8 from Part II on, and the maps of chapters 9 and 24. Cut: back pointers that repeat what a reader in order has just read, and second forward pointers to the same chapter. Pointers written as part of a sentence ("the governor of chapter 17") were left.
* The author asked for mocks on orchestrators; chapter 8 prefers a fake that throws on an unexpected call to a mock that fixes the order of calls. Chapter 7 now says the orchestrator's test passes doubles and knows which were called, and chapter 8 keeps its distinction; the two agree.
* Red and green were already added to chapter 5 by `author-review-1`; chapter 8 now ties them to trust in an agent's test instead of repeating the cycle.
* The Portuguese layout of chapter 18's context folder and of chapter 6's slices, and two commit messages of chapter 19, were shortened or translated to fit 74 columns.
