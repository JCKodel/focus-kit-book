# ch13-19-session-folder

**Objective.** After chapters 13 and 19 the reader who works with a worktree per delivery knows which folder to open the host in for each command and why: `/propose` in `main/`, `/apply` in a fresh session inside the delivery's worktree, whose path `/propose` gives, never in the container; that `/apply` opened anywhere else stops before any edit and gives that path; and that the container's manual lets `main/`'s session edit the worktrees, with Claude Code's `additionalDirectories` as the example.

**Behaviour.** What the reader can do or explain after the two chapters:

* Asked "do I open the session in `library/` or in `main/`?", answer from chapter 19: never in `library/`, the container, which is not a checkout and holds no `AGENTS.md`, no documents and no commands; `/propose` in `main/`; `/apply` in the delivery's worktree.
* After `/propose return-book` in `main/`, open the fresh session in `library/.focus-kit/worktrees/return-book`, the path `/propose` gave when it ended and the one `git worktree list` prints in `main/`, and type `/apply return-book` there (chapter 19, the lending library).
* Say why `/apply` opens there: the complete page and the line's `[>]` are on the delivery's branch, `main/`'s queue shows the line as it was until the merge, and the index it stages into is the worktree's own (chapter 19).
* Edge, the wrong folder: with a worktree per delivery, `/apply return-book` opened in `main/` edits nothing, leaves the mark as it is, does not mark the line `[?]`, and gives the worktree's path (chapter 13, beside the refusal of an incomplete page; chapter 19).
* Edge, the strategy: on trunk `/apply` runs in the folder where the session runs, and with a branch per delivery it works on the branch `/propose` created; the stop belongs to a worktree per delivery alone, and no new sentence says otherwise.
* Say what the container's manual adds: how the host lets a session in `main/`, where `/propose` runs and writes the page in the worktree, edit `<hidden>/worktrees/`; in Claude Code, `"permissions": {"additionalDirectories": ["../.focus-kit/worktrees"]}` in `main/`'s `.claude/settings.json`, which gives file access to the worktrees with the same rules as `main/` and loads none of the commands each worktree holds, as Claude Code's documentation says (footnote).
* Edge, the source: the footnote opens the Claude Code page and section the chapter quotes; the quote is the documentation's own words, translated in the Portuguese edition as chapter 12 does.
* Edge: no passage of either chapter names a version, a date, a run or the incident that led the kit to this rule.

**Contract.** Two chapters, the same changes in both editions, against the files as they are now (en and pt line numbers match in both chapters: 278 lines in chapter 13, 361 in chapter 19). One sentence per line, as the chapters are laid out. New lines shift the later ones; every cite below is the line as it is now. The pt slug of `return-book` is `devolver-livro`, and the container is `biblioteca/` (chapter 19 pt :138 to :142).

* `book/en/13-apply.md` and `book/pt/13-apply.md`:
  * New line after :18 ("It always starts in a fresh session..."):
    * en: "With a worktree per delivery, that fresh session opens in the delivery's worktree, the folder whose path `/propose` gives when it ends, because the page and the line's `[>]` are on the delivery's branch ([chapter 19](19-worktrees.md))."
    * pt: "Com um worktree por entrega, essa sessão nova abre no worktree da entrega, a pasta cujo caminho o `/propose` dá ao terminar, porque a página e o `[>]` da linha estão no branch da entrega ([capítulo 19](19-worktrees.md))."
  * New line after :31 ("That refusal comes before any build..."):
    * en: "So does a session opened, with a worktree per delivery, in any folder but the delivery's worktree, `main/` included: it refuses the same way, edits nothing, leaves the mark as it is, and gives the worktree's path, where you open the fresh session again."
    * pt: "O mesmo vale para uma sessão aberta, com um worktree por entrega, em qualquer pasta que não o worktree da entrega, `main/` incluída: ela recusa do mesmo jeito, não edita nada, deixa a marca como está, e dá o caminho do worktree, onde você abre a sessão nova de novo."
  * :272 (key point): en "builds the page in a fresh session," becomes "builds the page in a fresh session, opened in the delivery's worktree when there is one,"; pt "constrói a página em uma sessão nova," becomes "constrói a página em uma sessão nova, aberta no worktree da entrega quando há um,". The rest stays.
