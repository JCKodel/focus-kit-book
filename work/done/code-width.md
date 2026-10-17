# code-width

**Objective.** A reader of either PDF reads every queue, page, commit message, prompt and rules file the book shows in a code block without a row wrapping, because no such block runs past 74 columns, and `make verify` fails the next one that does. Found by `m15-review` (work/done/m15-review.md, A10 and B12: "code blocks over 74 columns: en and pt 1:74, 8:17, 10:12, en 11:45, pt 11:46-55, en 14:37, pt 13:94, pt 15:30-31, en and pt 21:32-45. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. A check guards the width. docs/04 **Width of a block** already names the first occurrence, chapter 17's work record, which the PDF broke and was fixed by hand; this finding is the second, 24 rows in eight chapters, so the rule becomes a check (AGENTS.md: abstraction on the second concrete occurrence). It is `scripts/check_width.py`, rule `width`, run by `make verify` after prose and before links, which needs the network (docs/01 `make verify` row). Source: docs/04; AGENTS.md; docs/01.
2. TypeScript is not measured: docs/04 says "TypeScript may wrap", and pdf.css starts a wrapped line at the margin. Every other fenced block is measured, whatever its info string (none, `markdown`, `text`, `commit`), since each holds a text artifact docs/04's rule covers. The finding lists exactly the non-TypeScript rows; the TypeScript rows over 74 (chapters 3, 4, 5) stay. Source: docs/04 **Width of a block**; pandoc/pdf.css; m15-review A10, B12.
3. The check reads the files the prose check reads: both editions and both READMEs. The READMEs are clean today, so including them costs nothing, and the rule does not depend on where a block is printed. Source: scripts/check_prose.py `language_of`; docs/01.
4. A column is a character (a code point: `·`, `ç`, `ã` count one each); a tab runs to the next multiple of 8, the CSS default `tab-size`, since pdf.css sets none. No measured block holds a tab today. Source: pandoc/pdf.css (`pre`: 8pt, `white-space: pre-wrap`, no `tab-size`); docs/04 (74 columns is what an A5 page holds at the PDF's code size).
5. Fences are read one way by every check: a block opens on a run of three or more backticks or tildes after any indent and closes on a line that starts, after its indent, with the same run; so chapter 11's four-backtick `markdown` block measures its inner three-backtick queue. That rule lives in `mask` in scripts/markdown.py today (first occurrence); the width check is the second reader, so the opening pattern and the closing test move into markdown.py as names both use. Source: scripts/markdown.py `mask`; docs/01 (markdown.py is the Markdown reading shared by the scripts); AGENTS.md.
6. How a row is brought under 74 depends on what it is. A paragraph or a bullet in a Markdown or text artifact wraps at a word boundary, a bullet's continuation indented two spaces, with its words unchanged (chapter 11's paragraph and chapter 21's Objective already wrap inside their blocks). A row that is one line by its own rule is shortened, keeping its meaning: a queue line (one sentence per line, chapter 11) and a commit bullet (docs/05 §6: one-line bullets). The install sentence of chapters 8 and 10 breaks after its address: the address stays whole, so a reader can still copy it, and the paragraph after it already explains the address. Source: docs/04; docs/05 §6; chapters 8, 10, 11, 21.
7. Portuguese rewordings keep docs/03's words and the verbs the chapter already uses: `devolver-livro` keeps `registra` (docs/03 fixes "data de devolução"; `pt-fixed-terms` is open precisely against drift), and the commit bullet keeps the unique index the English bullet names. Source: docs/03 running example row; m15-review A6, A7; chapter 13.
8. English chapter 14 changes one word ("which provider?" to "what provider?") and the Portuguese row, already under 74, stays: the meaning is the same in both editions, which is what ADR-0004 asks of a change to one edition. Source: ADR-0004; chapter 14.
9. Any row over 74 that appears before /apply runs, in any chapter, outside the eight the line names (a later delivery lengthened it), is fixed in this delivery by the same policy: verify cannot be green otherwise, and that is the queue line's promise. Source: docs/05 §5 Verify.
10. No docs/03 term, no new queue line, no split: one script, a shared pattern, and 24 rows of text fit one page. Source: docs/03; docs/05 §1.

**Behaviour.**

Rows are found by their words; line numbers are as of the working tree when this page was written. The proposed text is what /apply writes unless a better wording keeps the meaning, the terms of docs/03 and the 74 columns.

* Chapter 1, the rules file (en 74, pt 74): the description paragraph wraps after "records" (en) and after "membros; um" (pt), words unchanged:
  * en: "A small library lends copies of its books to members; a librarian records" / "each loan and each return."
  * pt: "Uma pequena biblioteca empresta exemplares dos seus livros a membros; um" / "bibliotecário registra cada empréstimo e cada devolução."
* Chapters 8 (17) and 10 (12), both editions, four blocks: "Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md and do what it says." becomes two lines, "Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md" / "and do what it says." The sentence stays in English in the Portuguese edition, as it is today (a command the reader says).
* Chapter 11, the milestone (en 44-46, pt 46-48): the paragraph rewraps at 74, words unchanged:
  * en: "When it closes, a librarian can register books, their copies and members," / "lend a copy to a member for 21 days and record its return; a member with" / "an overdue book or a suspended membership is refused."
  * pt: "Quando ele fecha, uma bibliotecária consegue cadastrar livros, seus" / "exemplares e membros, emprestar um exemplar a um membro por 21 dias e" / "registrar a devolução; um membro com um livro atrasado ou com a inscrição" / "suspensa é recusado."
* Chapter 11, pt queue (51, 54, 55), slug column unchanged:
  * `[x] esqueleto` row: "app e servidor vazios, npm run verify, tela capturada".
  * `[>] emprestar-livro` row: "a bibliotecária empresta, e as regras podem recusar".
  * `[ ] devolver-livro` row: "registra a devolução · after emprestar-livro".
* Chapter 13, pt commit block (94): "- Cria a tabela emprestimo, um empréstimo aberto por exemplar por índice único" becomes "- Cria a tabela emprestimo, um aberto por exemplar por índice único". The English bullet stays.
* Chapter 14, en queue (37): "blocked: which provider?" becomes "blocked: what provider?" (74 columns). The Portuguese row stays.
* Chapter 15, pt milestone paragraph (30-32) rewraps, words unchanged: "Quando ele fecha, um bibliotecário consegue emprestar um exemplar e" / "registrar a sua devolução, e um membro vê os seus empréstimos com a data" / "de devolução de cada um."
* Chapter 21, the page `librarian-guide` / `guia-do-bibliotecario` (en and pt 32, 33, 37, 45): each long row wraps at a word boundary, words unchanged; a bullet's continuation is indented two spaces (under the text after `* ` or `* [ ] `), the Contract sentence continues at the margin.
* The check, run as `python3 scripts/check_width.py`, each case on a scratch file in `book/en/` removed afterwards:
  * a bare block with a row of 75 characters prints `book/en/<file>:<line>: width: 75 columns; a code block keeps to 74 (docs/04)` and exits 1;
  * a row of exactly 74 characters, accents and `·` included, prints nothing;
  * a `ts` block with a row of 90 characters prints nothing;
  * a row of 75 characters inside a three-backtick block nested in a four-backtick `markdown` block is reported at its line;
  * a row of 75 characters inside a `commit` or `text` block is reported;
  * a row of 200 characters of prose outside any block prints nothing;
  * a row that starts with one tab followed by 67 characters (75 columns) is reported;
  * a row of 75 characters in a block in README.md is reported at `README.md:<line>`;
  * every finding of a run is printed before the exit, one line each.
* `make verify` runs width after prose and before links; with one offending row it stops at width.
* After the fixes, `python3 scripts/check_width.py` prints nothing on the tree, and `make verify` is green.
* Fails: a TypeScript row reported; an inner fence closing an outer longer one; a row counted in bytes, so an accent makes a 74-character row fail; a URL broken across lines; a queue line or commit bullet wrapped onto two lines; one edition fixed and not the other's matching row; a row's meaning changed, or a Portuguese term that is not docs/03's or the chapter's.

**Contract.**

* `scripts/check_width.py`: reads `repo_files()` filtered as the prose check filters (book/en/*.md, book/pt/*.md, README.md, README.pt.md); for each line inside a fenced block whose info string's first word is not `ts` or `typescript`, measures `len(line.expandtabs(8))` and, above 74, prints `<path>:<line>: width: <n> columns; a code block keeps to 74 (docs/04)`. Exit 1 when anything is printed, else 0. Docstring in the form of the other checks. The limit 74 and the tab size 8 are named constants with a comment pointing to docs/04 and pdf.css.
* `scripts/markdown.py`: the fence rule `mask` uses becomes shared names, an opening pattern that captures the run and the info string, and a closing test (a line that starts, after its indent, with the opening run), used by both `mask` and `check_width.py`. `mask`'s output is unchanged (the prose and link checks see the same text).
* `Makefile` `verify`: `python3 scripts/check_width.py` after `check_prose.py`, before `check_links.py`.
* docs/01: a row `scripts/check_width.py  every fenced block but TypeScript, in both editions and both READMEs, keeps to 74 columns, a tab to the next multiple of 8 (rule "width")`; the markdown.py row names the fence pattern shared by mask and the width check; the `make verify` row reads "build, then parity, then em dash, then prose, then width, then links, then disclosure".
* docs/04 **Width of a block**: adds that `make verify` holds it (`width`), a column being a character and a tab running to the next multiple of 8 as in the PDF, every fenced block measured but `ts`.
* docs/05 §5 Verify: the list of checks adds "the block width check" after the prose rules.
* Chapters, both editions: the rows of Behaviour, nothing else. No section, docs/03 term, source or case is added; no Case A or Case B passage is touched.
* No docs/03 change and no docs/06 line beyond this delivery's own mark.
* Edges with other lines: `slice-paths` (chapters 13 and 14 at other lines), `pt-fixed-terms` (pt 11 at 100 and 148, pt 14 at 34, the same queue block as the en 14 row this page changes, which is not that row), `pt-placeholders` (pt 11:19, pt 13:167-176, pt 21:38, next to pt 21:37 in the same block) and `ch21-counts-once` (chapter 21 at 59-87) touch nearby text. /apply finds rows by their words. If another session's unstaged edit sits in the same block as a row this page changes, /apply stops and reports per docs/05 §4 and §6 instead of staging a mixed hunk; run `code-width` and `pt-placeholders` one after the other, either order.

**Out of scope.**

* TypeScript rows over 74 (chapters 3, 4, 5): docs/04 lets TypeScript wrap.
* Markdown tables outside code blocks: docs/04 names them in the rule, but they are not fenced and their rendered width is not a column count.
* The EPUB and the site: their width follows the reader's screen; 74 is the PDF's.
* Inline code in prose: it wraps with the sentence.
* Any other wording in the eight chapters, including what `pt-fixed-terms`, `pt-placeholders`, `ch10-commit-message` and `ch21-counts-once` will change: their own lines.

**Done when.**

* [x] Every row of Behaviour changed in both editions as described, nothing else in the chapters.
* [x] `scripts/check_width.py` exists, each check case of Behaviour run and its output recorded on this page, scratch files removed.
* [x] markdown.py shares the fence rule with `mask`; the prose and link checks give the same result as before.
* [x] Makefile, docs/01, docs/04 and docs/05 §5 updated as the Contract says.
* [x] Both editions written; no em dash; no narrated run; nothing private.
* [x] `make verify` green, the width check included.
* [x] `make book` builds both PDFs and EPUBs; in both PDFs none of the changed blocks wraps a row (an eye check of chapters 1, 8, 10, 11, 13, 14, 15 and 21); the delivery ends by giving the author both PDF paths.

**Proof.** Before editing, a scan of the tree found exactly the 24 rows of Behaviour and no other. Each check case run as `python3 scripts/check_width.py` (or its `check` on the scratch file), the scratch files then removed:

* a bare block with a 75-character row: `book/en/zz-w1.md:4: width: 75 columns; a code block keeps to 74 (docs/04)`, exit 1;
* a 74-character row of `ç`, `·` and `ã`: nothing;
* a `ts` block with a 90-character row: nothing;
* a 75-character row in a three-backtick block inside a four-backtick `markdown` block: `book/en/zz-w4.md:7: width: 75 columns; ...`, its own line;
* a 75-character row in a `commit` block and one in a `text` block: `book/en/zz-w5.md:4` and `book/en/zz-w5.md:8`, both;
* a 200-character prose row outside any block: nothing;
* a tab followed by 67 characters: `book/en/zz-w7.md:4: width: 75 columns; ...`;
* a 75-character row in a block appended to README.md: `README.md:50: width: 75 columns; ...`, exit 1, README.md restored byte for byte;
* the full run with all scratch files printed the five findings, one line each, then exited 1.

`make verify` with a scratch pair in both editions (parity needs the pair) stops at width with both findings. `mask` before and after the change gives identical output on all 85 Markdown files of the editions, the READMEs and docs/, with and without link targets; the prose and link checks are green. After the fixes `python3 scripts/check_width.py` prints nothing and `make verify` is green (build, parity, em dash, prose, width, links, disclosure). `make book` builds `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` and both EPUBs; in the text of both PDFs every changed row of chapters 1, 8, 10, 11, 13, 14, 15 and 21 sits on its own line as written, with no wrapped row.

**Divergences.** English chapter 14 also changes its prose quote of the same suffix (line 75, "`· resume: propose · blocked: which provider?`" to "what provider?"), so the sentence still quotes the queue row it explains; the Portuguese quote, like its row, stays.

**Omissions.** None.

**Decisions taken in /apply.** The chapter 14 quote above, the one change outside Behaviour's rows, taken as the recommended option since a quote that no longer matches its row is wrong. The check skips no front matter or HTML comment separately: no fence sits in either today, and mask's comment rule is not the width rule's concern. The info string is compared lower-cased.

**Review.** Delivery review by a read-only Opus agent on this delivery's diffs against the page, docs/01 and docs/04: nothing breaks the page, docs/04 or this delivery's lines. `check_width.py` matches the Contract; `mask` gives identical output on 430 Markdown files; the chapters hold exactly Behaviour's rows plus the chapter 14 quote recorded above; no URL, queue line or commit bullet is wrapped. Three notes: the docs/06 mark was still `[*]` when it read (the last edit, done after it); pt 11's `esqueleto` row, "tela capturada", loses the "primeira" of the English "first screenshot", which became the queue line `pt-skeleton-first`; pt 13's "um aberto por exemplar" drops the noun "empréstimo" but still reads as "one open loan per copy", left as the page wrote it.

```commit
feat(code-width): keep every code block but TypeScript to 74 columns

- scripts/check_width.py, rule width, run by make verify after prose
- markdown.py shares the fence rule between mask and the width check
- 24 rows in chapters 1, 8, 10, 11, 13, 14, 15 and 21 brought under 74
- docs/01, docs/04 and docs/05 name the check

work/done/code-width.md
```
