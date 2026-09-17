import json
from pathlib import Path

import pandas as pd

from src.common.logger import get_logger
from src.transform.data_quality_summary import generate_data_quality_summary

logger = get_logger("execution")

TEST_RESOURCES = Path(__file__).resolve().parent / "resources"
INPUT_DIR = TEST_RESOURCES / "input"
EXPECTED_DIR = TEST_RESOURCES / "expected"


def test_generate_data_quality_summary_counts_invalid_records():
    logger.info("INFO Creating source dataset for data quality summary validation.")
    dataframe = pd.read_csv(INPUT_DIR / "data_quality_summary_input.csv")

    logger.info("INFO Generating data quality summary.")
    summary = generate_data_quality_summary(dataframe)
    expected_summary = json.loads((EXPECTED_DIR / "data_quality_summary_expected.json").read_text(encoding="utf-8"))

    logger.info("INFO Validating generated summary counts.")
    assert summary["total_records"] == expected_summary["total_records"]
    assert summary["valid_records"] == expected_summary["valid_records"]
    assert summary["invalid_records"] == expected_summary["invalid_records"]
    assert summary["invalid_emails"] == expected_summary["invalid_emails"]
    assert summary["invalid_phone_numbers"] == expected_summary["invalid_phone_numbers"]
    assert summary["invalid_customer_ids"] == expected_summary["invalid_customer_ids"]


def test_generate_data_quality_summary_writes_json_report(tmp_path):
    logger.info("INFO Creating source dataset for JSON summary output validation.")
    dataframe = pd.read_csv(INPUT_DIR / "data_quality_summary_input.csv")
    output_path = tmp_path / "data_quality_summary.json"

    logger.info("INFO Generating summary JSON report.")
    summary = generate_data_quality_summary(dataframe)
    output_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    logger.info("INFO Validating saved summary output file.")
    assert output_path.exists()
    saved_summary = json.loads(output_path.read_text(encoding="utf-8"))
    expected_summary = json.loads((EXPECTED_DIR / "data_quality_summary_expected.json").read_text(encoding="utf-8"))
    assert saved_summary["total_records"] == expected_summary["total_records"]
    assert saved_summary["invalid_records"] == expected_summary["invalid_records"]
    assert saved_summary["invalid_emails"] == expected_summary["invalid_emails"]
    assert saved_summary["invalid_customer_ids"] == expected_summary["invalid_customer_ids"]
