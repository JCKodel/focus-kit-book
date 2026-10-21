# ch13-19-claim-script

**Objective.** After chapters 13 and 19 the reader knows how `/propose` claims its line: it runs the kit's claim script, `propose/scripts/claim.sh`, as one git command that git runs through its own `sh` from the repository's top on every host and terminal, Git for Windows' shell on Windows, with WSL still the recommended place to develop; the script checks the repository, the branch and the remote, refuses outside `main/` or off the default branch, creates or reuses the branch or worktree, pushes the branch, the line's claim, edits no document, and prints the path `/apply`'s session opens in.

**Behaviour.** What the reader can do or explain afterwards:

* Asked "how does `/propose` claim a line?", answer from chapter 13: it runs `git -c "alias.fk=!sh .agents/skills/propose/scripts/claim.sh" fk <slug> <strategy>`, the strategy being the Git slot's word, `trunk`, `branch` or `worktree` with the hidden folder and the prefix; the script edits no document, and the line's `[~]` stays `/propose`'s first edit.
* Say why the line goes through git: an alias starting with `!` is run by git's shell from the repository's top level (git's documentation, quoted), so the same line works from any folder of the checkout, in bash, zsh, PowerShell or cmd; it names `.agents/skills/` because the kit installs the script there as well as in `.claude/skills/`.
* A reader on Windows without WSL: the script runs through the `sh` Git for Windows installs, the installer's default, from PowerShell or cmd; WSL stays the kit's strong recommendation; when git cannot find `sh`, `/propose` says Git for Windows was installed without its shell and stops.
* On trunk: the script creates, fetches and pushes nothing and prints the session's folder; with a branch per delivery it switches to the slug's branch, creating and pushing it (chapter 18).
* With a worktree per delivery (chapter 19): say what the script refuses (outside a repository, detached `HEAD`, a slug a branch name cannot hold, no `origin`, a failed `git fetch`, a branch but the default one, a worktree or a delivery branch), what it only notes (`main` behind the remote; an unprefixed `<slug>` branch on the remote), what it creates or reuses and pushes, including a branch that never reached the remote, and that a failed push leaves the line unclaimed.
* Read the script's output for `return-book` / `devolver-livro`: `claim`, `branch`, `path`, `draft`; `path` is where `/apply` opens, `draft` a draft page `main/` holds for the slug, which `/propose` brings into the delivery.
* Chapter 8's "(chapter 13)" pointer, written by `ch08-update-2026-10-20-4`, lands on the passage that says how the script runs on Windows.
* Edge: chapter 19's exception to "the agent never pushes" covers the push of a resumed branch the remote lacks, and its key point says the script claims.
* Edge: no version, date, run, commit hash or before/after of the kit's change in chapter text (the kit's changelog stories stay out); nothing implies Case B ran on the process; no em dash.
* Fails: a passage implying the script decides whether a line is taken (it reports `existing`; `/propose` read the claim before, chapter 12 :28); a second copy of the alias line in chapter 19; the WSL recommendation pointed to chapter 8, which states only the requirement.

**Contract.** Two chapters and docs/03, the same changes in both editions, against the files as they are now (en/pt: chapter 13, 283/283 lines; chapter 19, 377/377); one sentence per line, as the chapters are laid out; anchors are quoted clauses, since lines move. Code examples are the script's own command and an output written for chapter 19 on the lending library, said so; the fenced block stays under 74 columns (docs/04, "Width of a block"); the alias line is inline, in prose.

