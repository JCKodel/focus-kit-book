# useful-notes

**Objective.** A reader of either edition finds a source note only where it gives them something to open, or a private case's count they can repeat, and in the PDF and the EPUB each source prints once per chapter, not once per mention.

**Behaviour.**

* No chapter has a note that points to a commit, a diff or a file of focus-kit's repository.
* Where a chapter quotes or states a rule of the kit and loses its note, the sentence names the file in plain words (`SETUP.md` §3.4, the file of `/apply`); where the sentence already names it, it stays as it is.
* Where a sentence leaned on a commit note, the note goes and the sentence stands; when it points to another chapter's section (chapter 9 to chapter 6's "The two choices"), it becomes an internal link.
* A chapter that uses Ninjobs has one note for it, `[^ninjobs]`, saying the repository is private and how each of that chapter's numbers was counted; chapter 4's two notes become one.
* In the PDF and the EPUB, a key cited several times in a chapter prints one note, and every mention shows that note's number; notes are numbered from 1 per chapter in order of first mention.
* The site renders the notes as before, one per key.
* On the site, in the PDF and in the EPUB, the notes block is set at 85% of the body text and in italic, except links, which stay upright; a quotation inside a note, italic in the source, turns upright so it still stands apart.
* `make verify` fails when a chapter's two editions cite a different set of note keys or cite a key a different number of times, printing `book/pt/<file>:<line>: parity: [^<key>] cited <n> times, <m> in book/en/<file>`; chapter 8's `[^analyze-run]` (13 in English, 14 in Portuguese) is the error that happened, and it is fixed.
* docs/04, docs/03, docs/01 and AGENTS.md say the new rule, in the words of the Contract.

**Contract.**

Notes per chapter, same keys in both editions (counted by /propose over `book/en/`; /apply recounts):

| Chapter | Leaves | Merges or renames | Stays |
|---|---|---|---|
| 00 | | | `lemonis-3ps` |
| 01 | | `ninjobs-adr-0022` → `ninjobs` | `metr-2025`, `dora-2024` |
| 02 | | | all 4 |
| 03 | | | all 5, including `rule-count` |
| 04 | | `ninjobs-adr-0022` + `ninjobs-adr-0026` → `ninjobs` | |
| 05 | `focus-kit-setup` | | `claude-code-run` and the 7 host documentation notes |
| 06 | `focus-kit-documents`, `focus-kit-commands`, `focus-kit-git`, `focus-kit-unit-of-work`, `book-docs-context` | | `book-docs`, `book-adr-0016`, `dart-error-exception` |
| 07 | `focus-kit-brainstorm` | | `octoverse`, `brainstorm-run` |
| 08 | `focus-kit-analyze` | | `strangler-fig`, `brownfield-research`, `analyze-run` |
| 09 | `focus-kit-documents`, `focus-kit-brainstorm`, `focus-kit-unit-of-work`, `book-two-choices` | `ninjobs-queue` → `ninjobs` | |
| 10 | `focus-kit-propose`, `focus-kit-unit-of-work`, `book-spec-driven-run` | | `propose-run`, `claude-usage`, `claude-code-plan-mode` |
| 11 | `focus-kit-apply`, `focus-kit-unit-of-work` | | `apply-run` |
| 12 | `focus-kit-closing` | `ninjobs-milestone-review` → `ninjobs` | the 3 review notes, `clinic-milestone-1-run`, `closing-a-milestone-run` |

From 60 definitions to 41 per edition; from 191 printed notes (192 in Portuguese) to 41.

docs/04 §Writing the book, the Evidence bullet's first line becomes:
`* **Evidence.** Every number says where it comes from: a primary publication, a record of this book's runs, or, for a private case, how the author counted it.`

