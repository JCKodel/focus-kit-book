# ch12-14-parallel-token

**Objective.** After chapter 14, with the sentences of chapters 11, 12 and 13 that describe the same step, the reader, developer or not, can read the two letters a queue line may carry after its slug, `(PA)`, the parallel token: the first place speaks for `/propose`, the second for `/apply`; `P` says the definition takes nothing from the pages of the lines above, `A` that the build touches none of their files; a `-` in a place makes that command wait, for every line above to be `[>]` or beyond before `/propose` and `[x]` before `/apply`; `after` holds both commands, token or not; whoever changes the queue re-judges the tokens the change affects, `/propose` corrects one from its page, and a line without one is judged from the pages and docs/01 as before.

**Behaviour.** What the reader can do or explain after the chapters:

* Read the example queue of chapter 14 (Contract): `search-catalog (PA)` may be defined and built now, while `lend-book` is `[*]`; `renew-loan (P-)` may be talked through now, but `/apply renew-loan` waits until every line above it is `[x]`, `lend-book` and `search-catalog` included, since its build changes `src/features/loans/` as `lend-book`'s does.
* Say what `-` in the first place waits for, and that it is not forever: had `renew-loan` been `(--)`, its `/propose` would wait for `search-catalog`, still `[ ]`, to be `[>]`; `lend-book`, `[*]`, already counts as beyond `[>]`.
* Say that a token reads against every line above, not only the one it conflicts with: the `-` of `renew-loan` also waits for `search-catalog`, which touches none of its files.
* Edge: a line with `(PA)` and `· after lend-book` still waits for `lend-book` to be `[x]` before either command: the token says what may run alongside the lines above, never that a line it needs may be skipped.
* Edge: a line with no token is judged as chapter 14 already says, from the pages and docs/01: the free lines that touch different files.
* Edge: run `/apply renew-loan` on its finished page while `lend-book` is `[*]`: it says what the line waits on, leaves `[>]` as it is, and stops; nothing is marked `[?]`, since a token, like an `after`, is an order, not a wait.
* Edge: run `/propose` on a `(-A)` line while a line above it is `[~]`: it says what the line waits on and does not start.
* Who writes and fixes a token: whoever adds, moves or rewrites a line re-judges the tokens the change affects, since the lines above the lines below it changed; `/propose`, once its page says what it takes and which files its Contract touches, corrects the line's token and says so; `/brainstorm` writes the tokens of a first milestone that will run as several sessions.
* A person who does not code reads the letters as two permissions, one per command: "may I start talking it through now?" and "may I start building it now?".
* Find it in the key points: chapter 11's line bullet, chapter 12's `/propose` bullet, chapter 13's `[*]` bullet, chapter 14's free-line bullet.

**Contract.** Eight files, `book/en/` and `book/pt/` of `11-queue-and-milestones.md`, `12-propose.md`, `13-apply.md`, `14-queue-states.md`, the same change in both editions, one sentence per line as the chapters are laid out. Line numbers are en's today; pt's are named where they differ.

