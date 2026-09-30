# pt-health-slice

**Objective.** A Portuguese reader of chapter 14 reads the server check of the first milestone as the English means it: the slice that asks whether the server answers, not a slice for health data, which the clinic's product rules exclude (chapter 7).

**Behaviour.**

* Chapter 14's Portuguese sentence on the server check reads: "A [fatia de health](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone/src/features/health), a verificação do servidor do primeiro marco, tem 6 arquivos:". Only "fatia de saúde" changes; the link and the rest of the sentence stay.
* "fatia de health" is the form chapter 10 already uses (pt/10:110).
* No "fatia de saúde" is left in the Portuguese edition. Every other "saúde" means health data and stays (chapter 7).
* The English edition is unchanged: "health slice" already means the server check.
* Finding F6 of the M4 review is settled.

**Contract.**

* Files: `book/pt/14-errors-and-slices.md`, the sentence quoted above (line 56 today), those two words only. `ch14-feature-boundary`, in flight, replaces line 53 and may move this line, so the quoted sentence is the reference, not the line number.
* Terms of docs/03: none new. As in `pt-slot-term` (the first occurrence), a translation choice for the clinic's code goes on the page and not into docs/03: docs/03 holds the book's own vocabulary.
* Sources, cases, exercises: unchanged.

**Out of scope.**

* "fatia `health`" at pt/11:129 and pt/15:420: neither reads as medical data. The author kept chapter 14 only.
* Chapter 10's "fatia de health" (pt/10:110): it is already the chosen form.
* A docs/03 row for the term: see Contract.
* The English edition: nothing to change.
* The other chapter 14 lines in flight (`ch14-feature-boundary`, `ch14-refusal-io`, `ch14-catch-all`): none of them touches this sentence.

**Done when.**

* [x] The sentence changed; `grep -rn "fatia de saúde" book/pt` finds nothing.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author: run once at the end of the M4.1 loop by the driver, on 2026-09-30, both PDFs built
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* The sentence changed as written, now at line 59 of chapter 14 after `ch14-feature-boundary`; only "saúde" became "health", link and rest unchanged. The grep finds nothing in the Portuguese edition.
* The English edition and docs/03 are untouched, as planned.
* `make verify` green. Staging and the commit are left to the driver of the M4.1 loop.
