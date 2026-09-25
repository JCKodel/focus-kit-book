# Spec Delta

## Purpose

Lets a client cancel their own appointment with at least 24 hours' notice so that the slot becomes available to others, and explains any refused cancellation.

## ADDED Requirements

### Requirement: Client cancels their own appointment with 24 hours' notice
The system SHALL let a caller cancel an appointment by giving the appointment identifier, the client name, and the current time in clinic local time. The cancellation SHALL succeed when the appointment is booked, belongs to that client name, and starts 24 hours or more after the current time. A successful cancellation SHALL set the appointment's status to `cancelled` and return the appointment. The appointment record SHALL be kept. The system SHALL NOT send any notification.

#### Scenario: Cancelling well ahead of time
- **WHEN** client "Ana" cancels their booked appointment 48 hours before it starts
- **THEN** the cancellation succeeds and the appointment's status is `cancelled`

#### Scenario: Cancelling exactly 24 hours ahead
- **WHEN** client "Ana" cancels their booked appointment exactly 24 hours before it starts
- **THEN** the cancellation succeeds and the appointment's status is `cancelled`

### Requirement: Late cancellation is refused
The system SHALL refuse a cancellation when the appointment starts less than 24 hours after the current time, including when the start time has already passed. The error message SHALL say that appointments can only be cancelled at least 24 hours before they start. A refused cancellation SHALL leave the appointment unchanged.

#### Scenario: Cancelling less than 24 hours ahead
- **WHEN** client "Ana" cancels their booked appointment 23 hours and 59 minutes before it starts
- **THEN** the cancellation is refused with an error message that says cancellations must be made at least 24 hours before the start
- **AND** the appointment's status stays `booked`

#### Scenario: Cancelling after the start time
- **WHEN** client "Ana" cancels their booked appointment after its start time has passed
- **THEN** the cancellation is refused with an error message that says cancellations must be made at least 24 hours before the start

### Requirement: Only the client who owns the appointment can cancel it
The system SHALL refuse a cancellation when the given client name does not exactly match the appointment's client name, with an error message that says the appointment does not belong to that client. The appointment SHALL stay unchanged.

#### Scenario: Another client tries to cancel
- **WHEN** client "Ben" tries to cancel an appointment booked by "Ana"
- **THEN** the cancellation is refused with an error message that says the appointment does not belong to "Ben"
- **AND** the appointment's status stays `booked`

### Requirement: Unknown or already cancelled appointments cannot be cancelled
The system SHALL refuse a cancellation for an identifier that matches no appointment, with an error message that says the appointment was not found. The system SHALL refuse a cancellation for an appointment that is already cancelled, with an error message that says it is already cancelled.

#### Scenario: Unknown appointment
- **WHEN** a client cancels using an identifier that matches no appointment
- **THEN** the cancellation is refused with an error message that says the appointment was not found

#### Scenario: Cancelling twice
- **WHEN** client "Ana" cancels an appointment they have already cancelled
- **THEN** the cancellation is refused with an error message that says the appointment is already cancelled

### Requirement: A cancelled appointment frees its slot
Once an appointment is cancelled, its start time SHALL be free to book again.

#### Scenario: Rebooking a freed slot
- **WHEN** client "Ana" cancels their appointment in time and client "Ben" then books the same start time
- **THEN** the new booking for "Ben" succeeds
