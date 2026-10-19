# ch22-cost-method

**Objective.** A reader can interpret historical token totals within their documented limits and measure future delivery costs using a matching window and session population.

**Behaviour.**

* The historical Ninjobs table retains its recorded input, cache-write, cache-read, output and total counts, with 221 sessions and 18,945 calls described as the author's historical count over the then-retained 21 days.
* The reader is told that the exact dates and session inclusion criteria were not recovered; no date is inferred from commits and no claim equates that population with the project's 93 completed pages.
* The section, opening, gain and key points no longer call 43.1 million total tokens, 149 thousand output tokens or 738 thousand tokens excluding cache reads a measured average per delivery; those averages and their baseline claims are removed wherever repeated in the chapter.
* Cache-read proportions and the average cache read per counted call remain reproducible from the same historical aggregate, clearly confined to that sample; no price or measured saving is inferred.
* To measure a new milestone, the reader records window boundaries and time zone, eligible sessions and calls (including proposals, retries and shared sessions), and the completed deliveries attributable to that same work; unmatched work is reported separately rather than divided by an unrelated page count.
* A fresh session reads the whole queue, including completed lines, so its starting context grows with that history; the chapter promises neither context nor bill bounded solely by the current delivery.

**Contract.** `book/en/22-cost-and-where.md` and `book/pt/22-cost-and-where.md`: opening, historical measurement section (rename to describe recorded token use), context explanation, Where an agent pays, How a team decides, gain and key points.
Retain the table's 271,807 input, 54,527,957 cache-write, 3,940,576,768 cache-read and 13,871,893 output tokens, total 4,009,248,425, and recompute its displayed proportions.
Existing provenance is the author's recorded count preserved by the chapter and `work/done/plain-numbers.md`; this delivery does not claim to have recounted absent logs.
The 93-page cut-off is documented by `work/done/rewrite.md`, but is not a denominator for this token sample and need not remain in this chapter; chapter 2 owns its separate historical observation.
Explain the existing deduplication rule for a Claude Code streamed answer (`message.id` plus `requestId`), without claiming that git records reconstruct missing session data.
Sources for queue reading: docs/05 §4 and the commands; terms remain those of docs/03.
No raw logs, private source paths, code or infrastructure enter the repository.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** New telemetry, another benchmark, vendor comparisons, changes to chapter 2's independently recorded page count, and claims about Case A: none establishes this missing sample boundary.

**Decision.** On 2026-10-18 the author chose to preserve the historical totals and remove averages per delivery.
Read-only inspection of available history did not recover the exact retained-log window or population; commits cannot supply missing host events.
The historical totals remain attributed observations with an explicit limitation, not a matched per-delivery measurement.

**Done when.**

* [x] Both editions pass every Behaviour check; all three per-delivery token averages and associated baseline claims are gone from this chapter, including its gain and key points.
* [x] Table totals, percentages and retained per-call arithmetic are recomputed and recorded; absent log verification is stated honestly.
* [x] The opening states reader value, gain matches the evidence, and no filler or useful measurement instruction is cut; every retained number keeps its provenance.
* [x] `make verify`, including disclosure, and `make book` pass; both PDFs are given to the author for passage review (docs/05 §5).

**Built.** Both editions of chapter 22. The opening promises a milestone's cost measured with a written window and session set, and what a fresh session carries and leaves out. The Ninjobs section is renamed "What Ninjobs recorded in tokens" (pt "O que o Ninjobs registrou em tokens"); it keeps the table and says the 21 days are the count's limit: their dates and the inclusion rule were not written down, the logs are gone, commits cannot rebuild calls to the model, so no per-delivery division is possible and a page count from another window would mix two samples. The 93-page division, 43.1 million, 149 thousand, 738 thousand, "Forty-three million" and the baseline sentence are gone, from the gain and key points too. 208 thousand per call is confined to "that sample". "Why the page and the documents keep sessions small" becomes "What a fresh session carries" (pt "O que uma sessão nova carrega"): the session reads the queue whole, done lines included, so its starting context grows with history; the one-sentence line slows that growth and does not stop it; what a fresh session removes is the earlier conversation. How a team decides lists the four things to write down (window and time zone; sessions and calls incl. proposals, retries and shared sessions, and the rule that chose them; the deliveries they finished; unmatched work on its own line) and divides only the calls that worked on those deliveries. The `message.id` plus `requestId` rule and the retention warning stay. The gain is one number, 98.3% of the sample's tokens as cache reads, carried by no key point.

**Proof.** Arithmetic recomputed from the retained aggregate: 271,807 + 54,527,957 + 3,940,576,768 + 13,871,893 = 4,009,248,425. Shares: input 0.0068% (shown 0.01%), cache write 1.360% (1.4%), cache read 98.287% (98.3%), output 0.346% (0.3%); the displayed values are unchanged. Cache read per call: 3,940,576,768 / 18,945 = 208,000.9, shown as about 208 thousand. The logs were not recounted; the totals remain the author's recorded count (`work/done/plain-numbers.md`). Queue reading sourced from docs/05 §4 (/propose reads the whole queue) and `.claude/skills/apply/SKILL.md` (reads docs/06). `make verify` green after the last edit; `make book` is run once by the batch driver for `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, for the author's passage review.

**Divergences.** None. No Case A or Case B passage was used or changed; Ninjobs is named by its published numbers only.

**Decisions.** The gain keeps one number, the 98.3% cache-read share confined to the sample, rather than none, because it is the chapter's surviving measured observation. Key point 2 says what the reader does (count cache reads apart) and carries no number. The 93-page count leaves this chapter; chapter 2 keeps its own. Percentages keep their earlier precision.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of both chapter files against this page and docs/04. Points: (1) "with them any way to count the table again" tied the lost recount to the logs before the window: now says the logs of those 21 days have gone since. (2) "the table counts every token the agent read and wrote" overclaimed coverage: now "counts tokens only". (3) The gain's "the part of the bill" let 98.3% read as a cost share: now "the column the way a team works can move". (4) Dividing the tokens of shared sessions double-counted their other work: now divides the calls that worked on those deliveries; pt "sessões compartilhadas". Verify ran again after the fixes.

```commit
docs(ch22-cost-method): keep token totals, drop unmatched averages

- Ninjobs table kept as a 21-day sample with an unrecovered boundary
- 43.1 M, 149 k and 738 k per delivery leave text, gain and key points
- A milestone count writes down window, sessions, deliveries, leftovers
- A fresh session reads the whole queue, so its context grows with it

work/done/ch22-cost-method.md
```
