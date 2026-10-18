# ch03-literal-type-comment

**Objective.** A reader of chapter 3 who does not know TypeScript reads, in a comment on the refusal example of `## A pure function`, that `"HasOverdueBooks"` (pt `"TemLivrosEmAtraso"`) is a type whose only value is that exact string, so the compiler accepts it, and no other string, where a `Refusal` is expected, and a typo does not compile; the string written twice no longer reads as a magic string that should have been a constant. From the author's reading of the book on 2026-10-18: the example "reads to someone who does not know TypeScript as a magic string written twice, as if `Recusa` should be a constant that `err` returns. [...] The author chose a comment in the code, not prose, to say so."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one. A comment in the code, not prose, and the author's layout are the author's decisions, not these.

1. *What the comment claims.* `err<E>(error: E)` is generic: `err("HasOverdueBoks")` alone compiles. What rejects the typo is `mayBorrow`'s declared return type, `Result<Member, Refusal>`. So the comment says the type's only value is the string and that, where a `Refusal` is expected, as in the `err` below, the compiler accepts that string and no other; it does not say `err` itself restricts the string, which would be false. The queue line's "so err takes no other" is read as "the `err` in this function". Source: chapter 3's own `err` (en 03:146), the draft ("the compiler accepts only that exact string in `err`"), docs/04 (every claim true).
2. *Placement.* Three comment lines directly above `type Refusal = "HasOverdueBooks";` (en 03:121) and `type Recusa = "TemLivrosEmAtraso";` (pt 03:122), with no blank line between comment and declaration; the blank lines before (after `type Member`) and after (before `function`) stay. This is how chapter 3's other comment sits on its declaration (en 03:101-102), and the layout of commit 8507633. Source: the draft, chapter 3, commit 8507633.
3. *Once, at this block only.* The union `LendRefusal` / `RecusaDeEmprestimo` (en 03:231, pt 03:231) and the prose on `Result<Loan, LendRefusal>` (en 03:186) come later and read on this comment; they get no comment and no pointer to it. Source: docs/04 §Writing the book (one fact said once), `early-no-forward-links`.
4. *No prose change.* The chapter's opening sentence, its sections, its gain and its key points stay as they are: the author chose a comment, not prose. Source: the draft.
5. *No docs/03 term.* "String literal type" is the language's name for the feature and stays a phrase inside the comment, for the reader who wants to look it up; docs/03 has no `literal` row and the book uses the phrase nowhere else. The rows `refusal` and `running example` already give `Refusal`, `Recusa` and `TemLivrosEmAtraso`. Source: docs/03 (rows `refusal`, `running example`).
6. *No docs/04 change.* This is the book's first code comment that explains a language feature to a reader who does not know the language; the first code comment, en 03:101-102, serves the method's rule on naming copies. One occurrence makes no rule (AGENTS.md, abstraction on the second occurrence); the second such comment would bring one to docs/04 §Code. Source: AGENTS.md, docs/04 §Code.
7. *Portuguese comment in Portuguese.* docs/04 lists comments among what the Portuguese code translates; `Recusa` and `err` keep the code's spelling, and `string` stays, as TypeScript names the type. Source: docs/04 §Writing the book, Evidence (docs/04:27).
8. *Width.* Every comment line holds under 74 columns at the top level, no tab; TypeScript blocks are exempt from the `width` rule, but the author asked for it. The block grows from 8 to 11 lines, under docs/04's 25. Source: the draft, docs/04 §Width of a block and §Code.
9. No new queue line, no split.

**Behaviour.**

* The reader of the English edition, in `## A pure function`, reads this block, the comment exactly as written:

```ts
type Member = { id: string; overdue: number };

// A string literal type: its only value is this exact string.
// Where a Refusal is expected, as in err below, the compiler
// accepts this string and no other, so a typo does not compile.
type Refusal = "HasOverdueBooks";

function mayBorrow(member: Member): Result<Member, Refusal> {
	if (member.overdue > 0) return err("HasOverdueBooks");
	return ok(member);
}
```

* The reader of the Portuguese edition, in `## Uma função pura`, reads this block, the comment exactly as written:

```ts
type Membro = { id: string; emAtraso: number };

// Um tipo literal de string: seu único valor é esta string.
// Onde se espera uma Recusa, como no err abaixo, o compilador
// aceita só esta string, e um erro de digitação não compila.
type Recusa = "TemLivrosEmAtraso";

function podePegarEmprestado(membro: Membro): Result<Membro, Recusa> {
	if (membro.emAtraso > 0) return err("TemLivrosEmAtraso");
	return ok(membro);
}
```

