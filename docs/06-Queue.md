# Queue

`[ ]` not yet defined · `[>]` defined, `work/<slug>.md` exists · `[x]` done, page in `work/done/`.
A line never leaves; it changes mark.

## M1. The book stands up

When this milestone closes, a chapter written in both languages builds into the website and into PDF and EPUB, `make verify` guards the build, the parity of the editions, the prose and the disclosure list, `main` publishes itself to GitHub Pages, a tag produces a Release, and the brownfield project is chosen.

```
[x] site-skeleton          MkDocs Material bilingual site, one placeholder chapter per edition, draft marker, make serve and make verify (strict build, parity, em dash)
[x] license-and-readme     AGPL-3.0 for scripts and code, CC BY-SA 4.0 for the text; README in English and Portuguese
[x] disclosure-scan        make scan against the out-of-repo disclosure list, locally and in Actions, part of make verify
[x] prose-rules            the anti-AI prose rules written in docs/04 and checked by make verify
[x] link-check             external links in the book checked, part of make verify (the strict build already fails on broken internal links)
[x] chapter-template       the chapter shape fixed, proven by chapter 1, Why process, written in both editions
[x] pdf-epub               make book produces PDF and EPUB in both editions from the same source
[x] pages-and-release      Actions publish the site on push to main and a Release with PDF and EPUB on a v* tag
[x] brownfield-research    three to five open-source candidates compared; the author picks one (OD-1); fork and tag
```

## M2. Part I, Foundations

When this milestone closes, a reader who has never followed a process knows why product, people and process decide a project built with agents, why a coding agent needs written context, what Spec-Driven Development is, and why focus-kit exists.

```
[x] product-people-process Prologue: product, people and process (Marcus Lemonis's three P's) applied to software built with agents, each pointed to the part of the book that answers it; Case B in one sentence
[x] how-agents-see         Chapter 2: statelessness, context window, context rot, fresh sessions, from primary sources
[x] spec-driven-run        Spec Kit, OpenSpec and focus-kit run on the same feature and brief; files, lines and words counted and committed for chapter 3
[x] spec-driven            Chapter 3: SDD, what Spec Kit and OpenSpec got right and where they weighed too much
[x] birth-of-focus-kit     Chapter 4: why Ninjobs left OpenSpec, and the process that became focus-kit
```

## M3. Part II, The focus-kit method

When this milestone closes, a reader can install the kit, document a new or an existing project, and deliver a milestone with `/propose` and `/apply`, following the guided project.

```
[x] guided-project-repo    the guided project's public repository, name chosen (OD-2), a tag per chapter
[x] commit-hooks           pre-commit and commit-msg hooks run the disclosure list on staged files and messages; make verify checks the history's messages
[x] install-and-hosts      Chapter 5: install, update, and how each host invokes the commands; Claude Code shown running, Copilot and Codex from their cited documentation, and why the hosts are alike enough that the method does not depend on one
[x] the-documents          Chapter 6: docs/00 to 06, ADRs, AGENTS.md, and why documents do the work
[x] brainstorm             Chapter 7: /brainstorm on the guided project, and choosing a stack by what the agent knows (the Ninjobs lesson of chapter 4)
[x] analyze                Chapter 8: /analyze on the brownfield project
[x] two-choices            Chapter 6 gains "The two choices": FOCUS (four pieces, whole / two principles / neither) and git (trunk / branch / worktree) in a paragraph each, so chapters 7 and 8 point back to them; Parts III and IV still teach them
[x] queue-and-milestones   Chapter 9: the queue, the marks, milestones and their paragraphs
[x] propose                Chapter 10: /propose, one page, reading it before /apply, and splitting what does not fit
[x] apply                  Chapter 11: /apply, verify, proof, documents, stage, never commit
[x] clinic-milestone-1     the guided project's milestone 1 built line by line with /propose and /apply, each page and staged change reviewed and committed by the author, recorded; no chapter
[x] closing-a-milestone    Chapter 12: the whole-milestone review of the clinic's milestone 1 with /code-review, findings become queue lines; Ninjobs' milestone review as the counter-example
[x] useful-notes           a source note only where the reader gains something to open: notes on a commit or on focus-kit's files leave (the sentence names the file), a private case keeps one note per chapter saying how its numbers were counted; a source cited several times in a chapter prints one note in the PDF and the EPUB, not one per mention (191 notes over 13 chapters); notes smaller and in italic, links upright; parity checks note keys; docs/04, docs/03, docs/01 and AGENTS.md say the new rule; both editions
[x] the-governor           Chapter 13: which concrete error would it have caught, and what the process does not have
[x] m3-review              the review of M3 as docs/05 §8 says: the Prologue to chapter 13 read end to end in both editions against the product questions and M3's paragraph; each confirmed finding becomes a line in a new milestone M3.1
```

