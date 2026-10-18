# copyright-version

**Objective.** A reader of a PDF or EPUB, in either edition, reads on the
page with the copyright line which version of the book they hold and the
date it was published, and where to look for a newer one; the author
releases only a book that was built, with that page, on their machine.

**Behaviour.**

* The author runs `make release` after `v1.2.3`: before asking to push, it
  writes `1.2.4 2026-10-18` (today) to `VERSION`, builds the book with
  `make book` in release mode, and prints the four files' paths with the
  next tag and the commits since the last one. The rights page of each
  file reads, in English: "This is version 1.2.4 of the book, published on
  2026-10-18. Check https://github.com/JCKodel/focus-kit-book/releases for
  a newer version."; in Portuguese: "Esta é a versão 1.2.4 do livro,
  publicada em 2026-10-18. Veja se há uma versão mais nova em
  https://github.com/JCKodel/focus-kit-book/releases.". In the PDF the
  sentence sits under the copyright line; in the EPUB it is part of the
  rights text.
* The author answers `y`: it commits `VERSION` alone with the message
  `chore(release): v1.2.4`, pushes `main`, tags that commit `v1.2.4`
  (annotated) and pushes the tag. The job `release` builds from the tag
  and its four files carry the same sentence, with no "unpublished".
* The author answers anything else: `VERSION` is restored as it was,
  nothing is committed or pushed, the refusal line says so.
* `make book` fails during `make release` (a broken link, say): `VERSION`
  is restored, nothing is committed or pushed, the build's own findings
  print, then `Makefile:1: release: make book is not green; nothing was
  pushed`, exit 1.
* `make release` where pandoc, weasyprint or pypdf is missing: the build's
  `not found` line, then the same refusal; nothing changed.
* `VERSION` says `1.2.2` while the newest tag is `v1.2.3`:
  `make release` refuses before building,
  `VERSION:1: release: VERSION says 1.2.2 but the newest tag is v1.2.3`.
* The author runs `make book` for a chapter review on any commit after
  `v1.2.3`, or with uncommitted edits: the rights page reads "This is
  version 1.2.3 of the book, published on 2026-10-16, with changes not
  yet published, built on 2026-10-18. Check …"; pt: "Esta é a versão
  1.2.3 do livro, publicada em 2026-10-16, com alterações ainda não
  publicadas, gerada em 2026-10-18. Veja se há …".
* `make book` on the tagged commit `v1.2.3` with a clean tree, or with no
  git at all (a downloaded archive): the first reads as published; the
  second as "with changes not yet published", since nothing proves it is
  the tag.
* `VERSION` missing, or not `X.Y.Z YYYY-MM-DD` on one line: `make book`
  prints `VERSION:1: book: VERSION must be one line "X.Y.Z YYYY-MM-DD"`
  and exits 1.
* The site footer keeps the copyright line as today, with no version.

**Contract.**

* `VERSION`, new, at the repository root, committed: one line
  `X.Y.Z YYYY-MM-DD`, the newest release and its date. This delivery
  creates it as `1.2.3 2026-10-16`, the tag `v1.2.3` and its date, so the
  first build after it says 1.2.3. Only `make release` changes it.
