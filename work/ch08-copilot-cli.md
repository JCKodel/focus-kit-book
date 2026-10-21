# ch08-copilot-cli

**Objective.** After chapter 8 the reader can tell the two GitHub Copilot hosts apart and invoke the kit's commands in either: Copilot in VS Code, which takes a command through a prompt file in `.github/prompts/` and asks for the slug, and the GitHub Copilot CLI, GitHub's agent in the terminal, which reads `AGENTS.md` merged with `CLAUDE.md` and `GEMINI.md`, takes the skills from `.agents/skills/` with no pointer file, runs one as `/propose`, and, like Claude Code, runs a skill only when the person names it; chapter 10's short table says the same.

**Behaviour.**

* Given chapter 8's host table, the reader finds two Copilot rows: "GitHub Copilot in VS Code", as the single row reads today, and "GitHub Copilot CLI": rules from `AGENTS.md`, merged with `CLAUDE.md` and `GEMINI.md`; commands from `.agents/skills/`; you type `/propose` (SETUP.md §1 at 2026.10.20.4, :133-134).
* The reader knows the CLI needs no pointer file: it reads `.agents/skills/` itself, and its slash command is the skill's own name, where Copilot in VS Code gets its slash command from a prompt file that asks for the slug.
* The reader knows the CLI's rules come from three files at once, merged: `AGENTS.md`, `CLAUDE.md` and `GEMINI.md`, so what the team writes in `CLAUDE.md` or `GEMINI.md` reaches the CLI too (the CLI reference, "Custom instructions locations": "loads custom instructions from these locations simultaneously (all are merged)", accessed 2026-10-21).
* The reader knows the CLI honours `disable-model-invocation`, the field Claude Code's skills carry, so in both a message that matches a skill's description runs nothing; "on the other hosts, invoke the commands yourself" now leaves both out (SETUP :162-165; the CLI reference, "Skill frontmatter fields").
* The reader knows the CLI's documentation does not say whether a slug typed after `/propose` reaches the command, as for Cursor and Devin Desktop, so they name the delivery in the message if it does not (SETUP :134; the CLI reference, checked 2026-10-21, documents `argument-hint` and no argument substitution).
* The reader still learns the folder order for a skill in both skills folders, `.agents/skills/` before `.claude/skills/`, first found wins, now said of the CLI, whose reference documents it.
* Given chapter 10's table, the reader finds the same two Copilot rows with what to type: "GitHub Copilot in VS Code", `/propose`, and it asks for the slug; "GitHub Copilot CLI", `/propose`.
* Key points name both: Copilot in VS Code as `/propose`, which asks for the slug, the Copilot CLI as `/propose`, and the folder order as the CLI's.
* Edge: en 9 ("another in Copilot inside their editor") and en 34 ("Copilot asks for no slug", of `/brainstorm` and `/analyze`) stay; both are still true of Copilot in VS Code, and the CLI asks for no slug either. Their Portuguese (pt 9, pt 34) stays.
* Edge: the CLI reference lists `.github/skills/` before `.agents/skills/`; the kit writes nothing there, so the chapter does not name it. The CLI also reads `.claude/rules/`, `.github/copilot-instructions.md` and personal files; the chapter names only the three files the kit's row names.
* Fails: a claim not on SETUP.md at `ffbec72` or on the CLI reference; the changelog's "on the Free plan included" (not on the cited page); the harness run that told the CLI to ask for the skill by name (a narrated run); a claim that the CLI reads `AGENTS.md` twice through `CLAUDE.md`'s `@AGENTS.md`, or how the merged files combine; a quote from the page carrying an em dash; `.github/skills/` in the chapter; a commit hash or `(PA)` in the chapter; anything later than `ffbec72`; an em dash; one edition changed without the other. /apply removes it before verify.

**Contract.** Both editions, same changes; English is the source (ADR-0004). Line numbers as the files are now (HEAD `b595ca0`; chapter 8 last changed by `ch08-update-2026-10-20-4`).

`book/en/08-install-and-hosts.md` and `book/pt/08-install-and-hosts.md`, "How each host finds the commands" / "Como cada host encontra os comandos":