* `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`:
  * New line after :130 (`git worktree list` prints two lines):
    * en: "The container itself is not a checkout: it holds `main/` and `.focus-kit/`, but no `AGENTS.md`, no documents and no commands, so a session opened there has none of what the kit reads; every session opens in `main/` or in a worktree."
    * pt: "O próprio contêiner não é um checkout: ele guarda `main/` e `.focus-kit/`, mas nenhum `AGENTS.md`, nenhum documento e nenhum comando, então uma sessão aberta ali não tem nada do que o kit lê; toda sessão abre em `main/` ou em um worktree."
  * After :132 (the manual), a blank line, then a new line, a blank line, the block below, a blank line and a second new line:
    * en, first: "The same manual says how your host lets a session in `main/` edit the worktrees, since `/propose` runs there and writes the page in the delivery's worktree; in Claude Code it is one setting in `main/`'s `.claude/settings.json`, where `../.focus-kit/worktrees` is the worktrees' folder seen from `main/`:"
    * pt, first: "O mesmo manual diz como o seu host deixa uma sessão em `main/` editar os worktrees, já que o `/propose` roda ali e escreve a página no worktree da entrega; no Claude Code é uma configuração no `.claude/settings.json` de `main/`, onde `../.focus-kit/worktrees` é a pasta dos worktrees vista de `main/`:"
    * The block, the same in both editions, info string `json`:
      ```json
      {
        "permissions": {
          "additionalDirectories": ["../.focus-kit/worktrees"]
        }
      }
      ```
    * en, second: "It adds the worktrees to the folders the session reads and edits, under the same rules as `main/`, and loads none of the commands each worktree holds, which a session in `main/` already has: folders listed there \"*grant file access only*\".[^claude-code-permissions]"
    * pt, second: "Ela soma os worktrees às pastas que a sessão lê e edita, sob as mesmas regras de `main/`, e não carrega nenhum dos comandos que cada worktree guarda, que uma sessão em `main/` já tem: pastas listadas ali \"*concedem só acesso a arquivos*\".[^claude-code-permissions]"
  * :184, en: "`/apply <slug>` runs in a fresh session opened in that folder, builds the page, and stages the change." becomes "`/propose` ends by giving that folder's path, and `/apply <slug>` runs in a fresh session opened in it, builds the page, and stages the change."
  * :184, pt: "O `/apply <slug>` roda em uma sessão nova aberta naquela pasta, constrói a página, e coloca a mudança em stage." becomes "O `/propose` termina dando o caminho dessa pasta, e o `/apply <slug>` roda em uma sessão nova aberta nela, constrói a página, e coloca a mudança em stage."
  * Three new lines after :184, before "By default, you use the delivery...":
    * en: "On the lending library, after `/propose return-book` in `main/`, you open that session in `library/.focus-kit/worktrees/return-book`, the folder `git worktree list` prints too, and type `/apply return-book` there."
    * pt: "Na biblioteca, depois do `/propose devolver-livro` em `main/`, você abre essa sessão em `biblioteca/.focus-kit/worktrees/devolver-livro`, a pasta que o `git worktree list` também imprime, e digita `/apply devolver-livro` ali."
    * en: "It opens there because the page and the line's `[>]` are on the delivery's branch, while `main/`'s queue shows the line as it was until the merge, and the index it stages into is the worktree's own."
    * pt: "Ela abre ali porque a página e o `[>]` da linha estão no branch da entrega, enquanto a fila de `main/` mostra a linha como estava até o merge, e o índice em que ela coloca a mudança em stage é o do worktree."
    * en: "Opened in any other folder, `main/` included, `/apply` stops before any edit and gives the worktree's path ([chapter 13](13-apply.md))."
    * pt: "Aberto em qualquer outra pasta, `main/` incluída, o `/apply` para antes de qualquer edição e dá o caminho do worktree ([capítulo 13](13-apply.md))."
  * :198, en: "...one in each worktree for its `/apply`." becomes "...one in each worktree for its `/apply`, and none in the container."; pt: "...uma em cada worktree para o seu `/apply`." becomes "...uma em cada worktree para o seu `/apply`, e nenhuma no contêiner."
  * :350 (key point), after "the line's marks live on the branch until the merge;" (pt "as marcas da linha ficam no branch até o merge;"):
    * en inserts: " each session opens where it works, `/propose` in `main/`, which edits the worktrees by the container's manual, and `/apply` in a fresh session in the worktree whose path `/propose` gives, stopping before any edit anywhere else, never in the container;"
    * pt inserts: " cada sessão abre onde trabalha, o `/propose` em `main/`, que edita os worktrees pelo manual do contêiner, e o `/apply` em uma sessão nova no worktree cujo caminho o `/propose` dá, parando antes de qualquer edição em qualquer outro lugar, nunca no contêiner;"
  * New footnote after :361, the last:
    * en: "[^claude-code-permissions]: Anthropic, \"Configure permissions\", Claude Code documentation, section \"Additional directories grant file access, not configuration\", accessed 2026-10-21. <https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration>"
    * pt: "[^claude-code-permissions]: Anthropic, \"Configure permissions\", documentação do Claude Code, seção \"Additional directories grant file access, not configuration\", acesso em 2026-10-21. <https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration>"
    * The quoted words are the section's: "Directories listed in `permissions.additionalDirectories` in a settings file grant file access only and don't load any of the configuration below", the configuration being skills, command files and subagents; the same page says files in additional directories "follow the same permission rules as the original working directory". /apply reads the page again on the day it builds and writes that day's date if it differs; if the page no longer says it, /apply stops and says so.
