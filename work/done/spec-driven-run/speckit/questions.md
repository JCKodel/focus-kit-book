# SpecKit: questions and answers

SpecKit asked no question in the run that counts (permission mode `auto`).

| Step | Question asked |
|---|---|
| `/speckit-constitution` | none |
| `/speckit-specify` | none; the tool reports "no open clarification questions" and records its own assumptions in the spec (24 hours inclusive, a slot as one start time, ownership checked first) |
| `/speckit-plan` | none |
| `/speckit-tasks` | none |

Where the brief leaves a choice open, SpecKit chose without asking and wrote the choice into its files, and the optional `/speckit-clarify`, which exists to ask, was not run (see `../README.md`).

## Discarded attempt

A first `/speckit-constitution` in `acceptEdits` stopped without writing: the template script `.specify/scripts/bash/resolve-template.sh` needs Bash, which that mode denies. The step was repeated in `auto`; nothing had been written.
