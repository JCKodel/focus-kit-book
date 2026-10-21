# ch08-23-branch-read

**Objective.** After chapters 8, 12, 13, 14, 17, 18, 19, 20 and 23 the reader learns one rule for reading the queue off trunk, the rule docs/05 §4 states: each slug's line comes from its branch, local or remote, with the lines only a branch has, reconciled by slug. A branch already on the remote means the line is taken, unless the definition is being resumed. And chapter 8's Git item says only what the record of `kit-2026-10-20-1` holds.

**Behaviour.**

* Given chapter 12 :27 and its key point :172 (pt :27, :181), and chapter 20 :62 and its key point :89 (pt :62, :89), the reader sees each slug's line read from its branch, not from "its worktree or branch" (C22, C5 of `work/done/m25-review.md`).
* Given chapter 14 :64 (pt :65) and chapter 20 :62's tail, the reader sees a mark become visible to a reader once it is committed on a branch, and on the remote once that commit is pushed. No passage promises a mark that is only in a worktree's file, which the reading rule never reads (C5).
* Given chapters 8 :103, 12 :27, 13 :28, 14 :193, 17 :132, 20 :62 and 23 :66 (pt 8 :105, 12 :27, 13 :28, 14 :194, 17 :132, 20 :62, 23 :66), the reader sees the lines only a branch has taken in, in the same phrase chapter 14 :62 already uses (C27, C5).
* Given chapter 18 :25 and chapter 19 :179, the reader sees `/propose` check the remote for the slug's branch, a branch already there meaning the line is taken unless the definition resumes, as chapter 12 :28 says. It then either creates the branch or reuses it on resumption (C27).
* Given chapter 8's excerpt, the Git item reads "trunk, with the Publish policy, the agent never pushes", as a project choice, `None`, with no ADR number and no sentence about the kit's slot, because `work/done/kit-2026-10-20-1.md` :84 records neither. The explanation after it (en :89, pt :91) no longer claims that this item shows what the kit says beside the choice (C6).
* Fails if any of these remains: "worktree or branch" (pt "worktree ou ... branch") in a sentence this delivery edits; a passage in the list above that reads lines off trunk without the lines only a branch has; a promise that a worktree's file shows a mark to other readers; ADR-0010 or the kit's slot offer in the Git item; a row of chapter 8's block over 74 columns (docs/04); one edition changed without the other; anything later than focus-kit 2026.10.20.1 taught.
* Edge: on trunk every passage keeps reading the folder's one queue. Nothing about trunk changes, and `git fetch` and the "taken" wording stay where `ch08-23-fetch-taken` put them.

**Contract.** Both editions, same change; English is the source (ADR-0004). Line numbers are as the files are at HEAD `7664d02`. The rule is docs/05 §4 :128 to :133 as it reads at HEAD, the template's text at 2026.10.20.1: "after `git fetch`, a line whose branch exists is taken, whatever main shows, and whoever reads the queue there, a board or a session picking free lines or resolving an `after`, takes each slug's line from that branch, local or remote, and the lines only a branch has, reconciled by slug as below." The shared phrase is chapter 14 en :62 / pt :63: "from its branch, local or remote, and the lines only a branch has" / "no branch dele, local ou remoto, e as linhas que só um branch tem". Each edit below is anchored on the quoted clause alone, so a neighbour's change to the rest of the sentence does not move it.

* `book/en/08-install-and-hosts.md` :76 to :79, inside the fenced excerpt:
  * now:
    ```
    * docs/05 §5, Git: a project choice, not a migration: trunk, ADR-0010,
      with the Publish policy, the agent never pushes. The kit's slot
      offers, for a branch or a worktree per delivery, /propose pushing
      the branch it creates; on trunk no branch is created. None.
    ```
  * becomes (rows of 61 and 56 columns):
    ```
    * docs/05 §5, Git: a project choice, not a migration: trunk,
      with the Publish policy, the agent never pushes. None.
    ```
* `book/pt/08-install-and-hosts.md` :76 to :80, inside the fenced excerpt:
  * now:
    ```
    * docs/05 §5, Git: uma escolha do projeto, não uma migração: trunk,
      ADR-0010, com a Publish policy, o agente nunca envia. O slot
      do kit oferece, para um branch ou um worktree por entrega, o
      /propose enviar o branch que cria; no trunk nenhum branch é
      criado. Nenhuma.
    ```
  * becomes:
    ```
    * docs/05 §5, Git: uma escolha do projeto, não uma migração: trunk,
      com a Publish policy, o agente nunca envia. Nenhuma.
    ```
  * The other rows of both blocks do not move.
