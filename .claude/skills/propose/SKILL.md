---
name: propose
disable-model-invocation: true
description: >-
  Define the next delivery in work/<slug>.md, one page, by conversation.
  Writes no code, migration or test.
argument-hint: <slug>...
allowed-tools: Bash(git:*)
metadata:
  version: "2026.10.20.5"
---
You are the stakeholder's thinking partner. The slugs are `$ARGUMENTS`:
none, ask for one; several, one subagent per slug, opened at once where
docs/05 §4 allows, each taking its slug from the message that opens it and
running on the word of the person who typed the command, which names them all.

Read docs/00 (product), docs/03 (domain), docs/01 (architecture), docs/05
(process) and docs/06 (queue), and the deliveries in flight in `work/`. Do
not start a blocked line until its recorded reason is resolved, nor a line
docs/05 §4 says waits, by its token or its `after`; a `[~]` line is
resumed only on the person's word that its session ended. Otherwise claim
the line as docs/05 §2 says: run
`git -c "alias.fk=!sh .agents/skills/propose/scripts/claim.sh" fk <slug> <strategy>`,
the strategy being what docs/05 §5's Git slot says, `trunk`, `branch` or
`worktree <hidden> <prefix>`. Continue at the path it prints; your first
edit there marks it `[~]`. If git cannot find `sh`, Git for Windows was
installed without its shell: say so and stop.
Follow every slot of docs/05 §5 that names this command, the project's own
included. Another line changing mark meanwhile is another session's work.

What the documents answer, you do not ask: decide, write it on the page
and name the document, so the person corrects it in the review instead of
answering twice. Talk until the scope fits one page; where documents leave
more than one reading, give your assessment and ask, recommendation first;
if it does not fit one page, propose a split and write only the first.

Write `work/<slug>.md` as docs/05 §3 defines, using docs/03's terms; add a
new concept there first. Draft the Behaviour scenarios yourself from the
documents, failures and edges included; the person corrects them and does
not write them. Mark `[>]` only when the definition is complete.
If an answer or a dependency is missing, save the draft and block it as
docs/05 §4 says, with `resume: propose`.

Files in docs/05's documentation language; talk in the person's language.
Write no code, migration, test or configuration. End by showing the
page's queue line and asking the person to read and question the page as
docs/05 §3 says, with corrections in this conversation. Then give
`/apply <slug>` for a fresh session, written as this host invokes commands,
opened in the delivery's worktree, if any, its path written out.
