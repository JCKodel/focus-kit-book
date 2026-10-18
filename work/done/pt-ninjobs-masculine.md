# pt-ninjobs-masculine

**Objective.** A reader of the Portuguese edition meets Ninjobs as *o Ninjobs*, an app and a site, from the prologue to the last chapter, and every word that agrees with it agrees in the masculine; docs/03 records it, so the next chapter cannot drift. Found by the author's reading of the book on 2026-10-18: "Ninjobs is masculine in Portuguese: o Ninjobs, because it is an app (aplicativo) or a site, both masculine nouns." This reverses `pt-ninjobs-article` (work/done/pt-ninjobs-article.md), which chose the feminine without the author; the author now decides the masculine.

**Decided without the author.** The batch had no one to answer; each choice is the recommended one. The gender itself is the author's decision, not one of these.

1. *Agreement, not only the article, as `pt-ninjobs-article` decision 2 did.* Each sentence that names Ninjobs is read whole: a contraction (`na` to `no`, `da` to `do`, `à` to `ao`, `pela` to `pelo`), a pronoun (`ela`, `dela`, `a`), a participle or an adjective that refers to Ninjobs changes to the masculine; a word that refers to something else in the sentence (the queue, a page, a number, the product's site) keeps its gender. Counted on 2026-10-18, two words beyond the article refer to Ninjobs: pt 11:28 "a fila dela" (the queue is Ninjobs's) and pt 16:78 "as verificações antigas a terem acompanhado" (the old checks went along with Ninjobs). Source: the author's draft ("with agreement (contractions, pronouns, participles)"), Portuguese grammar.
2. *Headings change with the text.* Two headings hold a contraction, pt 03:7 "O que cresceu na Ninjobs" and pt 22:26 "O que uma entrega custou na Ninjobs"; they change as every other use does. Their anchors change, and no link in `book/`, `README.pt.md` or `docs/` points to either (grep on 2026-10-18). Source: `pt-ninjobs-article`'s "Decisions taken in /apply", which changed chapter 22's heading the same way.
3. *docs/03 replaces the sentence, it does not add one.* The `case` row's last sentence, "In Portuguese, Ninjobs takes the feminine article: a Ninjobs, na Ninjobs, da Ninjobs.", becomes the masculine with the author's reason, so the next chapter takes both the article and why from the glossary. Source: the author's draft, docs/03's header ("The Portuguese term is fixed"), docs/05 §7.
4. *The whole edition at apply time.* The check runs on `book/pt/` and `README.pt.md` as they are when this line is applied, not on the line numbers counted here; any feminine use another delivery wrote before it is fixed by this one, and a delivery applied after it reads the amended docs/03 row. The lines counted on 2026-10-18 are a courtesy, listed under Behaviour. Source: `pt-ninjobs-article` decision 4.
5. *English untouched.* The English edition writes Ninjobs with no article; nothing changes there, so edition parity is unaffected and ADR-0004 is met as in `pt-ninjobs-article` decision 5: the choice exists only in Portuguese. Source: ADR-0004, docs/04 §Tests (parity).
6. *`work/done/pt-ninjobs-article.md` stays as it is.* It is the record of what was decided then; this page names it as the delivery it reverses. Source: `m16-review` decision 4 (work/done/ is not rewritten).
7. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* A reader of the Portuguese edition finds Ninjobs after a masculine article or contraction wherever it appears: "O Ninjobs", "o Ninjobs", "No Ninjobs", "no Ninjobs", "do Ninjobs", "ao Ninjobs", "pelo Ninjobs" if one is needed.
* Examples, at /propose: pt 06:46 "A Ninjobs abriu ao público em 2026-09-10" becomes "O Ninjobs abriu ao público em 2026-09-10"; pt 06:73 "deu à Ninjobs quatro telas" becomes "deu ao Ninjobs quatro telas"; pt 11:28 "Na Ninjobs eu deixei as linhas crescerem: a fila dela tinha 102 entregas" becomes "No Ninjobs eu deixei as linhas crescerem: a fila dele tinha 102 entregas"; pt 16:78 "depois de as verificações antigas a terem acompanhado" becomes "depois de as verificações antigas o terem acompanhado".
* Kept by decision 1, because they agree with another noun: pt 11:167 "Na Ninjobs ela guardou" keeps "ela" (the queue, pt 11:166) and only its contraction changes; pt 22:100 "ele" (the number, pt 22:99); pt 13:142 "ele estava atual" (the site); pt 12:133 "ela era" (the page); pt 07:56 "um app web fino" and pt 22:28 "construído", already masculine.
* Counted on 2026-10-18 over `book/pt/`: 39 occurrences of Ninjobs in 14 files, every one feminine, 19 "Na", 8 "na", 7 "A", 2 "a", 2 "da", 1 "à"; `README.pt.md` names Ninjobs nowhere. The lines: pt 00:62, 106, 107; 02:66; 03:7, 9, 254; 04:234; 06:3, 8, 46, 49, 73, 79; 07:10, 56, 144; 09:49; 11:28, 167; 12:126, 133; 13:142, 222; 15:136, 150; 16:10, 26, 78; 21:70; 22:26, 28, 47, 75, 78, 90, 95, 100, 105.
* Checked at apply time, after every edit:
  * `grep -rnE "(^|[^[:alpha:]])([Aa]|[Dd]a|[Nn]a|à|À|[Pp]ela|[Pp]ra|[Uu]ma|[Dd]uma|[Nn]uma|[Dd]essa|[Nn]essa|[Ee]ssa|[Ee]sta|[Ss]ua|[Mm]inha|[Tt]oda)s? Ninjobs\b" book/pt README.pt.md` prints nothing.
  * `grep -rn "Ninjobs" book/pt README.pt.md`, every line read in its sentence and its neighbours for decision 1's agreement; the page lists each sentence changed beyond its article, en line beside it.
  * `grep -o "Ninjobs" -r book/pt | wc -l` gives the same count before and after (39 at /propose): nothing added or removed.
  * `grep -rn "cresceu-na\|custou-na" book README.pt.md README.md docs` prints nothing (decision 2).
  * `git diff --stat book/en README.md` shows nothing changed by this delivery.