## M3.1. What the review of M3 found

When this milestone closes, every confirmed finding of the M3 review is settled: from the Prologue to chapter 13, each chapter explains or points to every term, file and tool it relies on, keeps the promise of its opening, says each thing once, and means the same in both editions; and a reader following the guided project is told to build the rest of milestone 1 with `/propose` and `/apply`, with a tag to compare it against.

```
[x] ch1-openspec-pointer   Chapter 1: the Ninjobs count of OpenSpec changes and lines of spec says what they are, or points to chapter 3, where OpenSpec is explained, not only to chapter 4; both editions
[x] ch3-docs-pointer       Chapter 3: the edits to docs/03 and docs/06 say what those documents are, or point to chapter 6; both editions
[x] ch4-rule-failures      Chapter 4: every rule of focus-kit names the failure it answers, as the opening promises; "A queue" and "The agent never commits" have none today; both editions
[x] ch4-adr-docs05         Chapter 4: ADRs and docs/05 are said in a few words where they appear, with a pointer to chapter 6; both editions
[x] ch5-prompt-file-en     Chapter 5: the English gains the sentence that explains the prompt file's last line, which today exists only in the Portuguese
[x] ch6-placing-a-fact     Chapter 6: the reader places one new fact in the document that owns it, in the text and in an exercise, as the opening promises; both editions
[x] ch6-section-reference  Chapter 6: the docs/04 description names "Living documents" instead of "section 6", which reads as docs/04's own section; both editions
[x] pt-stage-term          Portuguese edition: one term for git's stage from chapter 4 on, where chapters 4 to 6 say "prepara" and chapter 7 on says "coloca em stage"
[x] ch8-tag-form           Chapter 8: says why the brownfield project's tag is book-v1-analyze and not the book-v1/<chapter-slug> of chapter 5; both editions
[x] ch8-accept-edits       Chapter 8: says what acceptEdits is and whether a reader in an interactive session meets the same gap; both editions
[x] ch9-what-apply-reads   Chapter 9: the sentence whose "It" has no clear antecedent says plainly what tells /apply the page exists; both editions
[x] ch10-unit-of-work      Chapter 10: "One unit of work" points to chapter 9 instead of repeating its paragraph on trunk and the waiting page; both editions
[x] ch10-usage-share       Chapter 10: the /usage percentages say what they are a share of, so the ratio drawn from them can be judged; both editions
[x] headless-runs          Chapters 7, 11 and 12: say the book's runs are headless, what --continue does, and that in an interactive session the reader keeps talking in the same session; both editions
[x] ch11-unticked-item     Chapter 11: says why the skeleton page was committed with its npm run dev item unticked, against its own question on Done when; both editions
[x] ch11-commit-command    Chapter 11: shows the command that commits the staged change with the suggested message; chapter 17 teaches the rest; both editions
[x] milestone-1-bridge     Between chapters 11 and 12: the reader is told to build the rest of the clinic's milestone 1 with /propose and /apply, with a tag to compare against, so M3's paragraph has somewhere to point; both editions
[x] ch12-numbered-findings Chapter 12: the English list of the ten summaries is numbered, as the decisions and the Portuguese already are
[x] ch13-unmet-terms       Chapter 13: "spec delta" and "specialized subagent" are explained where they appear, since no earlier chapter meets them; both editions
```

