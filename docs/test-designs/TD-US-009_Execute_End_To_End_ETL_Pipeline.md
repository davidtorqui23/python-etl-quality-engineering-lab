# TD-US-009

## Story
US-009

Execute End-To-End ETL Pipeline

---

## Feature
Execute End-To-End ETL Pipeline

---

# Positive Scenarios

## TS-001
Raw dataset contains valid and invalid rows.

Expected Result:
The ETL pipeline validates, normalizes, summarizes, and loads the valid subset.

---

## TS-002
Raw dataset contains a valid schema.

Expected Result:
No structural validation failure occurs and the ETL flow proceeds.

---

## TS-003
Dataset includes invalid emails and phone values.

Expected Result:
Invalid rows are excluded from the final load and the quality summary reflects the exclusion.

---

## TS-004
Pipeline executes to completion.

Expected Result:
Execution logs show stage transitions and final summary output.

---

# Negative Scenarios

## TS-005
Dataset structure is invalid.

Expected Result:
The pipeline raises a ValueError before proceeding to transformation or load.

---

## TS-006
Dataset contains missing required column values.

Expected Result:
The validation layer rejects the invalid rows and the ETL flow continues with the valid subset.

---

# Data Quality Risks
- Missing or invalid schema columns
- Customer IDs with non-numeric values
- Malformed email entries
- Invalid phone number formats
- Unclear pre-load quality status
- Incomplete log coverage across ETL stages

---

# Automation Strategy

Automation Level:
High

Framework:
Pytest

Validations:
- raw dataset reads successfully
- schema validation passes or fails appropriately
- customer ID validation executes
- email validation executes
- phone validation executes
- normalization runs before summary generation
- data quality summary created
- valid records loaded to SQLite
- execution logs created in English
