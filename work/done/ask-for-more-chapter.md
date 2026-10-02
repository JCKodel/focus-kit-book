# ask-for-more-chapter

**Objective.** After chapter 25 the reader knows why an agent's first answer feels final, names the four things an agent never proposes on its own, and sends the challenge protocol when the work is worth its cost; the prologue tells them, in the place where it asks them to trust no one blindly, that this chapter exists.

**Behaviour.**

* A reader who stops after the prologue knows that validating an agent includes asking it for more, and that Part V, chapter 25, shows how.
* A reader of chapter 25 can say, with a source for each, three reasons a first answer gets accepted: a person stops at the first answer good enough (Simon), takes the aid's answer in place of checking (automation bias, Skitka), and lacks the time or the means to improve it (Lee et al.).
* They can name the four things an agent does not propose unasked: to test a limit it claimed, to fit the result to its reader's time, to fit it to the cost of each use, and what nobody asked for.
* They can type the four turns of the challenge protocol, and say why turn 2 asks for a test and not "Are you sure?" (sycophancy, Sharma et al.).
* They know what the protocol bought on the book's experiment and what it cost: the blind judge sent the challenged answer in 9 of 9 pairs, and the challenged session cost 2.6 to 8 times the first answer; so they can decide when it is worth sending.
* They read Case A's card as the author's own slip, and read, in the same section, that the experiment did not reproduce it: no first answer called the tabs impossible.
* They know the experiment's limits: three pairs per arm, not a study, and the judge was a fresh session of the model that wrote the answers, not the author.

**Contract.**

Files:

```
book/en/25-asking-for-more.md    new; # 25. Asking for more
book/pt/25-asking-for-more.md    new; # 25. Pedir mais
book/en/00-product-people-process.md   the seed; the parts map
book/pt/00-product-people-process.md   the same, translated
docs/00-Product.md               Contents gains Part V; Audience
docs/adr/ADR-0017-the-rewrite.md amendment: Part V, chapter 25
docs/06-Queue.md                 ask-for-more-chapter [x]
```

No draft marker: the chapter is written whole in this delivery.

The prologue (both editions):

* §People, **Ego**: after "The answer is a role: the person interprets, guides and validates, and trusts no one blindly, agent or colleague, the author of the code included.", one or two sentences: validating includes asking for more, because an agent's first answer is rarely the best it can give and it does not offer what you did not ask for; Part V shows how to ask.
* §What the team gains, the parts map: after the Part IV line, "Part V is the person: why an agent's first answer feels final, and how to ask for more." (pt: "A Parte V é a pessoa: ...").

docs/00: Contents gains the row `| V. The person decides | 25 Asking for more |`; Audience: every audience reads Part V (the non-coders' line becomes "the prologue, chapters 1 to 3, Part II, Part IV and Part V"; the tech leads' "Parts III, IV and V"; the developers new to process "Parts I, II and V").

Chapter 25, sections in order, each tied to a clause of M9's paragraph:

1. Opening, at most three sentences.
2. `## The card I accepted` (pt `## O card que eu aceitei`): Case A, the author's own slip (clause: Case A's Teams card). Text below, for OD-3.
3. `## Why the first answer feels final` (pt `## Por que a primeira resposta parece final`): satisficing, automation bias, the barriers people report, and what an unchecked answer costs outside what the model does well (clause: why the first answer feels final).
4. `## What the agent does not propose` (pt `## O que o agente não propõe`): the four, each with why the agent leaves it out, from what it sees (it answers the question it was given, with what is in its window); the experiment's first answers as the example of each (clause: what an agent never proposes).
5. `## The challenge protocol` (pt `## O protocolo de desafio`): the four turns verbatim, why each is worded as it is, and that the agent's questions are answered from what the person knows; chapter 2's index and chapter 23's cache are named as where the technique for the cost turn lives (clause: the protocol).
6. `## What the protocol bought, and what it cost` (pt `## O que o protocolo rendeu, e quanto custou`): the three arms in a sentence each, the scores, the cost, the cost arm's per-question numbers, the limits, and when it pays (clause: the experiment as the team's gain).
7. `## What the team gains`, `## Key points`.

The Case A passage, as it will read (English; the Portuguese is its translation), for the author's approval (OD-3):

