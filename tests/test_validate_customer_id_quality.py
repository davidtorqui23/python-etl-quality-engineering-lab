import pandas as pd

from src.common.logger import get_logger
from src.validation.customer_id_validator import CustomerIDValidator, validate_customer_id_quality

logger = get_logger("execution")


VALID_CUSTOMER_IDS = [5001, 5002, 5003]


def build_valid_dataframe():
    return pd.DataFrame(
        {
            "customer_id": VALID_CUSTOMER_IDS,
            "email": ["a@example.com", "b@example.com", "c@example.com"],
        }
    )


def test_valid_customer_ids_pass_validation():
    logger.info("Running the valid customer_id validation test.")
    df = build_valid_dataframe()

    result = CustomerIDValidator.validate_customer_id_quality(df)

    assert result["is_valid"] is True
    assert result["invalid_rows"] == []


def test_non_numeric_customer_ids_fail_validation():
    logger.warning("Running the non-numeric customer_id validation scenario.")
    df = build_valid_dataframe().copy()
    df["customer_id"] = df["customer_id"].astype(object)
    df.loc[1, "customer_id"] = "50A3"

    result = validate_customer_id_quality(df)

    assert result["is_valid"] is False
    assert 1 in result["invalid_rows"]
    assert "non-numeric" in result["message"].lower()


def test_blank_customer_ids_are_rejected():
    logger.warning("Running the blank customer_id validation scenario.")
    df = build_valid_dataframe().copy()
    df["customer_id"] = df["customer_id"].astype(object)
    df.loc[2, "customer_id"] = " "

    result = CustomerIDValidator.validate_customer_id_quality(df)

    assert result["is_valid"] is False
    assert 2 in result["invalid_rows"]
    assert "blank" in result["message"].lower()


def test_missing_customer_id_column_fails_validation():
    logger.warning("Running the missing customer_id column validation scenario.")
    df = pd.DataFrame({"user_id": [5001, 5002]})

    result = CustomerIDValidator.validate_customer_id_quality(df)

    assert result["is_valid"] is False
    assert result["message"] == "Missing required column: customer_id"
