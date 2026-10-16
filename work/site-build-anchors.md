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

* [ ] In a scratch copy, each Behaviour case prints the finding stated, with the output recorded on the page, and the first two print nothing at warning level before the change.
* [ ] On the tree, `make build` prints nothing and exits 0.
* [ ] docs/01: the `mkdocs.yml` row says the site validates anchors, the `scripts/build.py` row says a repeated link gets a finding on each line, and §How errors travel says a missing heading fails the strict build and each broken link is found at every line it stands on. docs/04 §Tests: "the strict build catches a broken internal link" gains "or one to a heading that does not exist".
* [ ] `make verify` green. No screen changes: the site renders as before, so no screenshot.

**Decisions in the review.**

* `links.anchors` only, not every validation key: the finding is about anchors (docs/05 §7; recommendation of this session).
* One finding per line the link stands on, not per MkDocs warning: MkDocs warns once per distinct anchor target and once per occurrence of a missing file, so the lines cannot come from the warnings (seen in the scratch copy).
* The end of a link is the character after it, so `#one-place` is never found inside `#one-place-per-fact` (recommendation of this session).
* Same-page anchors fail as well: MkDocs reports them under the same key.
* Pages in flight: none touches `mkdocs.yml` or `scripts/build.py`. Several lines edit docs/01 and docs/04 §Tests in other rows and sentences (`repo-files-any-name`, `hook-hash-lines`, `em-dash-every-text`, `links-url-bounds`, `parity-notes-readmes`, `entry-apostrophes`, and `book-build-links`, `epub-chapter-links` in docs/01): stage by hunk (docs/05 §6). `renumber-chapters` rewrites `NN-<slug>.md` links; it adds no anchor.
