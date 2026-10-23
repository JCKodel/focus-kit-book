# m30-review

**Objective.** The author can decide whether each promise of M30 holds in both editions, having read in both PDFs the passages this page names, and whether everything changed since `ea83160` holds under the code reading by areas, with every confirmed failure recorded as a new line under this review.

**Behaviour.**

* With every line in this review's `after` `[x]`, /apply builds both PDFs at the end commit and gives the author the clause tests below, each with its passages and their start pages in both editions; the author reads them and answers each test: holds, or fails with what the author saw. A clause no delivery answers, or one that fails in the author's hands, is a finding (docs/05 §8).
* On the author's word in the review's /apply session, read-only area readers read one fixed range, `git diff <base>..<end>`, between the base and the end commit below; one checker tests each candidate against that same snapshot and labels it seen, latent or weak before the author sees it (docs/05 §5, Milestone review; §8). The session says it is time and starts the readers only on that word.
* No word of the author for this review is quoted on this page: the command that opened this definition, `/propose m30-review m31-review`, is the word for /propose, not for the reading or the tests. If the author, in the /apply session or relayed to it, gives the word that the review's session take the tests and the confirmation, /apply quotes that word on this page, answers each test from its own reading of the passages in both PDFs, records the answers as the review's, never the author's, and takes the word as the author's confirmation of each candidate the checker marks seen, the latent and weak ones listed as dropped (docs/05 §8, the paragraph on the person's word). Without that word, the author decides which candidates become findings.
* The readers and the checker report back to the review's own session, the one running /apply: the session launches each as a foreground Agent call and receives its final report itself. A checker's marks that reach the session only through a working file or another session's summary are not its report; the session asks the checker again, or the line waits as below. Working files go under the session's scratchpad directory, in its `m30/` folder, and the candidate table in `m30-candidates.md` beside it, then onto this page.
* Each confirmed candidate becomes a `[ ]` line under this review in docs/06, candidates sharing a file or a cause sharing a line; every candidate not confirmed is listed on this page with its mark. No fix is made here.
* A clause with no answer, a required reader that cannot run, a checker whose report does not reach the session, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8); a partial reading that found nothing never closes it.
* A commit made during the reading does not move the end commit; what it changed is named as outside this reading.
* Edge, the sources: the clauses rest on three web pages, not on a kit's history. The chapters reader fetches the three URLs of chapter 22's notes at reading time and records the date; a value that differs from the chapter is a candidate, source drift, named as such, not a clause failure by itself.
* Edge, the fix round: M29's three finding lines, `ch08-other-items-claude-md` (`a4f2cb9`), `ch14-renewal-example` (`6815936`) and `m29-records-claims` (`589f668`), with their define commits (`f443055`, `b4c6228`, `54c819f`), are in the range. They get no second review (docs/05 §8): their paths are read by their area's reader, as one delivery's work against another's, and no clause here tests them. Chapter 8 also holds `book-films`' hunk; its reader reads chapter 8 whole at the end commit.
* Edge, the release: `18cdae4` (`chore(release): v1.2.7`, tagged `v1.2.7`) changes `VERSION` alone, as docs/05 §6 says the release commit does; it is read by the build reader, with no clause, as m22-review and m23-review read theirs.
* Edge, the later milestone: `book-films` (`2e2717b`) is M31's line, committed before this page, so it is inside the range: its paths are read by their area's reader and named as M31's, with no clause here; M31's clauses are m31-review's. m31-review's base, by docs/05 §8, is this review's commit, which comes after `2e2717b`, so `book-films`' code is outside that range unless m31-review's page names another base and why; this reading is then the code reading `book-films` gets, and the page says which of its paths were read. That base is m31-review's decision, not this page's.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree or the index. While this page was written another session was defining `m31-review` beside it, its line in docs/06 and its page `work/m31-review.md` that session's work, not findings here (docs/05 §4).

**Contract.** Clause tests from docs/06's M30 paragraph, each against the named delivery's page in `work/done/` and the cited chapter passages in both PDFs (`output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`). Lines are en / pt at `2e2717b`; where one number is given it is the same in both.

