# site-build-anchors

**Objective.** The author runs `make build` or `make verify` and it fails, naming each line, when a chapter links to a heading that does not exist, on another chapter or on its own page; today the site builds and says nothing at warning level.

**Behaviour.**

The proof uses a scratch copy of the tree with scratch edits, never the tree itself. Finding B2 (site part) and B7 were re-read first and hold.

* Today (seen, run in the scratch copy without the block): a scratch line `[x](10-the-documents.md#no-such-heading)` in `book/en/02-how-agents-see.md` makes `mkdocs build --strict` print an `INFO` line and exit 0, so `make verify` stays green. A `[q](#nope-here)` to a heading of the page itself does the same.
* With the `validation:` block of the Contract, the same two lines are `WARNING`s, `--strict` aborts, and `scripts/build.py` prints, exit 1:

      book/en/02-how-agents-see.md:114: build: Doc file 'en/02-how-agents-see.md' contains a link '10-the-documents.md#no-such-heading', but the doc 'en/10-the-documents.md' does not contain an anchor '#no-such-heading'.
      book/en/02-how-agents-see.md:116: build: Doc file 'en/02-how-agents-see.md' contains a link '#nope-here', but there is no such anchor on this page.

* The Portuguese edition reports on its own: the same link in `book/pt/02-how-agents-see.md` prints a `book/pt/...` finding, whatever the English edition holds.
* A link to a heading that exists, `10-the-documents.md#one-place-per-fact`, prints nothing.
* B7, the same broken link on lines 114, 118 and 120 of one file prints three findings, one per line (MkDocs warns once for an anchor link however many times it stands in a file, so today the finding would sit on line 114 only). The same link twice on line 114 prints that line once.
* B7, a missing file linked on lines 94 and 96 (`[a](99-gone.md)`) prints two findings, at 94 and at 96; today both say 94 (MkDocs warns once for each occurrence of a missing file, and `locate` names the first line both times).
* B7, a link that is the start of a valid one is not found in it: a broken `10-the-documents.md#one-place` is reported on its own line and never on a line holding only `10-the-documents.md#one-place-per-fact`.
* A warning that names a file but no link keeps its line 1, and one that names no file keeps `mkdocs.yml:1`, as today.
* On today's tree `make build` prints nothing and exits 0. Checked read-only in a scratch copy with the block added: `book/` holds no link with `.md#` and none that starts `](#`, so no existing link can fail, and `scripts/build.py` exited 0. This is the tree as it is; a delivery of M15 that adds an anchor link answers for it in its own `make verify`.

**Contract.** `mkdocs.yml` gains, at the top level:

    validation:
      links:
        anchors: warn

The other validation keys keep their defaults; no case of theirs has happened (docs/05 §7). `validation` exists since MkDocs 1.5 and `links.anchors` since 1.6; the venv has 1.6.1 (`mkdocs-material` pulls it in). The shorthand `validation: anchors: warn` also works in 1.6.1 (seen in the scratch copy), but the nested form is the one MkDocs documents.

`scripts/build.py`: `locate(message)` returns the list of `(file, line)` for a message instead of one pair. When the message names a doc file and a link, the lines are every line of that file where the link follows `(`, `(<` or `]:` and is followed by the end of the line, a space, `)` or `>`; none found gives line 1. `main` prints one finding per distinct `(file, line, message)`. The finding format `file:line: build: message`, the rule name and exit 1 do not change.

**Out of scope.**

* The book build (`make book`): `book-build-links`.
* The external-link check: it judges addresses, and `check_links.py` skips anchors on purpose (`link-check`).
* README links: MkDocs does not build the READMEs.
* The other validation keys: no case has happened (docs/05 §7).

**Done when.**

* [x] In a scratch copy, each Behaviour case prints the finding stated, with the output recorded on the page, and the first two print nothing at warning level before the change.
* [x] On the tree, `make build` prints nothing and exits 0.
* [x] docs/01: the `mkdocs.yml` row says the site validates anchors, the `scripts/build.py` row says a repeated link gets a finding on each line, and §How errors travel says a missing heading fails the strict build and each broken link is found at every line it stands on. docs/04 §Tests: "the strict build catches a broken internal link" gains "or one to a heading that does not exist".
* [x] `make verify` green. No screen changes: the site renders as before, so no screenshot.

