# Clinic Weigh-in

A TypeScript module that books appointments for a small clinic. Prose in English; identifiers in English.

## Read before acting
- the product: docs/00 · the vocabulary: docs/03
- how it is built: docs/01 · the server: docs/02
- style and tests: docs/04 · process: docs/05 · queue: docs/06

## Non-negotiables
- No screen: a feature is a function the module exports (docs/00, ADR-0006).
- Storage stays in memory: no database, file or network (ADR-0002).
- A client is its `clientName`: no login, no accounts (ADR-0007). Nobody is notified (ADR-0009).
- Every time is the clinic's local time; no time-zone handling (ADR-0008).
- The open decisions of docs/00 are asked, never assumed.
- One delivery = one page in work/<slug>.md: /propose to define, /apply to build.
- No em dash in any text a user reads.
- The agent stages and suggests the commit message. It never commits.

## Do not rebuild
- Nothing removed on purpose yet.

## How to work
- One file per feature in `src/`, its test beside it; a shared file only on the second use (docs/01).
- A rule that can refuse returns a Result; `throw` is never flow (docs/01, ADR-0003).
- The verify command of docs/05 §5 before declaring anything done.
- Abstraction on the second concrete occurrence, and the delivery says
  which was the first.
- Ambiguity → ask. Documents are living: a delivery that changes behaviour
  updates the document that owns it, in the same delivery.