* Dates are `YYYY-MM-DD` in both editions, the one date form docs/04
  already uses (its sources' `accessed YYYY-MM-DD`).
* `mkdocs.yml`, under `extra` of each edition, beside `draft_banner`:
  `book_version` and `book_version_unpublished`, the two sentences above
  with the placeholders `{version}`, `{date}` and, in the second,
  `{built}`; the releases URL is written in them, the one the READMEs
  already give. `scripts/build_book.py` reads them as it reads
  `draft_banner`, and a missing one is `mkdocs.yml:1: book: no <key> for
  edition <edition>`.
* `scripts/build_book.py`: the rights page is the copyright line, then the
  version sentence in its own paragraph; the EPUB's `rights` is both,
  joined by a space. Published wording when called with `--release`, or
  when a tag `v<version>` points at `HEAD` and `git status --porcelain` is
  empty; otherwise the unpublished one, `{built}` being today's date.
* `scripts/release.py`, after `make verify` and the next tag: the check
  that `VERSION` names the newest tag, then write `VERSION`, run
  `python3 scripts/build_book.py --release`, print the paths, ask; restore
  `VERSION` with `git checkout -- VERSION` on any refusal after writing it.
  On yes: `git commit -m "chore(release): vX.Y.Z" -- VERSION`, push `main`,
  annotated tag on that commit, push the tag.
* `.github/workflows/verify.yml`, job `release`: checkout with
  `fetch-depth: 0`, so the tag is there for the published wording.
* Documents, same delivery: docs/01's layout gains `VERSION`, its
  `make book` row says where the version sentence comes from, its
  `make release` row says it writes `VERSION`, builds the book, and
  commits; `docs/manuals/release-the-book.md` gains pandoc, weasyprint and
  pypdf in what must be in place, the build and the commit in its steps,
  the rights page in how to tell it worked, and in how to undo it that the
  release commit stays on `main` unless reverted; docs/05 §6 says the
  release commit is the one commit a script makes, on the author's `y`,
  with no page and no body.
* No docs/03 term: version, release and tag are there or ordinary words.

**States.** Not applicable: no screen.

**Visual reference.** Not applicable: the rights page keeps its place and
style; the sentence is a second paragraph in `.rights-page`.

**Out of scope.**

* The site footer: the site is always the newest text, there is nothing to
  check for.
* The version on the cover or title page: the queue line asks for the page
  with the copyright line.
* Changing how the next tag is chosen (`BUMP`): unchanged.
* A changelog of the book: no delivery asked for it.

**Done when.**

* [x] `VERSION` exists with `1.2.3 2026-10-16`.
* [x] `make book` on this tree prints both PDFs' and EPUBs' paths, and the
  rights page of both PDFs, and the rights of both EPUBs, show the
  unpublished sentence in their language.
* [x] `python3 scripts/build_book.py --release` shows the published sentence.
* [x] A `VERSION` broken by hand makes `make book` fail with the line above;
  restored afterwards.
* [x] `make release` refusals checked without pushing: a `VERSION` that does
  not match the newest tag; answering `n` leaves `VERSION` and the tree as
  they were (run on a throwaway clone, never pushing).
* [x] No em dash in the new strings; `make verify` green.
* [x] docs/01, docs/05 §6 and the release manual updated.
* [x] The delivery ends with both PDFs' paths for the author to look at the
  rights page.

## What happened

**Built.** `VERSION` (`1.2.3 2026-10-16`, the tag `v1.2.3` and its date);
`book_version` and `book_version_unpublished` under `extra` of each
edition in `mkdocs.yml`; `scripts/build_book.py` reads `VERSION`
(`book_version`), decides published or not (`published`: the tag
`v<version>` in `git tag --points-at HEAD` and an empty
`git status --porcelain`, false with no git) and writes the sentence as a
second paragraph of `.rights-page` and after the copyright in the EPUB's
`rights`; `scripts/release.py` checks `VERSION` against the newest tag
after `make verify`, writes it, runs `build_book.py --release`, asks,
commits `VERSION` alone, pushes; `fetch-depth: 0` in the job `release`.
The first reading of `VERSION` is the book build's; `release.py` imports
`book_version` from it, the second, rather than parsing it again.

**Decisions.**

* A malformed `VERSION` at `make release` refuses as
  `VERSION:1: release: VERSION must be one line "X.Y.Z YYYY-MM-DD"`, the
  book's message under the release's rule; the page named only the
  mismatch.
* Every refusal after `VERSION` is written restores it, Ctrl-C and end of
  input at the prompt included (`except BaseException`).
* From the review: a push of `main` that fails after `y` also undoes the
  release commit (`git reset HEAD~1`, then `git checkout -- VERSION`), so
  `make release` can simply run again; a push of the tag that fails leaves
  `main` pushed and the tag local, and the manual says to push the tag.
  The page did not say what a failed push does.
* From the review: `build_book.py` with any argument but `--release`
  refuses with `Makefile:1: book: usage: build_book.py [--release]`, so a
  typo cannot build the unpublished wording silently.
* No new check or test file: docs/04's tests are the checks, and no check
  names an error this delivery would have caught; the proof below is by
  hand.
* Proof of a screen: the site is untouched (the footer renders no new
  key; `overrides/main.html` reads only `draft_banner`), so the screen is
  the PDF's rights page, saved as
  `work/done/copyright-version-rights-en.png` and `-pt.png`.

**Proof.**

* `make book` on this tree: the four paths; the PDFs' third page and the
  EPUBs' `dc:rights` carry the unpublished sentence, "version 1.2.3 ...
  published on 2026-10-16, with changes not yet published, built on
  2026-10-18", and its Portuguese, under the copyright line; the
  Portuguese still fits the page.
* `build_book.py --release`: the published sentence in all four files.
* `VERSION` as `1.2.3`, with a second line, as `v1.2.3 2026-10-16`, empty,
  and missing: each `VERSION:1: book: VERSION must be one line
  "X.Y.Z YYYY-MM-DD"` and exit 1; restored. A missing
  `book_version_unpublished` in pt: `mkdocs.yml:1: book: no
  book_version_unpublished for edition pt`; restored.
* A throwaway clone, the delivery committed there as a disposable fixture,
  its push URL set to a path that does not exist, `make hooks` run:
  `VERSION` at `1.2.2` refused with `VERSION:1: release: VERSION says
  1.2.2 but the newest tag is v1.2.3` after verify; `VERSION` at `1.2.3`
  answered `n` built the book with "version 1.2.4 ... published on
  2026-10-18", then refused, leaving `VERSION`, the tree, `HEAD` and the
  tags as they were; answered `y`, the push of `main` failed and the
  commit was undone, `VERSION` restored, no tag. The repository's `main`
  and tags never changed.
* In the clone, `v1.2.3` moved locally onto `HEAD`: published wording with
  a clean tree, unpublished after an edit; a `git archive` of it, with no
  git: unpublished.
* Not run: the refusal for a missing pandoc, weasyprint or pypdf during
  `make release`; it goes through the same restore as `n`.
* `make verify` green.

**Review.** A read-only Opus agent read this delivery's diffs and new
files against the page and docs/04: every Behaviour and Contract item
present, strings byte for byte. Fixed: the failed push of `main` (above),
the docs that said a refusal after `y` commits nothing, two "tagging by
hand" bullets in the manual merged, `release.py` no longer splits the
book's message, the `--release` typo. Kept: the PDF hyphenates "pub-lished"
and prints the URL as text, as the copyright line does.

**Divergences.** None from the page beyond the decisions above.

```commit
feat(copyright-version): the rights page says the book's version

- VERSION at the root, 1.2.3 2026-10-16; only make release changes it
- rights page and EPUB rights: version, date, where to find a newer one
- unpublished wording off the tag or with edits, --release for release
- make release checks VERSION, writes it, builds the book, commits it
- docs/01, docs/05 §6 and the release manual updated

work/done/copyright-version.md
```
