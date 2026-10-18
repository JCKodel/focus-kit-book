# ch19-agent-does-git

**Objective.** A reader of chapter 19, under "Worktrees in the kit", reads that the agent never takes a step that changes the history on its own, that they can always ask it for any git step, a commit message, a conflict, a commit, a merge or a push, and that each step comes after their own reading of what it will carry; chapter 18's rule agrees with it. Both editions. From the author's reading of the book on 2026-10-18: "pt 19:177, 'O agente nunca faz commit, merge, resolve um conflito ou remove um worktree: cada passo que muda o histórico é seu, como em toda estratégia de git', must make clear that the person can always ask the agent to do something in git for them: write a commit message, resolve conflicts, commit, merge and push. What matters is validating the result by hand; but if git gets complicated, the agent is more than expert at solving any kind of git problem. The kit's rule stays as it is: the agent does not commit on its own initiative; asked, it acts on the person's word."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *Said once, in chapter 19, where the author marked it.* Chapter 19 teaches the conflict, the merge and the worktree's removal, so the sentence that names them is the place; chapter 18 teaches commits, remotes and merges but its line 171 only states the rule, and gains three words so it agrees (decision 2). Chapter 13 changes nothing. Source: the draft; docs/04 §Writing the book (one fact said once).
2. *Chapter 18's "never the agent" becomes "never the agent on its own".* en 18:171 "the person commits and merges, never the agent" (pt 18:171 "nunca o agente") read as an absolute after chapter 19 says the person may ask; "the person decides each commit and merge, never the agent on its own" keeps the rule and agrees. Source: book/en/18-git-essentials.md:171.
3. *The kit's rule is unchanged and is read as the agent's own initiative.* docs/05 §5 Git slot ("The agent stages; it never commits or merges"), §6 ("The agent suggests the message; the person commits after reviewing") and AGENTS.md say what the agent does unasked, and `/apply` ends at the stage. The book teaches the kit as it is: no sentence says `/apply` or any command commits. The draft says the same ("the agent does not commit on its own initiative; asked, it acts on the person's word"). Source: docs/05 §5, §6; docs/04 **The kit as it is**; the apply skill.
4. *The person's reading comes before each step, in the book text.* Chapter 13 says a commit means a person read the change (en 13:180), and chapter 19 lists four costs of letting agents commit a batch of applies (en 19:280-284); two of them, a commit nobody read and, in one folder, a commit that takes what another session staged, hold even for a commit the person asked for. So the new line says which reading comes before which step: the staged diff, holding only the delivery, before the commit; the resolved file, with no marker left, before the merge commit (the trap of en 19:215-219, "The trap: committing the markers"); `git log` before the push. With that, en 19:280-284 stays true untouched: it is about commits nobody read. Source: book/en/13-apply.md:175-182; book/en/19-worktrees.md:215-219, 280-284.
5. *No superlative about the agent's skill with git.* The draft's "more than expert at solving any kind of git problem" has no source for "any", and docs/04 asks every claim to be real. The line says what the agent does instead: it knows the commands that undo a tangle chapters 18 and 19 already teach, a rebase left half done or a commit on the wrong branch. Source: docs/04 §Writing the book; the claim handling of `agent-never-unsure` (its decision 4).
6. *What stays, and why.* en/pt 13:1 and 13:146-148 describe the command `/apply`, which ends at the stage; en/pt 18:55 and 18:184 say the agent stages and the person commits, the kit's flow; en/pt 19:5, 19:37 and 19:278 say every commit stays yours, still true as your decision; en/pt 19:280-284, decision 4. None says the agent cannot do a step when asked.
7. *Both editions ask in the verb.* The author's complaint is that pt 19:177 hides the ask; the new lines open with "Ask" / "Peça".
8. *Line numbers.* At /propose the sentence is at en 19:177 and pt 19:177, the rule at en 18:171 and pt 18:171. Apply finds each by its text.
9. No new docs/03 term, no new queue line, no split, no source note.

**Behaviour.**

* The reader of chapter 19, in English, under "## Worktrees in the kit", reads in place of the line that begins "The agent never commits, merges, resolves a conflict or removes a worktree:" these three lines:
  * "The agent never commits, merges, resolves a conflict or removes a worktree on its own: every step that changes the history is yours to decide, as in every git strategy."
  * "Ask, and it takes any of them for you: it writes the commit message, resolves the conflict, commits, merges or pushes, and knows the commands that undo a tangle such as a rebase left half done or a commit on the wrong branch."
  * "Each step comes after your reading: ask for the commit once the staged diff holds only the delivery, for the merge commit once the resolved file has no marker left, and for the push once `git log` shows what will leave."
