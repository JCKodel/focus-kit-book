# m38-fixes

Defined before the author read it: the author's word for this run, relayed by the session that runs the queue on the author's behalf on 2026-11-13, is "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão" (close every open line of docs/06 without supervision), and for the reviews "Todas, médios entram" (every medium finding enters the one fixes line). So each question the documents leave open is answered by the agent's recommendation, marked "decided by the agent, the author corrects it in the review" (docs/05 §4, a command that says to decide alone).

**Objective.** After this delivery the reader of chapters 5 to 21 meets one definition of a grave finding, one account of who runs the slow tests, a suspended member's broken refusal that says how it broke, a key point that gives a finding something to carry it rather than always a line, and a quick guide that names the mark `/apply`'s last message opens with; and the reader of the PDF, in both editions, sees `🚨`, `⚠️` and `✅` drawn in their place on the line, with a word beside each.

**Behaviour.** What the reader can do or explain afterwards, one group per medium finding of `work/done/m38-review.md` (its numbering, M1 to M6):

* M1 (grave). From chapter 11, 14 or 15 alone, or docs/03's `finding` row, and from chapter 13 by its pointer to chapter 11's four tests, say the four tests of a grave finding: it breaks a clause of the milestone's paragraph for a person on its usual path, loses or exposes data, leaves verify red, or is a fix a delivery in flight cannot go on without.
* M1, failure: asked "chapter 13 says chapter 11 has three tests and chapter 14 has four; which is it?", the reader finds four everywhere; no "three tests" / "três testes" is left in `book/`.
* M1, edge: chapter 8's quoted migration report (en :72 to :74 / pt :73 to :75), a shortened record of one template sentence, keeps its words; it is a quotation, not the book's definition.
* M2 (marks in the PDF). Open either PDF at any page with a mark (chapter 10's step 6, chapter 13's last-message bullet, its example's last message and the sentence under it, its key point, chapter 14's output block and key point 3): each `🚨`, `⚠️` and `✅` sits on the baseline of its own line, at the size of the text around it, in colour, with no gap where it should be and no glyph above the line; inside a code block it starts its line.
* M2, words: at chapter 13 :193 and in key point :336 each mark has its word beside it, as :139 already gives them (siren, warning sign, check mark / sirene, sinal de aviso, sinal de visto), so a reader whose copy draws no glyph still reads which mark it is.
* M2, failure: the PDF embeds no font from the machine that built it: `pdffonts` on each PDF lists only Merriweather, Instrument Serif, Iosevka Term and Noto Color Emoji; Apple Color Emoji, the fallback today, is absent.
* M2, edge: the pages move nowhere they should not: both PDFs keep their page counts within what the text edits of M1 and M3 to M6 add (267 / 280 at HEAD; the scratch build of the CSS fix alone gave 267 / 280), and each edition's contents still fits one page (the build fails otherwise).
* M2, edge: the site and the EPUB are unchanged by the toolchain change (the site already draws the marks in place; the EPUB carries no fonts, docs/01).
* M3 (slow tests). From chapter 5 alone, say that verify has a ceiling, five minutes unless the team says otherwise; that each delivery runs the slow tests that cover what it changed; that the review closing the milestone runs them all and, when verify ran past its ceiling, says which tests go to the slow ones; and that a slow test failing there keeps the milestone open.
* M3, in passing: chapter 7's summary of the Verify slot and chapter 15's sentence on the slow tests say the same, in a clause each (small 7 and small 8 of the review, met by choice, below).
* M4 (`fix-suspended`). From chapter 14's "A line from a finding" alone, say how a member chapter 13 shows refused by a tested rule can still borrow: `lend` refuses a member whose `suspended` is true, as its tests prove with a member built that way, but suspending a member from the members screen records the suspension in another field, which `findMember` does not read.
* M4, failure: asked "chapter 13 tested the refusal; how can chapter 14 find it broken?", the reader answers from :201 / :203 alone: the tests built their suspended member, and the real suspension never reaches the rule; chapter 13 (:151, :165 to :167, :178, :189) is unchanged and still true: the rule refuses, the note says the refusal does not tell until when.
* M5 (chapter 21). Chapter 21's last key point tells the reader to give every finding something that carries it, a line when grave and a note otherwise, never every finding a line.
* M5, edge: the Case B story at :89 keeps its words; the key point is the general lesson, and docs/00 says Case B did not run on the process.
* M6 (quick guide). From chapter 10's step 6 alone, say what `/apply`'s last message opens with: `🚨`, a siren, for a new line or a flaw that blocked the delivery, `⚠️`, a warning sign, for a note, or `✅`, a check mark, for neither; the rest of step 6, as `m37-fixes` left it, unchanged.
* In the Portuguese edition, the same, with docs/03's terms and chapter 13's words for the marks.

