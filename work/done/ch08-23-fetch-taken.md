# ch08-23-fetch-taken

**Objective.** After chapters 8, 13, 14, 17 and 23 the reader knows that wherever a session or a board reads the queue off trunk, it runs `git fetch` first, counts a line whose branch exists as taken even before any of its marks is pushed, and reads each slug's line from that slug's branch, local or remote, as docs/05 §4 and chapter 14's key points say; and the Portuguese chapter 8 says "ocupada" as the rest of the Portuguese edition does.

**Behaviour.**

* Given chapter 8's paragraph on the next command (en :110, pt :114), the reader sees the update run `git fetch` first and count a line whose branch exists as taken before naming the first free line (C2 of `work/done/m24-review.md`).
* Given chapter 13 :28, the reader sees `/apply` do the same before it resolves its `after` and weighs the next free line (C2, lead L1).
* Given chapter 17 :132 and the key point :151, the reader sees the "where are we" session count a line whose branch exists as taken, in flight even before any of its marks is pushed, besides running `git fetch` (C3).
* Given chapter 23 :66, the manager's bullet reads each slug's line from its branch after `git fetch`, a line whose branch exists counting as taken (C2).
* Given chapter 14 :62 and :172 (pt :63, :173), the reader reads each slug's line "from its branch, local or remote", the words of the key point en :188 / pt :189 and of docs/05 §4, not "from its worktree, or from its branch" (C6).
* Given the Portuguese excerpt of chapter 8 (pt :71, :77), the reader reads "está ocupada", the word Portuguese chapters 12, 14, 18, 19 and 20 use (C5).
* Fails: a passage in these five chapters that reads lines off trunk without `git fetch` or without the taken rule; "worktree or branch" left in a sentence this delivery edits; "tomada" left in pt chapter 8; a block row over 74 columns (docs/04); one edition changed without the other; anything later than focus-kit 2026.10.20 taught.
* Edge: on trunk every passage keeps reading the folder's one queue; nothing about trunk changes.

**Contract.** Both editions, same change; English is the source (ADR-0004). Line numbers as the files are now (HEAD `cd045ba`). Wording from the installed kit at 2026.10.20: docs/05 §4 ("after `git fetch`, a line whose branch exists is taken, whatever main shows ... takes each slug's line from that branch, local or remote"), docs/03 `free line` and `claim`, chapter 14 :61 ("before any mark on it is pushed").

* `book/en/08-install-and-hosts.md` :110, from "so the update" to the link:
  * now: `so the update reads each slug's line from its worktree or branch, local or remote, and reconciles them by slug ([chapter 14](14-queue-states.md)).`
  * becomes: `` so the update runs `git fetch` first, counts a line whose branch exists as taken even before any of its marks is pushed, whatever the main branch shows, and reads each slug's line from its branch, local or remote, reconciling them by slug ([chapter 14](14-queue-states.md)). ``
* `book/pt/08-install-and-hosts.md` :114, from "então a atualização":
  * now: `então a atualização lê a linha de cada slug no worktree ou no branch dele, local ou remoto, e as reconcilia pelo slug ([capítulo 14](14-queue-states.md)).`
  * becomes: `` então a atualização roda `git fetch` antes, toma como ocupada, antes mesmo de qualquer marca dela ser enviada, uma linha cujo branch existe, mostre o que mostrar o branch principal, e lê a linha de cada slug no branch dele, local ou remoto, reconciliando-as pelo slug ([capítulo 14](14-queue-states.md)). ``
* `book/pt/08-install-and-hosts.md`, inside the fenced excerpt: :71 `está tomada. Proposto,` becomes `está ocupada. Proposto,` (row 68 to 69 columns); :77 `está tomada, mostre` becomes `está ocupada, mostre` (row 62 to 63 columns). No other row of the block moves.
* `book/en/13-apply.md` :28, from "so it reads":
  * now: `` so it reads each line its `after` names, and each line it weighs for the next free line, from that slug's worktree or branch, local or remote, and reconciles them by slug (chapter 14). ``
  * becomes: `` so it runs `git fetch` first, counts a line whose branch exists as taken even before any of its marks is pushed, whatever the main branch shows, and reads each line its `after` names, and each line it weighs for the next free line, from that slug's branch, local or remote, reconciling them by slug (chapter 14). ``
* `book/pt/13-apply.md` :28, from "então ele lê":
  * now: `` então ele lê cada linha que o seu `after` nomeia, e cada linha que pesa para a próxima linha livre, no worktree ou no branch daquele slug, local ou remoto, e as reconcilia pelo slug (capítulo 14). ``
  * becomes: `` então ele roda `git fetch` antes, toma como ocupada, antes mesmo de qualquer marca dela ser enviada, uma linha cujo branch existe, mostre o que mostrar o branch principal, e lê cada linha que o seu `after` nomeia, e cada linha que pesa para a próxima linha livre, no branch daquele slug, local ou remoto, reconciliando-as pelo slug (capítulo 14). ``
