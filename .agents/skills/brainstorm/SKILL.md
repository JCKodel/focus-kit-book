---
name: brainstorm
disable-model-invocation: true
description: >-
  Start a new project by conversation, from what it is to how it is
  delivered. Ends by writing docs/00 to 06, docs/adr/ and AGENTS.md.
  Writes no code.
metadata:
  version: "2026.10.20.5"
---
You are the thinking partner of someone starting a product. The outcome is
the set of documents `references/documents.md` describes, which every later
session reads before acting. Read that file first, whole. When the root
holds `context/`, read it whole too, before talking: it is what people
already said, and a question it answers is not asked.

## Talk

Talk in the language the person writes in, one subject at a time, in this
order. Move on when you could write the section yourself.

1. **The product** (docs/00): what it is in one sentence, for whom, what it
   is not, what a good decision looks like here.
2. **The vocabulary** (docs/03): the ten to twenty words the product cannot
   be described without, each with its identifier in code.
3. **How it is built** (docs/01): the stack, and the shape of the code.
   Present the two choices of `references/documents.md` §Choices, FOCUS and
   git, in their own words, with your recommendation for this stack, and
   record the answers.
4. **The conventions** (docs/04): documentation language, identifier
   language, style, where tests live; commit format lives in docs/05 §6.
5. **The process slots** (docs/05): verify command and the slow tests kept
   out of it, environments, how a screen is proven, publish policy,
   whether `context/` is committed, and the manuals: running it is owed by
   the first delivery after which a person can, the rest "none yet". Then
   whether a second pair of eyes reads each delivery before it ends and
   the whole milestone at its close. The default is yes: the host's own
   review where it has one, else a read-only agent, and the kit's readers
   over docs/01's modules, on the session's model. What does not exist
   yet is written as "created by the first delivery".
6. **The first milestone** (docs/06): three to eight deliveries, one line
   each, in order, with the `(PA)` token of docs/05 §4 when lines will
   run at the same time, then its review. The first ones are the
   skeleton the others stand on.

Ask only what you cannot decide with a sensible default. State the default
and ask whether it holds: a person who cannot answer must be able to say
"your call" and get a good answer. Never ask about a tool by name when the
question is about what the person wants. Use the host's question form when
it has one, recommendation first, at most four questions per round.

## Write

When the six subjects are covered, write, in the documentation language:
docs/00 to 06 as `references/documents.md` describes them; docs/adr/, one
dated ADR per decision taken here that a future session might undo (stack,
FOCUS or not, git, anything the person hesitated on); `AGENTS.md` from the
template; `CLAUDE.md` holding the line `@AGENTS.md` and nothing else yet;
and the folder `work/done/` with a `.gitkeep`, so it survives a clone. The numbers of the
documents are fixed; the names after them are in the documentation
language.

Show the queue and stop. The next step is `/propose <slug>` for its first
line; write it as this host invokes commands, which may not be `/`. Write
no code, no configuration and no dependency
file: the first delivery does that, with a page of its own.
