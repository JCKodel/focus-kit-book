# ch09-14-token-wording

**Objective.** After chapters 9, 11, 13 and 14 the reader, developer or not, reads the parallel token in one wording: `/brainstorm` writes it on the first milestone's lines when lines will run at the same time, as chapter 9 now shows; a change re-judges the tokens it affects, the moved line's own included; a `-` is a wait and an `after` an order, neither a `[?]`; chapter 11's line template carries the token; chapter 14's `renew-loan` example says what its block shows; and the Portuguese chapter 14 keeps one verb for the members line.

**Behaviour.** What the reader can do or explain after the chapters:

* Follow chapter 14's link for who writes the tokens to chapter 9 and find it there: the first milestone's lines carry their token when lines will run at the same time, in the kit's words (brainstorm step 6, SETUP.md §3 at the kit's `9be385a`, installed as `.claude/skills/brainstorm/SKILL.md` :40 to :43).
* Say which tokens a move re-judges: the moved line's own and those of the lines it passed, since those are the lines whose lines above changed; a line below both places keeps the same lines above and needs no new judgement. An added line: its own and those of the lines below it.
* Edge: move `renew-loan (P-)` from below `search-catalog` to above it: `search-catalog`'s token is re-judged, since `renew-loan` is now above it, and `renew-loan`'s, since `search-catalog` no longer is; `members`, above both places, is not.
* Tell apart what chapter 13 says stops `/apply`: an `after` is an order, a `-` is a wait, and neither marks the line `[?]`; the command says what it waits on and leaves the mark as it is.
* Read chapter 14's example without a mismatch: `/apply renew-loan`, once its page is finished and its line `[>]`, while `lend-book` is `[*]` and `search-catalog` `[ ]`, says it waits on both and stops; the block above it still shows the line as `[ ]`, before its definition.
* Read chapter 11's line template and see where the token goes, right after the slug, and that the sentence above says it is there only when the line has one.
* Read chapter 11's gloss of the token as speaking for the line's own two commands, not for "what may run" in general.
* In the Portuguese edition, read the members line in chapter 14's two blocks with the same verb, "cadastra", as chapter 11's.

**Contract.** Nine files: `book/en/` and `book/pt/` of `09-starting-a-project.md`, `11-queue-and-milestones.md`, `13-apply.md`, `14-queue-states.md`, and `docs/03-Domain.md`. Line numbers are at HEAD `7664d02`, en / pt where they differ. Each change replaces only the quoted words; the rest of each sentence stays.

* **C1, chapter 9, "`/brainstorm`: a new project", item 6** (:23):
  * en: "three to eight deliveries, one line each, in order, then its review" becomes "three to eight deliveries, one line each, in order, each with its parallel token, two letters saying whether it may run beside the lines above it, when lines will run at the same time ([chapter 14](14-queue-states.md)), then its review".
  * pt: "de três a oito entregas, uma linha cada, em ordem, e depois a revisão dele" becomes "de três a oito entregas, uma linha cada, em ordem, cada uma com o seu token de paralelismo, duas letras que dizem se ela pode rodar ao lado das linhas acima dela, quando linhas vão rodar ao mesmo tempo ([capítulo 14](14-queue-states.md)), e depois a revisão dele".
  * `/analyze`'s item 6 (:88) stays: the installed analyze skill names no token in its first-milestone item (`.claude/skills/analyze/SKILL.md` :48).
* **C1, chapter 14** (:105 / :106):
  * en: "`/brainstorm` writes them for a first milestone that will run as several sessions ([chapter 9](09-starting-a-project.md))" becomes "`/brainstorm` writes them on the first milestone's lines when lines will run at the same time ([chapter 9](09-starting-a-project.md))".
  * pt: "o `/brainstorm` os escreve para um primeiro marco que vai rodar como várias sessões ([capítulo 9](09-starting-a-project.md))" becomes "o `/brainstorm` os escreve nas linhas do primeiro marco quando linhas vão rodar ao mesmo tempo ([capítulo 9](09-starting-a-project.md))".