* Table, en 116 / pt 118: the row becomes "GitHub Copilot in VS Code" / "GitHub Copilot no VS Code", its cells unchanged. A new row follows it:

  en: `| GitHub Copilot CLI | `AGENTS.md`, merged with `CLAUDE.md` and `GEMINI.md` | `.agents/skills/` | `/propose` |`

  pt: `| GitHub Copilot CLI | `AGENTS.md`, mesclado com `CLAUDE.md` e `GEMINI.md` | `.agents/skills/` | `/propose` |`

* en 126 / pt 128: "Codex, Copilot and Devin Desktop, formerly Windsurf, read `AGENTS.md` on their own." becomes "Codex, Copilot in VS Code and Devin Desktop, formerly Windsurf, read `AGENTS.md` on their own." with its notes unchanged; pt "O Codex, o Copilot no VS Code e o Devin Desktop, antes Windsurf, leem o `AGENTS.md` sozinhos." A new line follows:

  en: "The GitHub Copilot CLI, GitHub's agent in the terminal, reads `AGENTS.md`, `CLAUDE.md` and `GEMINI.md` together and merges them, so what the team writes in either of the other two reaches it as well.[^copilot-cli-reference]"

  pt: "O GitHub Copilot CLI, o agente do GitHub no terminal, lê o `AGENTS.md`, o `CLAUDE.md` e o `GEMINI.md` juntos e os mescla, então o que o time escreve em qualquer dos outros dois também chega até ele.[^copilot-cli-reference]"

* en 128 / pt 130: "Copilot's slash command comes from a prompt file" becomes "Copilot in VS Code takes its slash command from a prompt file", the rest unchanged; pt "O Copilot no VS Code tira o seu comando de barra de um arquivo de prompt", the rest unchanged. A new line follows:

  en: "The Copilot CLI needs no such file: it reads the skills from `.agents/skills/` itself and runs one by its name, `/propose`.[^copilot-cli-reference]"

  pt: "O Copilot CLI não precisa desse arquivo: ele lê as skills de `.agents/skills/` sozinho e roda uma pelo nome, `/propose`.[^copilot-cli-reference]"

* en 130 / pt 132, the `disable-model-invocation` sentence: after its note, a new sentence: en "The Copilot CLI honours the same field.[^copilot-cli-reference]"; pt "O Copilot CLI respeita o mesmo campo.[^copilot-cli-reference]". en 131 / pt 133 ("On the other hosts, invoke the commands yourself; ...") unchanged; it now reads after both.
* en 132 / pt 134: "For Cursor and Devin Desktop, neither vendor's documentation says" becomes "For Cursor, Devin Desktop and the Copilot CLI, no vendor's documentation says", the rest unchanged; pt "Para o Cursor, o Devin Desktop e o Copilot CLI, nenhum dos fornecedores diz na documentação", the rest unchanged.
* en 133 / pt 135: "Copilot reads both skills folders, and its CLI reference says what happens" becomes "The Copilot CLI reads both skills folders, and its reference says what happens", the rest unchanged; pt "O Copilot CLI lê as duas pastas de skills, e a sua referência diz o que acontece", the rest unchanged.
* "Key points" / "Pontos-chave", en 171 / pt 173: "Copilot as `/propose`, which asks for the slug," becomes "Copilot in VS Code as `/propose`, which asks for the slug, the Copilot CLI as `/propose`,"; pt "o Copilot no VS Code como `/propose`, que pede o slug, o Copilot CLI como `/propose`,"; and "Copilot takes a skill from" becomes "the Copilot CLI takes a skill from"; pt "o Copilot CLI pega uma skill de".
* Note `[^copilot-cli-reference]`, en 180 / pt 182: "accessed 2026-10-19" becomes "accessed 2026-10-21"; pt "acesso em 2026-10-21". No new note.
* Everything else in chapter 8 unchanged, en 9 and en 34 and their Portuguese included (see Behaviour).

`book/en/10-quick-guide.md` and `book/pt/10-quick-guide.md`, "Before you start" / its Portuguese, the table, en 23 / pt 23: the row becomes "GitHub Copilot in VS Code" / "GitHub Copilot no VS Code", its cell unchanged; a new row follows: en `| GitHub Copilot CLI | `/propose` |`, pt the same. Nothing else in chapter 10 changes; en 32's "or, where neither works, in your message" already covers the CLI.

