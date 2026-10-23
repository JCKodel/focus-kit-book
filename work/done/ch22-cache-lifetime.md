# ch22-cache-lifetime

**Objective.** A reader of chapter 22 knows that the host keeps a conversation's cache only while the conversation keeps using it, that a pause past the cache's lifetime makes the next call write the whole context again at the write price instead of reading it at the read price, what lifetime Claude Code gives each kind of request, and how to change it.

M30's paragraph (docs/06): "a reader of chapter 22 knows that the cache lasts only while the conversation keeps using it, and that a pause past its lifetime makes the next turn rebuild the whole context at the write price instead of reading it at the read price." This page answers it alone.

**Behaviour.**

* A reader explains that every call that reads the cache renews its lifetime, so the cache stays while the conversation keeps working, and that the lifetime is counted from the start of the call that wrote or read it, not from the end of its answer: an answer that takes 4 minutes to stream leaves about 1 minute of a five-minute cache for the next call.
* A reader explains what a pause costs: once the lifetime has passed, the next call finds no cache and writes the whole context again, at 1.25 times the price of an input token for a five-minute cache or 2 times for a one-hour cache, where a read would have cost 0.1 times, or 0.05 or 0.025 times on the models the pricing page names.
* A reader works out from those multipliers that the context part of the first call after a long pause costs 12.5 to 80 times what the same context cost on the call before it (1.25 / 0.1 at the least, 2 / 0.025 at the most), and the chapter says "tens of times" nowhere a ratio it gives is below 20.
* A reader on Claude Code says which lifetime a request gets: the main conversation one hour on a Claude subscription within the plan's usage, five minutes with an API key, a cloud provider or the plan's usage credits; subagents and the other requests outside the main conversation five minutes.
* A reader changes it: `promptCacheTtl` for the main conversation and `subagentPromptCacheTtl` for the rest, each taking `5m` or `1h`, from Claude Code v2.1.242; and says when the hour pays (a session left idle and resumed) and when it costs more (short bursts that never pause past five minutes, where the higher write price buys nothing).
* A reader who counts a milestone, as the chapter already teaches, reads a rise in the cache write column as the cache being rebuilt, by pauses past its lifetime or by new sessions, beside the existing reading of output and cache reads.
* A reader on a subscription finds no claim of how a cache write counts against the plan's usage: no source says, and the chapter states prices only as multipliers of the per-token price.
* The Portuguese edition says the same with the same numbers in its own format (1,25; 12,5; 0,025), the term `tempo de vida do cache` and no synonym.

**Contract.**

* Files: `book/en/22-cost-and-where.md` and `book/pt/22-cost-and-where.md` only, and docs/03 (done by this proposal, below). Same headings in both editions (parity).
* Sections that change, en line numbers as of today:
  * Opening (lines 3 to 4): a third sentence, the chapter's opening keeping at most three (docs/03, Entities): the reader can say why the first turn after a long pause can cost many times the one before it, and set how long the cache lasts.
  * §What a host bills, line 24: the multipliers sentence gives the one-hour write as well, 2 times, beside the five-minute 1.25 and the read of a tenth or less.
  * New H2 after §What a host bills and before §What Ninjobs recorded in tokens, title "How long the cache lasts" (pt "Quanto tempo o cache dura"): renewal by every read, the lifetime counted from the start of the call with the 4-minute example, what the call after a pause pays and the 12.5 to 80 ratio with its arithmetic, Claude Code's two buckets and their defaults, the two settings, their values and version, and when the hour pays. The agent chose this place and title: the section explains a column the section before defines, and the Ninjobs table after it reads better with it known.
  * §How a team decides, line 104: the sentence "output up means more was built, cache reads up means sessions grew" gains the cache write column: up means the cache was rebuilt, by pauses past its lifetime or by new sessions.
  * §What the team gains (lines 109 to 110): one sentence, the team knows what a pause costs and sets the lifetime to how it works, with the multipliers as its evidence.
  * §Key points: a fifth bullet (at most five, docs/04): every read renews the cache; a pause past its lifetime, five minutes or an hour, makes the next call write the whole context at 1.25 or 2 times the input price instead of reading it at 0.1 or less; Claude Code's defaults and `promptCacheTtl`.
  * No other section changes. The Ninjobs table and its 1.4% of cache writes get no reading of pauses: nothing recorded says why those writes happened (docs/04, Evidence).
