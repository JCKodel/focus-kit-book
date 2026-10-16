# entry-apostrophes

**Objective.** A plain entry of the prose rules or of the disclosure list that holds an apostrophe, `'` or `’`, matches text written with either one, as docs/04 §Prose rules already says.

**Behaviour.**

* The plain entry `don't` finds `don't` and `Don’t`; the entry `don’t` finds both too. Today each finds only its own.
* The plain entry `o'brien` in the disclosure list finds `O’Brien` in a file and in a path, with the matched part masked as `***` in the path, as for any entry.
* An entry with several apostrophes (`rock 'n' roll`) matches each of them independently: `rock ’n' roll` is found.
* An entry that ends in an apostrophe (`students'`) finds `students’`; one that starts with an apostrophe (`'tis`) finds `’tis`. Neither gets a word boundary on that side, as today.
* The whole-word rule is unchanged: `don't` does not match inside `abdon’t`, and case is ignored.
* An entry with no apostrophe (`acme`, `10.0.0.`) compiles to the same pattern as today.
* A `re:` entry is not rewritten: `re:don't` finds `don't` and not `don’t`; the entry that wants both writes `re:don(’|')t`, as the entries of docs/04 do. An invalid `re:` entry still raises `re.error`, which both callers report as `invalid regular expression`.
* The other quotation marks, `‘` and the double quotes, are not apostrophes and are not matched.
* `make verify` on the book as it stands gives the same output: no plain entry of docs/04 holds an apostrophe today.

**Contract.**

`scripts/patterns.py`, `compile_entry(entry)`, signature and exceptions unchanged.

* A plain entry is split on `'` and `’`; each part goes through `re.escape`; the parts are joined with the class `['’]`. The boundary rule is applied to the first and last characters of the original entry as now: `(?<!\w)` when the first is a word character, `(?!\w)` when the last is. The result is compiled with `re.IGNORECASE`.
* A `re:` entry is compiled as is.

Documents, in the same delivery: docs/04 line 56 says "In a plain entry, `'` and `’` are both apostrophes and match either; a `re:` entry spells both, as `(’|')`" (today it says "the entries that hold one accept either", true of none that is a `re:`); docs/01's `scripts/patterns.py` row (line 37) adds "an apostrophe of a plain entry matches either".

**Out of scope.**

* Rewriting the apostrophes inside a `re:` entry: a pattern is the author's own, and a class such as `[']` would break under a rewrite.
* Normalising the scanned text instead of the entry: every file would be rewritten in memory for a rule that only entries need.
* The accented-letter and case rules of the matcher.

**Done when.**

* [ ] A scratch check of `compile_entry` covers each Behaviour line, its output recorded on the page: there is no test directory, and docs/04 §Tests says the checks are the tests (the entries of docs/04 and a made-up disclosure list run through `check_prose.py` and `check_disclosure.py`).
* [ ] `make verify` green, with the same output on the current book; no output shows a term of the real list.
* [ ] docs/04 line 56 and docs/01 line 37 updated.

**Decisions in the review.**

* Only plain entries are made apostrophe-blind; `re:` entries are left alone. docs/04 says "the entries that hold one", and its own `re:` entries already spell `(’|')` out, which they would not need if the code did it (docs/04 §Prose rules; recommendation of this session).
* The fix is in `compile_entry`, so the prose rules and the disclosure list change together; that is the first and only change to this shared function, so no new abstraction (docs/05 abstraction rule).
* `‘` is left out: docs/04 names two apostrophes only.
* The finding is latent (B11 of `m14-review`), so the delivery adds no entry to docs/04.