## M4. Part III, FOCUS architecture

When this milestone closes, a reader can organize code by feature with exceptions as values, and knows when the four pieces pay their way and when they do not.

```
[x] errors-and-slices      Chapter 14: exceptions as values and vertical slices, the two principles that stand alone
[x] four-pieces            Chapter 15: View, Orchestrator, Use Case, Repository, one table and one flow, and when the four pieces pay their way
[x] clinic-orchestrator-tests  The clinic's client orchestrators become plain functions that receive their repositories, each with unit tests with fakes, by a recorded run
[x] four-pieces-injection  Chapter 15 at the clinic's tested orchestrators: the client orchestrator's two files, and injection only where a test passes a second implementation, a fake
[x] testing-and-agents     Chapter 16: testing each piece, and how the architecture helps an agent
[x] kit-milestone-review   focus-kit bff8414 reinstalled in the book, the clinic and the fork; each docs/05 says the review is the last line of every milestone and its findings open <M>.1; every open milestone of the three queues ends with its review line; the clinic's findings milestone becomes 1.1 and "the owner runs the day" milestone 2
[x] kit-milestone-review-chapters  Chapters 7, 8, 9 and 12 follow focus-kit bff8414: the review is the last line of every milestone, a delivery run with /propose and /apply that checks the paragraph clause by clause and reviews the code; each confirmed finding is a line in a new milestone <M>.1 right after, which ends with its own review and may open .2; /brainstorm and /analyze end the first milestone with it; chapter 12's quote of §8 follows, and chapters 12, 13, 14 and 15 name the clinic's milestones 1.1 and 2 as renamed by kit-milestone-review; both editions
[x] m4-review              the review of M4 as docs/05 §8 says: the Prologue to chapter 16 read end to end in both editions against the product questions and M4's paragraph; each confirmed finding becomes a line in a new milestone M4.1; §8 gains the review's recipe, m3-review being the first occurrence
[x] m4-code-review         /code-review of the clinic's code from book-v1/closing-a-milestone to book-v1/four-pieces; each confirmed finding becomes a line in M4.1
```

## M4.1. What the review of M4 found

When this milestone closes, every confirmed finding of the M4 review is settled: chapter 3's key points say what its run showed; Part III says what makes one feature and whether a slice may use another slice's code, and its definitions of a refusal, an error, a unit test and injection fit the clinic's code it shows; chapter 14 tells an error from an exception in any language, says why a throw must not steer the flow, and keeps a library's exceptions out of the domain; it shows a piece that has a job and still costs more than it gives; every excerpt can be followed from its text; a reader following the guided project is told to build the code that chapter 15's tag holds; the clinic's client orchestrators publish every in-flight state as an update of the current state, send the weekly hours editor's reports through one tested event, declare each repeated type once, and take only the event shapes its docs/01 describes; and the Portuguese edition means what the English means.

