# Queue

`[ ]` not yet defined · `[~]` being defined · `[>]` completely defined, `work/<slug>.md` ready for /apply · `[*]` being built · `[x]` done, page in `work/done/` · `[?]` waiting, with `· resume: propose` or `· resume: apply` before `· blocked: <reason>` or `· blocked: after <slug>, <slug>` at the end of the line.
A line never leaves; it changes mark, at the moment the work changes (docs/05 §4).
A line is the mark, the slug, one sentence and its suffixes; what happened goes on its page. Longer lines written before kit-2026-10-16 are in this file's history, at the commit before it.
The order is the priority: the next delivery is the first free line, one whose `· after <slug>` lines are all `[x]`; `· after <slug>`, written when the line is added, is an order, not a block.

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
[x] install-and-hosts      Chapter 5: install, update, and how each host invokes the commands, and why the method does not depend on one host
[x] the-documents          Chapter 6: docs/00 to 06, ADRs, AGENTS.md, and why documents do the work
[x] brainstorm             Chapter 7: /brainstorm on the guided project, and choosing a stack by what the agent knows (the Ninjobs lesson of chapter 4)
[x] analyze                Chapter 8: /analyze on the brownfield project
[x] two-choices            Chapter 6 gains "The two choices": FOCUS and git in a paragraph each, so chapters 7 and 8 point back to them
[x] queue-and-milestones   Chapter 9: the queue, the marks, milestones and their paragraphs
[x] propose                Chapter 10: /propose, one page, reading it before /apply, and splitting what does not fit
[x] apply                  Chapter 11: /apply, verify, proof, documents, stage, never commit
[x] clinic-milestone-1     the guided project's milestone 1 built line by line with /propose and /apply, each page and staged change reviewed and committed by the author, recorded; no chapter
[x] closing-a-milestone    Chapter 12: the whole-milestone review of the clinic's milestone 1 with /code-review, findings become queue lines; Ninjobs' milestone review as the counter-example
[x] useful-notes           a source note only where the reader gains something to open, one note per source in the PDF and the EPUB, with docs/04, docs/03, docs/01 and AGENTS.md saying the rule; both editions
[x] the-governor           Chapter 13: which concrete error would it have caught, and what the process does not have
[x] m3-review              the review of M3 as docs/05 §8 says: the Prologue to chapter 13 read end to end in both editions against M3's paragraph
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
[x] milestone-1-bridge     Between chapters 11 and 12: the reader is told to build the rest of the clinic's milestone 1 with /propose and /apply, with a tag to compare against; both editions
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
[x] kit-milestone-review   focus-kit bff8414 reinstalled in the book, the clinic and the fork, each milestone of the three queues ending with its review line
[x] kit-milestone-review-chapters  Chapters 7, 8, 9 and 12 to 15 follow focus-kit bff8414: the review is the last line of every milestone and its findings open a milestone <M>.1; both editions
[x] m4-review              the review of M4 as docs/05 §8 says: the Prologue to chapter 16 read end to end in both editions against M4's paragraph
[x] m4-code-review         /code-review of the clinic's code from book-v1/closing-a-milestone to book-v1/four-pieces
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
[x] ch15-event-delivery    Chapter 15: names the delivery that added the event functions after chapter 12, so a reader following the clinic can match book-v1/four-pieces; both editions
[x] ch15-route-io          Chapters 6, 14 and 15: the route that reads the request body squares with "the only place an infra exception becomes a Result" and "only the repository does I/O"; both editions
[x] ch15-submit-event      Chapter 15: says the hook's submitEvent is bookingEvents.ts's submit imported under another name, and what shown and latest hold; both editions
[x] slice-imports          Chapters 14, 15 and 16: say whether a slice may import another slice's code, as slotsOf imports the repositories of three other slices, and when that code moves to src/lib/ instead; both editions
[x] ch15-injection-rule    Chapter 15: the injection rule, its key point and "Nowhere else is anything passed" fit the code, where every repository function receives db; both editions
[x] ch15-piece-cost        Chapter 15: "When the pieces pay their way" shows a piece that has a job and still costs more than it gives, so a reader can weigh one; both editions
[x] ch16-unit-test         Chapter 16: the definition of a unit test fits the route test, which drives the route, the use case, the repository and SQLite; both editions
[x] ch16-it-each           Chapter 16: the text describes the it.each over two refusal codes and an exception as it runs, and says what it.each does; both editions
[x] ch16-reading-count     Chapter 16: the key point's 20 of 95 files gets a baseline, or "small" is stated as a description, not a measure; both editions
[x] clinic-booking-submit  useBooking's submit publishes its in-flight state as an update applied to the current state, as docs/01 says, by a recorded run
[x] clinic-hours-save      useWeeklyHours' save publishes its in-flight state as an update applied to the current state, so an edit just before Save is kept, by a recorded run
[x] clinic-hours-report    the weekly hours editor's reports, saving included, reach the professionals section through one report member of HoursSection and one tested professionals event, by a recorded run
[x] clinic-update-type     the update type (current) => State and the starter shape are each declared once and shared, as the clinic's AGENTS.md asks, by a recorded run
[x] clinic-event-shapes    the clinic's docs/01 names every shape an event with a call takes, by a recorded run
[x] ch14-failure-kinds     Chapter 14: says what an error and an exception are without Dart's classes, and that a library's exception becomes the domain's value at the boundary; both editions
[x] m4.1-review            the review of M4.1 as docs/05 §8 says: the Prologue to chapter 16 read end to end in both editions against M4.1's paragraph
[x] m4.1-code-review       /code-review of the clinic's code that M4.1 changed, a3e2470...6edc9ad
```

## M4.2. What the review of M4.1 found

When this milestone closes, every confirmed finding of the M4.1 review is settled: chapter 3's key points say only what its run showed; chapter 7 says which of the clinic's non-negotiables are the kit's; Part III's definitions of a feature and a unit test fit the clinic's code it shows, and it says what the reader does about a bug that the boundary's catch hides; chapter 14's boundary squares with the routes that import a library's type; chapter 15 places every catch in a piece, explains the rule its view excerpt shows, prints the brief the reader is told to answer with, and its key point on when a piece is written meets its section; the clinic's weekly hours editor and booking form take no edit while a save or a booking is in flight, and only the hook can report that a save is in flight; and the Portuguese edition uses the terms chapter 3 taught and summarizes chapter 10's diff as it is.

```
[x] pt-spec-change-terms   Portuguese edition: chapters 1, 4 and 13 say "mudança" and "especificação", the terms chapter 3 taught, where today they say "change", "spec" and "specs" with no gloss
[x] ch3-key-point-rules    Chapter 3: the key point says of OpenSpec's once-per-project files only what the section shows; both editions
[x] ch7-agents-fixed-lines Chapter 7: says which lines of the clinic's AGENTS.md non-negotiables are the kit's fixed lines and which the project's; both editions
[x] pt-skeleton-diff       Portuguese edition: chapter 10's summary of the skeleton diff puts exit code 1 in Behaviour, where the diff has it, and names the data/ folder the server now creates
[x] ch14-keepless-feature  Chapter 14: the definition of a feature has a place for a slice that keeps nothing, as health does; both editions
[x] ch14-swallowed-bug     Chapter 14: says what the reader does about a bug that query turns into a DatabaseFailed nobody sees, and squares it with reason 4 of "Why not throw"; both editions
[x] ch14-library-types     Chapter 14: squares "changes that code alone" with the routes that import DatabaseSync's type; both editions
[x] ch15-brief-printed     Chapter 15: prints the author's brief for orchestrator-tests that the reader is told to answer with, as chapters 7, 8 and 10 print theirs; both editions
[x] ch15-uncaught-pieces   Chapters 14 and 15: say which piece openDatabase and migrate belong to; both editions
[x] ch15-view-rule         Chapter 15: says that tooLateToCancel in the booking view comes from the use case the client imports, so the excerpt can be checked against the view's "Forbids"; both editions
[x] ch15-shape-cost        Chapter 15: the key point on when a piece is written meets the section, which keeps healthEvents.ts for one shape across hooks; both editions
[x] ch16-unit-test-fakes   Chapter 16: the definition of a unit test fits the event tests' fake repositories and the stubbed localStorage and fetch; both editions
[x] clinic-busy-fields     the weekly hours editor's time inputs and the booking form's name and phone are disabled while a save or a booking is in flight, by a recorded run
[x] clinic-hours-answer    load answers only a refusal or nothing and save only "saved", "failed" or a refusal, so no answer can leave the professionals section busy for good, by a recorded run
[x] m4.2-review            the review of M4.2 as docs/05 §8 says for a last round of fixes: only what M4.2's lines changed, both editions, against M4.2's paragraph
```

## M5. Part IV, Git for agents and teams

When this milestone closes, a reader can choose between trunk, a branch per delivery and a worktree per delivery, run agents in parallel, use the commit as the human review, and run a team's work on GitHub with pull requests, issues and a Projects board.

```
[x] git-essentials         Chapter 17: commits, branches, merges, trunk and git-flow
[x] clinic-worktrees       the clinic switches to a worktree per delivery, and route-errors and minutes-of are built by two agents at once in two worktrees and merged by the author, by a recorded run
[x] worktrees              Chapter 18: worktrees and parallel agents, and where parallelism really stops
[x] commit-as-review       Chapter 19: the agent stages, the person commits, and why
[x] github-for-teams       Chapter 20: pull requests as the team's review, issues, Projects boards, and why the wiki is not docs/
[x] m5-review              the review of M5 as docs/05 §8 says
```

## M6. Part V, Beyond code

When this milestone closes, a reader can adapt the process to a team's tools, including GitHub issues and a Projects board kept in step by the kit, ask the project questions as they would ask a colleague, from how it is going to who owes them an answer, and use the method on work that is not software.

```
[x] customizing            Chapter 21: extra marks, question deliveries, proof files and a board mirror (Case A)
[x] project-as-assistant   Chapter 22: the documents as the whole project's memory, for engineering and product alike
[x] beyond-software        Chapter 23: analyses, proposals, codeless projects, client communication as a source of truth, data work, and this book
[x] cost-and-where         Chapter 24: what coding agents cost, where they pay and where they do not, and how a team decides, with measured numbers
[x] adoption               Chapter 25: taking the method to a team and a company
[x] m6-review              the review of M6 as docs/05 §8 says
```

## M7. Appendices and launch

When this milestone closes, version 1 is tagged, the PDF and EPUB are on its GitHub Release, and focus-kit points to the book.

```
[x] glossary               Appendix: the glossary, generated from docs/03 in both editions
[x] templates              Appendix: every document template, annotated
[x] workshop-map           Appendix: the parts mapped to workshop sessions, with timings
[x] exercise-answers       Appendix: answers to every exercise, linked to the guided project's tags
[x] cover                  make book puts each edition's cover on the PDF's first page and as the EPUB's cover image
[x] m7-review              the review of M7 as docs/05 §8 says: the whole book and its appendices read end to end in both editions against M7's paragraph, before v1 is tagged
[x] launch                 v1 tag and Release, so the PDFs and EPUBs have stable links, and focus-kit's README links the site and those files (OD-4)
```

## M8. The rewrite

When this milestone closes, the book is 25 chapters in both editions in three movements, the base, the method and the team, with no run narrated, no guided project and no exercises, every chapter saying what the team gains with its evidence, and the author has read it whole and decided what M7 still needs.

```
[x] rewrite                the whole book rewritten in one delivery (ADR-0017): Part I the base, Part II the method, Part III git and the team's tools, Part IV beyond code; both editions
[x] author-review-1        the author's own reading of the cover and the Prologue to chapter 5, fixed by conversation
[x] author-review-2        the author's second batch, chapters 7 to 22, fixed by conversation
[x] pdf-design             the PDF of both editions in the design the author chose on the canvas (direction C), with the cover, the EPUB and the site unchanged
[x] milestone-review-kit   chapters 13, 16 and 17 and docs/03 teach the milestone review as focus-kit d333348 defines it; both editions
[x] milestone-review-process  the book's docs/05 §4, §7 and §8 follow focus-kit d333348's milestone review
[x] m8-review              the author reads the rest of the book, chapter 6 on, and sends findings by conversation; each batch is fixed as an author-review-<n> line here, with no review of its own
```

## M9. Asking for more

When this milestone closes, a reader knows why an agent's first answer feels final, what an agent never proposes (the test of a limit it claimed, the reader's time, the cost, what nobody asked for), and how to ask for more with a challenge protocol, with a recorded experiment and published studies as the evidence; the prologue plants the idea and chapter 25 teaches it.

```
[x] ask-for-more-experiment  three arms on the lending library, first answer against the challenge protocol, 3 runs per arm, judged blind by the author, recorded
[x] ask-for-more-chapter     Chapter 25, alone in a new Part V, and a seed in the prologue: why the first answer feels final and the challenge protocol; both editions
[x] m9-review                the review of M9: the prologue and chapter 25 read against M9's paragraph, clause by clause
[x] ch25-protocol-findable   a reader of chapter 25 knows what the challenge protocol is and where its four turns are written, and finds them again without rereading the section; both editions
[x] ch25-cost-for-subscribers  a reader on a fixed subscription knows from chapter 25 what the protocol costs them, and no per-token price reads as the bill of their own session; both editions
```

## M10. The six marks

When this milestone closes, a reader knows the six marks of focus-kit 2026.10.05 (`[ ]`, `[~]`, `[>]`, `[*]`, `[x]`, `[?]`), why each is set at the moment the work changes and not when a command ends, the three cases of `[?]` and its two suffixes, and how a queue read as a kanban shows work while it happens; Case A's Azure Boards delay and its hand-made `[?]` are the evidence, and the book's own queue and process follow the kit.

```
[x] queue-states             a chapter of its own on the queue's six marks, who sets each and when, with chapters 13, 14, 15, 17, 18 and 21, docs/03, docs/05 §4 and this queue's header following the kit; both editions
[x] context-slot             docs/05 §5 gains the kit's Context slot: `context/` listed in `.gitignore`, not created
[x] m10-review               the review of M10 as docs/05 §8 says
[x] pdf-contents-one-page    the contents of each edition's PDF fit on one page, and a chapter's number in it is no larger than its page number; both editions
[x] pdf-footnote-numbers     footnote numbers in each edition's PDF render as plain numbers beside their notes, with no coloured block behind them, in Preview too; both editions
```

## M11. What a critique found

When this milestone closes, a reader who hears that the page needs the whole answer before the work starts, that the method needs FOCUS, or that a person who commits after nine good deliveries stops reading finds the book's answer where the doubt arises: exploring is a conversation with the agent before any page, the method works with any of the three architectures, and the review of chapter 15 is the defence against automation bias.

```
[x] critique-fixes           chapters 10, 14 and 15: exploring by conversation before any page, the same page under any architecture, and automation bias with the review as its defence; both editions
[x] m11-review               the review of M11 as docs/05 §8 says
```

## M12. focus-kit 2026.10.13

When this milestone closes, the book teaches focus-kit 2026.10.13 and the repository runs on it: two sessions in one working tree on free lines, the queue's order as its priority and `· after <slug>` as an order, not a block, `/propose` deciding what the documents answer, Behaviour drafted with concrete inputs and failure cases, the commit message in a `commit` block on the page, code changed only inside `/apply`, `/apply` staging only its delivery and naming the next steps, manuals in `docs/manuals/`, and an update that reports migrations instead of rewriting the project's documents; the kit's changelog, paraphrased, is the evidence.

```
[x] kit-2026-10-13           reinstall the kit at 2026.10.13 and apply its migration report to docs/05, AGENTS.md, this header and docs/manuals/
[x] ch21-one-tree             chapter 21 (and 20 and 10 where they choose git): two sessions in one working tree on free lines that touch different files, and when a worktree still pays; both editions · after kit-2026-10-13
[x] ch13-16-queue-order       chapters 13 and 16: the order is the priority, the next delivery is the first free line, and `· after <slug>` against `[?]`; both editions · after kit-2026-10-13
[x] ch14-propose-decides      chapter 14: /propose decides what the documents answer, and Behaviour with a concrete input, the result the user sees and the cases that must fail; both editions · after kit-2026-10-13
[x] ch15-apply-ends           chapter 15: the `commit` block on the page and in the conversation, staging only the delivery, and the person's next steps in the host's form; both editions · after kit-2026-10-13
[x] ch10-12-manuals           chapters 10 and 12: docs/manuals/, what goes there and who writes it (/analyze, /apply); both editions · after kit-2026-10-13, ch15-apply-ends
[x] ch11-update-migrations    chapter 11: updating reports migrations for docs/04, docs/05 and AGENTS.md, the changelog, and each command naming the next; both editions · after kit-2026-10-13
[x] ch10-commit-format        chapters 10 and 12: docs/04 no longer holds the format of a commit message, docs/05 §6 does; both editions · after ch10-12-manuals
[x] ch18-19-only-apply        chapters 13 and 19: code changes only inside /apply, and AGENTS.md answers "where are we?" from the queue; both editions · after kit-2026-10-13
[x] m12-review                the review of M12 as docs/05 §8 says
```

## M13. focus-kit 2026.10.16

When this milestone closes, the book teaches focus-kit 2026.10.16 and the repository runs on it: a worktree per delivery in a container folder, /apply reading only its own queue lines, a queue line as mark, slug, one sentence and suffixes, a slot as what and the command, a manual for a proof on another machine, and a request that continues as /propose in the same session.

```
[x] kit-2026-10-16           reinstall the kit at 2026.10.16 and apply its migration report
[x] ch15-24-apply-reads      chapters 15 and 24: /apply reads only its queue lines and why; both editions · after kit-2026-10-16
[x] ch13-short-lines         chapters 13 and 19: a queue line is one sentence, and a request may continue as /propose in the same session; both editions · after kit-2026-10-16
[x] ch10-12-slots-manuals    chapters 10 and 12: a slot says what and the command, and a manual also holds a proof /apply runs on another machine; both editions · after kit-2026-10-16
[x] ch11-update-2026-10-16   chapter 11: the update example and its migration report at 2026.10.16; both editions · after kit-2026-10-16
[x] ch21-container           chapter 21: a worktree per delivery in a container folder, as 2026.10.15 shapes it; both editions · after kit-2026-10-16
[x] m13-review               the review of M13 as docs/05 §8 says
[x] kit-as-it-is             the book describes focus-kit as it is today, never comparing it with an earlier version of itself, and docs/04 says so; both editions
[x] plain-numbers            no passage of the book reads as a run of numbers: each keeps the numbers that prove its point; both editions · after kit-as-it-is
[x] ch21-worktree-first      chapter 21 says what a worktree is before it relies on the word; both editions
```

## M14. focus-kit 2026.10.16.2

When this milestone closes, the book teaches focus-kit 2026.10.16.2 and the repository runs on it: a milestone review that also reads the code through the Milestone review slot, `/apply` reading the whole queue and ending on which environment is at which version, a request outside `/apply` that stops at the line with a draft for a fresh `/propose`, a hidden folder and a branch prefix named by the kit and no tool that plants it, every slot of docs/05 §5 named where the book lists them, and an update example at the current version.

```
[x] kit-2026-10-16-2         reinstall the kit at 2026.10.16.2 and apply its migration report to docs/05, AGENTS.md and the skills
[x] ch17-review-reads-code   chapters 13, 17 and 25: the milestone review also reads the code, through the Milestone review slot, and a confirmed finding is a line; both editions · after kit-2026-10-16-2
[x] ch15-24-whole-queue      chapters 15 and 24: /apply reads the whole queue, marks `[x]` after the stage and ends on which environment is at which version; both editions · after kit-2026-10-16-2
[x] ch13-14-19-line-stops    chapters 13, 14 and 19: a request outside /apply stops at the line, with a draft page when the line cannot hold it, and /propose runs in a fresh session; both editions · after kit-2026-10-16-2
[x] ch21-hidden-folder       chapter 21: the container's hidden folder and branch prefix are `.focus-kit/` and `focus-kit/`, and no tool that plants the kit is named; both editions · after kit-2026-10-16-2
[x] ch10-12-all-slots        chapters 10 and 12: every slot of docs/05 §5 where the book lists them, the questions /brainstorm and /analyze ask today, and what /analyze reads; both editions · after kit-2026-10-16-2
[x] ch11-update-2026-10-16-2 chapter 11: the install sentence as the kit's README gives it, the update example and its report at 2026.10.16.2, and the worktree slot's migration; both editions · after kit-2026-10-16-2
[x] ch14-18-kit-wording      chapters 14 and 18: the /propose sentence quoted as the kit writes it, the Contract's third reason, and the governor's "no gate beyond a complete page"; both editions · after kit-2026-10-16-2
[x] m14-review               the review of M14 as docs/05 §8 says · after ch14-18-kit-wording
[x] repo-files-any-name      every check reads every tracked or untracked file, whatever characters its name has
[x] site-build-anchors       the site build fails on a link to a heading that does not exist, and reports each broken link at its own line
[x] book-build-links         the book build fails on a link to a heading that does not exist, links every note mention, and orders appendices by number · after parity-notes-readmes
[x] parity-notes-readmes     parity counts every note mention, whatever its key, and fails when the two READMEs' sections differ
[x] hook-hash-lines          the commit-msg hook refuses a message whose stored text holds a listed term, lines starting with `#` included
[x] em-dash-every-text       the em dash check reads every text file outside `work/done/*-run/`, diagrams and files without an extension included
[x] links-url-bounds         the link check judges the address a reader's link points to, whatever Markdown form wraps it
[x] entry-apostrophes        a list entry written with either apostrophe matches both
[x] epub-chapter-links       in the EPUB a link to a chapter prints in the text's colour, as in the PDF
[x] venv-failed-install      a failed install leaves `.venv` to be rebuilt by the next make
[x] od4-kit-pointer          docs/00's OD-4 says what is true today of the kit's pointer to FOCUS
[x] docs01-retired-projects  docs/01 and `AGENTS.md` present no guided or brownfield project or chapter tag as live, and docs/01's tree names every ignored path
[x] docs03-current-rows      docs/03's waiting mark and tag rows say what docs/05 says today, and its references name sections that exist
[x] docs04-gain-number       docs/04 gives one rule for a gain's numbers, names no retired guided project, and its references name sections that exist
[x] docs05-no-exercises      docs/05 §3's chapter Contract lists no exercises
[x] docs06-legend            the queue's legend defines `[>]` as docs/05 §4 does
[x] ch03-restated-rule       chapter 3 says how many of each tool's files restate the rule, and gives the Ninjobs lines the cause chapter 9 gives; both editions
[x] ch09-key-points          chapter 9's key points give the cause its gain gives and no count the gain does not; both editions
[x] ch16-resume-apply        chapter 16 says once, as docs/05 §4 does, where a `resume: apply` line returns; both editions
[x] ch17-slot-none           chapter 17 says a Milestone review slot of none launches no deep review, apart from the base commit; both editions
[x] ch26-what-counts         chapter 26's sentences on following wrong advice and on the three runs say what each number counts; both editions
```

## M15. The reader's time

When this milestone closes, a reader reaches the method in five chapters instead of nine, every rule of the book is said once in the chapter that owns it with one source per point and one gain section, a reader sees what a five-line delivery costs before being asked to accept one, chapters 20 to 26 keep only what no manual gives, and a chapter after chapter 12 walks a reader from zero to the first delivery on a new project and on an existing one, step by step, with no repository.

```
[x] quick-guide              a new chapter after chapter 12: from install to the first delivery and its commit, one column for a new project and one for an existing one, one pointer per step; both editions · after m14-review
[x] prologue-and-why         chapters 0 and 1 become one prologue that opens with the METR study and ends in the three parts; both editions · after m14-review
[x] ch3-spec-cut             chapter 3 keeps the definition of a spec and the measured numbers, and drops the taxonomy and the tools the book never used; both editions · after m14-review
[x] simplicity-and-results   chapters 4 and 5 become one chapter that opens with Ninjobs, one section per principle, exception, refusal and error, and the exhaustive switch; both editions · after m14-review
[x] focus-and-slices         chapters 6 and 7 become one chapter, FOCUS, with the slice, the four pieces and the code shown once; both editions · after m14-review
[x] ch8-testing-trim         chapter 8 opens with the agent that writes too many tests, keeps one source per point and one gain section; both editions · after m14-review
[x] renumber-chapters        the chapters renumbered after the merges, with every cross-reference, index and build following; both editions · after prologue-and-why, simplicity-and-results, focus-and-slices, quick-guide
[x] method-said-once         chapters 9 to 19: each rule, mark list, number and story said once in the chapter that owns it, and the passages that read as the kit's manual cut to what the reader uses; both editions · after m14-review
[x] small-delivery-example   chapter 13: a five-line delivery shown end to end, so the reader sees what the smallest page costs before the rule asks for one; both editions · after method-said-once
[x] ch20-21-git-cut          chapters 20 and 21 open with the decision they serve, drop the history and the glossary a manual gives, and say each thing once; both editions · after m14-review
[x] ch22-26-team-cut         chapters 22 to 26: repeated sources, repeated gains and asides cut, the challenge protocol moved next to the story that needs it; both editions · after m14-review
[x] one-gain-section         every chapter ends with one gain section and no key points that repeat it, and the lack of a baseline is said once, in the prologue; both editions · after prologue-and-why, ch8-testing-trim, method-said-once, ch20-21-git-cut, ch22-26-team-cut
[x] review-slot-models       docs/05's Milestone review slot says how this repository's deep review runs and on which models, as the author decided after M14
[x] m15-review               the review of M15 as docs/05 §8 says
[x] disclosure-docstring     check_disclosure.py's docstring says when the run fails as docs/01 does
[x] docs01-empty-list        docs/01's make scan row says a list file with no entry fails the run even locally, as check_disclosure.py does
[x] docs03-finding-and-gain  docs/03's finding row includes a finding the code review confirms, and its team gain row allows no sentence on a missing number
[x] adr17-gain-amendment     ADR-0017 carries an amendment saying a gain with no number has no sentence about it
[x] docs05-review-checker    docs/05's Milestone review slot names the checker as the author runs it, Opus with the host's advisor on Fable
[x] stack-rule-once          the stack chosen by what the agent knows, and the Flutter story, are told in one chapter and pointed to from chapters 6, 9 and 22; both editions
[x] free-line-gloss          chapters 7 and 18 gloss a free line as docs/03 defines it, `[ ]` lines included; both editions
[x] pt-free-line-done        the Portuguese edition's free-line gloss says done with chapter 14's word, `feita`, not `pronta`, which also reads as ready, in chapters 7, 18 and 19
[x] line-rule-once           chapters 13 and 22 point to chapter 11 for the one-sentence queue line instead of restating it; both editions
[x] case-a-board-once        chapters 16 and 20 point to chapter 14 for the kanban board, the fold onto three columns and Case A's `[?]`; both editions
[x] slice-paths              chapters 13, 14 and 19 name the lending library's slices under `src/features/`, as chapter 4 does; both editions
[x] code-width               no code block in chapters 1, 8, 10, 11, 13, 14, 15 and 21 runs past 74 columns; both editions
[x] pt-skeleton-first        chapter 11's Portuguese queue says the skeleton's screenshot was the first, as the English does, within 74 columns
[x] pt-fixed-terms           the Portuguese edition uses docs/03's term and one word for each thing (due date, engine, view, fake, worktree, the checks, the fix-due-date slug) and means what the English means in chapters 11 and 14
[x] pt-placeholders          the Portuguese edition translates every placeholder and folder written for a chapter, notes the kit's English ones, and explains the imperative with its own commit (chapters 4, 7, 11, 13, 14, 18, 19, 21)
[x] ch03-opening             chapter 3 opens on what grew on Ninjobs without retelling chapter 6's causes and checks; both editions
[x] ch04-parnas              chapter 4 introduces Parnas's criterion with its source, or does not lean on it; both editions
[x] ch05-lend-pointer        chapter 5 points to the chapter where the use case `lend` is shown; both editions
[x] ch10-commit-message      chapter 10's commit message follows docs/05 §6's format as the book writes it; both editions
[x] ch12-review-skill        chapter 12 names no review skill the kit does not have; both editions
[x] ch15-first-commit        chapter 15 gives the first commit as a base for any milestone, as docs/05 §8 does; both editions
[x] ch17-delivery-time       chapter 17 measures how long a delivery took in a way that holds on trunk; both editions
[x] ch17-closing-commit      chapter 17 says how the commit that closes a delivery names it, as docs/05 §6 gives its last line; both editions
[x] ch18-log-evidence        chapter 18's log gives lend-book's commit as chapter 13 does, and its gain cites no illustration as evidence; both editions
[x] ch19-when-worktrees-pay  chapter 19 says one thing about when a worktree per delivery pays; both editions
[x] ch21-counts-once         chapter 21 gives each count once, its gain one number or pair, and points to chapter 13 for the pending-deletion story; both editions
[x] ch23-what-survives       chapter 23 says what survives of the method without Ninjobs' own product checks; both editions
[x] ch24-note-keys           chapter 24's numbers carry their note key at the claim; both editions
```

## M16. focus-kit 2026.10.17

When this milestone closes, the book teaches focus-kit 2026.10.17 and the repository runs on it: `/apply` having each delivery's own changes reviewed by a context that did not write them, with the host's own review where the agent can run it and keep it to the delivery's paths, else a read-only agent, fixing what breaks the page before it ends; a milestone review whose code reading is the kit's own and runs in any host that runs agents, over `git diff <base>..HEAD` and never a bare commit, split into the Milestone review slot's areas with one read-only agent each, every reader listing the paths it read and the line waiting as `[?]` when they miss part of the range, a checker marking every candidate seen, latent or weak before the person sees it, the review started on the person's word because it costs, and the reviews' readers and checker as the one specialized subagent the governor admits; Devin Desktop, formerly Windsurf, reading the commands from `.agents/skills/` and invoking them as `/<name>`; and a reader who runs `/propose` in a batch knows what each page must say about the answers chosen without them, and why the commit stays theirs when applies run in parallel.

```
[x] kit-2026-10-17           reinstall the kit at 2026.10.17 and apply its migration report to docs/05, docs/03, AGENTS.md and the skills · after m15-review
[x] ch13-delivery-review     chapter 13: /apply has its delivery's changes reviewed by a context that did not write them, the host's own review first, fixes what breaks the page and lines the rest; both editions · after kit-2026-10-17
[x] ch15-review-by-areas     chapter 15: the code reading over the range since the base, split by areas, one read-only agent each in any host, the paths read, a checker for every candidate, and the person's word; both editions · after kit-2026-10-17, ch13-delivery-review
[x] ch07-11-23-review-words  chapters 7, 11 and 23: the milestone review's code reading by areas on the person's word, no deep review a person launches, and chapter 7's slots with the Delivery review; both editions · after ch15-review-by-areas
[x] ch16-review-agents       chapter 16: the one specialized subagent the governor admits, the reviews' readers and checker, and the errors that let them in; both editions · after kit-2026-10-17, ch13-delivery-review, ch15-review-by-areas
[x] batch-propose            chapter 19: proposes run in a batch on the recommended answers, each page listing what it decided alone, while applies stay parallel only on free lines and every commit stays the person's; both editions · after ch16-review-agents
[x] ch08-10-devin-desktop    chapters 8 and 10 and docs/03: Devin Desktop, formerly Windsurf, its folder `.agents/skills/` and its `/propose <slug>`, and no `.windsurf/skills/`; both editions · after kit-2026-10-17
[x] ch08-09-review-slot      chapters 8 and 9: the update example and its report at 2026.10.17, and the questions on the delivery review and on the milestone review's areas and model; both editions · after kit-2026-10-17
[x] m16-review               the review of M16 as docs/05 §8 says · after ch13-delivery-review, ch15-review-by-areas, batch-propose, ch08-10-devin-desktop, ch08-09-review-slot, ch07-11-23-review-words
[x] docs04-width-rule        docs/04 names the width check among the tests, and docs/04 and `check_width.py` agree on which info strings go unmeasured
[x] width-comment-fence      `check_width.py` measures no fence inside an HTML comment, as `mask` does
[x] fence-commonmark         `markdown.py` opens and closes a fence where CommonMark does, and docs/01 says so
[x] docs01-helpers           docs/01 names every helper `markdown.py` shares, `target_end` among them, every script that uses them, and `check_width.py`'s use of `check_prose.py`
[x] adr17-section-name       ADR-0017's amendment names the docs/04 section `one-gain-section` changed
[x] docs06-m16-paragraph     docs/06's M16 paragraph names the reviews' readers and checker, and M15's `pt-free-line-done` sentence starts in its neighbours' column
[x] docs03-review-rows       docs/03's delivery review row fixes the text the delivery wrote, as the apply skill says, and its candidate row glosses seen
[x] ch15-range-pointer       chapter 15 points `<base>..HEAD` to the chapter that teaches a range, or teaches it; both editions
[x] ch19-batch               chapter 19's batch stages its adjacent marks in docs/06 without contradicting what a conflict is, and points question deliveries to chapter 20 as Case A's customization; both editions
[x] ch04-features-folder     the Portuguese chapter 4 gives `features/` as the book's name, not the kit's
[x] ch11-blocking-fix        chapter 11 blocks a delivery only on a prerequisite fix, as chapter 13 does, and the Portuguese queue says what the English one says; both editions
[x] pt-ninjobs-article       the Portuguese edition gives Ninjobs one article throughout
[x] docs04-features-reason   docs/04's Evidence gives `features/` chapter 4's reason, the book's name for the slices' folder, not a name an external format fixes
```

## M17. focus-kit 2026.10.18

When this milestone closes, the book teaches focus-kit 2026.10.18 and the repository runs on it: a milestone review's base is the commit of the previous milestone's review, or the first commit, so the range holds the fixes of its findings; a line waits in four cases, a code reading that missed part of its range among them, with what was read as its reason; the checker's seen is glossed with latent and weak; and a Delivery review that reads `git diff` also reads the files a delivery created.

```
[x] kit-2026-10-18           reinstall the kit at 2026.10.18 and apply its migration report to docs/05 §§4, 5 and 8, docs/03's waiting mark and the skills · after m16-review
[x] ch08-update-2026-10-18   chapter 8: the update example and its report at 2026.10.18, the base named as the previous review's commit; both editions · after kit-2026-10-18
[x] ch13-created-files       chapter 13: the delivery review reads the files the delivery created, untracked when it runs; both editions · after kit-2026-10-18
[x] ch14-four-waits          chapter 14: a line waits in four cases, a code reading that missed part of its range among them; both editions · after kit-2026-10-18
[x] ch15-review-base         chapter 15: the base is the commit of the previous milestone's review, or the first commit; both editions · after kit-2026-10-18
[x] ch14-resume-moment       chapter 14's fourth waiting case says the review was being built, so it resumes by `apply`; both editions
[x] ch15-waiting-reason      chapter 15's review line waits with `· blocked: <what was read>` after `· resume: apply`; both editions · after ch15-review-base
[x] m17-review               the review of M17 as docs/05 §8 says · after kit-2026-10-18, ch08-update-2026-10-18, ch13-created-files, ch14-four-waits, ch15-review-base, ch14-resume-moment, ch15-waiting-reason
[x] conflict-same-lines      chapter 19, docs/05 §4 and §6, and docs/03's conflict row define a conflict between two sessions in one way, so a batch's adjacent marks in one hunk of docs/06 are either staged or stopped for, consistently; both editions
[x] ch19-adjacent-mark-staging  chapter 19 says who stages a batch's adjacent mark and how a session stages one line of a shared hunk without an editor; both editions
[x] pt-ch19-index-word       the Portuguese chapter 19's key point says "a partir do índice", as chapter 13 and 19's batch paragraph say, not "a partir do stage"
[x] pt-librarian-masculine   the Portuguese edition says "o bibliotecário", as docs/03 fixes, in chapters 4, 5, 11, 14, 17 and 19
[x] ch15-review-range-order  chapters 15 and 8 say the review's range holds the next milestone's deliveries that landed after the review's commit, not every one of them; both editions
[x] ch15-first-commit-base   chapter 15 says what a first milestone's range leaves out of the first commit, instead of "the whole project"; both editions
[x] ch13-four-waits          chapter 13's list of when /apply cannot go on names all four cases a line waits in; both editions
[x] ch08-report-item-one     chapter 8's report item 1 says what text it replaces, as items 2 and 3 do; both editions
[x] pt-ch08-migration-label  the Portuguese chapter 8's key point names the changelog item's `Migração:` label as the English names `Migration:`
[x] untracked-diff-wording   chapter 8 and docs/03's untracked file row say a new file shows in `git diff --cached` once staged and never in plain `git diff`; both editions
[x] ch14-m1-return-book      chapter 14's first milestone holds `return-book`, like chapters 11 and 15; both editions
[x] docs03-checker-pt        docs/03 gives the checker and the labels seen, latent and weak their Portuguese words, and the Portuguese edition uses them
[x] docs05-fourth-case-version  docs/05 §4 and docs/03's waiting mark row say the fourth case came with focus-kit 2026.10.18
[x] docs05-review-concurrency  docs/05's Milestone review slot says how many review agents run at once
[x] docs05-four-cases-sentence  docs/05 §4's sentence on when a line waits reads as four cases, the fourth not an example of the third
```

## M18. What the author's reading found

When this milestone closes, a reader of chapters 0 to 7 learns each idea where it is named instead of being sent to a later chapter, a Portuguese reader reads "o Ninjobs", a reader with little TypeScript reads chapter 3's refusal without seeing a magic string, a team reads FOCUS as optional before deciding to adopt it, keeps its tests fast, and teaches the agent by talking to it instead of fixing its work by hand, and every passage the author's reading marked says what the author means.

```
[x] early-no-forward-links   chapters 0 to 7 explain in a few words each idea they name instead of pointing to a later chapter, and keep the pointers in their gain sections; both editions
[x] pt-ninjobs-masculine     the Portuguese edition and docs/03 give Ninjobs the masculine article, o Ninjobs, as an app or a site
[x] case-a-why-anonymous     the prologue says why Case A has no owner, client or business: a private corporate project whose name could not be published without authorization; both editions
[x] agent-never-unsure       the book says, where it fits best, that an agent never says "I don't know", and that the person's judgment is what tells a hypothesis from a fact; both editions
[x] ch02-gain-less-to-read   chapter 2's gain says plainly that the method writes less because the person must read all of it, and less to read is more attention; both editions
[x] pt-identifiers-choice    the Portuguese chapter 3 drops the sentence on which names are translated and says Portuguese identifiers are a teaching choice, not a recommendation
[x] ch03-literal-type-comment  chapter 3's refusal example carries a comment saying the string is a type the compiler checks, so err takes no other; both editions
[x] ch03-error-languages     chapter 3 says several languages separate a program's bug from a failure the caller handles, and that Dart does it most explicitly; both editions
[x] ch04-focus-optional      chapter 4 opens saying FOCUS is optional and the team decides after reading its gain, and the gain adds that one pattern across projects makes moving people cheaper; both editions
[x] ch04-uncle-bob           chapter 4 gives Robert C. Martin's nickname, Uncle Bob, where it first names him; both editions
[x] ch04-scalable-meaning    chapter 4's S says the project grows without one feature interfering with another, which is why it scales; both editions
[x] ch05-test-time           chapter 5 says agents write tests without minding how long they run, and the person keeps the suite fast with pure use cases and slower tests only where they pay; both editions
[x] ch05-random-values       chapter 5's section on swapping only I/O and the clock covers random values and anything else that changes between runs; both editions
[x] ch07-rag-and-numbers     chapter 7 says the documents work as retrieval made for the project, and that every focus-kit project gives each document the same number; both editions
[x] ch07-talk-not-edit       chapter 7 says the person changes the documents by talking to the agent, without the sentence that reads as a contradiction; both editions
[x] ch11-queue-grows         chapter 11 says three to eight deliveries is how a milestone starts, not a limit, and that the person decides what enters it, because agents tend to add; both editions
[x] ch11-agent-runs-propose  chapter 11 drops the claim that the agent cannot run /propose on its own; both editions
[x] ch13-teach-the-agent     chapter 13's staged review asks for each correction by talking to the agent, so it learns, instead of fixing by hand; both editions
[x] ch14-face-prototype      chapter 14's kanban board shows briefly face.kodel.com.br, the author's prototype of a board that runs on focus-kit; both editions
[x] try-before-commit        the book advises using the software being built before committing each page, as on Ninjobs: small things fixed in conversation while the delivery is open, larger ones as the next lines; both editions
[x] ch19-agent-does-git      chapter 19 says the person can always ask the agent to do a git step for them, a commit message, a conflict, a commit, a merge or a push, and checks the result; both editions
[x] ch19-git-step-wording   chapters 18 and 19 name only git steps and knots the book teaches where they say the agent acts on the person's word, say conflict marker, and give the Portuguese one phrase for the agent acting alone; both editions
[x] docs04-code-layout       docs/04's rule for code says declarations and `{ }` blocks are set apart by blank lines, as the author writes code
[x] m18-review               the review of M18 as docs/05 §8 says · after ch19-git-step-wording, ch14-face-prototype, try-before-commit, ch19-agent-does-git, docs04-code-layout, early-no-forward-links, pt-ninjobs-masculine, case-a-why-anonymous, agent-never-unsure, ch02-gain-less-to-read, pt-identifiers-choice, ch03-literal-type-comment, ch03-error-languages, ch04-focus-optional, ch04-uncle-bob, ch04-scalable-meaning, ch05-test-time, ch05-random-values, ch07-rag-and-numbers, ch07-talk-not-edit, ch11-queue-grows, ch11-agent-runs-propose, ch13-teach-the-agent
[x] copyright-version        the page with the copyright line says which version of the book this copy is and the date it was published, and asks the reader to check the book's GitHub repository for newer versions; `make release` writes them to a committed `VERSION` and builds the book before pushing; both editions
```

## M19. focus-kit 2026.10.18.1

When this milestone closes, the book teaches focus-kit 2026.10.18.1 and the repository runs on it: verify kept fast with the slow tests run by the milestone review, a line no clause needs going to the next milestone, /propose in the asking session or a fresh one, /apply's next steps starting with using the delivery, and the agent committing or merging only when asked; and every passage the comparison of the book with the kit on 2026-10-18 found false says what the kit does.

```
[x] kit-2026-10-18-1         reinstall the kit at 2026.10.18.1 and apply its migration report to docs/05 §§2, 4, 5, 6 and 8, docs/04, AGENTS.md and the skills · after m18-review
[x] ch08-update-2026-10-18-1 chapter 8: the update example and its report at 2026.10.18.1, and the Claude Code row that reads `AGENTS.md` alone only without a `CLAUDE.md`; both editions · after kit-2026-10-18-1
[>] ch05-13-slow-tests       chapters 5, 7, 13 and 15: verify fast on every delivery, the slow tests named in the Verify slot and run by the milestone review, and /apply saying when a test is too slow for verify; both editions · after kit-2026-10-18-1
[>] ch11-next-milestone      chapters 11, 14 and 15: a line no clause of the current milestone needs goes under the next milestone, and a review's finding stays in its own; both editions · after kit-2026-10-18-1
[>] propose-same-session     chapters 8 to 13 and 17: /propose runs in the session that asked for the change or in a fresh one, and /apply always in a fresh one; both editions · after kit-2026-10-18-1
[>] apply-use-first          chapters 10 and 13, and where chapters 18, 19, 22 and 23 describe the person's review: /apply's next steps start with using what the delivery changed; both editions · after kit-2026-10-18-1
[>] agent-commits-asked      chapters 6, 7, 13, 18, 19 and 23, and docs/00 contents: the agent never commits or merges on its own, and asked, it takes the step the person names; both editions · after kit-2026-10-18-1
[x] ch11-14-defined-mark     chapters 11 and 14: `[>]` means completely defined, not that the page exists, and a `[ ]` line may keep a draft; both editions
[>] ch21-done-when           chapter 21: /apply ticks every Done when item, as the kit says; both editions
[>] ch17-context-read        chapter 17: /brainstorm and /analyze read `context/` whole, and a later item is read on the person's request and turned into the documents; both editions
[x] ch14-back-to-open        chapter 14: a line returns to `[ ]` only as the kit says, `resume: propose` with its draft kept; both editions · after kit-2026-10-18-1
[x] ch08-10-fresh-start      chapters 8 and 10: /brainstorm and /analyze run in a fresh session after the install; both editions
[>] ch19-batch-staging       chapter 19: in a batch, /propose stages nothing, as the kit's /propose does; both editions
[>] ch18-kit-branches        chapter 18: git-flow and the squash merge are told as strategies outside the kit, whose branch is named after the slug and reverted in one merge; both editions
[x] ch06-23-kit-rules        chapters 6 and 23: the kit's rules as SETUP.md §2 lists them; both editions
[>] ch10-explicit-staging    chapter 10: the quick guide stages by explicit paths, never `git add -A`, as docs/05 §6 says; both editions
[x] ch08-hosts-details       chapters 8 and 10: Antigravity reads `AGENTS.md` directly with an always-on pointer, the Jules to Cline row in the tables, /brainstorm and /analyze take no slug, and Claude Code's skills disable model invocation; both editions
[>] ch09-empty-repo          chapter 9: a repository with no code starts with /brainstorm, as the kit says; both editions
[x] ch13-refuse-incomplete   chapter 13: /apply refuses an incomplete page and points to /propose, and only a `[>]` line becomes `[*]`; both editions
[>] ch02-93-moment           chapter 2: the 93 finished pages are counted after the opening, which had 91; both editions
[>] ch19-commit-by-index     chapters 13 and 19 and docs/05 §6: the person commits from an index holding one delivery, never by naming paths on `git commit`, and a conflict is a line both sessions edited, not a hunk, as the kit now says; both editions · after kit-2026-10-18-1
[x] ch13-review-base         chapter 13: the read-only review reads `git diff HEAD`, the branch's earlier commits and the created files; /apply updates documents and manuals before the review and runs verify again after any later edit; both editions · after kit-2026-10-18-1
[x] ch14-ended-and-dropped   chapters 14 and 23: a `[~]` or `[*]` line whose session ended is resumed on the person's word, and a cancelled delivery ends `[x] · dropped: <reason>`, which is how chapter 23's impossible request is written; both editions · after kit-2026-10-18-1
[>] ch18-revert-scope        chapters 18 and 19: one step reverts what git holds; a migration run or a message sent is undone as the page's Done when says, or not at all; both editions · after kit-2026-10-18-1
[>] ch15-review-head         chapter 15: the milestone review's page names the commit its reading started at, so the range stays fixed while readers work; both editions · after kit-2026-10-18-1
[>] ch07-ninjobs-focus       chapters 4, 6 and 7 and ADR-0016 distinguish the earlier whole-FOCUS requirement from the later simplification retaining two principles; both editions · after kit-2026-10-18-1
[ ] queue-legend-dropped     docs/06's legend and docs/03's mark and conflict rows say what focus-kit 2026.10.18.1 says: `· dropped:` on a cancelled line, and a conflict as a line both sessions edited · after kit-2026-10-18-1
[ ] ch12-defined-mark       chapter 12: the line becomes `[>]` when the page is completely defined, as docs/05 §3 says, not when it is written; both editions
[ ] ch19-partial-branch-commits chapter 19: a blocked /apply on a delivery branch stages its partial work for the person to commit there, as chapter 13 cites; both editions
[>] m19-review               the review of M19 as docs/05 §8 says · after kit-2026-10-18-1, ch08-update-2026-10-18-1, ch05-13-slow-tests, ch11-next-milestone, propose-same-session, apply-use-first, agent-commits-asked, ch11-14-defined-mark, ch21-done-when, ch17-context-read, ch14-back-to-open, ch08-10-fresh-start, ch19-batch-staging, ch18-kit-branches, ch06-23-kit-rules, ch10-explicit-staging, ch08-hosts-details, ch09-empty-repo, ch13-refuse-incomplete, ch02-93-moment, ch19-commit-by-index, ch13-review-base, ch14-ended-and-dropped, ch18-revert-scope, ch15-review-head, ch07-ninjobs-focus, queue-legend-dropped, ch12-defined-mark, ch19-partial-branch-commits
```

## M20. What the audit of 2026-10-18 found

When this milestone closes, every technical claim the audit of 2026-10-18 found to promise more than its example or rule guarantees says what holds: chapter 3's examples run as the text says, chapter 4's isolation is a goal, chapter 1 promises recovery and not immunity, chapter 12's page ties each scenario to the level that proves it, chapter 24 says in which phase its protocol runs, chapter 22 preserves historical token totals with explicit coverage limits and no unmatched per-delivery average, and `make verify` runs the chapters' examples.

```
[>] ch03-query-catch         chapter 3: `query` turns only the driver's failures into a value and rethrows the rest, and an async variant awaits inside the try, each case tested; the audit ran the original and saw a bug and a control object become DatabaseFailed and a rejected promise escape the Result; both editions
[>] ch03-exhaustive-switch   chapter 3: a Result makes the cases representable and checkable, not every switch exhaustive; shows `Record` and a switch with a `never` check and when each fails to compile; both editions
[>] ch12-scenario-levels     chapter 12: the example page ties each Behaviour scenario to the level that proves it, the race for the last copy to the repository test, and its Contract gives the column types or points to the schema that does; both editions
[>] ch04-isolation-claims    chapter 4: isolation as a goal, the consumers of a changed contract checked, and the function shared with the client leaves the server's decision authoritative over other data; both editions
[>] ch01-recovery-not-immunity chapter 1: a decision in a file survives compaction as something to reread, not as text kept in every call; reopen the page and documents after compaction or resumption; both editions
[>] ch24-protocol-phase      chapter 24: in which phase the protocol runs; after /apply's first result, what already satisfies the page goes in and a new capability becomes a line; both editions
[>] ch22-cost-method         chapter 22 preserves historical token totals with their unrecovered coverage limits, removes unmatched per-delivery averages, and explains the growing whole-queue input; both editions
[>] ch16-prevention-evidence chapter 16: an error documented in another project may justify prevention, with evidence and a proportionate cost; both editions
[x] ch14-blocked-column      chapter 14: a blocked line returns to `[ ]` or `[>]` as docs/05 §4 says, so the board shows it there and keeps no memory of a column; both editions · after ch14-back-to-open
[>] verify-examples          `make verify` runs the executable examples extracted from the chapters, starting with chapter 3's `query` · after ch03-query-catch
[>] m20-review               the review of M20 as docs/05 §8 says · after ch03-query-catch, ch03-exhaustive-switch, ch12-scenario-levels, ch04-isolation-claims, ch01-recovery-not-immunity, ch24-protocol-phase, ch22-cost-method, ch16-prevention-evidence, ch14-blocked-column, verify-examples, m19-review
```
