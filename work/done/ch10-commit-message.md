# ch10-commit-message

**Objective.** A reader following chapter 10's new project commits the documents `/brainstorm` wrote with a message in the kit's format as chapter 13 teaches it, an imperative subject (infinitive in the Portuguese edition) with no `docs:` prefix, and knows why this first message has no last line pointing to a page, in both editions. Found by `m15-review` (work/done/m15-review.md, A3: "10:43: a message written for the chapter with a `docs:` prefix and no imperative subject. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. Which format: the kit's, as chapter 13 §The message teaches it, not this repository's `<type>(<slug>):`. docs/04 line 26 already says so: a commit message written for a chapter "follows the kit's format, as chapter 13 teaches it, with no `<type>(<slug>):` prefix", first occurrence `lend-book` (chapters 12 and 13), second `due-date-format` (chapter 11). This page adds no rule; chapter 10's message is a third case under it. Source: docs/04 line 26, book/en/13-apply.md §The message, the kit's `references/documents.md` §6.
2. The format applies to this commit: `/brainstorm` writes docs/05 before step 3 commits it, and step 3's "You see" line already says docs/05 owns the format of every message from here. Source: chapter 10 lines 42 and 45, chapter 9's order of steps.
3. No last line: the kit's format ends with the page's actual path, and this commit belongs to no delivery, so it has no page. The message is a subject alone, still a `-m` one-liner, and the step says why in one clause of at most fifteen words. The alternative, a silent subject-only message, was not taken: step 7 tells the reader every message ends with `work/done/<slug>.md`, and step 3 would then look like a mistake. Source: docs/05 §6, chapter 13 §The message, chapter 10 line 57.
4. The subject: en "Add the kit and the documents from /brainstorm", pt "Adicionar o kit e os documentos do /brainstorm", 46 characters each, within 72. It names what the commit holds (step 3 commits the documents "with the kit's files") and keeps `/brainstorm` as one word the reader swaps, because the existing project's step 4 says "with `/analyze` in the message"; the swap gives "Add the kit and the documents from /analyze". No scope in parentheses: it would not help here. Source: chapter 10 lines 44 and 76, chapter 13 §The message.
5. Portuguese mood: the infinitive, "como uma ordem", as pt chapter 13 line 176 reads since `pt-placeholders` (9c56dab): "Emprestar um exemplar a um membro". Not "imperativo". Source: work/done/pt-placeholders.md, book/pt/13-apply.md.
6. "A message written for this chapter" stays: no source note, since a message written for the chapter has no original (docs/04 line 26). Line 45 ("from here, your docs/05 owns the format of every message") stays word for word.
7. No docs/03 term (docs/03 has `commit` and `commit block`; the format lives in docs/05 §6), no new queue line, no split: one line in each edition. Source: docs/03, docs/05 §1.

**Behaviour.**

* A reader of chapter 10 §A new project, step 3, reads (pt in parentheses), with everything before `git commit -m` unchanged:
  * "... then commit them with the kit's files: `git add -A`, then `git commit -m "Add the kit and the documents from /brainstorm"`, a message written for this chapter, a subject alone, since there is no page yet for its last line." ("... e então faça o commit deles com os arquivos do kit: `git add -A`, depois `git commit -m "Adicionar o kit e os documentos do /brainstorm"`, uma mensagem escrita para este capítulo, só o assunto, já que ainda não há página para a sua última linha.")
  /apply may polish the closing clause within these limits: one clause, fifteen words at most per edition, saying the message has no page line because no page exists yet; the subject exactly as above.
* The existing project's step 4 (line 76) is unchanged, and "with `/analyze` in the message" applied to step 3's subject gives "Add the kit and the documents from /analyze" ("Adicionar o kit e os documentos do /analyze"), a well-formed subject.
* Checked, both editions, on `book/en/10-quick-guide.md` and `book/pt/10-quick-guide.md`: `grep -n '"docs:' ` finds nothing; `grep -c 'commit -m'` gives 1; the quoted subject is 46 characters and starts with a verb, "Add" / "Adicionar"; `git diff` touches line 44 only.
* Fails: one edition changed and not the other; a `docs:` or any `<type>(...):` prefix kept; the pt subject in the imperative ("Adicione") or in English; a page path added to the message; `/brainstorm` dropped from the subject (step 4 then swaps nothing); line 45, line 76 or any other line of chapter 10 changed; any edit to chapter 13 or chapter 9.

**Contract.**

* Files: `book/en/10-quick-guide.md`, `book/pt/10-quick-guide.md`; no other file.
* Lines: 44 in both editions as of the working tree on 2026-10-17 (the review's 10:43 predates a one-line shift); found by text, the step that starts "3. Read the documents against chapter 9's checklist" / "3. Leia os documentos contra a lista de conferência do capítulo 9".
* Prose with inline code, not a code block: the 74-column block rule does not apply; the no-em-dash rule does.
* Terms of docs/03: none new. Sources: none added or removed. Cases: none; no Case A or Case B passage.
* docs/00 to docs/05: no change. docs/06: this line `[>]` by the driver, `[*]` when /apply starts, `[x]` by /apply. No new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same chapters.**

* `ch08-10-devin-desktop` (`[ ]`, M16): chapter 10's host table (line 27); a different hunk, no conflict.
* `ch05-lend-pointer` and `ch12-review-skill` (`[ ]`): chapters 5 and 12; no file in common.

**Out of scope.**

* Chapter 13 §The message: it is the format this page follows, already right in both editions.
* This repository's `<type>(<slug>):` format in docs/05 §6: the repository's own, not the book's.
* Line 45 and step 4's "with `/analyze` in the message": already true under the new subject.
* Chapter 9 §Review before you commit: it gives no message of its own.

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapter 10 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] `make verify` green, disclosure scan and commit messages included; no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Proof.**

* Line 44 of `book/en/10-quick-guide.md` and `book/pt/10-quick-guide.md` changed as Behaviour says; `git diff -U0` shows one hunk, `@@ -44 +44 @@`, in each edition.
* `grep -n '"docs:'` finds nothing in either edition; `grep -c 'commit -m'` gives 1 in each.
* Subjects: "Add the kit and the documents from /brainstorm" and "Adicionar o kit e os documentos do /brainstorm", 46 characters each, starting with a verb; no page path in the message.
* Closing clause: "a subject alone, since there is no page yet for its last line" (13 words), "só o assunto, já que ainda não há página para a sua última linha" (14 words).
* Line 76 unchanged in both editions; "with `/analyze` in the message" swaps step 3's subject to "Add the kit and the documents from /analyze".
* `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.** None: the closing clause is the one Behaviour proposes, unpolished.

**Decisions in /apply.** None beyond the page's own: nobody was asked; the batch takes the recommended option.

**Review.** A read-only Opus agent read the staged diff of this delivery's paths against the page, docs/04 and docs/05 §6. Findings:

1. docs/06 line still `[*]`: expected at review time; /apply's last edit marks it `[x]`. Done.
2. Commit block not yet on the page: expected; added below. Done.
3. pt line 44, "só o assunto" two lines after "um assunto por vez" (a topic of conversation); optional "só a linha de assunto". Not taken: the page fixes this clause's wording, and "assunto" is pt chapter 13's own word for a commit subject. No queue line.

No other finding.

```commit
docs(ch10-commit-message): give chapter 10's commit the kit's format

- en and pt step 3: an imperative (pt infinitive) subject, no `docs:` prefix
- say the message is a subject alone: no page exists yet for its last line
- step 4's `/analyze` swap still gives a well-formed subject

work/done/ch10-commit-message.md
```

