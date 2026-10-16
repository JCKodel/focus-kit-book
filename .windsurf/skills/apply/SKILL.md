---
name: apply
disable-model-invocation: true
description: >-
  Implement work/<slug>.md end to end: code, tests, verify, proof, docs,
  then stage and suggest the commit. Never commits.
argument-hint: <slug>
metadata:
  version: "2026.10.16.2"
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
docs/05 §4 to resume a blocked line; refuse an incomplete proposal and
point to /propose. Only a fully defined `[>]` line whose `after` is done
becomes `[*]`, your first edit. Another session's delivery in the same tree is not a
conflict; docs/05 §§4 and 6 say what is.

When work cannot go on, record what was built and what it waits on, leave
the page in `work/` and block it with `resume: apply` as docs/05 §4 says.
A prerequisite fix becomes a `[ ]` line above this one. End the page with
the partial message, show it in the conversation in the same `commit`
block, and follow docs/05 §6's blocked-work staging rule; report verify
and environments, and stop without claiming completion.

Build where docs/01 says, with its error convention. Write docs/04's tests.
Abstraction on the second concrete occurrence; the page names the first.
Add no dependency, layer or tool the page did not name. No em dash in any
text a user reads.

Run verify until green. Prove the delivery as docs/05 says; list divergences
and fix them until only what you can justify remains. Leave environments
as required. Record divergences, omissions, proof and decisions on the
page; update their owning documents and ADRs. When the delivery adds or
changes something a person does by hand, write or update its manual as
docs/05 §5 says. Tick every Done when item and
move the page to `work/done/`. Resolve dependent queue lines by docs/05 §4,
preserving their definition or implementation phase.

End the page with one final `commit` block in docs/05 §6's format, replacing
any earlier suggestion.
Stage only this delivery's changes as that section says and suggest the
same message in the conversation too, in the same `commit` block. Your
last edit marks the line `[x]` and stages that hunk. Never
commit or merge. Files and message in the documentation
language; talk in the person's language. Give the person's next steps,
each command written out: review the staged diff; commit with the
suggested message, and on a delivery branch merge it as docs/05 §5 says;
then the queue's next line and its command, written as this host invokes
commands, in a fresh session. The last thing you say is which environment
is at which version and the command that updates the others; never end
silent about it.
