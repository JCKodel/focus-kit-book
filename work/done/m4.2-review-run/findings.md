### F1. Chapter 14's remedy for a hidden bug covers only `query`, but the key point claims it for every catch at the boundary
* Where: `book/en/14-errors-and-slices.md:312`, `book/pt/14-errors-and-slices.md:312`
* Clause: it says what the reader does about a bug that the boundary's catch hides
* What: The new key point says "The catch at the boundary also catches bugs, so every repository runs in a test against SQLite with the real migrations". The same chapter lists other catches at the boundary: `request` in `src/lib/request.ts`, `remembered.ts`, and each route's body read. A SQLite test reaches none of them, and the new paragraph only talks about `query` and `DatabaseFailed`.
* Reader: A reader has no advice for a bug that `request` or `remembered.ts` turns into an ordinary failure value.
* Blocking: no. The advice given is correct for the database, which is the catch the section shows. It just stops short of the other catches the chapter lists.

### F2. Chapter 15 says the repository is the only piece that turns an exception into a value, but the route catches the request body
* Where: `book/en/15-four-pieces.md:438`, `book/pt/15-four-pieces.md:439`
* Clause: chapter 15 places every catch in a piece
* What: "So the table's "only" holds where events are served: of the four pieces, the repository alone turns an infra exception into a `Result`." The same chapter (line 380), and chapter 14, have the route, the server orchestrator, catch a body that arrived over the network and turn it into `BadRequest`. Nothing near line 438 recalls that this catch is chapter 14's "vexing" parse and not an infra exception.
* Reader: A reader who remembers line 380 sees the orchestrator catching during event handling, and the sentence that is supposed to close the question does not say why that catch is allowed.
* Blocking: no. The catch is placed in a piece at line 380, and chapter 14's "vexing" classification settles it for a careful reader, so no sentence is shown false.

### F3. Chapter 15 now says what the author did with the brief, not that the reader should answer with it
* Where: `book/en/15-four-pieces.md:18`, `book/pt/15-four-pieces.md:18`
* Clause: prints the brief the reader is told to answer with
* What: "Then run `/propose orchestrator-tests`; I ran it headless in Claude Code and answered its first round of questions with the author's brief, word for word". The old instruction ("answer its questions with the author's brief") became an account of the author's run. Line 24 does the same for later rounds ("Every later round was answered with…").
* Reader: A reader has to work out that they should paste the brief and then answer with the `Your call` rule, because the chapter never tells them to.
* Blocking: no. The brief is printed and the author's steps can be copied, so the reader can still follow them.

### F4. "The rule is written once, in the use case" is unclear right after the book shows the orchestrator comparing the deadline with `now`
* Where: `book/en/15-four-pieces.md:150`, `book/pt/15-four-pieces.md:151`
* Clause: explains the rule its view excerpt shows
* What: "So the rule is written once, in the use case, and the view holds none". The sentence just before it names "the use case `cancel`", but the rule the paragraph traces is `cancellationDeadline`. Also, the "already past the deadline" test (`cancellationDeadline(...) < now`) is written in `bookingEvents.ts`, the client orchestrator, whose "Forbids" column says "deciding rules". The text does not say why that comparison is not a rule.
* Reader: A reader may think the rule lives in `cancel`, and sees the orchestrator make a decision its own table forbids without being told why that is acceptable.
* Blocking: no. The deadline itself is written once in `rules.ts`, as the text says, and the view does hold no rule, so the claim the clause needs is true.

## Paragraph
chapter 3's key points say only what its run showed: ch3 §Key points · no tag
chapter 7 says which of the clinic's non-negotiables are the kit's: ch7 §The run on the clinic · no tag
Part III's definitions of a feature and a unit test fit the clinic's code it shows: ch14 §Vertical slices, §Key points; ch16 §A test for each piece · no tag
it says what the reader does about a bug that the boundary's catch hides: ch14 §Why not throw, §Exceptions as values in the clinic, §Key points · no tag
chapter 14's boundary squares with the routes that import a library's type: ch14 §The boundary, §Key points · no tag
chapter 15 places every catch in a piece: ch15 §What the clinic injects; ch14 §Exceptions as values in the clinic · no tag
explains the rule its view excerpt shows: ch15 §One event, one new state · no tag
prints the brief the reader is told to answer with: ch15 §The four pieces · no tag
its key point on when a piece is written meets its section: ch15 §Key points · no tag
the clinic's weekly hours editor and booking form take no edit while a save or a booking is in flight: clinic 21522b8
only the hook can report that a save is in flight: clinic 36d7ad9
the Portuguese edition uses the terms chapter 3 taught: pt ch1 §Key points; pt ch4 §How it was, §What went wrong, §Where it went, §Key points; pt ch13 §What the process does not have · no tag
summarizes chapter 10's diff as it is: pt ch10 §Read the page before `/apply` · no tag
