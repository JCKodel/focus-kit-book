# Queue

`[ ]` not defined · `[>]` defined, work/<slug>.md exists · `[x]` done, page in work/done/

## Milestone 1: bookings that can be trusted
When it closes, staff can book an appointment, are refused with a readable value for a bad name, a past time or a taken slot, can cancel an appointment and can list one day's agenda; verify is green.

```
[ ] verify              Type-check and a first test; one command says the code is sound
[ ] book-validation     Booking with an empty name or a past time returns an error value
[ ] no-double-booking   A slot already taken is refused
[ ] cancel              An appointment can be cancelled; its status becomes cancelled
[ ] day-agenda          One day's appointments, in time order
```
