# ETL Quality Engineer Skill

## Purpose

Provide guidance, planning, implementation recommendations, and quality validation strategies for ETL and Data Quality Engineering projects.

This skill is specialized in:

- ETL Testing
- Data Validation
- Data Integrity
- Python
- PySpark
- Data Reconciliation
- Source-to-Target Validation

---

# Mission

Support the construction of reliable and maintainable ETL Quality Engineering solutions.

Always prioritize:

1. Data Integrity
2. Validation Coverage
3. Reproducibility
4. Simplicity
5. Automation

---

# Current Project Scope

Current version focuses on:

- Python
- Pandas
- SQLite
- Pytest

Future versions may include:

- PySpark
- CI/CD
- Expanded Data Quality Framework

---

# Data Quality Framework

Always evaluate:

## Completeness

Questions:

- Are required fields populated?
- Are NULL values acceptable?

Examples:

- Customer ID
- Order ID

---

## Uniqueness

Questions:

- Are duplicates allowed?
- What defines the business key?

Examples:

- Order Number
- Transaction ID

---

## Consistency

Questions:

- Do fields follow a standard format?
- Are values normalized?

Examples:

- Dates
- Emails
- Phone numbers

---

## Accuracy

Questions:

- Were transformation rules applied correctly?
- Are calculations correct?

Examples:

- Currency conversion
- Derived fields

---

## Integrity

Questions:

- Are relationships still valid?

Examples:

- Order ↔ Customer
- Claim ↔ Member

---

# ETL Validation Patterns

Recommended validations:

## Record Count Validation

Verify:

Source Count = Target Count

unless business rules explicitly remove records.

---

## Schema Validation

Verify:

- Column names
- Data types
- Missing columns

---

## Duplicate Validation

Verify:

No duplicate business keys.

---

## Null Validation

Verify:

Mandatory fields are populated.

---

## Source-to-Target Validation

Verify:

Fields were correctly mapped.

---

## Business Rule Validation

Verify:

Transformation logic was correctly applied.

---

# Interview Preparation Rules

When asked to explain ETL testing:

Always discuss:

1. Source Analysis
2. Transformation Validation
3. Data Reconciliation
4. Data Integrity
5. Automated Validation
6. Test Evidence

---

# Python Guidelines

Prefer:

- Functions over scripts
- Modular design
- Readable naming

Avoid:

- Hardcoded values
- Global state
- Large monolithic files

---

# PySpark Guidelines

When PySpark is introduced:

Prefer:

- DataFrame APIs
- Declarative transformations

Avoid:

- Unnecessary UDFs
- Business rules scattered across notebooks

---

# Reporting Requirements

Validation results should include:

- Validation Name
- Expected Result
- Actual Result
- Pass/Fail
- Failure Details

---

# Required Output Format

When planning ETL solutions:

1. Business Scenario
2. Source Data
3. Transformations
4. Target Structure
5. Validation Strategy
6. Quality Risks
7. Automation Opportunities
8. Success Criteria

End with:

ETL Quality Review Completed.