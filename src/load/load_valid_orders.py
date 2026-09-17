from __future__ import annotations

import re
import sqlite3
from pathlib import Path
from typing import Any

import pandas as pd

from src.common.logger import get_logger

logger = get_logger("execution")

EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def _is_valid_email(value: Any) -> bool:
    if pd.isna(value):
        return False
    normalized = str(value).strip()
    return bool(normalized) and bool(EMAIL_PATTERN.fullmatch(normalized))


def _is_valid_phone(value: Any) -> bool:
    if pd.isna(value):
        return False
    normalized = str(value).strip()
    return bool(normalized) and bool(re.fullmatch(r"\d+", normalized))


def _is_valid_customer_id(value: Any) -> bool:
    if pd.isna(value):
        return False
    normalized = str(value).strip()
    return bool(normalized) and normalized.isdigit()


def _is_valid_row(row: pd.Series) -> bool:
    if "customer_id" in row.index and not _is_valid_customer_id(row["customer_id"]):
        return False
    if "email" in row.index and not _is_valid_email(row["email"]):
        return False
    if "phone" in row.index and not _is_valid_phone(row["phone"]):
        return False
    return True


def load_valid_orders(dataframe: pd.DataFrame, db_path: str | Path = "data/output/orders.db") -> dict[str, Any]:
    """Load only valid records into the SQLite orders table and return row-level statistics."""
    logger.info("Starting SQLite load execution.")
    if dataframe is None:
        raise ValueError("Input dataframe cannot be None.")

    db_location = Path(db_path)
    db_location.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(db_location))
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER,
                customer_id INTEGER,
                full_name TEXT,
                email TEXT,
                phone TEXT,
                order_date TEXT,
                country TEXT,
                amount REAL,
                status TEXT,
                product_code TEXT
            )
            """
        )
        conn.execute("DELETE FROM orders")

        valid_rows = dataframe[dataframe.apply(_is_valid_row, axis=1)].copy()
        inserted_count = 0
        if not valid_rows.empty:
            valid_rows.to_sql("orders", conn, if_exists="append", index=False)
            inserted_count = int(len(valid_rows))

        rejected_count = int(len(dataframe) - inserted_count)
        stats = {
            "database_path": str(db_location),
            "total_records": int(len(dataframe)),
            "inserted_records": inserted_count,
            "rejected_records": rejected_count,
        }

        logger.info("SQLite load completed. Inserted records: %s; rejected records: %s", inserted_count, rejected_count)
        return stats
    finally:
        conn.close()


def main() -> dict[str, Any]:
    """Load the normalized orders dataset into SQLite for downstream analytics."""
    source_path = Path("data/processed/orders_normalized.csv")
    if not source_path.exists():
        source_path = Path("data/raw/orders_raw.csv")

    dataframe = pd.read_csv(source_path)
    return load_valid_orders(dataframe, "data/output/orders.db")


if __name__ == "__main__":
    main()
