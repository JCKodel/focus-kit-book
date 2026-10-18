# pt-ninjobs-article

**Objective.** A reader of the Portuguese edition meets Ninjobs with one article from the prologue to the last chapter, the feminine, *a Ninjobs*, and every word that agrees with it agrees in the feminine; docs/03 records it, so the next chapter cannot drift. Found by `m16-review` (work/done/m16-review.md, chA-7: "pt, the article before Ninjobs is feminine in chapters 0, 2, 3, 4, 11, 12, 13, 15, 16, 21 and masculine in 6, 7, 9, 22; the range moved 9:49 to the masculine." Seen).

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *The feminine.* Counted on 2026-10-18 over `book/pt/`: 39 occurrences of Ninjobs, every one after an article or a contraction; 20 feminine in ten files (the prologue, chapters 2, 3, 4, 11, 12, 13, 15, 16 and 21) and 19 masculine in four (chapters 6, 7, 9 and 22, nine of them in chapter 22). The prologue's first use is feminine ("Na Ninjobs (<https://www.ninjobs.app>), meu próprio produto", pt 00:62), and the prologue is where docs/04 §Writing the book, Evidence has the Portuguese edition fix a name once; most files and the first meeting agree. Ninjobs is the product's name and Portuguese gives a brand either gender, so the documents leave the choice open; this one changes the fewest files' first use. Source: the count, docs/03 (`case`), the prologue.
2. *Agreement, not only the article.* Each sentence that names Ninjobs is read whole: a contraction (`no`, `do`, `ao`, `pelo`, `num`), a pronoun (`ele`, `dele`, `o`, `seu`), a participle or an adjective that refers to it changes to the feminine; a word that refers to something else in the sentence (the product's code, a repository, a team) keeps its gender. Source: Portuguese grammar; the finding names the article, and an article changed alone would leave the sentence disagreeing with itself.
3. *docs/03 records the gender.* The `case` row's Meaning gains one sentence, so a future chapter takes the article from the glossary: the error it would have caught is this finding (docs/05 §7). The row is the one that already names `ninjobs` as an identifier; no new row. Source: docs/03's header ("The Portuguese term is fixed: the Portuguese edition uses it and no synonym"), docs/04 §Languages.
4. *The whole edition at apply time.* This line is applied last of M16's and M17's open deliveries, so its check runs on `book/pt/` and `README.pt.md` as they are then, not on the line numbers counted here; any new masculine use another delivery wrote is fixed by this one. The lines counted on 2026-10-18 are a courtesy: pt 06:3, 8, 46, 49, 73, 79; 07:10, 56, 144; 09:49; 22:26, 28, 47, 75, 78, 90, 95, 100, 105.
5. *English untouched.* The English edition writes Ninjobs with no article; nothing changes there, and no heading, note or status changes in Portuguese, so edition parity is unaffected. ADR-0004's "a change to both" is met: the fault exists only in Portuguese, as with chapter 4's Portuguese-only sentence. Source: ADR-0004, docs/04 §Tests (parity).
6. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* A reader of the Portuguese edition finds Ninjobs after a feminine article or contraction wherever it appears: "A Ninjobs", "a Ninjobs", "Na Ninjobs", "na Ninjobs", "da Ninjobs", "à Ninjobs", "pela Ninjobs", "uma Ninjobs" if one is needed.
* Examples, pt chapter 6 at /propose: "O Ninjobs abriu ao público em 2026-09-10" becomes "A Ninjobs abriu ao público em 2026-09-10"; "deu ao Ninjobs quatro telas" becomes "deu à Ninjobs quatro telas"; "que se sustentou no Ninjobs" becomes "que se sustentou na Ninjobs".
* Checked at apply time, after every edit:
  * `grep -rnE "\b([Oo]|[Dd]o|[Nn]o|[Aa]o|[Pp]elo|[Pp]ro|[Uu]m|[Dd]um|[Nn]um|[Dd]esse|[Nn]esse|[Ee]sse|[Ee]ste|[Ss]eu|[Mm]eu|[Tt]odo)s? Ninjobs\b" book/pt README.pt.md` prints nothing.
  * `grep -rn "Ninjobs" book/pt README.pt.md`, every line read in its sentence for decision 2's agreement; the page lists each sentence changed beyond its article, en line beside it.
  * `grep -o "Ninjobs" -r book/pt | wc -l` gives the same count before and after (39 at /propose): nothing added or removed.
  * `git diff --stat book/en README.md` shows nothing changed by this delivery.
* docs/03's `case` row reads, in its Meaning: "A real project the book draws on; anonymous when private. Case A ran on the process; Case B did not, and the book says so wherever it appears. In Portuguese, Ninjobs takes the feminine article: a Ninjobs, na Ninjobs, da Ninjobs."
* Fails: a masculine form left anywhere in `book/pt/` or `README.pt.md`; a pronoun, participle or adjective left masculine where it refers to Ninjobs; a word that refers to something else changed; any text of the English edition changed; a Ninjobs occurrence added or removed; an em dash.

**Contract.**

* Files: every file under `book/pt/` that holds a masculine form at apply time (at /propose: `06-birth-of-focus-kit.md`, `07-the-documents.md`, `09-starting-a-project.md`, `22-cost-and-where.md`); `README.pt.md` if one appears there; `docs/03-Domain.md`, the `case` row only.
* Terms of docs/03: none new; the `case` row amended as Behaviour quotes. Sources: none added or removed. Cases: Ninjobs, its name only; no new fact about it, so docs/03 §Entities and invariants's rule on Ninjobs holds as it is. Exercises: none (ADR-0017).
* docs/00, docs/01, docs/02, docs/04, docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.** Applied last, after every other open line of M16 and M17. `docs03-review-rows` edits docs/03's `delivery review` and `candidate` rows, a hunk apart from `case`. `ch04-features-folder`, `ch11-blocking-fix` and `ch15-range-pointer` touch Portuguese chapters that already write the feminine. Any line that lands after this page was written is covered by decision 4's apply-time check.

**Out of scope.**

* The English edition: decision 5.
* Other Portuguese wording in the same sentences: only the agreement decision 2 names.
* `work/done/`: the record of what happened, not rewritten (`m16-review` decision 4).

**Done when.**

* [x] Behaviour's checks give what it names on the whole Portuguese edition and `README.pt.md` at apply time; every changed sentence listed on the page.
* [x] docs/03's `case` row amended as Behaviour quotes.
* [x] Each changed chapter still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, the change draws on no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunks of docs/03 and docs/06, commit message in a `commit` block.

**Proof.** At apply time, after every other line of M16 and M17 was committed: Behaviour's masculine grep over `book/pt` and `README.pt.md` prints nothing (on the committed chapter 22 it counted 9 before the change); `grep -o "Ninjobs" -r book/pt | wc -l` gives 39 before and after, and `README.pt.md` names Ninjobs nowhere; `git diff --stat book/en README.md` is empty. Every `grep -rn "Ninjobs"` line was read in its sentence. `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Changed sentences.** Nineteen lines in four files, each its article or contraction only, at the line numbers the page counted at /propose; none changed beyond it. Portuguese line, then the English line beside it.

* pt 06:3 "No Ninjobs" to "Na Ninjobs" (en 06:3, "On Ninjobs").
* pt 06:8 "O Ninjobs começou" to "A Ninjobs começou" (en 06:8).
* pt 06:46 "O Ninjobs abriu" to "A Ninjobs abriu" (en 06:46).
* pt 06:49 "do Ninjobs" to "da Ninjobs" (en 06:49).
* pt 06:73 "ao Ninjobs" to "à Ninjobs" (en 06:73).
* pt 06:79 "no Ninjobs" to "na Ninjobs" (en 06:79).
* pt 07:10 "No Ninjobs" to "Na Ninjobs" (en 07:10).
* pt 07:56 "O Ninjobs, um app web fino" to "A Ninjobs, um app web fino" (en 07:55).
* pt 07:144 "no Ninjobs" to "na Ninjobs" (en 07:143).
* pt 09:49 "No Ninjobs" to "Na Ninjobs" (en 09:49).
* pt 22:26, the heading, "no Ninjobs" to "na Ninjobs" (en 22:26); no link points to its anchor.
* pt 22:28 "O Ninjobs é" to "A Ninjobs é" (en 22:28).
* pt 22:47, 75, 78, 100 "No Ninjobs" to "Na Ninjobs" (en 22:47, 75, 78, 99).
* pt 22:90 and 105 "no Ninjobs" to "na Ninjobs" (en 22:89, 104).
* pt 22:95 "o Ninjobs" to "a Ninjobs" (en 22:94).

**Divergences.** None from Behaviour.

**Decisions taken in /apply.**

* Words kept masculine by decision 2, because they agree with another noun: pt 07:56 "um app web fino" (the apposition agrees with *app*), pt 22:28 "o meu próprio produto, construído" (with *produto*, as the prologue's "Na Ninjobs, meu próprio produto"), pt 22:100 "ele" (the number, "Um número por entrega"), pt 07:10 "mantê-los" (the places).
* Decision 5's "no heading changes" read as no structural change: chapter 22's heading holds a masculine contraction, so its contraction changes as every other use does, and parity is unaffected.

**Review.** One read-only agent on Opus read the diff of `book/pt` and `docs/03-Domain.md` and this line's hunk of docs/06 against this page and docs/04, and every Ninjobs sentence of the Portuguese edition with its neighbours: no findings.

```commit
docs(pt-ninjobs-article): give Ninjobs the feminine throughout pt

- Portuguese chapters 6, 7, 9 and 22: Ninjobs takes a feminine article or contraction, 19 lines
- docs/03's `case` row fixes the feminine for the next chapter

work/done/pt-ninjobs-article.md
```
