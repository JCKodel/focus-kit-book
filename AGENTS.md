# One Page at a Time

A free, bilingual book that teaches Spec-Driven Development, the focus-kit method, the optional FOCUS architecture and git for parallel agents, from beginner to advanced. Prose of the process documents in English; identifiers in English; the book in English (source) and Brazilian Portuguese.

## Read before acting
- the product: docs/00 · the vocabulary: docs/03
- how it is built: docs/01 · the server: docs/02
- style and tests: docs/04 · process: docs/05 · queue: docs/06

## Non-negotiables
- Nothing private enters the repository: private cases are only Case A and Case B, with no name, place, date of meeting, path or business detail; the disclosure scan is green (docs/03, ADR-0012).
- Ninjobs appears only through its process artifacts and published numbers, paraphrased; never its infrastructure, credentials, users or commercial plans (docs/03).
- A change to one edition is a change to both, in the same delivery; English is the source (ADR-0004).
- Every chapter opens with what the reader can do after it and is as long as proving that takes: no filler, nothing useful cut, no length target (ADR-0015).
- Every artifact shown is real and every number cites its source (docs/04).
- The book mentions none of the author's earlier books and copies no text from them (ADR-0005).
- One delivery = one page in work/<slug>.md: /propose to define, /apply to build.
- No em dash in any text a user reads.
- The agent stages and suggests the commit message. It never commits.

## Do not rebuild
- A GitHub wiki, written or mirrored (ADR-0001).
- Code examples in several languages (ADR-0008).
- A link shortener or playground server for snippets; the guided project's tags do that (docs/01).
- The `[?]` mark (ADR-0013).

## How to work
- Chapters are `book/<edition>/NN-<slug>.md`, same file name in both editions; scripts in `scripts/` (docs/01).
- Every check prints `file:line: rule: message` and exits non-zero (docs/01).
- `make verify` before declaring anything done.
- Abstraction on the second concrete occurrence, and the delivery says which was the first.
- Ambiguity → ask. Documents are living: a delivery that changes behaviour updates the document that owns it, in the same delivery.
