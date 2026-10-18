# ch12-scenario-levels

**Objective.** A reader can tie every scenario on a delivery's page to the test or manual check that actually proves it, and can see exact column types in the example Contract.

**Behaviour.**
* For a normal loan and the due-today edge, the page names pure use-case checks for the decision and due date, plus orchestration/screen checks for recording and displaying it.
* For overdue and suspended members, pure tests prove refusal; orchestration checks prove nothing is saved and the expected message reaches the view.
* For two requests for the last copy, a repository test with the real database constraints proves one loan succeeds and one returns `AlreadyLent`; no pure function test claims to prove the race.
* A reader reviewing the schema can identify each column's type and nullability and the active-loan uniqueness rule without guessing; a returned loan does not prevent lending that copy again.

**Contract.** `book/en/12-propose.md` and `book/pt/12-propose.md`, The page example and its explanation only.
Keep its five Behaviour scenarios and the existing messages.
The illustrative `loan` contract will spell out `copy_id` and `member_id` as non-null text identifiers, `lent_at` and `due_at` as non-null ISO calendar-date text (`YYYY-MM-DD`), and `returned_at` as nullable ISO calendar-date text; the unique index covers `copy_id` only while `returned_at` is null.
These types are the teaching choice for the authored example, consistent with chapter 3's string dates and chapter 5's SQLite repository example, not a claim about a real case's schema.
Done when names which scenario and observable each test proves, following `book/en/05-testing-each-piece.md` and its Portuguese counterpart; docs/05 §3 requires each Behaviour line be a test or manual check.
Sources: the existing chapters 3 to 5 and docs/03's pure function, repository, running example and behaviour terms; no new concept or case passage.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: the existing book layout.

**Out of scope.** Implementing a library or migration: the page is an explicitly authored teaching artifact; new scenarios and chapter 12's command lifecycle changes: separate queue lines own them.

**Done when.**
* [ ] Trace all five example scenarios to appropriate checks, including display, no write on refusal, real constraint race and returned-copy edge; no checklist promises all five as pure unit tests.
* [ ] The schema's types, nullability and unique-index predicate are explicit in both editions; the artifact remains within docs/04's 74-column block width.

* [ ] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [ ] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [ ] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).
