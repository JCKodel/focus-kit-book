# m32-review

**Objective.** The author can decide whether M32's promise holds, having read in the PDF of both editions the passages of chapters 8, 11 to 14 and 19 that teach focus-kit 2026.10.24's queue tree, and having run that tree on this repository, and whether everything changed since m31-review's commit holds under the code reading by areas, with every confirmed failure recorded as a new line under this review.

**Behaviour.**

* Precondition, the deliveries committed: when this page was written, `kit-2026-10-24` was committed (`914fc75`) and the other three M32 deliveries, `ch08-update-2026-10-24`, `ch11-14-queue-tree` and `ch19-queue-branches`, were `[x]` and staged but not committed, their changes in the index. The range must hold them, so they are committed, each as its own change (docs/05 §6), before this review's /apply starts. /apply checks it: `git log --diff-filter=A --format='%h %s' -- work/done/<slug>.md` returns one commit for each of the four records; if one returns nothing, /apply stops and asks the author to commit that delivery before the reading, and never commits it itself (docs/05 §5, Git; §6); if one returns more than one, /apply stops and reports instead of choosing.
* With every line in this review's `after` `[x]` and committed and, by its `(--)` token, every line above it `[x]`, /apply records the base and the end commit, builds both PDFs at the end commit and gives the author the clause tests below, each with its files and lines at the end commit and the PDF page of each passage in both editions; the author opens them and answers each test: holds, or fails with what the author saw. A clause no delivery answers, or one that fails in the author's hands, is a finding (docs/05 §8).
* The repository tests are taken on this repository at the end commit: the author runs `git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq trunk` in its folder and reads the tree it prints; at that moment this review's line is `[*]`, so the tree is M32's, the first milestone with a line not `[x]`, with `m32-review` in flight and no `[x]` line and no M33 line drawn.
* On the author's word in the review's /apply session, read-only area readers read one fixed range, `git diff <base>..<end>`, between the base and the end commit below; one checker tests each candidate against that same snapshot and labels it seen, latent or weak before the author sees it (docs/05 §5, Milestone review; §8). The session says it is time and starts the readers only on that word.
* No word of the author for this review is quoted on this page: the command that opened this definition, `/propose m32-review kit-2026-10-25 ch11-14-after ch19-claim-integration ch17-20-branch-on-origin ch09-design-slot ch08-update-2026-10-25`, is the word for /propose, not for the reading or the tests. If the author, in the /apply session or relayed to it, gives the word that the review's session take the tests and the confirmation, /apply quotes that word on this page, answers each test from its own reading of the passages in both PDFs and of the repository at the end commit, records the answers as the review's, never the author's, and takes the word as the author's confirmation of each candidate the checker marks seen, the latent and weak ones listed as dropped (docs/05 §8, the paragraph on the person's word). Without that word, the author decides which candidates become findings.
* The readers and the checker report back to the review's own session, the one running /apply: the session launches each as a foreground Agent call and receives its final report itself. A checker's marks that reach the session only through a working file or another session's summary are not its report; the session asks the checker again, or the line waits as below. Working files go under the session's scratchpad directory, in its `m32/` folder, and the candidate table in `m32-candidates.md` beside it, then onto this page.
* Each confirmed candidate becomes a `[ ]` line under this review in docs/06, in M32, candidates sharing a file or a cause sharing a line; every candidate not confirmed is listed on this page with its mark. No fix is made here.
* A clause with no answer, a required reader that cannot run, a checker whose report does not reach the session, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8); a partial reading that found nothing never closes it.
* A commit made during the reading does not move the end commit; what it changed is named as outside this reading.
* Edge, a candidate M33 already answers: M33's lines, queued after this review, already change some of what M32's chapters say, such as "from that slug's branch, local or remote" (chapter 12 :29, chapter 14, chapter 19), which `kit-2026-10-25`, `ch11-14-after`, `ch17-20-branch-on-origin` and `ch08-update-2026-10-25` replace with each slug's line read from its branch on origin. Such a candidate is listed on this page with its mark and the M33 line that answers it; it becomes a line here only where that M33 line's sentence does not hold it, the author deciding (The author's answers).
* Edge, the kit's later version: the sibling checkout `~/Projects/focus-kit` may hold 2026.10.25 by the time /apply runs. The kit comparison reads nothing later than `51ff062`, the commit `kit-2026-10-24`'s Contract names, with `git show 51ff062:<path>`.
* Edge, the trees are real output: chapters 11 to 14 and 19 print trees their pages say the installed `queue.sh` produced on scratch repositories. /apply reruns the script at the end commit on scratch repositories shaped as `ch11-14-queue-tree`'s and `ch19-queue-branches`' Contracts describe, outside this repository, and compares the output byte for byte with each chapter's block in both editions; a difference is a candidate for the checker.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree or the index. While this page was written another session's unstaged hunk of docs/06 added M33's heading, paragraph and seven lines; it is that session's work, not this delivery's (docs/05 §4). If it is committed before the end commit, it is in the range and read as part of docs/06 under no clause; if after, it is outside.

**Contract.** Clause tests from docs/06's M32 paragraph, each against its delivery's page in `work/done/` and the named passages. Lines are en / pt in the staged tree when this page was written (HEAD `914fc75` with the three deliveries' changes staged); where one number is given it is the same in both; /apply records them again at the end commit.

| Clause | Deliveries and passages | The author's test |
|---|---|---|
| The book teaches focus-kit 2026.10.24 | `ch08-update-2026-10-24`: chapter 8, "Install" / "Instalação" (:22, :24), the refusal sentence in "What the install never touches, and how to update" (:51), "What an update reports" (:61 to :90 / :61 to :92), "How each host finds the commands" (:151 / :153); `ch19-queue-branches`: chapter 19, "Worktrees in the kit" (:195 to :225), Key points (:412) | In chapter 8 of each PDF: do the kit's files hold the four commands with two small scripts the commands run through git, and do those scripts go through Git for Windows' shell? Does the refusal sentence name `.claude/skills/apply/SKILL.md` and focus-kit 2026.10.24, on a copy outside the repository? Does the report excerpt say focus-kit 2026.10.24 was installed and hold one pending migration, docs/05 §4 on what may run now with the template's two sentences quoted, beside the section numbers that match and the Git slot as a recorded choice, each item reported and none applied, with no count of files, no SETUP section number and no 2026.10.20.5 left? Does `/apply` name what may run next, the queue tree? In chapter 19 of each PDF: with a worktree per delivery, does the script read each delivery's line from its branch on origin, keep the mark furthest along, list the lines only a branch has, and say what it cannot see, a branch whose first mark is not pushed? Does each edition say the same? |
| And the repository runs on it | `kit-2026-10-24`: the eight installed `SKILL.md` (`version: "2026.10.24"`), both `propose/scripts/queue.sh`, docs/05 §4 (:110 to :115, :174 to :178), docs/03's `queue tree` row (:119), ADR-0018's `kit-2026-10-24` amendment (:88) | Do the eight `SKILL.md` under `.claude/skills/` and `.agents/skills/` say `2026.10.24`? Does docs/05 §4 say what may run now is answered by running `queue.sh` and showing its tree, the free lines offered as one command? Does the command in the row above print a tree, as the next clause tests? |
| What may run now comes from the kit's `queue.sh`, a tree of the current milestone with each line under the last line it waits on and its state | `ch11-14-queue-tree`: chapter 14, "What may run now" (:122 to :148 / :123 to :150), its key point (:246 / :248); chapter 11, "Size and order" (:89 / :92); `ch19-queue-branches`: chapter 19's tree (:195 to :225); `kit-2026-10-24`: docs/05 §4 | In each PDF: does chapter 14 say the agent runs the kit's queue script in one line, with the claim's strategy word, and that it edits nothing? Does its tree draw chapter 11's milestone with `return-book` and `my-loans` under `lend-book`, each with its state, no `[x]` line, and does the text say where a line with two pending `after` lines sits? Does chapter 11 say the script draws `return-book` under `lend-book` while `lend-book` is not `[x]`? On this repository, does the command print M32's tree with each line's state? |
| Ending with the lines free for /apply and for /propose together | `ch11-14-queue-tree`: chapter 14's tree and the sentences after it (:139 to :146 / :140 to :148); `ch19-queue-branches`: chapter 19's tree | In each PDF: does chapter 14's tree end with the lines free for `/apply` and for `/propose` together and the lines without a token listed to judge first, and does the text judge `search-catalog` and `m1-review` by the files each touches? Does the text say the four lines with tokens end with `free for /propose, together: search-catalog renew-loan`? Does chapter 19's tree end with `free for /apply, together: overdue-list`? |
| /propose and /apply typed with no slug show it | `ch11-14-queue-tree`: chapter 12, "What `/propose` does" (:25); chapter 13, "What `/apply` does" (:22); chapter 14 (:147 / :149); `kit-2026-10-24`: propose's and apply's `SKILL.md` | In each PDF: do chapters 12, 13 and 14 say `/propose` and `/apply` typed with no slug show the queue tree and ask which line to take? On this repository, does `/propose` typed with no slug in a session show the tree and ask (the author stops it there)? |
| /apply ends with it | `ch11-14-queue-tree`: chapter 13, "Green is not done" (:120), "`lend-book`, built", next step 4 (:169); chapter 14 (:147 / :149); `ch08-update-2026-10-24`: chapter 8 (:151 / :153); `kit-2026-10-24`: apply's `SKILL.md`, last paragraph | In each PDF: does chapter 13 say `/apply`'s last next step is what may run next, the queue tree, and does `lend-book`'s step 4 give `return-book` and `m1-review` as free for `/propose`, judge the review to wait and give `/propose return-book`? Does this review's own /apply end with the tree? |
| The free lines are offered as one command with several slugs, each slug one more agent at the cost of a session | `ch11-14-queue-tree`: chapter 12, "Several lines in one command" (:156 to :157 / :165 to :166); chapter 14 (:146 / :148), its key point; `kit-2026-10-24`: docs/05 §4 (:114 to :115) | In each PDF: does chapter 12 say each slug is one more agent costing as much as one session, and that asked what may run now, or typed with no slug, the agent offers the free lines as one such command? Does chapter 14 give `/propose search-catalog renew-loan` with that cost said? |

The queue lines' promises beyond M32's paragraph: chapter 19's reading off trunk (`ch19-queue-branches`) is tested under the first clause, as the passage that teaches it; chapter 8's sixteen files and §3.7 (`ch08-update-2026-10-24`) are, by that page's Behaviour, deliberately not stated in the chapter, and the first clause's test checks they are absent.

**Base.** `99d04a5` (`docs(m31-review): review M31, two findings`), the commit of m31-review, the previous milestone's review (docs/05 §8, docs/03's `milestone review` row), the one commit `git log --diff-filter=A --format='%h %s' -- work/done/m31-review.md` returns. The range therefore holds M31's fix round, `28cae3f` (`ch22-cache-route-host`) and `024a4a0` (`m31-records-claims`), which gets no second review and is read by the area readers without a clause (docs/05 §8); the release `920d3fc` (`chore(release): v1.2.8`), `VERSION` alone, read with no clause, as m30-review read `18cdae4`; M32's queue `a20faef`; `kit-2026-10-24`'s `914fc75`; and the three deliveries' commits, once made.

**End.** The commit HEAD is when the reading starts; /apply records it before launching any reader, and nothing it records later moves it. If this page or its `[>]` is committed before then, it is inside the range; if not, the readers read `work/m32-review.md` from the working tree beside the range, as the spec.

**Areas.** Planned: /apply runs `git diff --stat -M <base>..<end>` at its end commit, records every path and places each in an area of docs/05 §5's Milestone review slot. Expected, from the commits above:

* **Build:** `VERSION` (`920d3fc`); any other path of the `Makefile`, `scripts/`, the READMEs or `docs/manuals/` the range holds; none is expected.
* **Chapters:** `book/{en,pt}/22-cost-and-where.md` (`ch22-cache-route-host`); `book/{en,pt}/` chapters 8, 11, 12, 13, 14 and 19 (the three deliveries), read whole at the end commit.
* **The kit's skills:** the fourteen paths of `914fc75` under `.claude/skills/` and `.agents/skills/`, `queue.sh` among them, read against docs/05 §4 and `kit-2026-10-24`'s record; their byte comparison with the kit is a mechanical check below, not a reader's work.
* **The documents:** `docs/03-Domain.md`, `docs/05-Process.md`, `docs/06-Queue.md`, `docs/adr/ADR-0018-six-marks.md`, `work/kit-proposals.md` (its entry 14 is `ch19-queue-branches`', by that page's Contract), the records under `work/done/` of M31's fix round, the three it edited and M32's four, and `ch11-14-queue-tree`'s six screenshots, viewed.

**Readers.** Read-only readers on Opus, each keeping the session's advisor, Fable, then one read-only checker on Opus; each launch sets its model to Opus, no other model runs the review, and no agent runs on Fable itself (docs/05 §5, Milestone review). At most two of the review's agents run at a time. Planned by what the range holds at the end commit:

* pair 1: **chapters 8 and 11 to 14** (10 files), whole and by their range diffs, against their pages, the installed `queue.sh`, docs/05 §4 and SETUP.md and the changelog at the kit's `51ff062`; and **the kit's skills and the documents**, the fourteen skill paths, docs/03, docs/05, docs/06, ADR-0018, `work/kit-proposals.md` and `kit-2026-10-24`'s record, with this page;
* then **chapters 19 and 22 and the other records** (4 files), against `ch19-queue-branches`', `ch22-cache-route-host`'s and `m31-records-claims`' pages, the records those three edited, the other M32 records and the six screenshots; it runs alone, after the pair;
* an area too large for one careful reading splits again (docs/05 §8). The checker runs alone once the readers have reported, on every candidate in one report, as m29-review's /apply found best.

Each reader lists the paths it read, and the page records whether each kept the session's advisor, as each agent's own report says it.

**Slow tests.** The Verify slot names none (docs/05 §5); none is invented for this review.

**Known candidates.** None planned for the checker. One lead is /apply's own, before any reader: L1, the Precondition, whether each of the four records was committed, by `git log --diff-filter=A`; a gap stops the review as Behaviour says.

**Mechanical checks**, run by /apply at the end commit:

* `git -C ~/Projects/focus-kit show 51ff062:SETUP.md` has SHA-256 `90877174c1d6e18383f2f3d8ce42f367499cb166f89c6c932d9aa8366a07abec`, `kit-2026-10-24`'s; every one of SETUP §3's thirty-four destinations is byte-equal to its section at `51ff062`, and all eight installed `SKILL.md` carry `version: "2026.10.24"`.
* The trees rerun: the installed `queue.sh` on scratch repositories outside this one, shaped as `ch11-14-queue-tree`'s and `ch19-queue-branches`' Contracts say, in both editions, its output compared byte for byte with the chapters' blocks (Behaviour).
* The repository tree: `git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq trunk` in this repository prints M32's tree, and `git status` is the same before and after.
* `git status --short book/` is empty before `make book`, so the PDFs hold the end commit's `book/`; both PDFs contain the trees of chapters 14 and 19 and chapter 8's report excerpt, and /apply records each chapter's start page and the page of each passage in both editions.
* `git branch --list` shows `main` alone (trunk).
* `make verify` and `make book` are rerun by /apply after its last edit; their results here are /apply's, not this page's. A failure caused by another session's uncommitted file is named as that session's.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit; `ch11-14-queue-tree`'s six screenshots in `work/done/` show the tree block as built, on the site in light and dark and in the PDF, in both editions.

**Out of scope.**

* Fixing any finding: each becomes its own line (docs/05 §8).
* Re-testing M31's clauses or its findings: m31-review answered the clauses, and the fix round is read by the area readers, not tested by clause.
* Anything of focus-kit 2026.10.25 or later: M33's lines (Behaviour, the kit's later version).
* The kit's README, CHANGELOG and `test/`, which SETUP §3 does not install (`kit-2026-10-24`'s Out of scope).
* Changing the readers' model or the slot: docs/05 §5 owns it.
* The other session's M33 hunk of docs/06 and its lines (Behaviour, the shared tree).

