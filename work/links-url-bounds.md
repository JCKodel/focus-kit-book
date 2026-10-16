# links-url-bounds

**Objective.** The author runs `make verify` and the link check judges the address a reader's link points to, not the address plus the Markdown around it, so a URL written as an autolink, as its own link text, in bold or italic, or with parentheses in its path no longer fails with a false 404.

**Behaviour.**

The proof calls `urls_in(line)` on made-up lines in the scratchpad, no network; the fetching is unchanged.

* Finding B6 holds, run before this page. `urls_in` returns today, for a line with the URL `https://a.org/x`:

  | Line | Today's URL | Right URL |
  |---|---|---|
  | `<https://a.org/x(y)>` | `https://a.org/x(y` | `https://a.org/x(y)` |
  | `[https://a.org/x](https://a.org/x)` | `https://a.org/x](` and the target | one, `https://a.org/x` |
  | `**https://a.org/x**` | `https://a.org/x**` | `https://a.org/x` |
  | `*https://a.org/x*`, `_https://a.org/x_`, `~~https://a.org/x~~` | with the marker | `https://a.org/x` |
  | `[https://a.org/x]` | `https://a.org/x]` | `https://a.org/x` |
  | `see https://en.wikipedia.org/wiki/Foo_(bar).` | `.../Foo_(bar` | `.../Foo_(bar)` |
  | `“https://a.org/x”` | with the `”` | `https://a.org/x` |

  Each wrong one is fetched as written and answers 404 or fails to parse: a false finding.
* Unchanged, the cases that already work: `https://a.org/x, and https://b.org/y;` gives both without the `,` and `;`; `(see https://a.org/x).` gives `https://a.org/x`; `[t](https://a.org/x "title")` gives `https://a.org/x`; `[a][1]` with `[1]: https://a.org/x` gives the definition's URL; a `#fragment` and a query string stay in the URL; `https://` alone is no URL.
* A bold URL followed by punctuation (`**https://a.org/x**.`) gives `https://a.org/x`.
* A `)` ends the URL only when it has no `(` to close: `(see https://a.org/x).` strips it, `Foo_(bar)` keeps it, `https://a.org/x(y))` gives `https://a.org/x(y)`.
* The same URL twice on one line (link text and target) is reported once, at its first column; the same URL on two lines is still reported at each line.
* The URLs of today's tree do not change. Checked read-only before this page: the 91 distinct URLs `urls_in` extracts from both editions, both READMEs and `mkdocs.yml` hold no `(`, `)`, `[` or `]`, and the three with an underscore keep it inside the path (`history_of_toyota`, `2020id_`, `26-036_e7d0...`). After the change the set is the same 91, at the same lines. So no URL of the book is fixed here.
* Offline and the fetch results behave as today.

**Contract.**

Files:

```
scripts/check_links.py    urls_in(line), main()
docs/04-Conventions.md    §Tests: links names how an address is read
```

`urls_in(line) -> list[(column, url)]`, signature and sort unchanged:

* A link target `](…)` is the first word inside its balanced parentheses, as today (`markdown.target_end`), blanked from the line before the rest is read.
* An autolink: `<` followed by `http://` or `https://` runs to the next `>`, parentheses kept.
* Any other URL starts at `http://` or `https://` and ends at whitespace, `<`, `>`, `"`, `'`, a backtick, `]`, `“`, `”`, `‘`, `’` or the end of the line.
* Then, until nothing changes: a trailing `.`, `,`, `;`, `:`, `!`, `?`, `*`, `_` or `~` is cut, and a trailing `)` is cut while the URL holds more `)` than `(`.
* A result no longer than `https://` is dropped, as today.

`main()`: a `(file, line, url)` found twice by `urls_in` on one line is kept once, at the lowest column. Fetch, skip rules, offline rule, output format `file:line: links: <url>: <reason>` and exit code do not change. No new term in docs/03.

docs/04 §Tests, the `links` sentence, gains: an address is read as a reader follows it, whether bare, in `<…>`, as link text, in bold or italic, or with balanced parentheses. docs/01's `check_links.py` row is unchanged.

**Out of scope.**

* A `]` or `'` inside a URL, and a target written `](<url with spaces>)`: no URL of the book has one, and CommonMark treats them apart.
* A URL ending in `_` or `~` that is meant: none exists, and a closing emphasis marker is the likelier reading.
* What a server answers, redirects, the 401, 403 and 429 rule, timeouts: unchanged.
* The list of files read (`repo_files.py`): `repo-files-any-name`.

**Done when.**

* [ ] A scratch call of `urls_in` on every line of the table and of the unchanged list prints the right URL column, and the table's lines print the wrong ones before the change: both outputs recorded on the page.
* [ ] The set of URLs and lines `urls_in` extracts from the tree before and after is identical (91 distinct URLs), recorded on the page.
* [ ] A scratch line with the same URL as link text and as target is printed once by `python3 scripts/check_links.py` when that URL answers 404.
* [ ] docs/04 §Tests updated.
* [ ] `make verify` is green.

**Decisions in the review.**

* Bare URL parsing keeps the current regex's stops and adds `]` and curly quotes, instead of a Markdown parser: the check reads lines masked by `markdown.mask`, and a parser would be a second reading of the same text (docs/01, `markdown.py`; recommendation of this session).
* A trailing `)` is cut only when unbalanced: the Wikipedia form `Foo_(bar)` and `(see https://...)` are both right, as the finding asks for the position of `)`.
* Emphasis markers `*`, `_`, `~` are cut at the end only, so a URL with `_` inside stays whole.
* The duplicate on one line is dropped in `main()`, not in `urls_in`: the function stays a plain reader of a line, and the report is where two columns of one address become noise.
* No test file: docs/04 §Tests; the proof lives on the page after `/apply`, as in `repo-files-any-name`.
* Pages in flight: none touches `scripts/check_links.py`. `repo-files-any-name` changes `repo_files.py`, which it imports, without conflict. The pages in `work/` that edit chapters (`quick-guide`, `prologue-and-why` and others) may add URLs to the book, which this check will read with the new rules; none edits the script.
