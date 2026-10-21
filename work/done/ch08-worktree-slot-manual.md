# ch08-worktree-slot-manual

**Objective.** After chapter 8 the reader sees one rule for a worktree Git slot that names no folder: its folder is proposed only when the project already works in a container, and a missing manual letting a session in `main/` edit the worktrees is reported as lacking whatever the folder. The example of a choice "recorded with a date or an ADR, as the book's Git slot does" points at an excerpt whose Git item names its ADR (C1 and C3 of `work/done/m26-review.md`).

**Behaviour.**

* Given chapter 8 en :94 to :97 (pt :96 to :99), the reader sees the container condition limited to the folder: a worktree Git slot that names no folder has a folder proposed only in a container whose hidden folder holds `repo.git/`, and no folder with no container. "Whatever the folder", a slot whose project has no manual is reported as lacking it, which :76 (pt :78) makes a migration, and nothing in :94 says a migration comes only with a container (C1). This is SETUP step 4 at `da29c25` of the sibling checkout `~/Projects/focus-kit`, its docs/05 §5 item: "a worktree Git slot that names no folder, in a container whose hidden folder already holds `repo.git/`, gets that folder's name and its branches' prefix written in, so nothing moves, and one with no manual letting a session in `main/` edit the worktrees", two checks, the manual in its own clause.
* Given chapter 8's excerpt and the outcome sentence en :77 (pt :79), the reader sees the Git item read "a project choice, not a migration: trunk, ADR-0010, with the Publish policy, the agent never pushes", so "recorded with a date or an ADR, as the book's Git slot does" points at an ADR the excerpt shows (C3). The excerpt says it is paraphrased from `work/done/kit-2026-10-20-2.md`, whose Git item (:76, and the Contract's :18) reads "trunk, a recorded project choice (ADR-0010)".
* Fails if any of these remains: "gets a migration only when" (pt "recebe uma migração só quando") in :94 / pt :96; the excerpt's Git item without ADR-0010; a row of the excerpt over 74 columns (docs/04, rule `width`); one edition changed without the other; an em dash; any other sentence of chapter 8 changed.
* Edge: a worktree slot that names no folder, with no container and no manual, gets no folder proposed and the manual reported as lacking; :96 / pt :98 ("the report proposes no folder") and :97 / pt :99 already say so and do not move.

**Contract.** Both editions, same change; English is the source (ADR-0004). Line numbers as the files are at HEAD `dd0d75a`, unchanged since `cfcfc9d`, the commit the review read. Each edit is anchored on the quoted text alone.

* `book/en/08-install-and-hosts.md` :64, inside the fenced excerpt:
  * now: `* docs/05 §5, Git: a project choice, not a migration: trunk,`
  * becomes (70 columns): `* docs/05 §5, Git: a project choice, not a migration: trunk, ADR-0010,`
  * Rows :65 to :67 do not move.
* `book/pt/08-install-and-hosts.md` :65 to :68, inside the fenced excerpt:
  * now:
    ```
    * docs/05 §5, Git: uma escolha do projeto, não uma migração: trunk,
      com a Publish policy, o agente nunca envia. Um manual que deixe
      uma sessão no main/ editar os worktrees só é pedido a um slot Git
      de worktree. Nenhuma.
    ```
  * becomes (rows of 67, 69, 69 and 27 columns):
    ```
    * docs/05 §5, Git: uma escolha do projeto, não uma migração: trunk,
      ADR-0010, com a Publish policy, o agente nunca envia. Um manual que
      deixe uma sessão no main/ editar os worktrees só é pedido a um slot
      Git de worktree. Nenhuma.
    ```
  * The other rows of both blocks do not move.
* `book/en/08-install-and-hosts.md` :94: `and names no folder gets a migration only when the project already works in a container` becomes `and names no folder has a folder proposed only when the project already works in a container`.
* `book/pt/08-install-and-hosts.md` :96: `e não cita pasta recebe uma migração só quando o projeto já trabalha num contêiner` becomes `e não cita pasta só tem uma pasta proposta quando o projeto já trabalha num contêiner`.
* Unchanged: en :76, :77, :95 to :97 and pt :78, :79, :97 to :99; no docs/03 term; no other file.

Neighbours: `ch12-propose-worktree-path` touches chapter 12 and `m26-records-claims` records in `work/done/`; neither touches chapter 8. This delivery cites `work/done/kit-2026-10-20-2.md` :18 and :76 and does not edit it; the review's candidates for that record (C4, C5) are at its :55 and :56, not its Git item.

**Out of scope.**