* Chapter 14, opening (:3): "and say which lines can run at the same time" gains "and read the two letters a line may carry that say it".
* Chapter 14, "Six marks" (:32): "and `/apply` builds it once every line its `after` names is `[x]`" gains "and its token lets it (below)".
* Chapter 14, "The next line, and which run together":
  * :80 (pt :81), a line added later: gains that whoever adds or moves a line re-judges the tokens of the lines below it, whose lines above changed (the new section below).
  * :84 (pt :85): "the free lines, and among them those that touch different files" becomes "the free lines, by their tokens where they carry one, else those that touch different files"; the rest stays; :85-87 stay.
  * After :87 (pt :87), before the chapter 19 pointer, new sentences and one block, in this order:
    1. A line can say it once, for everyone who reads the queue, with two letters in parentheses right after its slug, its parallel token, `(PA)`.
    2. The first place speaks for `/propose`, the second for `/apply`, and each says whether that command may run while the lines above are still in flight; the pt edition says the letters stay P and A because the commands keep their English names.
    3. `P`: the definition takes nothing from their pages, so it can be talked through now; `A`: the build touches none of their files, so it can be built now.
    4. A `-` in a place makes that command wait: in the first, until every line above is `[>]` or beyond; in the second, until every line above is `[x]`.
    5. `after` still holds both commands, token or not.
    6. The block, written for this chapter, within 74 columns:

       en:
       ```
       [x] members              the librarian registers and suspends members
       [*] lend-book            the librarian lends a copy
       [ ] search-catalog (PA)  a member searches the catalog
       [ ] renew-loan (P-)      a member renews a loan once
       ```
       pt:
       ```
       [x] membros                  o bibliotecário registra e suspende membros
       [*] emprestar-livro          o bibliotecário empresta um exemplar
       [ ] buscar-catalogo (PA)     um membro busca no catálogo
       [ ] renovar-emprestimo (P-)  um membro renova um empréstimo uma vez
       ```
    7. `search-catalog`'s page takes nothing from `lend-book`'s and its build lives in `src/features/catalog/`, so both commands may run on it now.
    8. `renew-loan` can be talked through now, its rule being its own, but its build changes `src/features/loans/`, as `lend-book`'s does, so `/apply renew-loan` waits until every line above it is `[x]`, `search-catalog` included, which touches none of its files: a token reads against every line above.
    9. Had it been `(--)`, its `/propose` would wait for `search-catalog`, still `[ ]`, to be `[>]`; `lend-book`, `[*]`, already passes.
    10. Whoever changes the queue re-judges the tokens the change affects; `/propose` corrects a line's token from its page, once it knows what the page takes and which files the Contract touches; `/brainstorm` writes them for a first milestone that will run as several sessions ([chapter 9](09-starting-a-project.md)); a line without one is judged from the pages, as above.
    11. `/propose` and `/apply` wait as the token says: `/apply renew-loan` on its finished page while `lend-book` is `[*]` says what it waits on, leaves `[>]` as it is, and stops.
  * :83 (pt :83), "`/propose` and `/apply` do not start a line that is not free": stays; sentence 11 follows it in meaning, placed after the block.
* Chapter 14, "What the team gains" (:180, pt :181): "the free lines and the files they touch answer it from the queue, without a meeting" becomes "the free lines, their tokens and the files they touch answer it from the queue, without a meeting, and the person who knows which pages a line takes from and which files it touches writes it once, on the line, for every session that reads it". No number.
* Chapter 14, "Key points", the free-line bullet (:185, pt :186): "and free lines that touch different files can run at the same time" becomes "and free lines run at the same time as their `(PA)` tokens say, `P` for `/propose` and `A` for `/apply`, `-` waiting for every line above to be `[>]` or beyond before `/propose` and `[x]` before `/apply`, `after` holding both; whoever changes the queue re-judges the tokens, `/propose` corrects one from its page, and a line without one runs beside those that touch different files", docs/03's `free line` and `parallel token`.
* Chapter 12, "What `/propose` does":
  * :26: after "on a line whose `after` names a line not yet `[x]`, it says the same and does not start", gains "and so on a line whose token has `-` first, `(-A)` or `(--)`, while a line above it is not yet `[>]` or beyond (chapter 14)".
  * :27: "it reads its own line and each line its `after` names" gains "and, when its token waits, every line above it"; the rest stays.
  * After :30 (pt :30), the `[>]` sentence, one new sentence: with the page written, it judges the line's token from it, what the page takes from the pages above and which files the Contract touches, and corrects the token on the line when it says otherwise, saying so (chapter 14).
  * Key points, the `/propose` bullet (:171, pt :180): "judges its line and its `after` off trunk" becomes "waits as its line's `after` and token say, judging them off trunk"; after "marks the line `[~]` there while it talks and `[>]` when the page is completely defined" gains "corrects the token from the page".
