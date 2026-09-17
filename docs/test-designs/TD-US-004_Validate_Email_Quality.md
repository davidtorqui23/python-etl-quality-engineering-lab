# TD-US-004

## Story
US-004

Validate Email Quality

---

## Feature
Validate Email Quality

---

# Positive Scenarios

## TS-001
Dataset contains valid email addresses.

Expected Result:
Validation passes.

---

## TS-002
Dataset contains an email column.

Expected Result:
Validation confirms the column is present.

---

# Negative Scenarios

## TS-003
Dataset contains malformed email values.

Expected Result:
Validation failure with invalid row details.

---

## TS-004
Dataset contains blank email values.

Expected Result:
Validation failure with blank row details.

---

## TS-005
Dataset is missing the email column.

Expected Result:
Validation failure with missing column message.

---

# Data Quality Risks
- Missing values
- Invalid domain formatting
- Missing @ symbol
- Leading/trailing whitespace
- Missing schema field

---

# Automation Strategy

Automation Level:
High

Framework:
Pytest

Validations:
- email column exists
- values are not blank
- values match expected email format
- invalid rows reported
- validation result returned