> On Case A, the client project of chapter 18, the agent built a card for Microsoft Teams, written in Adaptive Cards, the format Teams uses to show a card in a chat.
> I wanted tabs on it.
> The agent said a card could not have tabs, and I took the answer and accepted the card without them.
> The client was disappointed with how it looked.
> Only then did I ask the agent to test what a Teams card renders, instead of telling me.
> It tested, found that the card could do more than it had said, and the card the client saw next pleased them.

Followed, in the same section, by: on the book's experiment, the same request on a newer model did not repeat it; none of the three first answers called tabs impossible, and all six cards switch tabs (checked from the card's JSON, not rendered in Teams); what the challenge changed there was the look, the phone, the reader's time and the cost. No email is quoted, nothing of the client appears.

The protocol, quoted as the reader types it (from `work/done/ask-for-more-experiment-run/prompts.md`):

1. "Before you change anything, ask me what you need to know to do this well."
2. "What did you say is not possible, or not worth doing? Test each one and show me the result."
3. "Who reads or uses this, how much time do they have, and what does each use cost? Change the result to fit."
4. "What did I not ask for that I would want? Add what is worth it, and tell me what you left out."

The Portuguese edition gives them translated and says before them that the experiment sent them in English.

Numbers the chapter may use, and only in these forms:

| Claim | Form | Key |
|---|---|---|
| Simon | "organisms adapt well enough to 'satisfice'; they do not, in general, 'optimize'", p. 129 | `simon-1956` |
| Skitka | 59% against 97% accuracy on the six events the aid did not flag (41% against 3% missed); on average 65% of the six wrong recommendations followed, all but one participant followed at least one; 80 students. Never "65% of participants" | `skitka-1999` |
| automation bias, definition | quoted only as "quoted in Mosier and Manzey 2019" | `mosier-manzey-2019` |
| Lee et al. | 319 knowledge workers' examples: lack of time 44, hard to improve the answer by re-prompting 72; more confidence in AI goes with less critical thinking reported (self-report, not measured quality) | `lee-2025` |
| Randazzo et al. | 244 consultants; 27% (63) handed the task to the model; 44% of those (28 of 63) took its output unchanged | `randazzo-hbs-26-036` |
| Dell'Acqua et al. | inside the frontier 12.2% more tasks, 25.1% faster, quality up 29.9% to 33.9%; outside it 19 percentage points less correct (84.5% against 60% and 70.6%); published version only | `dell-acqua-2026` |
| Sharma et al. | after "Are you sure?" models changed their first answer 32% (GPT-4) to 86% (Claude 1.3) of the time | `sharma-2024` |
| the experiment | rubric sums of 45, first against challenged: 31/39, 36/44, 24/39; sent challenged 9 of 9; cost for three runs 0.82/6.59, 1.09/3.39, 3.04/8.00 USD; cost arm 30 of 30 correct in both states, per five questions 20% and 16% cheaper in runs 1 and 2, 10% dearer in run 3; three pairs per arm; judge a fresh session of the same model | `ask-for-more-run` |