* **C1, docs/03, the `parallel token` row** (:117): "/brainstorm writes them for a milestone that will run in parallel" becomes "/brainstorm writes them on the first milestone's lines when lines will run at the same time"; the rest of the row stays. The row as /apply writes it:

  | parallel token | token de paralelismo | `(PA)`, `(P-)`, `(-A)`, `(--)` | Two letters after a queue line's slug saying whether its /propose and its /apply may run while the lines above it are in flight: `P`, the definition takes nothing from their pages; `A`, the build touches none of their files; `-` in either place waits, for every line above to be `[>]` or beyond before /propose and `[x]` before /apply; `after` holds for both commands, token or not; whoever changes the queue re-judges the tokens the change affects, /propose corrects one from the page, /brainstorm writes them on the first milestone's lines when lines will run at the same time, and a line without one is judged from the pages as before (docs/05 §4). |

* **C2, chapter 11, "Changing the queue"** (:179 / :184):
  * en: "re-judges its token and those of the lines below it, whose lines above changed (chapter 14)" becomes "re-judges the tokens the change affects, its own and those of the lines it passed, whose lines above changed (chapter 14)".
  * pt: "rejulga o token dela e os das linhas abaixo dela, cujas linhas acima mudaram (capítulo 14)" becomes "rejulga os tokens que a mudança afeta, o dela e os das linhas por onde ela passou, cujas linhas acima mudaram (capítulo 14)".
* **C2, chapter 14, "The next line, and which run together"** (:80 / :81):
  * en: "while whoever adds or moves a line re-judges the tokens of the lines below it, whose lines above changed (below)" becomes "while whoever adds or moves a line re-judges the tokens the change affects: an added line's own and those of the lines below it, a moved line's own and those of the lines it passed, the lines whose lines above changed (below)".
  * pt: "enquanto quem acrescenta ou move uma linha rejulga os tokens das linhas abaixo dela, cujas linhas acima mudaram (abaixo)" becomes "enquanto quem acrescenta ou move uma linha rejulga os tokens que a mudança afeta: o da linha acrescentada e os das linhas abaixo dela, o da linha movida e os das linhas por onde ela passou, as linhas cujas linhas acima mudaram (abaixo)".
* **C3, chapter 13, "What `/apply` does"** (:32):
  * en: "it does not start either, and leaves the mark as it is: an `after` or a token is an order, not a wait (chapter 14)" becomes "it does not start either, says what it waits on, and leaves the mark as it is: an `after` is an order and a `-` a wait, and neither marks the line `[?]` (chapter 14)".
  * pt: "ele também não começa, e deixa a marca como está: um `after` ou um token é uma ordem, não uma espera (capítulo 14)" becomes "ele também não começa, diz o que espera, e deixa a marca como está: um `after` é uma ordem e um `-` uma espera, e nenhum dos dois marca a linha como `[?]` (capítulo 14)".
* **C4, chapter 14** (:106 / :107):
  * en: "`/apply renew-loan` on its finished page while `lend-book` is `[*]` says what it waits on, leaves `[>]` as it is, and stops" becomes "once `renew-loan`'s page is finished and its line `[>]`, `/apply renew-loan` while `lend-book` is `[*]` and `search-catalog` `[ ]` says it waits on both, leaves the mark as it is, and stops".
  * pt: "`/apply renovar-emprestimo` na página pronta dela com `emprestar-livro` em `[*]` diz o que espera, deixa o `[>]` como está, e para" becomes "quando a página de `renovar-emprestimo` está pronta e a linha dela em `[>]`, `/apply renovar-emprestimo` com `emprestar-livro` em `[*]` e `buscar-catalogo` em `[ ]` diz que espera as duas, deixa a marca como está, e para".
  * The block (:95 to :100 / :96 to :101) stays: :101 to :104 reason from `renew-loan` at `[ ]`.
* **C7, pt chapter 14's block** (:97): "o bibliotecário registra e suspende membros" becomes "o bibliotecário cadastra e suspende membros", as :40 and chapter 11 :54 say; same length, so the block's columns stay.
* **C8, chapter 11, "The line", the template** (:19):
  * en: `[ ] <slug>    <what it delivers, one sentence> · after <slug>` becomes `[ ] <slug> (PA)  <what it delivers, one sentence> · after <slug>`.
  * pt: `[ ] <slug>  <o que ela entrega, uma frase> · after <slug>` becomes `[ ] <slug> (PA)  <o que ela entrega, uma frase> · after <slug>`.