* Chapter 13, "What `/apply` reads" and the start:
  * :26: "it must see that the lines its `· after` names are done before it starts" gains "and, when its token has `-` second, that every line above it is `[x]`".
  * :28: "reads each line its `after` names" gains "and every line above it when its token waits"; the rest stays.
  * :32: "On a `[>]` line whose `after` names a line not yet `[x]`" becomes "On a `[>]` line whose `after` names a line not yet `[x]`, or whose token has `-` second, `(P-)` or `(--)`, while a line above it is not yet `[x]`"; "an `after` is an order, not a wait" becomes "an `after` or a token is an order, not a wait".
  * :33: "whose `after` lines are all `[x]`" gains "and whose token lets it build".
  * Key points, the marks bullet (:273, pt :273): "It marks the line `[*]` with its first edit" gains ", once the line's `after` and token let it build".
* Chapter 11, widened as siblings:
  * :16: "A line is the mark, the slug, one sentence of what the delivery gives, and its suffixes" becomes "the mark, the slug, its token when it has one, two letters that say what may run while the lines above it are in flight ([chapter 14](14-queue-states.md)), one sentence ..."; the block at :19 stays.
  * :179: "A move keeps the line's `· after`" gains "and re-judges its token and those of the lines below it, whose lines above changed (chapter 14)".
  * Key points, the docs/06 bullet (:191, pt :196): "a mark, a slug, one sentence and its suffixes" becomes "a mark, a slug, its token when it has one, one sentence and its suffixes".
* Portuguese: "token de paralelismo" (docs/03), never "marca", which is the mark's word; "linhas acima", "em andamento"; slugs `membros`, `emprestar-livro`, `buscar-catalogo`, `renovar-emprestimo`; folders `src/features/catalogo/` and `src/features/emprestimos/`, as pt chapter 14 :86-87 writes them.
* Terms of docs/03: parallel token, queue line, free line, mark, after. Rows exist since kit-2026-10-20-1; none to add.
* Sources: docs/05 §4 and the installed propose, apply and brainstorm skills at 2026.10.20.1; docs/03's `parallel token`, `queue line`, `free line` rows. No footnote: the reader gains nothing to open.
* Cases: none. No number, version, date or commit.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 8: `ch08-update-2026-10-20-1`, in parallel.
* Chapter 9 :23, :88 and :138, `/brainstorm`'s first milestone: silent on the token, not false; chapter 14's new sentence 10 says `/brainstorm` writes them, pointing to chapter 9.
* Chapter 7 :62, what docs/05 §4 owns: "what may run at the same time" covers the token; true as it stands.
* Chapter 19 :288, pages written at once do not read each other: true, it is `P`'s reason; two later lines touch chapter 19.
* Chapter 11's line template at :19: shows the shape with `· after`, both optional; the token is named in :16 instead.
* The kit's reason as a story, the sessions its changelog tells: the book teaches the kit as it is today, with no version or before and after.
* `after` over the token with its own example: a later line of the queue (chapter 14), which deepens what sentence 5 states.
* Tokens on this repository's own queue lines: the driver writes them.

**Neighbouring lines on the same files**, applied after this one in queue order: later deliveries of the queue's plan, on where each session opens (chapter 13), a command typed with several slugs (chapters 12, 13, 14) and `after` over the parallel token (chapter 14). This Contract is written against the files as they are today; chapter 14's new block moves its later lines down.

**The token of this line.** `(PA)` holds: above it, every line is `[x]` but `ch08-update-2026-10-20-1`, chapter 8's update example; this definition takes nothing from its page, and this build touches none of its files (chapters 11 to 14 and this page). No correction.

**Decisions from the documents.**

* The token's meaning, thresholds and who re-judges it: docs/05 §4 and docs/03 `parallel token`; "`[>]` or beyond", not the milestone paragraph's shorthand.
* `/propose` and `/apply` wait as the token says: the installed propose and apply skills at 2026.10.20.1.
* Taught as the kit is today, no version or number: AGENTS.md, the author's rule.
* Both editions in the same delivery: ADR-0004.

**Decisions taken alone.**

