// Dates are calendar days written as "YYYY-MM-DD" strings. There are no times
// of day and no time zones: a loan is due on a day, not at an instant.

export type CalendarDate = string;

const PATTERN = /^\d{4}-\d{2}-\d{2}$/;
const MS_PER_DAY = 24 * 60 * 60 * 1000;

export function isCalendarDate(value: string): boolean {
  if (!PATTERN.test(value)) return false;
  const ms = Date.parse(`${value}T00:00:00Z`);
  return !Number.isNaN(ms) && new Date(ms).toISOString().slice(0, 10) === value;
}

function toUtcMs(date: CalendarDate): number {
  return Date.parse(`${date}T00:00:00Z`);
}

export function addDays(date: CalendarDate, days: number): CalendarDate {
  return new Date(toUtcMs(date) + days * MS_PER_DAY).toISOString().slice(0, 10);
}

// Whole days from `from` to `to`; negative when `to` is earlier.
export function daysBetween(from: CalendarDate, to: CalendarDate): number {
  return Math.round((toUtcMs(to) - toUtcMs(from)) / MS_PER_DAY);
}