* Checked at apply time:
  * `grep -n "string literal type" book/en/03-simplicity-and-results.md` prints one line, two lines above `type Refusal`.
  * `grep -n "tipo literal de string" book/pt/03-simplicity-and-results.md` prints one line, two lines above `type Recusa`.
  * `grep -rn "literal type\|tipo literal" book` prints those two lines only: said once.
  * `git diff --stat` for this delivery shows only the two chapter 3 files, 3 lines added in each.
  * Each comment line measures under 74 columns.
* Fails: a comment that says `err` itself accepts only the string; a comment on the later `LendRefusal` / `RecusaDeEmprestimo` union; a prose sentence added; a blank line between the comment and `type Refusal`, or a blank line removed elsewhere in the block; an English word in the Portuguese comment other than the code's names and `string`; a forward pointer; an em dash.

**Contract.**

* Files: `book/en/03-simplicity-and-results.md`, three lines inserted before en 03:121; `book/pt/03-simplicity-and-results.md`, three lines inserted before pt 03:122; the text as Behaviour quotes. Nothing else in either file.
* Sections: `## A pure function` (pt `## Uma função pura`), its one code block. Terms of docs/03: none new (decision 5). Sources: none added. Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.** Three other M18 pages edit chapter 3; none touches this code block, and no order is needed. Whichever lands second reads the chapter as the first left it.

* `pt-identifiers-choice` edits pt 03:25, above this block, and docs/04; unaffected by these lines.
* `ch03-error-languages` (a draft) edits the section `Exceção, recusa, erro` (pt 03:164), below this block; this delivery shifts its lines by three.
* `early-no-forward-links` places this delivery in "Result: the value that carries a failure"; the block is in `## A pure function`. This delivery shifts its chapter 3 lines below the block by three: en 03:133 / pt 03:134 (the pointer to chapter 4 in the same section), 220 and 250. Its counted line numbers are a courtesy and its apply-time check is a grep (its decision 8), so the shift breaks nothing. This comment holds no pointer.
* `docs04-code-layout` writes the blank-line rule this block already follows.

**Out of scope.**

* The union `LendRefusal` / `RecusaDeEmprestimo` and its prose: decision 3.
* A sentence in the chapter's prose: the author chose a comment (decision 4).
* A docs/03 term or a docs/04 rule for explaining comments: decisions 5 and 6.
* Other code blocks of the book: the author named this one.

**Done when.**

* [x] Both editions written: the comment as Behaviour quotes, in place, the block's layout kept; Behaviour's checks give what they name.
* [x] Chapter 3 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Proof.**

* en 03:121-123 and pt 03:122-124 hold the comment as Behaviour quotes, directly above `type Refusal` and `type Recusa`; the blank lines around it are kept.
* `grep -n "string literal type"` on en 03 prints 121, two lines above `type Refusal` (en 03:123); `grep -n "tipo literal de string"` on pt 03 prints 122, two lines above `type Recusa` (pt 03:124); `grep -rn "literal type\|tipo literal" book` prints those two lines only.
* `git diff --stat` on the two chapter 3 files: 3 lines added in each, nothing else.
* Comment lines measure 61 to 64 columns, at column 0, no tab.
* `make verify` green: build, parity, em dash, prose, width, links, disclosure. A first run failed on pt 01 parity, another delivery's file mid-edit; green on rerun.

**Divergences.** None from Behaviour.

**Decisions taken in /apply.**

* Run in a batch of applies on one tree: the driver marks this line in docs/06, runs `make book` once at the end of the batch and gives both PDF paths, and stages and commits this delivery by its paths.

**Review.** One read-only agent on Opus read the diff of both chapter 3 files against this page and docs/04: text matches Behaviour exactly, placement and blank lines kept, the TypeScript claim holds (the error comes from `mayBorrow`'s declared return type, not from `err`), natural Brazilian Portuguese, no em dash, under 74 columns. No findings.

```commit
docs(ch03-literal-type-comment): explain the literal type in a comment

- Chapter 3, both editions: a three-line comment on `type Refusal` / `type Recusa` says it is a string literal type and a typo does not compile

work/done/ch03-literal-type-comment.md
```
