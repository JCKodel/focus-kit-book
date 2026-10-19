# m19-review

**Objective.** The author can decide whether each promise of M19 holds in both editions and the installed process, with every confirmed failure recorded as a new finding in M19.

**Behaviour.**

* With every prerequisite completed, the author receives current PDFs and the clause checks below, with their starting pages in both editions; each answer is recorded as holds or fails with the observed fault.
* The review compares installed commands and active project documents with the kit version specified by the installation page, then checks the book's explanations against those rules.
* On the author's word, read-only area readers inspect one fixed commit range; a checker tests each candidate against that same snapshot and labels it seen, latent or weak before the author decides which become findings.
* A missing clause answer, unavailable required reviewer or incomplete path coverage leaves this review waiting with `resume: apply` and its actual reason; a passing partial reading never closes it.
* A new commit during reading does not move the fixed endpoint; later changes are identified as outside that reading. Confirmed findings become `[ ]` lines below this review in M19, with no fixes made here.

**Contract.** Clause checks from docs/06's M19 paragraph, each performed against the named delivery's completed page and the cited chapter passages in both PDFs:

| Promise | Deliveries and passages | Author's check |
|---|---|---|
| Installed kit and matching process | `kit-2026-10-18-1`, `ch08-update-2026-10-18-1`; installed files, docs/04 and docs/05, chapter 8 update example | Do the installed version and recorded migration report agree with the active rules and real example? |
| Fast verify and named slow tests | `ch05-13-slow-tests`; chapters 5, 7, 13 and 15 | Can the reader locate each suite and explain when it runs and how a slow failure is recorded? |
| Milestone placement | `ch11-next-milestone`; chapters 11, 14 and 15 | Where does unrelated work go, and where does a review's finding stay? |
| Proposal sessions and use before commit | `propose-same-session`, `apply-use-first`; affected passages in chapters 8 to 13, 17 to 19, 22 and 23 | Can a reader choose either proposal session, start apply fresh, use the result and request corrections before committing? |
| Git authority and isolation | `agent-commits-asked`, `ch19-commit-by-index`, `ch18-kit-branches`, `ch18-revert-scope`, `ch19-batch-staging`, `ch10-explicit-staging`; chapters 6, 7, 10, 13, 18, 19 and 23 | Is explicit authority distinct from autonomous action, does the index contain one delivery, and are external effects distinguished from git undo? |
| Queue and review lifecycle | `ch11-14-defined-mark`, `ch14-back-to-open`, `ch13-refuse-incomplete`, `ch14-ended-and-dropped`, `ch13-review-base`, `ch15-review-head`; chapters 11, 13 to 15 and 23 | Given draft, interrupted, blocked, cancelled and staged cases, can the reader select the mark, resumption and exact review input? |
| Remaining comparison corrections | `ch21-done-when`, `ch17-context-read`, `ch08-10-fresh-start`, `ch06-23-kit-rules`, `ch08-hosts-details`, `ch09-empty-repo`, `ch02-93-moment`, `ch07-ninjobs-focus`; their bounded Contract passages | Does each Behaviour scenario in these completed pages hold when read alongside the other chapters, including the two phases of Ninjobs and distinct count moments? |

Base: `1ac62f67b2f5462d7b49c53e395cb3a6b71156ef`, the commit of m18-review.
At apply start, after prerequisites are available, record the exact HEAD as endpoint and inventory `git diff --name-only <base>..<endpoint>` and its stat before launching readers.
Partition every changed path among build, chapters, kit skills and documents, assigning delivery records to documents; record every exclusion with its reason instead of silently omitting paths.
Split large areas into manageable path groups; use docs/05's Opus readers and checker, at most two concurrently, with no substitute model.
Run any slow tests actually named by the Verify slot; none is invented for the review.
Only this page, its final archive move, and its own queue mark/findings change; no schema, API or book content change.

**States.** Inapplicable: review, no screen.

