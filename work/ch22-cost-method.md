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

* [ ] Both editions pass every Behaviour check; all three per-delivery token averages and associated baseline claims are gone from this chapter, including its gain and key points.
* [ ] Table totals, percentages and retained per-call arithmetic are recomputed and recorded; absent log verification is stated honestly.
* [ ] The opening states reader value, gain matches the evidence, and no filler or useful measurement instruction is cut; every retained number keeps its provenance.
* [ ] `make verify`, including disclosure, and `make book` pass; both PDFs are given to the author for passage review (docs/05 §5).