* `book/en/14-queue-states.md` :62: `takes each slug's line from its worktree, or from its branch, local or remote,` becomes `takes each slug's line from its branch, local or remote,`; the rest of the sentence stays.
* `book/pt/14-queue-states.md` :63: `pega a linha de cada slug no worktree dele, ou no branch dele, local ou remoto,` becomes `pega a linha de cada slug no branch dele, local ou remoto,`; the rest stays.
* `book/en/14-queue-states.md` :172: `from each slug's worktree or branch, and moves` becomes `from each slug's own branch, local or remote, and moves`.
* `book/pt/14-queue-states.md` :173: `no worktree ou no branch de cada slug, e move` becomes `no branch de cada slug, local ou remoto, e move`.
* `book/en/17-project-as-assistant.md` :132, from "so the session runs":
  * now: `` so the session runs `git fetch` and takes each slug's line from its worktree or branch, local or remote, and reconciles them by slug (chapter 14): ``
  * becomes: `` so the session runs `git fetch`, counts a line whose branch exists as taken, in flight even before any of its marks is pushed, and takes each slug's line from its branch, local or remote, reconciling them by slug (chapter 14): ``; the clause after the colon stays.
* `book/pt/17-project-as-assistant.md` :132, from "então a sessão roda":
  * now: `` então a sessão roda `git fetch` e pega a linha de cada slug no worktree ou no branch dele, local ou remoto, e as reconcilia pelo slug (capítulo 14): ``
  * becomes: `` então a sessão roda `git fetch`, toma como ocupada uma linha cujo branch existe, em andamento antes mesmo de qualquer marca dela ser enviada, e pega a linha de cada slug no branch dele, local ou remoto, reconciliando-as pelo slug (capítulo 14): ``; the rest stays.
* `book/en/17-project-as-assistant.md` :151: `` from the delivery branches after `git fetch`, with the next command; `` becomes `` from the delivery branches after `git fetch`, counting a line whose branch exists as taken even before any of its marks is pushed, with the next command; ``.
* `book/pt/17-project-as-assistant.md` :151: `` nos branches das entregas depois de um `git fetch`, com o próximo comando; `` becomes `` nos branches das entregas depois de um `git fetch`, tomando como ocupada, antes mesmo de qualquer marca dela ser enviada, uma linha cujo branch existe, com o próximo comando; ``.
* `book/en/23-adoption.md` :66: `each slug's line from its worktree or branch, and who owes an answer` becomes `` each slug's line from its branch after `git fetch`, a line whose branch exists counting as taken even before any of its marks is pushed, and who owes an answer ``.
* `book/pt/23-adoption.md` :66: `a linha de cada slug no worktree ou no branch dele, e quem deve uma resposta` becomes `` a linha de cada slug no branch dele depois de um `git fetch`, uma linha cujo branch existe contando como ocupada antes mesmo de qualquer marca dela ser enviada, e quem deve uma resposta ``.
* Terms of docs/03: `free line` / `linha livre`, `claim` / `reivindicação`, `remote` / `remoto`, all present; "taken" / "ocupada" is plain language there, no row. No new row.
* Sources: none added; the chapters already point to chapter 14 and docs/05 §4 where they do.
* Neighbouring lines on the same files, all later in queue order, so this line is applied first and they write against its result: `ch08-update-2026-10-20-1` (chapter 8; it rewrites the excerpt that holds pt :71 and :77) and later deliveries of the queue's plan on chapter 8, the update example at later kit versions and the Copilot CLI as a host; `ch12-14-parallel-token` and later deliveries on a command typed with several slugs, where each session opens and the claim script (chapters 13 and 14); a later delivery on `after` over the parallel token (chapter 14). The parallel lines `ch18-19-fetch-resume` (18, 19) and `ch07-review-merge` (7) touch none of these files; `docs03-free-line-held` touches docs/03 only.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.**

* Chapter 17 :119: it already says "from the delivery branches after `git fetch`", AGENTS.md :37's line, which the review did not cite.
* Chapter 14 :63 to :65 (pt :64 to :66): they speak of where a mark becomes visible, a worktree's file included, not of where a reader takes the line; the review cited none.
* Chapter 8's other excerpt rows: en :76 already says "taken", and pt :71 and :77 are the only "tomada"; the excerpt at 2026.10.20.1 is `ch08-update-2026-10-20-1`'s.
* C1, C4 and P1: `ch18-19-fetch-resume`. D1: `ch07-review-merge`. P6: `docs03-free-line-held`. C7: weak, dropped by the checker.
* docs/03's rows: unchanged here.

**Decisions from the documents.**

* "From its branch, local or remote" is docs/05 §4's phrase at 2026.10.20 (the template in `.claude/skills/*/references/documents.md` :285) and chapter 14's key point; the taken rule is docs/03 `free line` and `claim`, and "before any mark on it is pushed" is chapter 14 :61.
* "Ocupada" for "taken": Portuguese chapters 12, 14, 18, 19 and 20 (C5).
* Chapter 13 :28 is in this line: m24-review's Decisions taken alone put it inside C2.
* Both editions in one delivery (ADR-0004); 74 columns per block row (docs/04); no em dash (AGENTS.md).

