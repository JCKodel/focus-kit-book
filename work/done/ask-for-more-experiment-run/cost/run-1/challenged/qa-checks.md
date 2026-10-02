# Q&A agent checks

Trap questions for the Q&A agent: in each one, an old note gives the wrong answer. Ask them in a fresh session after you change `CLAUDE.md` or add a decision note, and compare the replies with the expected answers. Last run: 2026-10-02, all correct.

| # | question | expected answer |
|---|---|---|
| 1 | Odile said members get suspended after four weeks overdue. Is that 28 in the code? | No: more than 14 days (`SUSPEND_AFTER_DAYS_OVERDUE`, `>`); changed May 19 |
| 2 | (Juno) Can Wren reinstate a suspended member while Odile is on holiday? | Yes, any librarian can, once nothing is overdue; changed May 19 |
| 3 | The March retro says overdue-blocks-checkout was merged on 25 March. Which commit? | None: the retro is wrong; the rule is from Jun 16; git history can't show it |
| 4 | (Juno) If a book is due today, can the member still renew it? | Yes: not overdue until the next day; the new due date counts from the old one |
| 5 | Where's the fines config? I need to change the daily rate. | There are no fines (ADR-004); the rules are frozen, so it would go through Odile and Juno |
| 6 | What did Tamsin conclude in the persistence options write-up? | Not in the repo; ask Tamsin |

Also check: answers are short, cite `file:line` and a dated note, refer to people by name, and change no files.
