# ID-US-006

## Story
US-006

Normalize Customer Data

---

## Feature
Normalize Customer Data

---

## Goal
Implement a reusable normalization capability that standardizes customer data before downstream ETL processing continues.

---

# Proposed Modules

src/transform/

---

# Proposed Files

src/transform/normalize_customer_data.py

---

# Proposed Function

normalize_customer_data(dataframe)

---

# Responsibilities

## normalize_customer_data(dataframe)
Apply:
- trim whitespace across string fields
- lowercase email values
- canonical mapping for country values
- digits-only phone normalization
- output dataframe ready for ETL processing

## main()
Generate the normalized dataset artifact at:
- data/processed/orders_normalized.csv

---

# Error Handling

ValueError

KeyError

---

# Dependencies

Pandas

re

---

# Status
Ready for verification