**Decisions from the documents.**

* The base is m31-review's commit, `99d04a5`, the first of docs/05 §8's cases.
* The three uncommitted deliveries are committed by the author before /apply starts, each as one change; /apply checks and asks, never commits (docs/05 §5's Git slot, §6).
* The author tests each clause by hand and confirms candidates, docs/05 §8's default: no word of the author for this review exists to quote, and a word holds only for the review whose page quotes it.
* The readers start only on the author's word in the /apply session (docs/05 §5's slot, §8's "it costs").
* A kit's-skills area this time, the range holding the installed kit (docs/05 §5's slot names it).
* The end commit and the path inventory are inputs /apply fixes before reading, not open scope (docs/05 §8).
* The token stays `(--)`: this review reads every page and file above it (docs/05 §4), as m31-review's does.
* This page and its line are left unstaged by /propose: docs/05 §2 gives staging to /apply.

**The author's answers.** Given in this /propose conversation on 2026-10-25.

* A candidate that an M33 line already answers is listed with that line and does not open a duplicate line here unless the M33 line's sentence does not hold it, though docs/05 §8 keeps a review's findings in its own milestone: M33 was queued before this review ran, and two lines for one fix would be built twice.

**Decisions taken alone.** The agent chose each of these, for the author's review.

* M32's paragraph is taken as seven clauses, by what the author can check: the book teaches 2026.10.24; the repository runs on it; the tree; its ending; no slug; /apply's end; the offer and its cost.
* The trees rerun on scratch repositories, and the repository's own tree, as mechanical checks beside the clause tests.
* Three readers, the first two as a pair, by the size of the areas; the kit's byte comparison is /apply's mechanical check, not a reader's.
* The readers and the checker are foreground Agent calls reporting to the review's session, with the working files in the scratchpad's `m32/` folder and the candidate table in `m32-candidates.md`, following m29-review's to m31-review's practice.

