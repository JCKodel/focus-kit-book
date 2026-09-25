# Process

How an idea becomes code in Clinic Weigh-in.

## 1. The rule

One delivery is one page, `work/<slug>.md`. If it does not fit one page,
it is two deliveries. The page is not a concision goal: it is the test that
the scope was understood. A scope that needs five pages has not been
decided yet.

## 2. The flow

docs/06 → /propose <slug> → work/<slug>.md → /apply <slug>, in a fresh
session → verify green, environments as §5 says → work/done/<slug>.md and
git add → a person reviews and commits.

/propose talks and writes the page, never code. /apply builds, proves,
updates the documents, stages and suggests the commit, never commits.

## 3. The page

    # <slug>

    **Objective.** One sentence: what the user can do afterwards.

    **Behaviour.** Verifiable scenarios in user language. Each line becomes
    a test or a manual check.

    **Contract.** Data, schema, API, message shapes, or "none". The only
    section that must be exact.

    **States.** Empty, loading, error, offline: one line each, or "the
    defaults". Only when there is a screen.

    **Visual reference.** Where the design is, and the viewports. Only when
    there is a screen.

    **Out of scope.** What does not enter, half a line of reason each.

    **Done when.** A mechanical checklist: tests X pass; verify green;
    screenshot matches Y.

After /apply the page also records what happened: what diverged, what was
dropped, what the proof found, the decisions taken.

## 4. The queue

docs/06: one line per delivery, in order, under milestones. The line never
leaves the queue; it changes mark: `[ ]` not defined, `[>]` defined and not
built, `[x]` done. Edited by conversation in any session.

## 5. This project

* **Documentation language:** English. Identifiers in English.
* **Verify:** created by the first delivery, `verify`: it type-checks with the
  TypeScript compiler and runs `node --test`. Until then `npm test` is the only
  command, and it finds no tests. Green before anything is declared done.
* **Environments:** Local, the only one: Node runs the module and its tests; a
  delivery leaves verify green there.
* **Proof of a screen:** no screens.
* **Publish policy:** nothing is published; there is no environment beyond local.
* **Git:** trunk. Everything on `main`, one delivery at a time. The agent
  stages; it never commits or merges.

## 6. Commit

The agent stages and suggests the message; the person commits after
reviewing. Imperative subject up to 72 characters, scope in parentheses
when it helps; body up to five one-line bullets, the highlights and not
the reasoning; last line points to `work/done/<slug>.md`, where the
reasoning lives.

## 7. What this process does not have

No formal spec, no spec delta, no change folder, no numbered tasks, no
gate before implementation, no specialized subagent, no tool the
deliveries did not ask for. When one of these is proposed, the question
is: which concrete error would it have caught? The answer names an error
that happened.

## 8. Closing a milestone

When a milestone closes, review the whole with what the host offers, and
each confirmed finding becomes a line in the queue, not a fix in the middle
of the next milestone.