Note definitions follow docs/04 §Source notes, URLs from `sources.md`: `simon-1956` (DOI 10.1037/h0042769), `skitka-1999` (the author's copy linked in row 1), `mosier-manzey-2019` (https://d-nb.info/1223023044/34), `lee-2025` (DOI 10.1145/3706598.3713778), `randazzo-hbs-26-036` (the HBS PDF, year from its front page), `dell-acqua-2026` (DOI 10.1287/orsc.2025.21838), `sharma-2024` (https://arxiv.org/abs/2310.13548), `ask-for-more-run` shaped as `[^spec-driven-run]`, pointing to `https://github.com/JCKodel/focus-kit-book/tree/main/work/done/ask-for-more-experiment-run`. A study named for the first time is introduced in a few words (docs/04).

Terms of docs/03 it introduces: challenge protocol, automation bias, sycophancy (all three already in docs/03). It leans on context window (chapter 2).

Cases: Case A (the card, above). Not Ninjobs, not Case B. Exercises: none.

**Out of scope.**

* The research report's other studies (Kosmyna, Gerlich, Bastani, Perry, Shen and Tamkin, Drosos, ClarifyGPT, Self-Refine, Cheung): they do not carry this chapter's point; one chapter, one argument.
* METR again: chapter 1 holds it.
* The context and cost technique itself: chapters 2 and 23 hold it; chapter 25 names them.
* The meeting that started M9: decided out in `ask-for-more-experiment`.
* Any detail of Case A beyond the passage above, and the client's email.
* Narrating the runs (ADR-0017): only counted numbers and the four turns appear.
* README changes: the READMEs list no chapters.
* m9-review: its own delivery.

**Done when.**

* [x] Both editions of chapter 25 written, same headings, with the opening, the gain section and at most five key points; no draft marker.
* [x] The prologue seed and parts map in both editions; docs/00 and ADR-0017 updated.
* [x] Opens with its value; no filler and nothing useful cut; no run narrated.
* [x] Every number in the forms of the table above, each with its note; no "65% of participants", no 2023 Dell'Acqua figure.
* [x] The author approved the Case A passage (OD-3).
* [x] `make verify` green, disclosure scan included.
* [x] `make book` run; the paths of both PDFs given to the author.
* [x] Page moved to `work/done/`, docs/06 marked `[x]`.

## What happened

* **Written whole**, both editions, same headings and note keys, no draft marker. The prologue's seed names "chapter 25, in Part V" instead of "Part V" alone, so a reader finds it by its number, as the prologue does for chapters 10 and 18. The tech leads' Audience line in docs/00 also says what Part V is for ("asking an agent for more"), in the form of the other two parts it lists.
* **OD-3, and the story corrected.** The author first approved the passage above, then, reading the chapter, said it was wrong: nobody asked for tabs. The client sent a PowerPoint of the cards they imagined; the agent had it and did not build them, saying the design looked more like a page than an Adaptive Card, with a remark about tabs and buttons though the design had none; the author accepted the excuse; only after the client said they were unhappy did the agent test what a card can do. The author added that a person without an LLM could say "not possible" of a paper sketch from laziness or not knowing the platform, and that models only amplify it. The section now tells that, in the author's words, approved in Portuguese and translated; the claim that the next card pleased the client was dropped, since the author did not state it. The experiment's paragraph no longer says the slip "did not repeat": it says no first answer called anything the card shows impossible. The page's own premise (an agent calling tabs impossible) came from the first telling, and the experiment's record keeps that premise as it was when the run was planned.
* **Numbers**: only the forms of the table. The first answers in "What the agent does not propose" are described without the record's other counts (words, fetches, denied calls); each claim was checked against the record: all three audience first answers carried a table, two cost judges named values copied from the code, the challenged audience files have no tables. Sharma's "five models" was cut, since that count is not in the table. The brief's "10 minutes" reads as "little time" for the same reason.
* **The protocol** is a numbered list, not a code block, because turn 3 is wider than the 74 columns of docs/04; the Portuguese says before it that the experiment sent the turns in English. "Are you sure?" never stands alone on a line (prose rule `reveal`).
* **Simon's quotation** in Portuguese renders "satisfice" as "se contentar"; the original is at the source. Mosier and Skitka's definition appears only as quoted in Mosier and Manzey 2019; titles and years of every note were read from the sources' own first pages (Randazzo et al.: 2025, the paper's copyright line; Skitka et al.'s task, a simulated flight, from the author's copy).
* **Dropped at the author's request**: the paragraph after the card story that said the experiment did not repeat the slip. The author could not tell what it meant, so neither could a reader; the Behaviour line "read, in the same section, that the experiment did not reproduce it" is not met, by decision. The experiment stays in its own section, where its arms are explained; "What the agent does not propose", whose examples come from it, now opens them with one sentence on what the three tasks were, since the removed paragraph had been the reader's first sight of the experiment.
* **Limits said in the text** include one from the record's What diverged that the table does not carry as a number: in some pairs the judge could tell which answer came later.
* **Proof**: `make verify` green, disclosure scan included; `make book` built both PDFs and EPUBs, chapter 25 present in both. No new kind of content, so no screenshot (docs/05 §5).
* **The PDF's contents**: row 25 spilled alone onto a second page in both editions, so the author asked to fit it on one; `pandoc/pdf.css` sets the contents rows at 8.5pt with a 12pt line (were the body's 9pt and 12.75pt). Both editions' contents now fit one page, with room for about two more rows.
* **Documents**: docs/00 (contents, audience), ADR-0017 (amendment, Part V); docs/03's terms were added by `/propose` and stand as written.
