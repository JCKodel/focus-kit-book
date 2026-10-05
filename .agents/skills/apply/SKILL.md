---
name: apply
description: >-
  Implement work/<slug>.md end to end: code, tests, verify, proof, docs,
  then stage and suggest the commit. Never commits.
argument-hint: <slug>
metadata:
  version: "2026.10.05"
---
Implement `work/$ARGUMENTS.md` in this session, completely. The page is the
scope; do not widen it.

Read the page, `AGENTS.md`, docs/01 (architecture), docs/04 (conventions)
and docs/05 (process). docs/05 holds this project's slots and you follow
them literally: the verify command, the environments and what a delivery
leaves up to date in each, how a screen is proven, the publish policy, the
git strategy. Work where the git strategy says: on the branch or worktree
`/propose` created for the slug, if any. If the page contradicts a
document, stop and say which: the document changes in the same delivery or
the page is wrong. Do not resolve it silently.

When the line is `[?]`, say what it waits on and go on only when the
person says it is resolved. Then mark the line in docs/06: `[>]` becomes
`[*]`, so the queue shows the build is under way.

When the work cannot go on, because it needs an answer nobody has given
yet, because another line must be done first (a fix you found becomes a
`[ ]` line above this one), or because the person says it is blocked,
stop: write into the page what was built and what it waits on, leave the
page in `work/`, mark the line `[?]` with `· blocked: <reason>` or
`· blocked: after <slug>, <slug>` at its end, then stage and suggest the
commit as below.

Build every piece where docs/01 says it goes, with the error convention
docs/01 names. Write the tests docs/04 asks for. Abstraction on the second
concrete occurrence, and the page says which was the first. Add no
dependency, layer or tool the page did not name. No em dash in any text a
user reads.

Run the verify command until it is green. Prove the delivery the way
docs/05 says (screenshot against the reference, end-to-end run, manual
check): list what diverges, fix it until only what you can justify
remains. Leave every environment as docs/05 requires, and never end silent
about them: the last thing you say is which environment is at which
version and the command that updates the others.

Then write into the page what happened: what diverged from the plan and
why, what was dropped, what the proof found, decisions taken (and the ADR,
if one). Update the documents the delivery changed: a new term into
docs/03, a new rule into the document that owns it, a decision into
docs/adr/. Tick every item of "Done when". Move the page to `work/done/`.
Mark the line in docs/06: `[*]` becomes `[x]`. A `[?]` line whose
`after` names only lines now `[x]` loses its suffix and goes back to
`[>]`, or `[ ]` when it has no page; say which.

`git add -A` and suggest the commit message in the format docs/05 defines.
Do not commit and do not merge, whatever the git strategy is. Files and
message in the documentation language; talk in the language the person
writes in.
