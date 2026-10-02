A lending library's members see their loans in Microsoft Teams.

## card.json

An Adaptive Card (v1.2) with sample data for one member. Whatever sends it
must fill in these values for each member on each send:

- **First tab:** set `isVisible: true` on `tabOverdue` if anything is overdue,
  otherwise on `tabActive`. The other two panels get `false`.
- **Selected tab marker:** the selected tab's button title starts with `● `
  in its own panel. Teams ignores button styles, so this is the only marker.
- **Tab counts:** the numbers in the button titles, e.g. `Overdue (1)`.
- **Next due:** the earliest due date among active loans. Leave out the line
  if there are none.
- **Day counts:** "N days left" and "N days overdue" are plain text. Cards
  can't calculate them.
- **Updated:** the date the card was made, so members can tell how old the
  day counts are.
- **Dates:** `{{DATE(YYYY-MM-DDT12:00:00Z, SHORT)}}`, all caps, no extra
  spaces. Anything else shows up as raw text. Midday UTC keeps the day right
  in most time zones; use the library's own offset if members are mostly
  local.
- **Empty tabs:** if a tab has no loans, show a line such as "Nothing
  overdue" instead of an empty panel.
