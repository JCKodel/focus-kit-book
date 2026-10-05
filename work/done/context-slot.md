# context-slot

**Objective.** A person or a session reading docs/05 §5 knows where this book keeps what people said: `context/` is listed in `.gitignore`, does not exist today, and the book's private sources live outside the repository, as focus-kit 2026.10.05's Context slot asks.

**Decided by the author.**
1. `context/` is listed in `.gitignore` and not created: the repository is public and the book's sources are private, so the folder may never be committed; the line also keeps a folder created by mistake out of git.
2. The slot says the folder is empty today: the book's sources (Case A, Case B, the author's other projects) stay in folders outside the repository, named nowhere (ADR-0012), and the author's decisions arrive by conversation and go straight into the documents.

**Behaviour.**

* docs/05 §5 has a **Context** line, between **Publish policy** and **Guided project and brownfield project**, in the kit's order (Publish policy, Context, Git).
* The line says `context/` is listed in `.gitignore` and why (the repository is public; the sources are private), that the folder does not exist today, and where the sources are instead, with no path, folder name or term of the disclosure list.
* `.gitignore` has a line `context/`; a file put in `context/` does not appear in `git status`.
* No chapter changes: chapter 19 already teaches the rule this slot follows.
* `make verify` is green, the disclosure scan included.

**Contract.**

* `.gitignore`: one line added, `context/`, after `output/`.
* docs/05 §5, new item after **Publish policy**; the wording below is the intent, /apply may tighten it:

  ```
  * **Context:** `context/` is listed in `.gitignore`: the repository is
    public and what people said about the book's cases is private. The
    folder does not exist today: the sources stay in the author's folders
    outside the repository, named nowhere (ADR-0012), and the author's
    decisions arrive by conversation and go into the documents. A folder
    created later stays out of git; back it up elsewhere.
  ```

* docs/06: the `context-slot` line becomes `[x]` and its description reads "docs/05 §5 gains the kit's Context slot: `context/` listed in `.gitignore`, not created".

**Out of scope.**

* Creating `context/` or moving any source into it: the author chose not to.
* The disclosure scan over ignored files: it reads `git ls-files --cached --others --exclude-standard` (`scripts/repo_files.py`), so it skips `context/` once ignored, and an ignored folder never reaches the repository.
* docs/03's "context folder" term: it already says docs/05 decides.
* Any chapter: chapter 19 already says a public repository ignores the folder.

**Done when.**

* [x] docs/05 §5 has the Context line; `.gitignore` has `context/`.
* [x] `git check-ignore context/x.md` prints the path.
* [x] `make verify` green.
* [x] The line in docs/06 `[x]`, this page in `work/done/`, staged, commit suggested.

**What happened.**

* Built as planned: the Context item went into docs/05 §5 with the contract's wording unchanged, after **Publish policy** and before **Guided project and brownfield project**. `context/` went into `.gitignore` after `output/`.
* Proof: `git check-ignore context/x.md` printed `context/x.md`; `context/` does not exist; `make verify` exited 0, disclosure scan included. No screen and no chapter, so no screenshot and no `make book`.
* Nothing diverged, nothing dropped, no new term (docs/03's "context folder" already defers to docs/05), no ADR.