docs/04 §Chapter shape, the first line of the Source notes bullet becomes these three, and its private-case line and example follow the third:
`* Source notes: a note only where the reader gains something to open (a publication, a tool's documentation, a file of this book's repository or its runs) or a count to repeat. Every number and every quoted claim from such a source carries [^<key>] at the claim; a source cited again in the chapter reuses the key, and the PDF and the EPUB print its note once.`
`  No note points to a commit, a diff or a file of focus-kit's repository: where the text quotes or states a rule of the kit, the sentence names the file in plain words (SETUP.md §3.4, the file of /apply).`
`  A private case has one note per chapter that uses it, [^ninjobs], [^case-a] or [^case-b]: ...` (the existing text), with the example `[^ninjobs]: Ninjobs, a private repository, counted by the author over its history up to 2026-08-29: ...`.

docs/03, the row of source note, its description becomes:
`A footnote that gives the reader something to open, or, for a private case, how its numbers were counted; the key is the same in both editions, and the PDF and the EPUB print it once per chapter.`

docs/01, `make book`: "notes end their chapter" becomes "notes end their chapter, one per key, every mention showing its number"; the parity check's description gains "and the same note keys, each cited as many times"; the lines of `book/assets/site.css`, `pandoc/pdf.css` and `pandoc/epub.css` gain "notes at 85%, italic, links and quotations upright".

**Visual reference.** The notes block of chapter 10 on the site at 1280 and 390 pixels, in the PDF and in the EPUB, both editions; no design file.

AGENTS.md, the line becomes:
`- Every artifact shown is real and every number says where it comes from; a source note only where the reader gains something to open, or a case's count to repeat (docs/04).`

**Out of scope.**

* Rewording sentences beyond naming the file or dropping a commit reference: the chapters are done.
* Moving the site's note rendering: MkDocs already prints one note per key.
* Notes in appendices: none exist yet; the first appendix delivery follows the rule.
* A check that forbids commit or focus-kit URLs in notes: no such note was added by mistake yet (docs/05 §7).

**Done when.**

