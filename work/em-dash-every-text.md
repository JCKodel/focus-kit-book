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

* [ ] In a scratch clone, the SVG, the extensionless file, the three other extensions and the invalid-UTF-8 case print the findings above, and the SVG and the extensionless file print nothing before the change; the binary and the run-folder cases print nothing both times; both outputs recorded on the page.
* [ ] `python3 scripts/check_em_dash.py` prints nothing on the clean tree, which holds the two SVGs and the seven extensionless files in its reading.
* [ ] docs/01's row and docs/04 §Tests updated.
* [ ] `make verify` is green.

**Decisions in the review.**

* Text is "no NUL byte in the first 8000", not a list of extensions and not a UTF-8 decode: it is what git decides for a diff, it needs no list to keep up to date, and a decode-based test would drop a file with one bad byte (recommendation of this session; the finding asks for "other text types").
* An invalid-UTF-8 text file is read with replacement, not reported: the check's job is the em dash, and the current code already reads with `errors="replace"`.
* The skip stays `work/done/*-run/` with no extension limit: docs/04 §Tests keeps those folders byte for byte as evidence, whatever the tool wrote in them.
* No test file: docs/04 §Tests; the proof is the scratch clone, as in `repo-files-any-name`.
* Pages in flight: none touches `scripts/check_em_dash.py`. `repo-files-any-name` changes `scripts/repo_files.py`, which this check imports; the two do not conflict, and both read `repo_files()` unchanged in signature.
