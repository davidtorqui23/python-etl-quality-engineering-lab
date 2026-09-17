# TD-US-006

## Story
US-006

Normalize Customer Data

---

## Feature
Normalize Customer Data

---

# Positive Scenarios

## TS-001
Dataset contains valid customer records.

Expected Result:
Normalization preserves integrity while trimming and standardizing values.

---

## TS-002
Dataset contains country aliases.

Expected Result:
Country values are standardized to canonical values.

---

# Negative Scenarios

## TS-003
Dataset contains extra spaces in string values.

Expected Result:
Leading and trailing whitespace is removed.

---

## TS-004
Dataset contains uppercase email addresses.

Expected Result:
Emails are normalized to lowercase.

---

## TS-005
Dataset contains phone values with formatting symbols.

Expected Result:
Phone numbers are converted to digits only.

---

# Data Quality Risks
- Leading or trailing whitespace in customer attributes
- Mixed case email addresses
- Country aliases and abbreviations
- Phone numbers containing spaces, punctuation, or country markers
- Inconsistent file output for downstream ETL steps

---

# Automation Strategy

Automation Level:
High

Framework:
Pytest

Validations:
- strings are trimmed
- email addresses normalized to lowercase
- country aliases mapped to canonical values
- phone number formatting stripped
- normalized output saved to processed dataset