| Clause | Deliveries and passages | The author's test |
|---|---|---|
| A reader of chapter 22 knows that the cache lasts only while the conversation keeps using it | `ch22-cache-lifetime`: chapter 22, the opening's third sentence (:5); "What a host bills" / "O que um host cobra", the multipliers sentence (:25); "How long the cache lasts" / "Quanto tempo o cache dura" (:27 to :45 / :27 to :46), its first paragraph (:29 to :31) and Claude Code's two groups and the settings (:39 to :45 / :39 to :46); key point 5 (:140 / :142); docs/03's `cache lifetime` row (written by its /propose) | Reading only the chapter, can you say how long the host keeps the cache, what renews it, and from when the lifetime counts, with the 4-minute answer that leaves about 1 minute of a five-minute cache? Can you say which lifetime Claude Code gives the main conversation on a subscription within its usage, with an API key, a cloud provider or usage credits, and subagents, and how `promptCacheTtl` and `subagentPromptCacheTtl` change it? Does each edition say the same, with the same numbers in its own format and the term `tempo de vida do cache` alone? |
| A pause past its lifetime makes the next turn rebuild the whole context at the write price instead of reading it at the read price | `ch22-cache-lifetime`: "How long the cache lasts" / "Quanto tempo o cache dura", its second paragraph (:33 to :37), the hour's trade (:44 to :45 / :45 to :46); "How a team decides" / "Como um time decide", the cache write column (:125 / :127); "What the team gains" / "O que o time ganha" (:132 / :134); key point 5 (:140 / :142) | Reading only the chapter, can you say what the first call after a pause past the lifetime pays for its context and why, at 1.25 or 2 times an input token against a read of 0.1, 0.05 or 0.025, and work out the 12.5 to 80 the chapter gives? Is it clear that the jump is in the context, the new text and the answer costing what they always cost? Does the chapter's "call" say what the paragraph's "next turn" promises, a turn's first call being the one that writes? Can you read a rise in the cache write column as the cache rebuilt? Does each edition say the same? |

What the queue line adds beyond M30's paragraph and the tests above, its "tens of times" and its sources' names and access date, has no clause: the chapter 22 reader reads it against the sources (L1, and the record's Divergences on the range 12.5 to 80).

**Base.** `ea83160` (`docs(m29-review): review M29, three findings`), the commit of m29-review, the previous milestone's review (docs/05 §8, docs/03's `milestone review` row). The range therefore also holds M29's fix round, `ch08-other-items-claude-md`, `ch14-renewal-example` and `m29-records-claims`, which gets no second review (docs/05 §8); the release commit of v1.2.7 (`18cdae4`, `VERSION`); and M31's `book-films` (`2e2717b`): the clause tests above are M30's alone, while the readers read the whole range.

**End.** The commit HEAD is when the reading starts; /apply records it before launching any reader, and nothing it records later moves it. Planned: `2e2717b` (`docs(book-films): link the films of focus-kit at work`), HEAD when this page was written; this page's define commit, and `m31-review`'s if it lands first, come after it, so /apply records the actual end and recomputes the inventory there.

**Areas.** The paths `git diff --stat -M ea83160..HEAD` shows today, at `2e2717b` (31 paths, 805 insertions, 56 deletions), by the areas of docs/05 §5's Milestone review slot. /apply recomputes them at its end commit and places any new path in its area:

