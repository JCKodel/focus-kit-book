# ch17-delivery-time

**Objective.** A reader of chapter 17 who asks how long a delivery took is told to measure it from the commit that added its line to the queue to the commit that closed it, a pair of commits that exists on trunk, instead of from the first commit that touched its page to the commit that moved it to `work/done/`, which on trunk are one commit; both editions. Found by `m15-review` (work/done/m15-review.md, B3: "17:26, 69: a delivery's time measured between two commits that on trunk are one. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The measure becomes "from the commit that added its line to the queue to the commit that closed it". On trunk a delivery's page and build are one commit (docs/05 §5 Git; docs/03 "trunk" and "unit of work"), and the marks `[~]`, `[>]` and `[*]` change in the working tree and reach the history only with the person's commit (chapter 14, "On trunk, the mark changes in the queue of the folder where the session runs, at once, and reaches the history with the person's commit."). So the history holds two moments of a delivery: the commit that put its `[ ]` line in docs/06 and the commit that closed it. Checked in this repository: the line `ch05-lend-pointer` entered docs/06 in the commit of `m15-review` and closed in its own commit, 2 h 20 min later the same day. The measure holds on a branch or worktree as well, where the closing commit is the merge, so the chapter needs no branch caveat. Sources: docs/05 §5, docs/03, chapter 14.
2. The chapter says what the measure counts: from asked to done, the waits included. The build alone leaves no trace in the history on trunk; a manager's "how long did it take" is answered honestly by the span from request to done, and the sentence says so instead of letting the reader take it for build time. The author may reject this if they want build time only, which would need a record the kit does not keep (docs/05 §7: no tool the deliveries did not ask for).
3. The chapter says why the closing commit alone cannot answer, and the edge where the history cannot: a line added in the same commit that closed it (docs/05 §2 lets /propose add a missing line, which a person may commit together with the delivery) has no earlier date. An agent asked for that delivery's time must say the history cannot tell, not guess (chapter 17 §The person is the brain).
4. Line 69's answer changes to the same pair of dates. "The commit dates of their five slugs" gives one date per slug on trunk, so no duration; it is the same finding (B3 names 17:69).
5. No git command is shown. Chapter 17 states every answer in prose and the agent does the lookup; chapter 18 teaches `git log`. A command finding the line's first commit (`git log -S`) also matches a later commit whose line names the slug in `· after`, so showing it would need a caveat this chapter does not need. Source: chapter 17 as it stands, docs/04 "Teach, do not report".
6. No number enters the chapter: the check of decision 1 is evidence for this page, not for the reader, and the chapter's gain keeps its one number (docs/04 "One gain", "Numbers that prove").
7. No pointer added. Line 21 already points to chapter 18 for the git history, and docs/04 §Chapter pointers allows one per chapter for each target; "trunk" is used from chapter 14 on.
8. No docs/03 term, no new queue line, no split: two files, two passages each. Sources: docs/03 ("queue line", "commit", "trunk" exist), docs/05 §1. No "lead time": the book does not use the term and the sentence says what it counts.

**Behaviour.**

* A reader of chapter 17 §What the agent already reads, after "In progress is the `[~]` and `[*]` lines, and blocked is the `[?]` lines, each with its reason.", reads, in place of "How long a delivery took is the distance between the first commit that touched its page and the commit that moved it to `work/done/`.", these two lines (one sentence per line, as the chapter is written):
  * en:
    * "How long a delivery took runs from the commit that added its line to the queue to the commit that closed it: from asked to done, the waits included."
    * "The closing commit cannot say it alone, because on trunk a delivery is one commit, which dates its end and not its start; a line added in that same commit has no earlier date, and the history cannot tell how long it took."
  * pt, §O que o agente já lê, after "Em andamento são as linhas `[~]` e `[*]`, e travado são as linhas `[?]`, cada uma com o seu motivo.", in place of "Quanto tempo uma entrega levou é a distância entre o primeiro commit que tocou a página dela e o commit que a moveu para `work/done/`.":
    * "Quanto tempo uma entrega levou vai do commit que acrescentou a linha dela à fila até o commit que a fechou: do pedido ao fim, com as esperas incluídas."
    * "O commit que a fecha não diz isso sozinho, porque no trunk uma entrega é um commit só, que data o fim dela e não o começo; uma linha acrescentada nesse mesmo commit não tem data anterior, e o histórico não sabe dizer quanto tempo ela levou."
* A reader of §The questions the team asks reads:
  * en: "* **How long did the last five deliveries take?** For each, the date its line entered the queue and the date of the commit that closed it." in place of "... The commit dates of their five slugs."
  * pt, §As perguntas que o time faz: "* **Quanto tempo levaram as últimas cinco entregas?** Para cada uma, a data em que a linha dela entrou na fila e a data do commit que a fechou." in place of "... As datas dos commits dos seus cinco slugs."
* The reader can explain why one commit cannot give a delivery's duration on trunk, and what the measure includes (the time the line waited in the queue).
* Checked, both editions, on `book/en/17-project-as-assistant.md` and `book/pt/17-project-as-assistant.md`:
  * en: `grep -c "first commit that touched"` gives 0; `grep -c "commit dates of their five slugs"` gives 0; `grep -c "the commit that added its line to the queue"` gives 1; `grep -c "the date its line entered the queue"` gives 1.
  * pt: `grep -c "primeiro commit que tocou"` gives 0; `grep -c "datas dos commits dos seus cinco slugs"` gives 0; `grep -c "o commit que acrescentou a linha dela à fila"` gives 1; `grep -c "a data em que a linha dela entrou na fila"` gives 1.
* The rest of chapter 17 is unchanged: line 21's pointer to chapter 18, line 65's "lines closed and lines opened per day", and the key point "how long each delivery took" stay as they are.
* Fails: one edition changed and not the other; the measure still naming the page's first commit or the move to `work/done/`; a git command, a number or a new pointer added; any other line of chapter 17 changed; any other file changed but this page and the line's marks in docs/06; an em dash.

**Contract.**

* Files: `book/en/17-project-as-assistant.md`, `book/pt/17-project-as-assistant.md`; no other file.
* Passages, found by text (line numbers in the working tree of 2026-10-17, a courtesy): §What the agent already reads / §O que o agente já lê, the sentence on line 26, replaced by two lines; §The questions the team asks / §As perguntas que o time faz, the bullet on line 69, its answer replaced.
* Terms of docs/03: none new ("queue line", "commit", "trunk", "delivery" already there). Sources: none added or removed. Cases: none; no Case A, Case B or Ninjobs passage changes. Code blocks: none added. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on nearby chapters.** None touches chapter 17 (`grep` of `work/*.md` for chapter 17 found none). `ch18-log-evidence` changes chapter 18 only; no file in common.

**Out of scope.**

* Line 65, "lines closed and lines opened per day, from the queue and the commit dates": it holds on trunk, since each closed line is a commit and each opened line a change to docs/06.
* The key point "how long each delivery took": names no mechanism, so it stands.
* Line 21, "the commit that closes a delivery ends with its slug": not this finding; the closing commit's last line is `work/done/<slug>.md`.
* A git command for the measure: decision 5.
* Build time alone, apart from the queue wait: the history on trunk does not hold it (decision 2).

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapter 17 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: links, edition parity, prose rules, block width, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, the change draws on no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Proof.**

* The Behaviour greps, both editions: "first commit that touched" / "primeiro commit que tocou" 0; "commit dates of their five slugs" / "datas dos commits dos seus cinco slugs" 0; "the commit that added its line to the queue" / "o commit que acrescentou a linha dela à fila" 1; "the date its line entered the queue" / "a data em que a linha dela entrou na fila" 1.
* `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* Divergences: none.

**Delivery review.** A read-only agent on Opus read `git diff` and `git diff --cached` of the two chapter files, this page and this line's hunk of docs/06 against this page and docs/04. The staged text matches Behaviour word for word in both editions; nothing else changed.

1. The line was still `[*]` and its hunk unstaged while Done when was ticked. Timing: the review runs before /apply's last edit, which marks the line `[x]` and stages its hunk.
2. The en "How long a delivery took runs from" reads a little awkwardly. Optional; kept, since it is Behaviour's text and parallels the question the paragraph answers. No change.
3. The key point "how long each delivery took" sits beside the new edge where the history cannot tell. The agent agrees it stands, as Out of scope says. No change.
4. Line 21, "the commit that closes a delivery ends with its slug", is inexact against docs/05 §6, whose last line is the page's path. Not this delivery's: a new `[ ]` line, `ch17-closing-commit`.

**Commit.**

```commit
docs(ch17-delivery-time): date chapter 17's deliveries from the queue

- Measure a delivery from the commit adding its queue line to its close
- Say why the closing commit alone cannot date a delivery on trunk
- Give the five deliveries' question the same pair of dates
- Both editions

work/done/ch17-delivery-time.md
```
