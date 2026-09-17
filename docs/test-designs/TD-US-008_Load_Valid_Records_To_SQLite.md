# TD-US-008

## Story
US-008

Load Valid Records To SQLite

---

## Feature
Load Valid Records To SQLite

---

# Positive Scenarios

## TS-001
Dataset contains all valid rows.

Expected Result:
All rows are inserted into SQLite and the inserted count matches the total row count.

---

## TS-002
Dataset contains some invalid rows.

Expected Result:
Only valid rows are inserted and the rejected count reflects the invalid rows.

---

## TS-003
Load operation runs twice.

Expected Result:
The database remains idempotent and the table is refreshed to the valid rows only.

---

# Negative Scenarios

## TS-004
Dataset contains blank or invalid email addresses.

Expected Result:
Rows are rejected and excluded from the load.

---

## TS-005
Dataset contains non-numeric customer IDs.

Expected Result:
Rows are rejected and excluded from the load.

---

## TS-006
Dataset contains invalid phone numbers.

Expected Result:
Rows are rejected and excluded from the load.

---

# Data Quality Risks
- Invalid customer ID values
- Invalid email formatting
- Invalid phone formatting
- Invalid load row counts
- Duplicate loads without cleanup

---

# Automation Strategy

Automation Level:
High

Framework:
Pytest

Validations:
- row counts match inserted records
- invalid records excluded
- load statistics returned
- execution logs created in English
