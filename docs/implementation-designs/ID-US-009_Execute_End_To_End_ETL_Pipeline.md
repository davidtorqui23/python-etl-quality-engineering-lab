# ID-US-009

## Story
US-009

Execute End-To-End ETL Pipeline

---

## Feature
Execute End-To-End ETL Pipeline

---

## Goal
Implement one end-to-end ETL pipeline that reads the raw order dataset, validates it, normalizes trusted records, summarizes quality, and loads valid rows into SQLite.

---

# Proposed Modules

src/load/

---

# Proposed Files

src/load/etl_pipeline.py

---

# Proposed Function

execute_etl_pipeline(raw_path, summary_path, db_path)

---

# Responsibilities

## execute_etl_pipeline(raw_path, summary_path, db_path)
- read the raw data source
- validate dataset structure
- validate customer IDs, email, and phone values
- drop invalid rows before transformation
- normalize the valid dataset
- generate a quality summary output
- insert valid rows into SQLite
- log each stage and final ETL summary

---

# Error Handling

ValueError

DataFrame validation errors

---

# Dependencies

Pandas

sqlite3

src.common.logger

src.transform.normalize_customer_data

src.transform.data_quality_summary

src.load.load_valid_orders

src.validation.*

---

# Status
Ready for verification
