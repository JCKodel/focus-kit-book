# ch10-usage-share

**Objective.** A reader of chapter 10 can judge the `/usage` figures and the ratio drawn from them, because the text says what each percentage is a share of and that the ratio compares totals, not single runs.

**Behaviour.**

* In §"Read the page before `/apply`", after the sentence with the four figures, one sentence says what they are: each is the command's share of all my Claude Code usage in that window, counted as the subscription counts usage against its limits; the rest of the usage, 52% and 39%, went to work outside the two commands.
* The ratio sentence says it compares the totals spent on each command in the window, not the cost of one run: `/apply` took from twice to more than three times what `/propose` took. The point it makes stays: `/apply` is where the usage goes, so a hole is cheaper to find on the page.
* "Approximate" and "all my projects together" stay, said once, in the text or in the note, not in both.
* The reader who opens `usage.txt` finds the figures under "What's contributing to your limits usage?" and "Top skills", as the text describes them.
* Both editions say the same.
* Finding F13 of the M3 review is settled.

**Contract.**

* Files: `book/en/10-propose.md` and `book/pt/10-propose.md`, lines 250 to 251 today; the note `[^claude-usage]` (line 473 in English, 475 in Portuguese) only if a fact moves between text and note.
* Figures: unchanged, from `work/done/propose-run/usage.txt`: `/apply` 32% and `/propose` 16% over the last 24 hours, 47% and 14% over the last 7 days; the rest, 52% and 39%, is 100 minus their sum.
* Sources: `[^claude-usage]`, already cited; no new note.
* Terms of docs/03: none new.
* Cases, exercises: unchanged.

**Out of scope.**

* The cost of one run of each command: `usage.txt` does not count runs; chapter 24 (`cost-and-where`) measures tokens per delivery.
* A new reading of `/usage`: the figures stay those read on 2026-09-28.
* The rest of the section (the questions and the second agent): `headless-runs` covers the second agent.

**Done when.**

* [x] Both editions say what the figures are a share of and that the ratio compares totals, same meaning.
* [x] Every number matches `usage.txt`.
* [x] `make verify` green, the link check included.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

## What happened

* English, after the four figures: "Each figure is the command's share of all my Claude Code usage in that window, counted as the subscription counts usage against its limits; the rest, 52% and 39%, went to work outside the two commands. So the ratio compares the totals each command took in a window, not the cost of one run: `/apply` took from twice to more than three times what `/propose` took. That is where the usage goes, and why a hole is cheaper to find on the page." Portuguese says the same.
* "Approximate" and "all my projects together" left the text: the note `[^claude-usage]` already says both, so it stays unchanged. "But the ratio is what matters" was dropped with them.
* Numbers checked against `usage.txt`: the figures are under "What's contributing to your limits usage?", in the "Top skills" line of each window; 100 - (32 + 16) = 52, 100 - (47 + 14) = 39; 32/16 = 2, 47/14 ≈ 3.4.
* Nothing else diverged from the plan, no document changed: no new term, no rule, no decision. F13 of the M3 review is settled.
* Proof: `make verify` green, `make book` built both PDFs.