**Contract.** Line numbers en / pt at `06f0119`, where m38-review read them, the same at HEAD `8867b24` (`git diff 06f0119 HEAD -- book/ pandoc/` is empty). Each change quotes the sentence it replaces, so a drift is found by the sentence; pt follows en sentence for sentence. The wording below is the agent's proposal; /apply may word it otherwise within what each item says, as long as each sentence stays true against the passages Behaviour names.

*M1, grave told with four tests.* The fourth test is docs/05 §4 :123 to :124's "So is a fix a delivery in flight cannot go on without", which focus-kit 2026.11.13 keeps word for word (`SETUP.md` :857 to :858 of the kit), and chapter 14 en :205 / pt :207's words for it.

* `book/{en,pt}/11-queue-and-milestones.md` en :98 / pt :101.
  * Replaced: "Each grave one, which breaks a clause of the paragraph for a person on its usual path, loses or exposes data, or leaves verify red, becomes a `[ ]` line of its own." / "Cada achado grave, que quebra uma cláusula do parágrafo para uma pessoa no seu caminho habitual, perde ou expõe dados, ou deixa a verificação vermelha, vira uma linha `[ ]` própria."
  * Proposed: "Each grave one, which breaks a clause of the paragraph for a person on its usual path, loses or exposes data, leaves verify red, or is a fix a delivery in flight cannot go on without, becomes a `[ ]` line of its own." / "Cada achado grave, que quebra uma cláusula do parágrafo para uma pessoa no seu caminho habitual, perde ou expõe dados, deixa a verificação vermelha, ou é uma correção sem a qual uma entrega em andamento não consegue seguir, vira uma linha `[ ]` própria."
* `book/{en,pt}/13-apply.md` :116 / :116.
  * Replaced: "A finding that is grave, by chapter 11's three tests, becomes" / "Um achado grave, pelos três testes do capítulo 11, vira".
  * Proposed: "A finding that is grave, by chapter 11's four tests, becomes" / "Um achado grave, pelos quatro testes do capítulo 11, vira". The rest of the sentence stays.
* `book/{en,pt}/15-closing-a-milestone.md` en :133 / pt :136.
  * Replaced: "A grave one breaks a clause of the paragraph for a person on its usual path, loses or exposes data, or leaves verify red, and becomes a `[ ]` line of its own." / "Um grave quebra uma cláusula do parágrafo para uma pessoa no seu caminho habitual, perde ou expõe dados, ou deixa a verificação vermelha, e vira uma linha `[ ]` própria."
  * Proposed: "A grave one breaks a clause of the paragraph for a person on its usual path, loses or exposes data, leaves verify red, or is a fix a delivery in flight cannot go on without, and becomes a `[ ]` line of its own." / "Um grave quebra uma cláusula do parágrafo para uma pessoa no seu caminho habitual, perde ou expõe dados, deixa a verificação vermelha, ou é uma correção sem a qual uma entrega em andamento não consegue seguir, e vira uma linha `[ ]` própria."
* `docs/03-Domain.md` :36, the `finding` row's definition column.
  * Replaced: "A grave one, in Portuguese grave, breaks a clause of the milestone's paragraph on a person's usual path, loses or exposes data, or leaves verify red, and becomes a `[ ]` line ending `· from <slug>`".
  * Proposed: "A grave one, in Portuguese grave, breaks a clause of the milestone's paragraph on a person's usual path, loses or exposes data, leaves verify red, or is a fix a delivery in flight cannot go on without, and becomes a `[ ]` line ending `· from <slug>`".
  * docs/03 is also changed by `kit-2026-11-13`, being built now, which migrates docs/03, docs/05, docs/06, AGENTS.md and ADR-0018. /apply runs after that delivery is committed, reads docs/03 then, and finds the row by the quoted sentence; if the migration already gave the row four tests, this bullet is done and /apply says so.

*M2, the marks in the PDF.* A toolchain change, plus two chapter sentences.

