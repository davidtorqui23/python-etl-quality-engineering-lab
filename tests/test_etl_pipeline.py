import json
import sqlite3
from pathlib import Path

from src.common.logger import get_logger
from src.load.etl_pipeline import execute_etl_pipeline


logger = get_logger("execution")

TEST_RESOURCES = Path(__file__).resolve().parent / "resources"
INPUT_DIR = TEST_RESOURCES / "input"
EXPECTED_DIR = TEST_RESOURCES / "expected"


def test_execute_etl_pipeline_end_to_end(tmp_path):
    source_path = tmp_path / "orders_raw.csv"
    database_path = tmp_path / "orders.db"
    summary_path = tmp_path / "quality_summary.json"

    input_csv = INPUT_DIR / "etl_pipeline_input.csv"
    logger.info("INFO Creating input dataset")
    source_path.write_text(input_csv.read_text(encoding="utf-8"), encoding="utf-8")

    logger.info("INFO Executing ETL pipeline")
    result = execute_etl_pipeline(source_path, summary_path, database_path)

    assert result["total_records"] == 4
    assert result["valid_records"] == 3
    assert result["invalid_records"] == 1
    assert result["inserted_records"] == 3
    assert result["rejected_records"] == 0
    assert Path(summary_path).exists()

    logger.info("INFO Validating generated summary")
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    expected_summary = json.loads((EXPECTED_DIR / "etl_pipeline_expected_summary.json").read_text(encoding="utf-8"))
    assert summary["total_records"] == expected_summary["total_records"]
    assert summary["invalid_records"] == expected_summary["invalid_records"]

    logger.info("INFO Validating SQLite records")
    with sqlite3.connect(database_path) as connection:
        rows = connection.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
    assert rows == 3


def test_execute_etl_pipeline_logs_each_stage_and_final_summary(tmp_path):
    source_path = tmp_path / "orders_raw.csv"
    database_path = tmp_path / "orders.db"
    summary_path = tmp_path / "quality_summary.json"

    input_csv = INPUT_DIR / "etl_pipeline_log_input.csv"
    logger.info("INFO Creating input dataset for execution logging validation")
    source_path.write_text(input_csv.read_text(encoding="utf-8"), encoding="utf-8")

    logger.info("INFO Executing ETL pipeline for logging validation")
    execute_etl_pipeline(source_path, summary_path, database_path)

    latest_log = sorted(Path("logs").glob("execution_*.log"))[-1].read_text(encoding="utf-8")
    assert "Starting ETL pipeline execution" in latest_log
    assert "Raw dataset loaded" in latest_log
    assert "Data normalization completed" in latest_log
    assert "ETL pipeline completed with final summary" in latest_log
