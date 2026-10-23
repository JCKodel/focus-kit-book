# ch22-cache-service

**Objective.** A reader of chapter 22 can say that a conversation's cache is kept where the model runs, on Anthropic's infrastructure or a cloud provider's, not by the host on their machine, and that the host, the program that runs the agent, sends the context with every call and chooses the cache lifetime for each request.

The queue line (docs/06, M30, a finding of `m30-review`, its C1): "chapter 22 and docs/03's cache lifetime row say that the service keeps the stored context and writes it again after a pause, the host being the program that runs the agent (docs/03, chapter 22's own definition) and choosing the lifetime per request, in the new section and wherever the chapter has the host store the cache; both editions." This page answers it alone. `m31-records-claims` later gave the line, in place of "the service keeps the stored context and writes it again", this page's words, "the stored context is kept where the model runs and written again", `service` being docs/03's FOCUS term (Decided by this proposal); the quote above is the line as this page read it.

**Behaviour.**

* A reader says where the cache is kept: where the model runs, on Anthropic's infrastructure with a Claude subscription or an API key, or on the cloud provider's when the model is reached through one; not on their machine and not in the host.
* A reader says what the host does with the cache: it sends the whole context with every call, as chapter 22 already says, and chooses the lifetime, five minutes or one hour, for each request; Claude Code's two groups and its two settings stay as the chapter gives them.
* A reader says what happens after a pause past the lifetime: the next call finds no cache where the model runs, so the context the host sends is written there again, whole, at the write price instead of the read price; the multipliers and the 12.5 to 80 range stay as they are.
* Edge: a reader does not confuse the host's session logs with the cache. The host keeps its logs on the reader's machine (§How a team decides, :108 and the retention sentence at :121, unchanged); deleting a log or its retention period ending changes nothing in the cache, and the cache lifetime says nothing about how long the logs last. The chapter states no sentence that ties the two.
* Failure the delivery removes: in chapter 22 (both editions) and in docs/03's `cache lifetime` row, no sentence has the host as the one that keeps, stores or writes the cache. Checked by reading every sentence that holds "cache" in both chapter files and the row; `host keeps` remains only for the logs.
* Every other use of "host" in chapter 22 keeps its meaning (en line numbers here and in the edge above; pt one or two lines later from :47 on), the program you run: it bills the call in tokens as the heading says (§What a host bills, :13, :16), runs commands (:21), sends the context (:23, key point 1), chooses the lifetime (:39), keeps logs (:50, :108, :121, :130, key point 4).
* The Portuguese edition says the same, with "onde o modelo roda", "a infraestrutura da Anthropic" and "o provedor de nuvem" for where the cache is kept, and never "serviço" for it (docs/03 fixes `serviço` as the FOCUS piece).
* docs/03's `cache lifetime` row reads the same as the chapter: the cache kept where the model runs, the host choosing the lifetime per request.

**Contract.**

* Files: `book/en/22-cost-and-where.md`, `book/pt/22-cost-and-where.md` and `docs/03-Domain.md` (the `cache lifetime` row only). No heading changes, so parity holds as it is.
* Passages that change, line numbers as of today, the same in both editions:
  * §What a host bills / §O que um host cobra, :19, the **Cache write** / **Escrita no cache** bullet: "text the host stores so that later calls can reuse it" becomes text kept where the model runs, at the host's request, so later calls can reuse it. No note: the claim is made and sourced at :29, a few lines on.
  * §How long the cache lasts / §Quanto tempo o cache dura, :29, its first sentence: "The host keeps a stored context only for a while ... chosen when the context is written" becomes: the stored context is kept where the model runs, on Anthropic's infrastructure with a subscription or an API key or on the cloud provider's, only for a while, the cache lifetime, five minutes or one hour, which the host chooses for each request. Notes at the claims: `[^claude-code-prompt-caching]` for where the cache lives and the host's choice, `[^anthropic-pricing]` for the two durations, as today.
  * Same section, :34: "The next call finds no cache, so the host writes the whole context again" becomes: the next call finds no cache, so the whole context the host sends is written again, at the write price instead of the read price. Its note stays `[^claude-code-prompt-caching]`.
  * Same section, :39 ("Claude Code chooses the lifetime per request, in two groups"): unchanged; it already has the host choose. /apply may shorten :29's clause on the choice so the two sentences do not repeat each other, keeping :29's general claim and :39's Claude Code detail.
  * `[^claude-code-prompt-caching]`, both editions: the section becomes "Where the cache lives" and "Cache lifetime" (pt: seções "Where the cache lives" e "Cache lifetime", the titles in their original language as docs/04 asks), and its access date the date /apply checks the claim (docs/04, Source notes). URL and key unchanged.
  * docs/03 :52, the `cache lifetime` row's Meaning: "How long the host keeps a stored context ..." becomes how long a stored context is kept where the model runs (Anthropic's infrastructure, or the cloud provider's that serves the model) after a call last wrote or read it, counted from the start of that call: five minutes or one hour, chosen by the host for each request and renewed by every read; a call after it ends has the whole context written again at the write price; Claude Code's choice per request and its setting, chapter 22. Term, Portuguese and Identifier columns unchanged.
  * No other passage changes. Key point 5 (:140), the gain sentence (:132), the opening (:5) and the column reading (:125) do not name who keeps the cache.