* The cause, found on this machine on 2026-11-14 with a scratch page and a scratch copy of the repository built by `scripts/build_book.py`, never in the tree. No font `pandoc/pdf.css` names holds `🚨` (U+1F6A8), `⚠️` (U+26A0 U+FE0F) or `✅` (U+2705), so weasyprint 69.0 (Pango and fontconfig) falls back to the machine's colour emoji font, here Apple Color Emoji: `pdffonts` on today's `output/*.pdf` lists `Apple-Color-Emoji` beside the repository's families. That font holds only `sbix` bitmaps (strikes 160 to 20 ppem, 800 units per em), and weasyprint draws the bitmap at about half the em, anchored above the baseline and to the right of the glyph's advance, which stays empty: the gap. It happens in Merriweather and in Iosevka Term, in a paragraph and in a `pre` block, at 9pt and at 20pt, and with the family named explicitly. It is not line height nor vertical alignment: `vertical-align: -0.4em`, `line-height: 1`, `display: inline-block` and `font-size: 2em` on the mark's `code` each left the bitmap where it was, relative to its box. A colour font with an `SVG ` table is drawn in place: the subset of Noto Color Emoji below drew each mark on its baseline, at text size, in colour, in both PDFs, at every place listed in Behaviour; the same subset without its `SVG ` table drew nothing, so weasyprint draws the `SVG ` glyphs and the table must stay. Two other fonts, Noto Emoji (monochrome) and Twemoji Mozilla (COLRv0, no `SVG ` table), named in a `@font-face` the same way, left the marks to Apple Color Emoji (`pdffonts` lists it, not them), drawn as before.
* `pandoc/fonts/NotoColorEmoji-Regular.ttf`, new: Noto Color Emoji 2.055, from `ofl/notocoloremoji/NotoColorEmoji-Regular.ttf` of `github.com/google/fonts` at commit `142c8963e7606b510c93a644c82a4c4cdeae6ef9` (sha256 of the source `4d82a18d8d95f60ba883ce242bbadbf84a576e987745dd7ba38d71c67cff2d73`, 25,332,736 bytes), cut to the three marks with fontTools 4.63.0, the one weasyprint 69.0 installs: `python3 -m fontTools.subset NotoColorEmoji-Regular.ttf --unicodes="U+1F6A8,U+26A0,U+2705,U+FE0F" --layout-features='*' --output-file=pandoc/fonts/NotoColorEmoji-Regular.ttf`. On this machine it gave 36,880 bytes, sha256 `edb0de71a1f014bc12219223114f7ed8d457a387e5d542ad04f3477932e68955`, with the tables `COLR`, `CPAL`, `GSUB`, `OS/2`, `SVG `, `cmap`, `glyf`, `head`, `hhea`, `hmtx`, `loca`, `maxp`, `name`, `post`, `vhea`, `vmtx`. A different size or hash with the same tables is no failure; a missing `SVG ` table is.
* `pandoc/fonts/NotoColorEmoji-OFL.txt`, new: the `OFL.txt` beside the source in the same directory and commit of `google/fonts` ("Copyright 2021 Google Inc. All Rights Reserved.", SIL Open Font License 1.1, no Reserved Font Name), so a subset may keep the name.
* `pandoc/pdf.css`, three changes, the ones the scratch build proved:
  * After the Iosevka Term `@font-face` (:10): `@font-face { font-family: "Noto Color Emoji"; src: url("fonts/NotoColorEmoji-Regular.ttf"); }`.
  * `html` (:56): `font-family: "Merriweather";` becomes `font-family: "Merriweather", "Noto Color Emoji";`.
  * `code, pre` (:89): `font-family: "Iosevka Term";` becomes `font-family: "Iosevka Term", "Noto Color Emoji";`.
  * The comment at the top, or one beside the `@font-face`, says in one line why: the marks fall to the machine's emoji font otherwise, whose bitmaps weasyprint draws above their place. No other rule changes; headings and the running head hold no mark today, and a family list there is not added for a mark that does not exist (Out of scope).
* `docs/01-Architecture.md`, the document that owns the build (AGENTS.md: a delivery that changes behaviour updates the document that owns it): :13's PDF row, after "Iosevka Term (code)", adds the marks `🚨`, `⚠️` and `✅` in Noto Color Emoji, cut to those three, after each family; :42's `pandoc/pdf.css` row says the same in its list; :44's `pandoc/fonts/` row adds "Noto Color Emoji (the three marks only, its `SVG ` table kept, which weasyprint draws)". Every mark in docs/01 stays inside inline code.
* `README.md` :48 and `README.pt.md` :48, the licence table: the fonts' row names Noto Color Emoji after Iosevka Term, same licence and file pattern. The family's name only, no glyph in either README (the prose rule `emoji` reads the READMEs).
* `book/{en,pt}/13-apply.md` :193 / :193, the sentence under the example's last message.
  * Replaced: "so the message opens with `⚠️` and no `✅`," / "então a mensagem abre com `⚠️` e não com `✅`,".
  * Proposed: "so the message opens with `⚠️`, the warning sign, and no `✅`, the check mark," / "então a mensagem abre com `⚠️`, o sinal de aviso, e não com `✅`, o sinal de visto,".
