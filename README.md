Português: [README.pt.md](README.pt.md)

# One Page at a Time

*Delivering Software and Projects with Coding Agents*

J.C. Ködel

A free book that takes a reader who has never followed any process to running whole projects with coding agents: Spec-Driven Development as the idea, focus-kit as the method and its tool, FOCUS as the optional architecture, and just enough git to work with parallel agents and teams.

## Read

* The site: <https://jckodel.github.io/focus-kit-book/>
* PDF and EPUB, in English and Portuguese: on this repository's [Releases](https://github.com/JCKodel/focus-kit-book/releases) and on <https://books.kodel.com.br>

## Build locally

You need Python 3 and make.

* `make serve` opens the site at <http://127.0.0.1:8000/>.
* `make verify` runs the checks.

## How it is written

The book is written with [focus-kit](https://github.com/JCKodel/focus-kit): `docs/` holds the project documents, `docs/06-Queue.md` the queue, and `work/done/` one page per delivery.
This repository is the book's example of a project that is not software.

## Contributing

* An error or a suggestion: open an issue.
* A fix: open a pull request that changes both editions, with `make verify` green.

Contributions are accepted under the license of the file they change.

## License

| What | License | File |
|---|---|---|
| The book's text and figures (`book/`), the project documents (`docs/`, `work/`) and these READMEs | CC BY-SA 4.0 | [`LICENSE-TEXT`](LICENSE-TEXT) |
| Scripts, build and site configuration (`scripts/`, `Makefile`, `mkdocs.yml`, `overrides/`, `book/assets/site.css`) | AGPL-3.0-only | [`LICENSE`](LICENSE) |
| focus-kit's installed command files | AGPL-3.0-only, under focus-kit's terms | [`LICENSE`](LICENSE) |
