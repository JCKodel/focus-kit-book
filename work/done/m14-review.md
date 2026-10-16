# m14-review

**Objective.** The author knows, clause by clause, whether M14's paragraph holds in the hands of a reader of the book and in this repository, in both editions, and, for the first time, whether the whole repository's code and documents hold under a deep review launched against the commit that closed M13; each confirmed finding is a `[ ]` line in M14 under this review.

**Decided from the documents.**

1. The person tests the clauses alone; the agent prepares, records and writes the lines (docs/05 §8; `m13-review` did the same).
2. The review also reads the code (docs/05 §8 after `kit-2026-10-16-2`): the page names the commit that closed M13, `0c50f1b`, the commit of `plain-numbers`, M13's last commit; the author launches the Milestone review slot's command against it, `/code-review ultra 0c50f1b`, and the agent never launches it. The repository's "code" is `scripts/`, the Makefile and the build; its documents are read with it.
3. The paragraph's first clause has two halves: the book teaches the kit, answered by M14's seven chapter lines, `ch14-18-kit-wording` included, and the repository runs on it, answered by `kit-2026-10-16-2`, tested by opening this repository's documents (`m13-review` decision 2).
4. A finding the code review confirms is a finding like the others: one `[ ]` line, saying what will be true. No second review (docs/05 §8).
5. The review is M14's last line and runs after every other M14 line is `[x]`: the queue line gains `· after ch14-18-kit-wording`, the one M14 line not yet done when this page was revised, written now because the dependency is known now (docs/05 §4, a known dependency is an `after`; §8, the review is the last line).

**Behaviour.**

* The author receives both PDFs (`make book`), the page where each passage below starts in each PDF, and the clause table, and tests each clause by reading the passages it names, in English and then in Portuguese; C1's second half by opening the files it names.
* For each clause the author answers, in the conversation, `C<n>: holds` or `C<n>: fails, <what the reader does not get>`; a clause that fails is a finding.
* The author launches `/code-review ultra 0c50f1b` only once every other M14 line is `[x]` and committed, so the review reads chapters 14 and 18 as `ch14-18-kit-wording` leaves them, and reports, in the conversation, which of its findings they confirm; each confirmed one is a finding.
* Each finding becomes one `[ ]` line in M14 under `m14-review`, saying what will be true, never how to fix it, shown to the author before staging; the author may reword them. No M14.1.
* An answer missing for some clauses, or the code review not yet launched: the page records what was given, the line waits as `[?]` with `· resume: apply · blocked: <what is missing>`, and nothing is staged (docs/05 §4, §6).
* Edge: `/apply` started while an M14 line other than this one is not `[x]`: the line waits as `[?]` with `· resume: apply · blocked: after <slug>`, and no passage is tested.
* No file under `book/` and no document but docs/06 and this page is edited by this delivery.

**Contract.**