* Facts, checked on 2026-10-23 at the sources the chapter already cites:
  * "How Claude Code uses prompt caching", §Where the cache lives: "Caching happens server-side, in whichever infrastructure serves your model"; with an API key, a Claude subscription or Claude Platform on AWS "the cache lives in Anthropic's infrastructure"; with Amazon Bedrock or Google Cloud's Agent Platform "the cache lives in your cloud provider's serving infrastructure"; "Wherever the cache lives, entries expire after a period of inactivity".
  * Same page, §Cache lifetime and §Choose the TTL yourself: Claude Code sets the TTL of each request by bucket; `promptCacheTtl`, `subagentPromptCacheTtl`, `5m` or `1h`, v2.1.242 (unchanged in the chapter).
  * Pricing page, "Prompt caching": the five-minute and one-hour writes and the reads, unchanged; "Prompt caching" page: the lifetime counted from the start of the request, unchanged.
  * No new number.
* Terms of docs/03: `host` (the program that runs the coding agent, :19) used only in that sense in chapter 22's cache passages; `cache lifetime` / `tempo de vida do cache` row edited as above. No new term (see Decided by this proposal). `service` / `serviço` (:63) is not used for where the cache is kept.
* Cases: none. No private case, so no author approval (docs/00 OD-3).
* Code examples: none.

**States** and **Visual reference.** Inapplicable: no screen, and no new kind of content.

**Out of scope.**

* The heading "What a host bills" and :16's "the host ... bills every call": the line names where the cache is kept and who writes it, not who invoices; the heading is the chapter's frame for the four kinds the host counts in its logs.
* Microsoft Foundry and a custom base URL or LLM gateway, the source's other two cases: the chapter names a subscription, an API key and a cloud provider, and the source is one note away.
* The review's other chapter 22 candidates, C2 to C6 (among them C4, the `cache lifetime` row's Identifier column listing `promptCacheTtl` alone, left as it is although this delivery edits the row's Meaning) and the record candidates C18 to C22: `m30-review` lists them as not confirmed by the author, none fixed.
* `m30-records-claims` and its files: another delivery, running in the same tree.
* Chapters 23 and 24: neither has the host store the cache (grep of both editions for "cache" finds none).

**Done when.**

* [x] Both editions written, same headings, same note keys each cited as many times (parity).
* [x] The chapter still opens with its value; no filler and nothing useful cut.
* [x] In both chapter files and docs/03's `cache lifetime` row, no sentence has the host keep, store or write the cache; every other "host" in chapter 22 is the program you run.
* [x] Every changed claim carries its note, and `[^claude-code-prompt-caching]` names both sections and the date /apply checked them.
* [x] The `status: draft` line is not added.
* [x] Delivery review by one read-only agent on Opus over `git diff HEAD` of the two chapter files and docs/03 and this line's hunk of docs/06, with both chapter files whole and the live source, against this page and docs/04 (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.
* [x] `make verify` green after the last edit.
* [x] `make book` builds, and the delivery ends giving the author both PDF paths (docs/05 §5).