**Done when.**

* [x] The four M32 deliveries are committed, by the Precondition's check; every line in this review's `after` is `[x]`, and every clause above has an answer, the author's, or, on the author's word quoted on this page, the review's, recorded as the review's.
* [x] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read, whether each agent kept the session's advisor as its report says, that each report reached this session, and every checked candidate with its mark are recorded on this page, with the candidate table.
* [x] Every confirmed candidate is in a `[ ]` line under this review, shared causes sharing a line; every candidate not confirmed is listed with its mark, and each one an M33 line answers names that line; nothing is fixed here.
* [x] The mechanical checks above are recorded with their results; `make verify` is green after the last edit and `make book` built both PDFs at the end commit, both run by this /apply and recorded in its Proof with the commit and both PDF paths, given to the author.
* [x] No separate Delivery review, a milestone review having none (docs/05 §7, no review of a review); this delivery's paths staged as docs/05 §6 says, the page moved to `work/done/` and its commit message suggested in a `commit` block, which ends the page.

**Precondition (/apply).** At the start, `git log --diff-filter=A` returned `914fc75` for `kit-2026-10-24` and nothing for the other three records, whose changes were staged together. /apply stopped and asked; the author chose, in this /apply session, that /apply commit the three, each as its own change. /apply saved the index as a tree, unstaged it, and committed each delivery's paths with its record's own message, docs/06 staged per line by blob so each commit holds its own `[x]` alone and the other session's M33 hunk stayed out: `7d8a0e7` (`ch08-update-2026-10-24`), `0cc0caa` (`ch11-14-queue-tree`), `ef990c3` (`ch19-queue-branches`). The tree of `ef990c3` equals the saved index (`git diff HEAD <tree>` empty), so the line numbers this page took on the staged tree hold at the end commit; spot-checked at every passage the Contract names, both editions. The check then returned one commit for each of the four records. `git log --diff-filter=A -- work/done/m31-review.md` returns `99d04a5` alone.

