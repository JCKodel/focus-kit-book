# Questions: cost, run 1

Each time the agent asked something, its message (the last text block of that turn, byte for byte) and the answer sent, which uses only the lines of `../brief.md` or "Use your judgment.".

## Asked in turn 2, answered in turn 3

Asked:

    I'll hold off on further changes. I've already written `CLAUDE.md` (uncommitted), so these questions are about whether it fits how you'll use the agent. Each has my current assumption in brackets, so you only need to answer where I'm wrong.

    1. **Who's asking, and where?** Is it the dev team in a terminal, or also Juno, Odile or Wren, maybe through Slack? That decides the tone. It also decides whether answers should cite `file:line` or explain rules in desk language. *(Assumed: the dev team, so code citations.)*

    2. **How does the agent run?** Is it an interactive Claude Code session, a scheduled cloud routine, or something triggered from chat? If it runs unattended, it can't get approval for commands, the same block I hit. Should I allow read-only commands like `npm test`, `git log` and `grep` in `.claude/settings.json`? *(Assumed: nothing pre-approved, so the agent only reads files.)*

    3. **Answer only, or also maintain?** I told the agent never to edit code or notes. Should it be allowed to fix the notes I found wrong? Those are the `retro-march.md` line, the stale "open" items in `questions for odile.md` and ADR 2's link to a missing file. Or should it keep a log of questions it couldn't answer, or update `CLAUDE.md` when a new decision lands? *(Assumed: strictly read-only.)*

    4. **Are my "known inconsistencies" calls right?** In particular: is the `retro-march.md` claim that overdue-blocks-checkout was merged on 25 March simply wrong? Or did a version land in March, get rolled back in April, and come back in June? I can't tell from the notes, and I've told the agent to treat the retro line as an error.

    5. **Is anything missing from the repo?** Examples: the rules list Bex keeps, the plain-language error messages Juno drafted with Wren, `rafe-notes-error-handling.md`, or the tracker and chat. If those live somewhere the agent can reach, it should know about them. If they don't, it should say "not in the repo" rather than guess.

    6. **How will `CLAUDE.md` stay current?** Q4 work (persistence, reports, UI) will add code and decisions. Who owns updating the guide? Should it point the agent to a convention instead, e.g. "new decisions go in `notes/` with a date and a `Supersedes:` line"? *(Assumed: someone on the team updates it by hand.)*

    7. **Commit it?** Should I commit `CLAUDE.md` to `main`, put it on a branch or PR, or leave it for you to review?

Answered:

    1. The questions come from developers and the product owner, about 20 a day.
    2. Each question opens a fresh session. Use your judgment.
    3. Use your judgment.
    4. Use your judgment.
    5. Use your judgment.
    6. The notes keep growing. Use your judgment.
    7. Use your judgment.