```
[x] ch3-key-point-ask      Chapter 3: the key point credits only OpenSpec with a question asked before writing, since the run shows Spec Kit asked nothing on its default path; both editions
[x] pt-slot-term           Portuguese edition: a slot of the slotMinutes grid gets its own term, apart from "horário livre" (a free slot), in chapter 6's excerpts of invariant 2 and ADR-0005
[x] ch14-feature-boundary  Chapter 14: says what makes one feature, and why the appointments slice holds cancelling while weekly hours and professionals have slices of their own; both editions
[x] ch14-refusal-io        Chapter 14: the definition of a refusal and its key point fit SlotTaken, the refusal the repository makes when the unique index refuses an insert; both editions
[x] ch14-catch-all         Chapter 14: says that query catches every thrown value, so a bug inside it becomes DatabaseFailed, and how that squares with "Error: a bug, thrown and never caught"; both editions
[x] pt-health-slice        Portuguese edition: chapter 14 calls the server check "fatia de health", as chapter 10 does, not "fatia de saúde", which reads as a slice for medical data
[x] ch15-event-delivery    Chapter 15: names the delivery that added the event functions after chapter 12, and tells a reader following the clinic to queue and build it, so their code can match book-v1/four-pieces; both editions
[x] ch15-route-io          Chapters 6, 14 and 15: the route that reads the request body squares with "the only place an infra exception becomes a Result" and "only the repository does I/O"; both editions
[x] ch15-submit-event      Chapter 15: says the hook's submitEvent is bookingEvents.ts's submit imported under another name, and what shown and latest hold; both editions
[x] slice-imports          Chapters 14, 15 and 16: say whether a slice may import another slice's code, as slotsOf imports the repositories of three other slices, and when that code moves to src/lib/ instead; both editions
[x] ch15-injection-rule    Chapter 15: the injection rule, its key point and "Nowhere else is anything passed" fit the code, where every repository function receives db; both editions
[x] ch15-piece-cost        Chapter 15: "When the pieces pay their way" shows a piece that has a job and still costs more than it gives, so a reader can weigh one; both editions
[x] ch16-unit-test         Chapter 16: the definition of a unit test fits the route test, which drives the route, the use case, the repository and SQLite; both editions
[x] ch16-it-each           Chapter 16: the text describes the it.each over two refusal codes and an exception as it runs, and says what it.each does; both editions
[x] ch16-reading-count     Chapter 16: the key point's 20 of 95 files gets a baseline, or "small" is stated as a description, not a measure; both editions
[x] clinic-booking-submit  useBooking's submit publishes its in-flight state as an update applied to the current state, as docs/01 says, and passes the state it books with into run, so the shown ref written during render leaves, by a recorded run
[x] clinic-hours-save      useWeeklyHours' save publishes its in-flight state as an update applied to the current state, so a time typed or a period added or removed just before Save is kept, by a recorded run
[x] clinic-hours-report    the weekly hours editor's reports, saving included, reach the professionals section through one report member of HoursSection and one tested professionals event, so forward, the four callbacks and the copied comment leave; this finishes the clinic's milestone 1.1 line orchestrator-tests, which left forward and the saving report in the hook untested, by a recorded run
[x] clinic-update-type     the update type (current) => State is declared once and shared, and so is the starter shape that submitStarted and saveStarted repeat, each with its first occurrence named, as the clinic's AGENTS.md asks, where today seven files declare the type, by a recorded run
[x] clinic-event-shapes    the clinic's docs/01 names every shape an event with a call takes once the lines above are done, where today it gives one and the booking's next event, the weekly hours' { update, report } and starter, and the remembered list's plain functions are written only in work/done, by a recorded run
[x] ch14-failure-kinds     Chapter 14: says what an error and an exception are without Dart's classes, why an exception must not steer the flow, and that a library's exception becomes the domain's value at the boundary, so the app has none; both editions
[x] m4.1-review            the review of M4.1 as docs/05 §8 says: the Prologue to chapter 16 read end to end in both editions against the product questions and M4.1's paragraph; each confirmed finding becomes a line in a new milestone M4.2
[x] m4.1-code-review       /code-review of the clinic's code that M4.1 changed, a3e2470...6edc9ad: from the kit update right after book-v1/four-pieces, left out, to the last clinic run of M4.1, which has no chapter tag; each confirmed finding becomes a line in M4.2
```

## M4.2. What the review of M4.1 found

When this milestone closes, every confirmed finding of the M4.1 review is settled: chapter 3's key points say only what its run showed; chapter 7 says which of the clinic's non-negotiables are the kit's; Part III's definitions of a feature and a unit test fit the clinic's code it shows, and it says what the reader does about a bug that the boundary's catch hides; chapter 14's boundary squares with the routes that import a library's type; chapter 15 places every catch in a piece, explains the rule its view excerpt shows, prints the brief the reader is told to answer with, and its key point on when a piece is written meets its section; the clinic's weekly hours editor and booking form take no edit while a save or a booking is in flight, and only the hook can report that a save is in flight; and the Portuguese edition uses the terms chapter 3 taught and summarizes chapter 10's diff as it is.

