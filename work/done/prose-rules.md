# prose-rules

**Objective.** The author runs `make verify` and it fails, naming the file, the line, the rule and what to do instead, when a text a reader reads (either edition of the book, or either README) contains a pattern that makes prose read as machine-written. The rules are written once, in docs/04.

**Behaviour.**

* docs/04 has a section `## Prose rules` with seven rules, each with its id, what to do instead, and its patterns for English, Portuguese or both: `filler`, `inflated`, `not-but`, `reveal`, `intensifier`, `exclamation`, `emoji`.
* On the clean tree, `python3 scripts/check_prose.py` prints nothing and exits 0.
* A line in `book/en/*.md` or `README.md` that matches an English pattern (or a `both` one) prints `file:line: prose: <id>: "<matched text>": <instead>` and exits 1. The same goes for `book/pt/*.md` and `README.pt.md` with the Portuguese patterns.
* A pattern in one language does not fire in the other edition: `as we saw` in `book/pt` is no finding.
* Text inside fenced code blocks, inline code, link and image targets, HTML comments and the front matter is not checked, because an artifact shown is real and is not rewritten to please a rule. Line numbers still count those lines.
* Adding a pattern to docs/04 is enough to make the check use it: nothing in `scripts/` changes.
* A malformed docs/04 section (missing, no rule, a rule with no message, an invalid `re:`) is a finding at its docs/04 line, and the check exits 1.
* `make verify` runs build, parity, em dash, prose, disclosure, in that order, and stops at the first failing group.

**Contract.**

Files:

```
docs/04-Conventions.md    section "## Prose rules": the rules, the only source of the patterns
scripts/check_prose.py    rule "prose"; Python 3 standard library only
scripts/patterns.py       compile_entry(entry) -> re.Pattern, moved out of check_disclosure.py
scripts/check_disclosure.py  imports compile_entry; behaviour unchanged
Makefile                  verify runs python3 scripts/check_prose.py after the em dash check
docs/01-Architecture.md   tree and the make verify row updated
```

`compile_entry` is the second concrete occurrence of the entry syntax (the first is `check_disclosure.py`, delivery `disclosure-scan`):
a plain entry is `re.escape(entry)` with `re.IGNORECASE`, `(?<!\w)` in front when its first character is a word character and `(?!\w)` after when its last one is; `re:<pattern>` is compiled as is, with `re.IGNORECASE`.

Format of the docs/04 section, parsed by the script:

```
## Prose rules

<free prose: why these rules exist; not parsed>

### <id>

<one line: what to do instead; this line is the finding's message>

* en: `<entry>`, `<entry>`
* pt: `<entry>`
* both: `<entry>`
```

* The section runs from `## Prose rules` to the next `## ` heading or the end of the file.
* A rule is a `### <id>` heading, with `<id>` in `[a-z-]+`. Its message is the first non-empty line after the heading that is not a bullet.
* A pattern line is a bullet starting with `* en:`, `* pt:` or `* both:`. Every backtick span on it is one entry, in the syntax of `compile_entry`. Any other line in a rule is prose and is not parsed.

The seed, as the author approved it (docs/04 may say it more clearly; the entries are exact, and `’|'` accepts both apostrophes):