* `book/en/08-install-and-hosts.md` :89: `the item names that choice and what the kit says beside it, and asks for no change.` becomes `the item names that choice and asks for no change.`
* `book/pt/08-install-and-hosts.md` :91: `o item cita essa escolha e o que o kit diz ao lado dela, e não pede mudança.` becomes `o item cita essa escolha e não pede mudança.`
* `book/en/08-install-and-hosts.md` :103: `reads each slug's line from its branch, local or remote, reconciling them by slug` becomes `reads each slug's line from its branch, local or remote, and the lines only a branch has, reconciling them by slug`.
* `book/pt/08-install-and-hosts.md` :105: `lê a linha de cada slug no branch dele, local ou remoto, reconciliando-as pelo slug` becomes `lê a linha de cada slug no branch dele, local ou remoto, e as linhas que só um branch tem, reconciliando-as pelo slug`.
* `book/en/12-propose.md` :27: `from that slug's worktree or branch, local or remote, reconciled by slug` becomes `from that slug's branch, local or remote, with the lines only a branch has, reconciled by slug`.
* `book/pt/12-propose.md` :27: `no worktree ou no branch daquele slug, local ou remoto, reconciliadas pelo slug` becomes `no branch daquele slug, local ou remoto, com as linhas que só um branch tem, reconciliadas pelo slug`.
* `book/en/12-propose.md` :172: `judging them off trunk from each slug's own branch or worktree` becomes `judging them off trunk from each slug's own branch`.
* `book/pt/12-propose.md` :181: `pelo branch ou worktree de cada slug` becomes `pelo branch de cada slug`.
* `book/en/13-apply.md` :28: `from that slug's branch, local or remote, reconciling them by slug` becomes `from that slug's branch, local or remote, and the lines only a branch has, reconciling them by slug`.
* `book/pt/13-apply.md` :28: `no branch daquele slug, local ou remoto, reconciliando-as pelo slug` becomes `no branch daquele slug, local ou remoto, e as linhas que só um branch tem, reconciliando-as pelo slug`.
* `book/en/14-queue-states.md` :64: `a worktree's file shows the mark the moment it changes, a branch once the mark is committed on it, a remote branch once that commit is pushed.` becomes `a branch shows the mark once it is committed on it, a remote branch once that commit is pushed.`
* `book/pt/14-queue-states.md` :65: `o arquivo de um worktree mostra a marca no momento em que ela muda, um branch quando a marca entra em um commit nele, um branch remoto quando esse commit é enviado.` becomes `um branch mostra a marca quando ela entra em um commit nele, um branch remoto quando esse commit é enviado.`
* `book/en/14-queue-states.md` :193: `from each slug's own branch, local or remote, and moves` becomes `from each slug's own branch, local or remote, with the lines only a branch has, and moves`.
* `book/pt/14-queue-states.md` :194: `no branch de cada slug, local ou remoto, e move` becomes `no branch de cada slug, local ou remoto, com as linhas que só um branch tem, e move`.
* `book/en/17-project-as-assistant.md` :132: `takes each slug's line from its branch, local or remote, reconciling them by slug` becomes `takes each slug's line from its branch, local or remote, and the lines only a branch has, reconciling them by slug`.
* `book/pt/17-project-as-assistant.md` :132: `pega a linha de cada slug no branch dele, local ou remoto, reconciliando-as pelo slug` becomes `pega a linha de cada slug no branch dele, local ou remoto, e as linhas que só um branch tem, reconciliando-as pelo slug`.
* `book/en/18-git-essentials.md` :25: `for the branch named after the slug, creates it and pushes it at once` becomes `for the branch named after the slug, a branch already there meaning the line is taken unless the definition resumes, creates it and pushes it at once`.
* `book/pt/18-git-essentials.md` :25: `pelo branch com o nome do slug, cria o branch e dá push nele na hora` becomes `pelo branch com o nome do slug, já que um branch que já está lá quer dizer que a linha está ocupada, a não ser que a definição seja retomada, cria o branch e dá push nele na hora`.
* `book/en/19-worktrees.md` :179: ``checks the remote for `<prefix>/<slug>`, creates the worktree`` becomes ``checks the remote for `<prefix>/<slug>`, a branch already there meaning the line is taken unless the definition resumes, creates the worktree``.
* `book/pt/19-worktrees.md` :179: ``consulta o remoto por `<prefixo>/<slug>`, cria o worktree`` becomes ``consulta o remoto por `<prefixo>/<slug>`, já que um branch que já está lá quer dizer que a linha está ocupada, a não ser que a definição seja retomada, cria o worktree``.
* `book/en/20-team-tools.md` :62: `reads each slug's line from its worktree or its branch, so one delivery's push carries every other delivery's mark as far as it can see it: a worktree's the moment it changes, a branch's once committed on it, a remote branch's once pushed.` becomes `reads each slug's line from its branch, local or remote, and the lines only a branch has, so one delivery's push carries every other delivery's mark as far as it can see it: a branch's once committed on it, a remote branch's once pushed.`
* `book/pt/20-team-tools.md` :62: `lê a linha de cada slug no worktree ou no branch dele, então o envio de uma entrega leva a marca de cada outra entrega até onde consegue vê-la: a de um worktree no momento em que ela muda, a de um branch quando entra em um commit nele, a de um branch remoto quando esse commit é enviado.` becomes `lê a linha de cada slug no branch dele, local ou remoto, e as linhas que só um branch tem, então o envio de uma entrega leva a marca de cada outra entrega até onde consegue vê-la: a de um branch quando entra em um commit nele, a de um branch remoto quando esse commit é enviado.`
* `book/en/20-team-tools.md` :89: `read from each slug's worktree or branch.` becomes `read from each slug's branch.`
* `book/pt/20-team-tools.md` :89: `lido do worktree ou do branch de cada slug.` becomes `lido do branch de cada slug.`
* `book/en/23-adoption.md` :66: ``each slug's line from its branch after `git fetch`, a line whose branch exists`` becomes ``each slug's line from its branch after `git fetch`, with the lines only a branch has, a line whose branch exists``.
* `book/pt/23-adoption.md` :66: ``a linha de cada slug no branch dele depois de um `git fetch`, uma linha cujo branch existe`` becomes ``a linha de cada slug no branch dele depois de um `git fetch`, com as linhas que só um branch tem, uma linha cujo branch existe``.
* Terms of docs/03: `remote` / `remoto`, `claim` / `reivindicação`, `free line` / `linha livre` exist; "taken" / "ocupada" is plain language. No new row.
* Sources: docs/05 §4 :128 to :133 at HEAD; `work/done/kit-2026-10-20-1.md` :84 for the Git item ("The Git slot is trunk with the Publish policy's 'the agent never pushes' ...: recorded project choices; none."); chapter 12 :28 for the taken-unless-resuming phrase. No source note: the reader gains nothing to open.
* Neighbouring lines on the same files. Before this line: `ch09-14-token-wording`, which changes chapters 13 and 14 and may reword the token clause of 13 :28. That is why /apply matches on the quoted clauses and not on whole sentences, and finds the lines again by text if they moved. After this line, writing against its result: `ch08-update-2026-10-20-2` to `-5` and `ch08-copilot-cli` (chapter 8); `ch13-19-session-folder` and `ch13-19-claim-script` (chapters 13 and 19); `ch12-14-18-several-slugs` (chapters 12, 13, 14 and 18); `ch14-after-over-token` (chapter 14). `m25-records-claims` touches records only.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.**