* **C9, chapter 11, "The line"** (:16):
  * en: "two letters that say what may run while the lines above it are in flight" becomes "two letters that say whether its `/propose` and its `/apply` may run while the lines above it are in flight".
  * pt: "duas letras que dizem o que pode rodar enquanto as linhas acima dela estão em andamento" becomes "duas letras que dizem se o `/propose` e o `/apply` dela podem rodar enquanto as linhas acima dela estão em andamento".

Terms of docs/03 used: `parallel token`, `dependency`, `waiting mark`, `free line`; none new. Sources: none new; the chapters cite no number here. Cases: none; every example is the lending library's, written for chapters 11 and 14, as they say.

Neighbours: `ch08-23-branch-read` changes chapter 13 :28 and chapter 14 :62, :64 and :193 (and chapters 8, 12, 17 to 20, 23); this line changes chapter 13 :32 and chapter 14 :80, :97 (pt), :105 and :106, so no line is shared, and it is applied after this one, against these files as this delivery leaves them. `m25-records-claims` changes records only.

**States.** Inapplicable: a chapter, no screen.

**Visual reference.** Inapplicable: no figure; the two PDFs of `make book` are the review copy.

**Out of scope.**

* Chapter 12 :172 ("worktree or branch"): `ch08-23-branch-read`'s (C22).
* Chapter 14's key points (:206 / :207), whose "re-judges the tokens" is shorter but not wrong, and chapter 12's: no finding names them.
* docs/03's `dependency` row (:114), "an order, not a wait", and chapter 11 :88 and :194, which say it of `after` alone: true as written; C3's fault is chapter 13 saying it of the token too.
* docs/05 §4: the kit's template words, not this project's to reword (C18, latent).
* The latent and weak candidates of m25-review (C10, C17, C18): dropped there.
* Chapter 9 :88, `/analyze`: its skill writes no token.

**Decisions from the documents.**

* Who writes the tokens, and when, in the kit's words: brainstorm step 6, "with the `(PA)` token of docs/05 §4 when lines will run at the same time" (installed skill, 2026.10.20.1 at `9be385a`), over docs/03's "a milestone that will run in parallel" and chapter 14's "a first milestone that will run as several sessions"; docs/03's row follows the kit (docs/03 is this project's, the skill the kit's).
* "The tokens the change affects" is docs/05 §4's and docs/03's phrase; the add and move cases spell it out by "the lines above it", the token's own measure (docs/03 `parallel token`).
* "`-` waits" is docs/03's and docs/05 §4's; "an order, not a wait, and the line keeps its mark" is docs/03's `dependency` row; chapter 13 now says each of its own thing.
* The token `(PA)` holds: every line above in M25 is `[x]`, so the definition takes nothing from a page in flight and the build touches no file of one (docs/05 §4); no correction. The neighbour `ch08-23-branch-read (P-)` waits on this line's `[x]` to build.

**Decisions taken alone** (the batch's driver asked for recommended answers; correct them in the review).

* C4 is fixed in the sentence, not the block: the block shows the queue before any definition, and :101 to :104 reason from it; the sentence names both lines the wait is on, as :103 says a token reads against every line above.
* C8's template shows `(PA)` itself rather than a `<token>` placeholder, so the reader sees the token's shape; the sentence above says it is there only when the line has one.
* Chapter 9 glosses the token in one clause where it first appears, since the reader meets it there before chapter 11 or 14 (memory: explain the basics first), and links chapter 14, which teaches it.
* Chapter 13 :32 gains "says what it waits on", which chapter 14 :106 and m25-review's clause 4 already say of `/apply`; it adds no rule.

**Done when.**

* [ ] Every change of the Contract made in both editions, and docs/03's row as written above; nothing else in those files changed.
* [ ] Each chapter still opens with its value; no filler and nothing useful cut; no number added; no em dash.
* [ ] `make verify` green.
* [ ] `make book` run after the last edit, with its commit and both PDF paths recorded in the Proof: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* [ ] The Delivery review (docs/05 §5) read the changes against this page and docs/04, its reader and whether it kept the session's advisor recorded.
