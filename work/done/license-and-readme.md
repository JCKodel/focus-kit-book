# license-and-readme

**Objective.** A visitor to the repository or the site learns in one screen what the book is, where to read or download it, how to build it, how to contribute and which license covers which file, in English or Portuguese.

**Behaviour.**

* GitHub shows `README.md` in English; its first line links to `README.pt.md`, whose first line links back.
* Both READMEs have the same sections, in the same order, saying the same thing.
* The README says which license covers what: prose (the book's text and figures, `docs/`, `work/`, the READMEs) is CC BY-SA 4.0; everything else (scripts, `Makefile`, `mkdocs.yml`, `overrides/`, `book/assets/site.css`, the focus-kit files) is AGPL-3.0-only.
* `LICENSE` stays the AGPL-3.0 text; `LICENSE-TEXT` holds the CC BY-SA 4.0 legal code, unchanged.
* Every page of the site, in both editions, shows in its footer the copyright and both licenses, in the edition's language, with links.
* `make verify` is green.

**Contract.**

Files:

```
LICENSE          unchanged (AGPL-3.0 text, already in place)
LICENSE-TEXT     CC BY-SA 4.0 legal code, verbatim from
                 https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt
README.md        English
README.pt.md     Portuguese
mkdocs.yml       copyright, and its Portuguese override in the i18n language pt
```

README sections, in this order (headings of `README.pt.md` in parentheses):

| Section | Content |
|---|---|
| first line | `Português: [README.pt.md](README.pt.md)` · pt: `English: [README.md](README.md)` |
| H1 | `One Page at a Time` · pt `Uma Página de Cada Vez`; the subtitle of docs/00 on the next line; `J.C. Ködel`; one sentence on what the book teaches, from docs/00 Purpose |
| `## Read` (`## Ler`) | the site, `https://jckodel.github.io/focus-kit-book/` (pt: `https://jckodel.github.io/focus-kit-book/pt/`); PDF and EPUB in both editions on the repository's Releases and on `https://books.kodel.com.br` |
| `## Build locally` (`## Gerar localmente`) | needs Python 3 and make; `make serve` opens the site at `http://127.0.0.1:8000/`; `make verify` runs the checks |
| `## How it is written` (`## Como é escrito`) | one paragraph: written with focus-kit (`https://github.com/JCKodel/focus-kit`); `docs/` holds the project documents, `docs/06-Queue.md` the queue, `work/done/` one page per delivery; the repository is the book's example of a project that is not software |
| `## Contributing` (`## Contribuir`) | an error or a suggestion: open an issue; a fix: a pull request that changes both editions, with `make verify` green; contributions are accepted under the license of the file they change |
| `## License` (`## Licença`) | the table below |

License table (pt with the column headers `O quê`, `Licença`, `Arquivo`):

| What | License | File |
|---|---|---|
| The book's text and figures (`book/`), the project documents (`docs/`, `work/`) and these READMEs | CC BY-SA 4.0 | `LICENSE-TEXT` |
| Scripts, build and site configuration (`scripts/`, `Makefile`, `mkdocs.yml`, `overrides/`, `book/assets/site.css`) | AGPL-3.0-only | `LICENSE` |
| focus-kit's installed command files | AGPL-3.0-only, under focus-kit's terms | `LICENSE` |

Site footer (`copyright` in `mkdocs.yml`, HTML allowed by Material):

* en: `© 2026 J.C. Ködel · Text: <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a> · Code: <a href="https://www.gnu.org/licenses/agpl-3.0.html">AGPL-3.0</a>`
* pt: `© 2026 J.C. Ködel · Texto: <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br">CC BY-SA 4.0</a> · Código: <a href="https://www.gnu.org/licenses/agpl-3.0.html">AGPL-3.0</a>`

Documents this delivery changes:

* ADR-0003: an amendment, dated, extending CC BY-SA 4.0 to `docs/`, `work/` and the READMEs (prose by nature, and the book quotes them as artifacts), and naming `book/assets/site.css` as code.
* docs/01: `LICENSE`, `LICENSE-TEXT`, `README.md`, `README.pt.md` in the tree.
* docs/04 §Languages: the README exists in both languages, `README.md` and `README.pt.md`, changed in the same delivery.

**Out of scope.**

* A parity check for the READMEs: they change rarely; it enters on the first drift found (docs/05 §7).
* SPDX headers in each file: the README's table covers it.
* The license page inside the PDF and EPUB: `pdf-epub`.
* The Read links working: the site and Releases come with `pages-and-release`; the links are written now with their final addresses.
* Repointing focus-kit to the book: `launch` (OD-4).

**Done when.**

* [x] `LICENSE-TEXT` identical to the fetched legal code (byte comparison recorded in the page); `LICENSE` unchanged.
* [x] `README.md` and `README.pt.md` with the sections above, same order, links between them.
* [x] Footer checked in the built site, both editions, both links working: screenshot `work/done/license-and-readme-<edition>-footer-1280.png` and `-390.png`.
* [x] ADR-0003 amended; docs/01 and docs/04 updated.
* [x] `make verify` green.
* [x] docs/06: `license-and-readme` marked `[x]`; page moved to `work/done/license-and-readme.md`.
* [x] Changes staged, commit message suggested, nothing committed.

**What happened.**

Diverged from the plan: nothing.

Nothing dropped.

The proof found:

* `LICENSE-TEXT` fetched from `https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt` on 2026-09-24 and compared with `cmp`: identical, 20138 bytes, SHA-256 `28a9529c7d0bb4dc51f4bf5c116a3d16ef247a052f7591466768ddf563fd1cf5`. `git diff LICENSE` empty.
* The mkdocs-static-i18n plugin accepts `copyright` per language, so the Portuguese footer is an override in the `pt` language, as the Contract says.
* In the built site the footer is on every page of both editions (home and chapter 1), with the edition's text; the three links answer 200 (`by-sa/4.0/`, `by-sa/4.0/deed.pt-br`, `agpl-3.0.html`).
* Screenshots of chapter 1 in `work/done/license-and-readme-<edition>-footer-<width>.png`, dark scheme as in `site-skeleton`. The 390 shots use the same iframe method; the first attempt cropped from the wrong offset and showed the page cut on the left, so the iframe was centred in the 500 pixel window and the crop centred too.
* Material prints "Made with Material for MkDocs" under the copyright in English in both editions: the theme hardcodes the text in `partials/copyright.html`. Left as it is: not part of this Contract; hiding it (`extra.generator: false`) or translating it would be a queue line.
* `make verify` green.

Decisions: none beyond the Contract; ADR-0003 carries the amendment it named.
