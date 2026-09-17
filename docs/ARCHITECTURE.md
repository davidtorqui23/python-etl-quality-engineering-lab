# Architecture

## Objective

Simulate realistic ETL and Data Quality validation scenarios using Python and PySpark.

The architecture must remain simple, modular, and interview-friendly.

---

# High-Level Flow

Source Data
    ↓
Extract Layer
    ↓
Transform Layer
    ↓
Load Layer
    ↓
Validation Layer
    ↓
Reporting Layer

---

# Extract Layer

Responsibilities:

- Read source files.
- Validate source availability.
- Validate schema existence.
- Capture extraction metadata.

Examples:

- CSV
- JSON
- Parquet

Output:

Raw dataset loaded into memory.

---

# Transform Layer

Responsibilities:

- Standardize formats.
- Remove duplicates.
- Normalize values.
- Apply business rules.
- Create derived fields.

Examples:

- Email standardization
- Date transformation
- Currency formatting
- Data cleansing

Output:

Clean dataset ready for loading.

---

# Load Layer

Responsibilities:

- Persist processed data.
- Validate load completion.
- Handle loading failures.

Initial target:

- SQLite

Future targets:

- PostgreSQL
- Snowflake
- Data Warehouse platforms

Output:

Loaded dataset.

---

# Validation Layer

Responsibilities:

- Verify source-to-target integrity.
- Execute automated quality checks.
- Generate validation results.

Quality dimensions:

## Completeness

Verify:

- No required values are missing.

Examples:

- Customer ID
- Order ID

## Uniqueness

Verify:

- No duplicate business keys.

Examples:

- Order ID
- Claim ID

## Consistency

Verify:

- Data formats are standardized.

Examples:

- Dates
- Emails

## Accuracy

Verify:

- Transformation rules were correctly applied.

Examples:

- Currency conversion
- Derived values

## Integrity

Verify:

- Relationships remain valid.

Examples:

- Customer and Order relationships

---

# Reporting Layer

Responsibilities:

- Generate validation summaries.
- Capture failures.
- Produce execution evidence.

Outputs:

- Console report
- Validation report
- Test evidence

---

# Initial Technology Stack

Version 1.0

- Python
- Pandas
- SQLite
- Pytest

Version 2.0

- PySpark

Version 3.0

- CI/CD
- Expanded validation framework

---

# Planned Repository Structure

python-etl-quality-engineering-lab/

data/
    raw/
    processed/

database/

src/
    extract/
    transform/
    load/
    validation/
    reporting/

tests/

reports/

docs/

.github/

---

# Quality Engineering Principles

- Reproducible validations
- Synthetic data only
- Data integrity first
- Small vertical slices
- Automated evidence
- Incremental architecture
- AI-assisted engineering

---

# Current Version

Architecture Version: 0.1

Status:

Approved for project initialization.