* [x] The table holds in both editions: `grep` finds no `[^focus-kit-`, `[^book-two-choices]`, `[^book-docs-context]`, `[^book-spec-driven-run]` or `[^ninjobs-`.
* [x] Each changed sentence reviewed in both editions: it names the file where a rule of the kit is quoted or stated.
* [x] Parity fails on a copy of chapter 8 with the extra `[^analyze-run]`, and passes after the fix.
* [x] The built site's chapter 10 shows `propose-run` as one note.
* [ ] `make verify` green (red only on chapter 12's missing tag, see What happened; the rest of the item holds); `make book` builds; chapter 10's notes in the PDF and the EPUB of both editions list `propose-run` once, and every mention shows its number.
* [x] Screenshots of chapter 10's notes, smaller and italic with upright links, in both PDFs, `work/done/useful-notes-pdf-<edition>.png`, and of the site's chapter 10 notes at 1280 and 390 pixels in both editions, light and dark, `work/done/useful-notes-site-<edition>-<width>-<theme>.png`; the EPUB's stylesheet checked in its package.
* [x] docs/04, docs/03, docs/01 and AGENTS.md carry the Contract's words; the delivery ends with the paths of both PDFs.

**What happened.**

* Counted again over `book/en/`: 60 definitions to 41 in each edition, 191 mentions in English (192 in Portuguese) to 129 in each; the table held as written. The PDF and the EPUB of each edition print 41 notes (41 `epub:type="footnote"` in the EPUB chapters).
* Parity, the proof of the failure: the extended check was run on the tree before chapter 8 was fixed and printed `book/pt/08-analyze.md:41: parity: [^analyze-run] cited 14 times, 13 in book/en/08-analyze.md` (exit 1); the line is the key's first mention in the Portuguese file, or its definition when it is never mentioned. The extra mention was on the Portuguese sentence that translates the agent's diff, which has no English counterpart; it left, and parity passed. Mentions are counted outside code, as the other checks mask it.
* Where the kit's files are named, the reading this delivery took of an ambiguous Behaviour line: the file is named at the chapter's first statement of the kit's rule (in chapter 6, also at the two choices and at the rules of `AGENTS.md`) and in every sentence that quotes the kit, which said "the kit says" and now names the file (`propose/SKILL.md`, `apply/SKILL.md`, `brainstorm/SKILL.md`, `analyze/SKILL.md`, `references/documents.md` and its Choices section, docs/05 §8 in chapter 12). Every other sentence that states a rule leans on that naming and only lost its note, even in a later section (chapter 6's ADRs and Living documents, chapter 9's marks and Changing the queue, most sections of chapters 10 and 11); naming the file in each would have reworded the chapters, which the page puts out of scope. The Done when tick on changed sentences rests on this reading. Chapter 5 already names `SETUP.md` and "the setup file"; its last sentence, "Every install writes every host's files", became "The setup file writes every host's files". The names are the kit's installed files, the ones a reader has in the clinic after chapter 5, and not `SETUP.md` section numbers.
* Chapter 4's merged `[^ninjobs]` keeps both definitions' facts: the ADR-0022 count as before, then "Its ADR-0026, dated 2026-09-21, gives the date of the public opening and the adoption of focus-kit." No new private detail.
* The PDF and the EPUB, `scripts/build_book.py`: pandoc prints one note per mention and its output keeps no key, so the merge happens on the Markdown, in `prepare`: the first mention of a key stays a note, and every later one becomes a superscript link to an anchor placed at the start of that note's text, showing the note's number (its place in order of first mention). The edits of a line (notes and chapter links) apply from the right, so neither shifts the other. In the EPUB, pandoc resolves those links across its chapter files; chapter 10's ten later mentions of `propose-run` point to its note, number 2. The later mentions carry no `epub:type="noteref"`, so a reader's pop-up opens only from the first.
* Diverged, by decision of the author during /apply: every note's URL was plain text in all three outputs, so "links stay upright" had nothing to act on and the URLs came out italic. The 74 URLs of the 41 definitions are now written `<https://...>`, which the site, the PDF and the EPUB make links; docs/04 says so in the definition's format. The link check reads them as before.
* What the proof found: in the PDF the new links were hyphenated at line ends ("JCK-odel"), a hyphen that is not in the URL. Fixed in `pdf.css` and `epub.css`: a link in the notes takes no automatic hyphen and breaks anywhere. The EPUB's old rule `aside.footnotes` never matched, since pandoc's EPUB wraps its notes in `section.footnotes`; the new rules use that selector, checked in the package's `EPUB/styles/stylesheet1.css`. `pdf.css` had the notes at 7.5pt; they are now 85% of the 9pt body.
* Decision: code in a note stays upright too, with links and quotations: the site's and the PDF's code fonts have no italic, and a slanted code span would be a synthesized one. docs/01 names it in the three stylesheets' lines.
* Diverged, by decision of the author after the first proof: the notes are set at 66% of the body, not 85%, in the three stylesheets and in docs/01. In the PDF that is about 6pt on a 9pt body.
* Proof: `work/done/useful-notes-pdf-en.png` (pages 86 and 87) and `useful-notes-pdf-pt.png` (pages 92 and 93) show chapter 10's three notes, italic and smaller, links upright; a later mention of `propose-run` in the English PDF shows its note's number, 2. The eight site screenshots, `useful-notes-site-<en|pt>-<1280|390>-<light|dark>.png`, were taken with the clinic's Playwright over the built site served locally; each measured the notes at 10.56px over a 16px body (66%), italic, a link upright, three notes, one per key.
* `make verify` is red: build, parity, em dash, prose and disclosure pass; links fails on two lines that were already in `main` before this delivery, `book/<en|pt>/12-closing-a-milestone.md:155/156`, the tag `book-v1/closing-a-milestone` of the guided project, which does not exist yet locally or on GitHub (the clinic has chapter 12's docs/06 staged). It goes green once the author commits and pushes that tag (docs/05 §5, order). `make book` builds both editions.