**Base and end.** Base `99d04a5`; end `ef990c3` (`docs(ch19-queue-branches): read every delivery's line from its branch`), HEAD when the reading started, recorded before any reader. The range holds `28cae3f`, `024a4a0`, `920d3fc`, `a20faef`, `914fc75`, `7d8a0e7`, `0cc0caa` and `ef990c3`. This page and its `[*]` are uncommitted and read from the working tree as the spec; the other session's M33 hunk of docs/06 is uncommitted and outside the range.

**Inventory.** `git diff --stat -M 99d04a5..ef990c3`: 49 paths, by area.

* Build (1): `VERSION`.
* Chapters (14): `book/{en,pt}/` 08, 11, 12, 13, 14, 19 and 22.
* The kit's skills (14): `.claude/skills/` and `.agents/skills/` each `analyze/SKILL.md`, `analyze/references/documents.md`, `apply/SKILL.md`, `brainstorm/SKILL.md`, `brainstorm/references/documents.md`, `propose/SKILL.md`, `propose/scripts/queue.sh`.
* The documents (20): `docs/03-Domain.md`, `docs/05-Process.md`, `docs/06-Queue.md`, `docs/adr/ADR-0018-six-marks.md`, `work/kit-proposals.md`, `work/done/` `ch08-update-2026-10-24.md`, `ch11-14-queue-tree.md` and its six screenshots, `ch19-queue-branches.md`, `ch22-cache-route-host.md`, `ch22-cache-service.md`, `kit-2026-10-24.md`, `m30-records-claims.md`, `m31-records-claims.md`, `m31-review.md`.