**Visual reference.** Existing English and Portuguese PDFs, chapter sections above; apply records current PDF page numbers.

**Out of scope.** Fixing findings, re-reviewing previous milestone clauses, changing review models, or assuming the author waived PDF reading or authorized readers merely by approving this definition.

**Decision.** The author authorized early definition before prerequisites complete; their `after` gate remains.
The endpoint and concrete path inventory are execution inputs fixed before reading, not unsettled review scope (docs/05 §8 and `ch15-review-head`).

**Done when.**

* [x] Every clause has the author's answer, and every named prerequisite is completed and available.
* [x] Base, endpoint, area inventory, slow-suite outcomes, reader coverage and checked candidates are recorded; required approvals are recorded.
* [x] Every confirmed failure is a separate queue finding in M19; no fix is silently made.
* [x] `make verify` is green after final edits, both PDFs were built for the author's reading, and this review alone is staged and archived with its suggested commit message.


## Execution

**Range.** Base `1ac62f67b2f5462d7b49c53e395cb3a6b71156ef` (m18-review), endpoint `5dbd674f8dbe3d08e10df860664697167f0d1e2d`, frozen at the start of the reading after `ch13-scope-question-term` committed; nothing was committed during the reading. `git diff --stat`: 129 files, 4860 insertions, 937 deletions. The range also holds M20's deliveries, so M20's code reading is this one (m20-review's base is this review's commit).
Paths outside the batch's commits (VERSION, scripts/release.py, scripts/build_book.py, mkdocs.yml, docs/manuals/release-the-book.md, work/kit-proposals.md, copyright-version) came from `d114df1`, the author's commit that planned M19.

**Areas and coverage.** Six read-only Opus readers, two at a time, then one Opus checker: chapters 00-08, chapters 09-16, chapters 17-24 (both editions), the build (Makefile, scripts, .github, mkdocs.yml, VERSION, READMEs), documents and kit skills (docs, AGENTS.md, .claude, .agents; skills compared byte for byte with SETUP.md §3 of 2026.10.18.1, all equal), delivery records (work, docs/06). Every path was read; two binary screenshots in work/done were not, being no record. **Slow tests:** the Verify slot names none.

**PDFs.** `make book` at the endpoint, 2026-10-18 23:26: `output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`. Chapter start pages (en / pt), make book 2026-10-18 23:26 at 5dbd674:
1 11/11 · 2 19/19 · 3 24/24 · 4 40/41 · 5 54/56 · 6 63/65 · 7 68/70 · 8 78/80 · 9 88/90 · 10 96/99
11 103/106 · 12 113/117 · 13 121/127 · 14 136/143 · 15 146/154 · 16 154/163 · 17 161/170 · 18 168/178
19 178/189 · 20 195/207 · 21 200/212 · 22 205/218 · 23 211/225 · 24 217/231

**Checked candidates** (seen 34, 12 of them low; latent 3; weak 3), waiting for the author's confirmation:

