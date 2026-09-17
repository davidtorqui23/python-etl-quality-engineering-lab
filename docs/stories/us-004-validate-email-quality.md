# US-004

## Title

Validate Email Quality

## Business Value

As a Data Quality Engineer

I want to validate email addresses

So that malformed email values are rejected before downstream processing

## Acceptance Criteria

- Email column exists.
- Email values are not null or blank.
- Email values match the expected email pattern.
- Invalid emails are reported with row context.
- Validation result is returned.
