# how-agents-see

**Objective.** After chapter 2 the reader can explain why a coding agent knows only what is in its context window at each call, why a long session gets worse, and what to keep in writing so a fresh session starts right. The chapter also fixes how the book draws diagrams, on its first real one.

**Behaviour.**

* The reader can say what the model remembers between two calls (nothing), and who sends the conversation again each time (the host).
* The reader can list what one call's context window holds: the host's instructions, the rules file, the files read, the tool output, the conversation so far, and says it is measured in tokens and has a limit.
* The reader can say what context rot is and cite two measurements: accuracy drops when the relevant information sits in the middle of a long input, and 18 models grew less reliable as the input grew, even on simple tasks.
* The reader can say what compaction is and what it costs: a summary replaces the conversation, and a detail that mattered can be lost.
* The reader can say why a decision belongs in a file the agent reads when a session starts, and why each delivery gets a fresh session, with deciding and building kept apart.
* An author drawing a later diagram finds the rule in docs/04 §Files and needs to ask nothing.

**Contract.**

Chapter 2, `book/en/02-how-agents-see.md` and `book/pt/02-how-agents-see.md`:

* Title: "How an agent sees your project" / "Como um agente enxerga o seu projeto".
* Sections, in order (headings may be reworded in the writing; both editions keep the same structure):
  1. Opening: the Objective's first sentence, in at most three sentences.
  2. The model remembers nothing between calls: the Messages API is stateless and the host sends the whole conversation every time; a new session starts empty.
  3. The context window: what one call holds, the diagram below, tokens, the limit. No window sizes of any model.
  4. More context, less accuracy: context rot, from Liu et al., Chroma and Anthropic.
  5. When the window fills: compaction, and what it loses.
  6. What this changes in your project: decisions in files read at the start of every session, with the excerpt of this repository's AGENTS.md below; one fresh session per delivery, deciding apart from building. It points to chapters 6, 10 and 11 without teaching them.
  7. Key points. No exercises (Part I).
* Voice: "you" throughout; no case story.
* docs/03 terms introduced: `context window`, `token` (new), `context rot`, `compaction` (new), `fresh session`. Statelessness gets no term: the Messages API sentence and `fresh session` carry it. The Portuguese edition uses the fixed Portuguese term of each.
* Fundamentals are written from the primary sources below; no text of the author's earlier books is reused (ADR-0005).
* Watch the prose rules: state each point directly (`not-but`) and open no section with a short question (`reveal`).
* Sources, each checked on 2026-09-25 in the publication; the only number in the chapter is 18:
  * `[^messages-api]`: Anthropic, "Messages", accessed 2026-09-25. https://platform.claude.com/docs/en/build-with-claude/working-with-messages. Confirmed: "The Messages API is stateless, which means that you always send the full conversational history to the API." The page has no year, so the note carries the access date in its place (see docs/04 below).
  * `[^liu-2024]`: Liu et al., "Lost in the Middle: How Language Models Use Long Contexts", 2024. https://arxiv.org/abs/2307.03172. Confirmed in the abstract: performance "is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models". The year is the TACL volume's; if /apply does not find 2024 on the TACL page, it uses 2023, as arXiv says "accepted for publication in TACL, 2023".
  * `[^chroma-2025]`: Chroma, "Context Rot: How Increasing Input Tokens Impacts LLM Performance", 2025. https://research.trychroma.com/context-rot. Confirmed (technical report, 2025-07-14, Hong, Troynikov, Huber): "we evaluate 18 LLMs"; "model performance varies significantly as input length changes, even on simple tasks"; "their performance grows increasingly unreliable as input length grows".
  * `[^anthropic-context-2025]`: Anthropic, "Effective context engineering for AI agents", 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents. Confirmed (published 2025-09-29): context rot, "as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases", across all models; context as "a finite resource with diminishing marginal returns"; compaction, "taking a conversation nearing the context window limit, summarizing its contents, and reinitiating a new context window with the summary"; overly aggressive compaction "can result in the loss of subtle but critical context whose importance only becomes apparent later".
* Artifact: this repository's `AGENTS.md`, from its first line (`# One Page at a Time`) to the end of the §Read before acting list, copied from the file when /apply writes the chapter, in English in both editions (identifiers and documents are English), presented as what a fresh session reads first.
* Cases: none. No Ninjobs, no Case A or Case B, so no OD-3 approval.

The diagram, the book's first:

* What it shows: one call. A box, the context window, with a visible limit, holding in order: the host's instructions, the rules file, the files read, the tool output, the conversation so far; an arrow from the host into the box, marked as sent again on every call. Labels use the docs/03 terms of each edition.
* Files: `book/assets/02-context-window.en.svg` and `book/assets/02-context-window.pt.svg`, SVG text written by hand (no generator), with an opaque light background so it reads in the dark theme, and fonts that fall back to a generic family. Each edition links its own: `![<alt>](../assets/02-context-window.<edition>.svg)`, with the alt text in the edition's language.
* No new tool: MkDocs, pandoc with weasyprint, and EPUB readers show SVG as they are.

Documents changed:

