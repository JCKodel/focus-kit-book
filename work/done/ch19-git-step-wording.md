# ch19-git-step-wording

**Objective.** A reader of chapter 19, under "Worktrees in the kit", reads one list of the git steps the agent never takes on its own and takes when asked, sees as its examples of an undone tangle only commands the book teaches, reads "conflict marker" as the chapter names it, and in Portuguese reads chapter 18's rule with the same phrase for the agent acting alone as chapter 19. Both editions. From the delivery review of `ch19-agent-does-git` (work/done/ch19-agent-does-git.md, its Review findings 1 to 4), 2026-10-18.

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *The two lists agree by adding push to line 177.* en/pt 19:177 names four steps (commit, merge, resolve a conflict, remove a worktree) and 19:178's "any of them" names commit, merge, conflict and push, without the worktree. Line 179 asks the reader to read `git log` before the push, so push stays; line 177 gains it, and line 178 gains "removes the worktree". A push changes the history the remote holds, so "every step that changes the history" still reads true. Source: the draft; book/en/19-worktrees.md:177-179.
2. *The tangles are two the book teaches.* `git merge --abort` for a merge stopped by a conflict (en/pt 19:215) and `git revert` for a delivery to take back (en/pt 18:138, the verb of en 18:15). The commands are named so the reader recognises them when the chapter teaches them. Source: the draft; the Review of `ch19-agent-does-git`, finding 2.
3. *"marker" becomes "conflict marker" / "marcador de conflito"*, the term of en/pt 19:4 and 19:186. Source: the draft.
4. *pt 18:171 ends "nunca o agente por conta própria"*, the phrase of pt 19:177; "sozinho" could read as "never without the person". English 18:171 already says "on its own" and is unchanged. Source: the draft.
5. *Line numbers.* At /propose the lines are en/pt 19:177-179 and en/pt 18:171. Apply finds each by its text.
6. No new docs/03 term, no new queue line, no split, no source note.

**Behaviour.**

* The reader of chapter 19, in English, under "## Worktrees in the kit", reads in place of lines 177 to 179:
  * "The agent never commits, merges, pushes, resolves a conflict or removes a worktree on its own: every step that changes the history is yours to decide, as in every git strategy."
  * "Ask, and it takes any of them for you: it writes the commit message, resolves the conflict, commits, merges, pushes or removes the worktree, and knows the commands that undo a tangle, such as `git merge --abort` for a merge stopped by a conflict or `git revert` for a delivery to take back."
  * "Each step comes after your reading: ask for the commit once the staged diff holds only the delivery, for the merge commit once the resolved file has no conflict marker left, and for the push once `git log` shows what will leave."
* The reader of the Portuguese edition, under "## Worktrees no kit", in place of lines 177 to 179:
  * "O agente nunca faz commit, merge ou push, resolve um conflito ou remove um worktree por conta própria: cada passo que muda o histórico é decisão sua, como em toda estratégia de git."
  * "Peça, e ele dá qualquer um desses passos por você: escreve a mensagem de commit, resolve o conflito, faz o commit, o merge ou o push, remove o worktree, e conhece os comandos que desfazem um nó, como `git merge --abort` para um merge parado por um conflito ou `git revert` para uma entrega a desfazer."
  * "Cada passo vem depois da sua leitura: peça o commit quando o diff em stage tiver só a entrega, o commit de merge quando o arquivo resolvido não tiver nenhum marcador de conflito, e o push quando o `git log` mostrar o que vai sair."
* The reader of chapter 18 in Portuguese, under "## Escolher", reads the line that begins "Seja qual for, a regra é a mesma" ending in "nunca o agente por conta própria." in place of "nunca o agente sozinho.".
* English chapter 18 and the rest of both chapters are unchanged.
* Checked at apply time:
  * `grep -n "rebase left half done\|rebase parado no meio\|no marker left\|nenhum marcador,\|agente sozinho" book/*/1[89]-*.md` prints nothing.
  * `grep -n "git merge --abort\` for a merge\|git merge --abort\` para um merge" book/*/19-worktrees.md` prints one line per edition.
  * `git diff book/` shows, for this delivery, only these lines.
* Fails: a step in line 178 that line 177 does not name, other than writing the commit message; an example of a tangle the book does not teach; a sentence saying the agent acts unasked; an em dash; a `not-but` pattern; a run narrated.

**Contract.**

* Files: `book/en/19-worktrees.md`, `book/pt/19-worktrees.md` (lines 177 to 179); `book/pt/18-git-essentials.md` (the end of line 171).
* Terms of docs/03: none new; "conflict marker" as chapter 19 has it. Sources: none added. Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.** No other M18 page or draft edits chapter 18 or 19.

**Out of scope.**

* English chapter 18: it already says "on its own" (decision 4).
* The four costs at en/pt 19:280-284 and the rest of chapter 19: `ch19-agent-does-git` settled them.

**Done when.**

* [x] Both editions written as Behaviour says, with the review's wording (Divergences).
* [x] Chapters 18 and 19 still open with their value, keep their gain, no filler and nothing useful cut.
* [x] Every number sourced: none added.
* [x] `make verify` green.
* [x] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author: by the driver, once at the end of the batch.
* [x] Page in `work/done/`, the line `[x]`, commit message in a `commit` block.

**Proof.**

* en/pt 19:177-179 and pt 18:171 read as Behaviour says, with the two wordings of Divergences.
* Behaviour's greps: the old phrases print nothing; the `git merge --abort` example prints one line per edition (19:178).
* `git diff --stat` on the three paths: 7 insertions, 7 deletions, only these lines.
* `make verify`: build, parity, em dash, prose, width and disclosure green; links green but for the web.archive.org note at en/pt 24:159, refused by the network at run time, outside this delivery.

**Divergences.** Two wordings from the review, kept to the page's intent:

* en/pt 19:178 "the commands that undo a tangle" became "undo a step" / "desfazem um passo": `git revert` takes back a delivery, which is no tangle, and "step" holds both examples.
* pt 19:177 "merge ou push, resolve um conflito" became "merge ou push, nem resolve um conflito": a negative list reads in Portuguese with "nem" instead of two "ou" in a row.

**Decisions taken in /apply.**

* Run in a batch of applies on one tree: the driver marks this line in docs/06, runs `make book` once at the end of the batch, and stages and commits this delivery by its paths.
* The two review wordings are applied here and recorded as divergences, as the batch rules say for wording on text this delivery wrote.

**Review.** One read-only agent on Opus read the diff of the three paths against this page and docs/04, with chapters 18 and 19 in both editions: nothing breaks the page or docs/04; both lists name the same five steps; both examples are taught (19:215, 18:138); "conflict marker" matches 19:4. Two optional wordings, applied (Divergences).

```commit
docs(ch19-git-step-wording): name only taught git steps where the agent acts on the person's word

- Chapter 19, Worktrees in the kit: the steps the agent never takes alone and takes when asked are one list, push and worktree removal included; the examples are `git merge --abort` and `git revert`; "conflict marker"
- Chapter 18, Escolher (pt): the rule ends "nunca o agente por conta própria"

work/done/ch19-git-step-wording.md
```