* Numbers and claims, all checked on 2026-10-23 at the sources below:
  * pricing page, §Feature-specific pricing, "Prompt caching": 5-minute write 1.25x base input, valid 5 minutes; 1-hour write 2x, valid 1 hour; cache read 0.1x, 0.025x on Claude Fable 5.1 and Claude Mythos 5.1, 0.05x on Claude Opus 5.5 and Claude Sonnet 5.5, "Same duration as the preceding write"; "Cache hits and refreshes: Reading a prompt prefix from the prompt cache, which also refreshes it."
  * Prompt caching page, §How prompt caching works: "The lifetime is measured from the start of the request that writes or reads the cache entry, not from the end of its response", with the 4-minute response leaving "about 1 minute".
  * "How Claude Code uses prompt caching", §Cache lifetime: "Each request that hits the cache resets the timer"; after a long enough gap "the next request recomputes the full input"; the table of the two buckets (main conversation one hour on a subscription within plan usage, five minutes on usage credits, an API key or a cloud provider; everything else five minutes, except server-controlled helper requests that get one hour on a subscription); usage credits drop the main conversation to five minutes; §Choose the TTL yourself: `promptCacheTtl` and `subagentPromptCacheTtl`, `5m` or `1h`, any other value ignored, v2.1.242 or later; the hour helps a session left idle and costs more on short bursts.
  * The ratios 12.5, 20, 25, 40, 50 and 80 are arithmetic on those multipliers, shown in the text.
* Sources (docs/04, Source notes), keys the same in both editions:
  * `[^anthropic-pricing]`, existing: its access date becomes 2026-10-22 (pt `acesso em 2026-10-22`), the date the queue line gives, since the figures it backs were checked again; section stays "Prompt caching"; URL becomes the address the old one now redirects to, `<https://platform.claude.com/docs/en/about-claude/pricing>`.
  * `[^claude-code-prompt-caching]`, new: Anthropic, "How Claude Code uses prompt caching", Claude Code documentation, section "Cache lifetime", accessed 2026-10-22. `<https://code.claude.com/docs/en/prompt-caching>`.
  * `[^anthropic-prompt-caching]`, new: Anthropic, "Prompt caching", Claude Platform documentation, section "How prompt caching works", accessed 2026-10-22. `<https://platform.claude.com/docs/en/build-with-claude/prompt-caching>`. The queue line names two sources, but the start-of-request rule is stated on neither: docs/04 asks a note at every sourced claim, so the third note is decided by docs/04, not by choice.
* Terms of docs/03: `cache lifetime` / `tempo de vida do cache`, added by this proposal. `token`, `context window`, `subagent`, `compaction` already there; "cache write" and "cache read" are the chapter's own, as today (pt "escrita no cache", "leitura do cache").
* Cases: none. Ninjobs only through the existing table, unchanged. No private case, so no author approval (docs/00 OD-3).
* Code examples: none; the settings appear as names and values in inline code, no settings file is shown.

**States** and **Visual reference.** Inapplicable: no screen, and the chapter brings no kind of content the build has not shown before.

**Out of scope.**

