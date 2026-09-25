# Brief

Given word for word to SpecKit, OpenSpec and focus-kit in the run of `work/done/spec-driven-run.md`.

## Feature

A client can cancel their own appointment up to 24 hours before it starts. A cancelled appointment frees its slot. A cancellation later than that is refused with a message that says why.

## Answers

Storage stays in memory. There is no screen: the feature is a function in the module. The client is identified by `clientName`, with no login. Times are the clinic's local time. Tests use `node --test`. No notification is sent.

## Principles

Keep it simple. TypeScript, strict. Every rule has a test.

## Rule for a question the brief does not answer

Take the default the tool offers; with none, answer "the simplest option".
