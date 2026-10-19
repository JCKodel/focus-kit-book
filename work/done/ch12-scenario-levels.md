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
* [x] Trace all five example scenarios to appropriate checks, including display, no write on refusal, real constraint race and returned-copy edge; no checklist promises all five as pure unit tests.
* [x] The schema's types, nullability and unique-index predicate are explicit in both editions; the artifact remains within docs/04's 74-column block width.

* [x] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [x] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [x] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).

**Built.** Both editions of chapter 12, the example page and its explanation only. Contract: `loan` (pt `emprestimo`) lists each column with its type and nullability, `copy_id` and `member_id` as non-null text, `lent_at` and `due_at` as non-null `YYYY-MM-DD` text, `returned_at` as `YYYY-MM-DD` text, null while the copy is out, and the unique index on `copy_id` where `returned_at` is null, with its consequence in words: one open loan per copy, a returned copy lent again. Done when: one item per level in chapter 5's names, the unit tests of `lend` for the due date, both refusals and due today; the tests of `lendRequested` with fake repositories for `Lent`, `Refused` and no `insertLoan` on refusal; the repository test with the real migrations for the race and the returned copy; end-to-end tests for what the screen shows, all three messages included. The explanation says which test proves each Behaviour line, why the race is the repository's, and that the Contract gives types, nullability and the index rule in words. The five Behaviour lines and their messages are unchanged.

**Divergences.** None. No Case A or Case B passage was used or changed; the `[>]` wording on lines 26 and 148 is left to ch12-defined-mark.

**Decisions.** `YYYY-MM-DD` stays literal in the Portuguese edition, an external notation (docs/04). The returned-copy edge is a repository check in Done when, not a sixth Behaviour line, since the page keeps the five. The race message is proven end to end with an open loan of the copy already saved, which makes `insertLoan` return `AlreadyLent` against the real index.

**Proof.** `make verify` green after the last edit, rule `width` included for the example block in both editions; `make book` is run once by the batch driver for `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, for the author's passage checks.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of both chapter files against this page, docs/03, docs/04 and chapters 3 to 5. Points: (1) the suspended and race messages had no check reaching the screen: the end-to-end item now covers all three messages. (2) "may be empty" mislabelled nullability: "may be null" (pt "pode ser nula"). (3) the repository item did not say the first loan is saved: it does. (4) "the overdue member" (pt "o membro atrasado") read as a late member: "the member with an overdue book". (5) "with fakes": "with fake repositories", as chapter 5 and the pt say. (6) an overloaded sentence: split, the race's reason in its own sentence. Smaller: "carrying that refusal", the member shown in the end-to-end check, the message's period: all applied. Verify ran again after the fixes.

```commit
docs(ch12-scenario-levels): tie each scenario to the test that proves it

- Done when names the level and observable that prove each Behaviour line
- The race for the last copy is the repository test's, not a pure test's
- The loan Contract gives each column's type, nullability and index rule
- A returned copy can be lent again, proven by the repository test

work/done/ch12-scenario-levels.md
```
