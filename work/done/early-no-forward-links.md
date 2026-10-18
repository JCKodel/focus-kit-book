# early-no-forward-links

**Objective.** A reader of chapters 0 to 7 learns each idea where the text names it, in a few words, instead of being sent to a later chapter; only the gain sections, and chapter 6's map of rules, keep their pointers. Both editions. From the author's reading of the book on 2026-10-18: "The first chapters are full of links to future, distant chapters. The reader reads the whole book and will remember a short introduction; they do not need to know where an idea lives."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *Every later chapter, not only distant ones.* The draft says "future, distant chapters"; the queue line says "instead of pointing to a later chapter". The page follows the queue line, which m18-review checks against. The pointers whose target is itself inside chapters 0 to 7 are listed apart in Behaviour (marked *near*), so the author restores them with one word in review. Source: docs/06 M18, the draft.
2. *Chapter 6's "Each rule and its failure" keeps its five pointers.* docs/04 §Writing the book, Chapter pointers, protects it by name ("where the pointers are the content, a map of where each step is taught (chapter 6's rules ...)"), and it has the shape the author exempted in the gain sections: the rule explained, then where it lives. Source: docs/04, the draft's exception.
3. *Parts stay.* "The example of Part I" places the reader, and "the method Part II teaches" (en 00:99, 02:27) already says what Part II holds; a Part is a division of the book the reader sees in the table of contents, not a chapter the text sends them to. The line says chapter. Source: docs/06 M18's line.
4. *Pointers back stay.* A pointer to an earlier chapter is not a link to the future; docs/04's rule for them (keep only where the sentence leans on a specific detail, or for the reader who skipped chapters 3 to 5) is unchanged. Source: the draft, docs/04, docs/00 §Audience.
5. *Two kinds of treatment, the words left to /apply.* Where the sentence already says the idea, only the pointer goes (kind *a*). Where it names a term the reader has not met in chapters 0 to that point, the pointer goes and a few words take its place, with the meaning of docs/03's row for that term (kind *b*). /apply writes the words; this page writes no book text. Source: the draft, docs/03, docs/05 §3.
6. *docs/04 changes in this delivery.* Two of its bullets allow what the author now refuses: "or the text says which chapter explains it" and "A pointer forward names a term the reader has not been taught, once per chapter for each target". Both are amended for chapters 0 to 7 only, the author's scope; chapters 8 on keep the rule as it is. Source: AGENTS.md (documents are living), docs/05 §7.
7. *No new check in `scripts/`.* A check would need an exception list (gain sections, chapter 6's map, Parts, pointers back); docs/04 holds the rule, Behaviour's grep runs at apply time and m18-review reads the chapters. Source: docs/05's governor (a step enters when it names the concrete error it would have caught; this one is caught by the review already queued).
8. *Applied last of M18's lines on chapters 0 to 7.* Other lines add text to these chapters, and ch05-test-time defers a gloss of "milestone" to this line's rule; the apply-time grep runs on the chapters as they are then, and the line numbers below are a courtesy counted on 2026-10-18. Source: docs/06 M18, work/ch05-test-time.md.
9. No new docs/03 term, no new queue line, no split: 34 lines per edition fit one review.

**Behaviour.**

* A reader of chapters 0 to 7, in either edition, meets no "chapter N", "capítulo N" or link to a chapter whose number is greater than the one being read, outside `## What the team gains` (pt `## O que o time ganha`) and chapter 6's `## Each rule and its failure` (pt `## Cada regra e sua falha`).
* Each pointer below goes; en line, pt line, target, kind (decision 5). *Near* marks a target inside chapters 0 to 7 (decision 1).
  * Prologue: 37/37 ch 7, a, near (the sentence says the product is written down); 45/45 ch 1, a, near; 55/55 ch 24 and Part V, a (the sentence says to ask for more); 61/61 ch 16, b, the governor: a step stays only while it names the concrete error it would catch; 62/62 ch 2 and ch 6, a, near; 66/66 ch 17, a; 95/95 ch 12, a; 97/97 ch 13, a.
  * Chapter 1: 69/69 "from chapter 3 on", a, near ("Part I" stays, decision 3); 83/83 ch 7, a, near; 89/89 ch 12 and 13, a (the sentence says what `/propose` and `/apply` do).
  * Chapter 2: 20/20 ch 12, a; 59/59 ch 7, a, near.
  * Chapter 3: 11/11 ch 6, a, near; 98/99 ch 4, a, near (the folder is said); 133/134 ch 4, a, near (the orchestrator is said, "the function around the rule"); 220/220 ch 5, a, near; 250/250 ch 16, b, the governor named as the method's rule, the sentence's content kept.
  * Chapter 4: 54/55 ch 5, a, near (each piece has its own test); 198/200 ch 5, a, near.
  * Chapter 5: 60/60 ch 12, a (the page of a delivery is met in chapters 1 and 2); 147/147 ch 13, a (the proof is said).
  * Chapter 6: 9/9 ch 7, a, near (ADRs are said); 38/38 ch 9, a; 43/43 ch 16, a (the governor's question is said).
  * Chapter 7: 15/15 ch 12, a; 17/18 ch 9, b, `/brainstorm` defines a new project by conversation and `/analyze` reads an existing repository, as chapter 9 teaches them (docs/03's `command` row names both); 35/36 ch 13, a, and ch 15, b, the milestone review: the review that closes a milestone (docs/03); 36/37 ch 13, a; 41/42 ch 11, a; 59/60 ch 14, a (a free line is said in the sentence); 61/62 "Chapters 18 and 19 teach the three.", the sentence goes, it holds only the pointer; 83/84 ch 13, a; 89/90 ch 8, b, a host: the program that runs the coding agent (docs/03), unless chapters 0 to 7 already said it by then.
* Stays: the gain sections' pointers (en 00:106, 02:67 and any other); chapter 6's map of rules (en 06:58, 62, 64, 66, 68); every Part mention; every pointer back; the chapters' links to sources and notes.
* docs/04 reads, in "Teach, do not only show", its sentence that ends "or the text says which chapter explains it" continued: "...or the text says which chapter explains it; in chapters 0 to 7, the base, it is explained where it appears and no later chapter is named (first: `early-no-forward-links`, from the author's reading)." and, after the first sentence of "Chapter pointers": "In chapters 0 to 7 no pointer forward stands outside `## What the team gains` and chapter 6's map of rules: the reader reads the whole book and keeps a short introduction, not where the idea lives (since `early-no-forward-links`, which cut 34 per edition)." The count is the one /apply makes.
* Checked at apply time, after every edit: for each file `book/{en,pt}/0[0-7]-*.md` with number N, every match of `[Cc]hapters? (\d+)`, `[Cc]apítulos? (\d+)` or `\]\((\d\d)-` whose number is greater than N, outside the two exempt sections, is printed; the list is empty. The same script run before the edit prints the 34 lines per edition above, adjusted for what other deliveries added.
* Every changed sentence still reads whole: no bare term where a pointer was, no dangling "as" or "and" left by a cut parenthesis.
* Fails: a pointer forward left outside the exempt sections; a kind *b* term left without its few words; a gain or chapter 6 map pointer removed; a pointer back or a Part removed; any chapter from 8 on changed; the editions differing in which pointers go; an em dash.

**Contract.**

* Files: `book/en/00-product-people-process.md` to `book/en/07-the-documents.md` and their eight Portuguese twins, the sentences Behaviour lists only; `docs/04-Conventions.md`, the two bullets Behaviour quotes.
* Terms of docs/03: none new; the glosses use the meaning of its rows `governor`, `milestone review`, `host`, and of `/brainstorm` and `/analyze` as chapter 9 teaches them. Sources: none added or removed. Cases: Ninjobs and Case A as the chapters already tell them; no new fact. Exercises: none (ADR-0017).
* docs/00, docs/01, docs/02, docs/03, docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.** Other sessions' pages of M18; this one applies after them (decision 8) and edits only the pointer sentences.

* `ch02-gain-less-to-read`: chapter 2's gain section, which this line does not touch.
* `ch03-literal-type-comment`: chapter 3's refusal code block (section "A pure function"; the page first placed it in "Result", corrected at apply). `ch03-error-languages`: chapter 3's "Exception, refusal, error" (pt 03:164). `pt-identifiers-choice`: pt 03:25 and docs/04 §Writing the book's Evidence and Code bullets, a hunk apart from the two bullets here. None holds a pointer of this list.
* `ch04-focus-optional`: chapter 4's opening and gain. `ch04-uncle-bob`: en 04:28. `ch04-scalable-meaning`: the S of FOCUS (pt 04:102). None holds a pointer of this list.
* `ch05-test-time`: chapter 5's testing sections, near en 05:138 to 148, where 05:147 is edited here; a gloss of "milestone" it adds follows decision 5. `ch05-random-values`: chapter 5's "Swap only I/O and the clock".
* `ch07-rag-and-numbers`: chapter 7's "The seven documents", where 07:35, 36 and 41 are edited here. `ch07-talk-not-edit`: pt 07:133, "Living documents".
* `case-a-why-anonymous`: the prologue's gain (pt 00:107), exempt here. `agent-never-unsure`: chapter 1, place chosen by its page. `pt-ninjobs-masculine`: articles across `book/pt/`; a pointer sentence here keeps whatever article that line leaves. `docs04-code-layout`: docs/04's code rule, a hunk apart.

**Out of scope.**

* Chapters 8 on: the author's scope; docs/04's rule for them is unchanged (decision 6).
* The gain sections and chapter 6's map: decision 2 and the author's exception.
* Parts and pointers back: decisions 3 and 4.
* A check in `scripts/`: decision 7.
* Other wording in the same sentences: only what the pointer's removal requires.
* `work/done/`: the record of what happened, not rewritten.

**Done when.**

* [x] Behaviour's apply-time check prints nothing for both editions; every changed sentence listed on the page, en and pt line beside each.
* [x] docs/04's two bullets amended as Behaviour quotes, with the count /apply made.
* [x] Both editions changed alike; each changed chapter still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: edition parity, prose rules, width, links, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage changes beyond a pointer (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author: by the driver, once at the end of the batch (batch rule 4).
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunks of docs/04 and docs/06, commit message in a `commit` block: the page moved by /apply; the mark, the staging and the commit by the driver (batch rules 1 and 2).

## Applied (2026-10-18)

**What changed.** Lines are after the edit, en/pt; the before-edit check, run after every other M18 delivery on chapters 0 to 7 was committed, found the same 34 sentences per edition as Behaviour, at new line numbers; no other delivery added a pointer forward.

* Prologue: 37/37 (ch 7, near), 45/45 (ch 1, near), 55/55 ("chapter 24, in Part V" goes whole, as listed), 61/61 (ch 16, kind b: "a rule this book calls the governor" / "uma regra que este livro chama de regulador"; the sentence already states the rule; "this book" and not "the method", which the prologue has not named by then, and chapter 3's only "method" before it is Extreme Programming), 62/62 (ch 2 and 6, near; the sentence ends "writing the spec became the work."), 66/66, 95/95, 97/97.
* Chapter 1: 87/87 ("from chapter 3 on" goes, near; "Part I" stays), 101/101 (ch 7, near), 107/107 (ch 12 and 13).
* Chapter 2: 20/20, 59/59 (ch 7, near).
* Chapter 3: 11/11 (ch 6, near), 98/99 (ch 4, near), 136/137 (ch 4, near; "the function around the rule" stays), 232/233 (ch 5, near), 262/263 (ch 16, kind b: "This book calls that question the governor and makes it the rule every step..." / "Este livro chama essa pergunta de regulador e faz dela a regra que todo passo...").
* Chapter 4: 58/59 (ch 5, near: "and each has its own test" / "e cada uma tem o seu próprio teste"), 203/205 (ch 5, near).
* Chapter 5: 81/81 (ch 12), 168/168 (ch 13).
* Chapter 6: 9/9 (ch 7, near), 38/38 (ch 9), 43/43 (ch 16; "the governor" already named in the prologue and chapter 3).
* Chapter 7: 15/15 (ch 12), 17/18 (ch 9, kind b: "`/brainstorm`, which defines a new project by conversation, or `/analyze`, which reads an existing repository, writes them once"), 45/46 (ch 13 kind a, ch 15 kind b: "the areas into which the review that closes a milestone splits its code reading" / "as áreas em que a revisão que fecha um marco divide a leitura do código"), 46/47 (ch 13), 51/52 (ch 11), 69/70 (ch 14; the parenthesis ends "defined yet or not)"), 71/72 ("Chapters 18 and 19 teach the three." becomes "Part III teaches the three." / "A Parte III ensina as três."), 92/93 (ch 13), 98/99 (ch 8, kind a: "host" is defined in chapter 1, line 10, so "Every host reads it" needs no gloss).

**Divergences.**

* Behaviour's check, run literally, also prints chapter 3's footnote `[^rust-book-errors]` ("The Rust Programming Language, chapter 9"), a chapter of another book, which Behaviour keeps as a source. The script skips footnote definitions (lines starting `[^`); with that it prints nothing for either edition.
* 07:98/99 is kind a, not b: the page's own condition ("unless chapters 0 to 7 already said it") holds, chapter 1 defines the host.
* "Milestone" in 07:45/46 needs no gloss: ch05-test-time glosses it at 05:41. Only "the review that closes a milestone" is said.
* docs/04's "after the first sentence of Chapter pointers" is read as after "A pointer forward names a term the reader has not been taught, once per chapter for each target.", the first sentence after the bold label and its parenthesis.
* The count in docs/04 reads "38 pointers in 34 sentences per edition" where Behaviour quoted "34 per edition": 00:62, 01:107, 07:45 and 07:71 named two chapters each (the review's wording, applied).
* 07:71/72: Behaviour said the sentence goes whole. The review found that cutting it leaves trunk, branch, pull request and merge with nothing said of them, since chapters 0 to 6 teach no git; a kind *b* the page missed. It now names Part III, which the prologue says is git (decision 3 keeps Parts), and no chapter.
* 07:45 reads "the areas into which the review that closes a milestone splits its code reading", the review's wording, clearer than stacking the two clauses.
* docs/04's bullet "Teach, do not only show" keeps its example "chapter 7 shows that document", cited from the prologue's `author-review-1`: it is the record of the rule's first occurrence and the rule still holds for chapters 8 on; the prologue no longer has that clause.

**Proof.** `make verify` green (strict build, parity, em dash, prose, width, links, disclosure). Apply-time check after the edits: `en lines 0`, `pt lines 0`. `make book`: by the driver at the end of the batch.

**Delivery review.** A read-only Opus agent, which did not write the changes, read `git diff` of the sixteen chapters and docs/04 against this page and docs/04. It found one thing that broke docs/04: once 07:71/72 was cut, git's terms had nothing said of them. That is fixed by naming Part III. It made two wording suggestions, 07:45 and the docs/04 count, and both were applied (see Divergences). Everything else passed: no pointer forward is left, even under a wider search (number words, "the chapter on", bare links); gains, chapter 6's map, Parts and pointers back are intact; the glosses read whole; both editions changed alike; no em dash; docs/04 matches Behaviour. `make verify` green again after the fixes, and the check prints nothing. Nothing new for the queue.

**Decisions.** The page's own list, applied as written, except for the divergences above.

```commit
docs(early-no-forward-links): say each idea where it appears in chapters 0 to 7

- cut 38 pointers forward in 34 sentences per edition, chapters 0 to 7
- gloss the governor, /brainstorm and /analyze, the milestone review
- chapter 7 names Part III for git strategies, no chapter
- docs/04: no pointer forward in the base outside gains and ch 6's map

work/done/early-no-forward-links.md
```
