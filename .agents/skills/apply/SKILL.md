---
name: apply
disable-model-invocation: true
description: >-
  Implement work/<slug>.md end to end: code, tests, verify, proof, docs,
  then stage and suggest the commit. Never commits on its own.
argument-hint: <slug>...
metadata:
  version: "2026.10.20.3"
---
The slugs are `$ARGUMENTS`: none, ask for one; several, one subagent per
slug, opened at once where docs/05 §4 allows, each taking its slug from
the message that opens it and running on the word of the person who typed
the command, which names them all. Implement `work/<slug>.md` in this
session, completely; the page is the scope: do not widen it.

Read the page, `AGENTS.md`, docs/00 (product), docs/01 (architecture),
docs/03 (domain), docs/04 (conventions), docs/05 (process) and docs/06
(queue). Follow every slot of docs/05 §5 literally, the project's own
slots included. Before editing, inspect the working tree and index as
docs/05 §6 says. Work on the branch /propose created, if any; with a
worktree, only in a session opened in it or a subagent sent to its path,
every file and command at that path: elsewhere, stop before any edit and
give the path.

If the page contradicts a document, stop and say which: the document changes
in this delivery or the page is wrong. Do not resolve it silently. Follow
docs/05 §4 to resume a blocked line, or a `[*]` line the person says its
session left; refuse an incomplete proposal and point to /propose. Otherwise
only a fully defined `[>]` line that §4's token and `after` let build
becomes `[*]`, your first edit. docs/05 §§4 and 6 say what a conflict is.

When work cannot go on, record what was built and what it waits on, leave
the page in `work/` and block it with `resume: apply` as docs/05 §4 says.
A prerequisite fix becomes a `[ ]` line above this one. End the page with
the partial message, show it in the conversation in the same `commit`
block, and follow docs/05 §6's blocked-work staging rule; report verify
and environments, and stop without claiming completion.

Build where docs/01 says, with its error convention and docs/03's
identifiers. Write docs/04's tests; one too slow for verify goes with
docs/05's slow tests and you say so, never into verify silently. Add no
dependency, layer or tool the page did not name.

Run verify until green. Prove the delivery as docs/05 says, fixing
divergences until only what you can justify remains. Update the documents
and ADRs the delivery changes, and the manual of anything it adds or changes
that a person does by hand (docs/05 §5). Then have this delivery's changes,
by its paths and no other delivery's, reviewed as docs/05 §5's Delivery
review says by a context that did not write them. Fix what breaks the page,
docs/04 or the text this delivery wrote and run verify again; anything else
becomes a `[ ]` line. A later edit to anything verify covers runs it once
more. Leave environments as required. Record divergences, omissions, proof,
the review and decisions on the page; tick every Done when item, move the
page to `work/done/` and resolve dependent lines as docs/05 §4 says.

End the page with one final `commit` block in docs/05 §6's format, replacing
any earlier one; stage only this delivery's changes as that section says;
show the same message in the conversation in a `commit` block. Your last
edit marks the line `[x]` and stages that hunk. Never commit or merge unless
the person asks. Files and message in the documentation language; talk in
the person's language. Give the person's next steps, each command written
as this host invokes commands: use what the delivery changed, as its user
would, and ask here for what is wrong; review the staged diff; commit with
the suggested message, merging a delivery branch as docs/05 §5 says; then
the queue's next line and its command. End saying which environment is at
which version and the command that updates the others; never end silent.
