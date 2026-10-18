# ch11-agent-runs-propose

**Objective.** A reader of chapter 11 reads, under "Changing the queue", why a change asked in an ordinary session waits for `/propose` in a fresh session even when they say "define it now", told as the kit's rule and the error it prevents, without the claim that the agent cannot run `/propose` on its own, and knows that a host may run the command in the same session when asked or offer to, and what to do then. Both editions. From the author's reading of the book on 2026-10-18: "en 11:102, 'the agent cannot run `/propose` on its own, since it is a command the host runs, and a page written without it starts without what `/propose` reads', is not true: Claude Code offers to run /propose from the conversation and runs it itself, without the person typing `/propose`."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *The sentence holds two claims and only the first is false.* "The agent cannot run `/propose` on its own, since it is a command the host runs" is a claim about hosts, and the vendor documentation contradicts it: in Claude Code, a skill with `disable-model-invocation: true` is one Claude can invoke "Not on its own", and a command's name written after plain text in the person's message "counts as your permission for that message: Claude can run the skill while it responds" (Claude Code docs, "Extend Claude with skills", sections "Control who invokes a skill" and "Where you write the skill's name", read 2026-10-18); chapter 8's table already says OpenCode and Zed run a command "by asking for the skill" (en 08:113). "Saying 'define it now' changes nothing" stays true as the kit's rule: docs/05 §2 and AGENTS.md have the answer stop and name `/propose <slug>` for a fresh session. Source: the vendor page, docs/05 §2, book/en/08-install-and-hosts.md.
2. *The reason is said as the error the rule prevents, in the present.* A fresh session's window holds the rules file, the documents and the draft and nothing of the asking conversation (chapter 1, en 01:86), so the page holds only what was written down, which is all `/apply` will have (chapter 12, en 12:32). No chapter pointer is added: the sentence says the reason itself. Source: docs/04 §Writing the book, **The kit as it is** ("a rule's reason is the error it prevents, said in the present"), book/en/01-how-agents-see.md, book/en/12-propose.md.
3. *No host is named and no host mechanism is taught here.* The new sentence says only that a host may run the command in the same session when the person names it in their message, and that some offer to; this is true in every host the book covers, since any agent can read a skill file and some hosts run a named command. The author's observation fits it: Claude Code offering, then running on the person's word. No sentence says a host runs `/propose` unasked; Claude Code's own documentation says it blocks that. Where each host's switches are taught stays chapter 8's. Source: docs/00 ("Not a reference for any host's features"), the vendor page.
4. *The kit's fresh-session rule is not changed.* The kit ships its four commands with `disable-model-invocation: true` in `.claude/skills/` and `.agents/skills/`, and `allow_implicit_invocation: false` for Codex: the person invokes them. The book teaches the kit as it is, so the paragraph tells the reader to open a fresh session. Whether the kit should allow `/propose` in the asking session where the host can run it is a change to the kit's docs/05 §2, outside this book; if it happens, this paragraph changes again. Source: docs/04 **The kit as it is**, the skill files.
5. *The fifth key point stays.* en 11:171 (pt 11:176) says "`/propose` in a fresh session", still true, and has no "cannot". Source: book/en/11-queue-and-milestones.md.
6. *Line numbers.* The draft cites en 11:102; at /propose the sentence is at en 11:103 and pt 11:106. Apply finds it by its text.
7. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* The reader of chapter 11, in English, under "## Changing the queue", reads in place of the line that begins "Saying "define it now" changes nothing" these two lines:
  * "Saying "define it now" gets the same answer: the kit runs `/propose` in a fresh session, whose window holds the rules file, the documents and the draft and nothing of this conversation, so the page holds only what was written down, which is all `/apply` will have."
  * "A host may still run the command here when you name it in your message, and some offer to; the page would then be written beside everything said in this session, so open a fresh one."
* The reader of the Portuguese edition, under "## Mudando a fila", in place of the line that begins "Dizer "defina agora" não muda nada":
  * "Dizer "defina agora" recebe a mesma resposta: o kit roda o `/propose` numa sessão nova, cuja janela contém o arquivo de regras, os documentos e o rascunho, e nada desta conversa, então a página guarda só o que foi escrito, que é tudo o que o `/apply` terá."
  * "Um host pode mesmo assim rodar o comando aqui quando você o nomeia na sua mensagem, e alguns se oferecem para isso; a página seria escrita ao lado de tudo o que foi dito nesta sessão, então abra uma sessão nova."
* The line before ("The draft is where the detail waits", pt "O rascunho é onde o detalhe espera") and the line after ("A change this small still goes through the whole method", pt "Uma mudança tão pequena") are unchanged.
* Checked at apply time:
  * `grep -n "cannot run \`/propose\` on its own\|não consegue rodar o \`/propose\` sozinho" book/*/11-queue-and-milestones.md` prints nothing.
  * `grep -n "gets the same answer\|recebe a mesma resposta" book/*/11-queue-and-milestones.md` prints one line per edition.
  * `git diff book/` shows, for this delivery, only this paragraph's lines in both editions.
* Fails: any sentence saying the agent cannot run `/propose`, or that a host runs it unasked; a host named or a host setting (`disable-model-invocation`, `allow_implicit_invocation`) explained in chapter 11; the fresh-session rule softened into a preference; a `not-but` pattern; a pointer to a later chapter; a change to the key points or any other line of chapter 11; an em dash; a run narrated.

**Contract.**

* Files: `book/en/11-queue-and-milestones.md`, `book/pt/11-queue-and-milestones.md`; one line under "Changing the queue" / "Mudando a fila" becomes two (en 11:103, pt 11:106 at /propose).
* Terms of docs/03: none new; `host`, `fresh session` and `command` as the book has them. Sources: none added. Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `ch11-queue-grows` edits `### Size and order`, the third key point and adds the note `[^m15-queue]` in chapter 11, and leaves §Changing the queue to this delivery (its decision 8). No shared hunk; whichever lands first shifts line numbers, and each finds its text by the text.
* `early-no-forward-links` edits chapters 0 to 7 only; this delivery adds no pointer.
* `ch07-talk-not-edit` and the other M18 pages touch other chapters.

**Out of scope.**

* Chapter 8 does not say that the kit ships `disable-model-invocation: true` for Claude Code's commands (en 08:119 names only Codex's switch): a candidate line for chapter 8, by conversation, not this delivery.
* A change to the kit's fresh-session rule: focus-kit's repository (decision 4).
* The fifth key point: decision 5.

**Done when.**

* [ ] Both editions written: the two lines as Behaviour says.
* [ ] Chapter 11 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [ ] Every number sourced: none added.
* [ ] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [ ] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.
