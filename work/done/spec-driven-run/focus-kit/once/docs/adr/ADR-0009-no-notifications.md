# ADR-0009: No notifications

**2026-09-25 · decided in /analyze.** Context: the module only books and answers the code that calls it. Decision: nobody is notified of anything, by email, SMS or otherwise. Consequences: no messaging dependency or side effect; a booking, refusal or cancellation is visible only in the value the function returns.
