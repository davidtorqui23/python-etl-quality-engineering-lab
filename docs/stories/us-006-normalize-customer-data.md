# US-006

## Title

Normalize Customer Data

## Business Value

As a Data Quality Engineer

I want customer data to be normalized

So that downstream ETL processes consume standardized and consistent information

## Acceptance Criteria

- String fields are trimmed for leading and trailing whitespace.
- Email addresses are converted to lowercase.
- Country values are standardized to the canonical project values.
- Phone numbers are normalized by removing spaces and special formatting.
- Original data integrity is preserved while producing the normalized dataset.
- A normalized dataset is generated in the processed output location.
