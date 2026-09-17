# Python ETL Quality Engineering Lab

## Mission

Build a Quality Engineering portfolio focused on:

- ETL Testing
- Data Validation
- Data Integrity
- Python Automation
- PySpark
- AI-Assisted Engineering

The objective is interview preparation and portfolio development.

---

# Engineering Principles

Prioritize:

1. Simplicity
2. Readability
3. Reproducibility
4. Data Integrity
5. Automated Validation

Avoid premature optimization.

---

# Technology Decisions

Current stack:

- Python
- Pandas
- SQLite
- Pytest

Future stack:

- PySpark
- CI/CD
- Expanded Data Quality Framework

Do not introduce:

- Java
- Scala
- Airflow
- Docker

until explicitly approved.

---

# Data Rules

Use only:

- Synthetic data
- Public datasets

Never use:

- Client data
- Production data
- PII
- Healthcare records
- Financial records

---

# ETL Philosophy

Every ETL flow must contain:

Extract
Transform
Load

No shortcut implementations.

---

# Validation Philosophy

Every ETL scenario must include automated validations.

Minimum validations:

- Record Count Validation
- Null Validation
- Duplicate Validation
- Schema Validation

---

# Quality Dimensions

Always evaluate:

## Completeness

Missing values.

## Uniqueness

Duplicate business keys.

## Consistency

Format standardization.

## Accuracy

Transformation correctness.

## Integrity

Relationship validity.

---

# Python Standards

Use:

- Type hints where helpful
- Small functions
- Clear naming
- Separation of responsibilities

Avoid:

- Global state
- Monolithic scripts
- Hardcoded paths

---

# PySpark Standards

When PySpark is introduced:

- Prefer DataFrame API
- Avoid unnecessary UDFs
- Keep transformations declarative
- Separate transformations from validations

---

# Testing Standards

Use:

- Pytest

Testing layers:

1. Unit Tests
2. Validation Tests
3. ETL Integration Tests

---

# Reporting Standards

Validation results should explain:

- What was tested
- Expected result
- Actual result
- Pass/Fail status

---

# AI Usage

Copilot may:

- Plan architecture
- Suggest validation rules
- Review data quality scenarios
- Generate test cases

Copilot must not:

- Invent production requirements
- Invent business rules
- Assume missing data

---

# Current Version

Version: 0.1

Current Phase:

Architecture and project foundation.