* Compaction, resume and `/rewind` after a pause: the Claude Code page covers them, the queue line does not, and chapter 22 teaches the bill, not the commands.
* The cache's scope (one machine and directory, parallel sessions sharing it): not about lifetime.
* Prices in dollars or any model's per-token price: they change by model and date, and chapter 22 compares milestones, not vendors.
* How a subscription's usage limit counts cache writes: no source states it.
* Hosts other than Claude Code: the queue line and the sources are Claude Code's and Anthropic's.
* The environment variables and the order of precedence (`FORCE_PROMPT_CACHING_5M`, `ENABLE_PROMPT_CACHING_1H`, a subagent's `cacheTtl`): the two settings are what a team sets; the rest is the source's, one note away.
* Chapter 25's subscriber passages: untouched.

**Done when.**

* [x] Both editions written, same headings, same note keys each cited as many times (parity).
* [x] The chapter still opens with its value, in at most three sentences; no filler and nothing useful cut.
* [x] Every number and quoted claim of the new and changed passages carries its note, as listed in Contract.
* [x] The `status: draft` line is not added: the chapter is done before and after.
* [x] No em dash; prose rules, width and link checks green (the three URLs answer 200 today).
* [x] `make verify` green.
* [x] `make book` builds, and the delivery ends giving the author both PDF paths (docs/05 §5).

## Decided by this proposal

* Scope, section list, new section's place and title, the third note and the access date: the agent chose them from docs/04, docs/05 §3 and the sources, named above, for the person's review.
* Ratio stated as a range with arithmetic (12.5 to 80) instead of the queue line's "tens of times", which holds only from 20 up: the agent chose it from docs/04 (every number says where it comes from).

## Sources checked against the queue line (2026-10-23)

* Confirmed: renewal by every read; lifetime counted from the start of the request; 1.25 and 2 times for writes; reads at 0.1 times or less; Claude Code's one hour for the main conversation on a subscription within plan usage, five minutes on an API key, a cloud provider or usage credits; subagents five minutes; `promptCacheTtl`.
* Differs or adds:
  * "Counted from the start of the request" is stated on the Prompt caching page, not on either source the line names; a third note.
  * "Tens of times": the smallest ratio is 12.5 (five-minute write against a 0.1x read); 20 and above only with the one-hour write or the cheaper reads.
  * Reads cheaper than 0.1x: 0.05x on Claude Opus 5.5 and Claude Sonnet 5.5, 0.025x on Claude Fable 5.1 and Claude Mythos 5.1.
  * The setting needs Claude Code v2.1.242 or later; `subagentPromptCacheTtl` sets the other bucket; on a subscription a few server-controlled helper requests outside the main conversation get one hour.
  * The pricing URL the chapter cites, `docs.anthropic.com/...`, now redirects to `platform.claude.com/...`.

## What /apply did

**Built.** Chapter 22 in both editions: a third opening sentence; §What a host bills gives the one-hour write, 2 times; the new `## How long the cache lasts` / `## Quanto tempo o cache dura` between §What a host bills and §What Ninjobs recorded in tokens, with renewal by every read, the lifetime counted from the start of the call and the 4-minute example, the price of a pause with the multipliers and the range 12.5 (1.25 / 0.1) to 80 (2 / 0.025), Claude Code's two groups and their defaults, `promptCacheTtl` and `subagentPromptCacheTtl` with `5m` or `1h` from v2.1.242, and when the hour pays; §How a team decides reads the cache write column; one gain sentence; a fifth key point; `[^anthropic-pricing]` at 2026-10-22 and its new URL, `[^claude-code-prompt-caching]` and `[^anthropic-prompt-caching]` added. docs/03's `cache lifetime` row, written by /propose, stays as written.

**Divergences.**

* The gain sentence and the fifth key point carry no multiplier: docs/04 **Numbers that prove** and **One gain** give the gain section one number (the 98.3% already there) and let a key point carry at most that number, so the multipliers stay in the new section, and the gain sentence's evidence is the pricing note. The delivery review judged this right.
* The arithmetic shows the two ends of the range, 1.25 / 0.1 and 2 / 0.025, not each of the six ratios the Contract lists: the ends prove the range, and docs/04 **Numbers that prove** keeps further arithmetic at the source.
* The Portuguese edition adds one sentence after the settings, saying their names and values are Claude Code's and stay in English, as docs/04 asks where such a name appears and as the chapter already does for the log fields.
* "Subagents and most other requests" stands for the Contract's "the other requests outside the main conversation", since the source gives a few server-controlled helper requests one hour on a subscription.

**Decisions taken by /apply.** The agent chose these alone: the wording of every new sentence; the order of the new section (lifetime and renewal, the price of a pause, Claude Code's groups, the settings); fixing the six review candidates below now, since each is in text this delivery wrote.

**Proof.** `make verify` green (exit 0) after the last edit; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` and both EPUBs. The three source pages were fetched again on 2026-10-23 and every claim of the new passages matches them; the link check reached all three URLs.

**Delivery review.** One read-only Opus agent, launched by this /apply, that wrote none of it, read `git diff HEAD` of the two chapters and docs/03, this line's hunk of docs/06 and this page, against the page, docs/04 and AGENTS.md, and fetched the three sources; it did not say it consulted an advisor. No candidate broke the page or docs/04. Six candidates, all fixed: key point 5 named the durations twice and dropped "within the plan's usage" (first mention cut, "within its usage" added, both editions); the gain sentence said "the host's own price multipliers", where the multipliers are Anthropic's (now "Anthropic's", both editions); the pt-only sentence on English names (kept, recorded above); and three pt wordings (the commas of §What a host bills' multipliers sentence, "se mantém" for "fica", "acrescenta" for "soma"). The review also noted that the chapter already uses "host" for both the program and the service that keeps the cache, older than this delivery; left as it is.

```commit
docs(ch22-cache-lifetime): teach how long the cache lasts

- chapter 22: new section on the cache lifetime, its renewal by every
  read, a pause's price (12.5 to 80 times the context) and Claude
  Code's defaults and settings; both editions
- the multipliers sentence gives the one-hour write; the cache write
  column reads as rebuilt cache; a gain sentence and a key point
- pricing note re-dated and moved to its new URL; two notes added
- docs/03: the term cache lifetime / tempo de vida do cache

work/done/ch22-cache-lifetime.md
```
