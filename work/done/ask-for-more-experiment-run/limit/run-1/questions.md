# Questions: limit, run 1

Each time the agent asked something, its message (the last text block of that turn, byte for byte) and the answer sent, which uses only the lines of `../brief.md` or "Use your judgment.".

## Asked in turn 2, answered in turn 3

Asked:

    Sure. I'll leave `card.json` alone until you've answered. These are the questions that would change the card most, roughly in order of impact:

    1. **How will the card be sent?** Will a bot post it, an incoming webhook or Power Automate, or a message extension? Webhooks and Power Automate posts can't handle `Action.Submit`, so the Renew/Pay buttons would need to become links (`Action.OpenUrl`) or be removed.
    2. **Who sees it, the member or library staff?** That decides which buttons belong. "Send reminder" fits staff, and "Pay late fee" fits the member.
    3. **Static sample or template?** Should the card keep fixed sample data, or be an Adaptive Card template (`${member.name}`, `$data` loops) with a separate `data.json`, so your code can fill in real loans?
    4. **What kind of loans?** I assumed library books. If they're equipment, financial loans or something else, the fields (title/author, due date, fees) need to change.
    5. **Which fields does each loan need?** For example item ID or barcode, cover image, renewal count, branch, fee details. Also, should History show fees paid or return condition?
    6. **Is the tab approach acceptable?** Teams has no real tabs, so the card swaps between three copies of the tab bar. Would you accept something simpler, like three buttons with no highlighted tab, to keep the JSON shorter?
    7. **Do you need mobile support or a minimum Teams version?** I used card version 1.5 and full width. If older clients or Outlook must render it, I'd target 1.4 or lower.
    8. **Any branding or wording requirements?** For example library name, colors, date format (US vs. other) and currency.

    If you only answer the first three, I can make sensible assumptions for the rest.

Answered:

    1. Use your judgment.
    2. The members open the card in Teams on desktop and on the phone.
    3. Use your judgment.
    4. Use your judgment.
    5. Use your judgment.
    6. The library wants it to look like a small app, not a list. Any feature that Teams' Adaptive Cards support may be used.
    7. The members open the card in Teams on desktop and on the phone. Any feature that Teams' Adaptive Cards support may be used.
    8. Use your judgment.

## Asked in turn 4, answered in turn 5

Asked:

    I could check four of the claims against Microsoft's documentation, and two were wrong or overstated. I couldn't test anything in Teams or the Designer: shell commands, web search and the adaptivecards.microsoft.com reference site were all blocked in this session. Pages on learn.microsoft.com did load, so these results come from Microsoft's Teams and Power Automate docs. I haven't changed `card.json`.

    | # | What I said | Result |
    |---|---|---|
    | 1 | Adaptive Cards have no real tabs, so I faked them. | **Holds, but not fully checked.** The Teams card reference and formatting pages list no tab element. Teams' only carousel is a bot sending several separate cards to swipe through, not tabs inside one card. The full element list is on adaptivecards.microsoft.com, which was blocked. |
    | 2 | Highlighting the selected tab needs three copies of the tab bar. | **Overstated.** The show/hide action can hide any element that has an ID, not just whole bars. One tab bar could hold a "selected" and an "unselected" version of each tab, and the buttons would switch those. That gives the same look with much less JSON. I haven't built or rendered it. |
    | 3 | Webhooks and Power Automate can't handle `Action.Submit`, so the buttons would need to become links. | **Half wrong.** Webhooks are confirmed: the docs say all elements work "except `Action.Submit`". Power Automate was wrong: its "post adaptive card **and wait for a response**" action does handle `Action.Submit`. However, "each Adaptive Card can be submitted only once." On this card, the first Renew or Borrow again click would be the only one that works, so a bot is still the right choice. |
    | 4 | The card can't act on button clicks by itself; a bot has to handle them. | **Confirmed.** The `Action.Execute` docs say they "bring the bot as the common backend for handling actions". |
    | 5 | Older clients or Outlook would need card version 1.4 or lower. | **Doesn't apply to your setup.** "Microsoft Teams mobile app supports Adaptive Cards up to version 1.6," and desktop does too. The card uses 1.5, so it's fine on both. I didn't check Outlook, and you don't need it. |
    | 6 | I left out book cover images so nothing depends on outside links. | **They're possible, with limits.** Images must be public HTTPS links to PNG, JPEG or GIF files of at most 1024 × 1024 pixels, and the docs say a link that redirects to the image isn't supported. Covers would work if the library hosts them itself. I couldn't check whether free cover services redirect. |
    | 7 | I couldn't check that the JSON is valid. | **Still true.** Running commands is blocked for this whole session, so I didn't try again. The Power Automate docs suggest pasting the JSON into the Adaptive Cards Designer or using the "Adaptive Card Viewer" extension for VS Code. |

    **Problems this found in `card.json`:**
    - **Green buttons won't show.** The docs say "Positive or destructive action styling is not supported in Adaptive Cards on the Teams platform." Renew and Pay $3.50 have `"style": "positive"`, so Teams ignores it and they look like normal buttons.
    - **Badge and ProgressBar are undocumented in the Teams docs I could reach.** Icon and button icons (`icon:Name`) are documented with the sizes, colours and styles I used. Badge and ProgressBar aren't, and they're also missing from the list of elements a fallback can use. Whether Teams supports them on phones is still unconfirmed, so the plain-text fallbacks matter.
    - **Icon names are unchecked.** I couldn't confirm names like `Library` and `ArrowRepeatAll` because the Fluent icon directory is on another site.
    - **Layout fits the guidance.** Microsoft advises at most three columns per row and fixed widths under about 48 px, and the card stays within that, which helps on phones.

    Should I remove the green button style and rebuild the tabs as a single tab bar (item 2)?

Answered:

    Use your judgment.
