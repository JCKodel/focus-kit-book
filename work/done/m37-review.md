# m37-review

**Objective.** The author can decide whether M37's promise holds, the clauses of its paragraph tested in the PDF of both editions and on this repository, and whether everything changed since m36-review's commit holds under the code reading by areas, with every confirmed finding graded: each grave one a line under this review, the medium ones in the one `m37-fixes` line, the small ones listed here.

This page was defined by the agent before the author read it, on the author's word for this run, relayed by the driver session on 2026-11-13: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão" (close every open line of docs/06 without supervision). Every question the documents leave open is answered by the agent's recommendation, written below as the agent's choice; the author reads the page and the diff at the end (docs/05 §4).

**Behaviour.**

* With every line above this review in M37 `[x]` and committed, and M36's finding line `m36-fixes` committed, /apply records the base and the end commit, builds both PDFs at the end commit, and answers each clause test below: holds, or fails with what was seen. A clause no delivery answers, or one that fails, is a finding (docs/05 §8).
* The review opens by copying onto this page, verbatim, the notes under `## For the review` of every page the range delivered, naming the pages that have none (today `ch13-apply-next` and `m36-fixes` have one each, below); the checker marks each note as it marks a candidate (docs/05 §8).
* Read-only readers on Opus read one fixed range, `git diff <base>..<end>`, one per area the range touches, at most two running at a time; one checker on Opus then marks every candidate and every note seen, latent or weak against the end commit (docs/05 §5, Milestone review). Every launch sets its model to Opus, runs in the foreground so its report reaches this session, and keeps the session's advisor.
* On the author's word, quoted below, the review's session takes the clause tests from its own reading of both PDFs and of the repository, and the word is the confirmation of each candidate the checker marks seen; the latent and weak ones are listed as dropped. These answers are the review's, never the author's (docs/05 §8).
* Every confirmed finding is graded by docs/05 §4 and §8: grave, when it breaks a clause of M37's paragraph for a person on its usual path, loses or exposes data, or leaves verify red, each its own `[ ]` line under this review ending `· after m37-review · from m37-review`; medium, met in ordinary use while the clause holds; small, a rare case, a latent or weak candidate, a cost nobody measured.
* On the author's word for the medium pick, every medium finding enters the one `m37-fixes` line, each an item of its page, ending `· after m37-review · from m37-review`; with no medium finding, no line. Small ones are listed on this page, numbered, and none becomes a line.
* A clause with no answer, a reader or checker whose report does not reach this session, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8).
* Edge, M36's fix line in the range: `m36-fixes` (chapters 14 and 15, both editions) was committed as `0e22d1a` while this page was written. Its paths are read by the area readers without a clause test and with no second review (docs/05 §8); its two items are given to the checker as a lead.
* Edge, a later milestone's delivery in the range: M38's `ch14-queue-findings` and `ch15-review-grades` are `[>]`, `ch13-apply-findings` is `[ ]`, and M39's `ch14-open-lines-search` has a page in `work/`; another session may commit one before the end commit. Its paths are read by the area readers without a clause test, its notes are copied here, since the range delivered its page, and the Outcome names it so that milestone's review knows its code was read here. The chapter 14 and 15 reader then tells `m36-fixes`' hunks from that delivery's; chapter 13's clause passages are found at the end commit by the sentences quoted below.
* Edge, a candidate an open line holds: a candidate one of M38's or M39's open lines already holds is listed with that line and is no finding here; `ch13-apply-next`'s note, which names `ch14-queue-every-milestone`, is checked by the checker against that line's own words, since the line says nothing of chapter 13's tree.
* Edge, the shared tree at build time: the PDFs read are the end commit's. When `git diff <end> -- book/` is empty, `make book` runs in the tree under the run's lock; when another session holds uncommitted edits in `book/`, /apply touches none of them (no stash, no restore) and builds from `git archive <end>` exported into the session's scratchpad, under the same lock. If that export cannot build, the line waits as `[?]` with `· resume: apply · blocked: after <slug>`, the slug whose edits hold `book/` (docs/05 §4, the third case).
* Edge, the kit's own scripts: no path under `.claude/skills/` or `.agents/skills/` is in the range today; a candidate in one is graded as any other, and its fix, when it enters, is a note in `work/kit-proposals.md`.
* Edge, the error's project: chapter 13's report of 2026-11-03 is told as the kit's changelog words it, with the person unnamed and no project; by the author's word of 2026-11-13 ("Sim, como o changelog") it is no Case A or Case B passage, so docs/05 §5's Case A and Case B slot asks nothing of this review.
* Edge, the shared tree while reading: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree or the index; a commit made during the reading does not move the end commit.

**Contract.** Clause tests from docs/06's M37 paragraph (:780, "`/apply` ending by telling the person each next step, and by running `queue.sh` though no one asked, its tree shown and its `next:` command written as the host invokes commands"), each against its delivery's page in `work/done/` and the named passages. Chapter 13 lines en / pt at `a0a9e3d`, the same at `0e22d1a` (`m36-fixes` does not touch chapter 13), with the sentence quoted, since lines drift; /apply finds their lines and PDF pages at the end commit. The clause ids below are this review's, not that page's C1 to C4.