* `book/en/13-apply.md` and `book/pt/13-apply.md`, "What `/apply` does":
  * New paragraph after the line "With several slugs and a worktree per delivery, you type `/apply a b` in a session in `main/` ..." (en :21) / "Com vários slugs e um worktree por entrega, ..." (pt :21), a blank line before it, six lines:
    * en:
      1. "The worktree's path `/propose` gives is the one the kit's claim script printed, `propose/scripts/claim.sh`, which `/propose` runs to claim its line before it writes the page, with the slug and the word of the project's Git slot, and which edits no document: the line's `[~]` stays `/propose`'s first edit."
      2. "The agent runs it as one line, `git -c "alias.fk=!sh .agents/skills/propose/scripts/claim.sh" fk <slug> <strategy>`, the strategy being `trunk`, `branch` or `worktree` with the hidden folder and the branch prefix."
      3. "`git -c` sets an alias named `fk` for that one command, and git runs an alias that starts with `!` through its own shell, `sh`, from the top of the repository: \"*Shell commands will be executed from the top-level directory of a repository*\", says git's documentation.[^git-config]"
      4. "So the line is the same from any folder of the checkout, in bash, zsh, PowerShell or cmd, on every host, and it names `.agents/skills/` because the kit installs the script there as well as in `.claude/skills/`, so the path exists on every host."
      5. "On Windows that `sh` is the one Git for Windows installs with git, the installer's default, so the script runs from PowerShell or cmd without WSL, though developing inside WSL is still the kit's strong recommendation, and the kit works the same there; when git cannot find `sh`, Git for Windows was installed without its shell, and `/propose` says so and stops."
      6. "On trunk the script creates, fetches and pushes nothing and prints the folder where the session runs; with a branch per delivery it switches to the slug's branch, creating and pushing it ([chapter 18](18-git-essentials.md)); with a worktree per delivery it creates or reuses the worktree and pushes its branch, and the `path` it prints is that worktree's ([chapter 19](19-worktrees.md))."
    * pt:
      1. "O caminho do worktree que o `/propose` dá é o que o script de reivindicação do kit imprimiu, `propose/scripts/claim.sh`, que o `/propose` roda para reivindicar a sua linha antes de escrever a página, com o slug e a palavra do slot Git do projeto, e que não edita nenhum documento: o `[~]` da linha continua sendo a primeira edição do `/propose`."
      2. "O agente o roda em uma linha só, `git -c "alias.fk=!sh .agents/skills/propose/scripts/claim.sh" fk <slug> <estratégia>`, a estratégia sendo `trunk`, `branch` ou `worktree` com a pasta oculta e o prefixo do branch."
      3. "O `git -c` define um alias chamado `fk` só para esse comando, e o git roda um alias que começa com `!` pelo seu próprio shell, o `sh`, a partir do topo do repositório: \"*Comandos de shell serão executados a partir do diretório de nível mais alto de um repositório*\", diz a documentação do git.[^git-config]"
      4. "Então a linha é a mesma de qualquer pasta do checkout, no bash, no zsh, no PowerShell ou no cmd, em todo host, e nomeia `.agents/skills/` porque o kit instala o script ali e também em `.claude/skills/`, então o caminho existe em todo host."
      5. "No Windows esse `sh` é o que o Git for Windows instala junto com o git, o padrão do instalador, então o script roda do PowerShell ou do cmd sem WSL, embora desenvolver dentro do WSL continue sendo a forte recomendação do kit, que funciona igual ali; quando o git não encontra o `sh`, o Git for Windows foi instalado sem o seu shell, e o `/propose` diz isso e para."
      6. "No trunk o script não cria, não busca e não dá push em nada e imprime a pasta onde a sessão roda; com um branch por entrega ele troca para o branch do slug, criando-o e dando push nele ([capítulo 18](18-git-essentials.md)); com um worktree por entrega ele cria ou reaproveita o worktree e dá push no seu branch, e o `path` que ele imprime é o desse worktree ([capítulo 19](19-worktrees.md))."
  * New footnote after `[^huang-2024]` (en/pt :283), the date the day /apply opens the page and checks the quote, which the local `man git-config` (variable `alias.*`) gives word for word:
    * en: "[^git-config]: Git, \"git-config\", the documentation, variable `alias.*`, accessed <date>. <https://git-scm.com/docs/git-config>"
    * pt: "[^git-config]: Git, \"git-config\", a documentação, variável `alias.*`, acesso em <date>. <https://git-scm.com/docs/git-config>"
  * Nothing else in the chapter changes; :19 ("the folder whose path `/propose` gives when it ends") and the key point at :277 stay true and lead into the new paragraph.