**Decisions in the review.**

* `links.anchors` only, not every validation key: the finding is about anchors (docs/05 §7; recommendation of this session).
* One finding per line the link stands on, not per MkDocs warning: MkDocs warns once per distinct anchor target and once per occurrence of a missing file, so the lines cannot come from the warnings (seen in the scratch copy).
* The end of a link is the character after it, so `#one-place` is never found inside `#one-place-per-fact` (recommendation of this session).
* Same-page anchors fail as well: MkDocs reports them under the same key.
* Pages in flight: none touches `mkdocs.yml` or `scripts/build.py`. Several lines edit docs/01 and docs/04 §Tests in other rows and sentences (`repo-files-any-name`, `hook-hash-lines`, `em-dash-every-text`, `links-url-bounds`, `parity-notes-readmes`, `entry-apostrophes`, and `book-build-links`, `epub-chapter-links` in docs/01): stage by hunk (docs/05 §6). `renumber-chapters` rewrites `NN-<slug>.md` links; it adds no anchor.

## What happened

**The error it catches** (docs/05 §7): a link to a heading that does not exist, on another chapter or on its own page, built green; MkDocs reports it at `INFO`, which `--strict` does not count. And a broken link that stands on several lines was found only at its first one, or at the first line holding a longer link it is the start of.

**Built.**

* `mkdocs.yml`: the `validation:` block of the Contract, at the top level after `docs_dir`.
* `scripts/build.py`: `locate(message)` returns a list of `(file, line)`. The link is matched by a regular expression: after `(`, `(<` or `]:` and any spaces, the link escaped, then the end of the line, a whitespace character, `)` or `>`. No line found gives line 1; no doc file gives `mkdocs.yml:1`. `main` prints each `file:line: build: message` once, in the order found.
* docs/01: the `scripts/build.py` and `mkdocs.yml` rows, and §How errors travel. docs/04 §Tests: the strict build's sentence.

**Diverged from the contract.** Nothing.

