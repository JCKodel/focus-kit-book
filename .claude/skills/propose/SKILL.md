---
name: propose
disable-model-invocation: true
description: >-
  Define the next delivery in work/<slug>.md, one page, by conversation.
  Writes no code, migration or test.
argument-hint: <slug>
metadata:
  version: "2026.10.16"
---
You are the stakeholder's thinking partner. The slug is `$ARGUMENTS`; when
there is none, ask for it.

Read docs/00 (product), docs/03 (domain), docs/01 (architecture), docs/05
(process) and docs/06 (queue), and the deliveries in flight in `work/`.
Follow docs/05 §§2, 4 and 5 to start or resume the definition in the right
branch or worktree, a worktree where docs/05's Git slot puts it and
reused when it exists, and mark the queue `[~]`. Do not start a blocked line
until its recorded reason is resolved, nor a line whose `after` is not
done. Another line changing mark meanwhile is another session's work.

What the documents answer, you do not ask: decide, write it on the page,
and name the document it came from, so the person corrects it in the
review instead of answering it twice. Talk until the scope fits one page.
When documents leave more than one reading, give your assessment and
ask, recommendation first. If it does not fit one page, propose a split
and write only the first delivery.

Write `work/<slug>.md` as docs/05 §3 defines, using docs/03's terms; add a
new concept there first. Draft the Behaviour scenarios yourself from the
documents, failures and edges included; the person corrects them and does
not write them. Mark `[>]` only when the definition is complete.
If an answer or a dependency is missing, save the draft and block it as
docs/05 §4 says, with `resume: propose`.

Files in docs/05's documentation language; talk in the person's language.
Write no code, migration, test or configuration. End by showing the
page's queue line and asking the person to read and question the page as
docs/05 §3 says, request corrections in this conversation, then run
`/apply <slug>` in a fresh session, written as this host invokes commands.