The clause table, what the author tests (M14's paragraph, quoted: "When this milestone closes, the book teaches focus-kit 2026.10.16.2 and the repository runs on it: a milestone review that also reads the code through the Milestone review slot, `/apply` reading the whole queue and ending on which environment is at which version, a request outside `/apply` that stops at the line with a draft for a fresh `/propose`, a hidden folder and a branch prefix named by the kit and no tool that plants it, every slot of docs/05 §5 named where the book lists them, and an update example at the current version."):

| | Clause | Answered by | Passage (en; pt the same headings) | How the author tests it |
|---|---|---|---|---|
| C1 | the book teaches focus-kit 2026.10.16.2 and the repository runs on it | `kit-2026-10-16-2`; every chapter line of M14 | 11 §What an update reports; 14 §What `/propose` does, §The page; 18 §What the process does not have. Repository: docs/05 §§2, 3, 4, 5, 7, 8; docs/03; `AGENTS.md`; the four skills' version | Does each rule below stand in this repository's documents as the chapter teaches it? Does any file under docs/ or `AGENTS.md` still say "same session", "reviews no code" or the earlier hidden-folder default? Is the sentence chapter 14 quotes found verbatim in the kit's README and README.pt, does its Contract give three reasons, and does chapter 18 read "no gate before implementation beyond a complete page"? |
| C2 | a milestone review that also reads the code through the Milestone review slot | `ch17-review-reads-code` | 17 §The review is a delivery, §Read the whole code once; 13 §The review, and its findings; 25 §Roles in a team | Can a reader say what the review's page names, who launches the deep review, against what, and what a confirmed finding becomes? |
| C3 | `/apply` reading the whole queue and ending on which environment is at which version | `ch15-24-whole-queue` | 15 §What it reads, §The message; 24 §Why the page and the documents keep sessions small | Can a reader say why `/apply` reads the whole queue, what keeps that read small, and what its last words are? |
| C4 | a request outside `/apply` that stops at the line with a draft for a fresh `/propose` | `ch13-14-19-line-stops` | 13 §Changing the queue; 14 §When you do not know yet; 19 §The manager's session | Asked for a small change in an ordinary session, does a reader know the answer stops at the line, where the detail goes, and what they run next? |
| C5 | a hidden folder and a branch prefix named by the kit and no tool that plants it | `ch21-hidden-folder` | 21 §Worktrees in the kit, §The life of a worktree | Can a reader name the default hidden folder and prefix, and does chapter 21 name no tool that plants the kit? |
| C6 | every slot of docs/05 §5 named where the book lists them | `ch10-12-all-slots` | 10 §The seven documents, §Where a new fact goes; 12 §`/brainstorm`: a new project, and §What it asks under `/analyze` | Can a reader list the nine slots, and say which ones each command asks about? |
| C7 | an update example at the current version | `ch11-update-2026-10-16-2` | 11 §Install, §What an update reports | Does the install sentence match the kit's README, and does each item of the report match a check the setup file makes today? |
| C8 | the whole, read by the code review | `/code-review ultra 0c50f1b`, launched by the author | the review's own output | Which findings does the author confirm? |

Line numbers and PDF pages are given by /apply from the files at the start of the delivery and from `make book`.

The review's queue line, as this page leaves it, and the findings' lines, in docs/06 under M14, after it:

```
[x] m14-review               the review of M14 as docs/05 §8 says · after ch14-18-kit-wording
[ ] <slug>                   <what will be true>
```

**Out of scope.**

* Fixing anything: each finding is its own delivery (docs/05 §8).
* Launching the code review: the author does, as the Milestone review slot says.
* M15's lines and pages, uncommitted in the tree: another delivery's work (docs/05 §4); they wait on this review, as their `· after m14-review` says.

**Done when.**

* [x] Both PDFs built and their paths given to the author, with the page of each passage.
* [x] Every clause answered by the author and recorded on this page; the code review launched and its confirmed findings recorded.
* [x] Each finding a `[ ]` line under `m14-review` in docs/06, worded as what will be true.
* [x] `make verify` green; page in `work/done/`, the line `[x]`, staged with its own hunk of docs/06 only, split from the uncommitted M15 section beside it with selective staging, never by path (docs/05 §6); the commit suggested in a `commit` block.

**Decisions in the review.**

* The base commit is `0c50f1b`, M13's last commit, as recommended; the slot's command is `/code-review ultra 0c50f1b`, launched by the author.
* Revised by a second /propose: passages named by the chapters' headings as they are today; C1 extended to chapters 14 and 18, for `ch14-18-kit-wording`; the queue line gains `· after ch14-18-kit-wording`, and the code review is launched only after that line is committed.

**Where each passage starts.** From `make book` at the start of the delivery, on 2026-10-16: `output/one-page-at-a-time.pdf` (en) and `output/uma-pagina-de-cada-vez.pdf` (pt), PDF page numbers.

| Clause | Passage | en | pt |
|---|---|---|---|
| C1 | 11 §What an update reports | 82 | 86 |
| C1 | 14 §What `/propose` does | 107 | 111 |
| C1 | 14 §The page | 108 | 112 |
| C1 | 18 §What the process does not have | 140 | 145 |
| C2 | 17 §The review is a delivery | 133 | 138 |
| C2 | 17 §Read the whole code once | 134 | 139 |
| C2 | 13 §The review, and its findings | 102 | 106 |
| C2 | 25 §Roles in a team | 192 | 202 |
| C3 | 15 §What it reads | 115 | 119 |
| C3 | 15 §The message | 121 | 125 |
| C3 | 24 §Why the page and the documents keep sessions small | 186 | 196 |
| C4 | 13 §Changing the queue | 102 | 106 |
| C4 | 14 §When you do not know yet | 112 | 116 |
| C4 | 19 §The manager's session | 148 | 153 |
| C5 | 21 §The life of a worktree | 165 | 172 |
| C5 | 21 §Worktrees in the kit | 167 | 175 |
| C6 | 10 §The seven documents | 72 | 76 |
| C6 | 10 §Where a new fact goes | 76 | 81 |
| C6 | 12 §`/brainstorm`: a new project | 90 | 94 |
| C6 | 12 §What it asks | 93 | 97 |
| C7 | 11 §Install | 80 | 84 |
| C7 | 11 §What an update reports | 82 | 86 |

C1's repository half, by line at the start of the delivery: docs/05 §2 line 14, §3 line 39, §4 line 88, §5 line 157 (Milestone review and Git slots inside it), §7 line 277, §8 line 285; docs/03 line 88 (container folder); `AGENTS.md`; the four skills, `.claude/skills/{analyze,apply,brainstorm,propose}/SKILL.md` line 9, each `version: "2026.10.16.2"`. A search of docs/ and `AGENTS.md` for "same session" finds docs/03 line 36 (headless: the reader keeps typing in the same session) and two `[x]` lines of docs/06, M3 and M13, as history; "reviews no code" is found nowhere.

**Divergences.**

* The code review (C8) was not `/code-review ultra 0c50f1b`. The author started it and cancelled it, launched `/code-review high 0c50f1b` in the background, and asked this session to run the review itself with agents on Sonnet. Four read-only agents read the whole: the build code against docs/01 and docs/04; the process documents, ADRs and manuals against each other and the installed skills; chapters 10 to 19, 21, 24 and 25 in both editions against the kit; and the kit's three installed copies, the READMEs and `.gitignore`. This session checked each finding against the file before showing it to the author, who confirms which ones count. docs/05 §5's Milestone review slot is unchanged: this was the author's call for this review, not a new rule.

**C8, the code review's candidates.** Checked by this session against the files; "seen" means the line says what the finding says, "latent" that nothing in the book triggers it today, "weak" that the claim does not hold as stated. The author confirms which count.

Build code:

* B1 `scripts/repo_files.py:11`: `git ls-files` without `-z` quotes a non-ASCII name, so the file is skipped by every check, the disclosure scan included; the pre-commit hook, which uses `-z`, would catch it. Seen.
* B2 `mkdocs.yml`: no `validation:` block, so a link to a missing heading, `NN-<slug>.md#<anchor>`, passes `--strict`; `make book` prints weasyprint's error and exits 0. Seen.
* B3 `scripts/check_disclosure.py:115`: the commit-msg hook skips lines starting with `#`, which `git commit -m` keeps in the commit. Seen.
* B4 `pandoc/epub.css:24`: `a[href*="#chapter-"]` never matches pandoc's `#<file>__chapter-` ids, so in the EPUB a chapter link keeps the link colour. Seen.
* B5 `scripts/check_em_dash.py:14`: SVG, extensionless files and other text types are not read. Seen, latent.
* B6 `scripts/check_links.py:47-65`: a URL inside `<...(x)>`, `[url](url)` or `**url**` is cut at the wrong place, giving a false 404. Reported with a reproduction, not reproduced here.
* B7 `scripts/build.py:30-34`: a repeated broken link is located at its first occurrence. Reported, minor.
* B8 `scripts/check_parity.py:21`, `scripts/build_book.py:49`: a mention followed by `:` is not counted, and an uppercase key is invisible. Seen in the regex, latent.
* B9 `scripts/build_book.py:140`: appendices sorted as text, `A10-` before `A2-`. Seen, latent.
* B10 `scripts/check_parity.py`: the READMEs' same sections in the same order (docs/04) are not checked. Seen.
* B11 `scripts/patterns.py`: a plain entry does not match the other apostrophe, against docs/04. Reported, latent.
* B12 `Makefile`: `touch .venv` after a failed install marks the venv as built. Reported, minor.

Documents:

* D1 docs/03:103: `resume: apply` back to `[>]` "only when its page is still complete", a condition docs/05 §4 dropped. Seen.
* D2 `AGENTS.md:28`, docs/01:72-73 and 102: the guided and brownfield projects and their tags described as live, against ADR-0017 and docs/05 §5. Seen.
* D3 docs/05:82-83: a chapter page's Contract lists "the exercises", retired by ADR-0017. Seen.
* D4 docs/00:89-90: OD-4 says the kit points FOCUS elsewhere until this book launches; the installed kit already points at this book's chapter 7. Seen.
* D5 docs/06:3: the legend says `[>]` "defined, `work/<slug>.md` exists", where docs/05 §4 says completely defined; a draft page can exist for a `[ ]` line. Seen.
* D6 docs/03:76: the `tag` row names the book's chapter tags as live; docs/03 retires them. Seen.
* D7 docs/03:96 and 118, docs/04:26: "§Evidence", "§Source notes", "§running example" name no heading. Seen.
* D8 docs/01's tree leaves out `context/` and `.DS_Store`, which `.gitignore` ignores. Seen, minor.

Chapters (L3 to L10 from the `/code-review high 0c50f1b` the author launched, which read M13's last commit):

* L1 chapter 16, en 92 and 134, pt 93 and 135: `resume: apply` said two ways, the key point keeping "only if its page is still complete", and line 92 differing from docs/05 §4's return to `[ ]` when scope became undecided. Seen.
* L2 chapter 17:20, both editions: "or none when the slot says so" reads as the base, not the slot. Seen, minor.
* L3 chapter 9:84, both editions: the key point says OpenSpec gave four screens and "its checks", where the gain above says the old process. Seen.
* L4 chapter 9:87, both editions: "six places" beside "many places" in key point 1, against docs/04's one number. Seen.
* L5 docs/04:32 against docs/04:45 and the gains of chapters 3, 9 and 26: "the one number" against a gain with no number or a before/after pair. Seen.
* L6 chapter 3:66, both editions: "a rule restated in each file", after "OpenSpec in 4 of its 6". Seen.
* L7 chapter 3:77, both editions: "OpenSpec produced 37,228 lines" makes the tool the cause, where chapter 9 names the old process. Seen.
* L8 chapter 24:39: 738 thousand "without cache reads" has no row; it is All minus Cache read, divided by 93, derivable from the table. Weak.
* L9 chapter 26:34: "followed at least one" lost its noun and the size of the effect. Seen.
* L10 chapter 26:139 (the review said 152), both editions: "In every run ... in two runs". Seen.

**The author's answers.**

* C1 to C7: holds, in both editions and, for C1, in the repository's documents.
* C8: the author confirmed the candidates above and asked for one line per file; where one fact stands in two files, the line holds both. L8 is left out, as this session judged it weak: the 738 thousand is the table's All minus Cache read, divided by 93.

**Findings, one line per file.** In docs/06 under `m14-review`, in this order:

| Line | Files | Candidates |
|---|---|---|
| `repo-files-any-name` | `scripts/repo_files.py` | B1 |
| `site-build-anchors` | `mkdocs.yml`, `scripts/build.py` | B2 (site), B7 |
| `book-build-links` | `scripts/build_book.py` | B2 (book), B8 (book), B9 |
| `parity-notes-readmes` | `scripts/check_parity.py` | B8 (parity), B10 |
| `hook-hash-lines` | `scripts/check_disclosure.py` | B3 |
| `em-dash-every-text` | `scripts/check_em_dash.py` | B5 |
| `links-url-bounds` | `scripts/check_links.py` | B6 |
| `entry-apostrophes` | `scripts/patterns.py` | B11 |
| `epub-chapter-links` | `pandoc/epub.css` | B4 |
| `venv-failed-install` | `Makefile` | B12 |
| `od4-kit-pointer` | docs/00 | D4 |
| `docs01-retired-projects` | docs/01, `AGENTS.md` | D2, D8 |
| `docs03-current-rows` | docs/03 | D1, D6, D7 (docs/03) |
| `docs04-gain-number` | docs/04 | L5, D7 (docs/04) |
| `docs05-no-exercises` | docs/05 | D3 |
| `docs06-legend` | docs/06 | D5 |
| `ch03-restated-rule` | chapter 3 | L6, L7 |
| `ch09-key-points` | chapter 9 | L3, L4 |
| `ch16-resume-apply` | chapter 16 | L1 |
| `ch17-slot-none` | chapter 17 | L2 |
| `ch26-what-counts` | chapter 26 | L9, L10 |

**Proof.** `make book` built both PDFs and EPUBs at the start; `make verify` green at the end. No file under `book/` changed.

**Decisions.** M15's lines wait only on `m14-review` (`· after m14-review`), so they are free once this line is `[x]`, while M14's findings are still open; that section is another delivery's uncommitted work and this delivery leaves it as it is.

```commit
docs(m14-review): review M14 clause by clause; 21 findings

- C1 to C7 hold in both editions and in the repository
- the code review read the build, the documents and the chapters
- 21 findings, one line per file, under m14-review in docs/06
- the review ran as agents at the author's request, not ultra

work/done/m14-review.md
```
