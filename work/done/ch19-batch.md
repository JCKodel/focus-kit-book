# ch19-batch

**Objective.** A reader of chapter 19 §Proposing in a batch knows why the batch's side-by-side marks in docs/06 are no conflict although git puts them in one hunk, and how to stage only one of them, and sees question deliveries as Case A's customization, described in chapter 20, instead of a step of the method; both editions. Found by `m16-review` (work/done/m16-review.md): chB-3, "19:270, a batch's adjacent marks in one hunk of docs/06 are called no conflict, against 19:70 and docs/05 §4, and `git add -p` cannot split adjacent lines"; chB-4, "19:265 points question deliveries to chapter 23 and offers them as method; chapter 20:60-62 and :84 define them as Case A's customization". Both seen.

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *The marks stay no conflict; the text says why the hunk does not make them one.* docs/05 §4 says both "Another line changing mark ... [is] that session's work, not a conflict: do not stop for them" and "A conflict is the same hunk edited by both"; chapter 19 lists another line's mark first among what is not a conflict (en 19:60) and the same hunk among what is (19:67). In a batch both hold at once. The recommended reading keeps the batch possible in one folder, as the kit's process and chapter 19 already teach it: no line of that hunk is changed by two sessions, each session changes only its own line's mark, and the hunk is what git shows, not what either session edits. The reading taken is 19:67's own gloss, "the same hunk, the same lines": a conflict is two deliveries on the same lines, and the new text names that gloss so the chapter reconciles itself. The alternative, counting adjacent marks as a conflict and ordering the applies, would make every batch of neighbouring lines sequential in one folder and contradict 19:60 and docs/05 §4's first sentence instead. Source: docs/05 §4, chapter 19 §What is and is not a conflict there. The tension starts in the kit's wording of docs/05 §4 (`m16-review` chB-3); it is a note for the kit, not a line here.
2. *What changes is the staging, and the chapter teaches it.* `git add -p` stages a file hunk by hunk (19:33), and its `s` splits a hunk only where an unchanged line separates two changes, so adjacent marks cannot be split with it; `e` opens the hunk in the editor, where the other lines' `+` lines are deleted and their `-` lines turned into context with a space, which is what git's own instructions in that editor say. The claim "`git diff --cached docs/06-Queue.md` shows you only that line staged" then holds. Source: the git documentation for `git add`, sections "Interactive mode" and "Editing patches"; /apply checks both behaviours in a scratch repository before writing, and the chapter shows no run (ADR-0017).
3. *A source note for `git add`.* The chapter cites git's documentation for every git behaviour it states (`[^git-commit]`, `[^git-diff]`, `[^git-merge]`); the new claim gets `[^git-add]` the same way, in both editions, accessed on /apply's date. Source: docs/04 §Chapter shape, Source notes.
4. *Question deliveries are Case A's, pointed to chapter 20.* docs/03's row ("Case A's customization"), chapter 20 §Question deliveries and its key point say so; chapter 23:38 uses one in a story, which is why the old pointer named it, but chapter 20 is where it is defined. The pointer is written in plain words, as the paragraph's other pointers (chapters 14 and 23) are, and is chapter 19's only pointer to chapter 20 (docs/04 §Chapter pointers). Source: docs/03, chapters 20 and 23.
5. *Only the two sentences change.* 19:283 ("stages its own hunk") and key point 1 ("its hunk of the queue") stay: true for lines far apart, the case they describe, and 270 now says what happens when lines sit side by side. Key point 2 stays: it lists another line's mark as no conflict, as decision 1 reads. Source: chapter 19 as it stands.
6. No docs/03 term (`question delivery`, `conflict`, `stage`, `hunk` as chapter 19 keeps it), no new queue line, no split.

**Behaviour.**

* A reader of chapter 19 §Proposing in a batch reads, in place of "A question delivery, a queue line whose only purpose is a written answer, asks it (chapter 23).":
  * en: "Case A gave such a question a line of its own, a question delivery, whose only output is a written answer; it is Case A's own customization, not a step of the kit (chapter 20)."
  * pt, §Propor em lote, in place of "Uma entrega de pergunta, uma linha da fila cujo único propósito é uma resposta escrita, a faz (capítulo 23).": "O Caso A deu a uma pergunta assim uma linha própria, uma entrega de pergunta, cujo único resultado é uma resposta escrita; ela é uma customização do próprio Caso A, não um passo do kit (capítulo 20)."
* The same reader reads, in place of the sentence "The lines of one batch sit side by side in the queue, so their marks fall in one hunk of docs/06; that is still another line's mark, no conflict, and before each commit `git diff --cached docs/06-Queue.md` shows you only that line staged.", one sentence per line:
  * en:
    * "The lines of one batch sit side by side in the queue, so git puts their marks in one hunk of docs/06."
    * "That hunk holds no conflict: no line in it is changed by two sessions, which is what the conflict above means by the same hunk, the same lines, and each session's change is its own line's mark, which the list of what is not a conflict names first."
    * "What it changes is the staging: `git add -p` splits a hunk with `s` only where an unchanged line separates two changes, so for adjacent marks you answer `e`, and git opens the hunk in your editor, where you delete the other lines' `+` lines and turn their `-` into a space.[^git-add]"
    * "Before each commit, `git diff --cached docs/06-Queue.md` then shows you only that line staged."
  * pt:
    * "As linhas de um lote ficam lado a lado na fila, então o git põe as suas marcas em um hunk do docs/06."
    * "Esse hunk não guarda conflito: nenhuma linha dele é mudada por duas sessões, que é o que o conflito acima quer dizer com o mesmo hunk, as mesmas linhas, e a mudança de cada sessão é a marca da sua própria linha, que a lista do que não é conflito nomeia primeiro."
    * "O que ele muda é o stage: o `git add -p` divide um hunk com `s` só onde uma linha sem mudança separa duas mudanças, então para marcas vizinhas você responde `e`, e o git abre o hunk no seu editor, onde você apaga as linhas `+` das outras linhas e troca o `-` delas por um espaço.[^git-add]"
    * "Antes de cada commit, `git diff --cached docs/06-Queue.md` então mostra só aquela linha em stage."
