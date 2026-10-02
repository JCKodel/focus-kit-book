# Scores

Filled blind before the key was applied, by a fresh headless session per pair (model `claude-opus-5-5`, read-only), not by the author: the author handed the judging to the agent (see `README.md`). Each session saw the request, `<arm>/brief.md`, the rubric's criteria and the two answers as `X/` and `Y/` (the files plus `answer.md`, the agent's last message of that state); the audience judge also had the report, the cost judge the starting project. The column State is the key of `blind/key.md`, applied after all nine scores were recorded. Scores 1 to 5; Sent is the judge's answer to "Which would you send, X or Y?"; Why is its one sentence.

### limit

| Pair | Side | State | asked | small app | phone | Sum | Sent |
|---|---|---|---|---|---|---|---|
| limit-1 | X | challenged | 4 | 5 | 4 | 13 | yes |
| limit-1 | Y | first | 4 | 3 | 3 | 10 |  |
| | | | | | | | Why: X's card looks like a small app and works on the phone, as the brief asks, while Y is a correct but plain tabbed list whose right-hand date columns crowd small screens. |
| limit-2 | X | challenged | 5 | 3 | 5 | 13 | yes |
| limit-2 | Y | first | 4 | 4 | 2 | 10 |  |
| | | | | | | | Why: X's single-column layout with a selected-tab marker that is always visible works on phones as well as desktop, while Y's two-column rows with unwrapped text would be cramped on a phone and its selected-tab highlight may not show in Teams. |
| limit-3 | X | first | 4 | 3 | 4 | 11 |  |
| limit-3 | Y | challenged | 4 | 5 | 4 | 13 | yes |
| | | | | | | | Why: Y meets the request and makes far better use of what Teams cards can do (styled tabs, icons, inline Renew/Pay buttons, compact rows) to give the app-like look the library wants, though its message is too long and refers to rounds the person never saw. |

### audience

| Pair | Side | State | decide in 10 min | nothing missing | figures match | Sum | Sent |
|---|---|---|---|---|---|---|---|
| audience-1 | X | challenged | 5 | 5 | 5 | 15 | yes |
| audience-1 | Y | first | 4 | 3 | 4 | 11 |  |
| | | | | | | | Why: X is built around the budget decisions, with the stakes for each, the budget drivers and the unaudited and unconfirmed-grant caveats, and its figures all match the report, while Y leaves those out and adds one unsupported 'record' claim. |
| audience-2 | X | first | 4 | 4 | 5 | 13 |  |
| audience-2 | Y | challenged | 5 | 5 | 4 | 14 | yes |
| | | | | | | | Why: Y sorts the seven decisions for a 10-minute phone read and adds the grant expiry, the unaudited status and a likely overstatement of fee income, outweighing a couple of loosely worded interpretive claims. |
| audience-3 | X | challenged | 5 | 5 | 5 | 15 | yes |
| audience-3 | Y | first | 3 | 4 | 5 | 12 |  |
| | | | | | | | Why: Both are accurate, but X leads with the seven decisions, management's recommendation, what happens to reserves under each choice and why the fee rise is reasonable, in a phone-friendly format that fits the board's 10 minutes. |

### cost

| Pair | Side | State | finds without reading all | stays right as notes grow | easy to keep up | Sum | Sent |
|---|---|---|---|---|---|---|---|
| cost-1 | X | first | 4 | 2 | 3 | 9 |  |
| cost-1 | Y | challenged | 5 | 4 | 4 | 13 | yes |
| | | | | | | | Why: Y covers the same rules in a leaner guide, adds a git check that spots new or changed notes, keeps answers short and reports a tested trial, which fits a growing set of notes and a per-token budget better than X's longer, static guide. |
| cost-2 | X | first | 3 | 2 | 2 | 7 |  |
| cost-2 | Y | challenged | 5 | 4 | 4 | 13 | yes |
| | | | | | | | Why: Y covers the same ground at about 60% of the per-session cost, points to the code instead of copying values, has the agent detect and report new notes, and tells the team how to keep the guide current. |
| cost-3 | X | first | 4 | 2 | 2 | 8 |  |
| cost-3 | Y | challenged | 5 | 4 | 4 | 13 | yes |
| | | | | | | | Why: Y keeps values in the code and adds a drift check, maintenance steps and a check file, so it stays correct and cheap as the notes grow, while X's copied rules table with line numbers will go stale silently. |

## Totals

| Arm | Score, first (of 45) | Score, challenged (of 45) | Sent: first | Sent: challenged |
|---|---|---|---|---|
| limit | 31 | 39 | 0 | 3 |
| audience | 36 | 44 | 0 | 3 |
| cost | 24 | 39 | 0 | 3 |

## Three tabs that switch (limit)

Checked from `card.json`, not in the Adaptive Cards Designer (see `README.md`): every card has three panels, one visible at the start, and `Action.ToggleVisibility` buttons whose every target exists in the card.

| Run | First | Challenged |
|---|---|---|
| limit-1 | yes | yes |
| limit-2 | yes | yes |
| limit-3 | yes | yes |
