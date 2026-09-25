# chapter-template

**Objective.** After chapter 1 the reader can explain why a coding agent that writes fast does not make a project faster, and name what a minimal process gives the agent: a decision in writing, a limit on scope, and a check before "done". The chapter also fixes the shape every later chapter copies.

**Behaviour.**

* The reader can say where the slow part of building software is when an agent writes the code: deciding what to build and checking that it works, not typing it.
* The reader can cite one measured result where AI assistance made experienced developers slower while they believed it made them faster, and say where it was measured.
* The reader can name three failures of working with an agent without a process: the agent fills gaps with guesses, scope grows during implementation, and "done" arrives without proof.
* The reader can say why too much process also fails, from one sentence on the Ninjobs case, and knows that chapter 4 tells that story.
* An author starting any later chapter finds its shape in docs/04 §Chapter shape and needs to ask nothing.

**Contract.**

The chapter shape, written into docs/04 §Chapter shape in place of the text "Fixed by `chapter-template`; until then" (terms from docs/03):

```
---
status: draft            only while the chapter is not done; the delivery removes the line (docs/05 §5)
---

# <Title>                H1, the chapter title; the navigation shows it

<opening>                first paragraph, no heading, at most three sentences: what the reader can do after it

## <Section>             the content, in H2 sections (H3 inside when needed); as many as the value takes

## Key points            pt: ## Pontos-chave; at most five bullets; every chapter

## Exercises             pt: ## Exercícios; Part II on only; absent in Part I
### Exercise N.M         pt: ### Exercício N.M; N the chapter number, M from 1

[^<key>]: <source>       source notes, at the end of the file
```

* One sentence per line in the source: a convention, not a check (no error it would have caught has happened, docs/05 §7).
* Source notes: every number and every quoted claim from a publication carries `[^<key>]` at the claim. The key is lowercase `[a-z0-9-]+`, the same in both editions (`[^metr-2025]`). The definition is `[^<key>]: <Author or organization>, "<Title>", <year>. <URL>`, with the title in its original language in both editions. For a case, the definition names the artifact without any path: `[^ninjobs-adr-0022]: Ninjobs, ADR-0022, 2026-08-29.`
* `mkdocs.yml` enables the `footnotes` Markdown extension so the site renders them; pandoc reads the same syntax for `pdf-epub`.
* Appendices (`A<n>-`) are out of this shape; see Out of scope.

Chapter 1, `book/en/01-why-process.md` and `book/pt/01-why-process.md`:

* Title: "Why process, when AI writes fast" / "Por que processo, quando a IA escreve rápido" (already in place).
* Sections, in order (headings may be reworded in the writing; both editions keep the same structure):
  1. Opening: the Objective above, in at most three sentences.
  2. Speed moved the bottleneck: typing was never the slow part; deciding and checking are.
  3. What goes wrong without a process: guesses filling gaps, scope growing mid-build, "done" without proof.
  4. What a minimal process is: a decision in writing, one page per delivery, a check before "done"; the method the book teaches is focus-kit.
  5. Too much process fails too: one sentence with the Ninjobs numbers below, pointing to chapter 4.
  6. Key points. No exercises (Part I).
* Voice: first person for the Ninjobs sentence, "you" for the rest (docs/04).
* The core argument is a contrast; write it as two statements ("Typing is fast. Deciding and checking are slow."), since the `not-but` prose rule fires on "not only X but Y" and its Portuguese form.
* docs/03 terms introduced: none formally; `focus-kit` is named as what the book teaches, and `sdd` is left to chapter 3.
* Sources, each checked against the publication in /apply; a number not found there is dropped, not approximated:
  * `[^metr-2025]`: METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 2025. https://arxiv.org/abs/2507.09089. Confirmed in the abstract: 16 developers, 246 tasks in mature projects they knew for 5 years on average; they forecast AI would cut completion time by 24%, estimated afterwards it cut it by 20%, and it increased it by 19%.
  * `[^dora-2024]`: Google Cloud, "Announcing the 2024 DORA report", 2024. https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report. Confirmed in that post: "As AI adoption increased, it was accompanied by an estimated decrease in delivery throughput by 1.5%, and an estimated reduction in delivery stability by 7.2%." The report's "per 25% increase in adoption" enters only if /apply finds it in the report (https://dora.dev/research/2024/dora-report/).
  * `[^ninjobs-adr-0022]`: Ninjobs, ADR-0022, 2026-08-29. Fifteen days, 87 commits and 35 OpenSpec changes produced 38,823 lines of spec for four screens and one domain table. Paraphrased; nothing else from that ADR enters the book.