**Slow tests.** None (docs/05 §5's Verify slot).

**Mechanical checks**, at `ef990c3`, outside this repository in the session's scratchpad `m32/` folder:

* `git -C ~/Projects/focus-kit show 51ff062:SETUP.md` has SHA-256 `90877174c1d6e18383f2f3d8ce42f367499cb166f89c6c932d9aa8366a07abec`, the Contract's. SETUP §3 rendered to its thirty-four destinations (3.1 to 3.7 in both skills folders, 3.8 to 3.11 four each, 3.12, and 3.13 as `GEMINI.md`'s first line, once): all thirty-four byte-equal at `ef990c3`. All eight installed `SKILL.md` carry `version: "2026.10.24"`.
* The trees rerun, the installed `queue.sh` and `claim.sh` from `git show ef990c3:`: chapter 14's nine lines under chapter 11's heading, `trunk`, byte-equal to chapter 14's tree (en :129 to :142, pt likewise) in both editions; the four token lines print `free for /propose, together: search-catalog renew-loan` (pt `buscar-catalogo renovar-emprestimo`), as chapter 14 :146 / :148 says; chapter 11's milestone (en :49 to :54, pt :52 to :57) with `lend-book` `[x]` prints `return-book` and `m1-review` `propose now, no token: judge`, nothing together, `judge first, no token: return-book m1-review`, as chapter 13's step 4 (:169) says; chapter 19's fixture (bare origin, `main/`, both lines claimed with `worktree .focus-kit focus-kit/`, `return-book` pushed at `[*]` with `damaged-copy` added, `overdue-list` at `[>]`), run from `main/`, byte-equal to chapter 19's block (:202 to :212) in both editions.
* The repository tree: `git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq trunk` printed, exit 0, `git status --porcelain` the same before and after:

  ```
  milestone: M32. focus-kit 2026.10.24
  [*] m32-review (--) · in flight: apply

  free for /apply, together: none
  free for /propose, together: none
  ```

* `git status --short book/` was empty before `make book`; `make book` built both PDFs at `ef990c3`, exit 0. Pages (the PDF page and the printed number agree), en / pt: chapter 8 starts 79 / 82, its "Install" passages 80 / 83, the refusal 81 / 84, the report excerpt 81 to 83 / 85 to 86, "How each host finds the commands" 84 / 88, `/apply` naming the tree 87 / 91; chapter 11 starts 106 / 111, the script drawing the order 110 / 115; chapter 12 starts 116 / 122, no slug 117 / 123, each slug's cost 123 / 130; chapter 13 starts 128 / 135, no slug 129 / 137, "Green is not done" 135 / 143, step 4 138 / 146; chapter 14 starts 146 / 154, "What may run now" and its tree 152 / 161, the four token lines and no slug 153 / 162, its key point 158 / 168; chapter 19 starts 196 / 207, "Worktrees in the kit" 204 / 215, its tree 205 / 216, the key point 215 / 227.
* `git branch --list` shows `main` alone.

