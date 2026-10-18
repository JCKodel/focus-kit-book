# 24. Asking for more

After this chapter you can send the challenge protocol, four messages, always the same, that follow an agent's first answer and are written out, ready to copy, under the section of that name, when the work is worth what they cost; and you can say why that first answer feels final and which four things an agent does not propose unless you ask.

## The card I accepted

On Case A, the client project of [chapter 17](17-project-as-assistant.md), the agent had to build cards for Microsoft Teams, written in Adaptive Cards, the format Teams uses to show a card in a chat.
The client sent a PowerPoint with the cards they imagined, and the agent had that file.
It did not build them.
It said the design looked more like a page than an Adaptive Card, and said something about tabs and buttons, though the client's design had no tabs.
I accepted the excuse, and the cards it built instead.
The client was unhappy with how they looked, and said so.
Only after that did the agent become a little more proactive and actually test what a Teams card can do.

The slip was mine as much as the agent's: it called the design unfeasible without testing it, and I accepted that without asking for the test.
The second of the four messages below would have made the agent test its claim and show me a card built from the client's PowerPoint before I accepted anything.

## The challenge protocol

The challenge protocol is four messages, always the same, that you send after the first answer, one at a time, each when the agent's reply to the previous one ends; each message and the agent's reply to it is a turn.
These are the four turns sent in the experiment this chapter's last section reports; copy them as they are:

```text
1. Before you change anything, ask me what you need to know to do
   this well.
2. What did you say is not possible, or not worth doing? Test each
   one and show me the result.
3. Who reads or uses this, how much time do they have, and what does
   each use cost? Change the result to fit.
4. What did I not ask for that I would want? Add what is worth it,
   and tell me what you left out.
```

**Turn 1 puts the questions before the work.**
The agent knows what it lacks better than you can guess, and "before you change anything" keeps it from rebuilding on a guess.
Answer its questions from what you know: who uses the result, on what, with how much time, what it costs.
That is the part of the work that was never in its window, and only you have it.
A question you cannot answer, say so, and let the agent choose.

**Turn 2 asks for a test, not for doubt.**
Asking "Are you sure?" invites a new answer chosen to please you.
Sharma and colleagues, researchers at Anthropic, measured it: after "Are you sure?", the models changed their first answer between 32% (GPT-4) and 86% (Claude 1.3) of the time.[^sharma-2024]
They call this sycophancy: a model tells the person what they seem to want, and drops a right answer as easily as a wrong one.
A test returns a result that does not depend on what you seem to want.
"Or not worth doing" catches the quiet limits, the things the agent left out without saying it could not do them.

**Turn 3 names the reader and the cost.**
Who uses the result, with how much time, and what each use costs: two of the four things an agent does not propose unless asked, which a section below names, in one question.
"Change the result to fit" asks for the change, not for advice about it.

**Turn 4 asks for what you did not ask for, and keeps you deciding.**
"Worth it" asks the agent to weigh each addition, and "tell me what you left out" puts the rest in front of you.
You stay the one who decides, which is the role the prologue gives the person.

## Why the first answer feels final

Three findings explain why a person keeps the first answer, and none of them is about the agent.

**A person stops at good enough.**
Herbert Simon, the economist and psychologist who studied how people decide, wrote in 1956 that "*organisms adapt well enough to 'satisfice'; they do not, in general, 'optimize'.*"[^simon-1956]
A person looks for an answer that is good enough for what they can see, and stops there.
An agent's first answer usually is: it runs, it reads well, it does what was asked.

**A person takes the aid's answer in place of checking.**
Kathleen Mosier and Linda Skitka defined automation bias in 1996: "*the tendency to use automated cues as a heuristic replacement for vigilant information seeking and processing*" (quoted in Mosier and Manzey 2019).[^mosier-manzey-2019]
Skitka, Mosier and Burdick measured it in 1999, with 80 students on a simulated flight task, some with an automated aid and some without.[^skitka-1999]
On the six events the aid did not flag, those with the aid were right 59% of the time against 97% without it.[^skitka-1999]
When the aid recommended something wrong, on six occasions, all but one of the participants who had the aid followed at least one of the wrong recommendations.[^skitka-1999]

