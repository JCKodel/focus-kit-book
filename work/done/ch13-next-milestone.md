# ch13-next-milestone

**Objective.** After chapter 13 the reader places a line the page did not ask for as chapter 11 says: in the current milestone only when a clause of its paragraph needs it, and otherwise under the next milestone, never right below the delivery because it is new. Found by `m19-review` (work/done/m19-review.md, B1: "`suspension-end`, which the page 'never asked for' and no clause of milestone 1's paragraph (ch11:44-46) needs, is placed below `return-book`, inside milestone 1"; B2: "'ask for it right below this delivery's line, so it is the next free line' places a line by recency, which ch11:106 and ch14:74 forbid").

**Behaviour.**

* Reading `lend-book`'s review in §`lend-book`, built, the reader sees `suspension-end` go under the next milestone, because milestone 1's paragraph promises that a suspended member is refused, not that the refusal says until when; `return-book` stays the next free line.
* Reading §Review the staged change, the reader learns that what the page did not ask becomes a `[ ]` line placed where its milestone's paragraph needs it, or under the next milestone, as chapter 11 says, because a line's place is its priority; and that the draft page, written in that conversation, keeps what the person saw for its `/propose`, so the definition still starts from what they remember.
* Reading the Key points, the reader finds the same rule: what the page did not ask becomes a line of the queue where its milestone's paragraph puts it, not "the queue's next line".
* Reading the Ninjobs sentence that closes the same paragraph, the reader learns that the rest went into the queue as lines, with no claim about where.
* Fails: either edition still says "below `return-book`" / "abaixo de `devolver-livro`" for `suspension-end`, "right below this delivery's line" / "logo abaixo da linha desta entrega", or "the queue's next line" / "na próxima linha da fila" in Key points; chapter 13 says whether chapter 11's milestone 2 already exists at that moment; one edition changed and not the other.
* No number, measurement or other meaning of the chapter changes; the `/apply` ending's "The queue's next free line is `return-book`" stays true.

**Contract.** Files: `book/en/13-apply.md` and `book/pt/13-apply.md`. Sentences located by content (line numbers move):

1. §`lend-book`, built: en "The page never asked for that, so it becomes the line `suspension-end`, placed in the queue below `return-book`, which stays the next free line." becomes, in substance, "The page never asked for that, and no clause of milestone 1's paragraph needs it: the paragraph promises the refusal, not its end date. So it becomes the line `suspension-end`, under the next milestone, created when there is none, as chapter 11 says, and `return-book` stays the next free line." pt "A página nunca pediu isso, então vira a linha `fim-da-suspensao`, posta na fila abaixo de `devolver-livro`, que continua sendo a próxima linha livre." becomes "A página nunca pediu isso, e nenhuma cláusula do parágrafo do marco 1 precisa disso: o parágrafo promete a recusa, não a data em que ela termina. Então vira a linha `fim-da-suspensao`, sob o próximo marco, criado quando não há nenhum, como o capítulo 11 diz, e `devolver-livro` continua sendo a próxima linha livre."
2. §Review the staged change: en "...; ask for it right below this delivery's line, so it is the next free line and its `/propose` starts from what you saw while you still remember it." becomes "...; it goes in this milestone when a clause of its paragraph needs it and under the next otherwise, as chapter 11 says, because its place is its priority; the draft page, written in this conversation, keeps what you saw while you still remember it, for its `/propose`." pt "...; peça a linha logo abaixo da linha desta entrega, para que ela seja a próxima linha livre e o `/propose` dela parta do que você viu enquanto ainda se lembra." becomes "...; ela vai neste marco quando uma cláusula do parágrafo dele precisa dela, e sob o próximo nos outros casos, como o capítulo 11 diz, porque o lugar dela é a sua prioridade; o rascunho da página, escrito nesta conversa, guarda o que você viu enquanto ainda se lembra, para o `/propose` dela."
3. The Ninjobs sentence right after it: en "... and the rest written as the next lines of the queue." becomes "... and the rest written as lines of the queue." pt "... e o resto escrito como as próximas linhas da fila." becomes "... e o resto escrito como linhas da fila."
4. Key points, the use-and-review point: en "make what the page did not ask the queue's next line" becomes "make what the page did not ask a line of the queue, where its milestone's paragraph puts it"; pt "transforme o que a página não pediu na próxima linha da fila" becomes "transforme o que a página não pediu em uma linha da fila, onde o parágrafo do seu marco a põe".

/apply may polish within these limits; nothing else in the chapter changes. Sources: chapter 11 §Milestones and §Changing the queue (the paragraph decides where a line goes; `due-date-format` under the next milestone), chapter 14 ("A line added later goes in the milestone whose paragraph needs it, never higher in the queue because it is new"), docs/05 §4 (the same rule), and docs/05 §2 (the draft holds what the line cannot). Terms of docs/03: milestone (marco), free line (linha livre), none new. Cases: the lending library, written for the chapter; Ninjobs by its author's account; no Case A or Case B passage, so OD-3 is inapplicable.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Chapter 13's line 24 and its `/apply` ending's "next free line": they name the first free line, which this change keeps. Chapter 11's milestone 2 paragraph: chapter 13 does not say whether `suspension-end` joins it. Chapters 11, 14 and 15: already say the rule. The review's own findings staying under the review (chapter 15): another case, not touched here.

**Decisions taken alone** (no person available, recommended answer taken). (1) Chapter 13 states the destination, "under the next milestone, created when there is none", and not whether chapter 11's milestone 2 exists at that moment of the example: the book's chapters do not fix a timeline between `due-date-format` and `lend-book`, and naming milestone 2 would put a suspension date under a paragraph about loan dates that does not answer it. (2) The "while you still remember" value is kept through the draft page chapter 11 already gives, written in the conversation where the person saw the problem, not through the line's position; the page claims nothing about which session runs that `/propose`, which docs/05 §2 leaves to the person. (3) Key point 7 and the Ninjobs sentence change too: the review named lines 130 and 174, but both echo the recency placement, and a key point repeating the old rule would leave the contradiction in place. The Ninjobs sentence only loses "next", so it claims nothing about where the author placed those lines.

**Done when.**

* [x] Both editions edited in the four places above, nothing else; each Behaviour line checked; the Fails phrases absent from `book/*/13-apply.md`.
* [x] The chapter still opens with its value and keeps its evidenced team gain; no filler and nothing useful cut; every number keeps its source; terms follow docs/03; no em dash.
* [x] No Case A or Case B passage changed or added, so OD-3 is inapplicable.
* [x] `make verify` green after the last edit; `make book` is run once by the batch driver at the end and gives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review.
* [x] No delivery review: the author waived it for this round; /apply does not add one.
* [x] Page archived to `work/done/` and commit message suggested.

**Record.**

* Built: both editions, the four places of the Contract, worded as it gives them; the §`lend-book`, built sentence split in two at its colon, one sentence a line.
* Proof: the Fails phrases are absent from `book/*/13-apply.md` (the `/apply` ending's "the queue's next line" at line 105 is out of scope and stays); chapter 13 does not name chapter 11's milestone 2; "`return-book` stays the next free line" kept.
* Divergences: none. Omissions: none.
* Delivery review: skipped on the author's word (2026-10-19).
* Decisions: those the page lists; no new one.
* `make verify`: green after the last edit.

```commit
docs(ch13-next-milestone): place unasked lines by milestone in ch 13

- en/pt: suspension-end goes under the next milestone; return-book
  stays the next free line
- review step and key point: an unasked line goes where its
  milestone's paragraph puts it, the draft keeps what you saw
- Ninjobs: the rest written as lines of the queue, no claim of where
```
