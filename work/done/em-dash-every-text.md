# em-dash-every-text

**Objective.** The author runs `make verify` and it fails, naming file and line, when any text file of the repository holds an em dash outside the recorded runs' folders, whatever the file's extension, so a diagram's labels and the extensionless files are read like the chapters.

**Behaviour.**

The proof uses a scratch clone with scratch files, never the tree.

* On the clean tree, `python3 scripts/check_em_dash.py` prints nothing and exits 0. Checked read-only before this page: of the files the check lists outside `work/done/*-run/`, 273 `.md`, 11 `.py`, 4 `.yaml`, 4 `.toml`, 4 `.txt`, 3 `.css`, 2 `.yml` and 1 `.html` are read today; the 2 `.svg` (`book/assets/02-context-window.en.svg`, `.pt.svg`) and the 7 without an extension (`Makefile`, `LICENSE`, `LICENSE-TEXT`, `.gitignore`, `.githooks/commit-msg`, `.githooks/pre-commit`, `work/done/.gitkeep`) are not, and none of the nine holds an em dash. The stricter check changes nothing on today's tree and nothing is fixed in a text.
* Finding B5 holds: the check keeps a file only when its suffix is in `EXTENSIONS` (`check_em_dash.py:14`), so `book/assets/x.svg` with a `<text>` label holding an em dash (U+2014) prints nothing today.
* After the change, that SVG prints `book/assets/x.svg:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence` and exits 1.
* The same message, at the right line, for an em dash in `Makefile`, in `.githooks/pre-commit`, in a `.json`, a `.sh`, a `.csv` and a `.ts` outside a run folder.
* A binary is not read: a file holding a NUL byte in its first 8000 bytes (git's own test) gives no finding even when the bytes `E2 80 94` occur in it, so the 87 PNGs, the fonts, the PDFs and the `.af` files of the tree are silent. A scratch `x.bin` with `00 E2 80 94` prints nothing.
* A text file that is not valid UTF-8 and has no NUL byte is still read, the bad bytes replaced; it does not raise, and an em dash in it is found.
* `work/done/<name>-run/` at any depth is still skipped, every extension: `work/done/foo-run/turn.diff` with an em dash prints nothing; `work/done/foo/page.json` and a file `work/done/foo-run.md` with one print a finding.
* Ignored paths (`output/`, `site/`, `.venv/`) are not listed by `repo_files()` and are not read, as today.
* Only U+2014 is searched; the en dash and the minus stay allowed, as today.

**Contract.**

Files:

```
scripts/check_em_dash.py   reads every listed file that is text; EXTENSIONS removed
docs/01-Architecture.md    the check_em_dash.py row
docs/04-Conventions.md     §Tests: the em dash sentence
```

`scripts/check_em_dash.py`:

* `is_text(data: bytes) -> bool`: no NUL byte in `data[:8000]`.
* `main()` reads each path of `repo_files()` as bytes, skips the run evidence (`is_run_evidence`, unchanged) and the files for which `is_text` is false, decodes the rest with `errors="replace"` and prints `<path>:<line>: em-dash: <MESSAGE>` per line holding U+2014, exit 1 when anything is printed.
* The message, the rule name `em-dash`, the output format and the module docstring's rule name do not change; the docstring says "every text file" and defines text as above.

docs/01: the row reads "no em dash in any text file (no NUL byte in its first 8000), whatever its extension, but the evidence of the runs, work/done/*-run/ (rule "em-dash")". docs/04 §Tests: the em dash sentence says every text file is read, a binary excepted, and the run folders are skipped for every extension. docs/03: no new term.

**Out of scope.**

* Other dashes and other characters (en dash, `--`): AGENTS.md forbids the em dash only.
* A file that may keep an em dash, such as a vendored legal text: none holds one today; the first one decides whether the skip list grows (docs/05 §7).
* Reading inside binaries (PDF, PNG text chunks): the covers and screenshots are not text the check can fix.
* Which files are listed (`repo_files.py`, names with special characters): `repo-files-any-name`.
* The disclosure scan's own reading of text files (it has its own rule for what is text): unchanged.

**Done when.**

* [x] In a scratch clone, the SVG, the extensionless file, the three other extensions and the invalid-UTF-8 case print the findings above, and the SVG and the extensionless file print nothing before the change; the binary and the run-folder cases print nothing both times; both outputs recorded on the page.
* [x] `python3 scripts/check_em_dash.py` prints nothing on the clean tree, which holds the two SVGs and the seven extensionless files in its reading.
* [x] docs/01's row and docs/04 §Tests updated.
* [x] `make verify` is green.

**Decisions in the review.**

* Text is "no NUL byte in the first 8000", not a list of extensions and not a UTF-8 decode: it is what git decides for a diff, it needs no list to keep up to date, and a decode-based test would drop a file with one bad byte (recommendation of this session; the finding asks for "other text types").
* An invalid-UTF-8 text file is read with replacement, not reported: the check's job is the em dash, and the current code already reads with `errors="replace"`.
* The skip stays `work/done/*-run/` with no extension limit: docs/04 §Tests keeps those folders byte for byte as evidence, whatever the tool wrote in them.
* No test file: docs/04 §Tests; the proof is the scratch clone, as in `repo-files-any-name`.
* Pages in flight: none touches `scripts/check_em_dash.py`. `repo-files-any-name` changes `scripts/repo_files.py`, which this check imports; the two do not conflict, and both read `repo_files()` unchanged in signature.

## What happened

**The error it catches** (docs/05 §7): the check kept a file only when its suffix was in `EXTENSIONS`, so an em dash in a diagram's label (`.svg`), in `Makefile`, in a hook or in any extension not on the list passed `make verify` in silence (finding B5).

**Built.** `scripts/check_em_dash.py` drops `EXTENSIONS` and the unused `Path` import, and adds `is_text(data: bytes) -> bool`, true when `data[:8000]` holds no NUL byte. `main()` reads each path of `repo_files()` as bytes, skips the run evidence (`is_run_evidence`, unchanged) and every file `is_text` rejects, decodes the rest with `errors="replace"` and prints the same `<path>:<line>: em-dash: <MESSAGE>` lines, exit 1 when anything is printed. The docstring's first line says "every text file" and its second defines text; the message, the rule name and the output format are unchanged.
docs/01, the `scripts/check_em_dash.py` row, and docs/04 §Tests, the em dash sentence, say so.
No abstraction: the disclosure scan has its own rule for what is text (out of scope), so the NUL test has one occurrence, this one.

**Diverged from the contract.** Nothing.

**Proof.** A scratch clone of this repository at the commit before this delivery, in the session's scratch directory. In the clone, with `E` the em dash (U+2014):

* `book/assets/x.svg`, one line, a `<text>` label holding `E`;
* `Makefile` and `.githooks/pre-commit`, a comment line holding `E` appended (line 34 and line 3);
* untracked `x.json`, `x.sh`, `x.csv` and `x.ts`, each holding `E` (line 1, 2, 2 and 2);
* `x.bin`, the bytes `00 E2 80 94 0A`;
* `latin1.log`, line 1 `caf` and the bytes `E9 20 FF` (not valid UTF-8, no NUL byte), line 2 holding `E`;
* `work/done/foo-run/turn.diff`, `work/done/foo/page.json` and `work/done/foo-run.md`, each holding `E`;
* `output/x.md` (ignored) holding `E`;
* `dashes.md` holding an en dash (U+2013), a hyphen-minus and a minus sign (U+2212).

Before the change (the clone's own `scripts/check_em_dash.py`):

```
$ python3 scripts/check_em_dash.py
work/done/foo-run.md:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
[exit 1]
```

After the change (this delivery's `scripts/check_em_dash.py` copied into the clone):

```
$ python3 scripts/check_em_dash.py
book/assets/x.svg:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
latin1.log:2: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
work/done/foo-run.md:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
work/done/foo/page.json:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
x.csv:2: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
x.json:1: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
x.sh:2: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
x.ts:2: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
.githooks/pre-commit:3: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
Makefile:34: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
[exit 1]
```

The SVG, `Makefile` and `.githooks/pre-commit` print their finding at their own line after the change and nothing before; so do the `.json`, `.sh`, `.csv`, `.ts` and the invalid-UTF-8 `.log`, which is decoded with replacement and does not raise. `x.bin`, `work/done/foo-run/turn.diff`, the ignored `output/x.md` and `dashes.md` print nothing both times. `work/done/foo-run.md` is found both times: it is a file beside the run folders, not inside one.

In this repository, `python3 scripts/check_em_dash.py` prints nothing and exits 0. Outside `work/done/*-run/` it now reads 294 `.md`, 11 `.py`, 4 `.yaml`, 4 `.toml`, 4 `.txt`, 3 `.css`, 2 `.yml`, 1 `.html`, the 2 `.svg` and the 7 files without an extension the page names, and leaves out as binary 87 `.png`, 7 `.ttf`, 2 `.pdf` and 2 `.af`; two of those, `book/assets/cover-en.png` and `book/assets/cover-en.af`, hold the bytes `E2 80 94` and give no finding. `make verify` is green.

**Noted, not fixed.** Nothing.

**Dropped.** Nothing.

**Decisions.**

* The page counted 273 `.md` files; 294 are read today, since the deliveries after the page was written added pages. The other counts match.
* The invalid-UTF-8 case uses a `.log` file, an extension the old list did not hold, so the proof shows the file is now read; a `.txt` would show the same decode both times.
* The docstring's first line became "Check every text file in the repository for an em dash." and a second line defines text, as the Contract asks.
* No screenshot: docs/05 §5 asks one of a toolchain delivery's rendered site, and this one changes nothing the site renders; the proof is the scratch clone, as the page says.
* No ADR and no manual: the change applies AGENTS.md's em dash rule to every text file and changes nothing a person does by hand.

```commit
fix(em-dash-every-text): read every text file for an em dash

- check_em_dash reads every listed file without a NUL byte in its first 8000
- diagrams, the Makefile, the hooks and any extension are read
- the run folders stay skipped, for every extension
- docs/01 and docs/04 say so

work/done/em-dash-every-text.md
```