**A person lacks the time or the means to improve it.**
A 2025 survey by Microsoft Research and Carnegie Mellon University asked 319 knowledge workers for examples of their own work with generative AI.[^lee-2025]
Among what kept them from thinking critically about an answer, 44 named a lack of time, and 72 said it was hard to improve the answer by asking the model again.[^lee-2025]
In the same survey, more confidence in AI went with less critical thinking, as the workers reported it themselves; the survey measured what they said, not the quality of their work.

An unchecked answer costs little while the task is one the model does well, and much when it is not.
In an experiment with consultants of the Boston Consulting Group, Dell'Acqua and colleagues found that on tasks inside what the model did well, consultants with AI finished 25.1% faster, with quality up 29.9% to 33.9%.[^dell-acqua-2026]
On a task outside it, those with AI were 19 percentage points less likely to be correct than those without it.[^dell-acqua-2026]
Nothing on the answer says on which side of that line it fell.

## What the agent does not propose

An agent answers the question it was given, with what is in its context window.
Four things lie outside that question, so it does not offer them unless asked.
None of them is a lack of skill: each needs something the question did not carry, or work the question did not ask for.
The examples below come from an experiment this book ran on three tasks of the lending library, each sent to an agent as one short request: a Teams card showing a member's loans, a summary of the library's annual report for its board, and a project set up for an agent that answers the team's questions every day (the last section of this chapter gives the results).

**To test a limit it claimed.**
When an agent says something cannot be done, it says so from what it remembers of the tool, and a test costs turns that nobody asked it to spend.
On the card task, one first answer said plainly that it had not been able to check the card and left the check to the person.[^ask-for-more-run]
Asked to test, the agents found what they had stated without checking: on the card, styles Teams does not show and elements its documentation did not confirm; in a summary for a board, decisions it had called routine that the report itself ranked among the most important.

**To fit the result to its reader's time.**
"Summarize the report for the board" does not say that the board has little time and reads on a phone.
The three first answers wrote their summary in the chat, with tables a phone cannot show; every challenged answer wrote a file with no tables, the board's decisions first.[^ask-for-more-run]

**To fit the result to the cost of each use.**
"Set the project up for an agent that answers the team every day" does not say that each question opens a fresh session and spends tokens, from the team's bill or from its plan's session limit.
Each first answer wrote one long guide for the agent without asking, and the judge found in two of them values copied from the code, which go stale without a sign when the code changes.[^ask-for-more-run]

**What nobody asked for.**
An agent that answers the question does not add what was not in it.
The challenged answers added what a person would have wanted and did not think to ask: a check file the agent runs against new notes so the guide stays right, the expiry of a grant and the fact that the accounts were not yet audited, a list of questions for the library's management.

## What the protocol bought, and what it cost

The experiment had three arms, each run three times on the same model, each run recording the first answer and then the answer after the four turns.[^ask-for-more-run]
In the limit arm, the agent built a Teams card with three tabs for a library member, for desktop and phone, to look like a small app.
In the audience arm, it summarized a long annual report for a board that decides the budget.
In the cost arm, it set up a small project for an agent that answers the team's questions every day, on notes that keep growing.

Each pair, first and challenged, was scored blind on three criteria of the arm, 1 to 5 each, so an arm sums to at most 45 over its three pairs.[^ask-for-more-run]

| Arm | First | Challenged |
|---|---|---|
| limit | 31 | 39 |
| audience | 36 | 44 |
| cost | 24 | 39 |

The judge would have sent the challenged answer in all 9 pairs.[^ask-for-more-run]

The challenge was paid for in time and tokens.
With the three runs of each arm summed, the challenged sessions took 2.9 to 8.8 times as long as the first answers, and wrote 2.7 to 9.4 times the output tokens.[^ask-for-more-run]
One session at a time, a first answer took 24 seconds to just over 2 minutes, and a challenged session 3 to 9 minutes.[^ask-for-more-run]

