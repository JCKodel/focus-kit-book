# ch15-range-pointer

**Objective.** A reader of chapter 15 §Read the code since the base, by areas learns what `<base>..HEAD` holds in the sentence that shows it, and is pointed to chapter 18 only for `HEAD`, the one part of it chapter 18 teaches, instead of being sent to chapter 18 for a range it never shows; both editions. Found by `m16-review` (work/done/m16-review.md, chB-2: "15:50 (pt :51) says chapter 18 teaches `<base>..HEAD`; chapter 18 has no `git diff` and no range." Seen).

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. Chapter 15 teaches the range, and chapter 18 is not given one. The queue line allows either. The sentence at 15:50 already says what `git diff` prints and that `<base>..HEAD` is "the range from the base to the last commit"; what it lacks is what the range holds and what `HEAD` is. Chapter 18 has no `git diff` and no range (`grep -n "diff\|\.\." book/en/18-git-essentials.md` finds neither); adding one there is a new section in a chapter no finding names, for a fact one clause here holds. Source: chapters 15 and 18 as they stand, docs/04 §Chapter pointers ("a forward pointer follows a sentence that already says something").
2. The pointer stays, narrowed to `HEAD`. Chapter 18 §Branches and tags teaches it ("`HEAD` is the commit you are on: usually the last commit of your branch, which moves with it", en 18:70, pt 18:70), and no chapter before 15 defines it (chapter 8:78 shows it inside the kit's report block only). docs/04 §Chapter pointers keeps a forward pointer that names a term the reader has not been taught, once per chapter; chapter 15 has no other pointer to chapter 18.
3. The pointer stays in plain words, with no link, as every chapter pointer in chapter 15 is written today (chapters 4, 13, 14 and 20 named in plain words). Source: chapter 15 as it stands.
4. Only the one sentence changes. Line 52's `git diff --stat <base>..HEAD` leans on it and needs nothing more. Source: chapter 15 as it stands.
5. No docs/03 term (no row for `HEAD` or range exists, and the sentence defines both where it uses them, as chapter 15 does today), no new queue line, no split.

**Behaviour.**

* A reader of chapter 15 §Read the code since the base, by areas reads, in place of the sentence that ends "(chapter 18 teaches it).":
  * en: "`git diff <base>..HEAD` shows them: `git diff` prints what changed between two commits, line by line, and `<base>..HEAD` is the range from the base to `HEAD`, the commit you are on, usually the last (chapter 18 teaches `HEAD`), so the diff holds every change made after the base, whichever delivery made it."
  * pt, §Leia o código desde a base, por áreas: "O `git diff <base>..HEAD` mostra todas: o `git diff` imprime o que mudou entre dois commits, linha a linha, e `<base>..HEAD` é o intervalo da base até o `HEAD`, o commit em que você está, em geral o último (o capítulo 18 ensina o `HEAD`), então o diff traz toda mudança feita depois da base, seja qual for a entrega que a fez."
* Checked on `book/en/15-closing-a-milestone.md` and `book/pt/15-closing-a-milestone.md`: `grep -c "chapter 18 teaches it"` (pt `grep -c "o capítulo 18 o ensina"`) gives 0; `grep -cF 'chapter 18 teaches `HEAD`'` (pt `grep -cF 'o capítulo 18 ensina o `HEAD`'`) gives 1; `grep -c "chapter 18"` (pt `"capítulo 18"`) gives 1.
* The rest of chapter 15 is unchanged, lines 20 and 150 (pt 20 and 153) included.
* Fails: one edition changed and not the other; the pointer still saying chapter 18 teaches the range; a range or `git diff` added to chapter 18; any other line of chapter 15 changed; an em dash.

**Contract.**

* Files: `book/en/15-closing-a-milestone.md`, `book/pt/15-closing-a-milestone.md`; no other file.
* Section and line: §Read the code since the base, by areas / §Leia o código desde a base, por áreas, its second paragraph's first sentence (en line 50, pt line 51 in the working tree of 2026-10-18; the text is the locator, the number a courtesy).
* Terms of docs/03: none new. Sources: none added or removed. Cases: none; no Case A, Case B or Ninjobs passage. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same chapter.**

* `ch15-review-base` (M17, after this page): chapter 15 §The review is a delivery (line 20) and line 150 (pt 153), what the base is. This page changes line 50 (pt 51) only and says nothing of which commit the base is, so the two pages touch different hunks; `ch15-review-base` starts from this page's text.

**Out of scope.**

* What the base is: `ch15-review-base`'s.
* A section on `git diff` or ranges in chapter 18: decision 1.
* Chapter 8:78, the kit's report block: the command's output, quoted as it is (docs/04 §The kit as it is).

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapter 15 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: links, edition parity, width, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, the change draws on no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Proof.** `git diff --numstat` of the two chapters: 1 insertion and 1 deletion each, en line 50 and pt line 51, which now read as Behaviour says. Behaviour's greps: `chapter 18 teaches it` and `o capítulo 18 o ensina` give 0; ``chapter 18 teaches `HEAD` `` and ``o capítulo 18 ensina o `HEAD` `` give 1; `chapter 18` and `capítulo 18` give 1. `make verify` green: build, parity, em dash, prose, width, links, disclosure. `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.** None.

**Omissions.** None.

**Decisions taken in /apply.** None beyond the page's.

**Review.** Delivery review by a read-only Opus agent on the diff of both chapters, this delivery's line of docs/06 and this page, against the page and docs/04. No findings: both sentences match Behaviour word for word and no other line changed; the greps give the named results; the new clause agrees with chapter 18:70 and keeps lines 51 and 52 reading; the pointer names a term not yet taught, once, after a sentence that already says something (docs/04 §Chapter pointers); the Portuguese says what the English says.

```commit
docs(ch15-range-pointer): say what the range holds and what HEAD is

- Chapter 15, both editions: `<base>..HEAD` runs to `HEAD`, the commit you are on, and holds every change after the base
- The pointer to chapter 18 names `HEAD`, the part it teaches

work/done/ch15-range-pointer.md
```