| Clause | Deliveries and passages | The test |
|---|---|---|
| K1. The book teaches focus-kit 2026.11.03 | `ch13-apply-next`: chapter 13 :5 / :5 (the opening, "your next steps told to you, the queue tree with the next command and, last of all, which environment is at which version"), :128 and :129 / :128 and :129, the example :173 to :193 / :173 to :193, key point 4 :312 / :312 | Does chapter 13 teach `/apply`'s ending as 2026.11.03's two sentences of the installed `apply/SKILL.md` have it (the marks the same file opens the last message with are `ch13-apply-findings`' to teach): the next steps told to the person, then the queue tree drawn though no one asked, then the environments? Does no other chapter tell that ending otherwise (Mechanical checks)? Do the two editions say the same, in docs/03's Portuguese terms ("árvore da fila") and the chapters' own ("script de fila", "próximos passos", "mesmo sem ninguém pedir")? |
| K2. And the repository runs on it | `kit-2026-11-03` (page added in `33432ee`, before the base; its text says the kit's files were rewritten at 2026.11.12 in `84de9f1`; applied outside /propose and /apply, with no Delivery review): ADR-0018 :106 to :108, "## Amendment, 2026-11-12 (kit-2026-11-03)"; the installed `apply/SKILL.md` :79 to :86, "Then tell the person their next steps ... Then run the queue script of docs/05 §4, though no one asked, and show its tree as §4 says, its `next:` command written for this host"; docs/03 :123's `queue tree` row, "/apply ends with it, as apply's says" | Does the installed `apply/SKILL.md`, in both skills folders, equal the kit's `SETUP.md` §3.4 at `4f5da97`, focus-kit 2026.11.12, the version the repository runs, and hold 2026.11.03's two sentences? Does ADR-0018 hold the amendment, and do docs/05, docs/03 and AGENTS.md need nothing, as the kit's changelog says ("no project document changes")? |
| K3. `/apply` ending by telling the person each next step | `ch13-apply-next`: chapter 13 :128 / :128, "Its last words are your next steps, each told to you: use what the delivery changed as its user would, ...; review the staged diff; commit with the suggested message", with the quote "*Tell them to review the staged diff, then to commit with the suggested message*" and its reason; :173 to :177 / :173 to :177, "Then it tells you your next steps:" and the three steps; key point 4 :312 / :312 | Does chapter 13 say each step is told to the person, use, review, commit, and give the reason in the present, a step written as a bare order in the agent's own instructions being the agent's to follow and contradicting its "never commit", so the agent says them and does none? Is the quote the installed file's words? |
| K4. And by running `queue.sh` though no one asked, its tree shown | `ch13-apply-next`: chapter 13 :129 / :129, "Then, though no one asked, it runs the kit's queue script and shows its tree (chapter 14)", with its reason; :179 to :193 / :179 to :193, the tree "in an example written for this chapter", :192, "An ending that waits to be asked names no next command: on 2026-11-03 a person reported that `/apply` had ended without naming the next command", and :193, "ask it for the tree" | Does chapter 13 give the reason in the present, the script answering whoever asks what may run now and no one having asked at the end of `/apply`? Is the tree the installed `queue.sh`'s real output on the chapter's example (Mechanical checks)? Is the report of 2026-11-03 told as the kit's changelog `## 2026.11.03` words it, with no person or project named? Does the reader learn what to do when a session ends without the tree? |
| K5. Its `next:` command written as the host invokes commands | `ch13-apply-next`: chapter 13 :129 / :129, "its `next:`, the first free line's command, written the same way"; :188 and :191 / :188 and :191, "`/propose return-book`, in a fresh session, in Claude Code, or `$propose return-book` in Codex (chapter 8's table)"; key point 4 :312 / :312 | Does chapter 13 say `next:` is written as the reader's host invokes commands, and do its two forms match chapter 8's table :132 to :133 (`/propose <slug>` in Claude Code, `$propose <slug>` in Codex)? |

The kit's changelog, `## 2026.11.03` in `CHANGELOG.md` and `CHANGELOG.pt.md` of the kit's repository, is the source the report, its date and the reason are checked against.

**Base.** `066b3bf` (`docs(m36-review): review M36, five clauses hold, two medium fixes`), the commit of m36-review, the previous milestone's review (docs/05 §8), the one commit `git log --diff-filter=A -- work/done/m36-review.md` returns. The range today holds M37's chapter delivery, `ch13-apply-next` (`a0a9e3d`), and M36's one finding line, `m36-fixes` (`0e22d1a`), read by the area readers without a clause and with no second review (docs/05 §8). `kit-2026-11-03` was committed before the base, in `33432ee`; K2 tests its result at the end commit.

**End.** The commit HEAD is when the reading starts, recorded before any reader; this page and its mark, uncommitted, are read from the working tree as the spec.

**Areas.** From `git diff --stat -M 066b3bf..0e22d1a`, nine paths; /apply recomputes them at the end commit, places every path in an area of docs/05 §5's Milestone review slot, and adds a reader for any area that appears:

* **Build:** no path of the `Makefile`, `scripts/`, the READMEs, `VERSION` or `docs/manuals/`; no reader.
* **The kit's skills:** no path; no reader.
* **Chapters:** `book/{en,pt}/` 13 (`ch13-apply-next`) and 14 and 15 (`m36-fixes`), six files, split in two readers.
* **The documents:** `docs/06`, and the two records under `work/done/` the range adds, `ch13-apply-next.md` and `m36-fixes.md`, read with the chapters they describe, docs/03, docs/04 and docs/05.

**Readers.** Three read-only readers on Opus, then one read-only checker on Opus alone; each launch sets its model to Opus, runs in the foreground and keeps the session's advisor, at most two at a time (docs/05 §5):

* pair 1: **chapter 13** (M37's delivery), both editions, whole at the end commit and by its range diff, against its page, the installed `apply/SKILL.md` and `queue.sh`, and chapters 8, 10, 12 and 14 where they tell `/apply`'s ending; and **chapters 14 and 15** (M36's finding line), both editions, whole at the end commit and by their range diffs, against `m36-fixes.md` and m36-review's two medium findings;
* then **the documents and records**, against each other, the chapters they describe, docs/04 and the kit's changelog;
* then the checker, on every candidate, every copied note and every lead in one report.

Each reader lists the paths it read and how (whole, diff, grep), and says whether it kept the advisor.

**Notes to copy**, as they stand today; /apply copies them verbatim from the end commit:

* `work/done/ch13-apply-next.md` :115, on chapter 13 :181's tree: "once M39's `ch14-queue-every-milestone` teaches it drawing every open milestone, this example's queue (milestone 2 holding `suspension-end`, which :154 creates) would also draw milestone 2 and offer `suspension-end`, so that line's /propose should re-run the script on this example and update the tree here."
* `work/done/m36-fixes.md` :94, on `book/pt/14-queue-states.md:230`, "e a revisão espera com ela até a pessoa redecidi-la" (en :228, "until the person re-decides it"): "-la" readable as `a revisão`, the same ambiguity as m36-review's M2.

**Slow tests.** None (docs/05 §5's Verify slot).

**Known leads**, given to the checker with the readers' candidates:

* L1, m36-review's two medium findings, read as fixed at the end commit in both editions: M1, chapter 14's reason that a review is neither dropped nor rewritten, against the 27-slug list; M2, chapter 15 :18's "re-decide it" read as the cancelled line.
* L2, chapter 10 :67 / pt :67, the quick guide's "You see ... your next steps, starting with using what the delivery changed": whether it leaves out the queue tree `/apply` now draws unasked.
* L3, chapter 8 :159 / pt :160, "`/apply` names what may run next, the queue tree", and chapter 13 :43, "it ends with what may run next, the queue tree": whether either tells the ending otherwise than chapter 13 :128 to :129.
* L4, pt chapter 13 :179's clause the English lacks, "e as palavras do script ficam em inglês, como o kit as imprime", against pt chapter 14 :138's own, "As palavras do script ficam em inglês, como o kit as imprime, assim como os sufixos.": whether the point is said twice.
* L5, chapter 13 key point 4 :312, "also when it stops blocked; its last words are your next steps ...", against `ch13-apply-next`'s Out of scope, which left a blocked ending's steps and tree out, and the installed `apply/SKILL.md` :76 to :86 ("done or blocked").
* L6, chapter 13 :192's "had ended without naming the next command" against the changelog's "had stopped naming the next command after an update", the delivery's recorded divergence; and docs/06 :784's "no longer bare sentences", the delivery review's seventh candidate, left as the line is.
* L7, `kit-2026-11-03.md`'s "Chapter 13 still teaches the old ending" and "no Delivery review ran", against the record of `ch13-apply-next` and ADR-0018 :108.
* L8, `ch13-apply-next`'s note: the kit's newest `queue.sh` (focus-kit 2026.11.13, `SETUP.md` §3.7 at the kit's `fdc845c`, extracted with `git show` into the session's scratchpad, nothing written in the kit's tree) run on chapter 13's example, to see whether it offers `suspension-end` as the note says.

**Mechanical checks**, run by /apply at the end commit:

* The installed `apply/SKILL.md` and `queue.sh`, in `.agents/skills/` and `.claude/skills/`, equal to the kit's `SETUP.md` §3.4 and §3.7 at `4f5da97`, focus-kit 2026.11.12, the version the repository runs (`kit-2026-11-13` is still open).
* Chapter 13 :128's quote, word for word against the installed `apply/SKILL.md` :82 to :83, "Tell them to review the staged diff, then to commit with the suggested message".
* The installed `queue.sh trunk` on a scratch repository holding chapter 11's milestone 1 with `lend-book` `[x]` and a milestone 2 with `suspension-end`, en and pt (pt chapter 11's heading and slugs): its output byte for byte chapter 13 :181 to :189 / pt :181 to :189.
* Chapter 13 :192 / pt :192 against the kit's `CHANGELOG.md` and `CHANGELOG.pt.md` `## 2026.11.03`: the date, the person unnamed, no project, place or business detail.
* Chapter 13 :191's two forms against chapter 8 :132 to :133.
* `book/` in both editions searched for a passage that tells `/apply`'s ending otherwise than chapter 13 :128 to :129 (today, en lines: chapter 8 :159, "`/apply` names what may run next, the queue tree"; chapter 10 :67, "your next steps, starting with using what the delivery changed"; chapter 13 :43 and :312; chapter 14 :134, "Asked what may run now, the agent does not read the end of every line for its `after`: it runs the kit's queue script", and :278, "Asked what may run now, the agent runs the kit's queue script and shows its tree"; pt chapter 14 at :135 and :280).
* The disclosure scan at the end commit.
* The repository's tree: `queue.sh trunk` prints M37 with `m37-review` in flight, `git status` the same before and after.
* `make book` at the end commit, as the shared-tree edge says; `make verify` after the last edit.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit.

**Out of scope.**

* Fixing any finding: grave ones become lines, medium ones the `m37-fixes` line (docs/05 §8).
* Re-testing M36's clauses: its fix line is read by the area readers, not tested by clause.
* Teaching 2026.11.12 and 2026.11.13 in the chapters: M38's and M39's lines.
* A blocked `/apply`'s ending beyond chapter 13 :73, "It ends the page with a partial message in a `commit` block and shows the same block in the conversation.": `ch13-apply-next` left it out; L5 only asks whether key point 4 says more than that page decided.

**Decisions from the documents.**

* The base is m36-review's commit, `066b3bf`, the first of docs/05 §8's cases.
* No build reader and no kit reader: the range touches neither (docs/05 §8, one reader per area it touches); /apply adds one if the inventory shows otherwise.
* The clause tests, the confirmation and the medium pick are taken on the author's word quoted below (docs/05 §8).
* The notes are copied from every page the range delivered (docs/05 §8).
* The installed skill and script are compared with the kit at `4f5da97`, the version the repository runs, not the kit's newest (docs/05 §4's provenance paragraph ends at 2026.11.12).

**The author's word for this review.** Relayed to this session by the driver session on 2026-11-13: "Todas, médios entram": every milestone review `m35-review` to `m39-review` runs; its session takes the clause tests from its own reading of both PDFs and confirms every candidate the checker marks seen (docs/05 §8); every medium finding enters the one `m37-fixes` line; small ones stay listed on the page and none becomes a line. And, for the dated errors: "Sim, como o changelog": they are told as the kit's changelog words them, with no project named, no place and no business detail, none a Case A or Case B passage.

**Decisions taken alone.** The agent chose each of these, for the author's review.

* M37's paragraph is taken as five clauses, by what can be checked: the book teaches 2026.11.03, the repository runs on it, the steps told to the person, the tree drawn unasked, and `next:` in the host's form.
* K2 tests the installed 2026.11.12 skill for 2026.11.03's two sentences, since the repository reinstalled the kit at 2026.11.12 and `kit-2026-11-03` is a record written after it, outside /propose and /apply.
* The chapters area splits in two, by milestone, as m36-review did: M37's delivery in chapter 13, M36's fix in chapters 14 and 15 (docs/05 §8, an area too large for one careful reading).
* The chapter passages are named by line at `a0a9e3d`, with the sentence quoted, since `m36-fixes` does not touch chapter 13; /apply finds the lines and pages at the end commit.
* The queue script is run on chapter 13's own example, so the test checks the chapter's claim and not only the script; the kit's newest script is run on it too, read-only, only to check `ch13-apply-next`'s note.
* The PDFs are the end commit's: built in the tree when `book/` equals it, else from an export of it in the scratchpad, so another session's uncommitted chapter edits are neither read nor touched.
* A later milestone's delivery committed inside the range is read here without a clause and named in the Outcome, so its own review knows.
* A candidate an open M38 or M39 line holds is listed with that line, as m36-review did.

**Done when.**

* [x] Every line above this review in M37 is `[x]` and committed, and `m36-fixes` committed; every clause has the review's answer, on the author's word quoted on this page.
* [x] Base, end, the inventory by area, each reader's paths read and its advisor, every copied note and candidate with its mark are on this page.
* [x] Every confirmed finding graded; each grave one a `[ ]` line under this review; every medium one an item of the `m37-fixes` line, when any; small ones listed, numbered.
* [x] The mechanical checks recorded; `make book` built both PDFs at the end commit; `make verify` green after the last edit, with its time.
* [x] The page in `work/done/`, its paths staged and its commit message suggested.

## Outcome

**Precondition and range, recorded before any reader.** Every line above this review in M37 is `[x]` and committed: `kit-2026-11-03` before the base (`33432ee`), `ch13-apply-next` `a0a9e3d`; M36's finding line `m36-fixes` `0e22d1a`. Base `066b3bf`, the one commit `git log --diff-filter=A -- work/done/m36-review.md` returns. End `0e22d1a` (`docs(m36-fixes): fix M36's two medium findings in chapters 14 and 15`), HEAD when the reading started. The range holds two commits, `a0a9e3d` and `0e22d1a`. No M38 or M39 delivery was committed in the range, so none is named here for its own review. This page and its marks are uncommitted and outside the range. The working tree's `book/` equalled the end commit throughout (`git diff 0e22d1a -- book/` empty), so the `git archive` fallback was not needed.

This review was built by the agent before the author read it, on the author's word quoted below; the author reads the page and the diff at the end (docs/05 §4).

**Inventory.** `git diff --stat -M 066b3bf..0e22d1a`: nine paths, by area. Build: none. The kit's skills: none. Chapters (6): `book/{en,pt}/` 13, 14, 15. The documents (3): `docs/06-Queue.md`, and under `work/done/` `ch13-apply-next.md` and `m36-fixes.md`. As the page expected.

**Slow tests.** None (docs/05 §5's Verify slot).

**Mechanical checks**, at `0e22d1a`:

* The installed `apply/SKILL.md` and `propose/scripts/queue.sh`, in `.agents/skills/` and `.claude/skills/`, byte-equal (`cmp`) to the kit's `SETUP.md` §3.4 and §3.7 at `4f5da97`, at the end commit and in the working tree.
* Chapter 13 en :128's quote, "*Tell them to review the staged diff, then to commit with the suggested message*", word for word the installed `apply/SKILL.md` :82 to :83 (wrapped there; the file goes on ", merging a delivery branch as docs/05 §5 says", which the chapter gives as "(and merge, on a delivery branch)").
* The installed `queue.sh trunk` on two scratch repositories, chapter 11's milestone 1 with `lend-book` / `emprestar-livro` `[x]` and a milestone 2 holding `suspension-end` / `fim-da-suspensao`: its output byte for byte chapter 13 en :182 to :188 / pt :182 to :188 (`diff` empty), exit 0.
* Lead L8: the kit's newest `queue.sh` (`SETUP.md` §3.7 at the kit's `fdc845c`, focus-kit 2026.11.13, extracted with `git show` into the scratchpad, nothing written in the kit's tree) on the same two repositories drew milestone 2 too and printed `free for /propose, in order: return-book suspension-end`, `next: /propose return-book`, as `ch13-apply-next`'s note says.
* Chapter 13 en :192 / pt :192 against the kit's `CHANGELOG.md` and `CHANGELOG.pt.md` `## 2026.11.03`: the date 2026-11-03, "a person" / "uma pessoa" unnamed, no project, place or business detail; "had ended without naming the next command" where the changelog says "had stopped naming the next command after an update", the delivery's recorded divergence (lead L6).
* Chapter 13 :191's two forms, `/propose return-book` in Claude Code and `$propose return-book` in Codex (pt the same with `devolver-livro`), against chapter 8 en :132 to :133 / pt :133 to :134, `/propose <slug>` and `$propose <slug>`: they match.
* `book/` at the end commit, both editions, searched for a passage that tells `/apply`'s ending: chapter 8 en :159 / pt :160 and chapter 14 en :134, :278 / pt :135, :280 tell nothing against chapter 13 :128 to :129; chapter 10 en :67 / pt :67 leaves the tree and its `next:` out (medium 2); chapter 13 :43 and :195 against :128 (small 4).
* The disclosure scan, `make scan`, exit 0.
* The repository's tree, `queue.sh trunk`, exit 0, `git status --porcelain` the same before and after: `milestone: M37. focus-kit 2026.11.03`, `[*] m37-review · in flight: apply`, both free lists `none`, `next: none`.
* `make book` with `book/` equal to the end commit, under the run's lock, exit 0, 16 seconds: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, read with `pdftotext -layout`.

**The author's word for this review.** Relayed to this session by the driver session on 2026-11-13: "Todas, médios entram": every milestone review `m35-review` to `m39-review` runs; its session takes the clause tests from its own reading of both PDFs and confirms every candidate the checker marks seen (docs/05 §8); every medium finding enters the one `m37-fixes` line; small ones stay listed on the page and none becomes a line. And "Sim, como o changelog": the dated errors are told as the kit's changelog words them, with no project named, no place and no business detail, none a Case A or Case B passage. By it, the clause answers below are the review's, from its own reading of both PDFs and of the repository at `0e22d1a`, never the author's; each candidate the checker marks seen is confirmed, the latent and weak ones listed as dropped.

**The clause answers, the review's.** PDF pages en / pt, counted from the PDF's first page; source lines en / pt at `0e22d1a`, the same as at `a0a9e3d`.

* **K1, the book teaches focus-kit 2026.11.03: holds, with one medium finding.** Chapter 13's opening p. 132 / 137 (:5, "your next steps told to you, the queue tree with the next command and, last of all, which environment is at which version"), :128 to :129 p. 140 to 141 / 146, the example :173 to :193 p. 143 to 144 / 149 to 150 and key point 4 :312 p. 150 / 156 teach `/apply`'s ending as the installed `apply/SKILL.md` :79 to :86 has it: the next steps told to the person, then the queue tree drawn though no one asked, then the environments. Chapters 8 and 14 tell nothing against it; chapter 10's quick guide leaves the tree out (medium 2). The two editions say the same, with "árvore da fila", "script de fila", "próximos passos" and "mesmo sem ninguém pedir"; pt :128 translates the kit's quote with no word that it is English (small 6).
* **K2, the repository runs on it: holds.** The installed `apply/SKILL.md`, in both skills folders, equals the kit's `SETUP.md` §3.4 at `4f5da97` (Mechanical checks) and holds 2026.11.03's two sentences, the steps each told ("Then tell the person their next steps ... Tell them to review the staged diff, then to commit with the suggested message") and the script run unasked ("Then run the queue script of docs/05 §4, though no one asked, and show its tree as §4 says, its `next:` command written for this host"). ADR-0018 :106 to :108 holds the amendment `kit-2026-11-03`; docs/03 :123's `queue tree` row says "/apply ends with it, as apply's says"; docs/05, docs/03 and AGENTS.md need nothing more, as the changelog says ("no project document changes"). The repository runs 2026.11.12's files, which hold 2026.11.03's; docs/06's `kit-2026-11-03` line does not say so (small 13).
* **K3, `/apply` ending by telling the person each next step: holds.** Chapter 13 :128 says each step is told to the person, use, review, commit, and gives the reason in the present: "a step written as a bare order in the agent's own instructions is the agent's to follow, and a bare "commit" there would contradict its "never commit"; with each step told to you, the agent says them all and takes none". The quote is the installed file's words. The example :173 to :177 gives the three steps on `lend-book`.
* **K4, running `queue.sh` though no one asked, its tree shown: holds.** Chapter 13 :129 gives the reason in the present, "the script answers whoever asks what may run now, and at the end of `/apply` no one has asked"; the tree :181 to :189 is the installed script's real output on the chapter's example (Mechanical checks); the report of 2026-11-03 is told with the person unnamed and no project, close to the changelog's words (lead L6, dropped); :193 tells the reader to ask for the tree when a session ends without it. The reason is said twice, at :129 and :192 (small 3).
* **K5, its `next:` command written as the host invokes commands: holds.** Chapter 13 :129 says `next:` is "the first free line's command, written the same way", as the reader's host invokes it; :191's `/propose return-book` in Claude Code and `$propose return-book` in Codex match chapter 8's table; key point 4 says "its `next:` written as your host invokes commands".

**Readers.** Three read-only readers on Opus, the first two as a pair, the third once the second ended, then the checker on Opus alone; at most two ran at once. Each was launched from this session with its model set to Opus and asked for the foreground; the host ran them in the background, and each final report reached this session as its completion notice, recorded here. Working files in the session's scratchpad, `m37/`.

* **Reader 1, chapter 13.** The range diff of both editions in full; en 13 whole, in line ranges; pt 13 by the diff, :40 to :46, :59, :69 to :76, :195 to :201, :300 to :313 and a grep of the whole file; `ch13-apply-next.md` whole; the installed `queue.sh` whole and run on two scratch repositories; `apply/SKILL.md` :28 to :48 and :60 to :95; docs/05 :96 to :215; docs/04 :3 to :64; docs/03 by grep; chapters 8, 10, 12, 14, 15 by grep, en 10 :60 to :80, pt 10 :66 to :68, en 14 :140 to :166; chapter 11 en :41 to :55, pt :43 to :58; the kit's changelog `## 2026.11.03`. Advisor present, called twice.
* **Reader 2, chapters 14 and 15.** The range diffs of the four files whole and `git log` of each over the range; en 14 :195 to :240 and by grep; pt 14 :214 to :233 and by grep; en and pt 15 :1 to :30, en :167, pt :170; `m36-fixes.md` whole; `m36-review.md` from Findings to its commit block; docs/05 :98 to :110, :194 to :218, :434 to :445; docs/03 and docs/04 by grep; `queue.sh` :125 to :165; chapter 11 en :70 to :78 and :93 to :97; `book/` by grep; the kit's changelog `## 2026.10.27.1`. Advisor present, called once.
* **Reader 3, the documents and records.** The range diffs of docs/06 and the six chapter files; whole: `ch13-apply-next.md`, `m36-fixes.md`, `kit-2026-11-03.md`; docs/06 :760 to :811; `m36-review.md`, ADR-0018, `apply/SKILL.md`, `queue.sh`, docs/03, docs/04, docs/05 §§3, 4, 5, 6 in part; the kit's changelogs `## 2026.11.03` and `## 2026.10.27.1`; the two commit messages against the pages' `commit` blocks (they match). Advisor present, called once.
* **The checker**, one agent on every candidate, note and lead in one report, each file opened at `0e22d1a`, the kit's `SETUP.md` at `e77578a` (2026.11.03) and `4f5da97`, its changelog and `fdc845c`'s queue fixture, and the open lines' marks and pages in the working tree read-only for ownership: 17 seen (its own tally said 16, one short of the rows it marked), 7 weak, 1 latent. Advisor present, called once.

Every path of the inventory was read by at least one reader, by its range diff at the least.

**Notes copied**, verbatim from the `## For the review` headings of the range's pages at `0e22d1a`:

* N1, `work/done/ch13-apply-next.md`: "book/en/13-apply.md:181 and book/pt/13-apply.md:181: the example's tree holds while the queue script draws only the first open milestone; once M39's `ch14-queue-every-milestone` teaches it drawing every open milestone, this example's queue (milestone 2 holding `suspension-end`, which :154 creates) would also draw milestone 2 and offer `suspension-end`, so that line's /propose should re-run the script on this example and update the tree here."
* N2, `work/done/m36-fixes.md`: "`book/pt/14-queue-states.md:230`, "e a revisão espera com ela até a pessoa redecidi-la" (en :228, "until the person re-decides it"): the same ambiguity as m36-review's M2, "-la" readable as `a revisão`, the nearer feminine noun; a person reading Portuguese may think the review is what gets re-decided, the more so once M1 removes :223 / :225's "a review is neither dropped nor rewritten", which told the reader a review is not re-decided. Found by `m36-fixes`' /propose, left as it is."

**Candidates.** The checker's marks, lines at `0e22d1a`, en / pt; `=` joins duplicates, graded once.

| Id | Where | Claim | Mark |
|---|---|---|---|
| R1-1 | ch13 :192 / :192 | The dated report against docs/04's "The kit as it is" | weak |
| R1-2 | ch13 :129, :192 | The reason, an ending that waits for the question names no next command, said twice | seen |
| R1-3 | ch13 :43, :128, :129, :195 | "it ends with ... the queue tree", "Its last words are your next steps", then the tree and the environments | seen |
| R1-4 | ch13 :312 | "both are said in the conversation and gone with it" said of the tree | weak |
| R1-5 = R3-2 | pt ch13 :128 | The kit's English quote translated with no word that the original is English (docs/04 :25) | seen |
| R1-6 = L5 | ch13 :69 to :76, :312 | A blocked ending: :312's "also when it stops blocked; its last words are your next steps" says more than :73 | seen |
| R1-7 = L2 | ch10 :67 / :67 | The quick guide's step 6 leaves out the tree and its `next:` | seen |
| R1-7 | ch8 :159 / :160; ch14 :134, :278 / :135, :280 | The same ending told otherwise | weak |
| R1-8 | ch13 :129 | "(chapter 14)" repeats the chapter's earlier pointers | seen |
| R1-9 | ch13 :129, :157, :181 | A long sentence; "tree" in two senses; the tree is trunk's, unsaid | seen |
| R2-1 = N2 | ch14 :228 / :230 | "re-decides it" / "redecidi-la" readable as the review | seen |
| R2-2 | ch14 :229 / :231 | "rewritten on what exists" / "reescrita" readable as the review | seen |
| R2-3 | ch14 :222 to :223 / :224 to :225 | Why a list is no good way out left to inference | seen |
| R2-4 | ch14 :223 / :225 | "dropping the review loses the test" against docs/06 :512 | weak |
| R2-5 | ch15 :18 / :18 | pt "e a revisão com ela": "ela" readable as "uma cancelada" | seen |
| R2-6 | ch14 :224 / :226 | 27 with no source note; the changelog's clause dropped | weak |
| R3-1 | `ch13-apply-next.md` :115 | The note sends a chapter 13 fix to a chapter 14 line; ":154" is the base's line, :155 at the end | seen, held by `ch14-queue-every-milestone` |
| R3-3 | docs/06 :783, :793 | `kit-2026-11-03` "the report lists no migration" while the files are 2026.11.12's; `kit-2026-11-12` `[x]` `· after m37-review` | seen |
| R3-4 | `m36-fixes.md` :42 to :45 | Marks `[>]` the queue never had at a commit | seen |
| R3-5 | `ch13-apply-next.md` :57 | "the kit's file leaves open" a blocked ending: true of 2026.11.03, not of the installed 2026.11.12 | seen |
| R3-6 | ch14 :223 / :225 | "every other line above it" can include the cancelled one | weak |
| R3-7 = L6 | docs/06 :784 | "had stopped naming", "no longer bare sentences" in a queue line | weak |
| R3-8 | `m36-fixes.md` :59 | "freed it" called the changelog's clause ("cleared it"); "keeps every fact" against :77 | seen |
| R3-9 | `ch13-apply-next.md` :89 | "C3, :172 to :194": the passage is :173 to :193 | seen |
| N1 | `ch13-apply-next.md` :115, ch13 :181 | The tree changes once 2026.11.13 is taught | latent, held by `ch14-queue-every-milestone` |
| L1 | ch14 :222 to :224, ch15 :18 | m36-review's M1 and M2 | fixed, both editions; R2-5 is M2's pt residue |
| L3 | ch8 :159 / :160; ch13 :43 | The ending told otherwise | ch8 weak; ch13 :43 in R1-3 |
| L4 | pt ch13 :179, pt ch14 :138 | The script's words in English said twice | weak: each once, in its own chapter |
| L7 | `kit-2026-11-03.md` :3, :12 | "no Delivery review ran", "Chapter 13 still teaches the old ending" | true when written, as ADR-0018 :108 says; no finding |
| L8 | the kit's newest `queue.sh` on the example | Draws milestone 2 and offers `suspension-end` | holds (Mechanical checks); N1's prediction |

**Findings.** By the author's word, every candidate marked seen is confirmed; the weak and latent ones are dropped and listed under small (docs/05 §8). R3-1 and N1 are held by `ch14-queue-every-milestone`, which the driver of this run will widen to cover chapter 13's example tree, since that line's own words name chapter 14 only; they are no findings here.

*Grave*: none. Every clause holds, nothing loses or exposes data, and verify is green.

*Medium*, met in ordinary reading while the clauses hold, each an item of `m37-fixes` by the author's word:

1. M1, R2-1 = N2: chapter 14 en :228, "and the review waits with it until the person re-decides it", pt :230, "e a revisão espera com ela até a pessoa redecidi-la": "it" / "-la" can attach to the review, the nearer noun, both feminine in Portuguese; since `m36-fixes`, :223 / :225 gives the review its own ways out, dropping it or rewriting it, so the reading is the more plausible. It is the twin of m36-review's M2, graded medium and fixed in chapter 15 :18, in the paragraph that teaches the rule. R2-2, the next sentence's "rewritten" in the same place, is small 7; the fix may meet it in passing.
2. M2, R1-7 = L2: chapter 10 en :67 / pt :67, the quick guide's step 6, "You see verify green, ... and your next steps, starting with using what the delivery changed": since `ch13-apply-next` the queue tree is no longer one of the steps but drawn after them unasked, with its `next:`, and the guide a newcomer follows step by step names neither; every `/apply` shows them. M37's clause holds in chapter 13, which the step points to.

*Small*, each a record's precision, a rare case, a wording few meet or a dropped candidate:

3. R1-2: chapter 13 :129 and :192 say the reason twice, "an ending that waited for the question would name no next command" and "An ending that waits to be asked names no next command".
4. R1-3: chapter 13 :128's "Its last words are your next steps" is followed by the tree and the environments (:129); :43 ends on the tree, :195 on the environments.
5. R1-6 = L5: chapter 13 key point :312's "also when it stops blocked; its last words are your next steps ..." lets a reader take the steps and the tree to follow a blocked ending, which :73 and `ch13-apply-next`'s Out of scope leave open; no open line names it (`ch13-apply-findings`' line names only the last message's opening marks).
6. R1-5 = R3-2: pt chapter 13 :128 translates the kit's English quote with no word that the original is English (docs/04 :25), as pt :59 and :207 already did; the delivery recorded the choice.
7. R2-2: chapter 14 en :229 / pt :231's "rewritten on what exists" / "reescrita" readable as the review.
8. R2-5: chapter 15 :18, pt "e a revisão com ela": "ela" readable as "uma cancelada"; "essa linha" steers the reader.
9. R2-3: chapter 14 en :222 to :223 / pt :224 to :225 leaves to inference why a list is no good way out; `m36-fixes`' review saw it and left it.
10. R1-8: chapter 13 :129's "(chapter 14)", once more in a chapter that already points there.
11. R1-9: chapter 13 :129's long first sentence; "tree" for the working tree at :157 and the queue tree at :129 to :193; the example tree is trunk's, unsaid.
12. R3-5: `ch13-apply-next.md` :57's "the kit's file leaves open" a blocked ending is true of 2026.11.03, the version taught, not of the installed 2026.11.12 ("done or blocked").
13. R3-3: docs/06 :783's `kit-2026-11-03` says nothing of the files being 2026.11.12's, and :793's `kit-2026-11-12` is `[x]` with `· after m37-review` open; ADR-0018 and `kit-2026-11-03.md` say how.
14. R3-4: `m36-fixes.md` :42 to :45 gives `[>]` marks the queue never had at a commit.
15. R3-8: `m36-fixes.md` :59 calls "freed it" the changelog's clause, which says "cleared it", and "keeps every fact" against :77.
16. R3-9: `ch13-apply-next.md` :89's "C3, :172 to :194" is one line off at each end.
17. Dropped, weak: R1-1, R1-4, R1-7's chapter 8 and 14 parts, R2-4, R2-6, R3-6, R3-7, L3's chapter 8 part, L4; latent: N1, held.

**The medium pick.** By the author's word quoted above, M1 and M2 enter the one `m37-fixes` line, each an item of its page, which is their list and is not split; no small finding is picked, so none becomes a line (docs/05 §8). The line sits under this review, `· after m37-review · from m37-review`, added with the host's file edit on that one line.

**Decisions taken alone in /apply.** For the author's review.

* R1-7's chapter 10 part is graded medium, as the checker leaned: the quick guide is the one list a newcomer follows step by step, and its step 6 says what the reader sees at the end of `/apply`; the tree and `next:` appear there every time. Chapter 8's and chapter 14's parts are weak and dropped.
* R2-1 = N2 is graded medium, as m36-review graded its twin M2 in chapter 15, so the two chapters are not graded apart for one wording.
* R1-6 is small and held by no line: it needs a blocked `/apply`, and the line nearest it, `ch13-apply-findings`, names only the last message's opening marks.
* R3-1 and N1 are listed as held by `ch14-queue-every-milestone` on the driver's word that it will widen that line; this review does not edit it.
* R1-1 is dropped as weak, as the checker marked it: the reason is said first in the present, and the dated report follows the author's word "Sim, como o changelog".
* PDF pages are counted from each PDF's first page, as `pdftotext` splits them; pt chapter 13 :192's sentence runs from p. 149 to 150.
* The partial reads are accepted: the page asked for chapters 13 to 15 read whole, and reader 2 read chapters 14 and 15 by their range diffs and the passages around them, reader 1 pt chapter 13 by its diff, ranges and a grep; every path of the inventory was read by its range diff at the least, which is what docs/05 §8 asks before a `[?]`, and the checker opened each candidate's file whole at the end commit.
* The readers were asked for the foreground and ran in the background, the host's way; each report reached this session, so no `[?]` was needed.

**Proof.** The mechanical checks and the clause answers above; `make book` at `0e22d1a`; `make verify` green after the last edit to this page and docs/06, 10 to 13 seconds a run, under the five-minute ceiling.

The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

```commit
docs(m37-review): review M37, five clauses hold, two medium fixes

- Base 066b3bf, end 0e22d1a; every clause of M37 holds in both PDFs
- apply/SKILL.md and queue.sh equal to the kit; tree run on chapter 13
- Three readers and a checker: 17 seen, 7 weak, 1 latent, 2 held
- m37-fixes under m37-review with the two medium findings

work/done/m37-review.md
```
