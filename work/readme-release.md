# readme-release

**Objective.** A reader of either README learns what `make release` checks, that it writes `VERSION`, builds the book and asks, and that on `y` it commits `VERSION` and pushes `main` and the tag, as the release manual says.

**Behaviour.**

* README.md's `make release` bullet names the checks the manual lists (`docs/manuals/release-the-book.md`, "What must be in place"): on `main` with no uncommitted change, not behind `origin/main`, commits since the newest `v*` tag, `make verify` green, `VERSION` naming the newest tag.
* It says the command writes the next version and today's date to `VERSION`, builds the book, which needs pandoc, weasyprint and pypdf as for `make book`, and asks.
* It says that on `y` it commits `VERSION` alone, pushes `main` and the next tag, and Actions attaches the PDF and EPUB of both editions to a new Release; `BUMP=minor` and `BUMP=major` stay.
* It points to `docs/manuals/release-the-book.md` for the steps.
* README.pt.md's bullet says the same in Portuguese, in the same place; both READMEs keep the same headings (the parity check).
* The bullet promises nothing the manual contradicts: it does not say a refusal always restores `VERSION` (the manual's network case leaves `main` pushed).

**Contract.** In `README.md`, the bullet that begins "`make release`, for the author only" becomes:

```
* `make release`, for the author only, publishes the book: on a clean `main`, not behind `origin/main`, with commits since the newest `v*` tag, `make verify` green and `VERSION` naming that tag, it writes the next version and today's date to `VERSION`, builds the book (pandoc, weasyprint and pypdf, as for `make book`) and asks; on `y` it commits `VERSION` alone and pushes `main` and the next tag (`BUMP=minor` or `BUMP=major` for a bigger step), and Actions attaches the PDF and EPUB of both editions to a new Release. The steps are in `docs/manuals/release-the-book.md`.
```

In `README.pt.md`, the bullet that begins "`make release`, só para o autor" becomes:

```
* `make release`, só para o autor, publica o livro: com a `main` limpa, sem estar atrás da `origin/main`, com commits desde a tag `v*` mais nova, `make verify` verde e `VERSION` nomeando essa tag, grava a próxima versão e a data de hoje em `VERSION`, gera o livro (pandoc, weasyprint e pypdf, como no `make book`) e pergunta; com `y`, faz o commit só do `VERSION` e envia a `main` e a próxima tag (`BUMP=minor` ou `BUMP=major` para um passo maior), e o Actions anexa o PDF e o EPUB das duas edições a uma nova Release. Os passos estão em `docs/manuals/release-the-book.md`.
```

No other line of either README changes.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: the READMEs render as GitHub Markdown; one bullet changes in each.

**Out of scope.**

* `scripts/release.py`'s docstring opening (D1 names it): the queue line scopes this delivery to the READMEs, and the docstring's body already says it writes `VERSION`, builds the book and commits.
* The refusal scope in release.py, docs/01 and the manual (D3 of m19-review): not confirmed by the author.
* The manual and docs/01: already right; the README follows them.

**Decisions taken alone.**

* The bullet points to the manual by path in code, not as a link, so the link check has nothing new to follow.
* The checks are listed in the manual's order; the refusal and undo cases stay in the manual, so the README makes no claim D3 would make false.
* "commit" stays as the Portuguese edition uses it ("faz o commit"), as chapters 7, 9 and 10 do ("fazer o commit").
* Written with no person available, on the author's batch authorisation; the `[~]` and `[>]` marks in docs/06 are the batch driver's.

**Done when.**

* [ ] Both READMEs carry the Contract's bullets in the same delivery, and every Behaviour line holds.
* [ ] `make verify` green after the last edit (parity and links included).
* [ ] The page is in `work/done/` and the line is `[x]`.
