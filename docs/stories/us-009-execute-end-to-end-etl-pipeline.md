# US-009

## Title

Execute End-To-End ETL Pipeline

## Business Value

As a Data Quality Engineer

I want to execute the complete ETL process

So that raw data can be transformed into trusted and loaded data through an automated pipeline

## Acceptance Criteria

- Raw data is read from the source file.
- Schema validation is performed.
- Customer ID validation is performed.
- Email validation is performed.
- Phone validation is performed.
- Data normalization is executed.
- A data quality summary is generated.
- Valid records are loaded into SQLite.
- Invalid records are rejected.
- Execution logs are created in English.
- The ETL pipeline executes successfully as a single end-to-end flow.
