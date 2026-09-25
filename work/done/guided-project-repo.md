# guided-project-repo

**Objective.** The guided project has a name, a license, a language and a tag rule, and a public repository `JCKodel/focus-kit-clinic` that holds only its README and licenses at tag `book-v1/start`, so chapter 5 can install the kit on it and every later chapter can quote it by tag.

**Behaviour.**

* The name `focus-kit-clinic` closes OD-2. It also settles "clinic or salon" (docs/00, ADR-0008) as a clinic, which chapter 3's run already used.
* /apply creates the repository locally in the sibling directory `../focus-kit-clinic` (`git init -b main`), writes the three files below, and stages them. It never commits, creates the remote, tags or pushes there either (docs/05 §5).
* After this delivery, the repository has no code and nothing that `/brainstorm` writes: no `docs/`, no `AGENTS.md`, no `package.json`. The clinic's name, its features and the stack decisions of chapter 7 are not settled here.
* The README is in English only. It says what the repository is and links the book at its site URL. It explains the tag rule and says which license covers what. It does not link or name any of the author's earlier books or their companion repositories (ADR-0005). It carries no term of the disclosure list.
* The tag rule: a chapter that changes the guided project ends with a tag `book-v1/<chapter-slug>` on the commit it quotes. A chapter that does not change it gets no tag, and its exercises start from the latest earlier tag. `book-v1/start` is the empty starting point, before chapter 5.
* Order for every later chapter: the author commits and pushes the guided project's tag before the chapter's `make verify` can pass, because `scripts/check_links.py` opens every tag URL the chapter cites.

**Contract.**

Repository: `JCKodel/focus-kit-clinic`, public, default branch `main`, description "The guided project of One Page at a Time: a clinic scheduling app built with focus-kit, one tag per chapter."

Files at `book-v1/start`, nothing else:

```
README.md      English. Sections: what this is (the clinic scheduling app the book builds, from an empty folder, with focus-kit); the book (https://jckodel.github.io/focus-kit-book/, Portuguese edition under pt/); tags (book-v1/start, then book-v1/<chapter-slug>, a chapter that changes nothing has no tag); licenses (the table below)
LICENSE        AGPL-3.0 text, the same file as this repository's LICENSE
LICENSE-TEXT   CC BY-SA 4.0 legal code, the same file as this repository's LICENSE-TEXT
```

Licenses (ADR-0003, applied unchanged):

| What | License |
|---|---|
| Code, scripts, configuration | AGPL-3.0-only |
| `docs/`, `work/`, README | CC BY-SA 4.0 |
| focus-kit's installed command files | AGPL-3.0-only, under focus-kit's own terms |

Tag: `book-v1/<chapter-slug>`, where `<chapter-slug>` is the chapter's file name without `NN-` and `.md` (`book/en/07-brainstorm.md` → `book-v1/brainstorm`). Annotated, message "One Page at a Time, chapter <slug>". A published tag never moves. A second edition of the book tags `book-v2/*`. The book quotes a file as `https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/<slug>/<path>`.

Language: identifiers and documents in English (the guided project's docs/05 slot will say English). The Portuguese edition shows its prose artifacts translated, as docs/04 §Evidence says.

Documents /apply changes in this repository:

```
docs/adr/ADR-0008-guided-project.md  "Amendment" dated at /apply: name, clinic over salon, licenses as ADR-0003, English only, the tag rule
docs/00-Product.md                   OD-2 closed, pointing to the amendment; the Mechanics line names JCKodel/focus-kit-clinic
docs/03-Domain.md                    guided project row: Identifier `JCKodel/focus-kit-clinic`, the placeholder note removed
docs/01-Architecture.md              the guided project line names the repository and the tag form
docs/04-Conventions.md               the Code line names the tag form
docs/05-Process.md                   §5 new slot "Guided project": the sibling directory ../focus-kit-clinic, the tag rule, and the order (the author pushes the tag, then the chapter's verify goes green)
docs/06-Queue.md                     guided-project-repo [x]
```

The author's commands after the commit here (written on this page and in the commit body; the agent never runs them):

```
cd ../focus-kit-clinic
git commit -m "Start: README and licenses"
gh repo create JCKodel/focus-kit-clinic --public --source=. --remote=origin --push --description "<description above>"
git tag -a book-v1/start -m "One Page at a Time, starting point"
git push origin book-v1/start
```

**Out of scope.**

* Installing the kit and running `/brainstorm`: chapters 5 and 7 (`install-and-hosts`, `brainstorm`).
* Any code, `package.json` or stack file: ADR-0008 fixes the stack and `/brainstorm` writes it down.
* A Portuguese README or a second repository: English only, decided here.
* The exercise answers' tags: `exercise-answers` decides whether answers get their own tags.
* A disclosure scan of the other repository: its three files are written here and read before staging. Scanning it every time would be a new tool that no delivery has asked for.

**What happened.**

* Built as planned: `../focus-kit-clinic` initialised on `main`, the three files written and staged, nothing committed there.
* The README goes slightly past the contract, inside its four sections: the Portuguese edition is a full link (`https://jckodel.github.io/focus-kit-book/pt/`), the license table has a File column as this repository's README does, and the tags section shows `git checkout book-v1/start` so a reader knows how to use a tag.
* docs/00 Mechanics now says "a tag per chapter that changes it", so the tag rule is not contradicted there.
* The docs/03 row `chapter tag` was written during /propose; this delivery only replaced the guided project's placeholder identifier.
* Proof: `cmp` shows `LICENSE` and `LICENSE-TEXT` identical to this repository's; the README has no em dash and matched no entry of the disclosure list in a one-off run of the scan's own loader (not a new tool); it names no earlier book. `make verify` green.
* No new ADR: ADR-0008 carries an amendment.

**Done when.**

* [x] `../focus-kit-clinic` exists, on `main`, with exactly `README.md`, `LICENSE` and `LICENSE-TEXT` staged and nothing committed.
* [x] The README has the four sections of the contract, no link to an earlier book or its companions, and no em dash.
* [x] `LICENSE` and `LICENSE-TEXT` are byte for byte this repository's files (`cmp`).
* [x] ADR-0008 amended; docs/00 OD-2 closed; docs/01, 03, 04, 05 and 06 updated as the contract says.
* [x] `make verify` green in this repository.

The two Author items stay unchecked when /apply stages:

* [ ] Author, after the commit here: the commands above run; the repository URL recorded here.
* [ ] Author: `git -C ../focus-kit-clinic ls-remote --tags origin book-v1/start` prints the tag.