* `book/{en,pt}/13-apply.md` :336 / :336, key point 4.
  * Replaced: "Its last message opens with `🚨`, `⚠️` or `✅`, for what the delivery left;" / "A sua última mensagem abre com `🚨`, `⚠️` ou `✅`, pelo que a entrega deixou;".
  * Proposed: "Its last message opens with a siren, a warning sign or a check mark, `🚨`, `⚠️` or `✅`, for what the delivery left;" / "A sua última mensagem abre com uma sirene, um sinal de aviso ou um sinal de visto, `🚨`, `⚠️` ou `✅`, pelo que a entrega deixou;".
  * The words are :139's own ("a siren", "a warning sign", "a check mark" / "uma sirene", "um sinal de aviso", "um sinal de visto"). Every mark stays in inline code: docs/04's prose rule `emoji` masks code and flags a bare one.

*M3, the slow tests in chapter 5.* Chapter 13 :81 to :87 owns the why; chapter 5 introduces the slow tests and now tells who runs them.

* `book/{en,pt}/05-testing-each-piece.md` :39 / :39.
  * Replaced: "and you decide what it runs." / "e você decide o que ele roda."
  * Proposed: "and you decide what it runs and its ceiling, how long it may take, five minutes unless you say otherwise." / "e você decide o que ele roda e o teto dele, quanto tempo ele pode levar, cinco minutos se você não disser outro."
* `book/{en,pt}/05-testing-each-piece.md` :41 / :41.
  * Replaced: "A milestone is a group of deliveries with a paragraph saying what is true when it closes, and the review that closes it runs those slow tests; one that fails keeps the milestone open until its fix is done." / "Um marco é um grupo de entregas com um parágrafo que diz o que é verdade quando ele fecha, e a revisão que o fecha roda esses testes lentos; um que falha deixa o marco aberto até a correção dele estar pronta."
  * Proposed, two sentences: "A milestone is a group of deliveries with a paragraph saying what is true when it closes; each delivery runs the slow tests that cover what it changed, so a break shows in the delivery that made it, and the review that closes the milestone runs them all and, when verify ran past its ceiling, says which tests go to the slow ones (chapter 13). A slow test that fails at that review keeps the milestone open until its fix is done." / "Um marco é um grupo de entregas com um parágrafo que diz o que é verdade quando ele fecha; cada entrega roda os testes lentos que cobrem o que ela mudou, para que uma quebra apareça na entrega que a causou, e a revisão que fecha o marco roda todos eles e, quando a verificação passou do teto, diz quais testes vão para os lentos (capítulo 13). Um teste lento que falha nessa revisão deixa o marco aberto até a correção dele estar pronta."
* `book/{en,pt}/07-the-documents.md` en :45 / pt :46, small 7 met in passing.
  * Replaced: "the command that verifies a delivery, with the command of any slow tests kept out of it for the milestone review," / "o comando que faz a verificação de uma entrega, com o comando dos testes lentos que ficam fora dele para a revisão de marco, se houver,".
  * Proposed: "the command that verifies a delivery and its ceiling, with the command of any slow tests kept out of it, each run by the delivery that changes what it covers and all by the milestone review," / "o comando que faz a verificação de uma entrega e o teto dele, com o comando dos testes lentos que ficam fora dele, se houver, cada um rodado pela entrega que muda o que ele cobre e todos pela revisão de marco,".
* `book/{en,pt}/15-closing-a-milestone.md` :21 / :21, small 8 met in passing.
  * Replaced: "a failing one is a finding, graded like the others (below)." / "um que falha é um achado, classificado como os outros (abaixo)."
  * Proposed: "a failing one is a finding, graded like the others (below); and when a delivery noted verify over its ceiling, the review says which tests go to the slow ones." / "um que falha é um achado, classificado como os outros (abaixo); e quando uma entrega anotou a verificação acima do teto, a revisão diz quais testes vão para os lentos."

*M4, how a tested refusal broke.* One clause at chapter 14's first example of a finding; chapter 13 unchanged.