On a fixed subscription, those tokens come out of the plan's session limit: the use of the model a plan allows in a window of hours, after which the host refuses new turns until the window ends.
The experiment's nine challenged sessions, run within about 45 minutes on one afternoon, spent my plan's limit before the protocol's last turn, which in all nine was sent again about 30 minutes later.[^ask-for-more-run]
Each protocol you send spends a share of that limit.
If you pay per token instead, [chapter 22](22-cost-and-where.md) shows how to turn tokens into a price.

The cost arm also measured what each setup costs in use.
Five questions about the project, each in a fresh session, were asked of every setup: all 30 answers were correct, first and challenged.[^ask-for-more-run]
In each of the cost arm's three runs, the five questions took the challenged setup 14% to 26% less time than the first-answer setup of the same run, and the challenged setup's five sessions wrote fewer output tokens in two runs and 9% more in the third.[^ask-for-more-run]

The limits are plain.
Three pairs per arm is a recorded experiment, not a study, and has no statistics.
The judge was a fresh session of the same model that wrote the answers, not the author, and it may share that model's taste; in some pairs it could also tell which answer came later.

So spend the protocol's time and tokens where the result pays them back: a result used many times or by someone with little time, such as a card members open every day, a summary a board decides on, a setup that spends tokens on every question.
Skip it for an answer you will check yourself in a minute.
When the agent says "not possible", turn 2 alone is the cheapest test there is.

## What the team gains

The prologue's role, that the person validates and trusts no one blindly, becomes four sentences anyone on the team can type, developer or not.
On the experiment, the answers they produced were the ones a blind judge would send in 9 of 9 pairs, for about 3 to 9 times the first answer's time and output tokens.[^ask-for-more-run]
What they avoid is what the studies measured: answers taken unchecked, from an aid, by people short of time, on tasks where the model may be wrong without showing it.[^dell-acqua-2026]

## Key points

* A first answer feels final because a person stops at good enough (Simon), takes the aid's answer in place of checking (automation bias, Skitka), and lacks the time or the means to improve it (Lee et al.).
* An agent does not propose, unasked, to test a limit it claimed, to fit the result to its reader's time, to fit it to the cost of each use, or what nobody asked for.
* The challenge protocol is four turns, sent one at a time after the first answer: (1) "Before you change anything, ask me what you need to know to do this well."; (2) "What did you say is not possible, or not worth doing? Test each one and show me the result."; (3) "Who reads or uses this, how much time do they have, and what does each use cost? Change the result to fit."; (4) "What did I not ask for that I would want? Add what is worth it, and tell me what you left out."
* Turn 2 asks for a test because "Are you sure?" invites sycophancy, a new answer chosen to please.
* Send the protocol where the result is used often or read in a hurry: it costs about 3 to 9 times the first answer's time and output tokens, which a subscriber pays from the plan's session limit, and its evidence is three pairs per arm, judged by the same model.

[^ask-for-more-run]: J.C. Ködel, "One Page at a Time", the record of the challenge protocol experiment, 2026-10, in the book's repository. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/ask-for-more-experiment-run>
[^simon-1956]: Herbert A. Simon, "Rational choice and the structure of the environment", 1956. <https://doi.org/10.1037/h0042769>
[^mosier-manzey-2019]: Kathleen L. Mosier and Dietrich Manzey, "Humans and Automated Decision Aids: A Match Made in Heaven?", 2019. <https://d-nb.info/1223023044/34>
[^skitka-1999]: Linda J. Skitka, Kathleen L. Mosier and Mark Burdick, "Does automation bias decision-making?", 1999. <https://web.archive.org/web/2020id_/http://lskitka.people.uic.edu/AutomationBias.pdf>
[^lee-2025]: Hao-Ping Lee et al., "The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers", 2025. <https://doi.org/10.1145/3706598.3713778>
[^dell-acqua-2026]: Fabrizio Dell'Acqua et al., "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality", Organization Science, 2026. <https://doi.org/10.1287/orsc.2025.21838>
[^sharma-2024]: Mrinank Sharma et al., "Towards Understanding Sycophancy in Language Models", 2024. <https://arxiv.org/abs/2310.13548>
