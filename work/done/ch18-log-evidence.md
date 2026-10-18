# ch18-log-evidence

**Objective.** A reader of chapter 18 finds in its `git log --oneline` the same `lend-book` commit chapter 13 suggested, every line in the kit's format, and a gain that claims nothing from an illustration written for the chapter.

**Decided without the author.** Chosen under the batch's rule, the recommended option each time; review these first.

1. Which log lines change: only `lend-book`'s, or all three? All three. docs/04 §Writing the book says a commit message written for the chapter on the lending library follows the kit's format as chapter 13 teaches it, with no `<type>(<slug>):` prefix; fixing one line would leave it beside two that are not in that shape. `lend-book` takes chapter 13's subject word for word in each edition; `return-book` takes the librarian's voice of chapter 11's queue line ("the librarian records a return", en 11:53; "registra a devolução", pt 11:56); the third line becomes `members`, the delivery before `lend-book` in chapter 11's queue, in place of "Start: documents and first milestone", which is not an imperative subject and not a delivery (docs/04; chapter 11; chapter 13). The other reading, changing only `lend-book`'s line, is what the finding names, and was rejected for that reason.
2. Where the slug goes. Out of the subject: chapter 13 puts it in the message's last line, `work/done/<slug>.md`, which `git log --oneline` does not print; the sentence after the log stops saying "with the delivery's slug at the end" and points to chapter 13 instead of teaching the format again, and the `git show` sentence names the last line, so the reader still learns where the slug is (chapter 13 §The format; docs/04 Said once).
3. What the gain says once the illustration is not its evidence. The gain alone: docs/03 `team gain` and docs/04 A gain per chapter give a number or a sourced claim where the book has one, "and otherwise the gain alone, with no sentence on the missing number". The sentence "The evidence is the history itself..." leaves the gain; what it taught, that such a log reads as the list of what users can do with one revert per line, moves to the sentence after the log, where the reader meets the log (docs/04 Say it where the doubt is born), so nothing useful is cut. Rejected: citing this book's own repository history as real evidence; a count of its commits goes stale with every commit, and it would bring this repository's `docs(<slug>):` format into the lending library's chapter.
4. The illustrative hashes (`a41c9e2`, `7d03b18`, `2f6e5a1`) stay. The no-hash rule (ADR-0017; AGENTS.md) forbids narrating a run; this block is marked as an illustration written for the chapter (18:42, kept, as docs/04 requires for a command's output written for the chapter), and the hash is what the paragraph above it teaches `--oneline` prints.
5. No new docs/03 term and no new queue line: `team gain` and `delivery` already hold what the chapter uses (docs/03).

**Behaviour.**

* A reader who compares chapter 13's `commit` block with chapter 18's log finds the same subject for `lend-book`: "Lend a copy to a member" (pt "Emprestar um exemplar a um membro").
* A reader of 18 §Commits and the history reads a log of three deliveries, newest first, `return-book`, `lend-book`, `members`, each an imperative subject (pt infinitive) with no slug, no type and no parentheses, and learns from the next sentences that the subject says what the delivery does as chapter 13 teaches, that `git show` shows the last line with the delivery's page in `work/done/`, and that such a log reads as the list of what users can now do, one revert per line.
* A reader of 18 §What the team gains reads the gain alone: one command to take a delivery back, one commit holding the change and the decision; no sentence calls the illustration evidence.
* Failure: before this delivery a reader meets "Lend a copy, and refuse when the rules say no (lend-book)" in 18 and "Lend a copy to a member" in 13, and is told the slug ends the subject while chapter 13 puts it in the last line; after it, no line of chapter 18 in either edition says either.
* Edge: the `return-book` line agrees with chapter 11's queue (a librarian records a return), not "Let a member return a copy".
* Edge: the log block stays a `text` block, each line under 74 columns, and keeps the sentence that marks it as an illustration.
* Edge: chapter 18's opening, its other sections and its key points (18:181-185) are unchanged; chapter 13 is unchanged.

**Contract.**

The findings were re-checked, not taken on trust. B2: en 18:46 "Lend a copy, and refuse when the rules say no (lend-book)" and pt "Empresta um exemplar, e recusa pelas regras (emprestar-livro)", against en 13:92 "Lend a copy to a member" and pt 13:92 "Emprestar um exemplar a um membro"; the slug itself matches, the subject and the slug's place differ, and 18:50 teaches the slug at the end of the subject. B24: en and pt 18:177 call the log, "an illustration, written for this chapter" (18:42), the gain's evidence. Both hold.

* **Chapter 18, both editions** (`book/en/18-git-essentials.md`, `book/pt/18-git-essentials.md`), file name, title and headings kept. Passages found by text; line numbers as of this page.
  1. The log block (en 18:44-48), en, becomes:

     ```text
     a41c9e2 Record the return of a copy
     7d03b18 Lend a copy to a member
     2f6e5a1 Register, suspend and reinstate members
     ```

     pt becomes:

     ```text
     a41c9e2 Registrar a devolução de um exemplar
     7d03b18 Emprestar um exemplar a um membro
     2f6e5a1 Cadastrar, suspender e reativar membros
     ```

     The sentence before it, "the output is an illustration, written for this chapter" / "a saída é uma ilustração, escrita para este capítulo", stays.
  2. The two sentences after the block (en 18:50-51), en, "Each line is one delivery, and its message says what a user can now do, with the delivery's slug at the end." and "`git show <hash>` opens one of them: the message, and every line it added and removed." become:
     "Each line is one delivery, and its subject says what the delivery does, in the imperative, as chapter 13 teaches; read from the top, such a log is the list of what users can now do, one revert per line, and a person who never opens the code can follow it."
     "`git show <hash>` opens one of them: the whole message, whose last line is the delivery's page in `work/done/`, and every line it added and removed."
     pt, "Cada linha é uma entrega, e a sua mensagem diz o que um usuário agora consegue fazer, com o slug da entrega no fim." and "`git show <hash>` abre uma delas: a mensagem, e cada linha que ela acrescentou e removeu." become:
     "Cada linha é uma entrega, e o seu assunto diz o que a entrega faz, no infinitivo, como o capítulo 13 ensina; lido de cima para baixo, um log assim é a lista do que os usuários agora conseguem fazer, um `git revert` por linha, e uma pessoa que nunca abre o código consegue acompanhá-lo."
     "`git show <hash>` abre uma delas: a mensagem inteira, cuja última linha é a página da entrega em `work/done/`, e cada linha que ela acrescentou e removeu."
  3. §What the team gains (en 18:177), the second sentence, en "The evidence is the history itself: the lending library's log, shown earlier in this chapter, reads as the list of what users can do, one line per delivery and one revert per line, and a person who never opens the code can follow it." and pt "A evidência é o próprio histórico: ... consegue acompanhá-lo." are removed. The first sentence (en 18:176 and its pt) stays as the whole gain.
  4. Nothing else in chapter 18 changes.
* **Terms:** `delivery`, `team gain`, as docs/03 has them; docs/03 unchanged. No new term, no new queue line.
* **Sources:** chapter 13 §The format and its `commit` block, chapter 11's queue example; no new source note, none removed.
* **Cases:** none. Code examples: none (the log is command output written for the chapter, already marked).
* **Abstraction:** none. This is the third chapter to show a lending-library commit message (first: `lend-book`, chapter 13; second: `due-date-format`, chapter 11, as docs/04 records); docs/04's rule already covers it, so no rule is added.

**Overlap with the lines in flight.** `free-line-gloss` and `pt-free-line-done`, which touched 18:165, are in `work/done/`. The pages in `work/` (`ch12-review-skill`, `ch15-first-commit`, `ch17-delivery-time`, `batch-propose`) touch chapters 12, 15, 17 and 19, none chapter 18 or 13. No file in common.

**Out of scope.**

* Chapter 13's `commit` block and format section: the source the log now follows, unchanged.
* This repository's own history as the gain's evidence: rejected in decision 3.
* Chapter 18's key points and its other sections: not named by B2 or B24.
* docs/03, docs/04, docs/05, docs/06 wording: unchanged.

**States.** Not applicable: no screen.

**Visual reference.** Not applicable: no screen.

**Done when.**

* [x] Chapter 18 changed in both editions as the Contract says, same headings; it still opens with its value; no filler and nothing useful cut.
* [x] `grep -n -E "\((lend-book|emprestar-livro)\)|refuse when the rules|recusa pelas regras|evidence is the|evidência é o|slug at the end|slug da entrega no fim" book/*/18-git-essentials.md` prints nothing.
* [x] `grep -n "Lend a copy to a member" book/en/18-git-essentials.md book/en/13-apply.md` and `grep -n "Emprestar um exemplar a um membro" book/pt/18-git-essentials.md book/pt/13-apply.md` each print the log line in chapter 18 and at least the `commit` block's subject in chapter 13 (13:92).
* [x] Every line of the log block is 74 columns or fewer; every number sourced (none added); no em dash.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Proof.**

* The Done when grep for the old wording prints nothing in either edition.
* "Lend a copy to a member" prints at en 18:46 and en 13:92 (and 13:176); "Emprestar um exemplar a um membro" at pt 18:46 and pt 13:92 (and 13:176).
* The longest log line is 47 columns; no number added; no em dash in either chapter file.
* `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* Divergences: none. Chapter 13 §The format allows "a scope in parentheses when it helps"; the three illustrative subjects take none, which the format permits and Behaviour asks.

**Delivery review.** A read-only agent on Opus read `git diff` and `git diff --cached` of the two chapter files, this page and this line's hunk of docs/06 against this page, docs/04 and docs/05 §6. The staged text matches the Contract word for word in both editions; the subjects agree with chapters 13 and 11; the commit block is in docs/05 §6's format. Nothing breaks the page, docs/04 or this delivery's lines.

1. en 18:50 says "one revert per line" and pt "um `git revert` por linha". Same meaning, and the Contract's text; kept, no change.
2. The log stops at `members`, while chapter 11's queue has earlier deliveries, beside a sentence saying the history runs back to the first commit. The block is marked as an illustration that "could read like this", as before, and Behaviour asks for these three lines; kept, no change and no queue line.

**Commit.**

```commit
docs(ch18-log-evidence): give chapter 18's log the kit's commit format

- Show lend-book's subject as chapter 13's commit block gives it
- Write the log's three subjects in the imperative, with no slug
- Say the slug is in the message's last line, read with git show
- Drop the gain's sentence citing the illustrative log as evidence
- Both editions

work/done/ch18-log-evidence.md
```
