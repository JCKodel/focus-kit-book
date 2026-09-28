# Brief

## Product
A scheduling app for one neighbourhood clinic. Clients book and cancel their own appointments with the clinic's professionals from their phones; the owner registers the professionals and their weekly hours.
Two sides: the client, who has no account and gives a name and a phone number; the owner, who signs in (your call how).
Rules: a professional cannot have two appointments at the same time. A client can cancel their own appointment up to 24 hours before it starts; a cancelled appointment frees its slot; a later cancellation is refused with a message that says why. Times are the clinic's local time.
Not: payments, notifications (SMS, email, push), medical records or any health data, more than one clinic.

## Stack
TypeScript, strict. A React PWA that the client and the owner open in the browser, over a small Node server that keeps the data in a SQLite file. No paid service: it runs on a machine at the clinic or on any free host.
Why: the most public code the agent learned from is in this language and library, and types and tests let it check its own work.

## Choices
FOCUS: FOCUS whole. Git: trunk.

## Conventions and process
English for documents and identifiers. Verify: created by the first delivery. Everything else: your call.

## First milestone
When it closes, the owner can register professionals and their weekly hours, a client can book a free slot, and a client can cancel up to 24 hours before. A professional's absences and the owner's view of the day come in the second milestone.

## Principles
Keep it simple. Every rule has a test. No em dash in any document.

## Rule for a question the brief does not answer
Answer "your call".
