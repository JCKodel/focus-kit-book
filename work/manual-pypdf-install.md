# manual-pypdf-install

**Objective.** A person on macOS with Homebrew's Python follows the build manual's install line and gets pypdf where `make book` finds it, without a refusal to work around.

**Behaviour.**

The finding comes from `work/done/m23-review.md`: B3 (`pip install pypdf` is refused (PEP 668) for the Homebrew `python3` that `make book` runs; it cites the build manual :15 and Makefile :36).

* `make book` runs `python3 scripts/build_book.py` (Makefile, target `book`), the first `python3` on the `PATH`, not `.venv/bin/python`; `scripts/release.py` runs the same `python3`. pypdf must be importable by that interpreter.
* Today, on macOS with Homebrew's `python3`, the manual's `pip install pypdf` stops at `error: externally-managed-environment` and installs nothing; `make book` then prints the pypdf message of "What breaks if a step is skipped" (`Makefile:1: book: pypdf not found; install it (see ...)`, with the pointer as `manual-link-pointers` leaves it) and writes nothing.
* A bare `pip` may also belong to another interpreter than the `python3` that `make` runs (on the author's machine `python3` is 3.14 while `/opt/homebrew/bin/python3 -m pip` reports 3.15), so the install command names the interpreter: `python3 -m pip`.
* `python3 -m pip install --user pypdf` is refused the same way (`error: externally-managed-environment`, checked at this page's writing); Homebrew has no `pypdf` formula (`brew info pypdf`: "No available formula"); pipx installs applications, and pypdf is a library. So the manual's macOS line is `python3 -m pip install --user --break-system-packages pypdf`, which installs into the user's site-packages of that `python3`, outside Homebrew's prefix.
* After it, `python3 -c "import pypdf"` exits 0 and `make book` prints the paths of both PDFs and both EPUBs.
* With a `python3` that is not externally managed (the python.org installer, pyenv), the same command installs pypdf; the flag is accepted and changes nothing.
* Debian or Ubuntu: unchanged, `sudo apt install pandoc weasyprint python3-pypdf` installs into the system `python3` that `make` runs.

**Contract.**

One file, edited by its text:

```
docs/manuals/build-the-book-from-a-clone.md  "What must be in place", the macOS sub-item of "For `make book`"
```

* The sentence "macOS: `brew install pandoc weasyprint` and `pip install pypdf`." becomes "macOS: `brew install pandoc weasyprint` and `python3 -m pip install --user --break-system-packages pypdf`, for the `python3` that `make book` runs; Homebrew's Python refuses a bare `pip install` and has no pypdf formula."
* Nothing else in the file changes: the summary sentence ("the PDF and EPUB add pandoc, weasyprint and pypdf"), the "For `make book`" item, the Debian line, "How to undo it" (pip is one of the package managers it names) and the pypdf message under "What breaks" stay true.
* Not touched: `scripts/build_book.py`'s pypdf message, `Makefile`, `requirements.txt`, `README.md`:18, `README.pt.md`:18, `docs/01-Architecture.md`, `release-the-book.md`; none states how pypdf is installed.
* No new term in docs/03; no chapter names pypdf (grep at this page's writing), so no edition changes. The manual is English only, as `README.pt.md` says.

Neighbouring line on the same file: `manual-link-pointers` edits this manual first (the pointer in "What breaks", :27 and :50 at its writing) and is applied before this line, in queue order. This delivery edits only the macOS sentence, by its text, on the file as that delivery leaves it; it does not touch the "What breaks" line or `build_book.py`'s message, which that page said this line "may touch".

**Out of scope.**

* Running `make book` from `.venv/` with pypdf in `requirements.txt`: it changes the command's behaviour and goes stale in docs/01 :13 and :70, both READMEs :18, the manual's summary and install items, `release-the-book.md`:18 and `scripts/release.py`:80; a delivery of its own if the author wants it.
* The workflow's `pip install pypdf==6.9.2` (`.github/workflows/verify.yml`): the runner's Python is not externally managed and the step passes.
* A pinned pypdf version in the manual: the workflow pins it for CI; the manual's reader needs any current one.
* `work/done/m23-review.md`, which quotes the old command: history.

**Done when.**

* [ ] On this machine, `python3 -m pip install --dry-run pypdf` and `python3 -m pip install --dry-run --user pypdf` print `error: externally-managed-environment`, and `python3 -m pip install --dry-run --user --break-system-packages pypdf` prints `Would install pypdf-...`, recorded.
* [ ] `python3 -c "import pypdf"` exits 0, recorded.
* [ ] The manual's macOS sentence reads as Contract says; `grep -n "pip install" docs/manuals/build-the-book-from-a-clone.md` prints only that line, recorded.
* [ ] `make book` prints both PDF paths, recorded.
* [ ] `make verify` green.
* [ ] The Delivery review as docs/05 §5 says.

**Decisions taken alone.**

* The fix is the manual's command, not `make book` moved to the venv: the line asks for pypdf "installed for the `python3` that `make book` runs", and the venv choice would touch seven other places (Out of scope).
* `--user --break-system-packages` over `--break-system-packages` alone: the package lands in the user's site-packages, not in Homebrew's prefix, so a `brew upgrade` or `brew uninstall python` neither breaks nor keeps it there; pip's own refusal names this flag as the way past it.
* `python3 -m pip`, not `pip3`: it binds the install to the interpreter `make` runs, which is what the finding is about.
* The manual says why in half a sentence (Homebrew refuses a bare `pip install` and has no formula), so a reader does not "fix" the flag away.
* The proof is dry runs: pypdf is already installed for this machine's `python3`, and a real install would change the machine.
* No line added under "What breaks if a step is skipped": the refusal is pip's own message, printed at the step itself, and the pypdf line there already covers a skipped install.
