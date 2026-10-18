# ch24-note-keys

**Objective.** A reader of chapter 24 finds, on every sentence that gives a number from a study or from the book's experiment, the note that says where that number comes from, so a number read alone is never left without its source, in both editions. Found by `m15-review` (work/done/m15-review.md, B22: "24:67-72: numbers with their note key only on the sentence before. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The scope is the chapter, not only B22's lines: the queue line says "chapter 24's numbers carry their note key at the claim", and m15-review files one line per file for what its candidates show. B22's lines (Skitka's results, Lee's counts) are the first occurrence; the experiment's sections have the same gap, its results keyed only on the sentence that introduces the experiment. Source: docs/06 (the line); work/done/m15-review.md (one line per file); docs/04 **Source notes** ("every number ... carries `[^<key>]` at the claim").
2. The rule the delivery applies, so the check is mechanical: a sentence carries a source's key when it states a number that source measured or counted (a result, a score, a time, a token count, a count of answers or sessions). A sentence that describes the study or the request (three tasks, three tabs, three runs per arm, a scale of 1 to 5, three pairs per arm in the limits) does not. Source: docs/04 **Source notes**; docs/05 §3 (each Behaviour line becomes a check).
3. Per-sentence keys follow the chapter's own precedent: the two consecutive Dell'Acqua sentences ("25.1% faster", "19 percentage points") each carry `[^dell-acqua-2026]`. A repeated key prints its note once in the PDF and the EPUB, so the reader pays one small mark per sentence and no extra note. Source: chapter 24 §Why the first answer feels final; docs/04 **Source notes** ("a source cited again in the chapter reuses the key").
4. The table of scores carries no key in a cell: the key goes on the sentence that introduces it ("Each pair, first and challenged, was scored blind ..."), the sentence that tells the reader what the table's numbers are. No chapter puts a key in a table today. Source: chapter 22's and chapter 5's tables (no key in a cell); docs/04 **Width of a block** (a cell stays short).
5. Lee's sentence "In the same survey, more confidence in AI went with less critical thinking ..." gives no number and no quotation, so it stays as it is; so do "Asked to test, the agents found ..." and "The challenged answers added ...", which report the run without a count. Source: docs/04 **Source notes** (numbers and quoted claims).
6. Key points stay unchanged: they restate the gain's figures ("about 3 to 9 times", "three pairs per arm"), and the gain's sentence already carries `[^ask-for-more-run]` at the claim. Source: docs/04 **One gain** (a key point carries at most the gain's number); chapter 24 §What the team gains.
7. Only markers are added: no word, number, heading or note definition changes. Source: the queue line; docs/04 **Numbers that prove** (the numbers already kept are the ones that prove).
8. No docs/03 term, no new queue line, no split: one chapter, one kind of edit, both editions. Source: docs/03 (no new concept); docs/05 §1.

**Behaviour.** In both editions of chapter 24 (`book/en/24-asking-for-more.md`, `book/pt/24-asking-for-more.md`), after /apply, each sentence below ends with the key named, placed after its closing punctuation as the chapter already does (`...of the time.[^sharma-2024]`). Sentences are named by their opening words; find them by text.

§Why the first answer feels final (pt §Por que a primeira resposta parece final):

* en "On the six events the aid did not flag, ..." / pt "Nos seis eventos que o auxílio não sinalizou, ...": `[^skitka-1999]`.
* en "When the aid recommended something wrong, on six occasions, ..." / pt "Quando o auxílio recomendou algo errado, em seis ocasiões, ...": `[^skitka-1999]`.
* en "Among what kept them from thinking critically about an answer, 44 ..." / pt "Entre o que os impediu de pensar criticamente sobre uma resposta, 44 ...": `[^lee-2025]`.

§What the agent does not propose (pt §O que o agente não propõe), each `[^ask-for-more-run]`:

* en "On the card task, one first answer said plainly ..." / pt "Na tarefa do card, uma primeira resposta disse com todas as letras ...".
* en "The three first answers wrote their summary in the chat, ..." / pt "As três primeiras respostas escreveram o resumo no chat, ...".
* en "Each first answer wrote one long guide for the agent without asking, ..." / pt "Cada primeira resposta escreveu um guia longo para o agente sem perguntar, ...".

§What the protocol bought, and what it cost (pt §O que o protocolo rendeu, e quanto custou), each `[^ask-for-more-run]`:

* en "Each pair, first and challenged, was scored blind ..." / pt "Cada par, primeira e desafiada, foi pontuado às cegas ...", the sentence before the table.
* en "The judge would have sent the challenged answer in all 9 pairs." / pt "O juiz teria enviado a resposta desafiada em todos os 9 pares.".
* en "With the three runs of each arm summed, ..." / pt "Somadas as três execuções de cada braço, ...".
* en "One session at a time, a first answer took 24 seconds ..." / pt "Uma sessão de cada vez, uma primeira resposta levou de 24 segundos ...".
* en "The experiment's nine challenged sessions, run within about 45 minutes ..." / pt "As nove sessões desafiadas do experimento, rodadas em cerca de 45 minutos ...".
* en "Five questions about the project, each in a fresh session, ..." / pt "Cinco perguntas sobre o projeto, cada uma numa sessão nova, ...".
* en "In each of the cost arm's three runs, the five questions took ..." / pt "Em cada uma das três execuções do braço do custo, as cinco perguntas levaram ...".

Checks a person runs, each per edition, counting citations with `grep -o '\[\^<key>\]' <file> | wc -l` (the count includes the note's definition line):

* `ask-for-more-run`: 13 (today 3); `skitka-1999`: 4 (today 2); `lee-2025`: 3 (today 2); `dell-acqua-2026` 4, `sharma-2024` 2, `simon-1956` 2, `mosier-manzey-2019` 2, unchanged.
* `git diff --word-diff` of each file shows only added `[^...]` markers; no word, number, heading, table row or note definition changed.
* `make verify` green, its parity check included (it compares each key's citations between the editions).
* Fails: one edition changed and not the other; a key in a table cell; a key on a sentence that only describes the study or the request (the "three tasks" sentence, the arms' descriptions, "Three pairs per arm"); a key point given a key; a different key on a sentence than the source of its number; any wording changed.

**Contract.**

* Files: `book/en/24-asking-for-more.md`, `book/pt/24-asking-for-more.md`; no other book file.
* Sections: §Why the first answer feels final (three markers), §What the agent does not propose (three), §What the protocol bought, and what it cost (seven). Headings, key points and note definitions unchanged.
* Terms of docs/03: none new. Sources: none added or removed; existing keys reused (`skitka-1999`, `lee-2025`, `ask-for-more-run`). Cases: none touched (the Case A card story has no number and is not edited).
* docs/00 to docs/05: no change. docs/06: this line `[>]` by the driver, `[*]` when /apply starts, `[x]` by /apply. No new queue line.

**Deliveries in flight on the same chapters.** No other queue line names chapter 24. Other sessions' pages and files in the tree are theirs (docs/05 §4); find passages by their words, not by line numbers.

**Out of scope.**

* Rewording any sentence or cutting any number: the finding is about where the key sits, not what the sentence says.
* The key points and the gain: the gain is keyed at its claim; key points restate it (decision 6).
* Sentences without a number from a source (decision 5).
* Other chapters with the same pattern: no finding names them.

**Done when.**

* [x] Both editions changed as Behaviour says; its counts give the results it names; the word diff shows only markers.
* [x] Chapter 24 still opens with its value, has its gain, no filler and nothing useful cut.
* [x] Every number sourced at its claim; `make verify` green, parity, width and disclosure scan included; no em dash.
* [x] No Case A or Case B passage changed, so no author approval under docs/00 OD-3 is needed.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Proof.**

* Thirteen markers added in each edition, at the sentences Behaviour names, found by their words; each sentence ended in a period with nothing after it, so the marker follows the period as the chapter's existing keys do.
* Counts per edition (`grep -o '\[\^<key>\]' <file> | wc -l`): `ask-for-more-run` 13, `skitka-1999` 4, `lee-2025` 3, `dell-acqua-2026` 4, `sharma-2024` 2, `simon-1956` 2, `mosier-manzey-2019` 2, as Behaviour names.
* `git diff --word-diff` of each file: 13 changed words, each a sentence's last word gaining its marker; no other word, number, heading, table row or note definition changed.
* `make verify` green: build, parity, em dash, prose, width, links and disclosure.
* `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`; in the text of each PDF, chapter 24's notes for Skitka, Lee, Dell'Acqua, Sharma and the experiment's record each print once.

**Divergences.** None.

**Omissions.** None.

**Review.** A read-only Opus agent read this delivery's diff against the page and docs/04: no finding on the book files (same 13 markers in both editions, each the right source, no key in a table cell, key point or describing sentence, no sourced number left without its key, no wording changed, no em dash). It found the queue line still `[*]` and its docs/06 hunk unstaged, which were this delivery's last step, not yet run when it read: the line is now `[x]` and its hunk staged.

```commit
docs(ch24-note-keys): key chapter 24's numbers at the claim

- Skitka's and Lee's results carry their note key on each sentence
- The experiment's results and costs carry its record's key each
- Both editions, markers only; each note still prints once

work/done/ch24-note-keys.md
```
