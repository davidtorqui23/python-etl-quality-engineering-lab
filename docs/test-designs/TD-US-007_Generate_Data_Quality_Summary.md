# TD-US-007

## Story
US-007

Generate Data Quality Summary

---

## Feature
Generate Data Quality Summary

---

# Positive Scenarios

## TS-001
Validated dataset includes all required fields.

Expected Result:
Summary returns total, valid, and invalid record counts.

---

## TS-002
Dataset includes invalid email values.

Expected Result:
Invalid email count is included in the summary.

---

## TS-003
Dataset includes invalid phone values.

Expected Result:
Invalid phone count is included in the summary.

---

## TS-004
Dataset includes invalid customer IDs.

Expected Result:
Invalid customer ID count is included in the summary.

---

# Negative Scenarios

## TS-005
Dataset contains missing values.

Expected Result:
Missing values are counted as invalid records.

---

## TS-006
Dataset is empty.

Expected Result:
Summary returns zero counts without failing the process.

---

# Data Quality Risks
- Missing values in required fields
- Invalid email and phone formats
- Blank or non-numeric customer IDs
- Incomplete quality counts before load decisions

---

# Automation Strategy

Automation Level:
High

Framework:
Pytest

Validations:
- total records counted
- valid records counted
- invalid records counted
- invalid emails counted
- invalid phone numbers counted
- invalid customer IDs counted
- summary available before load operations
