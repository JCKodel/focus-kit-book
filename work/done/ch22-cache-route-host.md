# ch22-cache-route-host

**Objective.** A reader of chapter 22 can say where a conversation's cache is kept by the infrastructure that serves the model, Anthropic's with a Claude subscription, an API key or Claude Platform on AWS, a cloud provider's own when that provider serves the model, and that Claude Code, the host the chapter's source names, chooses the cache lifetime for each request.

The queue line (docs/06, M31, a finding of `m31-review`, its C1 and C2): "chapter 22 says where the cache lives by the infrastructure that serves the model, as docs/03's cache lifetime row and its source say, Claude Platform on AWS included, and says that the lifetime is chosen per request of the host its source names, Claude Code, in the chapter and the row; both editions." This page answers it alone.

**Behaviour.**

* A reader says where the cache is kept: where the model runs, in whichever infrastructure serves it; on Anthropic's with a Claude subscription, an API key or Claude Platform on AWS; on the cloud provider's own when the provider serves the model, as Amazon Bedrock and Google Cloud's Agent Platform do; never on their machine.
* Failure the delivery removes (C1): no sentence of chapter 22 in either edition says the cache is on the cloud provider's infrastructure whenever the model is reached through one. A reader on Claude Platform on AWS, which is reached through AWS, does not conclude the cache is AWS's.
* A reader says who chooses the lifetime: Claude Code chooses it for each request, in two groups, as §How long the cache lasts already says at :40; the chapter states no rule for other hosts.
* Failure the delivery removes (C2): no sentence of either chapter file and none of docs/03's `cache lifetime` row has "the host", any host, choose the lifetime.
* Edge, the lifetime on Claude Platform on AWS: :41's "five minutes with an API key, through a cloud provider" stays. It is the source's table column ("Usage credits, API key, or cloud provider"), and Claude Code's page on Claude Platform on AWS gives that route the five-minute default too, so no reading of "cloud provider" there makes :41 wrong.
* Edge, what stays the host's: the host sends the context (:23, :29's first clause), asks for the write (:19, "at the host's request"), and keeps logs (:109, :122); none of these is about where the cache lives or who chooses its lifetime, and none changes.
* The Portuguese edition says the same, product names in English ("Claude Platform on AWS", "Amazon Bedrock", "Agent Platform do Google Cloud"), "o Claude Code" as the chooser, and never "serviço" for where the cache is kept (docs/03 :63 fixes it as the FOCUS piece).
* docs/03's `cache lifetime` row reads the same as the chapter: the lifetime chosen for each request, by Claude Code in chapter 22's source, not by "the host".

**Contract.**

