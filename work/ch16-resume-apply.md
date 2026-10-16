# ch16-resume-apply

**Objective.** After chapter 16 a reader knows where a `[?]` line with `resume: apply` goes back, said once and as docs/05 §4 says it: to `[>]`, or to `[ ]` with what `/propose` must settle when scope became undecided.

**Behaviour.**

* A reader of chapter 16 §Waiting finds the rule in one place: a line with `resume: apply` goes back to `[>]`; if scope became undecided, it goes back to `[ ]` instead, and the session says what `/propose` must settle.
* The same reader, at the key points, finds that a line leaves `[?]` by its resume phase and that `/propose` and `/apply` stop on a `[?]` line, with no second statement of where `resume: apply` returns and no condition ("only if its page is still complete") that docs/05 §4 does not have.
* A reader of chapter 15 §What `/apply` does finds that a `[?]` line waiting only on this delivery goes back by its resume phase, with the pointer to chapter 16, and no second account of where each phase returns.
* Failure: a reader who meets "back to `[>]` only if its page is still complete" in the key points and "back to `[>]`, and the person asks `/propose` for the page first" in the text takes two rules for one; after this delivery no sentence of chapters 15 or 16 says either.
* Edge: `resume: propose` keeps its sentence in §Waiting (back to `[ ]`, the draft stays); only the `resume: apply` rule changes.
* Edge: the sentence on how the phase is chosen (`propose` for a line that was `[ ]` or `[~]`, `apply` for `[>]` or `[*]`) stays where it is.

**Contract.**

The finding was re-checked, not taken on trust: chapter 16 en 92 says the line goes back to `[>]` and that the person asks `/propose` for the page first, where docs/05 §4 returns it to `[ ]`; en 134 says "only if its page is still complete", a condition docs/05 §4 does not have; chapter 15 en 64 gives the return to `[>]` with no exception. All three hold. The lines are as `renumber-chapters` and `method-said-once` will find them, so /apply finds each by its words.

* **Chapter 16, both editions, file name, title and headings kept.**
  1. §Waiting: `[?]`, "A line with `resume: apply` goes back to `[>]`; if the answer that freed it changed what its page must say, the person asks `/propose` for the page first, as with any page that no longer holds." becomes "A line with `resume: apply` goes back to `[>]`; if scope became undecided, it goes back to `[ ]` instead, and the session says what `/propose` must settle." (pt, line 93: "Uma linha com `resume: apply` volta para `[>]`; se o escopo ficou indefinido, volta para `[ ]` no lugar, e a sessão diz o que o `/propose` precisa decidir.")
  2. Key points, "`propose` back to `[ ]`, `apply` back to `[>]` only if its page is still complete;" becomes "by its resume phase;" with nothing in its place: "A line leaves `[?]` when the reason is resolved, by its resume phase; `/propose` and `/apply` stop on a `[?]` line, or one not free, until it is." (pt, line 135: "Uma linha sai de `[?]` quando o motivo se resolve, pela fase de retomada; o `/propose` e o `/apply` param em uma linha `[?]`, ou em uma que não está livre, até que esteja.")
  3. Nothing else in chapter 16 changes.
* **Chapter 15, both editions, line 64:** "goes back by its resume phase: to `[ ]` when it was `resume: propose`, to `[>]` when it was `resume: apply` ([chapter 16](16-queue-states.md))" becomes "goes back by its resume phase ([chapter 16](16-queue-states.md))". (pt: "volta pela fase de retomada ([capítulo 16](16-queue-states.md))".) The rest of the bullet is unchanged.
* **Terms:** waiting mark, resume suffix, as docs/03 has them; docs/03 unchanged (its waiting-mark row carries the same stale condition: `docs03-current-rows`).
* **Sources:** docs/05 §4 ("`resume: apply` to `[>]`. If scope became undecided, return `[ ]` and say what /propose must settle."), the book's own copy of the process the kit writes; no source note, as chapter 16 already cites docs/05 without one. The installed skills at 2026.10.16.2 hold no sentence on it: `/apply` only blocks with `resume: apply` as docs/05 §4 says.
* **Cases:** none. Code examples: none.

**Overlap with the deliveries in flight (docs/06 M15).**

* `method-said-once` (chapters 9 to 19): its list cuts "the parenthesis on `resume: apply`" from chapter 15 §What `/apply` does and shortens chapter 16 §Waiting and a sentence of §The next line. Chapter 15 line 64 is that parenthesis: this page makes the cut first, so when `method-said-once` runs (after `m14-review`) it finds that passage already done and leaves it. It must keep the one sentence of §Waiting on `resume: apply`, the owner of the rule.
* `one-gain-section` rewrites the key points of every chapter, chapter 16's included; it runs after `method-said-once`, so it starts from the key point as this page leaves it.
* `renumber-chapters` moves "chapter 16" and the file links by script; the pointer written here is an ordinary link and moves with it.
* `docs03-current-rows` changes docs/03 only, the same condition in its waiting-mark row; no chapter line is shared.
* `ch17-slot-none` touches chapter 17, not 15 or 16.

**Out of scope.**

* docs/03's waiting-mark row: `docs03-current-rows`.
* The cuts of chapters 15 and 16 beyond the lines above: `method-said-once`.
* The shape of the key points: `one-gain-section`.
* The `resume: propose` return and the choice of phase: unchanged.

**Done when.**

* [ ] Chapters 15 and 16 changed in both editions, same headings; each still opens with its value; no filler and nothing useful cut.
* [ ] `resume: apply` returns to `[>]`, or to `[ ]` when scope became undecided, stated once in chapter 16 §Waiting in both editions; no chapter 15 or 16 sentence has "only if its page is still complete" or the `/propose`-first clause (`grep` gives nothing in `book/`).
* [ ] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions in the review.**

* The rule is owned by chapter 16 §Waiting and stated there in docs/05 §4's words; chapter 15 and the key points keep a pointer or the phase only. Chosen alone, from the author's override ("say the rule once") and docs/04's No filler.
* Chapter 15 line 64 loses the `[ ]`/`[>]` mapping instead of gaining the exception: a third statement of the rule is the finding's cause, and chapter 16 is the first concrete occurrence (AGENTS.md, abstraction on the second occurrence). Chosen alone.
* The key point loses the mapping and the condition rather than repeating the exception, because the body states it two sentences above. Chosen alone.
* Pt "escopo ficou indefinido" for "scope became undecided", the word chapter 14 and the rest of the Portuguese edition use for scope ("o escopo ainda não foi entendido"); chosen alone.
* The finding holds as the review wrote it, with one addition from the author's override: chapter 15 line 64. Chosen from the override.