* `book/{en,pt}/14-queue-states.md` en :201 / pt :203.
  * Replaced: "finds that a suspended member can still borrow." / "descobre que um membro suspenso ainda consegue pegar um livro emprestado."
  * Proposed: "finds that a member suspended from the members screen can still borrow: `lend` refuses a member whose `suspended` is true, as its tests prove with a member built that way, but suspending a member from that screen records it in another field, which `findMember` does not read." / "descobre que um membro suspenso pela tela de membros ainda consegue pegar um livro emprestado: `emprestar` recusa um membro cujo `suspenso` é verdadeiro, como os testes dela provam com um membro construído assim, mas suspender um membro por essa tela registra isso em outro campo, que `buscarMembro` não lê."
  * Why it holds against the earlier chapters, checked by a sweep of "suspend" (en) and "suspens" (pt) over chapters 3 to 14: chapter 5 :88 and :126 build the member as data, `{ id: "m1", overdue: 0, suspended: false }` / `{ id: "m1", emAtraso: 0, suspenso: false }`, and the orchestrator's test passes `findMember` / `buscarMembro` as a fake; chapter 12's `lend-book` page (:98 to :112) proves the refusal by unit, orchestrator and end-to-end tests, each able to start from a member built suspended; chapter 13 :151, :165 to :167, :178 and :189 speak of that refusal, which still exists. The members feature is chapter 11's `[x] members`, "registers, suspends and reinstates members" (:51), so suspending from its screen is the librarian's usual path, and chapter 14 :207 / :209 ("going through on the librarian's usual path") stays true and keeps `fix-suspended` grave. The flaw is in what `findMember` reads, not in the rule nor the screen's message, so it is a flaw older than `return-book` in code it did not write, a finding (docs/05 §4).
  * Chapter 13's next step 1 (:197) tells the person to try a suspended member by hand; it does not say the person suspended one from the members screen, and no chapter says the person did, so nothing is contradicted. /apply checks that no sentence of chapters 12 to 14 says the end-to-end test or the hand try suspended a member from the members screen; if one does, the clause names a path that sentence did not take, within this item.
  * The queue blocks (en :233 to :239 and :243 to :247) and their column widths do not change.

*M5, chapter 21's key point.*

* `book/{en,pt}/21-beyond-software.md` :103 / :103.
  * Replaced: "* Give every finding a line, or it gets lost." / "* Dê uma linha a cada achado, ou ele se perde."
  * Proposed: "* Give every finding something that carries it, a line when it is grave and a note on a page otherwise (chapter 14), or it gets lost." / "* Dê a cada achado algo que o carregue, uma linha quando ele é grave e uma nota numa página quando não é (capítulo 14), ou ele se perde."
  * :89 / :89 stays word for word: it is a Case B passage, which docs/05 §5 lists for the author's approval when changed, and its "each finding needed a line, and a page whose Done when said ..." is the story's counterfactual; the key point carries the general lesson.

*M6, the mark in the quick guide.*

* `book/{en,pt}/10-quick-guide.md` :67 / :67, step 6's "You see" line, one clause at its start and nothing else changed.
  * Replaced: "You see verify green," / "Você vê a verificação verde,".
  * Proposed: "You see the last message open with what the delivery left, `🚨`, a siren, for a new line or a flaw that blocked it, `⚠️`, a warning sign, for a note, or `✅`, a check mark, for neither; verify green," / "Você vê a última mensagem abrir com o que a entrega deixou, `🚨`, uma sirene, para uma linha nova ou um defeito que a travou, `⚠️`, um sinal de aviso, para uma nota, ou `✅`, um sinal de visto, para nenhum dos dois; a verificação verde,".
  * :68's pointer to chapter 13, "What `/apply` does", already owns the why (:139); no pointer added. Key point :126 lists what the reader does, not what the reader sees, and stays.

Terms of docs/03: finding (achado), grave, note (nota), milestone review (revisão de marco), verify (verificação), slow test (teste lento), orchestrator (orquestrador), queue line (linha da fila). No new term. Sources: docs/05 §4 :121 to :124 and the kit's `SETUP.md` :855 to :858 at 2026.11.13 for M1; docs/05 §5's Verify slot and chapter 13 :81 to :87 for M3; chapter 13 :139 for the marks' words; the scratch build above for M2. No number added to a chapter. No source note added. Cases: none changed; chapter 21 :89 (Case B) untouched.

**States.** Inapplicable: chapters and the PDF build, no screen of an app.

**Visual reference.** The site's rendering of the marks, which draws them in place (m38-review's M2), and chapter 13 :139's words for them. Viewport: the PDF's A5 page, both editions.

**Out of scope.**

