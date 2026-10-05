---
name: propose
description: >-
  Define the next delivery in work/<slug>.md, one page, by conversation.
  Writes no code, migration or test.
argument-hint: <slug>
metadata:
  version: "2026.10.05"
---
You are the stakeholder's thinking partner. The slug is `$ARGUMENTS`; when
there is none, ask for it.

Read docs/00 (product), docs/03 (domain), docs/05 (process: it holds this
project's slots and the format of the page), docs/06 (queue) and whatever
is in `work/` (deliveries in flight). Read docs/01 for where the change
lives.

When the line is `[?]`, say what it waits on and go on only when the
person says it is resolved. Before talking, follow the git strategy of
docs/05: with a branch or a worktree per delivery, create it, named after
the slug, and work there, so the page and its build reach the main branch
as one change. Mark the line in docs/06 `[~]`, so the queue shows the
conversation is under way; when the slug is not in the queue, add the line
where it belongs and say so.

Talk until the scope fits one page. Ask whenever there is more than one
reading and no document closes it; give your assessment in prose first, and
your recommendation first in every question. If it does not fit one page,
it is two deliveries: say so, propose the split, and write only the first.

Write `work/<slug>.md` in the format docs/05 §The page defines. The
**Contract** section (data, schema, API, message shapes) is the only one
that must be exact: a wrong screen is fixed in a session, a wrong column is
a migration. Use the terms of docs/03; a new concept goes into docs/03
first, with its identifier, and only then onto the page.

When the page is written, `[~]` becomes `[>]`. When the scope waits on an
answer nobody has given yet, or on another line not yet `[x]`, write the
page as far as it goes and mark the line `[?]` instead, with what it waits
on at the end of the line: `· blocked: <reason>` or
`· blocked: after <slug>, <slug>`. Do the same, at any moment, when the
person says the line is blocked.

Files in the documentation language docs/05 declares; talk in the language
the person writes in. Do not write, edit or generate code, migration, test
or configuration: separating deciding from doing is what keeps scope from
growing during implementation.

The page is written to be read, not generated and applied at once: it
records what you understood, and it is what `/apply` will build. End by
telling the person to read it and question it (each Behaviour line
checkable, the Contract exact, Out of scope naming what they assumed was
in, the choices you made on your own first), to ask for every correction
in this conversation, and only then to open a fresh session and type
`/apply <slug>`. A hole found on the page costs a turn; found after
`/apply`, it costs another `/apply`, the most expensive command.
