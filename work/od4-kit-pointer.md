# od4-kit-pointer

**Objective.** After this delivery a reader of docs/00's OD-4 finds what is true today of the kit's pointers to this book, what is still open, and in which repository and after which delivery it is made.

**Behaviour.** What a reader of docs/00 and ADR-0005 finds.

* OD-4 says that the kit already points at this book. Checked on 2026-10-16 at focus-kit `70fc709`, the version installed here as 2026.10.16.2: its `README.md` and `README.pt.md` ("Documentation") give the site, the Releases and the source of this book, and the installed `references/documents.md` of `/analyze` and `/brainstorm` (the kit's `SETUP.md` §3) names the book and its title. No file of the kit names books.kodel.com.br or an earlier book. What the old OD-4 said, that the kit points at them until launch, is no longer true.
* OD-4 says what is open: the kit's FOCUS pointer is the sentence "FOCUS is chapter 7 of the book ... (`https://jckodel.github.io/focus-kit-book/07-four-pieces/`)" in `README.md`, `README.pt.md` (`/pt/07-four-pieces/`) and `references/documents.md`. M15's `focus-and-slices` removes that file and `renumber-chapters` moves the merged chapter again; the site has no redirects, so the URL stops answering once the site publishes the first, and "chapter 7" is wrong from then on. The pointer is repointed to the chapter's final address, named by the map in `work/done/renumber-chapters.md` (expected `04-focus`, not decided before that delivery is applied), in the three places above.
* OD-4 says where: in the focus-kit repository, by the author, after `renumber-chapters`, and that the installed copies here follow by the kit's next rerun (`kit-<version>` deliveries), never by editing `.claude/skills/` by hand. Until then the pointer is broken for as long as the site has published `focus-and-slices` and the kit has not moved; closing that window is the author's order of pushes.
* Failure: OD-4 does not say the decision is closed. It stays under "Open decisions", narrowed to this one pointer.
* ADR-0005 still reads "repointed at launch (docs/00 OD-4)". It gains one amendment line saying launch repointed the kit at this book and that the FOCUS pointer is the remainder, in OD-4. The ADR's decision does not change.

**Contract.** Text only. docs/00, the OD-4 bullet, replaced by:

```
* **OD-4, repointing the kit.** Launch repointed focus-kit at this book: its README and `documents.md` name the site, the Releases and the source (checked 2026-10-16 at kit `70fc709`).
  Open: the FOCUS pointer there names this book's chapter 7 and `.../07-four-pieces/`, which M15 removes and renumbers.
  The change is made in the focus-kit repository, in its README, README.pt and `documents.md`, to the chapter's final address once `renumber-chapters` is applied, not here.
```

(The bullet keeps "chapter 7" on purpose: it names the kit's old pointer. `renumber-chapters` rewrites "chapter N" only in docs/00's Contents and Audience, not in Open decisions; /apply checks that after M15 the bullet is still true.)

ADR-0005, under Consequences, one line: "Amendment, <date of /apply> (od4-kit-pointer): launch repointed the kit's README and `documents.md` at this book; the pointer to FOCUS is the remainder, in docs/00 OD-4."

**Out of scope.**

* Editing the focus-kit repository or the installed `.claude/skills/` copies: another repository, and the installed files are the kit's (docs/05 §5, the kit's planted files).
* Choosing the final URL: `renumber-chapters`.
* Naming the earlier book or its address in docs/00: the new bullet drops them, ADR-0005.
* Any other line of docs/00: Contents and Audience belong to M15's pages.

**Done when.**

* [ ] The kit's three places re-read at apply time (`git -C ../focus-kit grep -n "focus-kit-book"`), and the bullet says what they say then; if the kit moved, the bullet follows it.
* [ ] docs/00's OD-4 and ADR-0005's line written; no em dash; no other line of either file changes.
* [ ] `make verify` green; page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06 and of docs/00, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* OD-4 stays open, narrowed: docs/00, "Nobody closes these alone"; only the part the evidence shows done is recorded as done.
* The change is made in the focus-kit repository: OD-4's own text and ADR-0005.
* The earlier book is no longer named: ADR-0005, the book mentions none of the author's earlier books.

**Decisions in the review.**

* The bullet records the check by date and kit commit, and says the final address waits for `renumber-chapters`: chosen alone; the alternative, repointing the kit now to `06-focus`, would break again at the renumbering.
* ADR-0005 gets an amendment line, as ADR-0017 and ADR-0008 do, rather than a rewritten consequence: chosen alone.
* Overlap with pages in flight: docs/00 is edited by `focus-and-slices`, `renumber-chapters`, `prologue-and-why`, `simplicity-and-results` and `quick-guide` (Contents and Audience), a different part of the file from OD-4; `focus-and-slices` and `renumber-chapters` do not list the kit's URL, which is outside this repository. No page in flight edits ADR-0005. No docs/03 term is needed.
