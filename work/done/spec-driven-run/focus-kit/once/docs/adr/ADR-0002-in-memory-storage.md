# ADR-0002: Appointments live in memory

**2026-09-25 · observed, confirmed by the person.** Context: `src/appointment.ts` keeps appointments in a module-level array, and a delivery to make them survive a restart was offered and left out. Decision: storage stays in memory; no database, file or network. Consequences: a restart starts empty; there is no repository layer to build; tests must say how they start from an empty store; bringing storage in means amending this ADR and docs/00 first.