* Files: `book/en/22-cost-and-where.md`, `book/pt/22-cost-and-where.md`, and `docs/03-Domain.md` (the `cache lifetime` row's Meaning only). No heading changes.
* Passages, line numbers as of today, the same in both editions:
  * §How long the cache lasts / §Quanto tempo o cache dura, :29: "on Anthropic's infrastructure with a Claude subscription or an API key, or on the cloud provider's when you reach the model through one" (pt "na infraestrutura da Anthropic com uma assinatura do Claude ou uma chave de API, ou na infraestrutura do provedor de nuvem quando você chega ao modelo por meio dele") becomes: kept in whichever infrastructure serves the model, Anthropic's with a Claude subscription, an API key or Claude Platform on AWS, and the cloud provider's own when the provider serves the model, as Amazon Bedrock and Google Cloud's Agent Platform do. The first clause ("The host sends the context, but ... not on your machine") stays. Note: `[^claude-code-prompt-caching]`, as today, one.
  * Same section, :30: "which the host chooses for each request.[^claude-code-prompt-caching]" (pt "que o host escolhe para cada requisição.[^claude-code-prompt-caching]") is removed; the sentence ends at "five minutes or one hour" with its `[^anthropic-pricing]`. :40 ("Claude Code chooses the lifetime per request, in two groups.[^claude-code-prompt-caching]", pt "O Claude Code escolhe o tempo de vida por requisição, em dois grupos.") stays as the one claim of who chooses.
  * `[^claude-code-prompt-caching]`: cited 5 times per edition instead of 6, the same in both; its sections ("Where the cache lives" and "Cache lifetime"), URL and access date, 2026-10-23, stay: the facts were checked on that date (below). `[^anthropic-pricing]` and `[^anthropic-prompt-caching]` unchanged.
  * docs/03 :52, the `cache lifetime` row's Meaning: "five minutes or one hour, chosen by the host for each request and renewed by every read" becomes: five minutes or one hour, chosen for each request, by Claude Code in chapter 22's source, and renewed by every read. The rest of the Meaning ("kept where the model runs (Anthropic's infrastructure, or the cloud provider's that serves the model)", the count from the start of the call, the rewrite at the write price, the pointer to chapter 22) and the Term, Portuguese and Identifier columns stay: m31-review's C1 finds the row's "where" already right.
  * No other passage changes: :19, :23, :35, :41, the gain sentence (:133) and key point 5 (:141, which already names Claude Code).
* Facts, checked on 2026-10-23:
  * "How Claude Code uses prompt caching" (`https://code.claude.com/docs/en/prompt-caching`), §Where the cache lives: "Caching happens server-side, in whichever infrastructure serves your model. Where that is depends on how you authenticate"; "API key, Claude subscription, or Claude Platform on AWS: the cache lives in Anthropic's infrastructure"; "Amazon Bedrock or Google Cloud's Agent Platform: the cache lives in your cloud provider's serving infrastructure". §Cache lifetime, §Which TTL each request gets: "Claude Code decides the TTL per request, and every request falls in one of two fixed buckets"; the table's second column, "Usage credits, API key, or cloud provider".
  * "Claude Code on Claude Platform on AWS" (`https://code.claude.com/docs/en/claude-platform-on-aws`): "the Anthropic-operated Claude API with AWS authentication"; prompt caching on by default with the five-minute TTL. Checked, not cited: the chapter's note already holds the claim.
  * "Claude Platform on AWS", Claude Platform documentation: "Claude models run on Anthropic-managed infrastructure". Checked, not cited.
  * "Prompt caching", Claude Platform documentation, §Automatic caching: a request's `cache_control` takes `"ttl": "1h"`, five minutes by default; the basis for the row's "chosen for each request" without naming who.
  * No new number.
* Terms of docs/03: `host` (:19), `cache lifetime` / `tempo de vida do cache` (:52, edited as above), `service` / `serviço` (:63, not used). No new term.
* Sources: the three existing notes; no new key.
* Cases: none. No private case, so no author approval (docs/00 OD-3).
* Code examples: none.

**States** and **Visual reference.** Inapplicable: no screen, and no new kind of content.

**Out of scope.**

* A general claim that whatever program sends the request sets the lifetime: the Prompt caching page would support it, but the line names Claude Code, and the chapter teaches the host the reader runs.
* Microsoft Foundry (its cache depends on the deployment's hosting option) and a custom base URL or LLM gateway: the source's other two cases, one note away, left out as `ch22-cache-service` left them.
* :19's "at the host's request": it says who asks for the write, not where the cache lives or who chooses its lifetime.
* The row's "where" clause: m31-review's C1 says it holds.
* The records of `ch22-cache-service` and the queue line naming "the service": `m31-records-claims`, running in the same tree; its line and page are its own.
* Chapters 23 and 24: neither names where the cache lives or who chooses its lifetime (`ch22-cache-service` found no "cache" in them).

**Done when.**

* [x] Both editions written, same headings, same note keys each cited as many times (parity), `[^claude-code-prompt-caching]` 5 times in each.
* [x] The chapter still opens with its value; no filler and nothing useful cut.
* [x] In both chapter files, :29 names Claude Platform on AWS with Anthropic's infrastructure and Amazon Bedrock and Google Cloud's Agent Platform with the cloud provider's; "when you reach the model through one" / "por meio dele" appears nowhere.
* [x] A grep of both chapter files and docs/03 :52 for the host choosing (`host (chooses|escolhe)`, `chosen by the host`, `escolhido pelo host`) finds nothing; :40 is the one sentence on who chooses, naming Claude Code.
* [x] Every changed claim carries its note; every number sourced (no new number).
* [x] The `status: draft` line is not added.
* [x] No em dash.
* [x] Delivery review as docs/05 §5 says, the page recording what its agent read and what its report says of the advisor.
* [x] `make verify` green after the last edit.
* [x] `make book` run after the last edit with `git status --short book/` showing only this delivery's two files, its HEAD recorded, and the delivery ends giving the author both PDF paths, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` (docs/05 §5).

## Decided by this proposal

The agent chose each of these, for the person's review.

* The chapter names the source's examples, Claude Platform on AWS with Anthropic's infrastructure and Amazon Bedrock and Google Cloud's Agent Platform with the provider's own: "by the infrastructure that serves the model" tells a reader nothing without them, and the line asks for Claude Platform on AWS by name.
* :30 drops its clause on who chooses, leaving :40's "Claude Code chooses the lifetime per request" the one claim, over the other shape (:30 names Claude Code and :40 keeps only the groups): :40 already says it with the same note, and `ch22-cache-service`'s record noted the two sentences repeat (docs/04, no filler).
* The row says "chosen for each request, by Claude Code in chapter 22's source": the row defines a term, so the general fact (each request carries its lifetime, the Prompt caching page) stays general and the chooser is named as the line asks.
* No new note for Claude Platform on AWS: `[^claude-code-prompt-caching]` already states it (docs/04, a source cited again reuses its key); the two Platform on AWS pages are recorded here as checked.
* `[^claude-code-prompt-caching]`'s access date stays 2026-10-23, the date its two sections were checked again for this page.

## What happened

Built by /apply as one lane of `/apply ch22-cache-route-host,m31-records-claims`, on trunk, beside `m31-records-claims` in the same tree; that lane's files and its line of docs/06 are its own and are not in this delivery.

* :29, both editions: the cache is kept where the model runs, not on your machine, in whichever infrastructure serves the model: Anthropic's with a Claude subscription, an API key or Claude Platform on AWS; the cloud provider's own with Amazon Bedrock or Google Cloud's Agent Platform. One sentence, one `[^claude-code-prompt-caching]`.
* :30, both editions: the clause on who chooses the lifetime is gone; the sentence ends at "five minutes or one hour" with its `[^anthropic-pricing]`. :40 stays the one sentence on who chooses, naming Claude Code.
* docs/03 :52, the `cache lifetime` row: "chosen for each request, by Claude Code in chapter 22's source, and renewed by every read", as the Contract wrote it.
* `[^claude-code-prompt-caching]` is cited 5 times in each edition (7 at HEAD counting the definition, now 6); `[^anthropic-pricing]` and `[^anthropic-prompt-caching]` unchanged. No heading, number or note key changed.
* The source's §Where the cache lives was read again on 2026-10-23 for the review's candidates below; it holds the three cases as the Contract quotes them, Claude Platform on AWS "accessed through the Claude API".

**Divergence.** :29 also says, in a few words, what the three products are (docs/04, Teach, do not only show; the review's candidate 2): Claude Platform on AWS "is Anthropic's Claude API reached with an AWS account" (pt "a API do Claude da própria Anthropic acessada com uma conta da AWS"), from the source's "accessed through the Claude API" and the Claude Code page on Claude Platform on AWS ("the Anthropic-operated Claude API with AWS authentication"), checked and not cited, as the page decided; Bedrock and Agent Platform are "the platforms through which Amazon and Google serve the model themselves" (pt "as plataformas pelas quais a Amazon e o Google servem o modelo eles mesmos"), the Behaviour's "when the provider serves the model". The Portuguese says "plataformas", never "serviço".

**Delivery review.** One read-only agent on Opus (docs/05 §5), given the page and `git diff HEAD` of the two chapter files, docs/03 and this delivery's line of docs/06. It read, as it listed: this page; the diff; docs/04, opened as a file and read in full; book/en and book/pt 22-cost-and-where.md, lines 15 to 45 and greps of the whole files for the note keys and the Done when patterns; docs/03's `host` (:19), `cache lifetime` (:52) and `service` (:63) rows and greps for "cloud provider" and em dashes; HEAD's book/en/22-cost-and-where.md through `git show`, to count its notes; and a grep of book/ for Bedrock, Agent Platform and Platform on AWS. On the advisor its report says: "yes. It raised the same three candidates and asked me to check docs/03 line 52 for an em dash, which found none." It found nothing breaking the page and three candidates:

1. :29, both editions: one comma list inside another ("Anthropic's with a Claude subscription, an API key or Claude Platform on AWS, and the cloud provider's own"), so "an API key" read as a third place, and "and" joined two alternatives. Fixed: a colon opens the list of places and a semicolon divides them.
2. :29, both editions: Claude Platform on AWS, Amazon Bedrock and Agent Platform appear nowhere else in the book, and Claude Platform on AWS was not introduced (docs/04, Teach, do not only show). Fixed as the Divergence says.
3. docs/03 :52: the new "by Claude Code in chapter 22's source" repeats the row's ending ("Claude Code's choice per request and its setting, chapter 22"). Kept: the Contract fixes that wording, which the queue line asks for ("in the chapter and the row"); the reviewer called it a clarity point only. No `[ ]` line.

`make verify` green after the fixes and after the last edit. `make book` run after the last edit at HEAD `99d04a5`, green (two weasyprint warnings, `user-select: none`, as before); `git status --short book/` showed only ` M book/en/22-cost-and-where.md` and ` M book/pt/22-cost-and-where.md`. The PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

No new `[ ]` line. No dependent line to resolve: no line of docs/06 names `ch22-cache-route-host` in its `after`.

```commit
docs(ch22-cache-route-host): place the cache by who serves the model

- ch22 :29: Anthropic's with a subscription, an API key or Platform on AWS
- ch22 :29: the provider's own with Amazon Bedrock or Agent Platform
- ch22 :30: drop "the host chooses"; :40 names Claude Code, the chooser
- docs/03 cache lifetime: chosen per request, by Claude Code in the source

work/done/ch22-cache-route-host.md
```
