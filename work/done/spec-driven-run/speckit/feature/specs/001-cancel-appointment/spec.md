# Feature Specification: Client Appointment Cancellation

**Feature Branch**: `001-cancel-appointment`

**Created**: 2026-09-25

**Status**: Draft

**Input**: User description: "A client can cancel their own appointment up to 24 hours before it starts. A cancelled appointment frees its slot. A cancellation later than that is refused with a message that says why."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Cancel an appointment in good time (Priority: P1)

A client who has booked an appointment finds they can't make it. At least 24 hours before the
appointment starts, they cancel it. The appointment is marked as cancelled and the client gets
confirmation that the cancellation went through.

**Why this priority**: This is the core ability the feature exists for. Without it nothing else
in this spec applies.

**Independent Test**: Book an appointment more than 24 hours in the future, cancel it as the same
client, and check that it now shows as cancelled.

**Acceptance Scenarios**:

1. **Given** a client has a booked appointment starting 3 days from now, **When** that client
   cancels it, **Then** the appointment's status becomes "cancelled" and the client is told the
   cancellation succeeded.
2. **Given** a client has a booked appointment starting exactly 24 hours from now, **When** that
   client cancels it, **Then** the cancellation is accepted (exactly 24 hours counts as "up to
   24 hours before").

---

### User Story 2 - Late cancellation is refused with a reason (Priority: P1)

A client tries to cancel an appointment that starts in less than 24 hours. The cancellation is
refused, the appointment stays booked, and the client is told why: cancellations must be made at
least 24 hours before the appointment starts.

**Why this priority**: The 24-hour rule is the business rule this feature protects. Letting late
cancellations through, or refusing them silently, would both break the clinic's policy.

**Independent Test**: Book an appointment less than 24 hours in the future, try to cancel it, and
check that it is still booked and that the refusal message names the 24-hour rule.

**Acceptance Scenarios**:

1. **Given** a client has a booked appointment starting in 23 hours 59 minutes, **When** that
   client tries to cancel it, **Then** the cancellation is refused, the appointment stays booked,
   and the message explains that appointments can only be cancelled at least 24 hours before they
   start.
2. **Given** a client has a booked appointment that has already started or is in the past,
   **When** that client tries to cancel it, **Then** the cancellation is refused with the same
   24-hour explanation.

---

### User Story 3 - A cancelled appointment's slot can be booked again (Priority: P2)

After a client cancels, the time they had is free again, so another client (or the same one) can
book it.

**Why this priority**: This is the clinic's benefit from cancellations — no lost appointment time.
It depends on Story 1 working first.

**Independent Test**: Book a slot, cancel it in good time, then book the same start time for a
different client and check that the booking succeeds.

**Acceptance Scenarios**:

1. **Given** client A's appointment at a given time has been cancelled, **When** client B books
   that same time, **Then** the booking succeeds.
2. **Given** client A's appointment at a given time is still booked, **When** client B tries to
   book that same time, **Then** the booking is refused because the slot is taken.

---

### Edge Cases

- A client tries to cancel an appointment that belongs to someone else: refused, the appointment
  is unchanged, and the message says they can only cancel their own appointments.
- A client tries to cancel an appointment that is already cancelled: refused with a message saying
  it is already cancelled; nothing changes.
- A client tries to cancel an appointment that does not exist: refused with a message saying no
  such appointment was found.
- The cancellation arrives exactly at the 24-hour mark: accepted.
- When the deadline check and another refusal reason both apply (e.g. someone else's appointment
  that is also within 24 hours), the ownership/existence reason is reported first, so a client is
  never told details about an appointment that is not theirs.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Clients MUST be able to cancel an appointment they booked when the time remaining
  until it starts is 24 hours or more.
- **FR-002**: The system MUST refuse a cancellation when the time remaining until the appointment
  starts is less than 24 hours, including when the start time has already passed.
- **FR-003**: When a cancellation is refused because of the 24-hour rule, the system MUST tell the
  client that appointments can only be cancelled at least 24 hours before they start.
- **FR-004**: A refused cancellation MUST leave the appointment exactly as it was (still booked).
- **FR-005**: A successful cancellation MUST change the appointment's status to "cancelled"; the
  appointment record is kept, not deleted.
- **FR-006**: A slot MUST count as taken only while it holds a booked (not cancelled) appointment;
  a cancelled appointment MUST NOT stop anyone from booking the same start time.
- **FR-007**: The system MUST refuse to book a start time that already holds a booked appointment.
- **FR-008**: The system MUST refuse cancellation of an appointment by anyone other than the client
  who booked it, with a message saying why.
- **FR-009**: The system MUST refuse to cancel an appointment that is already cancelled, or that
  does not exist, with a message saying why.
- **FR-010**: Every refusal MUST carry a message a client can read and understand without further
  help.

### Key Entities

- **Appointment**: A client's reservation of a start time. Key attributes: which client booked
  it, when it starts, and its status — "booked" or "cancelled".
- **Slot**: A start time at the clinic. It is free unless a booked appointment occupies it.
- **Cancellation outcome**: Either success (appointment now cancelled) or refusal with a reason
  (too late, not your appointment, already cancelled, not found).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of cancellations requested 24 hours or more before the start are accepted, and
  100% requested later are refused.
- **SC-002**: Every refused cancellation shows a reason; 0 refusals without an explanation.
- **SC-003**: A slot freed by a cancellation can be booked by another client immediately, with no
  manual step by clinic staff.
- **SC-004**: A client can cancel an appointment in a single action once they have chosen it.
- **SC-005**: Each rule above (24-hour deadline, boundary at exactly 24 hours, slot freeing,
  ownership, already-cancelled) is covered by at least one automated test that fails if the rule
  is broken.

## Assumptions

- "Up to 24 hours before it starts" means the cancellation is allowed when at least 24 hours
  remain; exactly 24 hours is allowed, anything less is refused.
- Time is measured against the clinic's clock at the moment the cancellation is requested; time
  zones are not a concern for this single-location clinic.
- A "slot" is identified by its start time; the clinic can hold one appointment per start time.
  Booking does not currently enforce this, so this feature adds that check (FR-007) so that
  "freeing a slot" has meaning.
- A client is identified by the name they booked under; there is no separate login or account
  system in scope.
- Clinic staff cancelling on a client's behalf, late-cancellation fees, waitlists, and notifying
  other clients about freed slots are out of scope.
- Refusal messages are in English.