**The author's word for this review.** Given in this /apply session on 2026-10-25, as answers to two questions /apply asked. To "Os testes das sete cláusulas ... e a confirmação dos candidatos: quem faz?": "A sessão testa e confirma". To "A leitura de código custa ... Posso começar agora?": "Sim, comece". By the first, the clause answers below are the review's, from its own reading of both PDFs and of the repository at `ef990c3`, never the author's, and each candidate the checker marks seen is confirmed, the latent and weak ones listed as dropped (docs/05 §8). By the second, the readers started.

**The clause answers, the review's.** By the author's word above, each test answered by this session from its own reading of both PDFs built at `ef990c3` (`output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`, pages read as text with `pdftotext -layout`) and of the repository at `ef990c3`; these are the review's answers, not the author's. Lines are the Contract's, which hold at `ef990c3`.

* **The book teaches focus-kit 2026.10.24: holds.** Chapter 8, en 80 / pt 83: the kit's files are "the four commands, with two small scripts the commands run through git" ("com dois pequenos scripts que os comandos rodam pelo git"), and on Windows "the scripts the commands run (chapters 13 and 14) go through" Git for Windows' shell. En 81 / pt 84: the refusal sentence names `.claude/skills/apply/SKILL.md` and focus-kit 2026.10.24, on "a copy of the book's kit files, made outside the book's repository". En 82 / pt 85 to 86: the excerpt says "Installed: focus-kit 2026.10.24, in every SKILL.md", holds the one pending migration, docs/05 §4 on what may run now, with the template's two sentences quoted (translated in the Portuguese, which says so), beside the section numbers that match and the Git slot as a recorded choice, each ending `None` but the migration; the text says every item is reported, never done. No count of files, no SETUP section number, no `2026.10.20.5` in chapter 8 (grep at `ef990c3`, both editions). En 87 / pt 91: `/apply` names what may run next, the queue tree. Chapter 19, en 204 to 205 / pt 216 to 217: with a worktree per delivery the script reads each delivery's line from `origin/<prefix><slug>`, keeps the mark furthest along, lists `damaged-copy` (`exemplar-danificado`) as only on a branch, and says what it cannot see, a mark or branch not pushed, and the moment after a claim before its first mark is pushed. Both editions say the same.
* **And the repository runs on it: holds.** The eight `SKILL.md` say `version: "2026.10.24"`; docs/05 §4 (:110 to :117) says what may run now is answered by running `queue.sh` and showing its tree, the free lines offered as one command, each slug one more agent at the cost of a session; the command prints a tree (Mechanical checks).
* **What may run now comes from `queue.sh`, a tree: holds.** Chapter 14, en 152 / pt 161: the agent runs the kit's queue script in one line, "the same alias trick and the same strategy word as the claim script of chapter 13", and it edits nothing; its tree draws chapter 11's milestone with `return-book` and `my-loans` under `lend-book`, each with its state, no `[x]` line; the text says a line sits under "the one furthest down the queue of the pending lines its after names, with the others named after + after". Chapter 11, en 110 / pt 115: the script draws `return-book` under `lend-book` while `lend-book` is not `[x]`. On this repository the command printed M32's tree with each line's state.
* **Ending with the lines free for /apply and for /propose together: holds.** Chapter 14's tree ends with the two free lists and `judge first, no token: search-catalog m1-review`; en 153 / pt 161 to 162 judge `search-catalog` by `src/features/catalog/` and `m1-review` by its page; the four token lines end with `free for /propose, together: search-catalog renew-loan` (pt `buscar-catalogo renovar-emprestimo`). Chapter 19's tree ends with `free for /apply, together: overdue-list` (pt `lista-de-atrasos`) and its only-on-a-branch list.
* **/propose and /apply typed with no slug show it: holds.** Chapter 12 :25 (en 117 / pt 123), chapter 13 :22 (en 129 / pt 137) and chapter 14 :147 / :149 (en 153 / pt 162) say so, and that they ask which line to take. On this repository, propose's and apply's `SKILL.md` at `ef990c3` say "none, show what may run now as docs/05 §4 says and ask"; `/propose` typed with no slug was not run in a session for this review: the skill text is the answer, and /propose is not run by /apply.
* **/apply ends with it: holds.** Chapter 13 :120 (en 135 / pt 143): the last next step is what may run next, the queue tree; step 4 (:169, en 138 / pt 146) gives `return-book` and `m1-review` free for `/propose`, judges the review to wait and gives `/propose return-book`, what the scratch rerun prints. Chapter 14 :147 / :149 and chapter 8 :151 / :153 say it too; apply's `SKILL.md`'s last paragraph says "what may run next, as docs/05 §4 says". This review's /apply ends with the tree (its next steps).
* **The free lines are offered as one command with several slugs, each slug one more agent at the cost of a session: holds.** Chapter 12 :156 to :157 / :165 to :166 (en 123 / pt 130): each slug is one more agent costing as much as one session, and asked what may run now or typed with no slug the agent offers the free lines as one such command; chapter 14 (en 153 / pt 162) gives `/propose search-catalog renew-loan` with that cost.

