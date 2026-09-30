### F1. The Portuguese edition uses two words each for "spec" and for an OpenSpec "change"
* Where: `book/pt/01-why-process.md:72`, `book/pt/04-birth-of-focus-kit.md:9`
* Question: paragraph
* What: Chapter 3 teaches "especificação" for spec and "mudança" for an OpenSpec change, and chapter 1's body uses those words too. But chapter 1's key point says "spec", chapter 4 uses the bare English "change" and "changes" (lines 9, 16 and 28), and chapter 13 says "Spec formal", "Delta de spec" and "specs" (lines 48 to 49). None of these is glossed.
* Reader: A Portuguese reader who learned "mudança" in chapter 3 meets an untranslated "change" in chapter 4 and cannot be sure it is the same thing.

### F2. Chapter 2 credits a rules file with a position that a first message has too
* Where: `book/en/02-how-agents-see.md:49`, `book/en/02-how-agents-see.md:67`
* Question: 2
* What: Line 49 says the instruction you gave at the start "ends up in the middle". Line 67 then says "A decision in a file is loaded whole at the start of every session, near the beginning of the window." Both sit at the start of the window, and later files and output pile up after both. The real advantage, a fresh session that reloads the file, is in the next paragraph, but this sentence gives the credit to position.
* Reader: They may believe a rules file beats a first message inside one long session, which the cited research does not show.

### F3. A chapter 3 key point credits OpenSpec with project-wide rules the chapter never shows
* Where: `book/en/03-spec-driven.md:195`, `book/en/03-spec-driven.md:82`
* Question: paragraph
* What: The key point says "Spec Kit and OpenSpec both wrote the decision before code in files the agent reads, and rules once per project". The section "Some decisions are written once per project" describes only Spec Kit's constitution. OpenSpec's once-per-project row (3 files, 32 lines, 140 words) is never said to hold rules and is never shown.
* Reader: They take away, as a result of the run, a claim that nothing shown in the run supports.

### F4. The clinic's `AGENTS.md` excerpt cannot be split into the kit's lines and the project's
* Where: `book/en/07-brainstorm.md:165`, `book/en/07-brainstorm.md:184`
* Question: paragraph
* What: "Its non-negotiables are the kit's template with the project's own rules above the three fixed lines." Four lines follow "No paid service". Line 184 says each project line points at the document that holds its reason, yet "An open decision in docs/00 is asked, never assumed." points at nothing, so it fits neither group.
* Reader: They cannot tell which three lines the kit writes in every project and which the conversation added.

### F5. The Portuguese summary of the `skeleton` diff puts a change in the wrong section
* Where: `book/pt/10-propose.md:420`
* Question: paragraph
* What: The summary says the exit code 1 for a failed migration was added in the Contract, but the diff adds it to Behaviour (diff lines 294 to 297). It also leaves out the other Behaviour change: the server now creates the `data/` folder.
* Reader: A Portuguese reader who relies on the summary, as the edition invites, misplaces one change and misses another.

### F6. The definition of a feature does not cover the health slice the chapter shows
* Where: `book/en/14-errors-and-slices.md:54`, `book/en/14-errors-and-slices.md:71`
* Question: paragraph
* What: "A feature is one thing the app keeps, named by a term of the project's docs/03 (the appointment, the professional, the weekly hours), and its slice holds every action on it." Yet the health slice at lines 60 to 71 "stores nothing" and names no docs/03 term, and it is still a feature folder. The definition has no place for a feature that keeps nothing, such as a check or a report.
* Reader: They cannot tell from the rule why health is a slice, or where a similar feature goes in their own project.

### F7. The clinic's `query` breaks the chapter's own definition of an error, and the chapter leaves it there
* Where: `book/en/14-errors-and-slices.md:101`, `book/en/14-errors-and-slices.md:157`, `book/en/14-errors-and-slices.md:114`
* Question: paragraph
* What: An error is defined as "thrown and never caught", so it reaches your screen and your analytics. But `query` catches bugs too, and "The routes answer `DatabaseFailed` with its code alone and log nothing, so a bug caught there reaches neither your screen nor your analytics." Reason 4 of "Why not throw" then uses this same recommended `query` as its example of the harm of a wide catch. The chapter names the gap but gives no rule for it.
* Reader: If they copy the chapter's own boundary pattern, they silently swallow bugs, and they cannot tell whether reason 4 argues against the pattern they were just taught.

### F8. The SQLite boundary does not meet the claim made with the Apple example
* Where: `book/en/14-errors-and-slices.md:266`, `book/en/14-errors-and-slices.md:271`
* Question: 2
* What: "Nothing past that code knows Apple exists, so a second way to sign in, or a new version of Apple's SDK, changes that code alone." In the clinic, though, the repositories and routes import SQLite's `DatabaseSync` type (line 271), and the appointments repository, not `database.server.ts`, matches SQLite's English error text (lines 185 to 189). The chapter does not say whether a library type crossing the boundary is allowed.
* Reader: They cannot tell whether their routes importing a library's type breaks the boundary rule they just learned.