## Decided by this proposal

The agent chose each of these, for the person's review.

* The word for who keeps the cache. The line said "the service"; docs/03 fixes `service` / `serviço` as the FOCUS piece (:63) and its header fixes the Portuguese term, the Portuguese edition using it and no synonym (:4), so the chapter does not use it here. The agent chose to name the place as the source does, where the model runs, Anthropic's infrastructure or the cloud provider's, both already named in chapter 22, instead of adding a new docs/03 term (such as "model server"): the reader needs the fact once, in one section, and docs/04 asks no filler. Had a new term been chosen, docs/03 would gain its row first.
* The passages: :19, :29 and :34 of both editions and docs/03 :52, found by reading every "host" and "cache" sentence of chapter 22; the line names :19 through m30-review's decision ("the older one at :19 included").
* The note: `[^claude-code-prompt-caching]` reused, its sections widened, as docs/04 asks a cited source to keep its key.
* The edge on logs and cache, from :108 and :121, which keep "the host keeps a log" in its own sense.

## What happened

**Built.** Chapter 22, both editions: the **Cache write** bullet (:19) has the text kept where the model runs, at the host's request; §How long the cache lasts opens with two lines (:29, :30), where the cache is kept (Anthropic's infrastructure with a subscription or an API key, the cloud provider's through one, not your machine, `[^claude-code-prompt-caching]`) and how long, five minutes or one hour (`[^anthropic-pricing]`), chosen by the host for each request (`[^claude-code-prompt-caching]`); :35 has the whole context the host sends written again. `[^claude-code-prompt-caching]` names "Where the cache lives" and "Cache lifetime", accessed 2026-10-23. docs/03's `cache lifetime` row reads as the Contract gives it.

**Proof.** The source checked on 2026-10-23: §Where the cache lives, "Caching happens server-side, in whichever infrastructure serves your model", Anthropic's infrastructure for an API key, a subscription or Claude Platform on AWS, "your cloud provider's serving infrastructure" for Bedrock and Google Cloud's Agent Platform; §Which TTL each request gets, "Claude Code decides the TTL per request". A grep of both chapter files for the host keeping, storing or writing (`host (keeps|stores|writes|guarda|armazena|escreve)`) finds only the logs, en :109 and pt :110; "serviço" appears nowhere in the Portuguese chapter. `make verify` green after the last edit; `make book` builds both editions, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, before this delivery's commit `bc6fa75`, whose parent `9c65001` (`m30-records-claims`) was committed 72 seconds earlier, the two lanes sharing one tree; the build's HEAD and `git status --short book/` are not recorded.

**Divergences.** :29 of the Contract became two lines, :29 and :30, one claim and its note each, so the chapter's lines from :30 on are one later than the page's numbers. The host's choice carries `[^claude-code-prompt-caching]` beside the durations' `[^anthropic-pricing]`, so that note is cited 6 times per edition, the pricing note 4. The Done when's review item ticked the review "as docs/05 §5 says", and the review paragraph said the agent "keeps the session's advisor", the slot's words, not its report's, which this page does not record (Delivery review); the page has no define commit, its first commit being `bc6fa75`; `m31-records-claims` gave the item and the paragraph what is recorded.

**Decisions.** :30's general clause ("which the host chooses for each request") is kept beside :40's Claude Code detail: the Behaviour asks for the general claim, and :40 gives the two groups; the review noted the closeness and named no rule it breaks. The Portuguese edition says "na infraestrutura do provedor de nuvem quando você chega ao modelo por meio dele", the noun repeated so "na do provedor" does not lean on the clause before it.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of the two chapter files and docs/03, this line's hunk of docs/06, both chapter files whole, the page and docs/04, and checked the live source: no candidates. Whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.

```commit
docs(ch22-cache-service): keep the cache where the model runs

- Chapter 22: the cache is kept where the model runs, not on your machine
- The host sends the context and chooses the lifetime per request
- A pause past it has the whole context written again at the write price
- docs/03's cache lifetime row reads the same; note accessed 2026-10-23

work/done/ch22-cache-service.md
```