**Readers.** Three read-only readers on Opus, the first two as a pair, then the third alone, then the checker alone; at most two ran at once. Each was launched with its model set to Opus from this session; the host ran each in the background and delivered its final report to this session as its completion notice, which is the report recorded here. Working notes in the scratchpad's `m32/` folder.

* **Reader 1, chapters 8 and 11 to 14.** Read whole at `ef990c3`: en 08, 11, 12, 13, 14 and pt 08; the range diff of all ten files whole; pt 14 :1 to :90 line by line and the rest by its diff and greps; pt 11, 12 and 13 by their diffs, targeted reads, greps and an en/pt line-pair script for numbers and code spans. Also `queue.sh` and propose's `SKILL.md` whole, apply's `SKILL.md` :1 to :30 and :55 to :68, docs/05 §4 whole, docs/04 by grep and :40 to :45, the ch08 and ch11-14 records whole, the kit record by grep and :89 to :125, en 19 by grep, SETUP.md at `51ff062` (§1, §3.7's intro, §4) and its 2026.10.24 changelog entry. Its report: the advisor present, called twice.
* **Reader 2, the kit's skills and the documents.** Read whole: `.claude/skills/propose/scripts/queue.sh` (the same blob as `.agents/`'s), propose's and apply's `SKILL.md`, docs/03, docs/05, ADR-0018, `work/kit-proposals.md`, `work/done/kit-2026-10-24.md`; by range diff: analyze's and brainstorm's `SKILL.md` and `references/documents.md`, the six `.agents/skills/` copies (each the same blob as its `.claude/skills/` copy), docs/06 (and :694 to :722 whole); by grep: AGENTS.md, docs/01, docs/04, en 08, en 19, the ch08 record. It reran the kit record's Step 5 tree, byte-equal. Its report: the advisor present, called twice.
* **Reader 3, chapters 19 and 22 and the other records.** Read whole: en 19, en 22, the records `ch19-queue-branches`, `ch22-cache-route-host`, `m31-records-claims` and `ch11-14-queue-tree`, `queue.sh` and `claim.sh`; pt 19 by its diff and :1 to :195, :225 to :406, with :407 to :424 by its diff and a heading grep; pt 22 by its diff and :1 to :147 but :43 to :48; `ch22-cache-service`, `m30-records-claims` and `m31-review` whole or in part and by their diffs; the kit record whole; the ch08 record by grep; the six screenshots viewed; `VERSION`; docs/05 :100 to :182, docs/03 by diff and :116 to :121, docs/04 by grep, docs/06 :697 to :709, `work/kit-proposals.md` by diff, en 14 :50 to :70 and :118 to :152. Its report: the advisor present, called twice.
* **The checker**, one agent on all twenty-one candidates in one report, every file at `ef990c3`, the six screenshots opened; 13 seen, 5 latent, 3 weak. Its report: the advisor present, called twice.

Every path of the inventory was read by at least one reader, each through its range diff at the least: the build and chapter 22 by reader 3, the chapters 8 and 11 to 14 by reader 1, the fourteen skill paths and the documents by reader 2, the records and screenshots by reader 3. Where a reader read a file by diff and grep rather than whole, the report says so above; every hunk of the range was read.

**Candidates.** The checker's marks, with the M33 line that answers each, from the table in the scratchpad's `m32-candidates.md`:

