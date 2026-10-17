# ch03-opening

**Objective.** A reader opens chapter 3 on what grew on Ninjobs, one field that took eight files and 29 checks that never caught an error, and the lesson that KISS and YAGNI were lost one reasonable addition at a time, in three sentences that leave the causes and what replaced them to chapter 6, which tells that story once, in both editions. Found by `m15-review` (work/done/m15-review.md, A8: "3:9-14 retells chapter 6's causes and checks. Seen. The same numbers as evidence for other points (2, 3, 4, 7): weak.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. What the finding is: the retelling at lines 9-14, not the numbers. The checker marked "the same numbers as evidence for other points" weak, so a number that proves chapter 3's own point stays, and the 29 checks in chapter 3's gain and in chapter 16 are not touched. Source: m15-review A8.
2. Each fact of lines 9-14, sorted by its owner (AGENTS.md and docs/04: a story told once, in the chapter that owns it):
   * Eight files to show one field: stays. It is chapter 3's evidence for KISS and YAGNI in code, and chapter 4 line 222 points back to chapter 3 for it ("one field took eight files (chapter 3)").
   * 29 checks that never caught an error in the product: stays, as one clause with no characterization. It is the gain's one number (en 254, pt 255) and the process side of §The same principles in a process. The alternative, dropping it from the opening too, was not taken: the gain would then cite a number the chapter never set up.
   * "Costly to satisfy and cheap to get around": goes. Chapter 6 cause 4 and chapter 16 line 10 both say it; chapter 3 is the third copy.
   * The six places, with their list: goes. Chapter 6 cause 5 owns it, and chapter 7 owns one place per fact.
   * "The process that replaced it kept two checks ... and one place per fact": goes. Chapter 6 §Where it went line 42 owns the outcome.
   * "The architecture was not at fault; KISS and YAGNI were lost, one reasonable addition at a time": stays. It is the chapter's lesson, and chapter 6 cause 3 points to chapter 3 for exactly these two principles.
   Source: chapters 3, 4, 6 and 16 as they stand, docs/04 §Numbers that prove.
3. One pointer to chapter 6, inside a sentence that already says something, never a sentence of its own (docs/04 §Teach, do not only show). The chapter has one today, at line 14; it moves, it is not added. The form follows `stack-rule-once` decision 3, a non-owner pointing to the owner as a parenthesis, `(chapter 6 ...)` / `(o capítulo 6 ...)`. Source: docs/04 §Chapter pointers, work/done/stack-rule-once.md.
4. The heading `## What grew on Ninjobs` / `## O que cresceu na Ninjobs` stays: the queue line names it, and it is still what the section says. The opening paragraph (lines 3-5) and the Brooks paragraph (lines 16-18) stay word for word. Source: docs/06 line, docs/04 §Chapter shape.
5. The Portuguese edition keeps the chapter's feminine form, "Na Ninjobs", as its heading (line 7) and gain (line 255) write it. `stack-rule-once` decision 7 switched one line to "No Ninjobs" because the chapters it touched used that form; chapter 3 does not, and flipping line 9 alone would split the chapter against itself. The book uses both forms across chapters; one form for the whole book is a docs/03 question, not this line's. Source: book/pt 3, work/done/stack-rule-once.md.
6. No docs/03 term (Ninjobs is docs/03's `case`, KISS, YAGNI and DRY are named by the chapter as they stand), no new queue line, no split: one chapter, one section, one page. Source: docs/03, docs/05 §1.

**Behaviour.**

* A reader of chapter 3 §What grew on Ninjobs reads three sentences, then the Brooks paragraph unchanged (pt in parentheses):
  * "On Ninjobs, my own product, I let complexity grow, one reasonable addition at a time." ("Na Ninjobs, o meu próprio produto, eu deixei a complexidade crescer, uma adição razoável por vez.")
  * "I required the full layered form of the architecture on every feature, trivial forms included, so showing one field on a screen took eight files, and every delivery had to pass 29 checks that had never caught an error in the product." ("Eu exigia a forma completa, em camadas, da arquitetura em toda feature, formulários triviais incluídos, então mostrar um campo em uma tela levava oito arquivos, e toda entrega tinha que passar por 29 verificações que nunca tinham pegado um erro no produto.")
  * "The architecture was not at fault; KISS and YAGNI were lost (chapter 6 tells what went wrong and how the process restarted)." ("A culpa não era da arquitetura; KISS e YAGNI se perderam (o capítulo 6 conta o que deu errado e como o processo recomeçou).")
  /apply may polish within these limits: three sentences at most; the eight files, the 29 checks with "never caught an error in the product", the architecture not at fault and KISS and YAGNI lost all kept; the pointer inside the third sentence; nothing of chapter 6's causes or outcome added back.
* Chapter 3's opening (lines 3-5), heading (line 7), Brooks paragraph and its note, every later section, the gain (en 254, pt 255) and the key points are unchanged.
* Checked, both editions, on `book/en/03-simplicity-and-results.md` and `book/pt/03-simplicity-and-results.md`: `grep -n -i "six places\|seis lugares"` finds nothing; `grep -n -i "two checks\|duas verificações"` finds nothing; `grep -n -i "cheap to get around\|fáceis de contornar\|costly to satisfy\|caras de satisfazer"` finds nothing; `grep -n -i "eight files\|oito arquivos"` finds one line, in §What grew on Ninjobs; `grep -n "29"` finds two lines, that section and the gain; `grep -n "chapter 6\|capítulo 6"` finds one line, the section's third sentence.
* Chapter 4 line 222's "one field took eight files (chapter 3)" still finds the eight files in chapter 3; chapter 6 cause 3's pointer to chapter 3 for KISS and YAGNI still finds them lost in chapter 3's opening section.
* Fails: one edition changed and not the other; the eight files cut (chapter 4 line 222 then points to nothing); the 29 checks cut from the section or the gain; "costly to satisfy", the six places or the two kept checks still in chapter 3; the pointer to chapter 6 standing as a sentence of its own, or two pointers to chapter 6; the opening paragraph, the heading or the Brooks paragraph changed; any edit to chapters 4, 6 or 16; "No Ninjobs" in pt chapter 3.

**Contract.**

* Files: `book/en/03-simplicity-and-results.md`, `book/pt/03-simplicity-and-results.md`; no other file.
* Sections and lines (same in both editions): §What grew on Ninjobs lines 9-14, six lines, become three; lines 3-5, 7, 16-18 and everything after unchanged. Line numbers as of the working tree on 2026-10-17, with `pt-placeholders` `[>]` and not yet applied (it touches chapters 11, 13, 19 and 21).
* Terms of docs/03: none new. Sources: none added or removed; `[^brooks-silver-bullet]` stays where it is. Cases: Ninjobs by name, through its published numbers (eight files, 29 checks), as docs/00 §Mechanics and docs/03 allow; no Case A or Case B passage. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line `[>]` by the driver, `[*]` when /apply starts, `[x]` by /apply. No new queue line.
* Gain untouched: chapter 3 keeps its one gain section and its five key points, so `one-gain-section` is not reopened.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same chapters.**

* `pt-placeholders` (`[>]`): chapters 11, 13, 19 and 21; no file in common.
* `ch04-parnas` (`[ ]`): chapter 4, whose line 222 leans on chapter 3 keeping the eight files, which this page keeps.
* `batch-propose` (`[ ]`, M16): chapter 19; no file in common.

**Out of scope.**

* Chapter 6's five causes and §Where it went: the story, told once, left whole (`stack-rule-once` decision 2 leans on it too).
* Chapter 3's gain and its 29 checks: the gain's one number; the checker marked the reuse of numbers weak.
* Chapter 16 line 10's "costly to satisfy and cheap to get around": the governor's own evidence, not this finding.
* One Portuguese gender for Ninjobs across the book: a docs/03 question for its own line.
* Chapter 3's other sections: not the finding.

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapter 3 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number still sourced (Ninjobs's numbers counted by the author, as the prologue says); `make verify` green, disclosure scan included; no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, the section draws on no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Divergences.**

1. The Behaviour's `grep -n "29"` finds three lines in each edition, not two: the section, the gain and the `[^dart-core]` note, whose access date is 2026-09-29. The note matched before this delivery too and is not a Ninjobs number; the 29 checks stand in two lines, as the page means.

2. The second sentence takes a semicolon before the 29 checks instead of the Behaviour's ", and" (pt: "; toda entrega" for ", e toda entrega"). The review showed that "so" could read as covering both clauses, making the architecture the cause of the 29 checks, which chapter 6 lists as a separate cause. Every element the Behaviour requires stays.

**Decisions taken in /apply.**

1. The three sentences are the Behaviour's in both editions, polished only as Divergence 2 says. Recommended option, no question asked (batch run).

**Proof.**

* Both editions, §What grew on Ninjobs lines 9-11: three sentences; lines 3-5, 7 and the Brooks paragraph unchanged; the pt heading and line 9 keep "Na Ninjobs".
* The Behaviour's greps: "six places", "two checks" and "costly to satisfy"/"cheap to get around" and their Portuguese find nothing; "eight files"/"oito arquivos" finds line 10; "chapter 6"/"capítulo 6" finds line 11 only; "29" finds line 10, the gain and the note's date (Divergence 1).
* No change to chapters 4, 6 or 16; chapter 4's pointer to chapter 3's eight files and chapter 6's pointer to chapter 3's KISS and YAGNI still land.
* `make verify`: green. `make book`: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Review.** A read-only Opus agent read this delivery's diffs against the page and docs/04 (docs/05 §5). Nothing breaks the page, docs/04 or AGENTS.md: the greps, the pointers from chapters 4 and 6, the pointer to chapter 6 and the Portuguese all check. Two notes: the "so" in the second sentence could read as causing the 29 checks, fixed (Divergence 2); the gain's line numbers in the decisions (en 254, pt 255) are as of before the edit, now en 251 and pt 252, left as written since the decisions record the page as proposed. No new queue line.

```commit
docs(ch03-opening): open chapter 3 without retelling chapter 6

- What grew on Ninjobs says it in three sentences, in both editions
- keeps the eight files, the 29 checks and KISS and YAGNI lost
- leaves the causes and the restart to chapter 6, pointed to once

work/done/ch03-opening.md
```