| id | label | file:line | claim (one line) | proposed slug and line text |
|---|---|---|---|---|
| A1 | seen | book/en/08-install-and-hosts.md:30 (pt :30) | "commit it yourself, as with every change the agent makes" says the person always commits; ch06:64, ch07:70 and ch08's own item 3 (:84) let the agent commit when asked. agent-commits-asked's Contract left ch08 out. | M19. `ch08-commit-asked  chapter 8: after the install you commit what it wrote, or ask the agent to, as with every change (chapter 13); both editions` |
| A2 | seen (low) | book/en/08-install-and-hosts.md:118, :126 (pt :120, :128) | Antigravity's reading of `AGENTS.md` has no vendor note while Claude Code, Codex, Copilot and Devin have one and :140 says each row has its vendor page; SETUP.md §1 (:123-125) names the Antigravity pages. | M19. `ch08-antigravity-source  chapter 8: Antigravity's reading of AGENTS.md and its always-on rule cite the vendor pages the setup file names; both editions` |
| A3 | weak | book/en/08-install-and-hosts.md:137 vs book/en/09-starting-a-project.md:62 | Weak: ch09:62 is the session after /brainstorm, which asked for no change; propose-same-session's Divergences keep it fresh on purpose, and ch08:137 says "may". | drop |
| A4 | seen | book/pt/08-install-and-hosts.md:68, :85 | "uma entrega bloqueada" for the blocked work that ch13 (pt) now calls "travado"; ch13-scope-question-term Decision (2) left a book-wide word to a new line. | M19. `pt-blocked-term  the Portuguese edition says "travado" for a blocked line, delivery or /apply in chapters 8 and 17, as chapters 13, 14, 17 and 19 do, and docs/03 gives the word; the English already matches` |
| A5 | seen (low) | book/pt/08-install-and-hosts.md:75 | "quando pedido, dá o passo que a pessoa cita" vs pt06:64 and pt07:71 "quando pedem, ele dá o passo que a pessoa nomeia"; same rule, two wordings. | M19, fold into A1: `... and its report says the agent's rule in the words of chapters 6 and 7` |
| A6 | seen (low) | book/pt/08-install-and-hosts.md:143 | "da §1" treats § as feminine; every other pt passage uses "o §" / "no §". | M19, fold into A1 or A4 (one word, pt only) |
| B1 | seen | book/en/13-apply.md:130 (pt :130) | `suspension-end`, which the page "never asked for" and no clause of milestone 1's paragraph (ch11:44-46) needs, is placed below `return-book`, inside milestone 1; ch11:78, :106 and ch14:74 send it under the next milestone. ch11-next-milestone never reached ch13. | M19. `ch13-next-milestone  chapter 13: a line the page did not ask for, suspension-end and the one asked after using the delivery, goes in the milestone whose paragraph needs it or under the next, as chapter 11 says; both editions` |
| B2 | seen | book/en/13-apply.md:174 (pt :174) | "ask for it right below this delivery's line, so it is the next free line" places a line by recency, which ch11:106 and ch14:74 forbid. Text predates the range (try-before-commit); the contradiction came with ch11-next-milestone. | see B1 |
| B3 | latent | book/en/15-closing-a-milestone.md:22-24, :59; docs/05-Process.md:341-346 | A commit made after `<review-head>` and before the review's own commit falls in neither range. Nothing committed after 5dbd674 today. The rule is the kit's text (SETUP.md:887-890), which the chapter teaches as it is. | kit note (a chapter line would teach a rule the kit does not hold) |
| B4 | seen | book/en/16-the-governor.md:28-29 (pt :28-29) | ch16 says all 29 checks left and two others "took their place"; ch06:43 says two of the 29 stayed. The two chapters tell Ninjobs' restart differently. | M19. `ch16-two-checks-stayed  chapter 16: at Ninjobs' restart two of the 29 checks stayed, both guarding privacy, as chapter 6 says, not two new ones in their place; both editions` |
| B5 | seen | book/en/11-queue-and-milestones.md:164 (pt :169) | The due-date-format walk-through reviews the diff and commits with no use of the delivery first; apply's next steps, docs/05 §2, ch10 and ch13 put use first. apply-use-first and ch15-20-use-first left ch11 out. | M19. `ch11-use-first  chapter 11: the due-date-format example uses the delivery before reviewing its diff and committing, as chapter 13 says; both editions` |
| B6 | seen (low) | book/en/14-queue-states.md:35-47 (pt :35-48) | ch14's "first milestone" holds search-catalog, reservations, my-loans, due-reminder, which ch11's milestone 1 paragraph does not need, beside ch14:74's placement rule; ch15 gives a third paragraph. ch11-next-milestone saw it and left it (Decisions). | M19, author's call. `ch14-example-milestone  chapter 14: the example milestone shows the paragraph its lines answer, or is not called the lending library's first; both editions` |
| B7 | seen | book/en/09-starting-a-project.md:22 (pt :22) | The process slots /brainstorm asks for omit the slow tests kept out of verify; brainstorm/SKILL.md:32 names them, ch13 and ch15 rely on the slot. | M19. `ch09-slow-tests  chapter 9: /brainstorm asks for the slow tests kept out of verify and /analyze infers which tests are slow, as the kit's commands say; both editions` |
| B8 | seen | book/en/09-starting-a-project.md:73 (pt :73) | What /analyze infers omits "which tests are slow"; analyze/SKILL.md:25 infers it. | see B7 |
| B9 | seen (low) | book/pt/14-queue-states.md:90, :99, :161; book/pt/20-team-tools.md:42 | `corrigir-devolucao` names the due-date fix (en `fix-due-date`) but reads as "fix the return", beside `devolver-livro` and `corrigir-devolucao-atrasada`. | M19. `pt-due-date-slugs  the Portuguese edition names the due-date fix corrigir-data-de-devolucao in chapters 14 and 20, so it is not read as a fix of the return` (the longer slug must fit chapter 20's fenced queue block and verify's width check) |
| B10 | seen (low) | book/pt/11-queue-and-milestones.md:48 | "inscrição suspensa" where the same library's refusal says "matrícula" (pt03:280, pt12:61, :111). | M19, fold into B9 (one word, pt only) |
| C1 | seen | book/en/19-worktrees.md:317 (pt :317) | "Across worktrees it always conflicts at the merge" contradicts :204 and :207 (far-apart lines merge; neighbours meet) and docs/03's conflict row. | M19. `ch19-queue-conflict  chapter 19: across worktrees the queue conflicts at the merge when the two deliveries' lines are neighbours, as the chapter's conflict section says; both editions` |
| C2 | seen (low) | book/en/24-asking-for-more.md:63 (pt :63) | "Inside a delivery ... anything else becomes a line" is unqualified, while :36 and the key point :163 put what turn 4 finds during /propose into the page. | M20 (ch24-protocol-phase's promise). `ch24-turn4-phase  chapter 24: turn 4's rule says it holds after /apply's first result, as the phase paragraph says; both editions` |
| C3 | seen (low) | book/en/24-asking-for-more.md:138 (pt :138) | "chapter 22 shows how to turn tokens into a price": ch22 gives the multipliers (:24) and says a vendor's list gives the price (:103), not a conversion. Predates the range. | M19. `ch24-price-pointer  chapter 24: per-token billing points to chapter 22 for the four kinds of token and their multipliers, which a vendor's price list turns into a price; both editions` |
| C4 | seen | book/en/21-beyond-software.md:69 (pt :69) | "one page per chapter in work/" is false (one per delivery, several per chapter), and verify's list leaves out build, width, links and, since verify-examples, the examples (docs/01:68). | M19. `ch21-book-on-kit  chapter 21: this book runs on the kit with one page per delivery and a make verify that also runs chapter 3's examples, as docs/01 says; both editions` |
| C5 | seen | book/pt/17-project-as-assistant.md:96 | "qual linha da fila está bloqueada" against the same chapter's "travado são as linhas [?]" (:25) and "O que está travado" (:70). | see A4 |
| C6 | weak | book/pt/17-project-as-assistant.md:127-128 | Weak: `formato-devolucao` is the Portuguese name chapter 11 gives due-date-format throughout (pt11:107-172); the two editions name the same delivery. Its ambiguity is B9's. | drop (author may fold into B9) |
| C7 | seen (low) | book/pt/22-cost-and-where.md:24 | "um décimo disso" reads as a tenth of the cache write just named; en :24 says a tenth of an input token. | M19. `pt22-cache-read  chapter 22 in Portuguese: a cache read costs a tenth of an input token or less, as the English says` |
| C8 | seen (low) | book/en/18-git-essentials.md:156 | "Either step undoes ... and run nothing backwards": verb agreement ("runs"); pt correct. | M19. `ch18-runs  chapter 18 in English: either step "runs" nothing backwards; the Portuguese already agrees` |
| C9 | weak | book/en/23-adoption.md:73-74 | Weak: step 1 points to chapter 8, whose install ends by naming a fresh session for /analyze (ch08:32), and :79 points to chapter 10. | drop |
| D1 | seen | README.md:25 | `make release` described as before copyright-version: no VERSION written and checked, no book build (pandoc, weasyprint, pypdf), no release commit; contradicts manual :6-27 and docs/01:71. release.py:2's docstring opening says the same. | M19. `readme-release  the READMEs say make release checks and writes VERSION, builds the book, commits VERSION and pushes main and the tag, as the release manual says; both editions` |
| D2 | seen | README.pt.md:25 | Same stale text in Portuguese. | see D1 |
| D3 | seen (low) | scripts/release.py:8; docs/01-Architecture.md:71; docs/manuals/release-the-book.md:30 | "Any refusal after writing VERSION restores it" and "nothing committed or pushed" / "pushes nothing" are false when tagging or the tag push fails (release.py:97-98, after the try), which manual:56 describes. | M19. `release-refusal-scope  release.py, docs/01 and the release manual say a failed tag push leaves main pushed and the tag local, as the manual's recovery says; docs/01:47 says when VERSION is set back by hand` |
| E1 | seen | docs/adr/ADR-0010-trunk.md:12, :20 | Only the author commits, with no amendment; AGENTS.md:22 and docs/05 §§5, 6 let the agent commit or merge when asked and make release commit VERSION. | M19. `adr0010-commit-asked  ADR-0010 gains an amendment: the agent commits or merges when the person asks, and make release commits VERSION, as docs/05 §§5 and 6 say` |
| E2 | seen | docs/05-Process.md:311-315 | Blocked on trunk: "move this partial delivery to its own branch/worktree" against ADR-0010:21 (no worktree), the trunk Git slot and apply/SKILL.md:30; the kit's template §6 (documents.md:409-413) no longer has it. | M19. `docs05-blocked-trunk  docs/05 §6: a blocked delivery on trunk stays uncommitted and its prerequisite becomes a line above it, as the kit's template says, with no move to a branch or worktree` |
| E3 | latent | docs/05-Process.md:97-98; docs/06-Queue.md:6; docs/03-Domain.md:111-112 | "free when every line it names is [x]" also frees a line whose after names a dropped [x], which :145 gives to the person. No dropped line exists in the queue today. Same wording in SETUP.md:719, :762. | M19. `free-line-dropped  docs/06's legend and docs/03's dependency and free line rows say a line whose after names a dropped line waits for the person, as docs/05 §4 says`; plus kit note for SETUP.md and the skills' "whose after is done" |
| E4 | seen | docs/06-Queue.md:487-488 | ch13-scope-question-term (queued from ch12-defined-mark's review, edff53f) answers no clause of M19's paragraph, so §4 sent it to M20; it was also put in m19-review's after. ch16-six-rules-timeline (:484): weak, it corrects a passage against SETUP.md. | no line: both lines are `[x]` and a line never leaves; a note for the author on how a fix found in another delivery's review is placed |
| E5 | seen | docs/06-Queue.md:493, :505 | M20's paragraph promises "make verify runs the chapters' examples"; the delivery runs chapter 3's only (docs/04:173, docs/01:32 "no other chapter's examples are run", README:22; the reader's cites docs/04:179 and docs/01:47 are off). | M20 (its own clause; m20-review answers it), two remedies for the author: `m20-examples-clause  M20's paragraph says make verify runs chapter 3's examples, which is what verify-examples built`, or `verify-more-examples  make verify runs the executable examples of the chapters after chapter 3, as M20's paragraph promises` |
| E6 | seen | .claude/skills/brainstorm/references/documents.md:124 (and the three other copies) | "FOCUS whole ... Ninjobs chose this" has no phase, against ADR-0016:46. The copies are byte-equal to SETUP.md:575; the kit's README:198 says "Ninjobs took it whole". | kit note (SETUP.md §3.5 and both READMEs; the installed copies follow the next kit version) |
| E7 | seen | docs/03-Domain.md:108-109 | No Portuguese word for a blocked line or /apply, while the pt chapters use "travado"; docs/03:5 says a concept enters there first. | see A4 |
| E8 | seen (low) | docs/01-Architecture.md:47 | "only make release changes it" vs manual:17, :55 (set VERSION back by hand) and a revert. | see D3 |
| F1 | seen | work/kit-proposals.md:15 | Item 9 "Ninjobs took FOCUS whole ... the kit had it under the two principles" is superseded by ch07-ninjobs-focus (whole FOCUS before the restart, two principles after); the pending kit correction lives only in that page's Decisions. | M19. `kit-proposals-ninjobs-phases  work/kit-proposals.md's item 9 says Ninjobs required FOCUS whole until its restart and kept the two principles after, and names SETUP.md §3.5 and the kit's READMEs`; plus E6's kit note |
| F2 | seen | work/m20-review.md, Done when; work/m19-review.md:48 | m20-review only: it asks for no approval; m19-review's Done when 2 already asks "required approvals are recorded", without naming which. | M19: m19-review's /apply records the OD-3 answers (F3); m20-review is M20's: `m20-review-approvals  m20-review records the author's OD-3 answer for ch16-prevention-evidence's Case A paragraph` |
| F3 | seen | work/done/ch21-done-when.md:25 vs :29; work/done/ch14-ended-and-dropped.md:25 vs :31; work/done/ch16-prevention-evidence.md:25 vs :35; work/done/ch07-ninjobs-focus.md:34 vs :48 | OD-3 approval ticked `[x]` while the body says it was only asked: ch21 (Case B passage), ch14/ch23 (Case A), ch16 (Case A, M20); ch07 is a Ninjobs wording review, not OD-3. | M19: no line; m19-review lists the three OD-3 passages and records the author's answer before closing (its Done when 2); a refusal is a finding |
| F4 | latent | 41 work/done pages' `make book` Done when (e.g. ch02-93-moment.md:29 vs :40) | `make book` ticked while the Proof defers it to a batch driver; no commit records the result. The review's own PDF build covers it today. | no line; m19-review's PDF build is the evidence |

**Author's answers (2026-10-19).** Clauses: every clause taken as holding, without reading the PDFs, as in m17-review. OD-3: approved, the four passages committed under the batch: chapter 21's Case B sentence (ch21-done-when), chapter 23's and 14's Case A passage on the cancelled request (ch14-ended-and-dropped), chapter 16's Case A paragraph (ch16-prevention-evidence) and the Ninjobs two-phase wording in chapters 4, 6, 7 and ADR-0016 (ch07-ninjobs-focus). E5: the remedy is M20's paragraph saying chapter 3's examples. Candidates: the author reads the table before confirming.

**Findings (2026-10-19).** The author confirmed seven of the checked candidates; every other candidate is rejected, and the kit notes (B3, E3's kit part, E6) go to the author outside this repository. Each finding is a `[ ]` line below this review in M19, with no fix made here; on the author's word their round runs /propose and /apply with no further review:

* B4: `ch16-two-checks-stayed`
* B1, B2: `ch13-next-milestone`
* E2: `docs05-blocked-trunk`
* E1: `adr0010-commit-asked`
* D1, D2: `readme-release`
* A4, C5, E7: `pt-blocked-term`
* F1: `kit-proposals-ninjobs-phases`

**Verify.** `make verify` green after the last edit of this page.

```commit
docs(m19-review): review M19 and M20's code, seven findings

- one range, six Opus readers and a checker; 40 candidates checked
- the author took the clauses as holding and approved the four OD-3 passages
- seven findings queued in M19; the rest rejected, kit notes to the author

work/done/m19-review.md
```
