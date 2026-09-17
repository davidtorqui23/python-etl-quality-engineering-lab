import pandas as pd

from src.common.logger import get_logger
from src.validation.dataset_structure_validator import DatasetStructureValidator, validate_dataset_structure

logger = get_logger("execution")


VALID_COLUMNS = [
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


def build_valid_dataframe():
    return pd.DataFrame(
        [
            {
                "order_id": 1,
                "customer_id": 101,
                "full_name": "Jane Doe",
                "email": "jane@example.com",
                "phone": "555-0100",
                "order_date": "2024-01-01",
                "country": "US",
                "amount": 42.50,
                "status": "pending",
                "product_code": "ABC-100",
            }
        ]
    )


def test_valid_dataset_structure_passes():
    logger.info("Running the valid dataset structure test.")
    df = build_valid_dataframe()

    result = DatasetStructureValidator.validate_structure(df)

    assert result["is_valid"] is True
    assert result["missing_columns"] == []
    assert result["extra_columns"] == []


def test_missing_columns_are_reported():
    logger.warning("Running the missing columns validation scenario.")
    df = build_valid_dataframe().drop(columns=["email", "phone"])

    result = validate_dataset_structure(df)

    assert result["is_valid"] is False
    assert "email" in result["missing_columns"]
    assert "phone" in result["missing_columns"]


def test_extra_columns_are_flagged():
    logger.warning("Running the unexpected column validation scenario.")
    df = build_valid_dataframe()
    df["unexpected_column"] = ["value"]

    result = DatasetStructureValidator.validate_structure(df)

    assert result["is_valid"] is False
    assert "unexpected_column" in result["extra_columns"]


def test_empty_dataset_is_rejected():
    logger.warning("Running the empty dataset validation scenario.")
    df = pd.DataFrame(columns=VALID_COLUMNS)

    result = DatasetStructureValidator.validate_structure(df)

    assert result["is_valid"] is False
    assert result["message"] == "Dataset is empty."