* docs/03's `case` row reads, in its Meaning: "A real project the book draws on; anonymous when private. Case A ran on the process; Case B did not, and the book says so wherever it appears. In Portuguese, Ninjobs takes the masculine article, as an app or a site: o Ninjobs, no Ninjobs, do Ninjobs."
* Fails: a feminine form left anywhere in `book/pt/` or `README.pt.md`; a pronoun, participle or adjective left feminine where it refers to Ninjobs; a word that refers to something else changed; any text of the English edition changed; a Ninjobs occurrence added or removed; a link left pointing to a changed anchor; an em dash.

**Contract.**

* Files: every file under `book/pt/` that holds a feminine form at apply time (at /propose: `00-product-people-process.md`, `02-spec-driven.md`, `03-simplicity-and-results.md`, `04-focus.md`, `06-birth-of-focus-kit.md`, `07-the-documents.md`, `09-starting-a-project.md`, `11-queue-and-milestones.md`, `12-propose.md`, `13-apply.md`, `15-closing-a-milestone.md`, `16-the-governor.md`, `21-beyond-software.md`, `22-cost-and-where.md`); `README.pt.md` if one appears there; `docs/03-Domain.md`, the `case` row only.
* Terms of docs/03: none new; the `case` row amended as Behaviour quotes. Sources: none added or removed. Cases: Ninjobs, its name only; no new fact about it, so docs/03 §Entities and invariants's rule on Ninjobs holds as it is. Exercises: none (ADR-0017).
* docs/00, docs/01, docs/02, docs/04, docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.** M18's other drafts edit Portuguese chapters 0 to 7 and 11 to 13; none of them names Ninjobs in its page. `case-a-why-anonymous` edits pt 00:107, the same line as "A Ninjobs aparece pelo nome": whichever lands second edits the line as the first left it, and this delivery changes only the article and its agreement there. Any Portuguese sentence another delivery writes about Ninjobs is covered by decision 4: one applied before this line is fixed by its grep, one applied after reads the masculine in docs/03 and is checked by `m18-review`, which comes after every M18 line. The apply order is the driver's; applied last among the M18 lines that touch `book/pt/`, decision 4's grep is the only check needed.