```
[x] pt-spec-change-terms   Portuguese edition: chapters 1, 4 and 13 say "mudança" and "especificação", the terms chapter 3 taught, where today they say "change", "spec" and "specs" with no gloss
[x] ch3-key-point-rules    Chapter 3: the key point says of OpenSpec's once-per-project files only what the section shows, where today it credits OpenSpec with rules written once per project; both editions
[x] ch7-agents-fixed-lines Chapter 7: says which lines of the clinic's AGENTS.md non-negotiables are the kit's fixed lines and which the project's, where today it says "three fixed lines", four follow, and "An open decision in docs/00 is asked, never assumed." fits neither; both editions
[x] pt-skeleton-diff       Portuguese edition: chapter 10's summary of the skeleton diff puts exit code 1 in Behaviour, where the diff has it, and names the data/ folder the server now creates
[x] ch14-keepless-feature  Chapter 14: the definition of a feature has a place for a slice that keeps nothing, as health does, where today "A feature is one thing the app keeps" leaves it out; both editions
[x] ch14-swallowed-bug     Chapter 14: says what the reader does about a bug that query turns into a DatabaseFailed nobody sees, and squares reason 4 of "Why not throw" with using the same query as its example of harm; both editions
[x] ch14-library-types     Chapter 14: squares "changes that code alone" with the routes that import DatabaseSync's type; both editions
[x] ch15-brief-printed     Chapter 15: prints the author's brief for orchestrator-tests that the reader is told to answer with, as chapters 7, 8 and 10 print theirs, where today it is behind a note; both editions
[x] ch15-uncaught-pieces   Chapters 14 and 15: say which piece openDatabase and migrate belong to, since they catch in no piece today, against the table's "the only place an infra exception becomes a Result"; both editions
[x] ch15-view-rule         Chapter 15: says that tooLateToCancel in the booking view comes from the use case the client imports, so the excerpt can be checked against the view's "Forbids"; both editions
[x] ch15-shape-cost        Chapter 15: the key point on when a piece is written meets the section, which keeps healthEvents.ts for one shape across hooks, where today it says only "gives more than it costs"; both editions
[x] ch16-unit-test-fakes   Chapter 16: the definition of a unit test fits the event tests' fake repositories and the stubbed localStorage and fetch, where today it says a unit test "runs whatever that piece calls"; both editions
[x] clinic-busy-fields     the weekly hours editor's time inputs and the booking form's name and phone are disabled while a save or a booking is in flight, as the add, remove and submit buttons already are, so the screen shows only what was sent and a successful save closes no unsent edit, and the booking test that keeps a name typed after the click changes to match, by a recorded run
[x] clinic-hours-answer    load answers only a refusal or nothing and save only "saved", "failed" or a refusal, and "saving" is a report only useWeeklyHours makes, so no answer can leave the professionals section busy for good, where today WeeklyHoursAnswer's report allows "saving", by a recorded run
[x] m4.2-review            the review of M4.2 as docs/05 §8 says for a last round of fixes: only what M4.2's lines changed, both editions, against M4.2's paragraph; each confirmed finding, blocking or not, becomes a line at the start of M5, and no M4.3 opens
```

## M5. Part IV, Git for agents and teams

When this milestone closes, a reader can choose between trunk, a branch per delivery and a worktree per delivery, run agents in parallel, use the commit as the human review, and run a team's work on GitHub with pull requests, issues and a Projects board.

```
[x] git-essentials         Chapter 17: commits, branches, merges, trunk and git-flow
[x] clinic-worktrees       the clinic switches to a worktree per delivery, then route-errors and minutes-of are proposed and built by two agents at once in two worktrees and merged by the author with --no-ff, conflict included, by a recorded run; no chapter
[x] worktrees              Chapter 18: worktrees and parallel agents, and where parallelism really stops
[x] commit-as-review       Chapter 19: the agent stages, the person commits, and why; absorbed by rewrite as a section of chapter 15
[x] github-for-teams       Chapter 20: pull requests as the team's review, issues, Projects boards, and why the wiki is not docs/ (the agent reads the repository, not the wiki); absorbed by rewrite as chapter 21
[x] m5-review              the review of M5 as docs/05 §8 says; superseded: M5's chapters were rewritten whole by rewrite (M8), whose review is m8-review
```

