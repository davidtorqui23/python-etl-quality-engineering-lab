# Python ETL Quality Engineering Lab

A practical Quality Engineering portfolio focused on:

- ETL Testing
- Data Quality Validation
- Data Integrity
- Python Automation
- PySpark
- SQLite
- AI-Assisted Engineering

---

## Project Goal

Simulate real-world ETL testing scenarios using synthetic datasets and automated validation strategies.

The project is designed to demonstrate ETL Quality Engineering practices and prepare for enterprise-scale data quality environments.

---

## Current Architecture

```text
CSV
 ↓
Extract
 ↓
Transform
 ↓
Load SQLite
 ↓
Validation
 ↓
Report
```

---

## Technology Stack

### Version 1.0

- Python
- Pandas
- SQLite
- Pytest

### Future Versions

- PySpark
- GitHub Actions
- Data Quality Framework
- Automated Reporting

---

## Current Scenario

Orders Pipeline Validation

Dataset contains intentionally injected quality issues:

- Duplicate IDs
- Invalid emails
- Invalid phone numbers
- Missing values
- Invalid dates
- Country normalization issues
- Invalid amounts

Used to simulate real ETL validation scenarios.

---

## Project Structure

```text
data/
database/
docs/
reports/
src/
tests/
```

---

## Quality Dimensions

- Completeness
- Uniqueness
- Consistency
- Accuracy
- Integrity

---

## AI-Assisted Development

This project uses specialized AI agents to support story-driven ETL development, test automation, code review and data quality validation.

Before using an agent, review the execution guide:

HOW_EXECUTE.md

The guide explains:

- Which agent to select
- When to create a complete User Story
- How to add a test case to existing functionality
- How to fix a defect
- How to perform a technical refactor
- How to review test logging
- How to audit the repository
- How to execute tests and generate reports

### Quick Agent Selection

| Work Type | Agent |
|---|---|
| New business functionality | Delivery Manager |
| Additional test case | Test Automation Engineer |
| Bug fix | Delivery Manager |
| Technical refactor | Delivery Manager |
| Test logging improvement | Test Automation Engineer |
| Repository audit | Delivery Manager |

> Use `HOW_EXECUTE.md` as the source of truth for prompts and execution workflows.