**Out of scope.**

* The English edition: decision 5.
* Other Portuguese wording in the same sentences: only the agreement decision 1 names.
* `work/done/`, including `pt-ninjobs-article.md`: decision 6.

**Done when.**

* [x] Behaviour's checks give what it names on the whole Portuguese edition and `README.pt.md` at apply time; every sentence changed beyond its article listed on the page.
* [x] docs/03's `case` row amended as Behaviour quotes.
* [x] Each changed chapter still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, the change draws on no Case A or Case B passage (docs/00 OD-3); on pt 00:107 it touches only the article before Ninjobs.
* [x] `make book` run; both PDF paths given to the author: the driver builds the book once at the end of the batch.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunks of docs/03 and docs/06, commit message in a `commit` block: the driver marks the line and stages.

**Proof.**

* Count before and after over `book/pt/` and `README.pt.md` at apply time: 40 occurrences in 14 files, every one feminine before (20 "Na", 8 "na", 7 "A", 2 "a", 2 "da", 1 "à"); 40 after, every one masculine. The 40th, against the 39 counted at /propose, is pt 13:170 "Na Ninjobs, eu usei cada entrega", written by `try-before-commit` (decision 4). `README.pt.md` names Ninjobs nowhere.
* The feminine grep of Behaviour prints nothing; the `cresceu-na\|custou-na` grep prints nothing; `git diff --stat book/en README.md` is empty.
* A word diff of `book/pt` holds only: `Na`/`No` 20, `na`/`no` 8, `A`/`O` 7, `a`/`o` 3 (two articles, one pronoun), `da`/`do` 2, `à`/`ao` 1, `dela`/`dele` 1.
* `make verify`: build, parity, em dash, prose, width, links and disclosure, exit 0.

**Sentences changed beyond the article** (decision 1):

* pt 11:28 "a fila dela tinha 102 entregas" to "a fila dele tinha 102 entregas" (en 11:26 "its queue held 102 deliveries").
* pt 16:78 "depois de as verificações antigas a terem acompanhado" to "o terem acompanhado" (en 16:78 "after the old checks had gone with it").

**Kept by decision 1**, read in their sentences and neighbours: pt 11:174 "No Ninjobs ela guardou" (the queue), pt 12:133 "ela era" (the page), pt 13:142 "ele estava atual" (the site), pt 22:100 "ele" (the number), pt 07:66 "um app web fino" and pt 22:28 "construído", already masculine. No other pronoun, participle or adjective in the neighbouring lines refers to Ninjobs; in chapters 6, 16 and 22, where Ninjobs runs as the subject, every "ela", "dela" and "nela" was read and refers to another noun (a delivery, a rule, a change, the bill, a session, the page, an entry, the governor's error).

**Divergences.** None from Behaviour. The line numbers moved since /propose (other M18 deliveries landed first): 03:254 is now 03:267, 04:234 is 04:239, 07:56 is 07:66, 07:144 is 07:154, 11:167 is 11:174, 13:222 is 13:233, 02:66 is 02:69.

**Decisions taken in /apply.**

* The 40th occurrence, pt 13:170, changed as every other, by decision 4; the before and after counts are both 40.

**Review.** One read-only agent on Opus read `git diff -- book/pt docs/03-Domain.md` against this page and docs/04, and every Ninjobs line of the Portuguese edition in its sentence with two lines either side: no findings. Its one note, that the page's /propose counts say 39 and old line numbers, is answered under Proof and Divergences: 40 before and after, with the moved lines listed.

```commit
docs(pt-ninjobs-masculine): give Ninjobs the masculine throughout pt

- Portuguese edition: Ninjobs takes o, no, do, ao, 40 uses in 14 chapters
- Agreement: pt 11:28 "a fila dele", pt 16:78 "o terem acompanhado"
- docs/03's `case` row fixes the masculine, as an app or a site

work/done/pt-ninjobs-masculine.md
```
