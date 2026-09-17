# ID-US-007

## Story
US-007

Generate Data Quality Summary

---

## Feature
Generate Data Quality Summary

---

## Goal
Create a reusable summary function that evaluates dataset quality before load operations and returns counts for total, valid, and invalid records as well as invalid email, phone, and customer ID values.

---

# Proposed Modules

src/common/

---

# Proposed Files

src/common/data_quality_summary.py

---

# Proposed Function

generate_data_quality_summary(dataframe)

---

# Responsibilities

## generate_data_quality_summary(dataframe)
Compute:
- total_records
- valid_records
- invalid_records
- invalid_emails
- invalid_phone_numbers
- invalid_customer_ids

Apply validation logic for:
- email format
- phone format
- customer_id numeric format

Return structured dictionary for ETL decision-making.

---

# Error Handling

ValueError

Missing column checks should not fail the summary unless the source dataframe is None.

---

# Dependencies

Pandas

re

src.common.logger

---

# Status
Ready for verification