* **Build** (3 files): `README.md`, `README.pt.md` (`book-films`' two links), `VERSION` (the release), read beside the `Makefile`, `scripts/` and `docs/manuals/release-the-book.md`, which the range does not change.
* **Chapters** (8 files), both editions: `book/{en,pt}/08-install-and-hosts.md` (`ch08-other-items-claude-md` and `book-films`' film note), `14-queue-states.md` (`ch14-renewal-example`), `22-cost-and-where.md` (`ch22-cache-lifetime`, M30's only chapter), and `book/{en,pt}/index.md`, the site's home (`book-films`), placed here because it is `book/` content that both editions render.
* **The kit's skills:** no path; the range changes no skill or script under `.claude/` or `.agents/`, so no reader is planned for it and no comparison with the kit is made.
* **The documents** (3 files): `docs/00-Product.md` (`book-films`' Cases sentence, read against AGENTS.md's non-negotiables on the cases and Case B), `docs/03-Domain.md` (the `cache lifetime` row, `ch22-cache-lifetime`; the `migration` row, `m29-records-claims`), `docs/06-Queue.md`, and this page, `work/m30-review.md`, which the define commit adds.
* **Delivery records**, the 17 paths under `work/done/`: M30's `ch22-cache-lifetime`; M29's fix round, `ch08-other-items-claude-md`, `ch14-renewal-example`, `m29-records-claims`, and the eight pages `m29-records-claims` edited, `ch08-update-2026-10-20-5`, `ch08-update-choice-outcome`, `ch10-12-no-implicit-hosts`, `ch13-16-several-slugs-sessions`, `ch14-after-over-token`, `kit-2026-10-20-5`, `m28-claim-wording`, `m28-records-claims`; M31's `book-films` and its four screenshots, `book-films-home-{en,pt}-{1280,390}.png`.

Count: 3 + 8 + 0 + 3 + 17 = 31.

**Readers.** Three read-only readers on Opus, each keeping the session's advisor, Fable, then one read-only checker on Opus; each launch sets its model to Opus, no other model runs the review, and no agent runs on Fable itself (docs/05 §5, Milestone review). At most two of the review's agents run at a time. Planned, lean:

* pair 1: **chapter 22 and M30** (2 chapter files, docs/03, the `ch22-cache-lifetime` record), whole, with the three sources fetched at reading time, docs/04 on numbers, sources and the gain section, and chapters 23 and 24 by grep for what they say of the cache or the session limit; and **the rest of the chapters, the build and docs/00** (6 chapter files, 3 build files, docs/00, docs/06 and this page), chapters 8 and 14 whole at the end commit, the fix round's and `book-films`' hunks against their pages;
* then, in the first free slot: **records** (16 pages and the four screenshots), the fix round's pages against their Proof and Delivery review and `m29-records-claims`' replacements against its Contract, `book-films`' page against its screenshots. The checker runs alone once the three readers have reported, on every candidate in one report, as m29-review's /apply found best.

Each reader lists the paths it read, and the page records whether each kept the session's advisor, as each agent's own report says it.

**Slow tests.** The Verify slot names none (docs/05 §5); none is invented for this review.

**Known candidates for the checker**, leads to check, not findings. Each names the reader that reads it:

* L1, the notes' dates: all three of chapter 22's notes say accessed 2026-10-22, the queue line's date, while the record says every figure was checked on 2026-10-23 and the sources fetched again then; docs/04 on access dates. Chapter 22 reader.
* L2, chapter 22 :29 / :29, "The host keeps a stored context", against docs/03's `host` row, the program that runs the agent, while the cache is the service's; the point the delivery review noted and left; docs/03's `cache lifetime` row says the same. Chapter 22 reader.
* L3, key point 5 (:140 / :142), "five minutes otherwise", beside the section's three cases (API key, cloud provider, usage credits) and the subagents' five minutes; and "Subagents and most other requests" (:41) against the source's server-controlled helper requests. Chapter 22 reader.
* L4, unsourced claims of the new section: "on a long session is most of what a call sends" (:37), "chosen when the context is written" (:29), and the gain sentence (:132 / :134) carrying no number with a pricing note, against docs/04's **One gain** and **Numbers that prove**, which the record's Divergences cite. Chapter 22 reader.
* L5, the Portuguese-only sentence on the settings' English names (pt :44), against parity and docs/04. Chapter 22 reader.
* L6, `ch22-cache-lifetime`'s record: its Out of scope names "Chapter 25's subscriber passages", while the book ends at chapter 24 and docs/03's `session limit` row names chapter 24; its Delivery review "did not say it consulted an advisor", against docs/05 §5's Delivery review keeping the session's advisor, and its Done when holds no review item, the pattern of m29-review's C8 and C21; its Proof's `make book` names no commit or tree. Records reader.
* L7, chapter 8's film note (:27, :200 / :27, :202) and the home's and READMEs' links against docs/00's new Cases sentence (the book describes neither the project nor what the films run) and the queue line (engineering and business films, the other language's playlist one link away); the two `book-films`' edits to chapter 8 beside `ch08-other-items-claude-md`'s. Chapters, build and docs/00 reader.
* L8, M29's fix-round records against their Proof and Delivery review, the recurring pattern: each Done when tick, each review saying what its agent read and what its report says of the advisor; the thirty-six replacements of `m29-records-claims`' Contract found once each in the eight pages at the end commit, and docs/03's `migration` row against `kit-2026-10-20-5`. Records reader.

**Mechanical checks**, run by /apply at the end commit:

* `git status --short book/` is empty before `make book`, so the PDFs hold the end commit's `book/`; both PDFs contain "How long the cache lasts" / "Quanto tempo o cache dura" and `promptCacheTtl` in chapter 22, and /apply records each chapter's start page in both editions and the start page of each passage the clause table names.
* Chapter 22's headings and note keys are the same in both editions, each key cited as many times; the Portuguese numbers are in its format (`1,25`, `12,5`, `0,025`) and no English `1.25`, `12.5` or `0.025` stands in it; `tempo de vida do cache` is the only Portuguese term for the lifetime.
* The three URLs of chapter 22's notes answer at reading time, the date recorded.
* `git tag --points-at 18cdae4` shows `v1.2.7`, `VERSION` at the end commit reads `1.2.7` and the release commit changes `VERSION` alone; `git branch --list` shows `main` alone (trunk).
* `make verify` and `make book` are rerun by /apply after its last edit; their results here are /apply's, not this page's. A failure caused by another session's uncommitted file is named as that session's; one caused by an external host refusing the connection is named with the link.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit; /apply records the start page of every chapter in both editions.

**Out of scope.**

* Fixing any finding: each becomes its own line (docs/05 §8).
* Re-testing M29's clauses or its findings: m29-review answered the clauses, and the fix round is read by the area readers, not tested by clause.
* M31's clauses and its review: m31-review's; `book-films` is read here, not tested by clause.
* A kit comparison: no skill or script of the kit is in the range.
* A fresh-clone rerun: no script, `Makefile` or manual is in the range.
* Changing the readers' model or the slot: docs/05 §5 owns it.
* The other session's `m31-review` line and page (Behaviour).

**Decisions from the documents.**

* The base is m29-review's commit, the previous milestone's review, the first of docs/05 §8's cases.
* The fix round and the release commit are read by the area readers but have no clause here (docs/05 §8: findings get no second review), as m22-review treated v1.2.5.
* The author tests each clause by hand in both PDFs and confirms candidates, docs/05 §8's default. The author's word for this review, given in the /apply session on 2026-10-23 and relayed to this /apply, quoted as docs/05 §8 asks: asked "m30-review: is it time to start the code reading (three Opus readers, then one checker, on ea83160..2e2717b)?", the author answered "Yes, start now"; asked "Who answers M30's two clause tests (chapter 22 in both PDFs) and confirms the checker's candidates?", the author answered "I do (default)". The first is the word to start the reading; the second gives no word for the review to take the tests or the confirmation, so the author answers each test and decides which candidates become findings.
* The readers start only on the author's word in the /apply session (docs/05 §5's slot, §8's "it costs").
* The end commit and the final path inventory are inputs /apply fixes before reading, not open scope (docs/05 §8).
* The token stays `(--)`: this review reads every page and file above it, so neither its definition nor its build may run beside the lines above it (docs/05 §4), as m29-review's did.
* The queue line's promises beyond M30's paragraph get no clause: §8 takes the milestone's paragraph clause by clause, as m28-review left the Copilot CLI lines to its readers.

**Decisions taken alone.** The agent chose each of these, for the author's review.

* M30's paragraph is taken as two clauses, by what a reader must say: the cache lasts while in use; a pause past it costs a rebuild at the write price. The first carries Claude Code's lifetimes and settings, since they say how long "while in use" lasts on the host the book uses.
* `book/{en,pt}/index.md` sits in the chapters area, being `book/` content both editions render; `README.md` and `README.pt.md` in the build area, as m21-review to m23-review placed them.
* `book-films` is read by this review's readers, named as M31's, as m28-review planned for a later milestone's commit in its range.
* Lean readers, three: chapter 22 with its record and the sources, since its claims are checked against pages, not files; the other chapters with the build and docs/00, small hunks that meet in chapter 8; the records together, the recurring records pattern read in one place. The checker runs alone after them.
* The readers and the checker are foreground Agent calls reporting to the review's session, with the working files in the scratchpad's `m30/` folder and the candidate table in `m30-candidates.md`, following m29-review's practice, where the driver's word set them; here no word sets them.
* The sources are fetched again at reading time, and a difference is source drift, a candidate, not a clause failure: the clause asks what a reader of the chapter knows, the chapter's number being right on the date its note gives.

**Done when.**

* [x] Every line in this review's `after` is `[x]`, and every clause above has an answer, the author's from both PDFs, or, on the author's word quoted on this page, the review's, recorded as the review's.
* [x] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read, whether each agent kept the session's advisor as its report says, that each report reached this session, the sources' fetch date, and every checked candidate with its mark are recorded on this page, the candidate table also in the scratchpad's `m30-candidates.md`.
* [x] Every confirmed candidate is in a `[ ]` line under this review, shared causes sharing a line; every candidate not confirmed is listed with its mark; nothing is fixed here.
* [x] The mechanical checks above are recorded with their results; `make verify` is green after the last edit and `make book` built both PDFs at the end commit, both run by this /apply and recorded in its Proof with the commit and both PDF paths, given to the author.
* [x] No separate Delivery review, a milestone review having none (docs/05 §7, no review of a review); this delivery's paths staged as docs/05 §6 says, the page moved to `work/done/` and its commit message suggested in a `commit` block, which ends the page.

**End commit.** `2e2717b` (`docs(book-films): link the films of focus-kit at work`), HEAD when the reading started, recorded before any reader was launched: the planned end. No define commit was made for this page or for `m31-review`'s, so the page is not in the range: /apply read it from the working tree as the spec, uncommitted, and `git diff --stat ea83160..2e2717b -- work/m30-review.md` is empty. `git log ea83160..2e2717b` holds nine commits: `f443055`, `b4c6228`, `a4f2cb9`, `6815936`, `54c819f`, `589f668`, `18cdae4`, `8ddd77d`, `2e2717b`.

**Inventory at the end commit.** `git diff --stat -M ea83160..2e2717b`: 31 paths, 805 insertions, 56 deletions, the 31 of the Areas above. Build: 3 (`README.md`, `README.pt.md`, `VERSION`). Chapters: 8. Skills: 0. Documents: 3 (`docs/00-Product.md`, `docs/03-Domain.md`, `docs/06-Queue.md`). Records: 17. 3 + 8 + 0 + 3 + 17 = 31.

**Slow tests.** None (docs/05 §5's Verify slot names none).

**Mechanical checks, at `2e2717b`.**

* `git status --short book/` was empty before `make book`, so the PDFs hold the end commit's `book/`; `make book` printed both PDF and both EPUB paths, with two `user-select` warnings from weasyprint. Both PDFs contain "How long the cache lasts" / "Quanto tempo o cache dura" and `promptCacheTtl` in chapter 22 (en 225 and 226 / pt 238 and 239).
* Chapter 22's headings are the same eleven at the same levels in both editions, the Portuguese one line later from "O que o Ninjobs registrou em tokens" (pt :48) on, its settings paragraph holding one more sentence (pt :44, L5). Each note key is cited as many times in both: `anthropic-pricing` 4, `claude-code-prompt-caching` 4, `anthropic-prompt-caching` 1, each with its one definition. The Portuguese edition writes `1,25`, `0,1`, `0,05`, `0,025` and `12,5` (pt :25, :35, :36, :46) and no English `1.25`, `12.5`, `0.025`, `0.05` or `0.1`. Its only term for the lifetime is `tempo de vida` (`tempo de vida do cache` at :29 and :134, `tempo de vida` alone after it), with no `duração`, `validade` or `vida útil` of the cache.
* The three URLs of chapter 22's notes answered 200 on 2026-10-23 at 16:15 (-0300): `https://platform.claude.com/docs/en/about-claude/pricing`, `https://code.claude.com/docs/en/prompt-caching`, `https://platform.claude.com/docs/en/build-with-claude/prompt-caching`.
* `git tag --points-at 18cdae4` shows `v1.2.7`; `VERSION` at `2e2717b` reads `1.2.7 2026-10-21`; `18cdae4` (`chore(release): v1.2.7`) changes `VERSION` alone, one line. `git branch --list` shows `main` alone (trunk). The PDFs carry the unpublished version sentence, the tag not pointing at HEAD, as docs/01's `make book` row says.

**Start pages** (the PDF's printed page numbers, the cover being page 1, from each PDF's outline). Chapters, en / pt: prologue 5 / 5; 1: 11 / 11; 2: 19 / 19; 3: 24 / 24; 4: 40 / 41; 5: 54 / 56; 6: 63 / 65; 7: 68 / 70; 8: 79 / 82; 9: 90 / 95; 10: 99 / 104; 11: 106 / 111; 12: 116 / 122; 13: 127 / 134; 14: 145 / 153; 15: 158 / 167; 16: 167 / 176; 17: 175 / 184; 18: 183 / 192; 19: 194 / 204; 20: 213 / 225; 21: 219 / 231; 22: 224 / 237; 23: 232 / 245; 24: 238 / 251. Passages the clause table names, en / pt, each found in the PDF's text: the opening's third sentence 224 / 237; the multipliers sentence 225 / 238; "How long the cache lasts" / "Quanto tempo o cache dura" 225 / 238, its first paragraph 225 to 226 / 238 to 239, its second paragraph 226 / 239, Claude Code's two groups, the settings and the hour's trade 226 / 239; the cache write column 230 / 243; "What the team gains" / "O que o time ganha" 230 / 243; key point 5 231 / 244.

**Readers and the paths they read.** Three read-only agents on Opus, then one read-only checker on Opus, each launched by this session as a general-purpose agent with its model set to Opus and the brief `m30/brief.md` in the scratchpad, which kept it to `git show 2e2717b:<path>` and `git diff -M ea83160..2e2717b`, the spec excepted, and its working files to the scratchpad's `m30/` folder. Each was called as an Agent call from this session; the host ran each in the background and delivered its final report to this session as its completion notice, the report itself; none reached the session through a file or another session. At most two ran at a time: pair 1 (chapter 22 and M30; the other chapters, the build and docs/00), then the records reader in the slot the chapter 22 reader freed, then the checker alone, on C1 to C24, once the three readers had reported.

* Chapter 22 and M30: both chapter 22 files whole and by range diff; `ch22-cache-lifetime`'s record whole; docs/03 by range diff with its `host`, `token` and `session limit` rows; docs/04 by excerpt (Evidence, Numbers that prove, One gain, A gain per chapter, Source notes); docs/06's M30 paragraph and `ch22-cache-lifetime` line by grep; chapters 23 and 24, both editions, by grep for the cache, its lifetime, the session limit, pauses and idle sessions; the book's other source notes by grep; `git log ea83160..2e2717b`; this page from the tree. The three sources fetched on 2026-10-23 at 19:15 UTC, each HTTP 200, with no drift from the chapter. Its candidates 1 to 7, C1 to C7 here.
* The other chapters, the build and docs/00: `book/en/08-install-and-hosts.md` whole and by range diff, `book/pt/08-install-and-hosts.md` by range diff, excerpts and a whole-file parity script; both chapter 14 files by range diff, excerpts and the script, chapter 13 by excerpt; both `index.md` whole; both READMEs by range diff, headings and their "Read" sections, `scripts/check_parity.py` by grep; `VERSION` whole, `18cdae4` by `--stat` and its tag, the `Makefile`, `scripts/release.py`, `docs/manuals/release-the-book.md` and docs/05 by grep; docs/00 by range diff and its Mechanics section whole, AGENTS.md and docs/03's `case` row by grep; docs/06 by range diff (M29's three lines, M30's and M31's paragraphs and lines but `m31-review`'s) and `git log -p`; `book-films` and `ch14-renewal-example` whole, `ch08-other-items-claude-md` :1 to :90, m29-review's table by grep, as specs; docs/04 by grep; this page whole. The range's six film and playlist URLs answered 200 on 2026-10-23, each playlist holding its language's two films. Its candidates 1 to 5, C8 to C12 here.
* Records: `ch08-other-items-claude-md`, `ch14-renewal-example`, `m29-records-claims`, `ch22-cache-lifetime` and `book-films` whole; the four `book-films` screenshots extracted and viewed; the eight pages `m29-records-claims` edited by range diff, by a script counting each of its 36 replacements before and after, and by excerpts; docs/03 by rows, docs/05 §§3, 5 and 6, m29-review's table, docs/06 at nine commits by grep, the define commits' Done when, commit times and parents; chapters 8, 14 and 22 by excerpt or grep to check a record's claim. Its candidates 1 to 8, split by this session into C13 to C24.

The three lists cover the 31 paths of the inventory; none of the range went unread. On the advisor, as each report says: each of the three readers consulted the advisor once, the chapter 22 reader before writing its report, changing nothing; the other chapters' reader after orientation, adding checks and the numbering of three candidates; the records reader after drafting its candidates, adding checks and precision to three. Whether that advisor was the session's, Fable, the reports do not say.

**Candidates and the checker's marks.** C1 to C7 from the chapter 22 reader, C8 to C12 from the other chapters' reader, C13 to C24 from the records reader; lines at `2e2717b`, en / pt, as the checker corrected them. The checker read each at the end commit, the spec from the tree, fetched the Claude Code page once, and reported to this session as its completion notice; it consulted the advisor once, before its table, which changed C2 from weak to seen, low. The same table is in the scratchpad's `m30-candidates.md`.

| Id | Path:line at 2e2717b | Candidate | Mark |
|---|---|---|---|
| C1 | `book/{en,pt}/22-cost-and-where.md:29`, :34; `docs/03-Domain.md:52`; older use en/pt :19 | "The host keeps a stored context" and "the host writes the whole context again", while ch22 :16 and docs/03 :19 define the host as the program that runs the agent and the source says the cache is server-side | seen |
| C2 | `book/en/22-cost-and-where.md:144` / `book/pt/22-cost-and-where.md:146` | `[^anthropic-prompt-caching]` says accessed 2026-10-22; the record shows that page found and checked on 2026-10-23 (:29, :37, :69, :73, :92); the queue line names only the other two sources | seen, low |
| C3 | `book/{en,pt}/22-cost-and-where.md:5`, :34, :36; `docs/06-Queue.md:692`, :695 | The chapter says "call", never "turn"; the M30 paragraph promises "the next turn"; the chapter never says a turn's first call is the one that writes | seen, low |
| C4 | `docs/03-Domain.md:52` | The `cache lifetime` row's identifier lists `promptCacheTtl` alone and says "its setting", while ch22 :43 names `subagentPromptCacheTtl` too | seen, low |
| C5 | `book/{en,pt}/22-cost-and-where.md:40` | "the one you type in" is narrower than the source's main conversation, which also covers `-p` runs and Agent SDK turns | seen, low |
| C6 | `book/{en,pt}/22-cost-and-where.md:40-41` | The per-account lifetimes and the subagents' five minutes carry no note key at the claim; the key is on :39 (docs/04 :141) | seen, low |
| C7 | `book/en/22-cost-and-where.md:40` vs `book/en/24-asking-for-more.md:135`, `docs/03-Domain.md:53` | Usage credits past the plan (ch22) against the host refusing new turns (ch24) | weak: two plan configurations; neither text excludes the other |
| C8 | `docs/06-Queue.md:701` vs `docs/00-Product.md:28` | M31's paragraph says "real projects", docs/00 "a client project" (M31's) | seen, low |
| C9 | `docs/00-Product.md:27` vs :28 | :27's "only as Case A and Case B" beside :28's third client project | weak: :28 itself says the book links the films and describes neither the project nor what they run |
| C10 | `docs/00-Product.md:28` vs `README.md:15`, `README.pt.md:15`, `book/{en,pt}/index.md:9`, `book/{en,pt}/08-install-and-hosts.md:27` | docs/00 says the book does not describe "what the films run"; each link names it in a phrase, the exception book-films allowed (:11) not in docs/00 (M31's) | seen, low |
| C11 | `work/m30-review.md:38` vs its End commit record (spec, working tree) | The Areas say the define commit adds this page; no define commit was made | seen, low: planned text made stale by the end commit /apply recorded |
| C12 | `work/m30-review.md:46` (spec) | "16 pages and the four screenshots"; the range has 13 pages and 4 PNGs | seen, low |
| C13 | `work/done/ch08-other-items-claude-md.md:118` vs :110, :97 | Ticks "Delivery review as docs/05 §5 says" while its agent did not open docs/04 and called no advisor; Divergences "None" | seen |
| C14 | `work/done/ch08-other-items-claude-md.md:119` vs :107 | Ticks verify after the last edit; the Proof records verify only after the last edit to the chapters | seen, low |
| C15 | `work/done/ch14-renewal-example.md:38-46`, :63, :75 | No Delivery review item; the review called no advisor; Divergences silent (the sub-claim on the order of verify and book is weak) | seen, low |
| C16 | `work/done/ch14-renewal-example.md:54` | Calls `m29-records-claims` one of "the lines above in flight"; at `b4c6228` it was below this line and `[ ]` | seen, low |
| C17 | `work/done/m29-records-claims.md:131` | Calls `ch08-other-items-claude-md` and `ch14-renewal-example` `[~]` when the page was written; both `[x]` before its define commit `54c819f` | seen, low |
| C18 | `work/done/ch22-cache-lifetime.md:52` | Out of scope names "Chapter 25's subscriber passages"; the book ends at chapter 24 | seen, low |
| C19 | `work/done/ch22-cache-lifetime.md:94`, :54-62, :83-88 | The review consulted no advisor, Divergences silent, Done when has no review item | seen, low |
| C20 | `work/done/ch22-cache-lifetime.md:92`; `work/done/book-films.md:42` | `make book` names no HEAD or status of `book/` while two lanes shared the tree, committed 4 seconds apart | seen, low |
| C21 | `work/done/ch22-cache-lifetime.md:94` | "Six candidates, all fixed", while the Portuguese-only sentence was kept | seen, low |
| C22 | `work/done/ch22-cache-lifetime.md:35` vs :29, :69, :92 | Gives "checked again" as the reason for 2026-10-22, while the checks are recorded on 2026-10-23 | seen, low |
| C23 | `work/done/book-films.md:52-61`, :73, :77, :79 (M31's) | No review item, Divergences silent on the advisor, Proof with no HEAD or tree, no States or Visual reference though it changes a screen (docs/05 :57-61, :73-75) | seen, low |
| C24 | `work/done/m28-records-claims.md:136` | The same fact twice in one Done when item, after replacement 13 | seen, low |

Counts: seen 2 (C1, C13); seen, low 20; latent 0; weak 2 (C7, C9).

**Divergences.**

* Behaviour's third item opens "No word of the author for this review is quoted on this page"; the author's word is now quoted under Decisions from the documents, and it gives no word for the review to take the tests or the confirmation, so the item's default holds.
* The Areas' planned text (:38, the page "which the define commit adds"; :46, "16 pages and the four screenshots") is recomputed under End commit and Inventory: no define commit was made, the page is not in the range, and the records are 13 pages and 4 PNGs (C11, C12).
* The page asks for foreground Agent calls; each agent was called as an Agent call from this session and the host ran it in the background, its report reaching this session as its completion notice, as m29-review recorded.
* docs/05 §5 asks every agent to keep the session's advisor, Fable. Each of the four agents says it consulted an advisor once; none says that advisor was the session's, so whether it was is not recorded.
* The author's answers and confirmation were given in the /apply session on 2026-10-23 and relayed to this /apply, which resumed on them; the reading, the checker and the PDFs did not change after the relay.

**The clause answers**, the author's, from both PDFs at `2e2717b`, given in the /apply session on 2026-10-23 and relayed:

* A reader of chapter 22 knows that the cache lasts only while the conversation keeps using it: "Holds".
* A pause past its lifetime makes the next turn rebuild the whole context at the write price instead of reading it at the read price: "Holds".

**Findings**, the candidates the author confirmed. Asked which candidates become findings, with the options "All seen except C11, C12", "Only C1 and C13" and "Book text only", the author chose "Only C1 and C13". Each is its own line under this review in docs/06, the two sharing no file or cause:

* `ch22-cache-service`: C1, chapter 22 and docs/03's `cache lifetime` row having the host keep and write the cache.
* `m30-records-claims`: C13, `ch08-other-items-claude-md`'s record ticking its Delivery review as docs/05 §5 says.

Not confirmed by the author, each with the checker's mark: C2, C3, C4, C5, C6, C8, C10, C11, C12, C14, C15, C16, C17, C18, C19, C20, C21, C22, C23 and C24, seen, low; C7 and C9, weak. None is fixed here.

**The finding lines**, as written in docs/06 after `m30-review`:

```
[ ] ch22-cache-service (PA) chapter 22 and docs/03's cache
    lifetime row say that the service keeps the stored context and
    writes it again after a pause, the host being the program that
    runs the agent (docs/03, chapter 22's own definition) and
    choosing the lifetime per request, in the new section and
    wherever the chapter has the host store the cache; both
    editions · after m30-review
[ ] m30-records-claims (PA) the record of ch08-other-items-claude-md
    holds only what happened: its Delivery review tick matching
    what its agent read and what its report says of the advisor,
    the review without docs/04 or an advisor named in Divergences
    · after m30-review
```

Each is one line in docs/06, wrapped here to fit the page.

**Decisions taken by /apply.** The agent chose each of these.

* The readers' candidates were renumbered by this session, C1 to C24, the records reader's sixth and seventh split into C18 to C23, so the checker and this page use one numbering.
* The slugs: `ch22-cache-service` for C1, named after what the fix says; `m30-records-claims` for C13, as m26 to m29 named their record lines.
* Both lines are `(PA)`: their pages take nothing from each other and they touch different files (chapter 22 and docs/03; `work/done/ch08-other-items-claude-md.md`).
* C1's line names every passage of chapter 22 that has the host store the cache, the older one at :19 included, since the fix is one term used one way.

**Delivery review.** None separate: a milestone review has none (docs/05 §7, no review of a review); the readers and the checker above are its reading.

**Proof.** At the end commit `2e2717b`: the mechanical checks above; `make book` with `git status --short book/` empty, printing `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` with their EPUBs; the start pages above, found in those PDFs' text; the author's clause answers from them. `make verify` exit 0 before the readers started.

**Verify and book after the last edit.** See the line below, written after this page's move to `work/done/`.
`make verify` and `make book` were run after this page's last edit and the line's `[x]`, with `git status --short book/` empty, so the PDFs' `book/` is the end commit's `2e2717b`: both exit 0, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(m30-review): review M30, two findings

- Two clauses answered by the author from both PDFs at 2e2717b
- Three Opus readers over ea83160..2e2717b, one Opus checker
- 24 candidates: 2 seen, 20 seen low, 0 latent, 2 weak
- Two finding lines: chapter 22's host and cache; a record

work/done/m30-review.md
```
