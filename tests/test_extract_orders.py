from pathlib import Path

import pandas as pd
import pytest

from src.common.logger import get_logger
from src.extract.extract_orders import extract_orders

logger = get_logger("execution")


EXPECTED_COLUMNS = [
    "order_id",
    "customer_id",
    "full_name",
    "email",
    "phone",
    "order_date",
    "country",
    "amount",
    "status",
    "product_code",
]


def test_dataset_can_be_loaded():
    logger.info("Running dataset load validation test.")
    df = extract_orders("data/raw/orders_raw.csv")

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_dataframe_is_returned():
    logger.info("Checking the extracted object type and row count.")
    df = extract_orders("data/raw/orders_raw.csv")

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 50


def test_dataset_row_count_matches_expected():
    logger.info("Checking the expected row count for the raw dataset.")
    df = extract_orders("data/raw/orders_raw.csv")

    assert len(df) == 50


def test_structure_is_preserved():
    logger.info("Checking that the extraction preserves the expected columns.")
    df = extract_orders("data/raw/orders_raw.csv")

    assert list(df.columns) == EXPECTED_COLUMNS
    assert set(EXPECTED_COLUMNS).issubset(df.columns)


def test_file_existence_is_verified():
    logger.warning("Running the missing file validation scenario.")
    missing_path = Path("data/raw/does_not_exist.csv")

    with pytest.raises(FileNotFoundError):
        extract_orders(missing_path)

