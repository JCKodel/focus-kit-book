# docs04-code-layout

**Objective.** A writer, person or agent, who adds or edits a code block finds in docs/04's rule for code how the author lays code out, declarations and `{ }` blocks set apart by blank lines, and every TypeScript block of the book already reads that way in both editions. From commit 8507633 (2026-10-18, `style(code-blocks)`), in which the author reformatted the code of chapters 3 to 5 that way because it reads better to them, and said the book needs no sentence about it.

**Decided without the author.** The batch had no one to answer; each choice is the recommended one. The layout itself and "no comment in the book" are the author's decisions, not these.

1. *The rule, derived clause by clause from the commit's chapter blocks.* At the top level, one blank line between declarations, and a comment sits on its declaration with no blank line (en 03:101-103, pt 03:102-104, untouched by the commit and already so). Inside a body: a declaration, or a run of consecutive one-line declarations, has a blank line after it, and before it when a statement precedes it (en/pt 04 `lendRequested`, en/pt 05 `it` bodies and `fake`); a declaration or block whose `{ }` spans lines is set apart on both sides (en/pt 05 `const repositories = fake({ ... })`); the `return` that ends a body has a blank line before it (en/pt 03 `dueDate`, en 03 `query`'s catch, en/pt 04 `lendRequested`, en/pt 05 `fake`); a blank line is empty, no tab or space. Consecutive one-line declarations stay together: no chapter block has two in a row, so this clause comes from the commit's draft-note example (`returnCopy`: `const now`, `const fine`, `const returned` with no blank between). Source: commit 8507633.
2. *A guard and its return stay two lines.* A body that is one one-line guard (`if (...) return ...;`) and the `return` after it has no blank line: the author reformatted chapters 3 and 4 in that commit and left `mayBorrow` (en 03:121-126, pt 03:122-127) and `stateOf` (en 04:163-166, pt 04:165-168) as they were, and `ch03-literal-type-comment` quotes `mayBorrow` "exactly as written" with no blank before `return ok(member)`. The commit's draft note has the opposite once (`daysOverdue`, a blank before its last `return` after a guard, in a body that opens with a declaration); the author can overrule this clause in review. Source: commit 8507633, `work/ch03-literal-type-comment.md`.
3. *Braces are left out of the rule.* The commit braced a one-line `for` in one work/done page and kept `for (...) await ...;` on one line in another; the book has no one-line `if`, `for` or `while` whose body is not `return`, `throw` or `continue` (counted on 2026-10-18 over every `ts` block), so the rule covers what the book has. Source: commit 8507633, the count.
4. *Other chapters: none to bring in line.* The book's 22 `ts` blocks are all in chapters 3, 4 and 5 (7, 2 and 2 per edition); no untagged block holds code (counted on 2026-10-18: no `function`, `const` or `=>` in one). Checked against decisions 1 and 2, the commit missed two things, and this delivery fixes both in both editions as ADR-0004 asks:
   * pt 03:204-205: `consultar`'s catch has no blank line between `const mensagem` and `return err(...)`, where en 03:203-205 has one: a parity miss.
   * Six blank lines in the reformatted blocks hold spaces: en 03:204, en 04:188, en 05:110, pt 03:35, pt 04:190, pt 05:110. They become empty lines, which also keeps the blocks tab-indented.