`docs/03-Domain.md`, the host row (:19), its identifiers gaining `copilot-cli` after `copilot`, nothing else:

    | host | host | `claude-code`, `codex`, `copilot`, `copilot-cli`, `cursor`, `gemini-cli`, `antigravity`, `devin-desktop` | The program that runs the coding agent. |

Neighbouring lines on the same files: `ch13-19-claim-script` (M28, `[*]`) edits docs/03's claim row, a different row of the same file, and chapters 13 and 19, which this page does not touch; it comes first in queue order, so /apply here builds on its docs/03. `ch08-update-2026-10-20-4` (`[x]`) last changed chapter 8; the line numbers above are after it. No other chapter names the hosts: chapter 20's Copilot is the code review, chapters 11 and 21's is Copilot Studio; neither changes.

Sources: SETUP.md 2026.10.20.4, `git -C ~/Projects/focus-kit show ffbec72:SETUP.md` (SHA-256 `a8515b46…b1dc1e`), the host table :129-140 (rows :133-134), the paragraph naming the CLI reference :142-160, and :162-165 on `disable-model-invocation`; the kit's CHANGELOG.md, 2026.10.20.4, its second item; GitHub, "GitHub Copilot CLI command reference", <https://docs.github.com/en/copilot/reference/cli-command-reference>, fetched 2026-10-21, sections "Custom instructions locations", "Skill locations" and "Skill frontmatter fields", paraphrased, the existing note `[^copilot-cli-reference]`. Nothing later than `ffbec72`. No new term of docs/03 beyond the identifier above; "Copilot CLI" is a product name. No data, schema or API.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** `.github/skills/` and the CLI's other instruction files: the kit writes none. The changelog's Free plan remark and its harness run. Copilot in VS Code's own reading of `.claude/skills/`, unchanged. Chapters 13 and 19 and docs/03's claim row: `ch13-19-claim-script`. Chapter 20's Copilot code review. docs/06, docs/05, the kit repository, anything later than `ffbec72`.

**Decisions from the documents.**

* Two rows, the VS Code one first, named as SETUP §1 names them ("GitHub Copilot in VS Code", "GitHub Copilot CLI"), the chapter's commands column shortened to the folder as for every other row.
* The CLI's "You type" is `/propose`, with the slug caveat in prose beside Cursor and Devin Desktop, as SETUP :134 says "not documented" and the page, checked 2026-10-21, still does not document it.
* `disable-model-invocation` for the CLI: SETUP :162-165, confirmed on the page.
* No source note beyond the existing one: the date changes because the page was read again for this delivery.

**Decisions taken alone.** The agent chose each of these.

* Chapter 10's table is in this delivery: its lead-in says "a command takes the form of chapter 8's table", it goes stale with the new row, and no other line owns it. The queue line should read "chapters 8 and 10".
* docs/03's host row gains `copilot-cli`: the row lists the hosts, and the book now names one more. Kept to the identifier column.
* en 9 and en 34 stay: true as they are; widening them adds nothing the reader needs.
* The gain sentence for the CLI is the one this page gives (what the team writes in `CLAUDE.md` or `GEMINI.md` reaches it); "What the team gains" is unchanged, its "One repository opens ready in any host" covering the new row.
* `(PA)` judged `(P-)`: the definition takes nothing from the pages above (`P`); the build touches docs/03, which `ch13-19-claim-script`, `[*]` above it, also edits (`-`, its /apply waits for that line's `[x]`). Dropping the docs/03 row would make it `(PA)`; the author may choose that in review.

**Done when.**

* Both editions of chapters 8 and 10 changed as the Contract says, and docs/03's host row.
* The chapter still opens with its value; no filler and nothing useful cut.
* Every claim about the CLI traces to SETUP.md at `ffbec72` or the CLI reference accessed 2026-10-21.
* No em dash, no commit hash, no run narration in the chapters; disclosure scan green.
* `make verify` green; `make book` run and both PDF paths given.
