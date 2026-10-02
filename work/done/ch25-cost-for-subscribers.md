# ch25-cost-for-subscribers

**Objective.** A reader on a fixed subscription knows from chapter 25 what the challenge protocol costs them (time, output tokens and a share of the plan's session limit), and no price in dollars reads as the bill of their own session.

Finding C4 of `m9-review`: "the USD values say nothing to me, who pays a fixed subscription (and a session costing USD 8 is something scary for this context)". The USD 8.00 is three sessions summed, at the API's per-token price the host reports (`total_cost_usd`), so the chapter misled twice.

**Behaviour.**

* A reader finds in chapter 25 no amount in dollars: no `USD`, no `$`, in either edition. The experiment's prices stay in its record, which the note already opens.
* A reader learns what the protocol cost in time and in output tokens, per arm (the three runs of an arm summed, said so): the challenged sessions took 2.9 to 8.8 times as long as the first answers and wrote 2.7 to 9.4 times the output tokens. Where the chapter rounds (the opening line, the gain, the key point), it writes "about 3 to 9 times".
* A reader sees one session's size, said to be per session, so no sum reads as one session: a first answer took 24 seconds to just over 2 minutes; a challenged session 3 to 9 minutes.
* A reader on a subscription learns that the protocol spends their plan's session limit, with the experiment's own case: the nine challenged sessions, run in about 45 minutes, ran out the author's plan before the protocol's last turn, which was sent again about 30 minutes later. The chapter does not say that one protocol runs out a plan, and does not name the plan.
* A reader who pays per token is pointed to chapter 23 to turn tokens into a price, with no price given in chapter 25.
* The cost arm's use is said in time and output tokens, both, and run 3 is not merged into one sign: in runs 1 and 2 the challenged setup answered the five questions in 26% and 18% less time with 27% and 29% fewer output tokens; in run 3, in 14% less time with 9% more output tokens. All 30 answers correct, as today.
* Line 65 no longer says the team "pays for every token": each question opens a fresh session and spends tokens, from the bill or from the plan's session limit. Line 98 ("when the cost is tokens") reads the same way for both kinds of payer.
* The advice of when to send the protocol stays; it reads as spending time and the plan's limit where the result pays it back.
* The Portuguese edition says the same, with the same numbers in its own format (2,9; 8,8).

**Contract.**

* Files: `book/en/25-asking-for-more.md` and `book/pt/25-asking-for-more.md`. Only these sentences change, in both editions: the opening value line (en line 4), the cost-arm task sentence (line 65), Turn 3's techniques sentence (line 98), §What the protocol bought, and what it cost from "The challenge was paid for in tokens" to the cost arm's use (lines 121 to 126) plus a paragraph on the session limit, the advice paragraph if its wording needs it (line 132), §What the team gains (line 139) and the key point (line 148). The section titles stay.
* Numbers, all from `work/done/ask-for-more-experiment-run/README.md`, through the existing note `[^ask-for-more-run]`:
  * per arm, time: limit 201 s to 1,337 s (6.65), audience 81 s to 710 s (8.77), cost 390 s to 1,130 s (2.90);
  * per arm, output tokens: limit 24,220 to 147,419 (6.09), audience 7,376 to 68,989 (9.35), cost 41,420 to 110,334 (2.66);
  * per session: first 24 s (audience-2) to 132 s (cost-3); challenged 181 s (audience-3) to 526 s (limit-1);
  * cost arm, five questions per setup, first to challenged: seconds 53 to 39 (-26%), 60 to 49 (-18%), 81 to 70 (-14%); output tokens 4,746 to 3,448 (-27%), 5,545 to 3,961 (-29%), 5,997 to 6,537 (+9%);
  * session limit: §What diverged, protocol turn 4 hit "You've hit your session limit" in all nine runs; runs on 2026-10-02 between UTC 16:26 and about 17:10; resent about 30 minutes later.
* Terms of docs/03: `session limit` / `limite de sessão`, added by this proposal. `challenge protocol`, `token` already there.
* Sources: the run record only; no new note. Cases: none (Case A's Teams card is not touched). Exercises: none.

**Out of scope.**

* The record's USD columns (`work/done/ask-for-more-experiment-run/`): a record of what the host reported, not reader text.
* Chapter 23: it teaches per-token billing and is the pointer target; a subscription passage there is another delivery if wanted.
* Naming the plan or its limits: they change and the number would go stale.
* What the protocol is and where its turns are written: `ch25-protocol-findable`.
* The prologue: it plants the idea and gives no cost.

**Done when.**

* [x] Both editions changed in the sentences the Contract lists; every number above appears as written and matches the README.
* [x] `grep -nE 'USD|\$' book/*/25-asking-for-more.md` prints nothing.
* [x] The chapter still opens with its value; no filler, nothing useful cut.
* [x] `make verify` green.
* [x] `make book`, and the author is given the paths of both PDFs to read chapter 25.
* [x] docs/06: `ch25-cost-for-subscribers` is `[x]`; the page is in `work/done/`.

## What happened

* **Line numbers.** The Contract's line numbers predate `ch25-protocol-findable`, which added lines above; the same sentences were changed (en lines 5, 66, 105, 128 to 141, 139, 146, 155 before this delivery). Every listed sentence changed, the advice paragraph included ("spend the protocol's time and tokens where the result pays them back"; "a setup that spends tokens on every question" in place of "paid for").
* **The 45 minutes.** The record's window, UTC 16:26 to about 17:10, holds all nine runs and their measurements, the resent turn 4 included; it is not the duration of the challenged sessions alone. The chapter says the nine challenged sessions ran "on one afternoon, all within about 45 minutes", the plan ran out before the last turn, and the turn was sent again about 30 minutes later, without implying the two spans add up.
* **Per-arm numbers.** Written as "first against challenged" pairs (201 against 1,337 seconds, and so on) after the rounded ratio, so the reader sees what was summed; the ratios 2.9 to 8.8 and 2.7 to 9.4 are the README's sums divided.
* **The session-limit paragraph** defines the term in one clause (docs/03, `session limit`, added by /propose) and ends with one sentence that each protocol spends a share of that limit; it does not say one protocol runs out a plan, and names no plan.
* **The key point** also says a subscriber pays the protocol from the plan's session limit, so the point a skimming reader keeps covers the subscriber.
* **Proof.** `make verify` green on the second run; the first failed only on an HTTP 503 from GitHub for the LICENSE link, which this delivery does not touch. `make book` built both PDFs. The USD grep prints nothing.
* **Dropped:** nothing.