### F9. Chapter 15 tells the reader to answer with a brief it does not print
* Where: `book/en/15-four-pieces.md:18`
* Question: paragraph
* What: The reader is told to "answer its questions with the author's brief", but the brief is reachable only through the footnote to a run record. Chapters 7, 8 and 10 printed their briefs.
* Reader: To build the code that `book-v1/four-pieces` holds, a reader following the guided project has to leave the book.

### F10. The four-pieces table conflicts with chapter 14's list of where the clinic catches
* Where: `book/en/15-four-pieces.md:27`, `book/en/14-errors-and-slices.md:239`
* Question: 5
* What: The table, quoted from the clinic's docs/01, calls the repository "the only place an infra exception becomes a Result". Chapter 14 listed `openDatabase`, the migration runner and every route that reads a body as catching too. Chapter 15 (line 355) accounts only for the route.
* Reader: After chapter 14, they cannot place `openDatabase` or `migrate` in any piece, or reconcile them with the table's "only".

### F11. The view excerpt uses names the text never explains, one of them a rule's outcome
* Where: `book/en/15-four-pieces.md:87`, `book/en/15-four-pieces.md:126`
* Question: paragraph
* What: The text explains `typeName`, `typePhone`, `back` and `submit`. It does not explain `step`, `busy`, `tooLateToCancel`, `backButton`, `summary` or `errorStrings`. `tooLateToCancel` is the result of a rule, shown in the one piece whose "Forbids" column bans business rules, and the chapter never says where it comes from.
* Reader: They cannot check this excerpt against the "Forbids" column that the chapter tells them to read first.

### F12. A chapter 15 key point contradicts the piece the clinic keeps
* Where: `book/en/15-four-pieces.md:465`, `book/en/15-four-pieces.md:454`
* Question: 2
* What: The key point says "A piece is written when it has a job and that job gives more than it costs". The same chapter shows the clinic writing and keeping `healthEvents.ts`, which "costs more than it gives", for the sake of one shape across hooks, and lines 12 to 18 had the reader build it. The chapter never says whether a uniform shape is a valid reason under the rule.
* Reader: They get two conflicting rules and cannot decide which applies to a piece in their own code.

### F13. The definition of a unit test does not fit the tests the chapter shows
* Where: `book/en/16-testing-and-agents.md:24`, `book/en/16-testing-and-agents.md:25`
* Question: paragraph
* What: "A test Vitest runs is a unit test: it calls one piece directly, with no server running, and runs whatever that piece calls." But the event tests swap the repositories for fakes (lines 181 to 246), and `remembered.test.ts` and `request.test.ts` stub `localStorage` and `fetch` (lines 295 and 309). None of these runs whatever the piece calls.
* Reader: The definition classifies the chapter's own orchestrator test wrongly, so they cannot use it to judge their own tests.

### F14. The claim that a slice bounds what an agent reads goes further than the counts show
* Where: `book/en/16-testing-and-agents.md:350`, `book/en/16-testing-and-agents.md:368`
* Question: 2
* What: The opening and key point 5 state that "A slice bounds where an agent reads". The section itself admits "The record has no run of the same delivery without slices", and it finds that a delivery reads about as much as it touches. The fix outside any slice, `e2e-database-busy`, read the fewest files (4 of 77).
* Reader: They take as measured a claim the counts do not separate from the size of each delivery.

## Paragraph
every confirmed finding of the M4 review is settled: FINDING F1, F3, F5, F6, F7, F9, F11, F13
chapter 3's key points say what its run showed: FINDING F3
Part III says what makes one feature: FINDING F6
and whether a slice may use another slice's code: ch14 §Vertical slices · book-v1/closing-a-milestone
its definitions of a refusal fit the clinic's code it shows: ch14 §Exception, refusal, error · book-v1/closing-a-milestone
its definition of an error fits the clinic's code it shows: FINDING F7
its definition of a unit test fits the clinic's code it shows: FINDING F13
its definition of injection fits the clinic's code it shows: ch15 §What the clinic injects · book-v1/four-pieces
chapter 14 tells an error from an exception in any language: ch14 §Exception, refusal, error · book-v1/closing-a-milestone
says why a throw must not steer the flow: ch14 §Why not throw · book-v1/closing-a-milestone
and keeps a library's exceptions out of the domain: ch14 §The boundary · book-v1/closing-a-milestone
it shows a piece that has a job and still costs more than it gives: ch15 §When the pieces pay their way · book-v1/four-pieces
every excerpt can be followed from its text: FINDING F4, F11
a reader following the guided project is told to build the code that chapter 15's tag holds: FINDING F9
the clinic's client orchestrators publish every in-flight state as an update of the current state, send the weekly hours editor's reports through one tested event, declare each repeated type once, and take only the event shapes its docs/01 describes: m4.1-code-review
and the Portuguese edition means what the English means: FINDING F1, F5