* `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`, "Worktrees in the kit":
  * New block after the line "By default, you use the delivery, review and commit on the branch, ..." (en :201) / "Por padrão, você usa a entrega, ..." (pt :201), a blank line before it, the existing blank line after it:
    * en:
      1. "The check of the remote, the worktree, its branch and the push are one script, the kit's claim script, which `/propose` runs as [chapter 13](13-apply.md) shows, with `worktree .focus-kit focus-kit/`, or the hidden folder and prefix the slot names."
      2. "Before it changes anything the script refuses, printing `error:` with the reason and exiting with 2 instead of 0: outside a repository, on a detached `HEAD`, for a slug a branch name cannot hold, without a remote `origin`, when `git fetch` fails, and on any branch but the default one."
      3. "It refuses as well in a worktree or on a delivery branch: it runs from `main/`, as `/propose` does."
      4. "Without stopping, it notes when `main` is behind the remote, the delivery starting from the local `HEAD` all the same, and when a branch `return-book` without the prefix is on the remote, which is not the delivery's."
      5. "When the worktree exists but its branch never reached the remote, it pushes the branch then, and when a push fails it says the line is not claimed."
      6. "It prints a few `key: value` lines, here for `return-book`, new, in an example written for this chapter:"
      7. A blank line, then the fenced block (no info string, as the chapter's other git blocks), then a blank line:
         ```
         claim: new
         branch: focus-kit/return-book, on origin
         path: /projects/library/.focus-kit/worktrees/return-book
         draft: none
         ```
      8. "`claim` is `new`, `existing` when the worktree or its branch was already there, or `existing, branch pushed now`; `path` is the folder `/apply`'s session opens in; and `draft` is `none` or names a draft page `main/` holds for the slug, which `/propose` brings into the delivery."
    * pt:
      1. "A consulta ao remoto, o worktree, o seu branch e o push são um script só, o script de reivindicação do kit, que o `/propose` roda como o [capítulo 13](13-apply.md) mostra, com `worktree .focus-kit focus-kit/`, ou a pasta oculta e o prefixo que o slot nomeia."
      2. "Antes de mudar qualquer coisa o script recusa, imprimindo `error:` com o motivo e saindo com 2 em vez de 0: fora de um repositório, com o `HEAD` destacado, para um slug com um caractere que um nome de branch não aceita, sem um remoto `origin`, quando o `git fetch` falha, e em qualquer branch que não seja o padrão."
      3. "Ele recusa também em um worktree ou em um branch de entrega: roda a partir de `main/`, como o `/propose`."
      4. "Sem parar, ele avisa quando o `main` está atrás do remoto, a entrega partindo do `HEAD` local mesmo assim, e quando um branch `devolver-livro` sem o prefixo está no remoto, que não é o da entrega."
      5. "Quando o worktree existe mas o seu branch nunca chegou ao remoto, ele dá push no branch então, e quando um push falha ele diz que a linha não foi reivindicada."
      6. "Ele imprime algumas linhas `chave: valor`, aqui para `devolver-livro`, nova, em um exemplo escrito para este capítulo:"
      7. The fenced block, as in en (the script prints English keys):
         ```
         claim: new
         branch: focus-kit/devolver-livro, on origin
         path: /projetos/biblioteca/.focus-kit/worktrees/devolver-livro
         draft: none
         ```
      8. "O `claim` é `new`, `existing` quando o worktree ou o seu branch já estava lá, ou `existing, branch pushed now`; o `path` é a pasta em que a sessão do `/apply` abre; e o `draft` é `none` ou nomeia um rascunho da página que `main/` guarda para o slug, que o `/propose` traz para a entrega."
  * en :210: "apart from the branch `/propose` pushes when it creates it, the line's claim:" becomes "apart from the branch `/propose` pushes when it creates it or finds it missing from the remote, the line's claim:"; pt :210: "fora o branch em que o `/propose` dá push quando o cria, a reivindicação da linha:" becomes "fora o branch em que o `/propose` dá push quando o cria ou não o encontra no remoto, a reivindicação da linha:"; the rest stays.
  * Key point en :365: "`/propose` pushes the branch when it creates it, the line's claim," becomes "`/propose` claims the line with the kit's script, run as a git alias through git's own `sh`, Git for Windows' on Windows, which refuses outside `main/` and off the default branch, pushes the branch when it creates it or the remote lacks it, the line's claim, and prints the worktree's path,"; pt :365: "o `/propose` dá push no branch quando o cria, a reivindicação da linha," becomes "o `/propose` reivindica a linha com o script do kit, rodado como um alias do git pelo próprio `sh` do git, o do Git for Windows no Windows, que recusa fora de `main/` e fora do branch padrão, dá push no branch quando o cria ou quando o remoto não o tem, a reivindicação da linha, e imprime o caminho do worktree,"; the rest stays.
  * Nothing else in the chapter changes; :192 ("checks the remote for `<prefix>/<slug>` ... from the main branch's `HEAD` ... pushes the branch at once") is what the script does, the local `HEAD` included, and stays.
* `docs/03-Domain.md` :117, the row `claim`, replaced by this exact row (the code column gains the script and the full ref name the script checks, since `ls-remote` matches a pattern against the tail of a ref; the definition gains the script and the push on resume):

  ```
  | claim | reivindicação | `propose/scripts/claim.sh`; `git ls-remote --exit-code --heads origin refs/heads/<prefix>/<slug>` | With a branch or a worktree per delivery, the delivery's branch on the remote, which /propose pushes the moment it creates it, or when it resumes on a branch the remote lacks, the remote checked for one first, both by the kit's claim script, which /propose runs through git's own shell: after `git fetch`, a line whose branch exists is taken, whatever the main branch's queue shows, so that queue changes only through merges; on trunk no branch is created, the script creating, fetching and pushing nothing, and a line is taken by its mark in the one working tree (docs/05 §§2, 4, 5). |
  ```

* Terms: "claim script" / "script de reivindicação" is the row above, no new row. Sources: one new note, git-config, which the reader can open. Cases: none.
* Neighbouring lines: `ch08-update-2026-10-20-4` (M28, in flight) touches chapter 8 only and points its Windows sentence to chapter 13, which the new paragraph answers; `ch08-copilot-cli` touched chapter 8 only as its line read at this page's define commit `ed47eda`; at `f84d8d9`, this /apply's HEAD, the line named chapters 8 and 10 with `(P-)`, and its page edits docs/03's host row, another row of a file this page edits, its `(P-)` keeping its /apply until this line is `[x]`. No line in flight at `ed47eda` touched chapters 13 or 19 or docs/03.

**Out of scope.**

* Chapter 8, the Windows requirement and its pointer: `ch08-update-2026-10-20-4`'s; the Copilot CLI: `ch08-copilot-cli`'s.
* Chapter 12 :28 to :31 and its key point :191, and chapter 18 :25: they say what the claim does (remote checked, branch created and pushed at once, reused on resume, draft brought in, `[~]` the first edit, the worktree's path given at the end), all of which the script does; none goes stale, so none is a sibling sentence to widen to.
* The notation `<prefix>/<slug>` (chapter 19 :192 and :365, docs/03 :96 and :117), while the slot's prefix and the script's argument carry their own slash (`focus-kit/`): it is the kit's own notation (SETUP.md at `ffbec72` :641, the text it installs as `documents.md`), kept so the book reads as the kit; a kit note is the person's to add to `work/kit-proposals.md`.
* The kit's changelog stories (the laptop proof, `core.autocrlf`, the delivery found `[*]` in its worktree): the book teaches the kit as it is today, with no before/after.
* Codex's sandbox prompt on `.agents/` (the README): not this line's.
* Chapter 13's key point (en/pt :277): it is about `/apply`, "opened in the delivery's worktree when there is one" stays true, and the claim is `/propose`'s step; the script's key point is chapter 19's.

**Decisions from the documents.**

* The command, the strategy words, the `sh` stop: the installed propose skill (`.claude/skills/propose/SKILL.md`, its claim paragraph).
* What the script checks, refuses, notes, creates, pushes and prints, and that it edits no document: `.claude/skills/propose/scripts/claim.sh` as installed by `kit-2026-10-20-4`.
* Git for Windows' shell, the installer's default, from PowerShell or cmd without WSL, WSL "still strongly recommended, and the kit works the same there": README.md at `ffbec72` :37-40.
* Git runs a `!` alias through a shell from the top-level directory: git-config, `alias.*`, quoted.
* Taught as the kit is today, with no version, date or run (AGENTS.md; docs/04).

**Decisions taken alone.** The agent chose each of these.

* Placement: the general teaching (the alias line, why through git, Windows and WSL, the three slots) in chapter 13 beside :19's "the folder whose path `/propose` gives", since the queue line names chapters 13 and 19 and `ch08-update-2026-10-20-4`'s page points chapter 8's Windows sentence to chapter 13; the worktree specifics (refusals, notes, resume push, output) in chapter 19's kit section; the alias line written once, in chapter 13.
* Chapter 12 left unchanged: no sentence there goes stale (Out of scope); widening to it would move the teaching away from where the queue line and chapter 8 send the reader.
* The WSL recommendation is this line's, not chapter 8's, as `ch08-update-2026-10-20-4`'s page decided; chapter 13 states it with no pointer to chapter 8.
* Chapter 19 :210 and the key point :365: sibling sentences in this line's chapter that the script's push of a resumed branch makes incomplete ("pushes when it creates it"); widened, no other line owns them.
* docs/03's `claim` row amended rather than a new row for the script, so the chapters' "claim script" uses an existing term; the code column gains `refs/heads/` because the script gives the full name for the reason its comment states.
* The `<prefix>/<slug>` notation kept as the kit writes it (Out of scope).
* The output example's path `/projects/library/...` / `/projetos/biblioteca/...`: absolute, as the script prints, with no user name.
* One source note, git-config, in chapter 13 where the quote sits; chapter 19 cites none new.
* Queue line: no wording change; it already names what the page teaches.
* Token `(PA)`: the `after`, `kit-2026-10-20-4`, is `[x]`; the two other lines in flight or open, `ch08-update-2026-10-20-4` and `ch08-copilot-cli`, touched chapter 8 only at `ed47eda`, none of this page's files (`ch08-copilot-cli`, widened at `f84d8d9`, also edits docs/03's host row, its `(P-)` keeping its /apply until this line is `[x]`), and this page takes nothing from their pages but chapter 8's pointer, which holds whatever order they build in; `m28-review` waits by its `after`.

**Done when.**

* [x] Both editions changed as the Contract says in chapters 13 and 19, with the four wordings of Divergences, and docs/03's row replaced, nothing else in them.
* [x] `grep -n` finds, in both editions: chapter 13 "claim.sh" (en/pt), "WSL", "[^git-config]" twice (call and note); chapter 19 "claim: new", "existing, branch pushed now", "finds it missing from the remote" / "não o encontra no remoto", "claims the line with the kit's script" / "reivindica a linha com o script do kit".
* [x] `grep -c "alias.fk" book/*/19-worktrees.md` prints 0 for each edition (the alias line lives in chapter 13).
* [x] The git-config quote checked against <https://git-scm.com/docs/git-config>, `alias.*`, the day the note is dated.
* [x] Every statement about the script checked against `.claude/skills/propose/scripts/claim.sh`; the Windows sentence against README.md at `ffbec72` (`git -C ~/Projects/focus-kit show ffbec72:README.md`).
* [x] Each chapter still opens with its value, no filler and nothing useful cut, no number added, no em dash, no run narration, no version, date or commit hash in chapter text, nothing implying Case B ran on the process.
* [x] `make verify` green (the width check over chapter 19's new block included).
* [x] `make book` run, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent (Explore type), launched by this /apply, over this page and `git diff HEAD` of the five files, asked to read them against docs/04, docs/05 §§2 and 3, `AGENTS.md`, the propose skill and `claim.sh` (Delivery review): its reply shows docs/04's width rule, the propose skill and `claim.sh` read, and does not say whether it opened `AGENTS.md` or docs/05; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.
* [x] Page moved to `work/done/`, covered by the last verify.

**Divergences.** Four of the delivery review's findings changed the Contract's wording in both editions; the rest of the Contract is as written. One Done when item was reworded in /apply from its `ed47eda` text: the first gained "with the four wordings of Divergences". `m28-records-claims` gave the review item the paragraph's words. The neighbouring line `ch08-copilot-cli` widened at `f84d8d9`, before this page's commit, to chapter 10, its page editing docs/03's host row, its `(P-)` keeping its build after this line; `m28-records-claims` put the Contract's bullet and the token's reason in the past.

* Chapter 13, sentence 4: the first "on every host" / "em todo host" dropped, so "every host" says once what it means, the agent's hosts, beside the path it explains.
* Chapter 13, sentence 6: "creating and pushing it" / "criando-o e dando push nele" became "creating or reusing it and pushing it when the remote lacks it" / "criando-o ou reaproveitando-o e dando push nele quando o remoto não o tem", since `claim.sh` also reuses a branch already on the remote and pushes a local one the remote lacks.
* Chapter 19, sentence 2: the refusals gain "when it cannot tell the default branch" / "quando não consegue saber qual é o branch padrão", the script's own refusal before the default-branch check; the usage and unknown-strategy refusals stay out, since `/propose` never makes them.
* Chapter 19, key point: "run as a git alias ..., which refuses" became "which runs as a git alias ..., refuses" / "que roda como um alias ..., recusa", so "which" names the script and not Git for Windows' `sh`.

**Decisions.** The footnote is dated 2026-10-21, the day the quote was checked, in the format of chapter 18's `[^git-commit]`.

**Proof.**

* The git-config quote, word for word in the local `man git-config` (`alias.*`) and at <https://git-scm.com/docs/git-config>, fetched 2026-10-21: "Shell commands will be executed from the top-level directory of a repository, which may not necessarily be the current directory."
* Against `.claude/skills/propose/scripts/claim.sh`: the refusals (`die`, exit 2, `error:`) for a slug, a repository, a detached `HEAD`, a worktree or a delivery branch, `origin`, `git fetch`, the default branch; the two notes; the pushes of a new branch and of an existing one the remote lacks, each failing with "the line is not claimed"; trunk printing `claim: none, trunk` with no fetch or push; the output keys `claim`, `branch`, `path`, `draft`, and the worktree path `dirname(top)/<hidden>/worktrees/<slug>`; "Edits no document" in its header.
* The command, the strategy words and the `sh` stop against `.claude/skills/propose/SKILL.md`'s claim paragraph; the Windows sentence against README.md at `ffbec72` :37-40.
* Chapter 8's "(chapter 13)" / "(capítulo 13)" at en/pt :24 lands on chapter 13's Windows sentence, en/pt :27.
* `make verify` exit 0 after the review's fixes and the page's move, every check passed, the external link included; `make book` exit 0, on HEAD `f84d8d9` with this delivery's changes in the tree: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* Done when greps: chapter 13 "claim.sh" 2, "WSL" 1, "[^git-config]" 2 in each edition; chapter 19 "claim: new" 1, "existing, branch pushed now" 1, the :210 and key point wordings 1 each, "alias.fk" 0, in each edition; no em dash; en and pt at 291 and 393 lines.

**Delivery review.** One read-only Opus agent (Explore type), launched by this /apply over this page and `git diff HEAD` of the five files, with docs/03 only the `claim` row, asked to read them against docs/04, docs/05 §§2 and 3, `AGENTS.md`, the propose skill, `claim.sh`, README.md at `ffbec72` :37-40 and `man git-config`. Its reply shows it read the page's Contract, the five files' diff, docs/04's width rule, the propose skill's :26-27, `claim.sh`, README.md at `ffbec72` :37-40 and `man git-config`; it did not say whether it opened `AGENTS.md` or docs/05; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none. Its reply, in short: the text matched the Contract word for word in both editions, nothing else in the five files changed, line counts equal; no em dash, the only date in the footnote, no Case B; `alias.fk` 0 in chapter 19, `[^git-config]` 2 in each chapter 13; the block's longest line 62 columns; the quote, the Windows sentence and the `sh` stop matching their sources; every refusal, note, push and key holding against `claim.sh`. Findings: (1) chapter 13 :28, "creating and pushing it" says the script always creates the branch, while it also reuses one and pushes a local-only one; (2) chapter 19 :381, "which refuses" reads as referring to Git for Windows' `sh`; (3) chapter 13 :26, "on every host" twice; (4) chapter 19 :204, the refusal list leaves out "cannot tell the default branch"; (5) outside this delivery: in `claim.sh` :78-80, with a worktree per delivery, a branch that exists locally but not on the remote, with no worktree folder, makes `git worktree add -b` fail under `set -e` with git's own error, without `error:` or exit 2. Findings 1 to 4 fixed in both editions (Divergences); finding 5 is the kit's, a note for the person to add to `work/kit-proposals.md`, and the chapter's text stays true since that case is not among the refusals it lists.

```commit
docs(ch13-19-claim-script): teach the claim script in chapters 13 and 19

- chapter 13: how /propose runs the claim script through git's sh
- chapter 13: Windows runs it with Git for Windows' shell, WSL advised
- chapter 19: what the script refuses, notes, pushes and prints
- docs/03: the claim row names the script and the full ref

work/done/ch13-19-claim-script.md
```