* Chapter 8 en :72 to :74 / pt :73 to :75: a shortened quotation of the migration report's one template sentence, with three tests as that sentence words them; a quote, not the book's definition.
* Chapter 13 :72 / :72 and its other `· after` passages, and chapter 14's section on waiting (:172 to :198 / :174 to :200) and `fix-due-date`'s `[?]`: M39's `ch13-apply-after`, `ch14-after-never-waits` and `ch14-queue-every-milestone` own them.
* Chapter 21 :89: a Case B passage; changing it would need the author's approval (docs/00 OD-3), and the key point meets M5 alone.
* The EPUB: it carries no fonts and the reader's device draws the marks (docs/01). The site: it draws them in place already.
* Headings, the running head, the contents and the notes: they hold no mark; no family list is added for a mark that does not exist.
* A build check that fails when the PDF embeds a font from outside `pandoc/fonts/`: a proof tool, which enters only on the person's word (docs/05 §4); this page checks it by hand with `pdffonts`.
* N8 (small 9), `.github/workflows/verify.yml` installing no colour emoji font: with the marks' font in the repository, Actions no longer needs one, but no Actions run proves the released PDF, so the item is not claimed met; it stays the review's small 9.
* m38-review's small findings 10 to 29 and the dropped ones: not picked by the author's word. Small 7 and small 8 are met in passing by choice (Decisions); small 21 (pt "caminho habitual" and "caminho de costume") is not, though M1 edits a sentence with "caminho habitual": chapter 14's sentence is not changed.
* No further line: a fix page opens none (docs/05 §8).

**Overlap with the work in flight.** For /apply, and for whoever orders the builds:

* `kit-2026-11-13` (`[ ]` in docs/06, being built by another session now) migrates docs/03, docs/05, docs/06, AGENTS.md and ADR-0018. This page changes docs/03 :36's `finding` row, so its /apply runs after that delivery is committed and reads docs/03 then (M1 above). This line's `after` names only `m38-review`; the order is the driver's.
* `ch14-open-lines-search` (untracked draft in `work/`, `[ ]`) has no section chosen; it may add a tip to chapter 14. If it lands first, M4's line moves and is found by the quoted sentence. Same file: by docs/05 §4 the two builds do not run at once.
* `ch13-apply-after` (M39, draft page `work/ch13-apply-after.md`, being defined) edits chapter 13 :72 to :74, :135 and key point 2 :334, and its Out of scope leaves chapter 13 :116, the marks of the example's last message and key point 4 to this page: no sentence in common, but the same files, so the two builds do not run at once (docs/05 §4). `ch14-after-never-waits` and `ch14-queue-every-milestone` (M39, `[ ]`, no page) will edit chapters 13 and 14; none of this page's sentences is in the passages their lines name. Same files: not built at once.

**Done when.**

* [x] M1 to M6 read as the Contract says in both editions, with docs/03's row as M1 says.
* [x] A sweep of `book/` finds no "three tests" nor "três testes"; every place that lists the tests of a grave finding outside chapter 8's quotation (ch11, ch13 by pointer, ch14, ch15, docs/03) gives four.
* [x] `pandoc/fonts/NotoColorEmoji-Regular.ttf` holds an `SVG ` table and the code points U+1F6A8, U+26A0, U+2705 and U+FE0F; `NotoColorEmoji-OFL.txt` beside it; `pandoc/pdf.css`, docs/01 :13, :42, :44 and both READMEs' licence row changed as the Contract says.
* [x] `make book` (under the run's lock) builds both editions; `pdffonts` on each PDF lists no `Apple-Color-Emoji` and no family outside `pandoc/fonts/`; each edition's contents on one page; page counts recorded.
* [x] Proof of a screen (docs/05 §5), the PDF in both editions: a PNG of every PDF page that holds a mark, found by searching each PDF's text for the three glyphs (at HEAD: en 141, 145, 152, 166, 171 / pt 147, 150, 151, 158, 173, 179, plus chapter 10's step 6 once M6 adds its marks), saved as `work/done/m38-fixes-pdf-<edition>-<what>.png`; and the failure captured: chapter 13's last-message block page built from HEAD's `pandoc/pdf.css`, one per edition, `work/done/m38-fixes-pdf-<edition>-before.png`, rendered from the PDFs `make book` leaves in `output/` before the first edit, or from a `git archive HEAD` copy built in the session's scratchpad; never by `git stash` or a checkout in the tree. The 25 MB source font stays out of the tree: it is downloaded and cut in the scratchpad, and only the subset enters `pandoc/fonts/`. Each after image shows every mark on its line, in place, in colour. The site needs no screenshot: its build is untouched (docs/05 §5's Design slot names site changes).
* [x] Both editions written; no filler and nothing useful cut; no number added; no em dash; no run narration; every mark in a chapter inside inline code or a code block; no source note added.
* [x] `make verify` green after the last edit, with its time against the five-minute ceiling; the disclosure scan green.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says, over this delivery's paths, the new font and licence files, the PNGs, and this line's docs/06 hunk; only those staged; the page in `work/done/` and its commit message suggested. The author authorized one commit per slug for this run; the driver session commits this delivery with the message /apply writes, and never pushes.

**Decisions.**