* The other candidates of `m26-review`: their own lines (`ch12-propose-worktree-path`, `m26-records-claims`) or no line, as the review decided.
* The cites of chapter 8 in earlier records (C12): `m26-records-claims`.

**Done when.**

* [x] Both editions changed as the Contract says, and nothing else in them.
* [x] Opens with its value, no filler and nothing useful cut, every number sourced: unchanged by two clause edits and one ADR number.
* [x] No "gets a migration only when" / "recebe uma migração só quando" in chapter 8; ADR-0010 in both excerpts' Git item.
* [x] No em dash in the changed lines.
* [x] `make verify` green after the last edit, rule `width` included.
* [x] `make book` with its tree and commit, both PDF paths given.
* [x] Delivery review by one read-only Opus agent, launched by this lane, over this page and `git diff HEAD` of both chapter 8 files, with `work/done/kit-2026-10-20-2.md` :18 and :76 and SETUP.md at `da29c25` (Delivery review), the paragraph naming no docs/04, against which docs/05 §5 has it read; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded; only this delivery's paths and its docs/06 line staged; the page moved to `work/done/` and its commit message suggested.

**Decisions from the documents.** The two checks are separate because SETUP step 4 at `da29c25` gives the manual its own clause ("and one with no manual"), so the fix narrows :94 to the folder and keeps :97. The excerpt is paraphrased from `work/done/kit-2026-10-20-2.md`, whose Git item names ADR-0010, so restoring the number keeps the excerpt faithful; `ch08-23-branch-read` removed it because the record it then quoted, `kit-2026-10-20-1` :84, did not name it, a reason that no longer holds, and `ch08-update-2026-10-20-2`'s own Behaviour (:7) expected "trunk, ADR-0010" in the excerpt. Both editions in one delivery (ADR-0004); 74 columns per row (docs/04).

**Decisions taken alone.** The agent chose each of these:

* C3 fixed by restoring ADR-0010 to the excerpt rather than rewording en :77 / pt :79; the fallback, dropping "as the book's Git slot does", would lose the chapter's only example of a recorded choice.
* The wording "has a folder proposed only when" / "só tem uma pasta proposta quando", which matches :95's "proposes" and :96's "proposes no folder".
* The Portuguese Git item reflowed over its four rows, since "ADR-0010," does not fit on the first; the English one fits on its row.

**Parallel token.** `(PA)` holds: the definition takes nothing from the pages of `ch12-propose-worktree-path` or `m26-records-claims`, and the build touches only the two chapter 8 files, which neither touches.

**Divergences.**

* The Done when item on staging: the batch's rules had this lane stage nothing and leave docs/06 to the driver, so nothing is staged and the line's mark is not this lane's edit.
* None in the text: the four edits are the Contract's line for line, and nothing else in chapter 8 moved.

**Decisions taken alone in /apply.** None beyond the definition's.

**Delivery review.** One read-only Opus agent, launched by this lane, read this page, `git diff HEAD` of `book/en/08-install-and-hosts.md` and `book/pt/08-install-and-hosts.md`, `work/done/kit-2026-10-20-2.md` :18 and :76, and `SETUP.md` at `da29c25` of `~/Projects/focus-kit`; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded. Its reply: "No findings." It found only the four lines the Contract names changed, the same two edits in both editions with natural Brazilian Portuguese, the excerpt rows at 70 columns (en) and 67, 69, 69 and 27 (pt), no em dash, en :94 / pt :96 limiting the container condition to the folder with the manual still reported "whatever the folder" in en :97 / pt :99 as SETUP step 4 says, "trunk, ADR-0010" faithful to the record's :18 and :76, and en :77 / pt :79 now pointing at an ADR the excerpt shows. No new queue line.

**Proof.** `make verify` was run after the chapter edits and again after this record was written with the page moved to `work/done/`: exit 0 each time, every check passed, the link check included. The greps for "gets a migration only when" and "recebe uma migração só quando" print nothing in chapter 8, and neither file has an em dash. This lane ran `make book` on the tree at HEAD `460add8` with this delivery's edits unstaged, before its commit `c90ef6b`, in the one tree it shared with `ch12-propose-worktree-path`, defined at `460add8` and running beside it; what of that lane's uncommitted chapter 12 the tree held is not recorded. Exit 0, both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. Nothing pushed; no environment changes.

```commit
docs(ch08-worktree-slot-manual): propose a folder only in a container

- ch08: a worktree slot naming no folder has one proposed only in a
  container; the manual is reported lacking whatever the folder
- ch08: the excerpt's Git item names ADR-0010 again
- both editions

work/done/ch08-worktree-slot-manual.md
```
