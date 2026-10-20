# Build the book from a clone

## What it does and when

From a fresh clone of `JCKodel/focus-kit-book`, it serves the site locally, writes the PDF and EPUB of both editions to `output/`, and runs the checks green.
It is for a reader who wants a local copy, a contributor before a pull request, and the author on a new machine.
Each of the three goals needs only the tools its own step names: the site needs Python 3 and make, the checks add Node.js, the PDF and EPUB add pandoc, weasyprint and pypdf.

## What must be in place

* git.
* Python 3 with its `venv` module, and make. On Debian and Ubuntu the module is a package of its own: `sudo apt install python3-venv`.
* For `make verify`: Node.js 26.12.0 or later, the installer or binary for your system from <https://nodejs.org/dist/v26.12.0/> or, on macOS, `brew install node`.
* For `make book`: pandoc, weasyprint and pypdf.
  * macOS: `brew install pandoc weasyprint` and `pip install pypdf`.
  * Debian or Ubuntu: `sudo apt install pandoc weasyprint python3-pypdf`.
* The network, for the first `make serve`, which installs MkDocs into `.venv/` from `requirements.txt`, and for the link check of `make verify`.

## Steps

1. `git clone https://github.com/JCKodel/focus-kit-book.git`, then `cd focus-kit-book`.
2. `make` lists the commands, one line each.
3. `make serve`, then open <http://127.0.0.1:8000/>. Ctrl+C stops it.
4. `make verify`.
5. `make book`.

`make hooks`, `make scan` and `make release` are the author's: the hooks and the scan in `set-up-the-disclosure-list.md`, the release in `release-the-book.md`.

## How to tell it worked

* The site shows the book's home page in English, at <http://127.0.0.1:8000/focus-kit-book/>, where the address redirects, with the Portuguese edition one click away.
* `make verify` exits 0 and prints `disclosure: skipped, no list`.
* `make book` prints the paths of `output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf` and their EPUBs.

## How to undo it

Delete `.venv/`, `site/` and `output/`, all ignored by git, or the whole clone.
Nothing outside the clone changes but what the package manager installed.

## What breaks if a step is skipped

* No Node: `make verify` fails at the examples check with `Makefile:1: examples: node not found; install Node.js 26.12.0 or later (see docs/manuals/build-the-book-from-a-clone.md)`.
* A Node older than 26.12.0: it fails there with `Makefile:1: examples: node <version> found; Node.js 26.12.0 or later is required (see docs/manuals/build-the-book-from-a-clone.md)`.
* No pandoc, weasyprint or pypdf: `make book` prints `Makefile:1: book: <tool> not found; install it (see docs/manuals/build-the-book-from-a-clone.md)` and writes nothing.
* Offline: the link check prints `links: skipped, no network` and `make verify` can still pass locally; in Actions the same check fails.
* No `venv` module, as on Debian and Ubuntu without `python3-venv`: the first `make serve` stops at `python3 -m venv .venv`, before installing MkDocs; install the package, delete `.venv/` and run it again.
* `make hooks` without the disclosure list: the hooks refuse every commit, so a person running the book does not run it.
* The list on the machine and the hooks off, as for the author in a new clone: `make verify` fails with `Makefile:1: disclosure: hooks are off; run make hooks`.

The author's setup for the last two is in `set-up-the-disclosure-list.md`.