* Decided by the agent, the author corrects it in the review: M1 brings chapters 11, 13 and 15 and docs/03 to four tests, not chapter 14 and docs/05 to three, because docs/05 §4 and the kit at 2026.11.13 (`SETUP.md` :857 to :858) keep the fourth.
* Decided by the agent, the author corrects it in the review: M2's fix is a font, not CSS alignment. The scratch build showed the gap comes from weasyprint drawing Apple Color Emoji's `sbix` bitmaps, which no `vertical-align`, `line-height`, `display` or `font-size` moved; a subset of Noto Color Emoji with its `SVG ` table drew every mark in place in the whole book in both editions. The font lives in `pandoc/fonts/` like the others, as docs/01 :13 asks ("loaded from the repository so any machine sets the same pages"), cut to the three marks (36,880 bytes, not 25 MB).
* Decided by the agent, the author corrects it in the review: the toolchain change widens past `pandoc/pdf.css` to the font, its licence, docs/01 and the READMEs' licence row, since each owns a part of what the change adds.
* Decided by the agent, the author corrects it in the review: M2's proof is screenshots of the PDF, not the site at 1280 and 390 pixels, since only the PDF changes; the failure is captured from HEAD's stylesheet.
* Decided by the agent, the author corrects it in the review: M2's words beside the marks are chapter 13 :139's, placed before the marks in key point 4 and after each mark at :193, so the marks stay in inline code as the prose rule requires.
* Decided by the agent, the author corrects it in the review: M3 meets small 7 (chapter 7 :45 / :46) and small 8 (chapter 15 :21) in passing, a clause each, as the review allowed, since leaving them would keep chapter 5's fixed sentence contradicted two chapters later.
* Decided by the agent, the author corrects it in the review: M4 keeps the example and says how the tested rule broke (the tests built their suspended member; the members screen records a suspension in a field `findMember` does not read), rather than changing the flaw, so chapter 14's grading at :207 and its blocks stay, and chapter 5's tests, chapter 12's page and chapter 13's `lend-book` section are untouched. A first wording, the break on the lending screen, was dropped: chapter 12's end-to-end test and chapter 13's step 1 try the refusal there.
* Decided by the agent, the author corrects it in the review: M5 changes only the key point and leaves chapter 21 :89, a Case B passage, so nothing waits on the author's approval (docs/00 OD-3).
* Decided by the agent, the author corrects it in the review: M6 puts the mark first in step 6's "You see", as it is the first thing the last message shows, with chapter 13 :139's words beside each mark.
* From the documents: the six items and that they are one page (`work/done/m38-review.md`, the author's word; docs/05 §8); the fourth test (docs/05 §4); the build and its fonts (docs/01); the prose rule on emoji (docs/04); the Proof of a screen slot (docs/05 §5).

## Outcome

Built before the author read the page, on the author's word for this run ("Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão"), each open choice decided by the agent as the Decisions above and below say; the author corrects it in the review. The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

What was built, item by item:

* M1. Chapters 11 (en :98 / pt :101), 13 (:116, "four tests" / "quatro testes"), 15 (en :133 / pt :136) and docs/03's `finding` row now give four tests, the fourth in chapter 14's and docs/05 §4's words. The `kit-2026-11-13` migration had left the row at three tests, so this delivery changed it, found by the quoted sentence. A sweep of `book/` finds no "three tests" nor "três testes"; chapter 8's quotation is untouched.
* M2. `pandoc/fonts/NotoColorEmoji-Regular.ttf`, cut from the source the Contract names (downloaded to the scratchpad at commit `142c896`, sha256 and size as the page gives), with the page's command: 36,880 bytes, sha256 `edb0de71a1f014bc12219223114f7ed8d457a387e5d542ad04f3477932e68955`, the same 16 tables, `SVG ` among them. `pandoc/fonts/NotoColorEmoji-OFL.txt` is the source's `OFL.txt` byte for byte. `pandoc/pdf.css` has the `@font-face` with a one-line comment, and the family after Merriweather in `html` and after Iosevka Term in `code, pre`. docs/01 :13, :42 and :44 and both READMEs' licence row name the family. Chapter 13 :193 and key point 4 (:336) give each mark its word, in both editions.
* M3. Chapter 5 :39 and :41 (now :41 and :42), chapter 7 (en :45 / pt :46) and chapter 15 :21, in both editions.
* M4. Chapter 14 en :201 / pt :203. No sentence of chapters 12 to 14 says the end-to-end test or the hand try suspended a member from the members screen (sweep of "suspend"), so the clause stands as proposed.
* M5. Chapter 21 :103; :89 (Case B) untouched.
* M6. Chapter 10 :67, step 6's "You see", one clause at its start.

Divergences and decisions taken in the build:

* Decided by the agent: chapter 5's proposed sentence ended "(chapter 13)" / "(capítulo 13)"; the pointer is dropped, since docs/04 §Writing the book, Chapter pointers, allows no forward pointer in chapters 0 to 7 outside the gain section. The sentence says all the reader needs without it.
* Decided by the agent: pt chapter 5 :39 says "se você não disser outro tempo", not "outro", which left the pronoun with no noun (delivery review).
* The font holds U+FE0F as a variation sequence (cmap format 14) for U+26A0 and U+2705, not as a glyph of its own; the 25 MB source does the same, so the Done when item on the code points is met as the font can hold it.
* `fontTools.subset` needs `lxml` to cut an `SVG ` table; Python's isolated mode (`-I`) hides the user site where `lxml` lives here, so the cut ran with `-E -P`, from the repository's root, the source passed by path.
* Another delivery, `ch12-propose-after`, was committed (`46e961a`, chapter 12 in both editions) while this one was building; it touches no file of this page, so it is no conflict, but its text moved the English PDF by one page from chapter 12 on.

Proof:

* Verify: green, 40 seconds against the five-minute ceiling, after the last edit; the disclosure scan green. The binary font and the licence file pass every check (em dash skips a file with a NUL byte; the link check reads no file of `pandoc/fonts/`; the prose and width checks read the chapters and READMEs only).
* `make book`, under the run's lock: both editions built, each contents on one page. Pages: en 268 (267 at HEAD `8867b24`; the one page is `ch12-propose-after`'s, the first build of this delivery alone gave 267), pt 281 (280 at HEAD; the text edits of this page). `pdffonts` on each PDF: Instrument Serif, Iosevka Term, Merriweather and Noto Color Emoji, no `Apple-Color-Emoji`, no family outside `pandoc/fonts/` (weasyprint's synthesized Iosevka Term bold and oblique are the repository's Regular, as at HEAD).
* Proof of a screen, the PDF in both editions. Before, rendered from the PDFs `make book` had left in `output/` from HEAD's stylesheet, before the first edit: `work/done/m38-fixes-pdf-en-before.png` (en p145) and `work/done/m38-fixes-pdf-pt-before.png` (pt p150), chapter 13's last-message block, each mark drawn small above the line with an empty gap where it belongs. After, every page whose text holds a mark, found by searching each PDF for the three glyphs: en 105 (chapter 10), 142, 146, 153 (chapter 13), 167, 172 (chapter 14); pt 109 (chapter 10), 147, 150, 151, 159 (chapter 13), 173, 179 (chapter 14), saved as `work/done/m38-fixes-pdf-<edition>-<chapter>-p<page>.png`. Each shows every mark on its baseline, at text size, in colour, in paragraphs and at the start of its line in code blocks.
* The site and the EPUB: untouched by the toolchain change (`pandoc/epub.css`, `mkdocs.yml` and `book/assets/site.css` unchanged), so no screenshot.
* Slow tests: none in the Verify slot.
* Manuals: none names the fonts; none changes.

