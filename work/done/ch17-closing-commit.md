# ch17-closing-commit

**Objective.** A reader of chapter 17 is told how the git history ties a commit to its delivery as the kit's commit format really does it: the commit that closes a delivery ends with the path of its page, `work/done/<slug>.md`, instead of "ends with its slug"; both editions. Found by the delivery review of `ch17-delivery-time` (work/done/ch17-delivery-time.md, Delivery review finding 4: "Line 21, 'the commit that closes a delivery ends with its slug', is inexact against docs/05 §6, whose last line is the page's path.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The sentence names the last line as the page's path, `work/done/<slug>.md`, and not the subject's scope. docs/05 §6 gives the last line as "the page's actual path ... `work/done/<slug>.md` when done", and chapter 13 §The message teaches the same last line, while it makes the scope in parentheses optional ("with a scope in parentheses when it helps"); naming the subject would teach the reader something the kit's format does not promise. Sources: docs/05 §6, chapter 13 §The message.
2. Only the closing commit is named, as the sentence already does. On trunk a delivery is one commit (docs/05 §5 Git), and a blocked delivery on trunk stays uncommitted (docs/05 §6), so the `work/<slug>.md` last line of a partial message never reaches trunk's history; a branch's partial commit is not what this list item is about. Source: docs/05 §§5, 6.
3. No new pointer. Line 21 already points to chapter 18 for the git history, which already says the message's "last line is the delivery's page in `work/done/`" (its `git show` passage), so the new clause agrees with the chapter it points to; a pointer back to chapter 13 would repeat what a reader in order has read (docs/04 §Chapter pointers).
4. No other line of the book changes: `grep` of `book/` for "with its slug" and "com o slug" finds this line alone in the sense of a commit's last line. Chapter 17's other passages on the history (lines 26, 27, 66, 70) were settled by ch17-delivery-time and stay.
5. No docs/03 term, no new queue line, no split: one line in two files. Sources: docs/03 ("commit", "delivery", "commit block" exist), docs/05 §1.

**Behaviour.**

* A reader of chapter 17 §What the agent already reads reads, as the list item on the git history:
  * en: "* **The git history** (chapter 18): when each commit happened, and which delivery it belongs to, since the commit that closes a delivery ends with the path of its page, `work/done/<slug>.md`." in place of the same item ending "... ends with its slug."
  * pt, §O que o agente já lê: "* **O histórico do git** (capítulo 18): quando cada commit aconteceu, e a qual entrega pertence, já que o commit que fecha uma entrega termina com o caminho da página dela, `work/done/<slug>.md`." in place of the same item ending "... termina com o slug dela."
* The reader can say which line of a closing commit names its delivery, and where that commit's reasoning lives.
* Checked, both editions, on `book/en/17-project-as-assistant.md` and `book/pt/17-project-as-assistant.md`:
  * en: `grep -c "ends with its slug"` gives 0; `grep -c "ends with the path of its page"` gives 1.
  * pt: `grep -c "termina com o slug dela"` gives 0; `grep -c "termina com o caminho da página dela"` gives 1.
* Fails: one edition changed and not the other; the sentence naming the slug in the subject or a scope as the tie; a pointer, a number or a code block added; any other line of chapter 17 changed; any other file changed but this page and the line's marks in docs/06; an em dash.

**Contract.**

* Files: `book/en/17-project-as-assistant.md`, `book/pt/17-project-as-assistant.md`; no other file.
* Passage, found by text (line 21 in the working tree of 2026-10-17, a courtesy): §What the agent already reads / §O que o agente já lê, the list item that begins "**The git history**" / "**O histórico do git**", its closing clause replaced.
* Terms of docs/03: none new. Sources: none added or removed. Cases: none; no Case A, Case B or Ninjobs passage changes. Code blocks: none added. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on nearby chapters.** None touches chapter 17: `ch19-when-worktrees-pay` changes chapter 19, `ch21-counts-once` chapter 21, `batch-propose` chapter 19 and the kit; no file in common.

**Out of scope.**

* Chapter 13 §The message: it already gives the last line as `work/done/<slug>.md`; it is the source, not the finding.
* The subject's `<type>(<slug>)` scope of this repository's docs/05 §6: the kit's format makes it optional (decision 1).
* Chapter 17's measure of a delivery's time and the five deliveries' question: settled by ch17-delivery-time.
* A git command to find a delivery's commit: chapter 18 teaches `git log`.

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapter 17 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: links, edition parity, prose rules, block width, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, the change draws on no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Proof.**

* The Behaviour greps, both editions: "ends with its slug" / "termina com o slug dela" 0; "ends with the path of its page" / "termina com o caminho da página dela" 1.
* `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* Divergences: none.

**Delivery review.** A read-only agent on Opus read `git diff` and `git diff --cached` of the two chapter files, this page and this line's hunk of docs/06 against this page, docs/04 and docs/05 §6. The staged text matches Behaviour word for word in both editions and agrees with docs/05 §6 and chapters 13 and 18; no other line changed; the commit message meets §6. Findings: none.

**Commit.**

```commit
docs(ch17-closing-commit): end chapter 17's closing commit with its page

- Say the commit that closes a delivery ends with work/done/<slug>.md
- Both editions

work/done/ch17-closing-commit.md
```
