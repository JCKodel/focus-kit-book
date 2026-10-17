# line-rule-once

**Objective.** A reader learns the one-sentence queue line and why it is one sentence in one place, chapter 11 §The queue, and meets it in chapters 13 and 22 only as the fact each of them owns, `/apply` reading the whole queue and what that read costs, with a pointer to chapter 11, in both editions. Found by `m15-review` (work/done/m15-review.md, B9: "13:23 and 22:61: the one-sentence line rule, owned by 11. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. Which chapter owns the rule: chapter 11, en line 25, pt line 27, "the kit asks for one sentence ... every word on a line is read by every definition", with the Ninjobs numbers that prove it. Chapter 11 teaches the queue; chapters 13 and 22 already point to it. Source: m15-review B9, chapter 11, AGENTS.md (a rule said once in the chapter that owns it).
2. What in chapter 13 is not the duplicate and stays: line 22, `/apply` reads the whole queue, why, and that it names the next free line; that is chapter 13's own fact about its command. What goes is line 23's restatement of why the line is one sentence ("the queue grows with every delivery, and each line costs what one sentence costs"). Source: chapter 13, docs/04 §Chapter pointers.
3. Chapter 13 keeps one sentence, not none: it carries the one thing chapter 11 does not say, that a line's words are read by every build as well as by every definition, and leans on chapter 11's exact sentence, so the pointer back is allowed (docs/04 §Chapter pointers: a pointer back that leans on a specific detail; §Teach, do not only show: never a sentence that is only a pointer). Cutting line 23 whole was the alternative, closer to "said once" but leaving the reader of chapter 13 without the reason the whole read stays cheap. Source: docs/04.
4. Chapter 22 keeps its own claim, that the queue read rides along on every call and grows by a sentence per delivery, not by a page: that is the cost, which chapter 22 owns. What goes is the rule's restatement inside it ("the queue grows with every delivery, so each line holds one sentence"); the rule is named once, as chapter 11's. Source: chapter 22, docs/04 §Chapter pointers.
5. Chapter 22's key point on "one-sentence queue lines" (en 104, pt 105) stays: it summarises chapter 22's own claim about cache reads, not the rule. Source: chapter 22, `one-gain-section` (key points that summarise, not repeat a gain).
6. Pointer form: the chapters' own, plain "chapter 11" / "capítulo 11" in the sentence, as both lines write it today; no link added. Source: chapters 13 and 22, docs/04 §Chapter pointers names no form.
7. No docs/03 term (the queue line is already docs/03's `line`), no new queue line, no split: two chapters, two sentences, one page. Source: docs/03, docs/05 §1.

**Behaviour.**

* A reader of chapter 13 §What it reads reads line 22 unchanged, then, as line 23 (pt in parentheses): "So every word on a line is read by every build too, not only by every definition (chapter 11)." ("Então cada palavra de uma linha é lida também por toda construção, e não só por toda definição (capítulo 11).") Line 24, the `[*]` mark, follows unchanged. /apply may polish within these limits: one sentence, the build named, the pointer inside it, no restated reason for one sentence.
* A reader of chapter 22 §Why the page and the documents keep sessions small reads at line 61: "The queue is among those documents, whole, and what it reads at the start rides along on every call of the session; with chapter 11's one-sentence line, that read grows by a sentence per delivery, not by a page." ("A fila está entre esses documentos, inteira, e o que ele lê no começo vai junto em cada chamada da sessão; com a linha de uma frase do capítulo 11, essa leitura cresce uma frase por entrega, não uma página.") The rest of the section and key point en 104 / pt 105 stay.
* Checked, both editions: `grep -n -i "queue grows\|fila cresce" book/en book/pt` finds nothing; `grep -n -i "costs what one sentence costs\|custa o que custa uma frase"` finds nothing; `grep -n "chapter 11\|capítulo 11"` finds exactly one match on line 23 of chapter 13 and one on line 61 of chapter 22; chapter 11 lines en 25-27 / pt 27-29 unchanged.
* Fails: one edition changed and not the other; chapter 13 loses that `/apply` reads the whole queue; a pointer that stands as a sentence of its own; chapter 22 loses that the read rides along on every call or grows by a sentence per delivery; either chapter still says why a line is one sentence; any edit to chapter 11.

**Contract.**

* Files: `book/en/13-apply.md`, `book/pt/13-apply.md`, `book/en/22-cost-and-where.md`, `book/pt/22-cost-and-where.md`; no other file.
* Sections and lines (same in both editions): chapter 13 §What it reads line 23 rewritten (line 22 and 24 unchanged); chapter 22 §Why the page and the documents keep sessions small line 61 rewritten. Line numbers as of the working tree with `stack-rule-once` staged; that delivery left chapter 22 line 61 as it is.
* Terms of docs/03: none new. Sources: none added or removed. Cases: none; the Ninjobs numbers stay in chapter 11. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line `[>]` by the driver, `[*]` when /apply starts, `[x]` by /apply. No new queue line.
* Gains untouched: chapters 13 and 22 keep their gain sections and key points, so `one-gain-section` is not reopened.

**Deliveries in flight on the same chapters.**

* `stack-rule-once` (done, staged, not committed): chapter 22 lines 78 and 80; no line in common.
* `slice-paths`, `code-width`, `pt-placeholders` (`[ ]`): chapter 13 at other lines (87, 94, 167-176); no line in common.

**Out of scope.**

* Chapter 11's rule, its reason and the Ninjobs numbers: the owner, as it stands.
* Chapter 13's other reads (the page, `AGENTS.md`, docs/01, docs/04, docs/05): not the finding.
* Chapter 22's token table, its other sections and key point 104 / 105: chapter 22's own claims.

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapters 13 and 22 still open with their value, keep their gain, no filler and nothing useful cut.
* [x] Every number still sourced; `make verify` green, disclosure scan included; no em dash.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Divergences.**

* Chapter 13 line 23 polished within the Behaviour's limits, after the review: en "read by every build as well as by every definition" (the draft said both "too" and "not only"); pt opens with "Por isso," and says "tanto quanto", since the next sentence already opens with "Então". One sentence, the build named, the pointer inside it, no restated reason.

**Omissions.** None.

**Proof.**

* `grep -n -i "queue grows\|fila cresce" book/en book/pt` and `grep -n -i "costs what one sentence costs\|custa o que custa uma frase" book/en book/pt` find nothing.
* `grep -n "chapter 11\|capítulo 11"` in chapters 13 and 22 finds 13:23 and 22:61 in each edition, nothing else; chapter 11 has no diff.
* `make verify` green (build, parity, em dash, prose, links, disclosure); `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Review.** A read-only Opus agent read the staged diff and this line's hunk of docs/06 against this page and docs/04.

* docs/06 line still `[*]` and not staged: expected at review time; fixed by the last edit, `[x]` staged by its hunk.
* pt 13:23 opened with "Então" like 13:24: fixed (Divergences).
* en/pt 13:23 said "too" and "not only" at once: fixed in both editions (Divergences).
* Decision 3 says chapter 13 keeps "the reason the whole read stays cheap", which the new sentence does not carry: accepted. Chapter 13's sentence now says what the whole read costs a build; why it stays cheap, a sentence per delivery, is chapter 22's claim at 22:61, so the book keeps it once. Decision 3 stays as written, as the batch recorded it.
* Chapter 22 and chapter 11: no findings.

```commit
docs(line-rule-once): say the one-sentence line rule once, in chapter 11

- chapter 13 keeps that /apply reads the whole queue and says every build reads a line's words too, pointing to chapter 11
- chapter 22 keeps the read riding along on every call, growing a sentence per delivery, with chapter 11's one-sentence line
- the rule's reason and the Ninjobs numbers stay only in chapter 11
- both editions

work/done/line-rule-once.md
```
