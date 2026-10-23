# m31-review

**Objective.** The author can decide whether M31's promise holds in both editions, having opened the READMEs and the site's home in both languages and read chapter 8's film passage in both PDFs, and whether everything changed since m30-review's commit holds under the code reading by areas, with every confirmed failure recorded as a new line under this review.

**Behaviour.**

* With every line in this review's `after` `[x]` and, by its `(--)` token, every line above it `[x]`, m30-review included, /apply records the base and the end commit, builds both PDFs at the end commit and gives the author the clause tests below, each with its files and lines at the end commit and chapter 8's start page and the page of its film note in both PDFs; the author opens them and answers each test: holds, or fails with what the author saw. A clause no delivery answers, or one that fails in the author's hands, is a finding (docs/05 §8).
* The README and home tests are taken on the files at the end commit and on the site `make serve` builds from them (`http://127.0.0.1:8000/` and its `pt/` page), not on GitHub Pages, which shows `main` only after a push the agent never makes (docs/05 §5, Publish policy).
* On the author's word in the review's /apply session, read-only area readers read one fixed range, `git diff <base>..<end>`, between the base and the end commit below; one checker tests each candidate against that same snapshot and labels it seen, latent or weak before the author sees it (docs/05 §5, Milestone review; §8). The session says it is time and starts the readers only on that word.
* No word of the author for this review is quoted on this page: the command that opened this definition, `/propose m30-review m31-review`, is the word for /propose, not for the reading or the tests. If the author, in the /apply session or relayed to it, gives the word that the review's session take the tests and the confirmation, /apply quotes that word on this page, answers each test from its own reading of the files, the served home and chapter 8 in both PDFs, records the answers as the review's, never the author's, and takes the word as the author's confirmation of each candidate the checker marks seen, the latent and weak ones listed as dropped (docs/05 §8, the paragraph on the person's word). Without that word, the author decides which candidates become findings.
* The readers and the checker report back to the review's own session, the one running /apply: the session launches each as a foreground Agent call and receives its final report itself. A checker's marks that reach the session only through a working file or another session's summary are not its report; the session asks the checker again, or the line waits as below. Working files go under the session's scratchpad directory, in its `m31/` folder, and the candidate table in `m31-candidates.md` beside it, then onto this page.
* Each confirmed candidate becomes a `[ ]` line under this review in docs/06, candidates sharing a file or a cause sharing a line; every candidate not confirmed is listed on this page with its mark. No fix is made here.
* A clause with no answer, a required reader that cannot run, a checker whose report does not reach the session, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8); a partial reading that found nothing never closes it.
* A commit made during the reading does not move the end commit; what it changed is named as outside this reading.
* Edge, the films' code reading: `book-films` (`2e2717b`) lies before the base, so its diff is not in this range. Its paths were read by m30-review's readers, whose page says that reading is the one `book-films` gets and names its paths as M31's. /apply checks m30-review's page in `work/done/` records `book-films`' paths among those read; if it does not, the gap is m30-review's, which could not have reached `[x]` with paths of its range unread (docs/05 §4's fourth waiting case, §8), so /apply stops and reports the contradiction instead of reading them here.
* Edge, a fix of M31's clauses: a finding of m30-review that changes a passage this page names (chapter 8 is the likeliest) moves its line; the clause tests are taken at the end commit, and /apply records the lines there.
* Edge, the links break: a film or playlist that no longer answers fails `make verify`'s link check at `file:line: links: <url>: <reason>`; a film made private or removed still answers 200 (`book-films`' Behaviour), so the author's click on each link, not verify, is the test that it plays.
* Edge, the note's number: the site numbers chapter 8's film note 11 and the PDF numbers it 1 (`book-films`' Decisions taken by /apply); the mismatch is the renderers', not a failure of the clause.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree or the index. While this page was written another session had defined `m30-review` beside it, its line in docs/06 and its page `work/m30-review.md` that session's work, not findings here (docs/05 §4).

**Contract.** Clause tests from docs/06's M31 paragraph, each against `book-films`' page in `work/done/` and the named passages. Lines are en / pt at `2e2717b`; where one number is given it is the same in both; /apply records them again at the end commit.

| Clause | Deliveries and passages | The author's test |
|---|---|---|
| A reader of either edition finds the films that show focus-kit at work on real projects, in the edition's language | `book-films`: `README.md` :15 and `README.pt.md` :15, under "Read" / "Ler"; `book/en/index.md` :9 and `book/pt/index.md` :9, the site's home; chapter 8, §Install / §Instalação, the film sentence (:27) and its note `[^focus-kit-film]` (:200 / :202), in both PDFs; docs/00 §Mechanics, Cases (:28) | On each README and each home, do you find two links, the engineering film and the business film, each opening on YouTube the film of that edition's language, each named by what it shows? In chapter 8 of each PDF, right after the paragraph that ends "approve both." / "aprove os dois.", does one sentence say a film shows this install and the four commands at work, with a note that prints the address of the edition's engineering film? Does any of these passages name or describe the project the films show, its client, the company on screen, or what the films run, against docs/00's Cases sentence? Does each edition say the same, "film" in English and "vídeo" in Portuguese? |
| With the other language's playlist one link away | `book-films`: `README.md` :16 and `README.pt.md` :16; `book/en/index.md` :10 and `book/pt/index.md` :10; chapter 8 holds none, by `book-films`' Out of scope | On each README and each home, is the other language's playlist one link, named by its language and not by its YouTube title, and does it open the two films of that language? Does any link of an edition point to a single film of the other language? |

The queue line's promise beyond M31's paragraph, docs/00's Cases sentence, is tested under the first clause, its negative check; nothing else in the line goes beyond the paragraph.

**Base.** The commit of m30-review, the previous milestone's review (docs/05 §8, docs/03's `milestone review` row): the commit that adds `work/done/m30-review.md`, which does not exist while this page is written. /apply finds it with `git log --diff-filter=A --format='%h %s' -- work/done/m30-review.md`, whatever subject the person gave it, and records its hash and subject here before launching any reader. If that returns nothing, m30-review is `[x]` but not yet committed, since the person commits after /apply marks `[x]` (docs/05 §2): /apply stops and asks the author to commit it, and every `[x]` line of M30's fix round still uncommitted, before this reading, the range having to hold the fix round's commits. If it returns more than one commit, /apply stops and reports instead of choosing.

