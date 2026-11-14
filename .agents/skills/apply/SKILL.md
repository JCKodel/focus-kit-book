---
name: apply
disable-model-invocation: true
description: >-
  Implement work/<slug>.md end to end: code, tests, verify, proof, docs,
  then stage and suggest the commit. Never commits on its own.
argument-hint: <slug>...
allowed-tools: Bash(git:*)
metadata:
  version: "2026.11.13"
---
The slugs are `$ARGUMENTS`. None: show what may run now as docs/05 §4
says and ask. Several: one subagent per slug, opened at once where
docs/05 §4 allows, each taking its slug from the message that opens it.
They run on the word of the person who typed the command, which names
them all. Implement `work/<slug>.md` in this session, completely; the
page is the scope: do not widen it. Fixing what this delivery built is
not widening it.

Read the page, `AGENTS.md`, docs/00 (product), docs/01 (architecture),
docs/03 (domain), docs/04 (conventions), docs/05 (process) and docs/06
(queue). docs/05 may open with a line mapping the kit's section numbers
to its own; read by it. Follow every slot of docs/05 §5 literally, the
project's own slots included. Before editing, inspect the working tree
and index as docs/05 §6 says. Work on the branch /propose created, if any; with a
worktree, only in a session opened in it or a subagent sent to its path,
every file and command at that path: elsewhere, stop before any edit and
give the path.

If the page contradicts a document, stop and say which: the document changes
in this delivery or the page is wrong. Do not resolve it silently. Follow
docs/05 §4 to resume a blocked line, or a `[*]` line the person says its
session left; refuse an incomplete proposal and point to /propose. Otherwise
only a fully defined `[>]` line whose `after` is integrated, as §4 says,
and whose files no in-flight build touches, becomes `[*]`, your first
edit. docs/05 §§4 and 6 say what a conflict is.

When work cannot go on, record what was built and what it waits on and
leave the page in `work/`. A line that waits on another takes it as its
`after` and returns to `[>]`, as docs/05 §4 says; any other is blocked
with `resume: apply`. A prerequisite fix becomes a `[ ]` line above this
one, ending `· from <slug>`. End the page with the partial message, show it in the
conversation in the same `commit` block, and follow docs/05 §6's
blocked-work staging rule; report verify and environments, and stop
without claiming completion.

Build where docs/01 says, with its error convention and docs/03's
identifiers. Write the tests docs/04 asks for what the page says and for
each flaw this delivery fixes, and no others. One too slow for verify
goes with docs/05's slow tests and you say so, never into verify
silently. Add no dependency, layer or tool the page did not name.

Run verify until green. Prove the delivery as docs/05 says, fixing
divergences until only what you can justify remains. Update the documents
and ADRs the delivery changes, and the manual of anything it adds or changes
that a person does by hand (docs/05 §5). Then have this delivery's changes,
by its paths and no other delivery's, reviewed as docs/05 §5's Delivery
review says by a context that did not write them. Fix in this delivery
whatever the review, the proof or the build finds wrong in what it built
or changed, a case the page did not name included, and run verify again.
What it cannot fix without widening the page, or without a decision no
document answers, is not fixed. That, and anything wrong in what it did
not build or change, is a note on the page, never a new line, unless
docs/05 §4 calls it grave. Where §4 is silent, only a prerequisite fix
is grave, the note goes under Outcome, and the last message says docs/05
awaits its migration. A later edit to anything verify covers runs it once more. Leave
environments as required. Record divergences, omissions, proof, the
review, each fix and the decisions on the page, however long it grows.
Tick every Done when item and move the page to `work/done/`.

End the page with one final `commit` block in docs/05 §6's format, replacing
any earlier one; stage only this delivery's changes as that section says;
show the same message in the conversation in a `commit` block. Your last
edit marks the line `[x]`, staged, as docs/05 §4 says. Never commit or
merge unless the person asks. Files and message in the documentation
language; talk in the person's language. Open the last message, done or
blocked, with what the delivery left: `🚨` before each new line and each
flaw that blocked it, `⚠️` before each note and a verify over its
ceiling, `✅` when it is done and left none. Then tell the person their
next steps, each command written as this host invokes commands. Tell
them to use what the delivery changed, as its user would, and to say
here what is wrong. Tell them to review the staged diff, then to commit
with the suggested message, merging a delivery branch as docs/05 §5
says. Then run the queue script of docs/05 §4, though no one asked, and
show its trees as §4 says, its `next:` command written for this host.
End saying which environment is at which version and the command that
updates the others; never end silent.
