# ch12-defined-mark

**Objective.** After chapter 12 the reader knows that `/propose` marks a line `[>]` when the page is completely defined, as docs/05 §3 says, not when the file is written.

**Behaviour.**

* Reading "What `/propose` does", the reader says `[>]` means the page is completely defined, not merely written, finds the condition in chapter 14, and says a written page with a question still open is not `[>]`.
* Given `work/lend-book.md` (pt `work/emprestar-livro.md`) written while a Contract question is still being talked through, the reader says the line stays `[~]`; given one whose question was asked and not answered, the existing sentence on `[?]` and `· resume: propose` applies.
* Reading the Key points, the reader finds the same condition: `[>]` when the page is completely defined, not when it is written.
* The chapter keeps its opening, its problem, its page example and its team gain unchanged.

**Contract.** Files: `book/en/12-propose.md` and `book/pt/12-propose.md`. Two sentences per edition, located by content, since other sessions may have moved line numbers:

* "What `/propose` does": en "...and when the page is written, `work/<slug>.md`, the mark becomes `[>]`." / pt "...e quando a página está escrita, `work/<slug>.md`, a marca vira `[>]`." The `[>]` clause says the page is completely defined (docs/05 §3) and points to chapter 14 for the condition, which `ch11-14-defined-mark` placed under chapter 14's mark table; it does not restate the whole condition.
* Key points: en "...marks the line `[~]` while it talks and `[>]` when the page is written, or `[?]` when the scope waits..." / pt "...marca a linha `[~]` enquanto conversa e `[>]` quando a página está escrita, ou `[?]` quando o escopo espera...". "when the page is written" becomes "when the page is completely defined" (pt "quando a página está completamente definida").

The next sentence ("It ends by showing that queue line, `[>] lend-book ...`") and the `[?]` sentence with `· resume: propose` stay as they are. Terms of docs/03: page, mark, draft page; no new term. Sources: docs/05 §3's last paragraph and §4's mark table, the installed propose skill ("Mark `[>]` only when the definition is complete"). No number, no private case.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** The sentence on a `[?]` line ("goes on only when you say it is resolved"): it fits `resume: propose`, the only phase that returns to `/propose`, so it stays. Chapters 11, 13 and 14: already fixed by `ch11-14-defined-mark` and `ch13-refuse-incomplete`.

**Decisions from the documents.** The full condition lives once, in chapter 14 (ch11-14-defined-mark); chapter 12 names it and points there, so the condition is not kept in two places (docs/04, living documents).

**Done when.**

* [ ] Both editions written, same hunks; each Behaviour line checked against both.
* [ ] The chapter opens with its value; no filler and nothing useful cut; every number and quoted artifact keeps its source; terms follow docs/03; no em dash.
* [ ] No Case A or Case B passage changed or added, so the author's OD-3 approval is inapplicable.
* [ ] `make verify` green after the last edit; `make book` builds both editions and the page gives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review.
* [ ] Delivery review by a read-only Opus agent per docs/05 §5, its candidates answered on this page; page archived and commit message suggested.
