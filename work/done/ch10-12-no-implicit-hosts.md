# ch10-12-no-implicit-hosts

**Objective.** After chapters 10 and 12 the reader knows every host that chapter 8 says keeps a matching message from starting a command, Claude Code, the GitHub Copilot CLI and Codex, so neither chapter reads as if one or two hosts were the only ones.

**Behaviour.**

* Given chapter 10's "Before you start", the reader finds the sentence after the table naming the three hosts: in Claude Code, the GitHub Copilot CLI and Codex a command runs only when you name it, and a message that happens to match what it does starts nothing (finding C8).
* Given chapter 12's "Several lines in one command", the reader finds that the commands keep chapter 8's settings that stop a host from running a skill on its own: `disable-model-invocation` in Claude Code and the Copilot CLI, and the file beside each skill in Codex (finding C9).
* The reader finds the next sentence speaking of lifting one of those settings, not of one setting, and chapter 12's summary bullet naming both, so the section and its summary agree.
* The claims match chapter 8: Claude Code's skills carry `disable-model-invocation: true`, "The Copilot CLI honours the same field" (en 08 :133-134, pt 08 :135-136), and Codex's "small file beside each skill turns that off" (en 08 :132, pt 08 :134); neither chapter adds a source note, as chapter 8 holds the sources.
* Edge: Codex's mechanism is a file, not the field; no sentence says Codex honours `disable-model-invocation`.
* Edge: Copilot in VS Code and the other hosts are not named: chapter 8 does not say they enforce it, and "On the other hosts, invoke the commands yourself" (en 08 :135) still covers them.
* Edge: the hosts' names follow each place: "the GitHub Copilot CLI" in chapter 10, as its table row two lines above; "the Copilot CLI" in chapter 12, as chapter 8's short form.
* Fails: any other line of chapters 10 or 12 changed; a host named that chapter 8 does not say enforces it; Codex said to honour the field; a source note; an em dash; a commit hash; one edition changed without the other. /apply removes it before verify.

**Contract.** Both editions, same change; English is the source (ADR-0004). Line numbers as the files are now (HEAD `93a44e6`); chapter 8's, cited for the claims, may shift when `ch08-update-choice-outcome` lands, so /apply finds them by the sentence.

`book/en/10-quick-guide.md`, "Before you start", en :33:

* "In Claude Code and the GitHub Copilot CLI a command runs only when you name it: a message that happens to match what it does starts nothing." becomes

  "In Claude Code, the GitHub Copilot CLI and Codex a command runs only when you name it: a message that happens to match what it does starts nothing."

`book/pt/10-quick-guide.md`, "Antes de começar", pt :33:

* "No Claude Code e no GitHub Copilot CLI um comando só roda quando você o nomeia: uma mensagem que por acaso bate com o que ele faz não inicia nada." becomes

  "No Claude Code, no GitHub Copilot CLI e no Codex um comando só roda quando você o nomeia: uma mensagem que por acaso bate com o que ele faz não inicia nada."

`book/en/12-propose.md`, "Several lines in one command":

* en :159, "The commands keep the setting of chapter 8 that stops Claude Code from running a skill on its own, `disable-model-invocation`: the command you typed names every slug, and each subagent takes its slug from the message that opens it and runs on your word, so no subagent needs the setting lifted." becomes

  "The commands keep the settings of chapter 8 that stop a host from running a skill on its own, `disable-model-invocation` in Claude Code and the Copilot CLI and the file beside each skill in Codex: the command you typed names every slug, and each subagent takes its slug from the message that opens it and runs on your word, so no subagent needs a setting lifted."

* en :160, "Lifting it would bring back what it prevents:" becomes "Lifting one would bring back what it prevents:", the rest of the sentence unchanged.

* en :192, summary bullet, "the commands keep `disable-model-invocation`, since your command names every slug;" becomes "the commands keep what stops a host from running a command on its own, `disable-model-invocation` and Codex's file beside each skill, since your command names every slug;", the rest of the bullet unchanged.

`book/pt/12-propose.md`, "Várias linhas em um comando":

* pt :168, "Os comandos mantêm a configuração do capítulo 8 que impede o Claude Code de rodar uma skill por conta própria, `disable-model-invocation`: o comando que você digitou nomeia todos os slugs, e cada subagente tira o seu slug da mensagem que o abre e roda pela sua palavra, então nenhum subagente precisa que a configuração seja tirada." becomes

  "Os comandos mantêm as configurações do capítulo 8 que impedem um host de rodar uma skill por conta própria, o `disable-model-invocation` no Claude Code e no Copilot CLI e o arquivo ao lado de cada skill no Codex: o comando que você digitou nomeia todos os slugs, e cada subagente tira o seu slug da mensagem que o abre e roda pela sua palavra, então nenhum subagente precisa que uma configuração seja tirada."

* pt :169, "Tirá-la traria de volta o que ela impede:" becomes "Tirar uma delas traria de volta o que ela impede:", the rest unchanged.

* pt :201, summary bullet, "os comandos mantêm o `disable-model-invocation`, já que o seu comando nomeia todos os slugs;" becomes "os comandos mantêm o que impede um host de rodar um comando por conta própria, o `disable-model-invocation` e o arquivo do Codex ao lado de cada skill, já que o seu comando nomeia todos os slugs;", the rest unchanged.

