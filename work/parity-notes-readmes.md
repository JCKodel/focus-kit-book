# parity-notes-readmes

**Objective.** The author runs `make verify` and it fails when the two editions cite a note a different number of times, whatever the note's key looks like or what follows its mention, and when the two READMEs do not have the same sections in the same order (docs/04 §Languages); today neither is seen.

**Behaviour.**

The proof uses a scratch clone with scratch edits, never the tree, as `repo-files-any-name` does.

* On the clean tree, `python3 scripts/check_parity.py` prints nothing and exits 0. Checked read-only before this page: both READMEs have six headings at levels 1, 2, 2, 2, 2, 2; no note key in the book falls outside `[a-z0-9-]`, and no mention is followed by `:`. The stricter check therefore changes nothing on today's tree and nothing is fixed in a text.
* Finding B8 holds, seen by running `NOTE_REF` on `A claim.[^Dora_1]: and more[^a]: x`: it returns no key. So a key with an uppercase letter, `_` or `.` (`[^Dora_1]`, `[^Key.2]`) is never counted, and a mention followed by `:` mid-line (`more[^a]: x`) is never counted either.
* A note cited twice in `book/en/NN-<slug>.md` as `[^Dora_1]` and once in the Portuguese file prints `book/pt/NN-<slug>.md:<line>: parity: [^Dora_1] cited 1 times, 2 in book/en/NN-<slug>.md` and exits 1. Today the same files print nothing.
* A mention followed by a colon inside a line (`sentence[^a]: more`) counts as one citation of `a`.
* A line that starts with `[^a]:` (up to three spaces before it) is a definition: it is not a citation, its key is the fallback location of a finding, and a mention later on that line (`[^a]: text[^b]`) counts as a citation of `b`.
* A key with whitespace (`[^a b]`) is not a note and is not counted, as pandoc reads it.
* Code, link targets, HTML comments and the front matter are not read, as today.
* README pair: `README.pt.md` with seven headings against six prints `README.pt.md:<last line>: parity: 7 headings, English has 6`; a `###` where the English has `##` prints `README.pt.md:<line>: parity: heading level 3, English has level 2 at README.md:<line>`.
* A `#` line inside a fenced block of a README is not a heading, as in a chapter.
* The headings' words are not compared: they are translated.
* A missing `README.pt.md` prints `README.md:1: parity: no Portuguese counterpart README.pt.md`; a missing `README.md`, `README.pt.md:1: parity: no English counterpart README.md`. Both exit 1 and neither raises.
* Finding B10 holds: `check_parity.py` never opens a README today (`main` lists `book/en` and `book/pt` only), though docs/04 line 10 requires the same sections in the same order.

**Contract.**

Files:

```
scripts/markdown.py        NOTE_DEFINITION, NOTE_MENTION and mentions(line), shared
scripts/check_parity.py    imports them; compares the README pair
docs/01-Architecture.md    the check_parity.py row and the markdown.py row
docs/04-Conventions.md     §Tests: parity names the READMEs and the note keys
```

`scripts/markdown.py`:

* `NOTE_DEFINITION = re.compile(r"^ {0,3}\[\^([^\]\s^\[]+)\]:")`
* `NOTE_MENTION = re.compile(r"\[\^([^\]\s^\[]+)\]")`
* `mentions(line) -> list[str]`: the keys cited on a masked line, in order; a definition marker at the start of the line (`NOTE_DEFINITION`) is cut off first and is not a citation.

`scripts/check_parity.py`: `notes(path)` counts with `mentions` over `mask(text, keep_targets=False)` and takes the fallback location from `NOTE_DEFINITION`; `main()` ends with `compare(README.md, README.pt.md)` when both exist, else the counterpart finding above. `compare` is unchanged: a README has no front matter, so its status is `none` on both sides, and it has no notes. The finding format, `file:line: parity: message`, and exit 1 do not change.

The abstraction: the note pattern is written twice, `check_parity.py:21` (the first) and `build_book.py:49-50` (the second), so it moves to `markdown.py` now. This delivery does not touch `build_book.py`: `book-build-links` replaces its two patterns with these names and so fixes the same finding (B8) in the book build. This line runs first.

**Out of scope.**

* `build_book.py`: `book-build-links` owns its half of B8 and imports `mentions`.
* Comparing README headings' words, links or table rows: translated, and docs/04 asks for sections and their order.
* A definition with no citation, or a citation with no definition: the strict build reports them.
* The parity of `docs/`, `work/` or ADRs: one language.

**Done when.**

* [ ] In a scratch clone, each Behaviour case above prints the finding stated, or nothing, and the three note cases (uppercase key, mid-line colon, definition line) print nothing before the change: both outputs recorded on the page.
* [ ] `python3 scripts/check_parity.py` prints nothing on the clean tree.
* [ ] `build_book.py` is unchanged and still builds.
* [ ] docs/01's `check_parity.py` row says it also compares the two READMEs' heading levels and count, and its `markdown.py` row names the note patterns; docs/04 §Tests says the same in its parity sentence.
* [ ] `make verify` is green.

**Decisions in the review.**

* README order is compared by the heading levels and count in sequence, not by words: the words differ by edition, and the chapters' parity already works so (docs/04 line 10, `check_parity.py`; recommendation of this session).
* The key is any run without whitespace, `^`, `[` or `]`, as pandoc reads a label, not a wider list: an uppercase or `_` key then counts as the build sees it.
* The shared pattern goes to `markdown.py` and `build_book.py` is left to `book-build-links`, not edited here: one file per line (the M14 review's table), so this page does not take that line's half of B8. The author should run this line before `book-build-links`.
* No test file: docs/04 §Tests; the proof lives on the page after `/apply`, as in `repo-files-any-name`.
* Pages in flight: none touches `scripts/check_parity.py`, `scripts/markdown.py` or the READMEs' sections. `renumber-chapters` edits README chapter links only (sections unchanged), which this check accepts; `quick-guide` and `one-gain-section` change chapters, not READMEs.
