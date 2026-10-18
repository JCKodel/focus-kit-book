# ch07-talk-not-edit

**Objective.** A reader of chapter 7 reads, in one plain statement, that they change the documents by talking to the agent, without the sentence that first says they do not edit by hand and then recommends they do not, which reads as a contradiction. Both editions. From the author's reading of the book on 2026-10-18: "pt 07:133, 'Você não edita os documentos à mão, e eu recomendo que não edite', reads oddly. Better: 'Você não edita os documentos à mão, você conversa com o agente para alterá-los, apontando uma lacuna, um detalhe errado...'"

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *Two lines become two, the first one rewritten in the author's words.* Under "Living documents" the statement and the recommendation (en 07:132, pt 07:133 at /propose) and the "Talk to the agent" line after it say the same thing twice. The first line becomes the author's sentence, which ends on what the reader points at; the second keeps what the agent does and why, starting from "It finds". Nothing of the second line is lost: owner document, the documents saying where each fact lives, the conversation keeping the reason. Source: the draft, docs/04 §Writing the book (one sentence per line, no filler, nothing useful cut).
2. *English joins the two clauses with a semicolon.* The author's Portuguese comma joins two clauses, natural in Portuguese; English source reads "You do not edit the documents by hand; you talk to the agent to change them, ...". Source: ADR-0004 (English is the source, the editions say the same thing), the en chapter's own use of semicolons (en 07:15).
3. *"I recommend" is dropped, not moved.* The author's version has no recommendation; the chapter's key point (en 07:152, pt 07:153) already says "You change the documents by talking to the agent" with no recommendation, and stays. Source: the draft; docs/04 §Writing the book.
4. *Rest of chapter 7 unchanged.* The opening line (en 07:4) and the docs/06 line (en 07:42) already say "by talking to the agent" and "by conversation"; they agree and stay. Source: book/en/07-the-documents.md.
5. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* The reader of chapter 7, in English, under "Living documents", reads in place of the two lines that begin "You do not edit" and "Talk to the agent":
  * "You do not edit the documents by hand; you talk to the agent to change them, pointing at a gap, a wrong detail, something to add, change or remove."
  * "It finds the document that owns the fact and writes the change there, since the documents tell it where each fact lives, and the conversation keeps the reason."
* The reader of the Portuguese edition, under "Documentos vivos":
  * "Você não edita os documentos à mão, você conversa com o agente para alterá-los, apontando uma lacuna, um detalhe errado, algo a acrescentar, mudar ou remover."
  * "Ele encontra o documento dono do fato e escreve a mudança ali, já que os documentos lhe dizem onde mora cada fato, e a conversa guarda o motivo."
* The two lines after them ("Your part is to interpret, guide and validate" and "An agent's text reads as right") are unchanged.
* Checked at apply time:
  * `grep -n "I recommend you do not\|eu recomendo que não edite" book/*/07-the-documents.md` prints nothing.
  * `grep -n "you talk to the agent to change them\|você conversa com o agente para alterá-los" book/*/07-the-documents.md` prints one line per edition.
  * `git diff book/` shows only these two lines per edition.
* Fails: "I recommend" or "recomendo" kept anywhere in the paragraph; any of the second line's facts dropped; the key point or any other line of chapter 7 changed; a pointer to a later chapter added; an em dash.

**Contract.**

* Files: `book/en/07-the-documents.md`, `book/pt/07-the-documents.md`; the two lines under "Living documents" / "Documentos vivos" (en 07:132-133, pt 07:133-134 at /propose).
* Terms of docs/03: none new. Sources: none added or removed. Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `ch07-rag-and-numbers` edits chapter 7's "The seven documents" section (around 07:35-41), far from "Living documents"; no shared hunk.
* `early-no-forward-links` names this line as holding no pointer of its list (its page, "Deliveries in flight"); the new lines name no chapter or command.
* `pt-ninjobs-masculine` changes Ninjobs's article in pt 07:10, 56 and 144; the new lines have no Ninjobs mention.
* `ch13-teach-the-agent` (still a draft) says the same idea for code in chapter 13's staged review: correct by talking to the agent. This delivery touches chapter 7 only; the two agree and neither edits the other's file.
* Whichever lands first shifts line numbers; the lines are found by their text, not their number.

**Out of scope.**

* The key point (en 07:152) and the opening (en 07:4): decision 4.
* Chapter 13's review by conversation: `ch13-teach-the-agent`.

**Done when.**

* [x] Both editions written: the two lines as Behaviour says.
* [x] Chapter 7 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: none added.
* [x] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author: run by the batch driver at the end of the batch.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Divergences.** None. Both lines in each edition are the Behaviour's exact words.

**Proof.**

* The `grep` for "I recommend you do not" and "eu recomendo que não edite" prints nothing.
* The `grep` for the new first line prints one line per edition (en 07:142, pt 07:143).
* `git diff -- book/` on chapter 7 shows two lines changed per edition, nothing else.
* `make verify` passes build, parity, em dash, prose, width, links and disclosure, with exit 0.

**Review.** A read-only Opus reviewer that did not write the change read the diff against this page and docs/04. Nothing breaks the page or docs/04; the wording matches Behaviour, no fact of the old second line is lost, and no Fails pattern appears. Its one optional suggestion, a semicolon in the Portuguese line to match the English, is not applied: the page keeps the author's comma on purpose (decision 2). There is no new queue line.

**Decisions.** The batch driver owns docs/06, the staging and the commit, and runs `make book`.

```commit
docs(ch07-talk-not-edit): say the reader changes the documents by talking to the agent

- Chapter 7, both editions, "Living documents": the line that said the reader does not edit by hand and then recommended not to becomes one statement, in the author's words, that the reader talks to the agent to change the documents, pointing at what is wrong or missing; the next line keeps what the agent does and why

book/en/07-the-documents.md
book/pt/07-the-documents.md
docs/06-Queue.md
work/done/ch07-talk-not-edit.md
```
