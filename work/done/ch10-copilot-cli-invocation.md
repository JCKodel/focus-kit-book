# ch10-copilot-cli-invocation

**Objective.** After chapter 10 the reader knows that in Claude Code and in the GitHub Copilot CLI a command runs only when they name it, as chapter 8 says of both, so the quick guide no longer reads as if Claude Code were the only host that keeps a matching message from starting a command.

**Behaviour.**

* Given chapter 10's "Before you start", the reader finds the sentence after the table naming both hosts: in Claude Code and the GitHub Copilot CLI a command runs only when you name it, and a message that happens to match what it does starts nothing.
* The reader finds the host named as the table just above names it, "GitHub Copilot CLI", so the sentence and its row read as the same host.
* The claim matches chapter 8: Claude Code's skills carry `disable-model-invocation: true` and "The Copilot CLI honours the same field" (en 08 :133-134, pt 08 :135-136); chapter 10 adds no source note, as it carries none and chapter 8 holds the source.
* Edge: Copilot in VS Code is not named: chapter 8 does not say it honours the field, and "On the other hosts, invoke the commands yourself" (en 08 :135) still covers it.
* Edge: chapter 12 :159 and :192, "the setting of chapter 8 that stops Claude Code from running a skill on its own", stay: they speak of the subagents the person's command opens in Claude Code, and remain true; widening them is outside this finding.
* Fails: any other line of chapter 10 changed; Copilot in VS Code named in the sentence; a claim chapter 8 does not make; a source note; an em dash; a commit hash; one edition changed without the other. /apply removes it before verify.

**Contract.** Both editions, same change; English is the source (ADR-0004). Line numbers as the files are now (HEAD `c75deb0`, chapter 10 last changed by `ch08-copilot-cli`, which moved the sentence from :32 to :33).

`book/en/10-quick-guide.md`, "Before you start", en :33:

* "In Claude Code a command runs only when you name it: a message that happens to match what it does starts nothing." becomes

  "In Claude Code and the GitHub Copilot CLI a command runs only when you name it: a message that happens to match what it does starts nothing."

`book/pt/10-quick-guide.md`, "Antes de começar", pt :33:

* "No Claude Code um comando só roda quando você o nomeia: uma mensagem que por acaso bate com o que ele faz não inicia nada." becomes

  "No Claude Code e no GitHub Copilot CLI um comando só roda quando você o nomeia: uma mensagem que por acaso bate com o que ele faz não inicia nada."

No term of docs/03 is introduced (the host row already holds `copilot-cli`); no source is added; no case is drawn on. No other in-flight line touches chapter 10; `m28-review` comes after this line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapter 8: it already says both (the source of this finding).
* Chapter 12 :159 and :192: true of Claude Code's subagents as written.
* The review's note 2 on pt 08 :132 ("tira"): left by ch08-copilot-cli as optional, not this line's finding.
* Chapter 10's table and its slug sentence (en :32): already updated by ch08-copilot-cli and still true.

**Decisions taken alone.** The agent chose each one, per the batch rules; the author may correct them in review.

* The host is written "the GitHub Copilot CLI" / "no GitHub Copilot CLI", the table's name, rather than chapter 8's short "the Copilot CLI", so the sentence matches the row two lines above.
* No "(chapter 8)" pointer in the sentence: the section already sends the reader to chapter 8's table, and docs/04 wants no filler.
* Queue line wording: the line cites "(en :32)"; the sentence is at :33 since ch08-copilot-cli added the CLI's row. Suggested wording: `chapter 10: "In Claude Code a command runs only when you name it" (en :33) names the Copilot CLI too, which honours the same field (chapter 8); both editions · after ch08-copilot-cli`.
* `(PA)` judged `(PA)`: the definition takes nothing from a line in flight (`ch08-copilot-cli` is `[x]`), and the build touches only chapter 10, which no line above in flight edits.

**Divergences.** None: both sentences went in word for word as the Contract writes them, at en :33 and pt :33; no other line of chapter 10 moved.

**Decisions taken by /apply.** Nothing was open. The queue line's wording is the driver's to change (the batch rules keep docs/06 out of this lane); the suggested wording above stands for it.

**Proof.**

* `make verify`: green, every check passed (build, parity, em dash, prose, width, examples, links, disclosure), exit 0, before the review and again after the page's records and its move to `work/done/`.
* `make book`: run after the last verify, exit 0; the PDFs to review are `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** One read-only Opus agent, launched by this /apply over this delivery's paths only (`git diff HEAD` of both editions of chapter 10, and this page before these records), against this page, docs/04 and `AGENTS.md`, with chapter 8 en :128-137 and pt :130-139 for the claim. Its reply: no finding. Each edition changes one line, en :33 and pt :33, word for word as the Contract asks, and no other line of chapter 10 changed; the claim matches chapter 8 en :133-134 and pt :135-136; "GitHub Copilot CLI" is the name of the table row at en :24 and pt :24; no em dash, no commit hash, no source note, no run narration, and Copilot in VS Code is not named; the Portuguese "No Claude Code e no GitHub Copilot CLI" reads naturally, its article matching chapter 8's masculine "O Copilot CLI". It ran neither verify nor the book, being read-only. No private case, so OD-3 approval is inapplicable.

**Done when.**

* [x] Both editions of chapter 10 :33 changed as the Contract says, and nothing else in the chapter.
* [x] The chapter still opens with its value; no filler and nothing useful cut.
* [x] The claim traces to chapter 8 en :133-134 / pt :135-136.
* [x] No em dash, no commit hash, no run narration; disclosure scan green.
* [x] `make verify` green; `make book` run and both PDF paths given.

```commit
docs(ch10-copilot-cli-invocation): name the Copilot CLI in chapter 10

- chapter 10: a command runs only when named in Claude Code and the
  GitHub Copilot CLI, as chapter 8 says; both editions

work/done/ch10-copilot-cli-invocation.md
```
