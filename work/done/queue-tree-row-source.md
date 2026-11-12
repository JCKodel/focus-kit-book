# queue-tree-row-source

**Objective.** The author reads docs/03's `queue tree` row and ADR-0018's `kit-2026-10-24` amendment and finds the no-slug rule and /apply's ending cited to the skills that hold them, propose's and apply's `SKILL.md`, and docs/05 §4 cited only for what it holds: the tree and the offer of several slugs with its cost. Finding R2-4 of `work/done/m32-review.md`.

**Behaviour.**

* Reading docs/03's `queue tree` row (:121), the author finds "/propose and /apply typed with no slug show it and ask" followed by "as propose's and apply's `SKILL.md` say", and "/apply ends with it" followed by "as apply's says"; the row still ends "since focus-kit 2026.10.24 (docs/05 §4)", which covers the tree drawn and the offer.
* Reading ADR-0018's `kit-2026-10-24` amendment (:88), the author finds the same two cites in the same sentence, which still ends "(docs/05 §4)" after the offer and its cost.
* Opening `.agents/skills/propose/SKILL.md` :13 and `.agents/skills/apply/SKILL.md` :12, the author finds the no-slug rule ("None: show what may run now as docs/05 §4 says and ask"); opening apply's :84, the ending ("Then run the queue script of docs/05 §4, though no one asked"). At focus-kit 2026.10.24 (`ef990c3`) both skills held the no-slug rule too, and apply's ending was its own "then what may run next, as docs/05 §4 says", so the dated amendment holds as cited.
* Edge: every other sentence of the row and of the amendment reads as before; the amendment's heading and date stay.
* Edge, the shared tree: the sibling lines under `m32-review` may run in the same tree on chapters 8, 12, 13, 14 and 19; their files are theirs, and this delivery stages only its paths and its own line of docs/06.
* Fails: an anchor not found exactly once in its file; a chapter, docs/05, a skill or another ADR touched; an em dash; any line of docs/06 changed but this line's mark.

**Contract.** Two exact replacements, each anchor counted once in its file at HEAD `ec6258a`; each stays on its line, the rest of each file untouched.

`docs/03-Domain.md`, the `queue tree` row (:121):

1. "/propose and /apply typed with no slug show it and ask, /apply ends with it, and the free lines are offered as one command with several slugs, each slug one more agent costing as much as one session; since focus-kit 2026.10.24 (docs/05 §4)." becomes "/propose and /apply typed with no slug show it and ask, as propose's and apply's `SKILL.md` say, /apply ends with it, as apply's says, and the free lines are offered as one command with several slugs, each slug one more agent costing as much as one session; since focus-kit 2026.10.24 (docs/05 §4)."

`docs/adr/ADR-0018-six-marks.md`, the `kit-2026-10-24` amendment (:88):

2. "/propose and /apply typed with no slug show it and ask, /apply ends with it, and the free lines are offered as one command with several slugs, each slug one more agent costing as much as one session (docs/05 §4)." becomes "/propose and /apply typed with no slug show it and ask, as propose's and apply's `SKILL.md` say, /apply ends with it, as apply's says, and the free lines are offered as one command with several slugs, each slug one more agent costing as much as one session (docs/05 §4)."

Sources: `.agents/skills/propose/SKILL.md` :13 and `.agents/skills/apply/SKILL.md` :12 and :84 at `ec6258a` (2026.11.12); the same files at `ef990c3` (2026.10.24), propose :13 and apply :11 "none, show what may run now as docs/05 §4 says and ask", apply's last paragraph "then what may run next, as docs/05 §4 says"; docs/05 §4 at `ec6258a`, "Asked what may run now, run ... queue.sh ... and show its tree" and "Offer the free lines as one command with several slugs, saying each slug is one more agent and costs as much as one session", with no no-slug rule and no /apply ending; focus-kit's CHANGELOG.md, entry 2026.10.24, "`/propose` and `/apply` typed with no slug show that tree and ask, `/apply` ends with it, and docs/05 §4 says to run it whenever a person asks what may run now".

Terms: queue tree, as docs/03 has it; no row added. No chapter, no case, no number, no code example.

**States.** Inapplicable: documents, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* R2-5, "each under the last line it waits on" without `queue.sh`'s condition: dropped by `m32-review` as latent.
* The row's and the amendment's other clauses, the `(PA)` token mention included: not part of R2-4.
* Chapters 12, 13 and 14, which teach the no-slug rule: they cite no file for it.
* `work/done/m32-review.md`: it quotes the finding and stays as written.

**Decisions from the documents.**

* The finding and its cites: `work/done/m32-review.md`, R2-4, and its line bullet "`queue-tree-row-source` (PA): R2-4, one sentence in docs/03 and ADR-0018".
* The skill named as "propose's and apply's `SKILL.md`", the form `work/done/m32-review.md` uses (:29, :148).
* No `make book`: no chapter changes; Proof is verify green (docs/05 §5, Proof of a screen, for chapters; this delivery has no screen).

**Decisions taken alone.** The agent chose each of these; the author corrects them in the review. This page was written and built by the agent before the author read it, on the author's word to run the queue.

* Each cite sits after its own clause, and the closing "(docs/05 §4)" stays where it was, covering the tree and the offer, rather than one cite to "the skills" over both clauses: the no-slug rule is in both skills, the ending only in apply's.
* ADR-0018's amendment is corrected in place, as the finding asks, rather than by a new amendment: the change is a citation, and what the book runs did not change.
* The skills are cited at `.agents/skills/`, the kit's install path the row's own script cite uses; `.claude/skills/` holds the same files.

**Done when.**

- [x] Both replacements made, each anchor found once before and its replacement once after.
- [x] No other line of docs/03 or ADR-0018 changed; no chapter, skill or docs/05 touched.
- [x] `make verify` green, its time recorded.
- [x] Delivery review by a read-only agent on Opus, its findings fixed or noted.
- [x] Page in `work/done/`, line `[x]` staged, only this delivery's paths staged.

## Outcome

* Built as defined: both replacements made, each anchor found once at `ec6258a` and its replacement once after; no other line of docs/03 or ADR-0018 changed. No divergence, nothing dropped.
* Proof: `make verify` green, exit 0, in 59 seconds of wall time (11 seconds of user time), under the five-minute ceiling. No chapter changed, so no `make book`.
* Delivery review: a read-only agent on Opus read `git diff HEAD` of docs/03, ADR-0018 and this line's hunk of docs/06, and this page, against the page and docs/04. It found no defect: the replacements match the Contract, and the cites hold at `ec6258a` and at `ef990c3`. Its one optional point, writing "as apply's `SKILL.md` says" for "as apply's says", was not taken: the clause before names the file. Its report says it used no advisor.
* The decisions taken alone are above, for the author's review.

```commit
docs(queue-tree-row-source): cite the skills for no slug and the ending

- docs/03 queue tree row: no-slug rule and /apply's ending cite the skills
- ADR-0018 kit-2026-10-24 amendment: the same two cites, in place
- docs/05 §4 still cited for the tree and the offer of several slugs

work/done/queue-tree-row-source.md
```
