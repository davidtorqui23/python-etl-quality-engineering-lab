# US-003

## Title

Validate Customer ID Quality

## Business Value

As a Data Quality Engineer

I want to validate customer IDs

So that malformed identifiers are rejected before downstream processing

## Acceptance Criteria

- Customer ID column exists.
- Customer IDs are not null or blank.
- Customer IDs contain only numeric characters.
- Invalid customer IDs are reported with row context.
- Validation result is returned.
