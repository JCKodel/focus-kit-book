# pt-blocked-term

**Objective.** After this delivery the Portuguese reader meets one word, "travado", for a blocked line, delivery or `/apply` in every chapter, and docs/03 gives that word, so a later chapter cannot drift back to "bloqueado". Found by `m19-review` (work/done/m19-review.md, A4: chapter 8's "uma entrega bloqueada"; C5: chapter 17's "qual linha da fila está bloqueada" against the same chapter's "travado são as linhas `[?]`" and "O que está travado"; E7: docs/03 has no Portuguese word for a blocked line or `/apply`).

**Behaviour.**

* Reading chapter 8's update report, item 2, and the paragraph that explains it, the Portuguese reader finds "os commits que uma entrega travada já fez no seu branch", the word chapters 13 and 19 use for the same partial work.
* Reading chapter 17's paragraph on the second of the lending library's tables, the reader finds "qual linha da fila está travada", as the same chapter says "travado são as linhas `[?]`" and asks "O que está travado, e esperando o quê?".
* Opening docs/03, a writer finds a row `blocked | travado` saying the word covers a `[?]` line, its delivery and an `/apply` that stopped on it, and that the Portuguese edition never says "bloqueado" for it.
* `grep -n -i "bloquead" book/pt/*.md` prints nothing afterwards; chapter 21's "desbloqueia" is another word and stays.
* The English edition does not change: it says "blocked" throughout.
* No number, measurement or meaning of any chapter changes.

**Contract.**

* `book/pt/08-install-and-hosts.md`, two sentences located by content: in the fenced update report, item 2 ("docs/05, §5 Delivery review"), "os commits que uma entrega bloqueada já fez no" becomes "os commits que uma entrega travada já fez no" (the report is the book's translation and paraphrase of the kit's report, which the chapter says before the block, so the word is the book's; the line gets shorter and stays inside the block's width); in the paragraph "O item 2 faz a revisão ler a entrega inteira contra o último commit: ...", "os commits que uma entrega bloqueada já fez no seu branch" becomes "os commits que uma entrega travada já fez no seu branch".
* `book/pt/17-project-as-assistant.md`, one sentence: "A segunda diz qual linha da fila está bloqueada, por quem, e há quanto tempo, ..." becomes "A segunda diz qual linha da fila está travada, por quem, e há quanto tempo, ..."; the rest stays.
* `docs/03-Domain.md`, a new row placed after `blocked reason`, in substance:

      | blocked | travado | none | Said of a line marked `[?]`, of its delivery and of an /apply that stopped on it: waiting on its blocked reason; in Portuguese "travado", agreeing with its noun ("uma linha travada", "uma entrega travada"), never "bloqueado". |

  Its own row and not a change to `waiting mark`, whose Portuguese, "marca de espera", names the mark, not the state.

English counterparts, unchanged: chapter 8 "the commits a blocked delivery already made on its branch" (report and paragraph), chapter 17 "which queue line is blocked". Sources: chapters 13, 14, 17 and 19 in Portuguese, which already say "travado"; ch13-scope-question-term's decision (2), which left the book-wide word to this line. Cases: chapter 17's passage explains the lending library's tables, written for that chapter; no Case A or Case B passage changes, so the author's OD-3 approval is inapplicable.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Chapter 21's "desbloqueia": another meaning. Chapter 14's "travada", "travado" and the board's "TRAVADA" label: already the word. docs/03's `delivery review` and `waiting mark` rows: their English says "blocked", their Portuguese terms do not involve the word. The English edition: already consistent (ADR-0004: English is the source).

**Decisions taken alone** (no person available, recommended answer taken). (1) docs/03 gets a new row rather than a clause in `waiting mark`: docs/03 says the Portuguese term is fixed per term, and "blocked" is the word the chapters use, not the mark's name. (2) The report line in chapter 8 changes too: docs/04 has the Portuguese edition show an English prose artifact translated, and the chapter says this report is shortened, paraphrased and translated, so the translation's word follows docs/03. (3) The feminine "travada" where the noun is "linha" or "entrega", as chapter 14 already writes.

**Done when.**

* [ ] The three sentences and the docs/03 row above edited, nothing else; each Behaviour line checked; `grep -n -i "bloquead" book/pt/*.md` prints nothing.
* [ ] `book/en/` unchanged, and the page says why (ADR-0004: English is the source and already says "blocked").
* [ ] The chapters still open with their value and keep their evidenced team gain; no filler and nothing useful cut; every number keeps its source; no em dash.
* [ ] No Case A or Case B passage changed or added, so OD-3 is inapplicable.
* [ ] `make verify` green after the last edit; `make book` is run once by the batch driver at the end and gives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review.
* [ ] No delivery review: the author waived it for this round; /apply does not add one.
* [ ] Page archived to `work/done/` and commit message suggested.