* docs/04 §Files, the image line becomes: images are `book/assets/NN-<what>.png|svg`, with no text inside, so one image serves both editions; a diagram, whose labels are words, is an SVG written by hand, one per edition, `book/assets/NN-<what>.<edition>.svg`, with an opaque light background.
* docs/04 §Chapter shape, source notes: a publication without a date carries `accessed YYYY-MM-DD` in place of `<year>`.
* docs/01 §Stack, the Diagrams row: "SVG written by hand, one per edition, in `book/assets/`", why: no tool to install, and site, PDF and EPUB show SVG natively; Mermaid would bring back mermaid-cli and a browser into the build (ADR-0002, amendment).
* docs/adr/ADR-0002: an amendment dated the day of /apply, recording the decision above.

Files:

```
book/en/02-how-agents-see.md          chapter 2, no status: draft when done
book/pt/02-how-agents-see.md          chapter 2, no status: draft when done
book/assets/02-context-window.en.svg  the diagram, English labels
book/assets/02-context-window.pt.svg  the diagram, Portuguese labels
docs/04-Conventions.md                §Files diagram rule; §Chapter shape access date
docs/01-Architecture.md               §Stack Diagrams row
docs/adr/ADR-0002-mkdocs-material-and-pandoc.md  amendment
docs/03-Domain.md                     token, compaction (written by /propose)
```

**Out of scope.**

* Window sizes of any model: they change monthly and the book is not a host reference (docs/00).
* How each host loads its rules file and memory: chapter 5.
* The documents in depth: chapter 6. `/propose` and `/apply` in depth: chapters 10 and 11.
* SDD and its tools: chapter 3.
* Prompt caching, retrieval, MCP, multi-agent setups, prompt injection: none is needed to use the method.
* Tokenizers and the attention mechanism: one sentence on tokens is enough to reason about the limit.
* Mermaid and a diagram generator: decided against above.
* A check for diagrams or for SVG content: no error has happened that it would have caught (docs/05 §7).

**Done when.**

* [x] Both editions of chapter 2 written, same headings in the same order, `status: draft` absent from both.
* [x] Opens with its value in at most three sentences; ends with at most five key points; no exercises.
* [x] No filler and nothing useful cut: every sentence read against docs/00 product question 2.
* [x] Every number and quoted claim carries a source note whose text was found in the publication; any not found is dropped and recorded here.
* [x] The Portuguese edition uses `token`, `compactação`, `janela de contexto`, `degradação de contexto`, `sessão nova`, and no synonym.
* [x] The AGENTS.md excerpt matches the file byte for byte.
* [x] Both SVGs render on the site in light and dark themes and in the PDF and EPUB of their edition (`make book`); proof: `work/done/how-agents-see-<edition>-<where>.png` for site light, site dark and PDF, in both editions.
* [x] docs/04, docs/01 and ADR-0002 changed as the Contract says.
* [x] `make verify` green (build, parity, em dash, prose, links including the four source URLs, disclosure).
* [x] docs/06 line marked `[x]`; page moved to `work/done/how-agents-see.md` with what happened.

## What happened

* Written from the four sources, each fetched on 2026-09-25 and every quoted sentence found in it. The Liu note keeps 2024: the ACL Anthology lists the paper in TACL volume 12, 2024.
* Diverged: the Anthropic documentation page is titled "Using the Messages API", not "Messages"; the note uses the page's title.
* Diverged, by the author's choice during /apply: the Portuguese edition quotes each English source in English and follows it with its translation in parentheses. The rule went into docs/04 §Chapter shape, with the Portuguese form of the access date, `acesso em YYYY-MM-DD`.
* Contradiction found and resolved with the author: this page asked for screenshots, and docs/05 §5 said a chapter's proof is verify green alone. docs/05 §5 now says a chapter that brings a kind of content the build has not shown before (its first diagram) also proves it renders, in light and dark and in the PDF, both editions.
* Widened by one phrase: docs/01 §Stack, the Website row no longer gives "native Mermaid" as a reason, since the book does not use it. docs/01 §How the repository is organized says where the per-edition diagrams go.
* The diagram: one call, the host on top, an arrow "sent again on every call" into the context window, five bands in the order of the Contract, the rules file filled in the accent colour (the file section 6 is about), and a dashed limit line "limit, in tokens". 480 by 440, background `#fbfaf7`, Google Sans with generic fallbacks. The PDF has Google Sans from `pandoc/fonts/`, so it sets the diagram in the book's font; the site falls back to Roboto or the system font. The PDF sets the arrow label upright, since the book carries no italic Google Sans.
* The author's note on /design: not used. The page fixed an SVG written by hand, and one diagram is too few to set a visual identity for all of them. If later diagrams need one, it is a queue line of its own.
* The alt text is written as a caption, because pandoc prints it under the figure in the PDF and the EPUB; docs/04 §Files says so.
* Proof: `make verify` green. The Portuguese site resolves the image as `../../assets/02-context-window.pt.svg`, the English one as `../assets/02-context-window.en.svg`, both present in `site/assets/`. `make book` puts the diagram and its caption on page 8 of both PDFs and embeds it as `EPUB/media/file0.svg` in both EPUBs. The AGENTS.md excerpt compared with `diff` against `sed -n '1,/^- style and tests/p' AGENTS.md`, in both editions: identical. Screens: `work/done/how-agents-see-<en|pt>-<site-light|site-dark|pdf>.png`, taken with headless Chrome at 1280 by 2200 over the built site and with `pdftoppm` for page 8.
* Seen and left: weasyprint prints `Ignored user-select: none` twice, from pandoc's style for code blocks; this chapter has the book's first fenced block. It is a warning and changes nothing on the page.