| Id | Where, at `ef990c3` | Candidate | Mark | M33 line | Outcome |
|---|---|---|---|---|---|
| R1-1 | ch14 en :125 / pt :126 | Says the script reads "each delivery's line where it lives, as the section above says", while `queue.sh` reads origin only, keeps the mark furthest along and does not take a branch as the claim | seen | `ch11-14-after`, in part | Held by `ch11-14-after`, the author deciding; no line here |
| R1-2 | ch13 en/pt :39 | "the next free line" beside the queue tree | weak | `ch11-14-after` | Dropped |
| R1-3 | ch14 en :244 to :249 / pt :246 to :251 | Six key points; docs/04 :133 allows five | seen | none | `ch14-key-points-pointers` |
| R1-4 | ch08 en :102 / pt :104; ch12 :29; ch13 :39; ch14 en :62, :232, :249 / pt :63, :234, :251 | "local or remote" while `queue.sh` reads origin only | seen | `kit-2026-10-25`, `ch11-14-after`, `ch08-update-2026-10-25` | Held by those lines; no line here |
| R1-5 | ch08 en :24, :151 / pt :24, :153; ch12 en :25; ch13 en :22; ch14 en :125, :145 / pt :126, :147 | Forward pointers added beside existing ones; docs/04 :43, once per chapter for each target | seen | none | `ch14-key-points-pointers` |
| R1-6 | pt ch08 :75 | "cada slug é mais um agente" against "um agente a mais" in pt ch12 and ch14 | seen | `ch08-update-2026-10-25`, in part | Held by `ch08-update-2026-10-25`, the author deciding; no line here |
| R2-1 | docs/05 :133 to :139 | "local or remote" against §4's `queue.sh` | latent | `kit-2026-10-25` | Dropped |
| R2-2 | docs/03 :31 | Kanban board row "local or remote" | latent | `kit-2026-10-25` | Dropped |
| R2-3 | docs/03 :117 against :119 | The free line row and the queue tree's free lists, `queue.sh` without a branch check | latent | in part | Dropped |
| R2-4 | docs/03 :119; ADR-0018 :88 | Cite docs/05 §4 for the no-slug rule and /apply's ending, which live in the skills | seen | none | `queue-tree-row-source` |
| R2-5 | docs/03 :119; ADR-0018 :88 | "each under the last line it waits on" without `queue.sh` :137's condition | latent | none | Dropped |
| R2-6 | docs/06 :718 | `ch08-update-2026-10-24`'s line promises "sixteen files ... §3.7" | weak | none | Dropped, a recorded decision |
| R2-7 | `work/done/kit-2026-10-24.md` :30, :88 | "from docs/06 and work/ as `queue.sh` reads them"; it never reads work/ | seen | none | `m32-records-claims` |
| R3-1 | `work/done/ch08-update-2026-10-24.md` :121 | "2026.10.20.3 only at en 97 / pt 101"; pt is :99 | seen | none | `m32-records-claims` |
| R3-2 | `work/done/ch11-14-queue-tree-*.png`; record :154 | The six shots show chapter 14 before its review's two fixes, unsaid | seen | none | `m32-records-claims` |
| R3-3 | `work/done/ch19-queue-branches.md` :82, :86 | "reverses decision 4", which is about its own `(PA)` token | seen | none | `m32-records-claims` |
| R3-4 | `work/done/ch19-queue-branches.md` :101 | Quotes the changelog with "or in-flight", the chapter's own words | seen | none | `m32-records-claims` |
| R3-5 | ch19 en/pt :223, the example at :200 | A mark pushed mid-delivery, which the default flow never does | seen | `ch19-claim-integration`, in part | `ch19-example-marks`, the author deciding |
| R3-6 | ch19 en/pt :223 to :224 | A claimed line shows `propose now` against the claim rule | weak | `ch19-claim-integration` | Dropped |
| R3-7 | ch19 en/pt :199, :412 | "furthest along" lets an older `[>]` or `[*]` beat a later `[?]` | latent | `ch19-claim-integration` | Dropped |
| R3-8 | ch19 en/pt :205, :208 | `overdue-list (PA)` free together while :97 has both lines in `src/features/loans/` | seen | none | `ch19-example-marks` |

Noticed by the checker and not checked, outside this reading: `queue.sh` at `51ff062` reads `· after all` as a slug named `all`, which M33's review line uses; that is 2026.10.25's to answer (`kit-2026-10-25`, Out of scope).

**Findings.** By the author's word above, every candidate marked seen is confirmed, and the latent and weak ones are dropped as the table says. For the three seen candidates an M33 line answers in part, /apply asked the author, who chose in this session that R3-5 become a line here and R1-1 and R1-6 stay with `ch11-14-after` and `ch08-update-2026-10-25`. R1-4 is held whole by the M33 lines its row names. Four `[ ]` lines under this review in docs/06, in M32, candidates sharing a file or a cause sharing a line:

* `m32-records-claims` (PA): R2-7, R3-1, R3-2, R3-3, R3-4, four records' precision.
* `queue-tree-row-source` (PA): R2-4, one sentence in docs/03 and ADR-0018.
* `ch14-key-points-pointers` (PA): R1-3 and R1-5, the docs/04 questions `ch11-14-queue-tree` left to the person.
* `ch19-example-marks` (PA): R3-5 and R3-8, chapter 19's example at :200 to :224.

Each line is `· after m32-review` and carries `(PA)`: no other M32 line is in flight, and the four touch different files. No fix was made here.

**Proof.** The mechanical checks and the clause answers above; `make book` at `ef990c3` (Mechanical checks); `make verify` green after the last edit to anything it covers (this page and docs/06's lines), run by this /apply; `make book` at `ef990c3`, with `book/` clean, built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, given to the author. The repository's queue tree with this line `[*]` is under Mechanical checks.

**Decisions taken alone in /apply.** For the author's review.

* The three commits were made by blob for docs/06, one `[x]` each, since the three lines share one hunk with each other and with the other session's M33 block.
* The readers ran in the background and reported by completion notice, not as foreground calls as Behaviour planned; each notice was the agent's own final report, delivered to this session, so it is recorded as its report.
* The four lines group candidates by the file they would change, so no two lines edit the same file.

```commit
docs(m32-review): review M32, four findings

- The four M32 deliveries committed; base 99d04a5, end ef990c3
- Seven clauses hold, answered by the review on the author's word
- Kit destinations, chapter trees and the repository tree checked
- Three readers and a checker: 13 seen, 5 latent, 3 weak
- Four lines under m32-review in docs/06

work/done/m32-review.md
```
