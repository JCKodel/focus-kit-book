# ch07-12-loan-days

**Objective.** After chapters 7, 12 and 13 a reader finds the lending library's loan period of 21 days in one document, docs/03, as chapter 7's "Where a new fact goes" places it, and chapters 12 and 13 name that same document for it; both editions, least change.

**Behaviour.**

* Reading chapter 12's example page, the reader sees the 21 days cited to docs/03, the document chapter 7 gave the term and its value.
* Reading the paragraph after the page, the reader learns the 21 days come from docs/03, and Out of scope's reservations and fines from docs/00.
* Reading "Read the page before `/apply`", the reader's example of a question a document already answers names docs/03 as the document that says 21.
* Reading chapter 13's "`lend-book`, built", the reader's example of a page contradicting a document has docs/03 say a loan lasts 14 days, so the agent stops and asks which is true.
* Chapter 7 reads as it does: the number written once, in docs/03; docs/00 holds the rule the member meets and cites the loan period by name.
* Fails if: any passage of chapter 7, 12 or 13 still places the loan's length in docs/00; chapter 7 changes; a sentence of chapter 12 other than the three named below, or of chapter 13 other than the one named below, changes; the code block's layout or line wrapping changes beyond the citation; the chapter says how it read before or narrates a run; the two editions differ.

**Contract.**

`book/en/12-propose.md` and `book/pt/12-propose.md`, three places, each the citation only:

* Section "The page" (pt "A página"), the example page's first Behaviour line, en line 59, pt line 60: "(docs/00)" becomes "(docs/03)". The rest of the line and the block's wrapping stay.
* Same section, the paragraph after the page, en line 114, pt line 123: "the 21 days come from docs/00, and so do Out of scope's reservations and fines." becomes "the 21 days come from docs/03, and Out of scope's reservations and fines from docs/00." (pt "os 21 dias vêm do docs/03, e as reservas e as multas do Fora do escopo vêm do docs/00."). Wording is /apply's within that sense.
* Section "Read the page before `/apply`" (pt "Leia a página antes do `/apply`"), en line 137, pt line 146: "when docs/00 says 21" becomes "when docs/03 says 21" (pt "quando o docs/03 diz 21").
`book/en/13-apply.md` and `book/pt/13-apply.md`, one place, the document's name only:

* Section "`lend-book`, built" (pt "`emprestar-livro`, construída"), line 120 in both: "If docs/00 said a loan lasts 14 days" becomes "If docs/03 said a loan lasts 14 days" (pt "Se o docs/00 dissesse" becomes "Se o docs/03 dissesse"). The rest of the sentence stays. The line number is as of this page; /apply finds the sentence by its words, since `m21-git-slot-default` edits chapter 13 first.
* Stays: chapter 13's reading list at line 115 (docs/00 "for the rules a member meets", true as it stands) and every other line of chapter 13; chapter 7 in both editions (en 145 to 148, pt 146 to 149); every other line of chapter 12, its Out of scope lines citing docs/00 (en 86 to 88, pt 93 to 95) and its reading list at line 25 included.

Terms of docs/03 used: loan period, loan, due date; none new. No number added, no source note, no private case. Sources cited: none new.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapters 3, 4, 5, 11 and 13's other mentions of 21 days: they cite no document.
* docs/03, docs/00, docs/06: no edit; the queue line is the driver's.

**Decisions from the documents.**

* The loan period of 21 days is docs/03's: chapter 7, "Where a new fact goes" ("The term and its value, the loan period of 21 days ... go to docs/03, question 3 ... The number is written once, in docs/03; the other two documents use the term."), and chapter 13's reading list (line 22, docs/03 "whose table gives each term"; line 115, docs/00 "for the rules a member meets").
* So chapter 12 changes and chapter 7 stays: rewriting chapter 7's principle to fit one citation in an example would be the larger change, and wrong by its own questions.
* Reservations and fines stay docs/00's: question 2, an open decision is docs/00's (chapter 7), and chapter 12's Out of scope already says so.
* No before/after or version in the text: AGENTS.md, the driver.

**Decisions taken alone.**

* The Behaviour line keeps one citation, now "(docs/03)", attached to the 21 days it ends on, rather than citing both documents: fewest words, and the paragraph after the page names both sources.
* The third place, en 137 and pt 146, is in scope though finding K3 of `work/done/m21-review.md` named only lines 59 and 114: it says the same fact and would contradict the other two.
* Chapter 13:120 joins this delivery by the driver's decision: it is the same finding K3, and the queue line's text (chapters 7 and 12) is the driver's to widen in docs/06. /apply runs after `m21-git-slot-default` finishes chapter 13.

**Done when.**

* [ ] Both editions written, the same three citations changed in each chapter 12 file and the same one in each chapter 13 file, Portuguese read as Portuguese; the chapter opens as it did, no filler and nothing useful cut.
* [ ] `grep -n "docs/00" book/{en,pt}/12-propose.md` finds no line that holds "21"; `grep -n "21" ` on the same files shows docs/03 on the three lines; `grep -n "14 d" book/{en,pt}/13-apply.md` shows docs/03 on that sentence and no docs/00.
* [ ] `git diff` of this delivery touches only the three lines in each chapter 12 file and the one sentence in each chapter 13 file, and nothing in chapter 7.
* [ ] No em dash; no "no longer", "now", "não mais", "agora" added; no narrated run.
* [ ] Delivery review as docs/05 §5 says.
* [ ] `make verify` green; `make book` builds both editions and both PDF paths are reported (the driver may run it once for the batch).
* [ ] Only this delivery's paths staged; the page moved to `work/done/` and its commit message suggested.
