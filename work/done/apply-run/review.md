# Review

The author's requests, each sent with `--continue` to the run's session as written here, and the agent's reply to each, its text blocks byte for byte. The tool calls are in `turn-2.txt` and `turn-3.txt`; the changes to the staged tree are in `review.diff`.

## Request 1, turn 2

````markdown
1. **A package the page didn't name.** The kit says to add no dependency the page did not name. The agent added `@hono/node-server` without stopping to ask; it only recorded it in docs/01.
2. **A proof missing from the page.** The claim that a second start applies nothing was proven only by a Vitest test. The agent said so in its reply, but the page's What happened doesn't.
3. **An explanation in the wrong place.** The agent wrote why `npm run dev` wasn't run inside the unticked Done when item itself, instead of in What happened.
4. **A rule nobody running headless can follow.** The clinic's docs/05 still says "a delivery leaves it running", which a headless agent can't do. You might want the document to say that you start it yourself.
5. **An untested claim.** The page says "Ctrl+C stops both". You can check this when you start `npm run dev`: port 3000 should be free afterwards.
````

## Reply to request 1

````markdown
You're right on all five. I've fixed the page and docs/05 and staged them again. Only documents changed, not code, so I didn't rerun verify.

1. **`@hono/node-server`:** I should have stopped and asked before adding it. The page now says it was added without being named and stays only if you approve it. **Do you keep it?** Hono needs it (or a hand-written adapter) to listen on a Node port. If you say no, I'll take it out of `package.json` and docs/01.
2. **Second start:** "What happened" now says this was proven only by the Vitest test and that the server was never started twice.
3. **`npm run dev`:** the Done when item is back to the bare checklist line, still unticked. The reason it wasn't run is now in "What happened": the session was headless, `data/clinic.sqlite` was created by the failing start, and no migration is recorded.
4. **docs/05:** the local environment now says a delivery leaves the code ready to start and names the command, and you start it.
5. **Ctrl+C:** the page now calls this untested and gives the check: after stopping `npm run dev`, `lsof -i :3000` should print nothing.

I also saved two notes for future `/apply` runs: ask before adding any package the page didn't name, and put every gap in the proof into the page, not just into my reply.

The suggested commit message is unchanged.

**Environments:**
- **local:** the code is at this delivery and `data/clinic.sqlite` exists with no migrations recorded, but nothing is running. Start it with `npm run dev`.
- **production:** doesn't exist yet. The `deploy` delivery will create it.
````

## Request 2, turn 3

The agent's question on `@hono/node-server`, answered with the author's choice:

````markdown
Keep it
````

## Reply to request 2

````markdown
`@hono/node-server` stays. The page now records that you approved it at review, and it's staged. docs/01 already lists it, so nothing else changed. The suggested commit message is the same as before.

**Environments:**
- **local:** the code is at this delivery and `data/clinic.sqlite` exists, but nothing is running. Start it with `npm run dev`.
- **production:** doesn't exist yet. The `deploy` delivery will create it.
````