5. *No check script.* This is the first layout rule for code (`width` measures columns, another rule); 22 hand-written blocks in three chapters are read at review, and decision 2 is judgement, not a pattern. docs/04 marks it "(first: `docs04-code-layout`)", so the second layout rule or the second layout miss after this delivery brings a check (AGENTS.md, abstraction on the second occurrence). The mechanical part, no whitespace-only line in the book, is a grep in Behaviour's apply-time checks. Source: AGENTS.md, docs/04 §Tests.
6. *Where the rule goes in docs/04.* As its own continuation line of the Code bullet, after "Code is never presented as the output of a run." (docs/04:51), not inside docs/04:50, so it shares no line with `pt-identifiers-choice`'s edit of that line's parenthesis. The origin is cited as the author's reformat of chapters 3 to 5, by date, as docs/04 cites by slug and never by commit hash. Source: docs/04 §Writing the book (the `first:` form), docs/05 §7.
7. *No sentence in the book.* The chapters say nothing about layout; the author said none is needed. Source: commit 8507633's request.
8. *`work/done/` is not rewritten.* The commit touched two pages there; they are the record of what was decided, and this rule reads only `book/` (`m16-review` decision 4). Source: work/done/m16-review.md.
9. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* A writer opening docs/04 finds, after "Code is never presented as the output of a run.", this line, word for word:

  > Code is laid out as the author writes it, declarations and `{ }` blocks set apart by blank lines: at the top level, a blank line between declarations, and a comment on its declaration with none; in a body, a blank line after a declaration or a run of one-line declarations, and before it when a statement comes first, a blank line on both sides of a declaration or block whose `{ }` spans lines, and a blank line before the `return` that ends the body, except where the body is one guard and that `return`; a blank line is empty (first: `docs04-code-layout`, the author's reformat of chapters 3 to 5 on 2026-10-18).

* The reader of chapter 3 in Portuguese sees `consultar`'s catch as the English edition shows `query`'s: `const mensagem = ...;`, an empty line, `return err({ codigo: "BancoDeDadosFalhou", mensagem });`.
* Every other block reads as it does today, `mayBorrow` and `stateOf` included.
* Checked at apply time:
  * `grep -rnE "^[[:space:]]+$" book/` prints nothing.
  * For each `ts` block of chapters 3 to 5, the positions of its empty lines in English match its Portuguese twin's (a one-off comparison by the applier, no script added).
  * Each block of chapters 3 to 5, read against the docs/04 line, breaks none of its clauses.
  * `git diff --stat book/` shows only en 03, 04, 05 and pt 03, 04, 05: one line changed in each for the six whitespace lines, plus one line added in pt 03.
* Fails: a sentence about layout in a chapter; a blank line added to `mayBorrow` or `stateOf`; a block reformatted beyond the seven lines named; a `work/done/` page edited; the rule written inside docs/04:50's sentence; a new script or `make` target; an em dash.

**Contract.**

* Files: `docs/04-Conventions.md`, one line inserted after docs/04:51 (at /propose), the text as Behaviour quotes; `book/pt/03-simplicity-and-results.md`, one empty line inserted between pt 03:204 and 205, and pt 03:35 emptied; `book/en/03-simplicity-and-results.md` 204, `book/en/04-focus.md` 188, `book/en/05-testing-each-piece.md` 110, `book/pt/04-focus.md` 190, `book/pt/05-testing-each-piece.md` 110, each emptied of its spaces. Nothing else in these files.
* Terms of docs/03: none. Sources: none added. Cases: none. Code: no line of code changed, only blank lines. Exercises: none (ADR-0017).
* docs/00, docs/01, docs/02, docs/03, docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line. `scripts/`, `Makefile`: no change (decision 5).

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `pt-identifiers-choice` edits docs/04:28 and the parenthesis of docs/04:50; this line inserts after docs/04:51, a line apart. `ch05-test-time` edits docs/04:23, a hunk apart. Whichever lands second reads docs/04 as the first left it.
* `ch03-literal-type-comment` adds a comment above `type Refusal` / `type Recusa` with no blank line between them and keeps `mayBorrow` as it is: it already follows this rule (its decision 2), and decision 2 here keeps its quoted block valid. It shifts pt 03:204-205 by three lines; /apply finds the catch by its text.
* `pt-identifiers-choice` edits pt 03:25, `ch03-error-languages` the section `Exceção, recusa, erro`, `early-no-forward-links` pointers in chapters 3 to 5, `ch04-focus-optional` and `ch04-scalable-meaning` chapter 4's prose, `ch05-test-time` and `ch05-random-values` chapter 5's prose: none touches a blank line named here; whichever lands second finds the lines by their text, not their number.

**Out of scope.**

* A sentence in the book about layout: decision 7.
* Blank lines in `mayBorrow` and `stateOf`: decision 2.
* A rule on braces: decision 3.
* `work/done/` pages: decision 8.
* A check script: decision 5.

**Done when.**

* [ ] docs/04 holds the line Behaviour quotes, after docs/04:51.
* [ ] The seven blank lines of the book fixed, both editions; Behaviour's checks give what they name.
* [ ] Chapters 3 to 5 still open with their value and keep their gain; no text changed.
* [ ] Every number sourced: none added.
* [ ] `make verify` green: edition parity, prose rules, width, links, disclosure scan, no em dash.
* [ ] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunks of docs/04 and docs/06, commit message in a `commit` block.