* Terms of docs/03: worktree (:94), container folder (:95), bare repository (:96), manual (:119), index (:77). No new term and no row changed: "where each session opens" is a rule of the kit, not a term, and "the container's manual" is a `manual` of a `container folder`, as `work/done/kit-2026-10-20-2.md` reasoned.
* Sources: the installed skills at 2026.10.20.2, `.claude/skills/propose/SKILL.md` (its last sentence: "opened in the delivery's worktree, if any, its path written out"), `.claude/skills/apply/SKILL.md` ("with a worktree, only in a session opened in it: elsewhere, stop before any edit and give its path") and `.claude/skills/brainstorm/references/documents.md` :158 to :160 ("`/apply` runs in a session opened in it, never in `main/`; the container's manual lets a session in `main/` edit `<hidden>/worktrees/`"); focus-kit's `CHANGELOG.md` at `da29c25`, entry 2026.10.20.2, for the Claude Code setting; chapter 19 :180 (the marks on the branch) and :89 (each worktree's own index); Claude Code's permissions page, the one footnote.
* Cases: none. No number.
* Neighbouring lines on the same files: `ch08-update-2026-10-20-2` (M26, in flight) touches chapter 8 only, no file of this delivery. Later in queue order, finding these sentences as this delivery leaves them: M27's `ch12-14-18-several-slugs` (chapter 13) and M28's `ch13-19-claim-script` (chapters 13 and 19).

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 10, the quick guide: its steps assume trunk (:36), where no worktree exists and `/propose` gives no path.
* Chapter 8: not this line's; its :143 to :145, on what `/propose` names at its end, use the trunk example `lend-book`, and chapter 8 belongs to `ch08-update-2026-10-20-2`.
* Chapter 12 :32 and :172: :32 ends the trunk `lend-book` example, where there is no path to give, and :172 says where `/propose` starts, not what it says last; chapter 19 now says that `/propose` ends with the path.
* docs/03: no row, as the Contract says.
* The Claude Code setting in this repository: the book is on trunk and has no container (ADR-0010, `work/done/kit-2026-10-20-2.md`).
* Other hosts' ways to widen a session's folders: the kit names Claude Code's alone, and the manual is the project's to write for its host.
* The incident the kit's changelog tells: a before and after of a kit change, which the book does not tell.

**Decisions from the documents.**

* `/propose` in `main/`, `/apply` in the worktree, never in `main/`, the stop elsewhere and the container's manual: the installed propose and apply skills and the Choices' worktree bullet at 2026.10.20.2, word for word as the Sources quote them.
* The stop is scoped to a worktree per delivery: the apply skill says "with a worktree", and chapter 13 :28 already separates trunk, branch and worktree.
* The stop is placed beside the refusal of an incomplete page in chapter 13 (:30 and :31): like it, it comes before any edit, so nothing is built and the line is not marked `[?]`.
* The setting is the kit's own example, `"permissions": {"additionalDirectories": ["../<hidden>/worktrees"]}` in `.claude/settings.json`, written with the chapter's default `.focus-kit/` (chapter 19 :177).
* Taught as the kit is today, with no version, date or "now" (AGENTS.md, the M21 rule).
* No docs/03 row: `work/done/kit-2026-10-20-2.md`'s reasoning.

**Decisions taken alone.** The agent chose each of these.