Delivery review (one read-only Opus agent, over this delivery's paths, the new files, the PNGs and this line's docs/06 hunk): no must-fix. Fixed: docs/01 :13 said the emoji family came "after each family", while `pdf.css` adds it after the body's and the code's only (now says so, as :42 does); pt chapter 14 :203's "os testes dela" read as the screen's tests (now "dele", `emprestar` being masculine as in chapter 5); pt chapter 5 :39's "outro" (above). Kept as written, within the Contract: en chapter 14 :201's two colons, en chapter 7 :45's "its ceiling", and chapter 10's `⚠️` "for a note" (a verify over its ceiling is a note, so it holds). Verify and `make book` ran again after the fixes, green.

## For the review

* `pandoc/pdf.css` :247 and every rule naming one family (headings, the running head, the contents, `.footnote`, `.opening`): no emoji fallback, so a mark placed there later would fall to the machine's emoji font again and be drawn above its place; none holds a mark today (Out of scope).
* `pandoc/fonts/NotoColorEmoji-Regular.ttf`: its `name` table says "Copyright 2022 Google Inc.", its `OFL.txt` 2021; both are upstream's, unchanged.
* `.github/workflows/verify.yml`: small 9 of `m38-review` stays as it was; with the marks' font in the repository Actions needs no emoji font, but no Actions run of the release proved it.

```commit
fix(m38-fixes): grave in four tests, marks drawn in place in the PDF

- Chapters 11, 13, 15 and docs/03 give a grave finding's four tests
- PDF sets the marks in a cut of Noto Color Emoji, licence and docs/01
- Chapter 5 tells verify's ceiling and who runs the slow tests
- Chapter 14 says how a tested refusal broke; chapter 21 key point
- Chapter 10 step 6 names the mark /apply's last message opens with

work/done/m38-fixes.md
```
