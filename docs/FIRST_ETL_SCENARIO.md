# First ETL Scenario

## Scenario Name

Orders Pipeline Validation

---

# Business Context

An e-commerce platform exports daily order information.

The data is extracted from a source system and loaded into a reporting database.

Before reporting can be trusted, Quality Engineering validations must confirm that the ETL process preserved data integrity.

---

# Source File

orders_raw.csv

---

# Source Columns

order_id

customer_id

customer_email

order_date

country

amount

status

---

# Sample Data Expectations

Each order:

- Must have an Order ID
- Must have a Customer ID
- Must have a valid Email
- Must have an Order Date
- Must contain an Amount greater than zero

---

# Transformation Rules

## Email Standardization

Transform:

JOHN@EMAIL.COM

Into:

john@email.com

---

## Country Normalization

Transform:

USA
US
United States

Into:

United States

---

## Duplicate Removal

Duplicate Order IDs are not allowed.

Only one record may remain.

---

## Amount Validation

Amounts must be greater than zero.

Invalid amounts must be flagged.

---

# Load Target

SQLite Database

Table:

orders_clean

---

# Required Validations

## Record Count Validation

Verify:

Source Count

equals

Target Count

after approved duplicate removal.

---

## Null Validation

Verify:

order_id

customer_id

order_date

amount

contain no null values.

---

## Duplicate Validation

Verify:

No duplicate order_ids exist.

---

## Schema Validation

Verify:

Source schema matches expected schema.

---

## Source-to-Target Validation

Verify:

Fields are correctly mapped.

Source:

customer_email

Target:

customer_email

after transformation.

---

# Expected Deliverables

Version 1.0

- Source Dataset
- Extract Layer
- Transform Layer
- Load Layer
- Validation Layer
- Validation Report

---

# Interview Concepts Demonstrated

This scenario demonstrates:

- ETL Testing
- Data Quality Engineering
- Source-to-Target Validation
- Data Integrity
- Record Reconciliation
- Automated Validation
- Python Automation

---

# Success Criteria

The ETL process is considered successful when:

- Data is loaded successfully
- Required transformations are applied
- All validations pass
- Validation report is generated

---

# Version

Scenario Version: 1.0

Status:

Approved for implementation planning.