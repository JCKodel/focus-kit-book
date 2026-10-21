# m28-claim-wording

**Objective.** After chapters 13 and 19, docs/03's claim and container folder rows and ADR-0018's `kit-2026-10-20-4` amendment, the reader reads what the kit's claim script does as `.claude/skills/propose/scripts/claim.sh` (2026.10.20.4) does it: the worktree's branch is the prefix and the slug joined, `focus-kit/return-book` by default, not two names with a slash between; on trunk the path it prints is the top of the repository; a branch already on the remote is reused and not pushed again; and with a branch per delivery the remote is checked for the slug's own branch.

**Behaviour.** What the reader can do or explain afterwards:

* Asked which branch a worktree per delivery uses for `return-book` / `devolver-livro`, answer from chapter 19: `<prefix><slug>`, the prefix and the slug joined, `focus-kit/return-book` with the default prefix `focus-kit/`; a slot naming `wt/` gives `wt/return-book` (chapter 19's own example, unchanged). The script builds `$prefix$slug` (claim.sh :39).
* Asked which folder the script prints on trunk, answer from chapter 13: the top of the repository, whichever of its folders the session runs in; it is the folder git runs the alias from, which chapter 13's git-config quote earlier in the same paragraph says (claim.sh :15, :27).
* Asked whether the script pushes a branch already on the remote, answer from chapter 13 and ADR-0018: no; with a branch or a worktree per delivery it pushes the branch only when the remote lacks it, when it creates it or when it reuses a local one the remote never got (claim.sh :63, :69-72, :74-80, :85-96).
* Asked which ref the remote is checked for, answer from docs/03's claim row: `refs/heads/<slug>` with a branch per delivery, `refs/heads/<prefix><slug>` with a worktree per delivery (claim.sh :41, :39, :63).
* Edge: docs/03's container folder row names the same branch as chapter 19, `<prefix><slug>`, so the domain table and the chapter agree.
* Edge: chapter 13's sentences about where `/apply` and `/propose` *read* the queue ("the folder where the session runs", chapter 13 en :38, chapter 12 :28, :29, :164, :200, chapter 14 :59, chapter 17 :132) are untouched: they are about the queue a session reads, not the path the script prints.
* Fails: `grep -rn -e '<prefix>/<slug>' -e '<prefixo>/<slug>' book docs` prints a line; chapter 13's trunk clause still says "the folder where the session runs"; a worktree clause or the ADR saying the script "pushes its branch" with no condition; docs/03 :117 giving `refs/heads/<prefix>/<slug>` for both strategies.
* Edge: no version, date, run or commit hash in chapter text; no em dash; nothing implying Case B ran on the process.

**Contract.** Two chapters in both editions, docs/03 and ADR-0018, against the files as they are now (en/pt: chapter 13, 291/291 lines; chapter 19, 393/393); one sentence per line, as the chapters are laid out; anchors are quoted clauses, since lines move. Source for every statement: `.claude/skills/propose/scripts/claim.sh`, as installed by `kit-2026-10-20-4`.

* `book/en/13-apply.md` and `book/pt/13-apply.md`, "What `/apply` does", the sentence that begins "On trunk the script creates, fetches and pushes nothing" (en :28) / "No trunk o script não cria, não busca e não dá push em nada" (pt :28), replaced whole by:
  * en: "On trunk the script creates, fetches and pushes nothing and prints the top of the repository, whichever of its folders the session runs in; with a branch per delivery it switches to the slug's own branch, the slug with no prefix, creating or reusing it and pushing it only when the remote lacks it ([chapter 18](18-git-essentials.md)); with a worktree per delivery it creates or reuses the worktree and, the same way, pushes its branch only when the remote lacks it, and the `path` it prints is that worktree's ([chapter 19](19-worktrees.md))."
  * pt: "No trunk o script não cria, não busca e não dá push em nada e imprime o topo do repositório, qualquer que seja a pasta do repositório em que a sessão rode; com um branch por entrega ele troca para o branch do próprio slug, o slug sem prefixo, criando-o ou reaproveitando-o e dando push nele só quando o remoto não o tem ([capítulo 18](18-git-essentials.md)); com um worktree por entrega ele cria ou reaproveita o worktree e, do mesmo jeito, dá push no seu branch só quando o remoto não o tem, e o `path` que ele imprime é o desse worktree ([capítulo 19](19-worktrees.md))."
  * Nothing else in the chapter changes.
* `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`:
  * "Worktrees in the kit", the sentence that begins "`/propose <slug>` checks the remote for" (en :192) / "O `/propose <slug>` consulta o remoto por" (pt :192): en "checks the remote for `<prefix>/<slug>`, a branch already there" becomes "checks the remote for `<prefix><slug>`, the prefix and the slug joined, `focus-kit/return-book` with the default prefix `focus-kit/`, a branch already there"; pt "consulta o remoto por `<prefixo>/<slug>`, já que um branch" becomes "consulta o remoto por `<prefixo><slug>`, o prefixo e o slug juntos, `focus-kit/devolver-livro` com o prefixo padrão `focus-kit/`, já que um branch"; the rest of the sentence stays.
  * Key point (en :381 / pt :381): en "`<hidden>/worktrees/<slug>/` on `<prefix>/<slug>`," becomes "`<hidden>/worktrees/<slug>/` on `<prefix><slug>`,"; pt "`<oculta>/worktrees/<slug>/` no `<prefixo>/<slug>`," becomes "`<oculta>/worktrees/<slug>/` no `<prefixo><slug>`,"; the rest stays.
  * Nothing else in the chapter changes.
* `docs/03-Domain.md`:
  * :96, the row `container folder`, replaced by this exact row (sibling: same notation, see Decisions taken alone):

    ```
    | container folder | pasta contêiner | `.focus-kit/`, `focus-kit/` | The folder of a project with a worktree per delivery whose `main/` is the checkout; it keeps the bare repository in a hidden folder (`<hidden>/repo.git/`) and each delivery's worktree in `<hidden>/worktrees/<slug>/`, on the branch `<prefix><slug>`, the prefix and the slug joined; docs/05's Git slot may name the hidden folder and the prefix, and one that names neither means `.focus-kit/` and `focus-kit/`. |
    ```

  * :117, the row `claim`, replaced by this exact row (code column: the ref each strategy checks; definition: "the remote checked for one first" names which one):

    ```
    | claim | reivindicação | `propose/scripts/claim.sh`; `git ls-remote --exit-code --heads origin refs/heads/<slug>` with a branch per delivery, `refs/heads/<prefix><slug>` with a worktree per delivery | With a branch or a worktree per delivery, the delivery's branch on the remote, which /propose pushes the moment it creates it, or when it resumes on a branch the remote lacks, never one already there, the remote checked first for the slug's own branch with a branch per delivery and for the prefix and the slug joined with a worktree, both by the kit's claim script, which /propose runs through git's own shell: after `git fetch`, a line whose branch exists is taken, whatever the main branch's queue shows, so that queue changes only through merges; on trunk no branch is created, the script creating, fetching and pushing nothing and printing the top of the repository, and a line is taken by its mark in the one working tree (docs/05 §§2, 4, 5). |
    ```

* `docs/adr/ADR-0018-six-marks.md`, "Amendment, 2026-10-21 (kit-2026-10-20-4)" (:80), edited in place: "creates or reuses the branch or worktree, pushes its branch and prints the path the /apply session opens in" becomes "creates or reuses the branch or worktree, pushes its branch only when the remote lacks it, and prints the path the /apply session opens in"; the rest of the paragraph stays (its trunk clause, "prints the one working tree's path", is true: on trunk the top of the repository is that tree).
* Terms: no new row; the two rows above are replaced. Sources: none new; the script is the kit's installed file, already named in docs/03. Cases: none.
* Neighbouring lines: `ch13-16-several-slugs-sessions` (`[ ]`, after this line in the queue) touches chapter 13's :21 and :42, other sentences than :28, and is applied after this one; `ch10-12-no-implicit-hosts` (chapters 10, 12) and `ch08-update-choice-outcome` (chapter 8) touch none of this page's files; `m28-records-claims` touches `work/done/` pages only.

**Out of scope.**

* `work/done/kit-2026-10-20-4.md` :29, the record that C22 cites as equal to ADR-0018 :80: a record page, `m28-records-claims`' if anyone's; it says what that delivery wrote.
* `work/done/ch13-19-claim-script.md`, which kept `<prefix>/<slug>` on purpose: a record of what that delivery decided, true as history; not edited.
* The kit's own `<prefix>/<slug>` (SETUP.md at `ffbec72` :641, installed as `.claude/skills/{brainstorm,analyze}/references/documents.md` :151): the kit's text, not edited here; the note for the kit is below, for the person.
* Chapter 19's refusal list and the latent cases C1, C2, C7 and the weak C3, C4: dropped by the review.
* The "folder where the session runs" sentences about reading the queue (chapters 12, 13 :38, 14, 17): not stale; they say where a session reads, not what the script prints.
* Chapter 13 :21 and :42 (C35) and chapter 16: `ch13-16-several-slugs-sessions`'.

**Decisions from the documents.**

* Every statement against `claim.sh`: `branch="$prefix$slug"` (:39), `branch) branch=$slug` (:41), `path: $top` on trunk (:27, `top` from `git rev-parse --show-toplevel` :15), the remote check of `refs/heads/$branch` (:63), and a push only where `remote` is 0 (:69-80, :85-96).
* "The top of the repository" / "o topo do repositório": chapter 13's own words earlier in the same paragraph (:25), beside git's documentation quoted there.
* Taught as the kit is today, with no version, date or run (AGENTS.md; docs/04).

**Decisions taken alone.** The agent chose each of these.

* `<prefix><slug>` over keeping `<prefix>/<slug>` with a note that the prefix carries its slash: the script's own expression, and chapter 19 :190's `wt/` example already reads that way. This reverses `ch13-19-claim-script`'s decision to keep the kit's notation, on the review's word (C5); the book now departs from the kit's text to match the kit's script.
* A kit note for the person to add to `work/kit-proposals.md` if they choose (this page does not edit it): "**The branch notation** (from m28-review, C5). SETUP.md §3's `<prefix>/<slug>` reads as a double slash with the default prefix `focus-kit/`, while `claim.sh` builds `$prefix$slug`; the next version writes `<prefix><slug>`."
* docs/03 :96 widened as a sibling: it names the same branch in the same notation, would contradict chapter 19 once :192 changes, and no other line owns it.
* docs/03 :117's definition gains which ref is checked, "never one already there" and the trunk print, so the row says the four facts of the queue line itself, not only its code column.
* ADR-0018's amendment edited in place, not amended again: it describes the same version on the same day, and the change corrects a description, not a decision; no earlier finding line sets a precedent either way.
* Chapter 13's worktree clause says "only when the remote lacks it", which covers both the new branch and the resumed one the remote never got; chapter 19 :207 already says the second, unchanged.
* Chapter 13's branch clause gains "the slug's own branch, the slug with no prefix", so the reader of chapter 13 has the queue line's fourth fact without opening docs/03.
* Queue line: no wording change; it names docs/03's claim row, not the container folder row this page widens as a sibling (above).
* Token `(PA)`: every line above is `[x]`; the lines in flight beside it, `ch10-12-no-implicit-hosts` and `ch08-update-choice-outcome`, are below it and touch none of its files, and this page takes nothing from their pages; the only line touching one of its files, `ch13-16-several-slugs-sessions`, is below it and applied after it.

**Divergences.** One, from the delivery review: chapter 13 pt :28's trunk clause reads "qualquer que seja a pasta do repositório em que a sessão rode" in place of the Contract's first wording, "seja qual for a pasta dele em que a sessão roda", whose "dele" could point to the script and whose verb wanted the subjunctive; the Contract above now carries the new wording. Every other sentence went in word for word as the Contract writes it, at chapter 13 :28, chapter 19 :192 and :381 in both editions, docs/03 :96 and :117 and ADR-0018 :80; the chapters keep 291/291 and 393/393 lines. The Delivery review ran without the session's advisor, which docs/05 §5 asks it to keep: it consulted none; and it did not reread docs/04, docs/05 or AGENTS.md beyond what was in its context, while its Done when item, as defined, ticked it as read against them (Delivery review); `m29-records-claims` gave the item the paragraph's words. The commit message below, as `cbab6db` carries it, says docs/03's container folder and claim rows name the ref each strategy checks; only the claim row names the refs checked, the container folder row the branch a worktree is on, `<prefix><slug>`.

**Decisions taken by /apply.** The agent chose this one alone: the Portuguese fix above, the reviewer's own wording, taken as recommended. Nothing else was open; the queue line stands unchanged (docs/06 is the driver's in this batch).

