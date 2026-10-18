---
name: apply
disable-model-invocation: true
description: >-
  Implement work/<slug>.md end to end: code, tests, verify, proof, docs,
  then stage and suggest the commit. Never commits on its own.
argument-hint: <slug>
metadata:
  version: "2026.10.18.1"
---
Implement `work/$ARGUMENTS.md` in this session, completely. When the slug
is missing, ask for it. The page is the scope; do not widen it.

Read the page, `AGENTS.md`, docs/01 (architecture), docs/04 (conventions),
docs/05 (process) and docs/06 (queue). Follow docs/05's project slots
literally: verify, environments, proof, publish policy and git strategy.
Before editing, inspect the working tree and index as docs/05 §6 says.
Work on the branch or worktree /propose created, if any.

If the page contradicts a document, stop and say which: the document changes
in this delivery or the page is wrong. Do not resolve it silently. Follow
docs/05 §4 to resume a blocked line, or a `[*]` line the person says its
session left; refuse an incomplete proposal and point to /propose. Otherwise
only a fully defined `[>]` line whose `after` is done becomes `[*]`, your
first edit. Another session's delivery in the same tree is not a conflict;
docs/05 §§4 and 6 say what is.

When work cannot go on, record what was built and what it waits on, leave
the page in `work/` and block it with `resume: apply` as docs/05 §4 says.
A prerequisite fix becomes a `[ ]` line above this one. End the page with
the partial message, show it in the conversation in the same `commit`
block, and follow docs/05 §6's blocked-work staging rule; report verify
and environments, and stop without claiming completion.

Build where docs/01 says, with its error convention. Write docs/04's tests;
one too slow for verify goes with docs/05's slow tests and you say so,
never into verify silently. Abstraction on the second concrete occurrence;
the page names the first. Add no dependency, layer or tool the page did
not name. No em dash in any text a user reads.

Run verify until green. Prove the delivery as docs/05 says; list divergences
and fix them until only what you can justify remains. Update the documents
and ADRs the delivery changes, and the manual of anything it adds or changes
that a person does by hand (docs/05 §5). Then have this delivery's changes,
by its paths, reviewed as docs/05 §5's Delivery review says, by a context
that did not write them; another delivery's file is not this review's. Fix
what breaks the page, docs/04 or the text this delivery wrote and run verify
again; anything else becomes a `[ ]` line. Nothing verify covers changes
after its last green run: a later edit runs it once more. Leave environments
as required. Record divergences, omissions, proof, the review and decisions
on the page. Tick every Done when item and move the page to `work/done/`.
Resolve dependent queue lines by docs/05 §4, preserving their definition or
implementation phase.

End the page with one final `commit` block in docs/05 §6's format, replacing
any earlier suggestion. Stage only this delivery's changes as that section
says and suggest the same message in the conversation too, in the same
`commit` block. Your last edit marks the line `[x]` and stages that hunk.
Never commit or merge unless the person asks. Files and message in the
documentation language; talk in the person's language. Give the person's next steps,
each command written out: use what the delivery changed, as its user
would, and ask here for what is wrong; review the staged diff; commit
with the suggested message, and on a delivery branch merge it as docs/05
§5 says; then the queue's next line and its command, written as this
host invokes commands. The last thing you say is which environment is at
which version and the command that updates the others; never end silent.