* Chapter 14 teaches the token whole; chapters 11, 12 and 13 say what their part does with it and cite chapter 14, as `after` is taught.
* Widened to chapter 11 :16, :179 and :191: the line's anatomy reads false without the token, docs/03's `queue line` and docs/06's header now including it, and a move changes what is above; no other line owns chapter 11. The queue line should name "chapters 11, 12, 13 and 14".
* Chapter 9 not widened: silent, not false.
* The example is a short block of its own, four lines, so each token reads against lines the reader sees; `lend-book`'s sentence shortened in both editions so pt fits 74 columns.
* `renew-loan` is `(P-)`, the hook chapter 14 :87 already gives; `(--)` taught in one sentence, to show `-` first waits for pages, not for builds.
* For a non-developer, each letter as a permission for one command, in Behaviour only; the chapter's sentences 2 and 3 carry it.
* No new number in "What the team gains": the kit's evidence is a project the book does not name, and the book teaches the kit as it is.
* At build: chapter 14's new sentences go after en :86 / pt :87, the last sentence before the chapter 19 pointer; the page's "after :87" for en names the pointer itself, and "before the chapter 19 pointer" decides it. They form a paragraph of their own, set apart by blank lines.
* At build: the block is introduced by one sentence, "The same library, in four lines written for this chapter", so the block says it was written for the chapter, as docs/04 asks of every example.
* At build: chapter 12's key point reads "`[>]` when the page is completely defined, correcting the token from the page, or `[?]` when the scope waits", a participle so the list of marks keeps its "or".
* At build: chapter 11 :179's pt sibling is pt :184, which the page did not name.
* At build: the pt sentence 2 clause reads "as letras ficam P e A porque os comandos mantêm os nomes em inglês", in the same sentence, so the editions keep line parity.

**Divergences.** One from the Contract: chapter 12 :26's "and so on" shipped as "and likewise", a Delivery review note taken (Delivery review). The Contract said "Ten files" for the eight it names, chapters 11 to 14 in two editions, as the queue line names them; `m25-records-claims` corrected the count.

**Omissions.** None.

**Proof.**

* `make verify` green (exit 0) after the last edit to the chapters.
* `make book` exit 0, run by this lane before its commit `395975a`, in the one tree it shared with `ch08-update-2026-10-20-1`, committed at `5a478e6`; whether that commit came before the build is not recorded. PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. `work/done/m25-review.md` records the build at `dae2358`, whose `book/` is as `395975a` left it, both lines' chapters included, with both paths.
* Verify's parity and width checks pass on all four chapters, the two new blocks included.

**Delivery review.** One read-only Opus agent read `git diff HEAD` of the eight chapter files, the whole of en chapter 14's changed section, this page, docs/03's `queue line`, `free line` and `parallel token` rows and docs/05 §4; docs/04 it did not read directly, taking its rules from the brief and this page. It found nothing that breaks the page, docs/04 or the text. It noted six wording preferences: en 12 :26 "and so on" could read as "etc." (taken: "and likewise"); pt 14 "esperar X estar" (taken: "esperar até", in the counterfactual and the key point); the token's apposition in chapter 11 :16, the clause order of chapter 14 :3, "whose token lets it build" on a line without a token, and the back-reference of "A line can say it once" (all the Contract's wording, kept). One item outside the page: the chapter 9 link for `/brainstorm` writing tokens leads to a chapter silent on them, which this page's Out of scope already holds as silent, not false; no new queue line. Whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.

**Done when.**

* [x] Each passage of the Contract changed, both editions written; no other sentence changed.
* [x] Each chapter still opens with its value; no filler and nothing useful cut.
* [x] No number added; no em dash, version, date or commit hash in a chapter; no private case used, so no approval owed.
* [x] The new blocks within 74 columns in both editions.
* [x] `make verify` green.
* [x] `make book` built both editions, with both PDF paths.
* [x] Delivery review by one read-only Opus agent, over `git diff HEAD` of the eight chapter files and this page (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here taken from the brief and this page; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.

```commit
docs(ch12-14-parallel-token): chapters 11 to 14 teach the (PA) token

- chapter 14: the token, what each letter lets run, what - waits for
- chapter 14: a four-line example and who re-judges a token
- chapters 12 and 13: /propose and /apply wait as the token says
- chapter 11: a line's token and a move re-judging the tokens below

work/done/ch12-14-parallel-token.md
```