No term of docs/03 is introduced (the host rows already hold Claude Code, the Copilot CLI and Codex); no source is added; no case is drawn on. No other line in flight touches chapters 10 or 12: `m28-claim-wording` edits chapters 13 and 19, docs/03 and ADR-0018, `ch08-update-choice-outcome` chapter 8, `ch13-16-several-slugs-sessions` chapters 13 and 16, `m28-records-claims` records in `work/done/`.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapter 8: it already names all three (the source of this finding).
* Copilot in VS Code and the other hosts: chapter 8 makes no claim for them.
* The rest of chapter 12's subagent section: host-neutral already.
* The record `work/done/ch10-copilot-cli-invocation.md`, whose Out of scope kept chapter 12 as true of Claude Code: a record of what was decided then, left as it happened.

**Decisions taken alone.** The agent chose each one, per the batch rules; the author may correct them in review.

* Chapter 12 names each host's mechanism, the field for Claude Code and the Copilot CLI, the file for Codex, rather than one name for all, because chapter 8 says Codex turns it off with a file and not the field; the queue line's "setting" reads as "settings".
* Chapter 12's next sentence (en :160, pt :169) and its summary bullet (en :192, pt :201) are sibling sentences that would go stale with en :159 / pt :168 and belong to no other line, so they enter, as the batch rules allow.
* Codex enters chapter 12 although the review's C9 named only the Copilot CLI: the queue line names Codex, and chapter 8 en :132 says it.
* Short host names follow each chapter's habit: "the GitHub Copilot CLI" in chapter 10, beside its table; "the Copilot CLI" in chapter 12, as chapter 8 writes it.
* Queue line wording: unchanged.
* `(PA)` judged `(PA)`: the definition takes nothing from a line in flight (`m28-review` is `[x]`), and the build touches only chapters 10 and 12, which no line in flight edits.

**Divergences.** None from the Contract: the eight sentences went in word for word as the Contract writes them, at en 10 :33, pt 10 :33, en 12 :159, :160 and :192, and pt 12 :168, :169 and :201; no other line of chapters 10 or 12 moved. Chapter 8's cited lines did not move with `ch08-update-choice-outcome`: the claims are still at en 08 :132-135 and pt 08 :134-137. The Done when, as defined at `0ada2f1`, held no Delivery review item, which docs/05 §5 asks before /apply ends; the review ran as its paragraph records (Delivery review).

**Decisions taken by /apply.** Nothing was open. The queue line's wording is the driver's to change (the batch rules keep docs/06 out of this lane); it stands unchanged.

**Proof.**

* `make verify`: green, every check passed (build, parity, em dash, prose, width, examples, links, disclosure), exit 0, after the chapter edits and again after these records and the page's move to `work/done/`.
* `make book`: run after the verify that followed the records, before this delivery's commit `f628338`, whose parent is `12d5b84`, where docs/06 holds `m28-claim-wording` `[>]` beside it, the batch's lanes sharing one tree; the tree's HEAD and which lanes' uncommitted edits it held are not recorded; exit 0; the PDFs to review are `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. `make verify` ran once more after this line, green, exit 0.

**Delivery review.** One read-only Opus agent, launched by this /apply over this delivery's paths only (`git diff HEAD` of both editions of chapters 10 and 12), against this page, docs/04 and `AGENTS.md`, with chapter 8 en :128-137 and pt :130-139 for the claims. Its reply: no finding. All eight changed sentences match the Contract character for character (chapter 10 :33 in both editions; chapter 12 en :159, :160, :192 and pt :168, :169, :201); the diff is 8 insertions and 8 deletions across the four files, no other line touched; only Claude Code, the Copilot CLI and Codex are named, each backed by chapter 8 (en :132 / pt :134 for Codex's file, en :133-134 / pt :135-136 for the field and the Copilot CLI), and Copilot in VS Code and the other hosts are not named; no sentence says Codex honours `disable-model-invocation`; no source note, em dash, commit hash or run narration; the editions agree point for point, host names follow the page, and the Portuguese reads naturally; in both editions the section says "settings" and "Lifting one", and the summary bullet names both mechanisms. It ran neither verify nor the book, being read-only. Whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none. No private case, so OD-3 approval is inapplicable.

**Done when.**

* [x] Both editions of chapter 10 :33 changed as the Contract says, and nothing else in the chapter.
* [x] Both editions of chapter 12 changed at the three places the Contract says, and nothing else in the chapter.
* [x] Each chapter still opens with its value; no filler and nothing useful cut.
* [x] The claims trace to chapter 8 en :132-134 / pt :134-136.
* [x] No em dash, no commit hash, no run narration; disclosure scan green.
* [x] `make verify` green; `make book` run and both PDF paths given.

```commit
docs(ch10-12-no-implicit-hosts): name Codex beside the other two hosts

- chapter 10: a command runs only when named in Claude Code, the GitHub
  Copilot CLI and Codex; both editions
- chapter 12: the commands keep each host's setting, the field in Claude
  Code and the Copilot CLI, the file beside each skill in Codex
- chapter 12: the next sentence and the summary bullet agree

work/done/ch10-12-no-implicit-hosts.md
```
