# manual-link-pointers

**Objective.** A person who builds the book from a clone follows a link in a manual that `make verify` has checked, gets a failure message that names the file holding the install steps, and finds every manual naming the others the same way.

**Behaviour.**

The findings come from `work/done/m23-review.md`: B1 (the manuals' URLs are outside the link check), B7 with L5 (`(see README)` lands on a README with no install command, loops back inside the manual, and sends Portuguese readers to the English README) and B6 (`release-the-book.md` names one manual by its path and the others by bare names, in one list).

* The link check reads the manuals. `python3 scripts/check_links.py` fetches every external URL of each `docs/manuals/*.md`, read as it reads a chapter: code, HTML comments and front matter skipped, `127.0.0.1`, `localhost`, `example.com`, `example.org`, `example.net` (and their subdomains) and URLs under `site_url` not fetched. Today that adds `https://nodejs.org/dist/v26.12.0/` (`build-the-book-from-a-clone.md`:13) and `https://github.com/JCKodel/focus-kit-book/actions` (`publish-the-site.md`:21); `https://jckodel.github.io/focus-kit-book/` (`publish-the-site.md`:5) is under `site_url`, and the `git clone` URL (`build-the-book-from-a-clone.md`:21) is in code, so neither is fetched.
* A broken manual URL fails. A scratch line `<https://example.invalid.focus-kit-book.test/x>` or a 404 URL on a GitHub path added to a manual prints `docs/manuals/<file>.md:<line>: links: <url>: <reason>` and the check exits 1; the line is removed after the proof.
* A file outside the four groups is still not read: a URL in `docs/05-Process.md` or `work/` is not fetched.
* Offline, the manuals change nothing: every URL failing at DNS or connection still prints `links: skipped, no network` locally and fails in Actions.
* No Node on the `PATH`: `make verify` fails at the examples check with `Makefile:1: examples: node not found; install Node.js 26.12.0 or later (see docs/manuals/build-the-book-from-a-clone.md)`, exit non-zero.
* A Node older than 26.12.0: `Makefile:1: examples: node <version> found; Node.js 26.12.0 or later is required (see docs/manuals/build-the-book-from-a-clone.md)`.
* No pandoc, weasyprint or pypdf: `make book` prints `Makefile:1: book: <tool> not found; install it (see docs/manuals/build-the-book-from-a-clone.md)` and writes nothing.
* The build manual's "What breaks if a step is skipped" quotes those three messages exactly as the scripts print them, and docs/01's build paragraph quotes the book one.
* The manuals name a sibling manual one way: by its file name alone, in backticks, as `publish-the-site.md`:14 and `release-the-book.md`:9 and :19 already do. After the delivery `grep -n "docs/manuals/" docs/manuals/*.md` prints nothing.
* `make verify` green with the new URLs fetched online.

**Contract.**

Files and lines, as they are at this page's writing:

```
scripts/check_links.py                       docstring :4; files() :40-46
scripts/check_examples.py                    node_finding() :221, :225
scripts/build_book.py                        main() :468, :473
docs/manuals/build-the-book-from-a-clone.md  :27, :42-44, :50
docs/manuals/release-the-book.md             :18
docs/01-Architecture.md                      :33 (check_links row), :92 (build_book message)
docs/04-Conventions.md                       :170 (the links sentence)
```

* `check_links.files()` yields, besides what it yields today, every repository file (`repo_files()`) whose path starts with `docs/manuals/` and ends with `.md`, masked as the chapters are (`mask(..., keep_targets=True)`). Fetch, skip rules, offline rule, output `file:line: links: <url>: <reason>` and exit codes do not change. The docstring says "Reads both editions of the book, both READMEs, the manuals in docs/manuals/ and mkdocs.yml".
* The pointer in all four messages: `(see README)` becomes `(see docs/manuals/build-the-book-from-a-clone.md)`, the path from the repository root, where `make` runs; the rest of each message is unchanged, so the format stays `Makefile:1: <rule>: <message>`.
* Build manual :42-44 quote the new messages; :27 becomes "the hooks and the scan in `set-up-the-disclosure-list.md`, the release in `release-the-book.md`"; :50 becomes "is in `set-up-the-disclosure-list.md`".
* `release-the-book.md`:18 ends "(`build-the-book-from-a-clone.md`)".
* docs/01 :33: "every external URL in both editions, both READMEs, the manuals and mkdocs.yml still answers (rule "links")"; :92: the book message with the new pointer.
* docs/04 :170: "`links` catches an external URL in either edition, either README, a manual of `docs/manuals/` or `mkdocs.yml` that answers ...", the rest unchanged.
* No new term in docs/03; no chapter quotes these messages or names these files (grep at this page's writing), so no edition changes.

Neighbouring line on the same file: `manual-pypdf-install` changes `docs/manuals/build-the-book-from-a-clone.md`:15 (how pypdf is installed) and may touch :44 and the pypdf message in `build_book.py`:473; it is applied after this line, in queue order, on the file as this delivery leaves it.

**Out of scope.**

* The Portuguese reader: the manual is English only, which README.pt.md:26 already says ("em inglês"); a Portuguese manual is not asked.
* How pypdf is installed (B3): `manual-pypdf-install`.
* Making the manuals' file names Markdown links: they are code spans today, read in a clone or on GitHub, and no check reads `docs/` links; a link no check reads could go stale.
* `docs/05-Process.md` §5's paths (`docs/manuals/<file>`): a slot, read from the repository root, not a manual.
* A pointer to a section of the manual inside the message: the file names the install steps under "What must be in place", its second heading.
* Record pages in `work/done/` that quote `(see README)` (`readme-run-manual`, `m23-review`): history.

**Done when.**

* [ ] `files()` called from a scratch script lists the four `docs/manuals/*.md` beside the editions, the READMEs and `mkdocs.yml`; the URLs it extracts from the manuals are the two of Behaviour, recorded on the page.
* [ ] A scratch broken URL in a manual prints `docs/manuals/<file>.md:<line>: links: ...` and exit 1, recorded; the line removed.
* [ ] With `node` off the `PATH` the examples message, and with a missing tool the book message, print the new pointer, recorded.
* [ ] The build manual's :42-44 and docs/01 :92 match the scripts' strings byte for byte (grep recorded).
* [ ] `grep -n "docs/manuals/" docs/manuals/*.md` prints nothing.
* [ ] docs/01 and docs/04 updated.
* [ ] `make verify` green, online, with the manuals' URLs fetched.
* [ ] The Delivery review as docs/05 §5 says.

**Decisions taken alone.**

* Every `docs/manuals/*.md` is read, not only the build manual: the line says "the manuals' URLs", and `publish-the-site.md` holds a URL a reader follows.
* The pointer is the manual's path from the root, not "README" with a fixed README: docs/05 §5's Manuals slot says a place naming a command with steps points to its manual, and readme-run-manual moved the steps there.
* The quoted messages inside the build manual keep the pointer to the manual itself: they quote what the scripts print; the reader in the manual is already where the steps are.
* One way is the bare file name, not the path: three of the four cross-references between manuals already use it, they sit in one folder, and docs/05 §5's Manuals list names them so. The other choice would change `publish-the-site.md`, which the line does not name.
* docs/01 :33, :92 and docs/04 :170 go stale with this change and belong to no other line, so they enter (docs/05 §2, the owner document updated in the same delivery).
* The scratch broken URL's host ends in `.test`, a reserved name that never resolves and is not one of `SKIPPED_HOSTS`, so the check fetches it and fails at DNS; it is reported, not taken for "no network", because the other URLs answer. A 404 on a GitHub path is the second proof, an HTTP failure.
* No test file: the checks are the tests (docs/04 §Tests); the proof lives on the page, as in `links-url-bounds`. No new check, so docs/05 §7's rule does not apply.