**Proof.** Each case ran in its own fresh copy of the tree (`git archive HEAD`, then this delivery's `mkdocs.yml` and `scripts/build.py` copied in), with the venv's Python running the copy's `scripts/build.py`. Chapter 2 holds 112 lines, so lines appended after a blank line land on 114, 116 and so on.

Today, in a copy of HEAD without the block, the two links appended at 114 and 116 of `book/en/02-how-agents-see.md`; `mkdocs build --strict` filtered to the two links, exit 0, and `scripts/build.py` printed nothing, exit 0:

    INFO    -  Doc file 'en/02-how-agents-see.md' contains a link '#nope-here', but there is no such anchor on this page.
    INFO    -  Doc file 'en/02-how-agents-see.md' contains a link '10-the-documents.md#no-such-heading', but the doc 'en/10-the-documents.md' does not contain an anchor '#no-such-heading'.

Today, the same copy with `[a](99-gone.md)` inserted at lines 94 and 96, exit 1, both on 94:

    book/en/02-how-agents-see.md:94: build: Doc file 'en/02-how-agents-see.md' contains a link '99-gone.md', but the target 'en/99-gone.md' is not found among documentation files.
    book/en/02-how-agents-see.md:94: build: Doc file 'en/02-how-agents-see.md' contains a link '99-gone.md', but the target 'en/99-gone.md' is not found among documentation files.

With the change:

1. Other chapter at 114, own page at 116, exit 1:

        book/en/02-how-agents-see.md:116: build: Doc file 'en/02-how-agents-see.md' contains a link '#nope-here', but there is no such anchor on this page.
        book/en/02-how-agents-see.md:114: build: Doc file 'en/02-how-agents-see.md' contains a link '10-the-documents.md#no-such-heading', but the doc 'en/10-the-documents.md' does not contain an anchor '#no-such-heading'.

2. The same link at 114 of `book/pt/02-how-agents-see.md` alone, exit 1; the same again with the English edition holding the valid link at 114 gave the same single line:

        book/pt/02-how-agents-see.md:114: build: Doc file 'pt/02-how-agents-see.md' contains a link '10-the-documents.md#no-such-heading', but the doc 'pt/10-the-documents.md' does not contain an anchor '#no-such-heading'.

3. `[x](10-the-documents.md#one-place-per-fact)` at 114: nothing printed, exit 0.

4. The broken link twice on 114 (`[x](...) and [y](...)`), once on 118 and once on 120, exit 1:

        book/en/02-how-agents-see.md:114: build: Doc file 'en/02-how-agents-see.md' contains a link '10-the-documents.md#no-such-heading', but the doc 'en/10-the-documents.md' does not contain an anchor '#no-such-heading'.
        book/en/02-how-agents-see.md:118: build: Doc file 'en/02-how-agents-see.md' contains a link '10-the-documents.md#no-such-heading', but the doc 'en/10-the-documents.md' does not contain an anchor '#no-such-heading'.
        book/en/02-how-agents-see.md:120: build: Doc file 'en/02-how-agents-see.md' contains a link '10-the-documents.md#no-such-heading', but the doc 'en/10-the-documents.md' does not contain an anchor '#no-such-heading'.

5. `[a](99-gone.md)` inserted at 94 and 96, exit 1:

        book/en/02-how-agents-see.md:94: build: Doc file 'en/02-how-agents-see.md' contains a link '99-gone.md', but the target 'en/99-gone.md' is not found among documentation files.
        book/en/02-how-agents-see.md:96: build: Doc file 'en/02-how-agents-see.md' contains a link '99-gone.md', but the target 'en/99-gone.md' is not found among documentation files.

6. Broken `10-the-documents.md#one-place` at 114, valid `10-the-documents.md#one-place-per-fact` at 116, exit 1, nothing on 116:

        book/en/02-how-agents-see.md:114: build: Doc file 'en/02-how-agents-see.md' contains a link '10-the-documents.md#one-place', but the doc 'en/10-the-documents.md' does not contain an anchor '#one-place'.

7. A warning that names a file and no link: the copy's `mkdocs.yml` also set `absolute_links: warn` under `links`, and `[z](/abs)` stood at 114, exit 1. A warning that names no file: another copy with `no_such_key: 1` added to `mkdocs.yml`, exit 1:

        book/en/02-how-agents-see.md:1: build: Doc file 'en/02-how-agents-see.md' contains an absolute link '/abs', it was left as is.
        mkdocs.yml:1: build: Config value 'no_such_key': Unrecognised configuration name: no_such_key

8. The tree as it is, in a copy and then on the tree itself: `make build` printed only its command line and exited 0. `make verify` green.

**Noted, not fixed.** Nothing.

**Dropped.** Nothing.

**Decisions.**

* Taken alone in this batch: after `]:` the match allows any spaces, none included, where the old code required exactly one; a reference definition with two spaces or a tab is still found.
* Taken alone in this batch: "a space" after the link is read as any whitespace character, so a tab or a title after the link (`(url "title")`) ends it as well.
* Taken alone in this batch: case 7 needs a warning MkDocs gives only with a scratch setting, so `absolute_links: warn` and an unknown key were set in two separate copies; a configuration warning aborts the strict build before any page is read, so one copy could not show both.
* Taken alone in this batch: the `validation:` block sits right after `docs_dir`, with the other settings about where the pages are.
* No screenshot: the site renders as before, as the page says. No ADR and no manual: the change applies the strict build to one more kind of link and changes nothing a person does by hand.
* No queue line is resolved by this one: none waits on `site-build-anchors`.

```commit
fix(site-build-anchors): fail on missing headings, report every line

- mkdocs.yml validates links to headings (anchors: warn)
- build.py finds a broken link at each line it stands on, once per line
- a link that starts a longer valid one is no longer found inside it
- docs/01 and docs/04 say so

work/done/site-build-anchors.md
```