Why this base and not `8ddd77d`, so that `book-films`' own commit would be in M31's range: docs/05 §8 names another commit only "where no earlier review exists", and one will exist, since this line's `(--)` token holds its /apply until every line above it, m30-review included, is `[x]` (docs/05 §4). The smaller range loses nothing: `book-films` was read by m30-review's readers (Behaviour, the films' code reading). A base at `8ddd77d` would cost twice: it would read `book-films` a second time, and it would put m30-review's own commit and page inside M31's range, a reading of a review, which docs/05 §7 excludes and no earlier review's range has held, every base so far being a review's commit, which the diff leaves out. The agent chose this reading from the documents; the author overturns it in the review if `book-films` is to be read inside its own milestone's range whatever it costs.

The range therefore holds M30's fix round, the lines m30-review's findings become, which get no second review (docs/05 §8); no define commit was made for those lines or for this page, so none is in it (End commit); the clause tests above are M31's alone, while the readers read the whole range.

**End.** The commit HEAD is when the reading starts; /apply records it before launching any reader, and nothing it records later moves it. This page's define commit may land before or after the base: m30-review's page anticipates both orders. If it lands before, it lies outside the range and the readers read `work/m31-review.md` at the end commit beside the range; if after, it is inside.

**Areas.** Planned, since the range does not exist yet: /apply runs `git diff --stat -M <base>..<end>` at its end commit, records every path and places each in an area of docs/05 §5's Milestone review slot:

* **Build:** a path of the `Makefile`, `scripts/`, `README.md`, `README.pt.md`, `VERSION` or `docs/manuals/` that M30's fix round or a release touches; a release commit changing `VERSION` alone is read with no clause, as m30-review reads `18cdae4`.
* **Chapters:** `book/{en,pt}/` paths of M30's fix round, `book/{en,pt}/index.md` included, read whole at the end commit where they hold a passage of the clause table.
* **The kit's skills:** a path under `.claude/` or `.agents/`; none is expected, and with none no reader is planned for it and no comparison with the kit is made.
* **The documents:** `docs/` paths, `docs/06-Queue.md` among them, and the records under `work/done/` of M30's fix round; this page, uncommitted, was read from the working tree beside the range (End commit).

**Readers.** Read-only readers on Opus, each keeping the session's advisor, Fable, then one read-only checker on Opus; each launch sets its model to Opus, no other model runs the review, and no agent runs on Fable itself (docs/05 §5, Milestone review). At most two of the review's agents run at a time. Planned, lean, by what the range holds at the end commit:

* if M30 had findings: one reader for their chapter and build paths against their pages, with chapter 8 whole at the end commit where it is among them; one for their records and the documents, docs/06 and this page included; the two run as a pair;
* if M30 had none: the range holds docs/06 and this page alone (the define commit) and one reader reads them;
* an area too large for one careful reading splits again (docs/05 §8). The checker runs alone once the readers have reported, on every candidate in one report, as m29-review's /apply found best.

Each reader lists the paths it read, and the page records whether each kept the session's advisor, as each agent's own report says it.

**Slow tests.** The Verify slot names none (docs/05 §5); none is invented for this review.

**Known candidates.** None planned for the checker. One lead is /apply's own, before any reader: L1, whether m30-review's page records `book-films`' thirteen paths as read, and what its readers reported of them (its L7), as Behaviour says; a gap is reported, not read here.

**Mechanical checks**, run by /apply at the end commit:

* `git status --short book/` is empty before `make book`, so the PDFs hold the end commit's `book/`; both PDFs contain the film sentence and the address of the edition's engineering film in chapter 8, and /apply records chapter 8's start page and the page of the note in both editions.
* `git show <end>:README.md`, `README.pt.md`, `book/en/index.md` and `book/pt/index.md` hold the six URLs of `book-films`' Contract, each edition its own two films and the other language's playlist, and no film URL of the other language.
* `git branch --list` shows `main` alone (trunk).
* `make verify` and `make book` are rerun by /apply after its last edit; their results here are /apply's, not this page's. A failure caused by another session's uncommitted file is named as that session's; one caused by an external host refusing the connection is named with the link.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit, and the home served by `make serve` at it; `book-films`' four screenshots in `work/done/` show the home as built.

**Out of scope.**

* Fixing any finding: each becomes its own line (docs/05 §8).
* Re-testing M30's clauses or its findings: m30-review answers the clauses, and the fix round is read by the area readers, not tested by clause.
* `book-films`' code reading: m30-review's (Base).
* A kit comparison: no skill or script of the kit is expected in the range.
* Whether a film plays or still holds what it showed: the films live on YouTube, the author's; the author's click is the test (Behaviour).
* Changing the readers' model or the slot: docs/05 §5 owns it.
* The other session's `m30-review` line and page (Behaviour).

**Decisions from the documents.**

* The base is m30-review's commit, the first of docs/05 §8's cases, named by its subject since its hash does not exist yet (Base).
* The author tests each clause by hand and confirms candidates, docs/05 §8's default: no word of the author for this review exists to quote, and a word holds only for the review whose page quotes it.
* The readers start only on the author's word in the /apply session (docs/05 §5's slot, §8's "it costs").
* The end commit and the path inventory are inputs /apply fixes before reading, not open scope (docs/05 §8).
* The token stays `(--)`: this review reads every page and file above it (docs/05 §4), as m30-review's does.

**Decisions taken alone.** The agent chose each of these, for the author's review.

* The base at m30-review's commit and not `8ddd77d`, with the reasons under Base.
* M31's paragraph is taken as two clauses, by what a reader must find: the films in the edition's language; the other language's playlist one link away. "On real projects" is tested as the first clause's negative check, against docs/00's Cases sentence, since the book promises the films and must describe no project.
* The README and home tests are taken on the files and the site `make serve` builds, not on GitHub Pages.
* Lean readers, planned by what M30's fix round holds, since the range is unknown.
* The readers and the checker are foreground Agent calls reporting to the review's session, with the working files in the scratchpad's `m31/` folder and the candidate table in `m31-candidates.md`, following m29-review's and m30-review's practice.

**Done when.**

* [x] Every line in this review's `after` is `[x]`, and every clause above has an answer, the author's, or, on the author's word quoted on this page, the review's, recorded as the review's.
* [x] Base, end commit, the inventory of paths by area, the slow tests (none), what m30-review's page records of `book-films`' paths, each reader's paths read, whether each agent kept the session's advisor as its report says, that each report reached this session, and every checked candidate with its mark are recorded on this page, the candidate table on this page alone, the scratchpad having gone during the session (Divergences).
* [x] Every confirmed candidate is in a `[ ]` line under this review, shared causes sharing a line; every candidate not confirmed is listed with its mark; nothing is fixed here.
* [x] The mechanical checks above are recorded with their results; `make verify` is green after the last edit and `make book` built both PDFs at the end commit, both run by this /apply and recorded in its Proof with the commit and both PDF paths, given to the author.
* [x] No separate Delivery review, a milestone review having none (docs/05 §7, no review of a review); this delivery's paths staged as docs/05 §6 says, the page moved to `work/done/` and its commit message suggested in a `commit` block, which ends the page.

**The author's word.** Asked in this /apply session on 2026-10-23 "Who answers the two clause tests (READMEs, served home en/pt, chapter 8 p.80 en / p.83 pt) and confirms candidates?", the author chose "The session takes them", the option that read: "Your word, quoted on the page, lets the session answer the tests from its own reading (recorded as the review's) and confirms every candidate the checker marks seen." Asked in the same question set whether to start the code reading, the author chose "Start now (Recommended)".

