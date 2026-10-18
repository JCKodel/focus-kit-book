# docs03-checker-pt

**Objective.** A translator or an agent writing the Portuguese edition finds in docs/03 the fixed Portuguese words for the milestone review's checker and its three labels, "conferente", "visto", "latente" and "fraco", the words the Portuguese edition already uses, so no later chapter picks a synonym.

**Decided without the author** (batch rule of this run: the recommended answer, no question asked).

1. *The words are the ones the Portuguese edition already uses.* Every Portuguese chapter that names the checker (7, 11, 15, 16, 23) writes "conferente", as many times as its English names "checker", and chapters 8 and 15 write the labels "visto", "latente" and "fraco" (`m17-review`, R2-7). docs/03 fixes them; no chapter changes.
2. *"conferente", not the kit's "verificador".* The kit's `CHANGELOG.pt.md` calls the checker "verificador". In this book "verificação" is verify (chapter 7's slots), and chapter 16 writes "verificador automático" to gloss a lint, so "verificador" would read as a tool that verifies; "conferente" also matches chapter 11's "o marco conferido contra o parágrafo dele", the review's own verb. The book quotes no text of the kit's Portuguese changelog. `kit:` the author may tell the kit that its Portuguese changelog's "verificador" differs from the book's "conferente"; nothing in the kit is changed here.
3. *One new row and the labels inside the candidate row.* `checker` is a role and gets its own row, after `candidate`. The three labels are what the checker marks a candidate, and docs/03's `candidate` row already defines them; their Portuguese goes in that row's Meaning, as the `running example` row fixes its Portuguese words in its Meaning, so each label is defined in one place. The labels agree with "candidato", hence the masculine.
4. *The `milestone review` row stays.* It says "one checker marks each candidate seen, latent or weak", which the new row now defines.
5. *Shared file.* docs/03 is also changed by `untracked-diff-wording` (the untracked file row), `conflict-same-lines` (the conflict row) and `docs05-fourth-case-version` (the waiting mark row), other sessions of this batch; this page's rows, `candidate` and the new `checker` after it, are a separate hunk, so stage this delivery by hunk.
6. *Trunk; nothing staged by this definition; the driver sets docs/06's marks.*

**Behaviour.**

* Looking up "checker" in docs/03, a reader finds "conferente" and what the checker does: who it is, what it marks, that it fixes nothing.
* Looking up the candidate row, a reader finds seen, latent and weak with their Portuguese words visto, latente and fraco.
* Reading the Portuguese chapters 7, 8, 11, 15, 16 and 23, a reader meets only those words for the checker and the labels; "verificador" appears only in chapter 16's gloss of a lint.
* Failure: a chapter changed, a label defined in two rows, a Portuguese word in docs/03 that differs from the edition's, or a row of docs/03 other than these two changed.

**Contract.**

* **docs/03, the `candidate` row**, one replacement: "marked seen (true in the file today), latent (nothing triggers it today) or weak (the claim does not hold as stated) by the checker," becomes "marked seen (true in the file today), latent (nothing triggers it today) or weak (the claim does not hold as stated) by the checker, in Portuguese visto, latente and fraco, which agree with candidato,". The rest of the row is unchanged.
* **docs/03, a new row** right after the `candidate` row:

  `| checker | conferente | none | The one reader of a milestone review that comes after the area readers: an agent or the review's own session opens each candidate's file and marks it seen, latent or weak (candidate) before the person sees it; it fixes nothing (docs/05 §8). |`
* **The Portuguese edition.** No change: chapters 7, 11, 15, 16 and 23 already write "conferente" and chapters 8 and 15 "visto", "latente" and "fraco".
* **Terms of docs/03.** New: `checker` / `conferente`. Fixed in an existing row: the labels' Portuguese.
* **Sources.** None. **Cases.** None.
* **docs/06.** None from this page; the driver sets its line's marks.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* The kit's Portuguese changelog: the kit's, named for the author (decision 2).
* Rows for each label: defined once, in `candidate` (decision 3).
* The other docs/03 rows of this batch: their own lines (decision 5).

**Done when.**

* [x] docs/03 holds the Contract's two edits and no other change of this delivery; `git diff docs/03-Domain.md` for this delivery shows only the `candidate` row and the new `checker` row.
* [x] `grep -c "conferente" book/pt/*.md` gives the same count per file as `grep -c "checker" book/en/*.md` (7: 1, 11: 1, 15: 9, 16: 8, 23: 1), and `grep -n "verificador" book/pt/*.md` finds only chapter 16's lint gloss.
* [x] `git diff --stat book/` empty.
* [x] No em dash; `make verify` green (build, parity, em dash, prose, width, links, disclosure).
* [x] The Delivery review ran on this delivery's paths and the files it created (docs/05 §5), and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable.
* [x] Page moved to `work/done/`, the line `[x]`, docs/03 staged by hunk and this line's hunk of docs/06; the commit message suggested, `docs(docs03-checker-pt): ...`.

**Built.** docs/03's `candidate` row gives the labels their Portuguese words, visto, latente and fraco, and a new `checker` row after it gives "conferente" and what the checker does; both with the Contract's exact text. No chapter changed.

**Decisions at apply time.** None beyond the page's. No Case A or Case B passage.

**Divergences and omissions.** Decision 1 and the Contract say chapters 8 and 15 write the three labels; chapter 8 writes only "visto" (both editions name neither latent nor weak there), and chapter 15 writes all three. docs/03's words stand, since they are chapter 15's and chapter 8's "visto" agrees; the page's claim is corrected here rather than in its decision.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure). `grep -c` gives "conferente" in Portuguese as often as "checker" in English per chapter (7: 1, 11: 1, 15: 9, 16: 8, 23: 1); "verificador" appears only in chapter 16's lint gloss; `git diff --stat book/` is empty.

**Delivery review.** One read-only agent on Opus read this delivery's hunk of docs/03 and its line of docs/06 against this page, docs/04, docs/05 §§5 and 8 and the Portuguese chapters. No finding in the edits: both match the Contract, no other row changed, no em dash, and the checker row agrees with §8 and the Milestone review slot. One finding on the page, chapter 8's labels, recorded above under Divergences.

**Kit note for the author.** `kit:` the kit's Portuguese changelog calls the checker "verificador", where the book says "conferente" (decision 2).

```commit
docs(docs03-checker-pt): fix the checker and its labels' Portuguese words

- docs/03's candidate row gives seen, latent and weak as visto, latente, fraco
- A new checker row: conferente, who it is, what it marks, that it fixes nothing
- No chapter changes: the Portuguese edition already uses these words

work/done/docs03-checker-pt.md
```