## M6. Part V, Beyond code

When this milestone closes, a reader can adapt the process to a team's tools, including GitHub issues and a Projects board kept in step by the kit, ask the project questions as they would ask a colleague, from how it is going to who owes them an answer, and use the method on work that is not software.

```
[x] customizing            Chapter 21: extra marks, question deliveries, proof files, a board mirror (Case A), and the queue mirrored to GitHub issues and a Projects board, built and tagged in the guided project; absorbed by rewrite as chapter 21, with Case A's board mirror and no guided project
[x] project-as-assistant   Chapter 22: the documents as the whole project's memory, for engineering and product alike: what is pending, how is it going, how long each delivery took (queue plus git history), who is away; team and client conversations kept in a free notes folder, so "who owes me answers?" and "what must I ask, and whom?" are answered too (Case A, Case B); absorbed by rewrite as chapter 18, on Case A alone
[x] beyond-software        Chapter 23: analyses, proposals (Case B), codeless projects (Case A), client communication as a source of truth, data work (Ninjobs' database security rules as deliveries), and this book; absorbed by rewrite as chapter 22
[x] cost-and-where         Chapter 24: what coding agents cost, where they pay and where they do not, and how a team decides, with measured numbers; Ninjobs after the pivot as the case: tokens per delivery (Claude Code's session logs over the pages done and the commits, same days), why the page and the documents keep each session small, and why cache reads are counted apart; absorbed by rewrite as chapter 23
[x] adoption               Chapter 25: taking the method to a team and a company (Case B); absorbed by rewrite as chapter 24, with Case A's catches and Case B's note
[x] m6-review              the review of M6 as docs/05 §8 says; superseded: M6's chapters were written by rewrite (M8), whose review is m8-review
```

## M7. Appendices and launch

When this milestone closes, version 1 is tagged, the PDF and EPUB are on books.kodel.com.br, and focus-kit points to the book.

```
[ ] ninjobs-case           Appendix: the Ninjobs case end to end, with its numbers and their sources, including the token count after the pivot by kind, model and month, and how it was counted
[ ] glossary               Appendix: the glossary, generated from docs/03 in both editions
[ ] templates              Appendix: every document template, annotated
[ ] workshop-map           Appendix: the parts mapped to workshop sessions, with timings
[x] exercise-answers       Appendix: answers to every exercise, linked to the guided project's tags; retired by rewrite (ADR-0017): the book has no exercises
[ ] cover                  make book puts each edition's cover on the PDF's first page (book/assets/cover-<edition>.pdf, A5) and as the EPUB's cover image (book/assets/cover-<edition>.png)
[ ] m7-review              the review of M7 as docs/05 §8 says: the whole book and its appendices read end to end in both editions against the product questions and M7's paragraph, before v1 is tagged; each confirmed finding becomes a line in a new milestone M7.1
[ ] launch                 v1 tag and Release; focus-kit's README repointed in its own repository (OD-4)
```

## M8. The rewrite

When this milestone closes, the book is 25 chapters in both editions in three movements, the base, the method and the team, with no run narrated, no guided project and no exercises, every chapter saying what the team gains with its evidence, and the author has read it whole and decided what M7 still needs.

```
[x] rewrite                the whole book rewritten in one delivery (ADR-0017): Part I the base (why process, how agents see, SDD, KISS/YAGNI/DRY, pure functions and exceptions as values, features not layers, the four pieces, a test per piece), Part II the method (birth, documents, install, starting, queue, /propose, /apply, closing, governor, the project as the team's assistant), Part III git and the team's tools, Part IV beyond code (not software, cost, adoption); Ninjobs, Case A and Case B as the evidence; both editions; docs/00, 03, 04, 05, 06, AGENTS.md and ADR-0017 updated
[ ] m8-review              the review of M8 as docs/05 §8 says: the whole book read end to end in both editions against the product questions and M8's paragraph; each confirmed finding becomes a line in a new milestone M8.1
```