* The reader of the Portuguese edition, under "## Worktrees no kit" (the section's heading as it stands), in place of the line that begins "O agente nunca faz commit, merge, resolve um conflito ou remove um worktree:":
  * "O agente nunca faz commit, merge, resolve um conflito ou remove um worktree por conta própria: cada passo que muda o histórico é decisão sua, como em toda estratégia de git."
  * "Peça, e ele dá qualquer um desses passos por você: escreve a mensagem de commit, resolve o conflito, faz o commit, o merge ou o push, e conhece os comandos que desfazem um nó como um rebase parado no meio ou um commit no branch errado."
  * "Cada passo vem depois da sua leitura: peça o commit quando o diff em stage tiver só a entrega, o commit de merge quando o arquivo resolvido não tiver nenhum marcador, e o push quando o `git log` mostrar o que vai sair."
* The reader of chapter 18, in English, under "## Choosing" (pt "## Escolher"), reads the line that begins "Whichever it is, the rule is the same" ending in "and the person decides each commit and merge, never the agent on its own." in place of "and the person commits and merges, never the agent."; in Portuguese, "e a pessoa decide cada commit e cada merge, nunca o agente sozinho." in place of "e a pessoa faz o commit e o merge, nunca o agente.".
* The line after chapter 19's new lines ("To run two deliveries at once in worktrees", pt "Para rodar duas entregas ao mesmo tempo em worktrees") and the rest of both chapters are unchanged.
* Checked at apply time:
  * `grep -n "removes a worktree: every step\|remove um worktree: cada passo" book/*/19-worktrees.md` prints nothing.
  * `grep -n "Each step comes after your reading\|Cada passo vem depois da sua leitura" book/*/19-worktrees.md` prints one line per edition.
  * `grep -n "never the agent\.\|nunca o agente\.$" book/*/18-git-essentials.md` prints nothing; `grep -n "never the agent on its own\|nunca o agente sozinho" book/*/18-git-essentials.md` prints one line per edition.
  * `git diff book/` shows, for this delivery, only these lines in both editions of chapters 18 and 19.
* Fails: a sentence saying the agent commits, merges or pushes unasked, or that `/apply` commits; a step the line places before the person's reading; en/pt 19:280-284 (the four costs) softened or removed; a superlative about the agent's skill; a host named; a change to chapter 13; a `not-but` pattern; a pointer to a later chapter; an em dash; a run narrated.

**Contract.**

* Files: `book/en/19-worktrees.md`, `book/pt/19-worktrees.md` (one line becomes three, en 19:177, pt 19:177 at /propose); `book/en/18-git-essentials.md`, `book/pt/18-git-essentials.md` (the end of one line, en 18:171, pt 18:171).
* Terms of docs/03: none new; `stage`, `delivery`, `worktree` as the book has them. Sources: none added. Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* No other M18 page or draft edits chapter 18 or 19. `ch14-face-prototype` names chapter 19 only for a source note's format and does not edit it.
* `try-before-commit` and `ch13-teach-the-agent` both insert lines in chapter 13's "Review the staged change"; this delivery leaves chapter 13 as it is (decision 6), so no hunk is shared.
* `ch11-agent-runs-propose`, `early-no-forward-links` and the other M18 pages touch other chapters.

**Out of scope.**

* A change to the kit's rule that the agent stages and never commits on its own: focus-kit's repository (decision 3).
* How a host asks before running a git command: chapter 8's.
* Chapter 13: decision 6.

**Done when.**

* [x] Both editions written: chapter 19's three lines and chapter 18's ending as Behaviour says.
* [x] Chapters 18 and 19 still open with their value, keep their gain, no filler and nothing useful cut.
* [x] Every number sourced: none added.
* [x] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Proof.**

* en/pt 19:177 became three lines, 19:177-179, word for word as Behaviour says; en/pt 18:171 ends as Behaviour says.
* Behaviour's greps: the old chapter 19 sentence and the old chapter 18 ending print nothing; "Each step comes after your reading" / "Cada passo vem depois da sua leitura" and "never the agent on its own" / "nunca o agente sozinho" print one line per edition.
* `git diff --stat` on the four paths: 8 insertions, 4 deletions, only these lines.
* `make verify` green: build, parity, em dash, prose, width, links, disclosure.

**Divergences.** None from Behaviour. Decision 5's premise is wrong: chapters 18 and 19 teach `git rebase`, `git reset --hard`, `git revert` and `git merge --abort`, never a rebase stopped in the middle or a commit on the wrong branch; the line keeps the page's examples and the fix is queued (Review).

**Decisions taken in /apply.**

* Run in a batch of applies on one tree: the driver marks this line in docs/06, runs `make book` once at the end of the batch and gives both PDF paths, and stages and commits this delivery by its paths.
* The review's findings change the wording Behaviour fixed word for word, so they go to a queue line for the author instead of being applied here.

**Review.** One read-only agent on Opus read the diff of the four paths against this page and docs/04, with the context of chapters 18 and 19 in both editions: nothing breaks the page or docs/04; the four costs at en/pt 19:280-284 stay true. Four findings for a queue line: (1) en/pt 19:178 "any of them" points to line 177's four steps, while its list drops "removes a worktree" and adds "pushes"; (2) en/pt 19:178's tangles, a rebase left half done and a commit on the wrong branch, are not taught in chapters 18 or 19 (decision 5's premise); a taught one, such as a merge stopped by a conflict (`git merge --abort`, 19:213) or a commit to take back (`git revert`, 18:138), fits; (3) en/pt 19:179 "marker" comes before the conflict markers are taught at 19:186-199, and "conflict marker" / "marcador de conflito" matches 19:4; (4) pt 18:171 "nunca o agente sozinho" can read as "never without the person"; "por conta própria" matches pt 19:177.

```commit
docs(ch19-agent-does-git): say the agent takes any git step when asked

- Chapter 19, Worktrees in the kit: the agent takes no history step on its own; asked, it takes any, each after the person's reading
- Chapter 18, Choosing: the rule ends "never the agent on its own"

work/done/ch19-agent-does-git.md
```
