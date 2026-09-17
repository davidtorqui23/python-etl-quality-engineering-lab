# US-008

## Title

Load Valid Records To SQLite

## Business Value

As a Data Quality Engineer

I want valid records to be loaded into SQLite

So that downstream analytics and reporting can consume trusted data

## Acceptance Criteria

- A SQLite database is created under data/output.
- An orders table is created in the database.
- Only valid records are inserted into the table.
- Invalid records are rejected and excluded from the load.
- Inserted row count is validated after the load.
- Load statistics are generated for review.
- The shared logger is used and all log messages are in English.
