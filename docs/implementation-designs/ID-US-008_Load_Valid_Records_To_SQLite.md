# ID-US-008

## Story
US-008

Load Valid Records To SQLite

---

## Feature
Load Valid Records To SQLite

---

## Goal
Load only trusted business records into a SQLite table and return load statistics for downstream reporting and analytics consumption.

---

# Proposed Modules

src/load/

---

# Proposed Files

src/load/load_valid_orders.py

---

# Proposed Function

load_valid_orders(dataframe, db_path)

---

# Responsibilities

## load_valid_orders(dataframe, db_path)
- Create the target SQLite database directory if needed
- Create the orders table if it does not exist
- Filter invalid rows based on customer_id, email, and phone rules
- Insert the valid rows into SQLite
- Return load statistics including inserted and rejected counts
- Log execution in English using the shared logger

---

# Error Handling

ValueError

sqlite3 database errors

---

# Dependencies

Pandas

sqlite3

re

src.common.logger

---

# Status
Ready for verification