| id | message | en | pt |
|---|---|---|---|
| `filler` | say it; do not announce, recap or clear your throat | `re:in this chapter,? (we\|you) will`, `as we saw`, `as we have seen`, `as mentioned`, `it is worth noting`, `re:it(’\|')s worth noting`, `it is important to note`, `re:let(’\|')s dive`, `without further ado`, `in conclusion`, `in summary`, `to sum up` | `re:neste capítulo,? (vamos\|você vai)`, `como vimos`, `como mencionado`, `vale ressaltar`, `vale notar`, `vale destacar`, `re:é importante (notar\|destacar\|ressaltar)`, `sem mais delongas`, `em conclusão`, `em resumo`, `resumindo` |
| `inflated` | use the plain word | `re:\bdelv(e\|es\|ed\|ing)\b`, `tapestry`, `testament to`, `re:\bseamless(ly)?\b`, `re:\bleverag(e\|es\|ed\|ing)\b`, `re:\bunlock(s\|ed\|ing)?\b`, `re:\bempower(s\|ed\|ing\|ment)?\b`, `pivotal`, `game-changer`, `game changer`, `ever-evolving`, `fast-paced`, `cutting-edge`, `realm` | `re:\bmergulh(ar\|amos\|e\|o)\b`, `tapeçaria`, `re:\balavanc(ar\|a\|am\|ando)\b`, `re:\bpotencializ\w*`, `re:\bempoder\w*`, `divisor de águas`, `em constante evolução`, `de ponta` |
| `not-but` | say what it is; do not set it against what it is not | `re:\bnot (just\|only\|merely)\b.*\bbut\b`, `re:\bit(’\|')?s not\b.*\bit(’\|')?s\b`, `re:\b(is\|are)n(’\|')?t (just\|only\|merely)\b` | `re:\bnão (é \|são )?(apenas\|só\|somente\|simplesmente)\b.*\b(mas\|é\|são)\b` |
| `reveal` | state the point; do not stage it with a question or a teaser | `re:^[a-z]\w*(\s\w+){0,2}\?$`, `re:here(’\|')s (the thing\|why\|how\|what)`, `here is the thing` | `re:^[a-zà-ú]\w*(\s\w+){0,2}\?$`, `eis o segredo`, `eis por que`, `eis o porquê` |
| `intensifier` | cut the intensifier; the fact carries the weight | `truly`, `incredibly`, `absolutely`, `genuinely` | `verdadeiramente`, `incrivelmente`, `absolutamente`, `genuinamente` |
| `exclamation` | end with a full stop | both: `re:(?<![!<])!(?![!\[-])` (not `![` images, `!!!` admonitions or `<!--`) | |
| `emoji` | remove the emoji | both: `re:[\U0001F300-\U0001FAFF☀-➿]` | |

In the table `\|` stands for `|`: docs/04 writes the entries as bullets, not as a table, so no escaping is needed there.
Plain entries get their word boundaries from `compile_entry`; `re:` entries carry `\b` themselves where they need it.

`scripts/check_prose.py`:

* Files and language: from `repo_files()`, `book/en/**/*.md` and `README.md` are `en`; `book/pt/**/*.md` and `README.pt.md` are `pt`. Other files are not read.
* Each file is read as UTF-8. Before matching, a copy of each line has these replaced by spaces: the front matter (a first line `---` up to the next `---`), fenced code blocks (from a line starting with ```` ``` ```` or `~~~` to its closing fence), inline code spans, link and image targets `](…)`, and HTML comments `<!-- … -->`, including multi-line ones. Line numbers are those of the file.
* Each remaining line, stripped of surrounding whitespace, is matched against every entry of its language and every `both` entry. Each match is one finding; a line may give several.
* Output on stdout, one line per finding, and exit 1 when there is any:

```
<file>:<line>: prose: <id>: "<matched text>": <message>
docs/04-Conventions.md:1: prose: section "## Prose rules" missing or has no rule
docs/04-Conventions.md:<line>: prose: rule <id> has no message
docs/04-Conventions.md:<line>: prose: invalid regular expression
```

* The matched text can be printed: the patterns are public, unlike the disclosure list.

Examples on this page are for the rules; this page lives in `work/`, which the check does not read.

**Out of scope.**

* One sentence per line: not an anti-AI rule and a heuristic; `chapter-template` decides it.
* `docs/` and `work/`: process documents use spec prose on purpose, and they hold the patterns themselves.
* An allowlist or an inline escape: added when the first false positive happens (docs/05 §7); code spans already cover quoted artifacts.
* Style judgements no pattern can see (rhythm, the rule of three, uniform paragraph length): the milestone review reads for them (docs/05 §8).
* Merging the em dash check into this one: it covers every text file, not only what a reader reads, and already works.

**Done when.**

* [x] docs/04 has the `## Prose rules` section with the seven rules and a short paragraph on why; its `Anti-AI prose rules` bullet points to it.
* [x] With an untracked `book/en/99-probe.md` and `book/pt/99-probe.md` holding one line per rule, every rule fires in its language, with the output above and exit 1; the same lines inside a code fence, an inline code span, a link target, an HTML comment and the front matter give no finding; an English pattern in the pt probe gives none. Output recorded on this page; probes removed.
* [x] A rule with no message, an invalid `re:` entry and a missing section each give their docs/04 finding and exit 1 (on a scratch copy, restored).
* [x] `make scan` behaves as before after `compile_entry` moves (its recorded proof re-run with the made-up entries).
* [x] The existing chapters and both READMEs pass; any finding there is fixed in both editions and recorded here.
* [x] `make verify` green; with a probe planted, it stops at prose.
* [x] docs/01 and docs/04 updated; docs/06 line marked `[x]`.