**Decisions taken alone.**

* The C2 and C3 sentences in chapters 8, 13, 17 and 23 drop "worktree or" too, reading the line "from its branch, local or remote", so they agree with chapter 14 once C6 is fixed and with docs/05 §4. Only sentences the review cited change; the author can reverse it by keeping "worktree or branch" there.
* Chapter 17 :132 says "taken, in flight": the session's answer has an "In flight" heading, and the clause after the colon is about it.
* Portuguese order "toma como ocupada, antes mesmo de qualquer marca dela ser enviada, uma linha cujo branch existe", so "antes mesmo" cannot attach to "existe"; in chapter 17 :132 and 23 :66 the shorter forms read without that ambiguity.
* No queue-line wording change: the scope is the line's.

**Done when.**

* [x] Every site in the Contract reads as it says, in both editions; nothing else in the five chapters changed (`git diff -U0` shows one hunk per site, 16; with default context pt 8 :71 and :77 merge into one hunk).
* [x] `grep -n "worktree or branch\|worktree, or\|worktree ou no branch\|worktree dele, ou" book/{en,pt}/{08,13,14,17,23}-*.md` prints nothing, its output recorded in the Proof.
* [x] `grep -n "tomada" book/pt/08-install-and-hosts.md` prints only :67's "retomada" (resumption), not "taken"; `grep -nw "tomada"` prints nothing; recorded in the Proof (Divergences).
* [x] pt chapter 8's two excerpt rows at 69 and 63 columns, under docs/04's 74, measured in the Proof.
* [x] Both editions written, each chapter still opens with its value, no filler, nothing useful cut, every number sourced; nothing later than focus-kit 2026.10.20.
* [x] `make verify` green after the last edit.
* [x] `make book`: not run by this lane; the driver runs it after the batch and the milestone review records the build.
* [x] Delivery review by one read-only Opus agent, over this page and `git diff -U0 HEAD` of the ten chapter files, with docs/04's em dash and width rules (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.

**Built.** Every Contract site in both editions: chapter 8 :110 (pt :114) and pt 8's excerpt :71 and :77; chapter 13 :28; chapter 14 :62 and :172 (pt :63 and :173); chapter 17 :132 and :151; chapter 23 :66. All changes are within their lines, so no line number moved.

**Checked.** Each new sentence against the page's quotes of docs/05 §4 and docs/03 `free line` and `claim`, and against chapter 14 :61 and :72 (pt :62 and :73) and its key point en :188 / pt :189. No new term, so docs/03 is unchanged.

**Divergences.** The `tomada` grep of Done when matches "retomada" at pt 8 :67, inside the excerpt row "dele, ou reuse o existente na retomada"; the word means resumption, not taken, and stays. The whole-word grep prints nothing. Otherwise none from the Contract.

**Decisions taken alone in /apply.** None beyond the page's.

**Delivery review.** One read-only Opus agent read this page, `git diff -U0 HEAD` of the ten chapters, pt and en chapter 8 :60 to :90, chapter 14's "taken" / "ocupad" lines, docs/04's em dash and width rules and the Makefile's `verify` target, and ran the parity, em dash, prose, width, examples and links checks (links failed once with no output and passed on rerun). Nothing broke the page or docs/04. Findings:

* pt 8 :67, the `tomada` grep of Done when matches "retomada": recorded in Divergences and the item reworded to what the grep prints.
* en 8 :110 and 13 :28 (pt 8 :114, 13 :28), "the main branch shows" followed by "whatever the main branch shows": wording preference, kept; the Contract fixes the words.
* pt 17 :151, "dela" pointing forward to "uma linha": wording preference, kept; the order the page chose.
* en 8 :84 / pt 8 :87, the excerpt's "branch or worktree per delivery": the delivery mode, not a place to read a line; no change.

**Proof.**

* The first Done when grep printed nothing (exit 1).
* `grep -n "tomada" book/pt/08-install-and-hosts.md` printed `67:  dele, ou reuse o existente na retomada, trazendo para ele`; `grep -nw "tomada"` printed nothing (exit 1).
* `awk 'NR==71||NR==77{print NR": "length($0)}' book/pt/08-install-and-hosts.md`: `71: 69`, `77: 63`.
* `git diff -U0 HEAD -- book/`: 10 files, 16 insertions, 16 deletions, 16 hunks.
* `make verify` passed whole (build, parity, em dash, prose, width, examples, links, disclosure) after the chapter edits, and again after the last edit, the page's move and its records included.
* `make book`: not run by this lane; the driver runs it after the batch and the milestone review records the build.

```commit
docs(ch08-23-fetch-taken): fetch first and count a branch as taken

- ch 8, 13, 17, 23: git fetch first, a line whose branch exists is taken
- ch 8, 13, 14, 17, 23 read each slug's line from its branch
- pt ch 8 excerpt says "ocupada", as the rest of the edition

work/done/ch08-23-fetch-taken.md
```
