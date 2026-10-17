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

* [x] A scratch check of `compile_entry` covers each Behaviour line, its output recorded on the page: there is no test directory, and docs/04 §Tests says the checks are the tests (the entries of docs/04 and a made-up disclosure list run through `check_prose.py` and `check_disclosure.py`).
* [x] `make verify` green, with the same output on the current book; no output shows a term of the real list.
* [x] docs/04 line 56 and docs/01 line 37 updated.

**Decisions in the review.**

* Only plain entries are made apostrophe-blind; `re:` entries are left alone. docs/04 says "the entries that hold one", and its own `re:` entries already spell `(’|')` out, which they would not need if the code did it (docs/04 §Prose rules; recommendation of this session).
* The fix is in `compile_entry`, so the prose rules and the disclosure list change together; that is the first and only change to this shared function, so no new abstraction (docs/05 abstraction rule).
* `‘` is left out: docs/04 names two apostrophes only.
* The finding is latent (B11 of `m14-review`), so the delivery adds no entry to docs/04.

**Proof.**

A scratch script in the scratchpad calls `compile_entry` on each Behaviour line, keeps a copy of the function as it was to compare patterns, loads a made-up disclosure list (`o'brien`, then the invalid `re:(`) with `check_disclosure.load` and runs `check_disclosure.scan_file` on the path `notes/O’Brien-letter.md` with a line `Dear O’Brien,`. It then compiles every entry of docs/04's prose rules, and every entry of the real disclosure list printing only counts, with both versions of the function.

Before the change:

```
== matches: entry | text | found
"don't"            "don't"                  True
"don't"            'Don’t'                  False
'don’t'            "don't"                  False
'don’t'            'Don’t'                  True
"rock 'n' roll"    "rock ’n' roll"          False
"rock 'n' roll"    'Rock ’n’ Roll'          False
"students'"        'the students’ books'    False
"'tis"             '’tis the season'        False
"don't"            'abdon’t'                False
"don't"            'don’tcha'               False
"re:don't"         "don't"                  True
"re:don't"         'don’t'                  False
"re:don(’|')t"     'don’t'                  True
"re:don(’|')t"     "don't"                  True
"don't"            'don‘t'                  False
"don't"            'don"t'                  False
"don't"            'don“t'                  False
"don't"            'don”t'                  False
'acme'             'ACME corp'              True
== no apostrophe: same pattern as before
'acme'             True
'10.0.0.'          True
're:foo\\d+'       True
'a.b-c'            True
'-x'               True
== pattern of a plain entry with apostrophes
"don't"            (?<!\w)don't(?!\w)
"rock 'n' roll"    (?<!\w)rock\ 'n'\ roll(?!\w)
"students'"        (?<!\w)students'
"'tis"             'tis(?!\w)
== invalid re: entry
re:( raises re.error
== disclosure list, made up: o'brien
made-up-list.txt:2: disclosure: invalid regular expression
== docs/04 entries: compiled pattern unchanged
66 entries, 0 changed: []
plain entries holding an apostrophe: []
== real disclosure list: counts only
44 entries, 0 with a changed pattern
```

After the change:

```
== matches: entry | text | found
"don't"            "don't"                  True
"don't"            'Don’t'                  True
'don’t'            "don't"                  True
'don’t'            'Don’t'                  True
"rock 'n' roll"    "rock ’n' roll"          True
"rock 'n' roll"    'Rock ’n’ Roll'          True
"students'"        'the students’ books'    True
"'tis"             '’tis the season'        True
"don't"            'abdon’t'                False
"don't"            'don’tcha'               False
"re:don't"         "don't"                  True
"re:don't"         'don’t'                  False
"re:don(’|')t"     'don’t'                  True
"re:don(’|')t"     "don't"                  True
"don't"            'don‘t'                  False
"don't"            'don"t'                  False
"don't"            'don“t'                  False
"don't"            'don”t'                  False
'acme'             'ACME corp'              True
== no apostrophe: same pattern as before
'acme'             True
'10.0.0.'          True
're:foo\\d+'       True
'a.b-c'            True
'-x'               True
== pattern of a plain entry with apostrophes
"don't"            (?<!\w)don['’]t(?!\w)
"rock 'n' roll"    (?<!\w)rock\ ['’]n['’]\ roll(?!\w)
"students'"        (?<!\w)students['’]
"'tis"             ['’]tis(?!\w)
== invalid re: entry
re:( raises re.error
== disclosure list, made up: o'brien
made-up-list.txt:2: disclosure: invalid regular expression
notes/***-letter.md:1: disclosure: file path matches list entry 1
notes/***-letter.md:2: disclosure: matches list entry 1
== docs/04 entries: compiled pattern unchanged
66 entries, 0 changed: []
plain entries holding an apostrophe: []
== real disclosure list: counts only
44 entries, 0 with a changed pattern
```

Each apostrophe line of the Behaviour turns from `False` to `True`; the whole-word lines (`abdon’t`, `don’tcha`), the `re:` lines, the other quotation marks and the entries with no apostrophe print the same before and after. The made-up `o'brien` finds the path, masked as `***`, and the line; before, it found neither. No entry of docs/04 and none of the 44 of the real list compiles to a different pattern, so the change is latent on the book today.

`make verify` printed the same lines before and after the change, and is green.

**Noted, not fixed.** Nothing.

**Dropped.** Nothing.

**Decisions.**

* The manual `docs/manuals/set-up-the-disclosure-list.md` says the same in its step 1, where it gives the entry syntax to the person writing the list: the page named docs/04 and docs/01 only, but the manual is where that person reads the rule (docs/05 §5, Manuals; decision of this session).
* The apostrophe class is the literal `['’]` joined between the escaped parts, and the split uses a module constant `APOSTROPHES`: one place says which characters are apostrophes.
* No ADR: the change makes the code do what docs/04 already said.

```commit
fix(entry-apostrophes): match either apostrophe in a plain list entry

- a plain entry's `'` or `’` matches either, in the prose rules and the disclosure list
- `re:` entries compile as written
- docs/04, docs/01 and the disclosure list manual say so

work/done/entry-apostrophes.md
```
