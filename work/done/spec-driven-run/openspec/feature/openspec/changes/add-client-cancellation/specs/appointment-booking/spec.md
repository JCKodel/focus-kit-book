# Spec Delta

## Purpose

Lets the clinic record an appointment for a named client at a start time in clinic local time, with at most one booked appointment per start time.

## ADDED Requirements

### Requirement: Book an appointment for a client
The system SHALL let a caller book an appointment by giving a client name and a start time. A new appointment SHALL have a unique identifier, the given client name and start time, and the status `booked`.

#### Scenario: Booking a free start time
- **WHEN** a caller books an appointment for client "Ana" at a start time that no booked appointment holds
- **THEN** the system returns an appointment with a new identifier, client name "Ana", that start time, and status `booked`

### Requirement: One booked appointment per start time
A start time SHALL be held by at most one appointment with status `booked`. The system SHALL refuse to book a start time that a booked appointment already holds, with an error message that says the slot is already taken. Appointments with status `cancelled` SHALL NOT hold their start time.

#### Scenario: Booking a start time that is already taken
- **WHEN** a booked appointment exists at a start time and a caller books another appointment at the same start time
- **THEN** the booking is refused with an error message that says the slot is already taken
- **AND** no new appointment is created

#### Scenario: Booking a start time whose appointment was cancelled
- **WHEN** the only appointment at a start time has been cancelled and a caller books an appointment at that start time
- **THEN** the booking succeeds and the new appointment has status `booked`
