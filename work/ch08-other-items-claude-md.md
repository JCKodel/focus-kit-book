# ch08-other-items-claude-md

**Objective.** After chapter 8 the reader reads the update report's excerpt and the outcomes explained after it as one account, knows that the rest of docs/05 §4 was checked though the excerpt does not show it, and knows who writes `CLAUDE.md`: `/brainstorm` or `/analyze`, never the setup file.

**Behaviour.**

* Given the second outcome (en :86 / pt :87), the reader finds it pointing at the excerpt's two docs/05 §4 items that lack something, what `after` requires and a command told to decide alone, not at §4 as a whole, whose third item in the excerpt matches and ends in `None` (m29-review C2).
* Given the excerpt's closing line (en :79-80 / pt :79-80), the reader finds the rest of docs/05 §4 among the items the excerpt does not show, as the record says: "docs/05 §4, every other item: matches" (`work/done/kit-2026-10-20-5.md` :88) (C3).
* Given the hosts section's lead-in (en :120 / pt :121), the reader finds the setup file writing each host's command files and the pointers to `AGENTS.md` in `GEMINI.md` and `.agents/rules/focus-kit.md`, and `/brainstorm` or `/analyze` writing `AGENTS.md` and `CLAUDE.md` with its import, as the install section (en/pt :40-42) and the key point (en :183 / pt :184) say, and as SETUP at focus-kit `cc16f4e` says: :118-121 (everything the four commands write, `AGENTS.md` and `CLAUDE.md` among it, is never touched by the setup file), :275 and :350 (/brainstorm and /analyze write `CLAUDE.md` holding `@AGENTS.md`), §§3.11 and 3.12 (the setup file writes the rule and `GEMINI.md`'s pointer line) (C5).
* Given the Claude Code sentence (en :136 / pt :137), the reader finds `/brainstorm` or `/analyze` writing `CLAUDE.md` with the import, which every version reads, not "the kit" (C5).
* Given the Portuguese lead-in to the excerpt (pt :59), the reader of the source finds one sentence per line, as docs/04 :18 asks; the English (en :59) is one sentence already (C4).
* Edge: the excerpt's items themselves, the table rows, the first and third outcomes and en :168 / pt :169 ("The setup file writes every host's files") are unchanged.
* Fails: a block line over 74 columns (docs/04 :44, rule `width`); any other line of chapter 8 changed; a claim the record or SETUP does not make; an em dash; a commit hash; one edition changed without the other. /apply removes it before verify.

**Contract.** Both editions, same change; English is the source (ADR-0004). Line numbers as the files are now (HEAD `ea83160`). Source line breaks as given, one sentence per line; the block lines as given, measured at most 64 columns.

`book/en/08-install-and-hosts.md`:

* en :79-80, in the excerpt's block,

  ```
  The other items cover docs/05 §§2, 3 and 6 to 8, the other slots of
  §5, docs/04, docs/06 and AGENTS.md.
  ```

  becomes

  ```
  The other items cover docs/05 §§2, 3 and 6 to 8, the rest of §4,
  the other slots of §5, docs/04, docs/06 and AGENTS.md.
  ```

* en :86, "It lacks something, and the item gives the wording the template proposes and where it goes, as for docs/05 §4." becomes

  "It lacks something, and the item gives the wording the template proposes and where it goes, as the two docs/05 §4 items on `after` and on a command told to decide alone do."

* en :120, "The setup file writes what every host below needs:" becomes

  "The setup file writes each host's command files and the pointers to `AGENTS.md` in `GEMINI.md` and `.agents/rules/focus-kit.md`; `/brainstorm` or `/analyze` writes `AGENTS.md` and `CLAUDE.md` with its import (chapter 9); the table says where each host reads them:"

* en :136, "..., but only in a repository with no `CLAUDE.md`, so the kit writes `CLAUDE.md` with the import, which every version reads." becomes "..., but only in a repository with no `CLAUDE.md`, so `/brainstorm` or `/analyze` writes `CLAUDE.md` with the import, which every version reads." The rest of the line, its footnote included, stays.

`book/pt/08-install-and-hosts.md`:

* pt :59, one line, becomes two:

  "Esta é uma parte do relatório que a atualização para o focus-kit 2026.10.20.5 deu no próprio repositório deste livro, encurtada e parafraseada, e traduzida aqui: os documentos do livro são em inglês, e o relatório propôs o texto em inglês."

  "O registro dessa atualização é o `work/done/kit-2026-10-20-5.md`, no repositório do livro."

* pt :79-80, in the excerpt's block,

  ```
  Os outros itens cobrem o docs/05 §§2, 3 e 6 a 8, os outros slots do
  §5, o docs/04, o docs/06 e o AGENTS.md.
  ```

  becomes

  ```
  Os outros itens cobrem o docs/05 §§2, 3 e 6 a 8, o resto do §4,
  os outros slots do §5, o docs/04, o docs/06 e o AGENTS.md.
  ```

* pt :87, "Ele não tem alguma coisa, e o item dá o texto que o modelo propõe e onde ele entra, como no docs/05 §4." becomes

  "Ele não tem alguma coisa, e o item dá o texto que o modelo propõe e onde ele entra, como os dois itens do docs/05 §4 sobre o `after` e sobre um comando mandado decidir sozinho."

* pt :121, "O arquivo de setup escreve o que cada host abaixo precisa:" becomes

  "O arquivo de setup escreve os arquivos de comando de cada host e os ponteiros para o `AGENTS.md` no `GEMINI.md` e em `.agents/rules/focus-kit.md`; o `/brainstorm` ou o `/analyze` escreve o `AGENTS.md` e o `CLAUDE.md` com a sua importação (capítulo 9); a tabela diz onde cada host os lê:"

* pt :137, "..., mas só num repositório sem `CLAUDE.md`, então o kit escreve o `CLAUDE.md` com a importação, que toda versão lê." becomes "..., mas só num repositório sem `CLAUDE.md`, então o `/brainstorm` ou o `/analyze` escreve o `CLAUDE.md` com a importação, que toda versão lê." The rest of the line, its footnote included, stays.

No term of docs/03 is introduced; no source note is added (the excerpt already names its record; SETUP is the kit's, already named in the chapter); no case is drawn on. No neighbouring line touches chapter 8: `ch14-renewal-example` edits chapter 14, `m29-records-claims` record pages in `work/done/` and docs/03.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* The excerpt's items: they paraphrase the record and the review saw nothing wrong in them.
* en :168 / pt :169, "The setup file writes every host's files, whichever host runs it": SETUP :122's own wording, the kit's files for every host, true as written and not seen by the review.
* The table's rows: they come from SETUP's table and say where each host reads, not who writes.
* Reordering the Portuguese lead-in so it ends in a colon as the English does: the finding is one sentence per line, and the split meets it.
* Any record page in `work/done/` and docs/03: `m29-records-claims`' lane.

**Decisions taken alone.** The agent chose each one, per the batch rules; the author may correct them in review.

* The lead-in names `GEMINI.md` and `.agents/rules/focus-kit.md` as the setup file's: SETUP §§3.11 and 3.12 write them, and the chapter says so at :42 and :139, so "the rules files" for /brainstorm or /analyze, as the queue line has it, would deny it; the page names `AGENTS.md` and `CLAUDE.md` instead.
* Queue line wording: "the setup file writes each host's command files and /brainstorm or /analyze the rules files, CLAUDE.md with the import among them" becomes "the setup file writes each host's command files and pointers and /brainstorm or /analyze AGENTS.md and CLAUDE.md with the import"; the rest of the line stays.
* "the rest of §4" goes after "6 to 8", so the block's first line stays as it is but for its tail and both lines fit 74 columns (64 and 54 en, 63 and 58 pt).
* The second outcome names the two §4 items by their subjects, not by count alone, so the reader finds them in the excerpt.
* `(PA)` judged `(PA)` by docs/05 §4 :103-106: no line above is in flight (`m29-review` is `[x]`), the definition takes nothing from another page, and the build touches only chapter 8, which neither neighbouring line edits.

**Done when.**

* [ ] Both editions of chapter 8 changed at en :79-80, :86, :120, :136 / pt :59, :79-80, :87, :121, :137 as the Contract says, and nothing else in the chapter.
* [ ] The chapter still opens with its value; no filler and nothing useful cut.
* [ ] Every claim traces to `work/done/kit-2026-10-20-5.md` :88 or SETUP at focus-kit `cc16f4e` :118-121, :275, :350, §§3.11, 3.12.
* [ ] No em dash, no commit hash, no run narration; every block line within 74 columns; disclosure scan green.
* [ ] Delivery review as docs/05 §5 says, its record saying what the agent read and what its reply says of the advisor.
* [ ] `make verify` green after the last edit; `make book` run, with its HEAD and tree named, and both PDF paths given.