* The open question, chapter 10 or chapter 8: neither. Chapter 10 assumes trunk, and chapter 8 is another line's; the reply to the driver notes chapter 8 :143 to :145 in case `ch08-update-2026-10-20-2` wants them.
* Chapter 12 stays out, though its :32 says how `/propose` ends: chapter 19 holds the path, and M27's `ch12-14-18-several-slugs` edits chapter 12 next; the queue line keeps its wording.
* The reason for opening in the worktree is given as mechanism (the page and `[>]` on the branch, the worktree's own index), not as the changelog's incident: the book teaches a kit change as it is today, with no before and after.
* The footnote quotes the sentence that tells the settings key from `/add-dir`: the reader gains why the kit names the setting, since a folder added with `/add-dir` would load each worktree's copy of the commands, and has a page to open.
* "Never in the container" is said once where the container is laid out (:130), once beside the sessions per folder (:198) and in the key point, not in chapter 13, which does not lay out the container.
* The path `../.focus-kit/worktrees` is called "the worktrees' folder seen from `main/`", not "relative to `main/`": Claude Code's page does not say how a relative entry of `additionalDirectories` resolves, and the kit's example is written from `main/`.
* Token `(PA)`: every line above is `[x]` but `ch08-update-2026-10-20-2`, whose page this definition reads nothing from and whose file, chapter 8, this build does not touch; the `after` on `kit-2026-10-20-2`, `[x]`, holds for both commands.

**Done when.**

* [x] Both editions changed as the Contract says, and nothing else in the two chapters.
* [x] `grep -n "additionalDirectories" book/*/19-worktrees.md` prints one line per edition, in the block after :132's manual.
* [x] `grep -n "claude-code-permissions" book/*/19-worktrees.md` prints the use and the footnote in each edition, the footnote's page read on the day of the build.
* [x] `grep -n "contêiner\|container" book/*/13-apply.md` prints nothing new: chapter 13 does not lay out the container.
* [x] Each chapter still opens with its value, no filler and nothing useful cut, no number added, no em dash, no run narration, no version or date in chapter text.
* [x] `make verify` green.
* [x] `make book`: left to the driver after the batch; the milestone review records the build.
* [x] Delivery review by one read-only Opus agent, with the advisor, over this page and `git diff HEAD` of the four chapter files, against docs/04 and AGENTS.md.
* [x] Page moved to `work/done/`, covered by the last verify.

**Divergences.**

* Two sentences differ from the Contract's wording, after the delivery review: chapter 13 en's new line after :31 opens "The same holds for a session opened..." instead of "So does a session opened...", whose "So does" took the verb of "That refusal comes before any build" and read as the session coming before any build; the pt line, "O mesmo vale para...", already read so. In chapter 19's key point, both editions, "never in the container" ("nunca no contêiner") moved up beside "each session opens where it works", where it says that no session opens there, instead of following the stop.
* `make book`: the Done when item leaves it to the driver; the batch's rules had this lane run it after the last verify, and the Proof records it.
* The delivery review: the Done when item says "with the advisor"; it was one read-only Opus agent launched by this lane, and nothing shows it kept the session's advisor.
* New lines land where the Contract puts them; with them, chapter 13 has 280 lines and chapter 19 has 378 in both editions.

**Decisions taken alone in /apply.**

* The footnote's page was read on the day of the build, 2026-10-21, the date the Contract wrote: the section "Additional directories grant file access, not configuration" still says "Directories listed in `permissions.additionalDirectories` in a settings file grant file access only and don't load any of the configuration below", the configuration listing skills, command files and subagents, and its "Working directories" section says files in additional directories "follow the same permission rules as the original working directory". The anchor `#additional-directories-grant-file-access-not-configuration` is on the page.
* Both review findings were in text this delivery wrote, so both were fixed here rather than queued.

**Delivery review.** One read-only Opus agent, launched by this lane, read this page, `git diff HEAD` of `book/en/13-apply.md`, `book/pt/13-apply.md`, `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`, docs/04, AGENTS.md and docs/03, the installed propose and apply skills, and Claude Code's permissions page. It found the diff the Contract's line for line in both editions and nothing else changed, parity and the Portuguese slugs right, no em dash, no version, date, run or incident in chapter text, the stop scoped to a worktree per delivery, the quote the documentation's words, both claims about Claude Code on the page, and the footnote in docs/04's format. Findings and answers:

* `book/en/13-apply.md:31`: "So does" took the verb of the sentence before it, so read literally the session "comes before any build"; suggested "The same holds for a session opened...". Fixed.
* `book/en/19-worktrees.md:366` and `book/pt/19-worktrees.md:366`, the key point: "never in the container" after the stop could read as "it never stops in the container"; suggested moving it beside "opens". Fixed in both editions.
* An observation needing no fix: "same rules as `main/`" comes from the page's "Working directories" section, not the section the footnote names; one note per source opens the same page.

No new queue line.

**Proof.** `make verify` was run after the chapter edits, after the review's fixes with the page moved to `work/done/`, and again after this Proof was written: exit 0 each time, every check passed, the link check included. The Done when greps print one `additionalDirectories` line per edition (19 :140, in the block after the manual), the footnote's use (:145) and definition (:378) in each edition, and no new `container` or `contêiner` line in chapter 13. This lane ran `make book` after the second verify, exit 0, both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. Nothing pushed; no environment changes.

```commit
docs(ch13-19-session-folder): teach which folder each session opens in

- ch13: with a worktree, /apply opens in it; elsewhere it stops, no edit
- ch19: the container holds no kit; /propose gives the worktree's path
- ch19: Claude Code's additionalDirectories lets main/ edit worktrees
- both editions; footnote to Claude Code's permissions page

work/done/ch13-19-session-folder.md
```
