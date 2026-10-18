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
* `ch03-literal-type-comment`: chapter 3's refusal code block (section "Result: the value that carries a failure"). `ch03-error-languages`: chapter 3's "Exception, refusal, error" (pt 03:164). `pt-identifiers-choice`: pt 03:25 and docs/04 §Writing the book's Evidence and Code bullets, a hunk apart from the two bullets here. None holds a pointer of this list.
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

* [ ] Behaviour's apply-time check prints nothing for both editions; every changed sentence listed on the page, en and pt line beside each.
* [ ] docs/04's two bullets amended as Behaviour quotes, with the count /apply made.
* [ ] Both editions changed alike; each changed chapter still opens with its value, keeps its gain, no filler and nothing useful cut.
* [ ] Every number sourced: no number added.
* [ ] `make verify` green: edition parity, prose rules, width, links, disclosure scan, no em dash.
* [ ] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage changes beyond a pointer (docs/00 OD-3).
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunks of docs/04 and docs/06, commit message in a `commit` block.
