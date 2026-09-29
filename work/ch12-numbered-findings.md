# ch12-numbered-findings

**Objective.** The English reader of chapter 12 matches each decision to its finding by number, as the Portuguese reader already does.

**Behaviour.**

* The English block of the ten summaries numbers each line, `1.` to `10.`, in the run's order, as the Portuguese block does.
* The sentence before the block says the numbers are added here so the decisions below can refer to them; the rest of each line stays as the run printed it.
* The Portuguese sentence before its block says the same about its numbers.
* Finding F18 of the M3 review is settled.

**Contract.**

* Files: `book/en/12-closing-a-milestone.md` lines 62 to 75 today; `book/pt/12-closing-a-milestone.md` line 62 today (the sentence only; its block is already numbered).
* Each English line becomes `N. "summary": "…",`, keeping the text after the number byte for byte, so it can still be compared with the record.
* Sources: the existing `[^closing-a-milestone-run]` note. Terms, cases, exercises: unchanged.

**Out of scope.**

* Dropping the `"summary":` prefix and the trailing commas in English: they show the output was JSON, and the Portuguese translation already dropped them.

**Done when.**

* [ ] English block numbered 1 to 10; text after each number unchanged.
* [ ] Both lead sentences say the numbers were added.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