**What happened.**

Diverged from the plan:

* docs/04 says each rule once, as the page asked; the `reveal` and `exclamation` rules carry one prose line under the message ("a line that is only a question of up to three words", "skips `![`, `!!!` and `<!--`"), which the parser ignores.
* The `make scan` proof used fresh made-up entries (`quuxbar`, `198.51.100.`, `re:qx-\d{4}`): `work/done/disclosure-scan.md` records its own entries, so a list with them finds that page, as it should.

Nothing dropped.

The proof found:

```
clean tree                       python3 scripts/check_prose.py: no output, exit 0; 66 entries in 7 rules

book/en/99-probe.md and book/pt/99-probe.md, untracked, one line per rule, then the same
lines in a fence (``` in en, ~~~ in pt), an inline code span, a link target, an HTML comment
(one-line, and multi-line in en) and the front matter; the pt probe also holds an English line:
book/en/99-probe.md:7: prose: filler: "As we saw": say it; do not announce, recap or clear your throat
book/en/99-probe.md:8: prose: inflated: "leverage": use the plain word
book/en/99-probe.md:9: prose: not-but: "not just a check but": say what it is; do not set it against what it is not
book/en/99-probe.md:10: prose: reveal: "Why?": state the point; do not stage it with a question or a teaser
book/en/99-probe.md:11: prose: intensifier: "truly": cut the intensifier; the fact carries the weight
book/en/99-probe.md:12: prose: exclamation: "!": end with a full stop
book/en/99-probe.md:13: prose: emoji: "🚀": remove the emoji
book/pt/99-probe.md:7: prose: filler: "Como vimos": say it; do not announce, recap or clear your throat
book/pt/99-probe.md:8: prose: inflated: "alavancar": use the plain word
book/pt/99-probe.md:9: prose: not-but: "Não é apenas uma verificação, mas": say what it is; do not set it against what it is not
book/pt/99-probe.md:10: prose: reveal: "Por quê?": state the point; do not stage it with a question or a teaser
book/pt/99-probe.md:11: prose: intensifier: "verdadeiramente": cut the intensifier; the fact carries the weight
book/pt/99-probe.md:12: prose: exclamation: "!": end with a full stop
book/pt/99-probe.md:13: prose: emoji: "🚀": remove the emoji
                                 exit 1; nothing from the masked lines, nothing from "As we saw, this is truly pivotal." in pt

scratch edits of docs/04, restored after each:
intensifier message removed, and a `re:` entry made invalid:
docs/04-Conventions.md:45: prose: invalid regular expression
docs/04-Conventions.md:64: prose: rule intensifier has no message
                                 exit 1
heading renamed:                 docs/04-Conventions.md:1: prose: section "## Prose rules" missing or has no rule, exit 1
section with prose and no rule:  the same finding, exit 1

make scan, list quuxbar (entry 3), 198.51.100. (entry 4), re:qx-\d{4} (entry 5):
planted.md and notes-quuxbar.png, untracked:
notes-***.png:1: disclosure: file path matches list entry 3
planted.md:2: disclosure: matches list entry 3
planted.md:3: disclosure: matches list entry 4
planted.md:3: disclosure: matches list entry 5
                                 exit 2 from make; removed, exit 0
empty list, invalid re:, no list, CI=true with no list: exit 1, 1, 0 (skipped), 1, as recorded before
```

* `planted.md` line 2 held `Quuxbar`, `QUUXBAR Ltd` and `quuxbarology`: one finding, the whole-word rule still holds after the move.
* The existing chapters, both `index.md` and both READMEs pass: nothing to fix.
* `make verify` green with the real list; with `It works!` planted in `book/en/99-probe.md` (and a clean pt twin, so parity passes) it ran build, parity and em dash, then stopped at `book/en/99-probe.md:3: prose: exclamation: "!": end with a full stop`, exit 2 from make; removed, green.
* No screen changes, so no screenshot: the proof is the runs above.

Decisions: a `### ` heading whose id is not `[a-z-]+` is prose, not a rule; a finding in docs/04 does not stop the check, which still reports the files with the rules that compiled. No ADR.

Documents this delivery changed: docs/04 (§Prose rules, the Anti-AI bullet), docs/01 (tree, `make verify`, the `__pycache__/` line), docs/06.