**Proof.**

* Every statement checked against `.claude/skills/propose/scripts/claim.sh`: `branch="$prefix$slug"` (:39), `branch) branch=$slug` (:41), `path: $top` on trunk (:27, `top` :15), the check of `refs/heads/$branch` (:63), pushes only where `remote` is 0 (:69-73, :74-82, :85-97).
* `grep -rn -e '<prefix>/<slug>' -e '<prefixo>/<slug>' book docs` prints nothing; the "folder where the session runs" / "pasta onde a sessão roda" grep prints only :38 in each edition of chapter 13; the "pushes its branch only when" / "dá push no seu branch só quando" grep finds chapter 13 :28 in both editions and ADR-0018 :80.
* No em dash in the added lines; no version, date, run or hash in chapter text.
* `make verify`: green, every check passed, exit 0, after the edits, again after the Portuguese fix and the page's move to `work/done/`, and once more after these two lines.
* `make book`: exit 0, after that verify; `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** One read-only Opus agent, launched by this /apply over this page and `git diff HEAD` of the six files, against the Contract, docs/04, docs/05 §§2 and 3, AGENTS.md and `claim.sh`. It read the page, the diff, `claim.sh` and grep output over `book/` and `docs/`; it did not reread docs/04, docs/05 or AGENTS.md beyond what was in its context, and it consulted no advisor. Its reply: one minor finding, chapter 13 pt :28's "seja qual for a pasta dele em que a sessão roda" reads awkwardly, "dele" able to point to the script and the verb wanting the subjunctive, suggesting "qualquer que seja a pasta do repositório em que a sessão rode", fix now with the Contract line; fixed as Divergences says. Otherwise no finding: all six files changed exactly as the Contract says and nothing else; every statement matches `claim.sh`; docs/03 :117's "checked first" is the claim check, the bare `refs/heads/<slug>` check at :59 only printing a note chapter 19 already covers; the three Done-when greps hold; no em dash, run narration, version, date or hash; both editions agree; nothing touches Case B.

**Done when.**

* [x] Both editions changed as the Contract says in chapters 13 and 19, docs/03's two rows replaced and ADR-0018's sentence edited, nothing else in them.
* [x] `grep -rn -e '<prefix>/<slug>' -e '<prefixo>/<slug>' book docs` prints nothing; `grep -n "folder where the session runs\|pasta onde a sessão roda" book/*/13-apply.md` prints only :38's sentence in each edition.
* [x] `grep -n "pushes its branch only when\|dá push no seu branch só quando" book/*/13-apply.md docs/adr/ADR-0018-six-marks.md` finds chapter 13 in both editions and the ADR.
* [x] Every statement checked against `.claude/skills/propose/scripts/claim.sh`.
* [x] Each chapter still opens with its value, no filler and nothing useful cut, no number added, no em dash, no run narration, no version, date or commit hash in chapter text, nothing implying Case B ran on the process.
* [x] `make verify` green (docs/03's table rows included).
* [x] `make book` run, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, launched by this /apply, over this page and `git diff HEAD` of the six files (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here not reread beyond what was in its context, nor docs/05 or AGENTS.md; it read the page, the diff, `claim.sh` and grep output over `book/` and `docs/`, and consulted no advisor, which docs/05 §5 asks it to keep.
* [x] Page moved to `work/done/`, covered by the last verify.

```commit
docs(m28-claim-wording): say what the claim script does as it does it

- chapter 13: on trunk the script prints the top of the repository; it
  pushes a branch only when the remote lacks it; both editions
- chapter 19: the worktree's branch is <prefix><slug>,
  focus-kit/return-book by default; both editions
- docs/03: the container folder and claim rows name the ref each strategy
  checks
- ADR-0018: the kit-2026-10-20-4 amendment pushes only when the remote
  lacks the branch

work/done/m28-claim-wording.md
```
