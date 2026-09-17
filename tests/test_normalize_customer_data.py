from pathlib import Path

import pandas as pd

from src.common.logger import get_logger
from src.transform.normalize_customer_data import normalize_customer_data

logger = get_logger("execution")

TEST_RESOURCES = Path(__file__).resolve().parent / "resources"
INPUT_DIR = TEST_RESOURCES / "input"
EXPECTED_DIR = TEST_RESOURCES / "expected"


def test_normalize_customer_data_standardizes_records():
    logger.info("Starting the customer normalization validation test.")
    dataframe = pd.read_csv(INPUT_DIR / "normalize_customer_input.csv")

    normalized = normalize_customer_data(dataframe)
    expected = pd.read_csv(EXPECTED_DIR / "normalize_customer_expected.csv")

    assert normalized["full_name"].astype(str).tolist() == expected["full_name"].astype(str).tolist()
    assert normalized["email"].astype(str).tolist() == expected["email"].astype(str).tolist()
    assert normalized["phone"].astype(str).tolist() == expected["phone"].astype(str).tolist()
    assert normalized["country"].astype(str).tolist() == expected["country"].astype(str).tolist()
    logger.info("Customer normalization validation completed successfully.")


def test_normalize_customer_data_writes_output_file(tmp_path):
    logger.info("Checking that the normalized dataset is saved to disk.")
    input_data = pd.read_csv(INPUT_DIR / "normalize_customer_input.csv")
    output_path = tmp_path / "orders_normalized.csv"

    normalized = normalize_customer_data(input_data)
    normalized.to_csv(output_path, index=False)

    assert output_path.exists()
    saved = pd.read_csv(output_path)
    expected = pd.read_csv(EXPECTED_DIR / "normalize_customer_expected.csv")
    assert saved["email"].astype(str).tolist() == expected["email"].astype(str).tolist()
    assert saved["country"].astype(str).tolist() == expected["country"].astype(str).tolist()
    logger.info("Normalized output file validation completed successfully.")
