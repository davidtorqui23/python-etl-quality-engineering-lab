import sqlite3
from pathlib import Path

import pandas as pd

from src.common.logger import get_logger
from src.load.load_valid_orders import load_valid_orders

logger = get_logger("execution")

TEST_RESOURCES = Path(__file__).resolve().parent / "resources"
INPUT_DIR = TEST_RESOURCES / "input"
EXPECTED_DIR = TEST_RESOURCES / "expected"


def test_load_valid_orders_inserts_only_valid_records(tmp_path):
    logger.info("Starting SQLite load validation test.")
    database_path = tmp_path / "orders.db"
    dataframe = pd.read_csv(INPUT_DIR / "sqlite_load_input.csv")

    stats = load_valid_orders(dataframe, database_path)

    assert stats["total_records"] == 3
    assert stats["inserted_records"] == 2
    assert stats["rejected_records"] == 1

    connection = sqlite3.connect(database_path)
    try:
        stored = pd.read_sql_query("SELECT * FROM orders", connection)
    finally:
        connection.close()

    expected = pd.read_csv(EXPECTED_DIR / "sqlite_load_expected.csv")
    assert len(stored) == len(expected)
    assert stored["customer_id"].tolist() == expected["customer_id"].tolist()
    logger.info("SQLite load validation test completed successfully.")


def test_load_valid_orders_logs_execution_and_row_counts(tmp_path):
    logger.info("Checking SQLite logging and count metadata.")
    database_path = tmp_path / "orders_log_check.db"
    dataframe = pd.read_csv(INPUT_DIR / "sqlite_logging_input.csv")

    stats = load_valid_orders(dataframe, database_path)
    assert stats["inserted_records"] == 2
    assert stats["rejected_records"] == 0

    log_files = sorted(Path("logs").glob("execution_*.log"))
    assert log_files
    latest_log = log_files[-1].read_text(encoding="utf-8")
    assert "Starting SQLite load execution" in latest_log
    assert "SQLite load completed" in latest_log
    logger.info("SQLite logging and count checks completed successfully.")
