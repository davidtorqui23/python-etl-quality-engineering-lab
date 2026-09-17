# US-007

## Title

Generate Data Quality Summary

## Business Value

As a Data Quality Engineer

I want a quality summary report

So that I can understand the quality of the processed dataset before load operations

## Acceptance Criteria

- The summary reports the total record count.
- The summary reports valid and invalid record counts.
- The summary reports invalid email counts.
- The summary reports invalid phone number counts.
- The summary reports invalid customer ID counts.
- The summary is generated from the validated dataset before load operations.
- The summary uses the shared logger in src/common/logger.py and logs in English.