**Base.** `a961be3` (`docs(m30-review): review M30, two findings`), the one commit `git log --diff-filter=A --format='%h %s' -- work/done/m30-review.md` returns.

**End commit.** `bc6fa75` (`docs(ch22-cache-service): keep the cache where the model runs`), HEAD when the reading started, recorded before any reader was launched. `git log a961be3..bc6fa75` holds two commits, `9c65001` (`m30-records-claims`, 17:15:29) and `bc6fa75` (`ch22-cache-service`, 17:16:41). No define commit was made for this page or for the two fix lines: this page is uncommitted, in no range, and the readers read it from the working tree as the spec.

**Inventory**, `git diff --stat -M a961be3..bc6fa75`, 7 paths:

* **Build:** none.
* **Chapters:** `book/en/22-cost-and-where.md`, `book/pt/22-cost-and-where.md` (`ch22-cache-service`); no passage of the clause table, so chapter 8 is not among them.
* **The kit's skills:** none; no reader planned, no kit comparison.
* **The documents:** `docs/03-Domain.md` (the `cache lifetime` row), `docs/06-Queue.md` (M30's two fix lines), `work/done/ch08-other-items-claude-md.md` (edited by `m30-records-claims`), `work/done/ch22-cache-service.md`, `work/done/m30-records-claims.md`; and this page, from the working tree.

**Slow tests.** None: the Verify slot names none.

**L1, `book-films`' code reading.** `work/done/m30-review.md` records all thirteen of `2e2717b`'s paths as read (:130 for the READMEs, both `index.md`, chapter 8, docs/00 and docs/06; :131 for `book-films`' page and its four screenshots) and its readers' candidates on them (C10, C23, both seen, low, not confirmed by the author). No gap: nothing of `book-films` is read here.

**Mechanical checks**, at `bc6fa75`:

* `git status --short book/` empty before `make book`; `make book` exit 0, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` with their EPUBs. Chapter 8 starts on page 79 (en) and 82 (pt); the film sentence, right after "approve both." / "aprove os dois.", and its note 1 with `https://youtu.be/Ywp1iUtEVyY` / `https://youtu.be/r0fk_yVHgO4` are on page 80 (en) and 83 (pt), found in the PDFs' text.
* `git show bc6fa75:` of `README.md` :15-16 and `book/en/index.md` :9-10 hold `Ywp1iUtEVyY`, `4cqpi5CfnVc` and the Portuguese playlist `PLd13b_CIAdxo`; `README.pt.md` :15-16 and `book/pt/index.md` :9-10 hold `r0fk_yVHgO4`, `gnLcNYOI2MU` and the English playlist `PLCoT-CR09np8`; no film URL of the other language in either. Chapter 8 holds only its edition's engineering film (en :200, pt :202), the sentence at :27 in both.
* `git branch --list`: `main` alone.
* `make verify` exit 0 before the readers started.

**The clause answers**, the review's, on the author's word above, from this session's reading at `bc6fa75` of the files, the home `make serve` built (`http://127.0.0.1:8000/focus-kit-book/` and its `pt/`, the root redirecting there) and chapter 8 in both PDFs; each film's title read through YouTube's oEmbed and each playlist's films from its page on 2026-10-23:

* A reader of either edition finds the films that show focus-kit at work, in the edition's language: holds. Each README and each home has two links, the engineering film and the business film, each opening that edition's film ("focus-kit in practice: coding agents with a process (engineering)" and "... AI for project management, no code (business)"; "focus-kit na prática: agentes de código com processo (engenharia)" and "... IA para gestão de projetos, sem código (negócio)"), each named by what it shows in a parenthesis. In chapter 8 of each PDF, right after "approve both." / "aprove os dois.", one sentence says a film shows this install and the four commands at work, its note printing the edition's engineering film. No passage names or describes the project the films show, its client or the company on screen; the parentheses say what of the kit each film shows, which m30-review's C10 set against docs/00's "nor what the films run", not confirmed there. English says "film", Portuguese "vídeo", the same in both.
* With the other language's playlist one link away: holds. Each README and each home has one link to the other language's playlist, named "the Portuguese playlist" / "a playlist em inglês", not by its YouTube title; `PLd13b_CIAdxo` holds `r0fk_yVHgO4` and `gnLcNYOI2MU`, `PLCoT-CR09np8` holds `4cqpi5CfnVc` and `Ywp1iUtEVyY`. No link of an edition points to a single film of the other language.

Whether each film plays was not clicked: oEmbed answering with its title says the film is public, not that it plays (Behaviour, the links break).

**Readers.** Two read-only readers on Opus, run as a pair, then one read-only checker on Opus, alone; each launched from this session as an Agent call with its model set to Opus, the host running it in the background, its final report reaching this session as its completion notice. Each says it called the advisor tool once and that the tool does not name its model, so whether it was the session's, Fable, is not recorded.

* Chapter 22: both chapter files whole at `bc6fa75` and by range diff; `work/done/ch22-cache-service.md` whole; `work/done/m30-review.md` :125-222 by grep; `work/done/ch22-cache-lifetime.md`, docs/03's `host`, `cache lifetime` and `service` rows, docs/04, both chapters for dashes and the Portuguese one for "serviço", `book/` for "cache", all by grep; AGENTS.md from its context; Claude Code's prompt caching page and Anthropic's pricing page fetched on 2026-10-23. Its candidates CA and CB, C1 and C2 here.
* Records and documents: the range diff of docs/, `book/` and ch08's record; `work/done/ch22-cache-service.md` and `work/done/m30-records-claims.md` whole; ch08's record :84-131, `work/done/m30-review.md` :1-3 and :139-215, docs/05 by sections, docs/06 :686-708, both `index.md` whole, both READMEs :13-18; chapters 8, 22, 23 and 24, docs/00, docs/03, docs/04, `book-films` and `m29-records-claims` by grep; `f443055` and `a4f2cb9` of ch08's record by line; this page whole from the working tree with `git diff -- docs/06-Queue.md`; Claude Code's prompt caching page fetched. Its candidates C-a to C-h and two weak ones, C3 to C10 and C11 here, its second weak one being C1.

Every path of the range was read by at least one reader.

**Candidates**, renumbered by this session, checked by the checker against `bc6fa75` (this page from the working tree):

| # | Where | Claim | Mark |
|---|---|---|---|
| C1 | `book/{en,pt}/22-cost-and-where.md:29` vs `docs/03-Domain.md:52`, `work/done/ch22-cache-service.md:30`, :43 | The chapter keeps the cache "on the cloud provider's when you reach the model through one"; its source puts Claude Platform on AWS on Anthropic's infrastructure, as docs/03's "the cloud provider's that serves the model" allows | seen |
| C2 | `book/{en,pt}/22-cost-and-where.md:30`, `docs/03-Domain.md:52` | "The host chooses" the lifetime per request, said of every host, sourced only from Claude Code's page; M30's page put other hosts out of scope | seen |
| C3 | `work/done/ch22-cache-service.md:72` vs :57 | Proof's `make book` with no HEAD, `book/` status or PDF paths, while the parallel lane, 72 s away in one tree, recorded all three | seen, low |
| C4 | `work/done/ch22-cache-service.md:55`, :78 | Delivery review tick in C13's form, restating docs/05 §5 on the advisor instead of what the report said | seen |
| C5 | `work/done/ch22-cache-service.md:14`, :25 | Cites chapter 22 ":38", blank at the base; the sentence is at :39 | seen, low |
| C6 | `work/done/m30-records-claims.md:26` | Cites m30-review ":183", a blank line; the bullets are :181-182 | seen, low |
| C7 | `9c65001`'s body, `work/done/m30-records-claims.md:81-82` | A body bullet wrapped onto two lines, against docs/05 §6's one-line bullets | seen, low |
| C8 | `work/m31-review.md:34`, :36, :43, :48 | The page relies on define commits that were not made and lists itself among the range's paths | seen, low |
| C8' | `docs/06-Queue.md:707` | `[>]` should have been committed before /apply | weak |
| C9 | `docs/06-Queue.md:697` vs `docs/03-Domain.md:63` | `ch22-cache-service`'s line says "the service keeps", docs/03's FOCUS term, which its own page refuses for the chapter | seen, low |
| C10 | `work/done/ch22-cache-service.md:63` vs `docs/03-Domain.md:4` | Restates docs/03's header as "used with no other meaning"; it says "uses it and no synonym" | seen, low |
| C11 | `work/done/ch22-cache-service.md:26`, :65 | Attributes to docs/04 more than it says of the access date and the key | weak |

Counts: seen 3 (C1, C2, C4); seen, low 7 (C3, C5, C6, C7, C8, C9, C10); latent 0; weak 2 (C8', C11).

**Findings**, the candidates the checker marks seen, confirmed by the author's word above; candidates sharing a file or a cause share a line:

* `ch22-cache-route-host`: C1 and C2, chapter 22 :29-30 and docs/03's `cache lifetime` row, which both hold.
* `m31-records-claims`: C3 to C10 but C8', the records not holding what happened, and `ch22-cache-service`'s queue line, the same delivery's record of what it did.

Dropped, weak, on the author's word: C8' and C11. None is fixed here.

**The finding lines**, as written in docs/06 after `m31-review`:

```
[ ] ch22-cache-route-host (PA) chapter 22 says where the cache
    lives by the infrastructure that serves the model, as docs/03's
    cache lifetime row and its source say, Claude Platform on AWS
    included, and says that the lifetime is chosen per request of
    the host its source names, Claude Code, in the chapter and the
    row; both editions · after m31-review
[ ] m31-records-claims (PA) the records of ch22-cache-service,
    m30-records-claims and m31-review hold only what happened:
    make book with its HEAD, tree and both PDF paths, the Delivery
    review tick saying what its agent read and what its report says
    of the advisor, line numbers as they were, docs/03 restated as
    it says, a commit body of one-line bullets, the define commits
    that were not made, and ch22-cache-service's line without
    docs/03's FOCUS term service · after m31-review
```

Each is one line in docs/06, wrapped here to fit the page.

**Divergences.**

* The page asks for the working files in the session's scratchpad and the candidate table also in `m31-candidates.md`; the scratchpad went away during the session, after the readers launched, so no reader wrote notes and the table is on this page alone. The Done when item is reworded to say so.
* The page asks for foreground Agent calls; each agent was called from this session and the host ran it in the background, its report reaching this session as its completion notice, as m29-review and m30-review recorded.
* docs/05 §5 asks every agent to keep the session's advisor, Fable; each report says it consulted an advisor once and cannot name its model, as m30-review recorded.
* End (:36) foresaw this page's define commit before or after the base, and Readers' second case (:48) a range holding it; neither happened, and no define commit was made for M30's fix lines either, whose pages first entered git with their own commits, `9c65001` and `bc6fa75` (End commit, C8); `m31-records-claims` gave Base (:34) and Areas (:43) what happened.
* "No word of the author for this review is quoted on this page" (Behaviour) no longer holds: the word is quoted above.

**Decisions taken by /apply.** The agent chose each of these.

* The readers' candidates renumbered C1 to C11 by this session, the records reader's second weak one merged into C1, its C-f split by the checker into C8 and C8'.
* "Seen, low" counted as seen for the word's confirmation, as docs/05 §8 has three marks and "low" is the checker's note of consequence.
* Two lines: C1 and C2 share chapter 22 :29-30 and docs/03's row; C3 to C10 share the cause, records of the fix round and of this review not holding what happened, C9 being the same delivery's queue line. Slugs `ch22-cache-route-host`, after what the fix says, and `m31-records-claims`, as m26 to m30 named their record lines; both `(PA)`, touching different files.

**Delivery review.** None separate: a milestone review has none (docs/05 §7, no review of a review); the readers and the checker above are its reading.

**Proof.** At the end commit `bc6fa75`: the mechanical checks above; `make book` with `git status --short book/` empty, printing `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` with their EPUBs; the start pages above, found in those PDFs' text; the home served by `make serve` at `http://127.0.0.1:8000/focus-kit-book/` and `pt/`. `make verify` exit 0 before the readers started.

**Verify and book after the last edit.** See the line below, written after this page's move to `work/done/`.
`make verify` and `make book` were run after this page's last edit and the line's `[x]`, with `git status --short book/` empty, so the PDFs' `book/` is the end commit's `bc6fa75`: both exit 0, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(m31-review): review M31, two findings

- Two clauses answered by the session on the author's word
- Two Opus readers over a961be3..bc6fa75, one Opus checker
- 12 candidates: 3 seen, 7 seen low, 0 latent, 2 weak
- Two finding lines: chapter 22's cache route and host; records

work/done/m31-review.md
```