* Chapter 17 :119: it says "from the delivery branches after `git fetch`", the words of the kit's `AGENTS.md` line (SETUP.md 2026.10.20.1, :999 to :1001). Adding more would make it say more than the rules line it paraphrases.
* Chapter 14 :209 (pt :210), key point: "from each slug's own branch, local or remote" already agrees with the rule. No candidate cites it for the lines only a branch has, and a key point stays short. Chapter 12 :172 and chapter 20 :89 likewise only lose "or worktree".
* Chapter 14 :62 (pt :63): it already holds the full phrase and is the source of the shared wording.
* Chapter 8 :93 ("Git stays trunk"): still true.
* docs/05, docs/03 and the records, including `ch08-update-2026-10-20-1`'s page, which said the Git item stays word for word: history, left as it was; `m25-records-claims` owns the records.
* The candidates of the other two finding lines: `ch09-14-token-wording` and `m25-records-claims`.

**Done when.**

* [x] Every edit of the Contract made in both editions, and nothing else in the nine chapters moves.
* [x] `grep -n "worktree or\|worktree ou" ` over the edited sentences finds none; ADR-0010 is gone from chapter 8's block; every row of the block is within 74 columns.
* [x] Both editions written, each opens with its value, no filler and nothing useful cut, every number sourced (no number added), no em dash.
* [x] Delivery review by one read-only Opus agent, over this page and `git diff HEAD` of the eighteen chapter files (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here, with AGENTS.md, taken from the context it was given and not opened as files; its report says it consulted an advisor once, of which this session has no other record.
* [x] `make verify` green.
* [x] `make book` exit 0, with `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Decisions taken alone.**

* The reading rule is docs/05 §4 as it reads at HEAD ("from that branch, local or remote, and the lines only a branch has"). The quote handed with the task ("from its worktree's file, or from its branch") is the 2026.10.19.1 template, replaced by `kit-2026-10-20`, and following it would reverse C22.
* One shared phrase everywhere: chapter 14 :62's "and the lines only a branch has" / "e as linhas que só um branch tem", with "with" / "com" where "and" would read as a second object.
* Chapter 14 :64 and chapter 20 :62's tail lose the worktree's-file clause. `ch08-23-fetch-taken` had kept :64 out as being about visibility, but with readers taking the line from the branch, a promise about a worktree's file contradicts the rule, and C5 now cites it.
* Siblings beyond the cited lines: chapter 12 :27 and chapter 20 :62 get the full phrase because they are edited anyway; chapter 14 :193 gets it because C5 cites it; the key points 12 :172, 14 :209 and 20 :89 stay short.
* C6: the Git item is cut to what the record holds, and chapter 8 :89 / pt :91 drops "and what the kit says beside it", which would otherwise claim the excerpt shows a kit sentence it no longer holds. The kit's own rule (SETUP.md 2026.10.20.1 :42 to :44, "with what the kit says") is not retaught here.
* The taken-unless-resuming wording in chapters 18 and 19 reuses chapter 12 :28's phrase, adding "unless the definition resumes" so that reuse on resumption does not read as a contradiction.
* Token `(P-)` confirmed: the definition takes nothing from `ch09-14-token-wording`'s page; the build shares chapters 13 and 14 with it, so it waits for that line to be `[x]`.

**Built.** The twenty-eight replacements of the Contract in the eighteen files, each matched on its quoted clause alone, every clause found once and at the line the Contract names (`ch09-14-token-wording` and `m25-records-claims` moved none of them). Chapter 8's Git item is two rows in each edition, en 60 and 56 characters, pt 67 and 54; the Contract's "61" counted `§` as two bytes. `git diff --stat HEAD -- book/` shows 29 insertions and 34 deletions over the eighteen files, the five lines fewer being chapter 8's two blocks.

**Proof.** `make verify` exit 0 after the Contract's edits (build, parity, em dash, prose, width, examples, links, disclosure). No added line of the diff holds "worktree or" or "worktree ou"; `ADR-0010` no longer appears in either chapter 8.

**Divergences.** Two, both from the Delivery review: en chapter 14 :64 reads "a branch shows the mark once the mark is committed on it", not the Contract's "once it is committed on it", where "it" could be read as the branch; pt keeps the Contract's words, whose "ela" can only be the mark. And the Contract (:15) and the second Decision taken alone quote chapter 14 en :62 / pt :63 as "and the lines only a branch has" / "e as linhas que só um branch tem", which at `7664d02` read "adds the lines only a branch has" / "acrescenta as linhas que só um branch tem"; the edits carry the Contract's phrase, and the quotes stay as the plan wrote them.

**Decisions taken by /apply.** Chapters 18 :25 and 19 :179 keep the Contract's "unless the definition resumes" beside the sentence's later "or reuses it when the definition resumes", as the page's decision on them chose, so the taken rule never reads as having no exception.

**Delivery review.** One read-only Opus agent, launched with the eighteen chapter files and this page as the delivery's paths. It read this page, docs/05 :125 to :135, `work/done/kit-2026-10-20-1.md` :80 to :90, `git diff HEAD` of the eighteen files, the edited sentences in context (chapter 8 en :66 to :106 and pt :66 to :108, 12 :27 to :28, 14 en :62 to :64 and pt :63 to :65, 18 :25, 19 :179, 20 :62), `git show 7664d02` of chapter 14 :62, and grepped `book/` for em dashes, ADR-0010 and "worktree or/ou"; AGENTS.md and docs/04 it says came from the context it was given; it did not open them as files. Its report says it consulted an advisor once before reporting; this session has no other record of that. It found every replacement at its named line in both editions, nothing else moved, chapter 8's rows within 74 columns, and the edits agreeing with docs/05 §4 :128 to :133, chapter 12 :28 and chapter 14 :62. Findings: Built said twenty-six replacements for the Contract's twenty-eight, fixed above; chapters 18 and 19 state the resumption exception twice in one sentence, not taken, as Decisions taken by /apply says; en chapter 14 :64's "it" was ambiguous, taken as the Divergence above; the page's Contract quotes chapter 14 :62 as "and the lines only a branch has" while the line reads "adds the lines only a branch has", the edits' words being docs/05 §4 :133's, left as the page's history. Nothing false outside this delivery.

**Verify and book after the last edit.** `make verify` exit 0 after the review's fixes; then `make book` exit 0, built from HEAD `6daa835` with this delivery's unstaged edits in `book/` and no other change there, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. `make verify` exit 0 again after this page's last edit.

```commit
docs(ch08-23-branch-read): nine chapters read the queue as §4 says

- Each slug's line from its branch, with the lines only a branch has
- No reader promised a mark that is only in a worktree's file
- Chapters 18 and 19: a branch on the remote means the line is taken
- Chapter 8's Git item says only what kit-2026-10-20-1 records

work/done/ch08-23-branch-read.md
```
