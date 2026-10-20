# readme-run-manual

**Objective.** A visitor reading "Build locally" in either README sees at a glance what the book needs and what each `make` command does, and opens `docs/manuals/build-the-book-from-a-clone.md` for the install commands, the checks that it worked and what breaks, which only the manual holds.

**Behaviour.** Manual checks (docs/04 §Tests: no check reads the READMEs' bullets, as `make-help` and `readme-make-list` decided).

* README.md, "Build locally": one sentence names what is needed, Python 3 and make, Node.js 26.12.0 or later for `make verify`, pandoc, weasyprint and pypdf for `make book`; five one-line bullets name `make`, `make serve`, `make verify`, `make book` and the author's three commands; a last sentence links the manual.
* README.pt.md, "Gerar localmente": the same, in Portuguese, saying the manual is in English (docs/05 §5: documentation language English).
* A visitor who follows the link on GitHub lands on the manual, which has the install commands the README no longer holds: the nodejs.org address and `brew install node`, the `brew` and `apt` lines for pandoc, weasyprint and pypdf, and `python3-venv` on Debian and Ubuntu.
* A person whose `make verify` prints `install Node.js 26.12.0 or later (see README)`, or whose `make book` prints `book: <tool> not found; install it (see README)`, finds in the README the tool named and one link to how to install it.
* `make release` and `make hooks` keep no paragraph in the README: their steps are in `docs/manuals/release-the-book.md` and `docs/manuals/set-up-the-disclosure-list.md`, which the build manual names.
* `docs/manuals/release-the-book.md`, "What must be in place": the pandoc, weasyprint and pypdf line points to the build manual instead of the README's section, which no longer holds their install commands.
* Every bullet left is true beside `make`'s eight lines and the manual: none counts the commands, none repeats an install command or a version but the requirement sentence's Node.js 26.12.0.
* The headings of both READMEs stay as they are (parity counts headings); the other sections do not change.
* Fails if: one edition changes without the other (ADR-0004); the README no longer names Node.js or pandoc, weasyprint and pypdf, so a `(see README)` message lands on nothing it names; an install command stays in the README beside the manual's; the link's target does not exist; an em dash.

**Contract.** Text only.

README.md, lines 16 to 30 (from `## Build locally` to the Debian bullet), replaced by:

```
## Build locally

You need Python 3 and make; `make verify` adds Node.js 26.12.0 or later, and `make book` pandoc, weasyprint and pypdf.

* `make` lists its commands, one line each.
* `make serve` opens the site at <http://127.0.0.1:8000/>.
* `make verify` runs the checks; without the disclosure list, which only the author has, the scan is skipped.
* `make book` writes the PDF and the EPUB of both editions to `output/`.
* `make hooks`, `make scan` and `make release` are the author's.

How to install each tool, how to tell each step worked and what breaks when one is skipped: [docs/manuals/build-the-book-from-a-clone.md](docs/manuals/build-the-book-from-a-clone.md).
```

README.pt.md, lines 16 to 30 (from `## Gerar localmente` to the Debian bullet), replaced by:

```
## Gerar localmente

Você precisa de Python 3 e make; o `make verify` pede também Node.js 26.12.0 ou mais novo, e o `make book`, pandoc, weasyprint e pypdf.

* `make` lista os seus comandos, uma linha cada.
* `make serve` abre o site em <http://127.0.0.1:8000/>.
* `make verify` roda as verificações; sem a lista de exposição, que só o autor tem, a varredura é pulada.
* `make book` grava o PDF e o EPUB das duas edições em `output/`.
* `make hooks`, `make scan` e `make release` são do autor.

Como instalar cada ferramenta, como saber que cada passo deu certo e o que quebra quando um é pulado, em inglês: [docs/manuals/build-the-book-from-a-clone.md](docs/manuals/build-the-book-from-a-clone.md).
```

The blank line before `## How it is written` / `## Como é escrito` stays.

`docs/manuals/release-the-book.md`, line 18, from:

```
* pandoc, weasyprint and pypdf installed, since `make release` builds the book before it asks (README, "Build locally").
```

to:

```
* pandoc, weasyprint and pypdf installed, since `make release` builds the book before it asks (`docs/manuals/build-the-book-from-a-clone.md`).
```

No docs/03 term is needed. docs/01's README line ("how to build") stays true.

**States.** No screen.

**Visual reference.** No screen.

**Out of scope.**

* The `(see README)` in the messages of `scripts/check_examples.py` and `scripts/build_book.py`: they are quoted word for word by the build manual, docs/01 and `work/done/kit-2026-10-19-2.md`, and the README still names the tool and links the manual.
* The build manual itself: kit-2026-10-19-2 wrote it and it already holds every step the README drops.
* "How it is written", "Contributing" and the other sections: not what the line names.
* A new check of the READMEs' links: `links` fetches external URLs only, and one relative link is read by hand.

**Done when.**

* [x] README.md and README.pt.md, "Build locally" and "Gerar localmente", read exactly as the Contract says, one line per sentence and per bullet; no other line of either changes.
* [x] `docs/manuals/release-the-book.md` line 18 reads as the Contract says.
* [x] Read by hand beside `make`'s output and the manual: every bullet is true in both editions, and no install command is in both the README and the manual.
* [x] The link's target, `docs/manuals/build-the-book-from-a-clone.md`, exists relative to the repository root, where GitHub resolves a README's relative link, in both editions.
* [x] `make verify` green; page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.


**Decisions taken from the documents.**

* Steps out of the README, a pointer in: docs/05 §5, Manuals, "a slot that names such a command points to its manual instead of holding the steps", and a manual stands alone (`work/done/kit-2026-10-19-2.md`, Decisions from the documents).
* No check and no test: docs/04 §Tests, as `make-help` and `readme-make-list` decided for the same section.
* Both editions in the same delivery: ADR-0004; the headings stay, which `parity` compares (docs/04).
* The manual is linked in English from the Portuguese README: docs/05 §5, documentation language English.
* The release manual's cite of the README follows in this delivery: a delivery that changes behaviour updates the document that owns it (AGENTS.md).

**Decisions taken alone** (the author asked for recommended answers; correct them in the review):

* Shrink rather than keep the steps and add a pointer: keeping both says each install command twice, in the README and in the manual, and the copies already drift (the README has no `python3-venv`, the manual does).
* Shrink, not to a pointer alone: the requirement sentence stays because the scripts' `(see README)` messages send a person there, and it names the tools so they land on something; the five bullets stay because a visitor sees what each command does without leaving GitHub.
* Node.js 26.12.0 stays in the requirement sentence, the one version the README keeps: the scripts' messages print it beside `(see README)`, and the README had it before.
* The `make release` and `make hooks` paragraphs become one bullet naming the author's three commands: their steps are in their manuals, which the build manual names; `make scan`, unlisted until now, joins them because the build manual groups the three.
* The `make verify` bullet drops the sentence on chapter 3's examples: it is in docs/05 §5 Verify and in the manual's failure lines; the scan clause stays, since a contributor needs `make verify` green (Contributing) and should not expect the scan.
* The `make book` bullet drops "each opening on its cover": a detail of the output, not of building it.
* The pointer is a relative Markdown link whose text is the path, so a GitHub visitor clicks it and the path matches the queue line; README line 26's backticked path for the release manual goes with its bullet.
* `docs/manuals/release-the-book.md` line 18 is repointed in this delivery instead of a new queue line: it cites the README's section for the install commands this delivery moves out.
* The queue line keeps its wording: "points to" holds for a section that shrinks and links; the page says how much stays.

**Decisions taken alone in /apply.**

* None open: the Contract fixed every line; the batch's driver marks the queue line and runs `make book` once for the batch, so this session did neither (the delivery changes no chapter).

**Divergences.** None: both sections read as the Contract says, byte for byte; no other line of either README changed.

**Proof.** Read beside `make`'s eight lines and `docs/manuals/build-the-book-from-a-clone.md`: every bullet is true in both editions; the manual holds the nodejs.org address, `brew install node`, the `brew` and `apt` lines and `python3-venv`, and the README none of them; the link's target exists from the repository root. No other file in `docs/`, `scripts/` or `.claude/` cites the content removed. `make verify` green after the last edit, the page's move included; `make book` is run by the batch's driver.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of README.md, README.pt.md and `docs/manuals/release-the-book.md` against this page, docs/04 and AGENTS.md, ran `make help` and searched `docs/`, `scripts/` and `.claude/` for citations of the removed text. No findings.

```commit
docs(readme-run-manual): point Build locally to the build manual

- README.md and README.pt.md: requirements, five bullets, one link
- install commands and author-only steps live in the manuals only
- release manual cites the build manual for pandoc, weasyprint, pypdf

work/done/readme-run-manual.md
```