* Cases: Ninjobs only. No Case A or Case B, so no OD-3 approval.

Files:

```
docs/04-Conventions.md     §Chapter shape: the shape above replaces "until then"
docs/03-Domain.md          chapter shape, opening, key points, exercise, source note (written by /propose)
mkdocs.yml                 markdown_extensions: footnotes
book/en/01-why-process.md  chapter 1, status: draft removed
book/pt/01-why-process.md  chapter 1, status: draft removed
docs/01-Architecture.md    only if the footnotes extension needs a line there
```

**Out of scope.**

* Appendix shape: the first appendix delivery fixes it, with a real one in hand.
* A check for the chapter shape or for one sentence per line: no error has happened that it would have caught (docs/05 §7); parity already compares heading levels.
* The full Ninjobs story and the OpenSpec numbers in detail: chapter 4 and the appendix.
* SpecKit, OpenSpec and SDD by name as a subject: chapter 3.
* Context windows and why agents forget: chapter 2.
* Rendering footnotes in PDF and EPUB: `pdf-epub`.
* The home page (`index.md`) of either edition.

**Done when.**

* [x] docs/04 §Chapter shape holds the shape of the Contract; "until then" is gone.
* [x] `mkdocs.yml` enables `footnotes`; a source note renders as a footnote on the site in both editions.
* [x] Both editions of chapter 1 written, same headings in the same order, `status: draft` removed from both.
* [x] Opens with its value in at most three sentences; ends with at most five key points; no exercises.
* [x] No filler and nothing useful cut: every sentence read against docs/00 product question 2.
* [x] Every number carries a source note whose figure was found in the publication; any figure not found is dropped and recorded here.
* [x] Ninjobs appears only as the paraphrased numbers above; no Case A or Case B.
* [x] `make verify` green (build, parity, em dash, prose, links including the source URLs, disclosure).
* [x] docs/06 line marked `[x]`; page moved to `work/done/chapter-template.md` with what happened.

**What happened.**

Diverged from the plan:

* `[^dora-2024]` cites the report, not the blog post: `DORA, "Accelerate State of DevOps Report 2024", 2024. https://dora.dev/research/2024/dora-report/`. The "for every 25% increase in AI adoption" framing was found in the report PDF (printed page 40, "Exploring the downstream impact of AI"), so it entered, and a figure cited to a source must be in that source. The same page names small batch sizes and robust testing and hypothesizes that changelists grow with AI; the chapter paraphrases that with a second reference to the same note.
* The chapter names the three pieces as the section list does ("one page per delivery"); the opening keeps the Objective's "a limit on scope".
* The docs/04 shape says "pandoc reads the same syntax for PDF and EPUB" in place of "for `pdf-epub`", since docs/04 outlives the delivery; the appendix bullet says the first appendix delivery fixes their shape.
* docs/01 needed one word: the `mkdocs.yml` line of the tree now says "footnotes".

Nothing dropped: every figure was found in its publication.

* METR, arXiv abstract: 16 developers, 246 tasks, 5 years on average, forecast 24% faster, estimated 20% faster, measured 19% slower.
* DORA 2024: 1.5% throughput and 7.2% stability, in the blog post and, per 25% of adoption, in the report.
* Ninjobs ADR-0022, 2026-08-29: fifteen days, 87 commits, 35 OpenSpec changes, 38,823 lines of spec, four screens, one domain table. Nothing else from it entered.

The proof found:

* `make verify` green: build, parity, em dash, prose, links (both source URLs answer), disclosure with the list present.
* Both editions have 75 lines, the same five H2 sections in the same order, no front matter, three source notes with the same keys.
* The built pages `site/01-why-process/index.html` and `site/pt/01-why-process/index.html` each hold one `footnote` block with three notes and four references (`dora-2024` is referenced twice and gets two back links); no draft banner.
* Every sentence was read against docs/00 product question 2; cut in the reading: "This has been measured." and "I learned this the hard way".

Decisions: none needing an ADR.
