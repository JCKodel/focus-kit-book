# Checks for the question-answering agent

Questions with known answers. Most are traps: an older note gives the wrong answer. Ask a few in fresh sessions after changing `CLAUDE.md` or after a rule changes, and compare. If a rule changes, update the expected answer here too.

| Question | Correct answer | Wrong answer it might give, and why |
|---|---|---|
| How long overdue before a member is suspended? | More than 14 days (14 = no, 15 = yes), `features/loans/suspension.ts` | 28 days or "four weeks" (02-11, 04-08, ADR-004); 30 days (holds draft) |
| Can Wren lift a suspension, or only Odile? | Any librarian, but only once nothing is overdue | Only the head librarian (01-26, 02-11, 04-08) |
| Can a member with an overdue book borrow another? | No, `member-has-overdue-loans` (06-16) | Yes, until suspended (04-08, questions Q2) |
| When did "overdue blocks checkout" go in? | 16 June 2026 | March (`retro-march.md` is wrong) |
| How many renewals, and from which date? | Max 2, each adding 21 days to the current due date | Unlimited (kickoff); from today (Rafe's first version) |
| Is a loan overdue on its due date? | No, from the day after | Yes (bug fixed 06-02) |
| What's the fine per day? | There are no fines (ADR-004) | 0.20 per day (kickoff, Loan Service Design) |
| How do holds work? | They don't exist; there's only a draft, revisited in December | Describes the draft as if it were built |
| Can a librarian borrow books? | Only by registering separately as an ordinary member | Yes, as a librarian |
| Do due dates skip days the library is closed? | No; staff handle closures by hand | — |
| Who decided the deposit policy for the local history collection? | There's no deposit policy; those items never leave the building (ADR-004 notes). Anything beyond that: ask Odile via Juno | Invents a policy |