* The note, at the end of both files with the chapter's other notes: `[^git-add]: Git, "git-add", the documentation, sections "Interactive mode" and "Editing patches", accessed <YYYY-MM-DD>. <https://git-scm.com/docs/git-add>` (pt: `acesso em <YYYY-MM-DD>`), the date /apply opens the page.
* Checked on `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`: `grep -c "chapter 23"` (pt `"capítulo 23"`) gives 0; `grep -c "chapter 20"` (pt `"capítulo 20"`) gives 1; `grep -c "still another line's mark"` (pt `"continua sendo a marca de outra linha"`) gives 0; `grep -cF '[^git-add]'` gives 2 in each edition.
* Fails: one edition changed and not the other; the text still saying a question delivery is the method's, or pointing it to chapter 23; the text saying adjacent marks are a conflict, or that `git add -p` separates them by splitting; a staging instruction /apply's scratch check does not confirm; any other sentence of chapter 19 changed; an em dash.

**Contract.**

* Files: `book/en/19-worktrees.md`, `book/pt/19-worktrees.md`; no other file.
* Section and lines: §Proposing in a batch / §Propor em lote, the sentence at en and pt line 265 and the sentence at en and pt line 270, and one note definition at each file's end (working tree of 2026-10-18; the text is the locator, the numbers a courtesy).
* Terms of docs/03: none new. Portuguese words: hunk `hunk`, stage `stage`, question delivery `entrega de pergunta`, as chapter 19 and docs/03 keep them.
* Sources: `[^git-add]`, added, both editions.
* Cases: Case A, one sentence, repeating what chapter 20 §Question deliveries already says (a customization Case A recorded, whose only output is a written answer); no new detail. Listed here for the author's approval (docs/00 OD-3): the en and pt sentences in Behaviour's first item.
* Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same chapter.** None: no other open line of M16 or M17 names chapter 19.

**Out of scope.**

* docs/05 §4's two sentences: the kit's wording; decision 1's note for the kit.
* 19:283, key points 1 and 2: decision 5.
* Chapter 23:38's question delivery: a story that uses one, right as it stands.
* How an agent stages one line without an editor: the chapter teaches what the person checks before committing, as 19:40 to 55 do.

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] `s` and `e` behave as the new sentence says, checked in a scratch repository outside this one; no run shown in the chapter.
* [x] Chapter 19 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: links (the new URL included), edition parity (the note cited once in each edition), width, prose rules, disclosure scan, no em dash.
* [x] The author's approval of the Case A sentence, given in reading this page before /apply; without it the line waits as `[?]` with `· resume: apply · blocked: Case A sentence not approved` (docs/00 OD-3). Deferred: the batch's driver has the author approve the batch's Case A passages at its end, so the line does not wait; the sentences are listed under Contract, Cases.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Proof.** A scratch repository outside this one, git 2.56.0, a three-line file with its first two lines changed: `git add -p` offered no `s` for the hunk and, asked for it, answered "Sorry, cannot split this hunk"; `e`, with the second line's `+` line deleted and its `-` line turned into context with a space, staged only the first line's change. With an unchanged line between the two changes, `s` split the hunk in two. The editor's own instructions read "To remove '-' lines, make them ' ' lines (context)." and "To remove '+' lines, delete them." The page at <https://git-scm.com/docs/git-add> has the sections "Interactive mode" and "Editing patches", checked on 2026-10-18. Both editions' greps give Behaviour's results: 0, 1, 0, 2. `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. This delivery's own hunk of docs/06 sits beside the batch's other `[>]` marks, so it was staged as the new sentence says, with only its own line.

**Divergences.** None from Behaviour.

**Decisions taken in /apply.**

* The pt note follows the edition's other git notes: "a documentação, seções \"Interactive mode\" e \"Editing patches\", acesso em 2026-10-18", the page naming only `acesso em`.
* The note sits after `[^git-diff]` and before `[^parallel-run]`, the order of first citation in the chapter.
* "(chapter 20)" stays plain words, as the page says: a forward pointer after a sentence that says something (docs/04 §Chapter pointers).

**Review.** One read-only agent on Opus read the two chapters' diffs and this line of docs/06 against this page and docs/04: no findings. It noted the second new sentence is long, the page's exact wording; kept.

```commit
docs(ch19-batch): stage a batch's adjacent marks; question deliveries

- Say why a batch's marks in one hunk of docs/06 are no conflict
- Teach `git add -p` with `e` for adjacent marks, `s` cannot split
- Cite git-add's documentation in both editions
- Point question deliveries to chapter 20 as Case A's customization

work/done/ch19-batch.md
```
