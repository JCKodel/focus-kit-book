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

* [x] In a scratch clone, each Behaviour case above prints the finding stated, or nothing, and the three note cases (uppercase key, mid-line colon, definition line) print nothing before the change: both outputs recorded on the page.
* [x] `python3 scripts/check_parity.py` prints nothing on the clean tree.
* [x] `build_book.py` is unchanged and still builds.
* [x] docs/01's `check_parity.py` row says it also compares the two READMEs' heading levels and count, and its `markdown.py` row names the note patterns; docs/04 §Tests says the same in its parity sentence.
* [x] `make verify` is green.

**Decisions in the review.**

* README order is compared by the heading levels and count in sequence, not by words: the words differ by edition, and the chapters' parity already works so (docs/04 line 10, `check_parity.py`; recommendation of this session).
* The key is any run without whitespace, `^`, `[` or `]`, as pandoc reads a label, not a wider list: an uppercase or `_` key then counts as the build sees it.
* The shared pattern goes to `markdown.py` and `build_book.py` is left to `book-build-links`, not edited here: one file per line (the M14 review's table), so this page does not take that line's half of B8. The author should run this line before `book-build-links`.
* No test file: docs/04 §Tests; the proof lives on the page after `/apply`, as in `repo-files-any-name`.
* Pages in flight: none touches `scripts/check_parity.py`, `scripts/markdown.py` or the READMEs' sections. `renumber-chapters` edits README chapter links only (sections unchanged), which this check accepts; `quick-guide` and `one-gain-section` change chapters, not READMEs.

## What happened

**The error it catches** (docs/05 §7): parity read a note only when its key matched `[a-z0-9-]+` and no `:` followed the mention, so `[^Dora_1]` cited twice in one edition and once in the other, or `sentence[^a]: more` in one edition only, passed in silence (finding B8); and it never opened a README, so `README.pt.md` could gain, lose or demote a section with no finding (finding B10).

**Built.** `scripts/markdown.py` holds `NOTE_DEFINITION`, `NOTE_MENTION` and `mentions(line)` as the Contract writes them. `scripts/check_parity.py` imports them: `notes(path)` reads the masked lines once, counts `mentions(line)` and takes a key's location from its first mention, else from its first definition line (`NOTE_DEFINITION`). `main()` compares the README pair after the chapters. `compare`, the finding format and exit 1 are unchanged.
docs/01: the `check_parity.py` row names the README pair and "whatever the key"; the `markdown.py` row names the three note names. docs/04 §Tests: a parity sentence before the strict build's.
The abstraction: the note pattern's first occurrence is `check_parity.py` (its old `NOTE_REF`), the second `build_book.py:49-50`; it moved to `markdown.py`, and `build_book.py` is left to `book-build-links`, as the page says. A second one: "the one of the pair that is missing" was written once, in the chapter loop (the first); the README pair is the second, so both go through one function, `pair(en, pt)`.

**Diverged from the contract.** Nothing in behaviour. Two choices in form, below under Decisions: `pair(en, pt)` instead of writing the counterpart findings inline in `main()`, and the definition lines read from the masked text instead of the raw text.

**Proof.** A scratch clone of this repository at the commit before this delivery (8c4183b). A script writes each case's pair as a new chapter, `book/en/90-proof.md` and `book/pt/90-proof.md` (no front matter, so status `none` on both sides), runs `python3 scripts/check_parity.py` and removes the pair; the README cases edit the clone's README and restore it with `git checkout`. The cases, English first, Portuguese second, `\n` a new line:

* 2: `A claim.[^Dora_1]\nAgain.[^Dora_1] And.[^Key.2]\n\n[^Dora_1]: Source.\n[^Key.2]: Other.` against `Uma afirmação.[^Dora_1]\nDe novo. E.\n\n[^Dora_1]: Fonte.\n[^Key.2]: Outra.`
* 3: `A sentence[^a]: more.\n\n[^a]: Source.` against `Uma frase: mais.\n\n[^a]: Fonte.`
* 4a: `A claim.[^a]\n\n[^a]: Source.[^b]\n[^b]: Other.` against `Uma afirmação.[^a]\n\n   [^a]: Fonte.[^b]\n[^b]: Outra.` (the definition indented three spaces, a mention after its marker on both sides)
* 4b: the same English against `Uma afirmação.[^a]\n\n  [^a]: Fonte.\n  [^b]: Outra.` (the mention of `[^b]` missing, the definitions indented)
* 5: `One.[^a b] Two.[^a b]` against `Um.[^a b]`
* 6: front matter `title: "[^z]"`, then ``Code `[^z]`, [link](https://example.com/[^z]) <!-- [^z] -->`` and a fenced block holding `[^z]`, against the same front matter without the key and no `[^z]` at all
* 7: `\n## Extra\n` appended to `README.pt.md`; 8: `## Ler` made `### Ler`; 9: a fenced block holding `# not a heading` appended to `README.pt.md`; 10: `README.pt.md` deleted; 11: `README.md` deleted

Before the change (the clone's own scripts):

```
== 0 clean tree
$ python3 scripts/check_parity.py
[exit 0]
== 1 the old pattern and mentions() on: A claim.[^Dora_1]: and more[^a]: x
NOTE_REF: []
== 2 [^Dora_1] cited twice in English, once in Portuguese; [^Key.2] once and none
$ python3 scripts/check_parity.py
[exit 0]
== 3 a mention followed by a colon mid-line, in English only
$ python3 scripts/check_parity.py
[exit 0]
== 4a definition lines, the Portuguese one indented, each with a mention after the marker
$ python3 scripts/check_parity.py
[exit 0]
== 4b the same, the mention of [^b] missing in Portuguese: the indented definition is the location
$ python3 scripts/check_parity.py
book/pt/90-proof.md:1: parity: [^b] cited 0 times, 1 in book/en/90-proof.md
[exit 1]
== 5 a key with whitespace, twice in English, once in Portuguese
$ python3 scripts/check_parity.py
[exit 0]
== 6 [^z] in front matter, inline code, a link target, an HTML comment and a fence, English only
$ python3 scripts/check_parity.py
[exit 0]
== 7 README.pt.md with seven headings
$ python3 scripts/check_parity.py
[exit 0]
== 8 README.pt.md with ### where English has ##
$ python3 scripts/check_parity.py
[exit 0]
== 9 a # line inside a fenced block of README.pt.md
$ python3 scripts/check_parity.py
[exit 0]
== 10 README.pt.md missing
$ python3 scripts/check_parity.py
[exit 0]
== 11 README.md missing
$ python3 scripts/check_parity.py
[exit 0]
```

After the change (this delivery's `scripts/markdown.py` and `scripts/check_parity.py` copied into the clone):

```
== 0 clean tree
$ python3 scripts/check_parity.py
[exit 0]
== 1 the old pattern and mentions() on: A claim.[^Dora_1]: and more[^a]: x
mentions: ['Dora_1', 'a']
== 2 [^Dora_1] cited twice in English, once in Portuguese; [^Key.2] once and none
$ python3 scripts/check_parity.py
book/pt/90-proof.md:1: parity: [^Dora_1] cited 1 times, 2 in book/en/90-proof.md
book/pt/90-proof.md:5: parity: [^Key.2] cited 0 times, 1 in book/en/90-proof.md
[exit 1]
== 3 a mention followed by a colon mid-line, in English only
$ python3 scripts/check_parity.py
book/pt/90-proof.md:3: parity: [^a] cited 0 times, 1 in book/en/90-proof.md
[exit 1]
== 4a definition lines, the Portuguese one indented, each with a mention after the marker
$ python3 scripts/check_parity.py
[exit 0]
== 4b the same, the mention of [^b] missing in Portuguese: the indented definition is the location
$ python3 scripts/check_parity.py
book/pt/90-proof.md:4: parity: [^b] cited 0 times, 1 in book/en/90-proof.md
[exit 1]
== 5 a key with whitespace, twice in English, once in Portuguese
$ python3 scripts/check_parity.py
[exit 0]
== 6 [^z] in front matter, inline code, a link target, an HTML comment and a fence, English only
$ python3 scripts/check_parity.py
[exit 0]
== 7 README.pt.md with seven headings
$ python3 scripts/check_parity.py
README.pt.md:49: parity: 7 headings, English has 6
[exit 1]
== 8 README.pt.md with ### where English has ##
$ python3 scripts/check_parity.py
README.pt.md:11: parity: heading level 3, English has level 2 at README.md:11
[exit 1]
== 9 a # line inside a fenced block of README.pt.md
$ python3 scripts/check_parity.py
[exit 0]
== 10 README.pt.md missing
$ python3 scripts/check_parity.py
README.md:1: parity: no Portuguese counterpart README.pt.md
[exit 1]
== 11 README.md missing
$ python3 scripts/check_parity.py
README.pt.md:1: parity: no English counterpart README.md
[exit 1]
```

Every Behaviour case prints the finding the page states, or nothing. Before the change, the uppercase key (2), the mid-line colon (3), the definition lines (4a) and every README case (7 to 11) printed nothing; 4b printed its finding at line 1, since the old fallback did not read an indented definition, and now prints it at the definition's line 4. Case 7's line 49 is the last line of the edited `README.pt.md`.
In this repository, `python3 scripts/check_parity.py` prints nothing and exits 0; `make verify` is green; `scripts/build_book.py` has no diff and `make book` builds the PDF and EPUB of both editions.

**Dropped.** Nothing.

**Decisions.**

* `pair(en, pt)` holds the "compare when both exist, else the missing one's finding" rule for the chapters and the README pair, instead of the Contract's inline `main()` ending: the rule's second occurrence, and the findings are the ones the Behaviour states, the chapters' unchanged.
* Neither README present prints nothing: the Behaviour names only one missing, and with neither there is no pair to compare (decided in this session, not asked).
* The fallback location reads `NOTE_DEFINITION` on the masked lines, not on the raw text as before: a definition inside a fenced block is code and is not read, as the Behaviour says of code; the location of a mention still wins over a definition's, as before.
* The definition-line case of the Done when is proved by 4a, a pair that prints nothing before and after, plus 4b for the fallback location; a mention after a definition marker was already counted before, so no input makes that case print a finding only after the change.
* No screenshot: docs/05 §5 asks one of a toolchain delivery's rendered site, and this one changes nothing the site renders; the proof is the scratch clone, as the page says.
* `book-build-links` keeps `· after parity-notes-readmes` and is now free: an order, not a block (docs/05 §4).
* No ADR: the check applies docs/04 §Languages to the READMEs and changes no decision.

```commit
fix(parity-notes-readmes): count every note, compare the READMEs

- markdown.py: NOTE_DEFINITION, NOTE_MENTION and mentions, any key pandoc reads
- check_parity counts a mention whatever its key and whatever follows it
- check_parity fails when README.pt.md's headings differ from README.md's
- docs/01 and docs/04 §Tests say so

work/done/parity-notes-readmes.md
```
