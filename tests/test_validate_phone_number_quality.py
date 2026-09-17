import pandas as pd

from src.common.logger import get_logger
from src.validation.phone_validator import PhoneValidator, validate_phone_quality

logger = get_logger("execution")


VALID_PHONES = [
    "3001000001",
    "3001000002",
    "3001000003",
]


def build_valid_dataframe():
    return pd.DataFrame(
        {
            "phone": VALID_PHONES,
            "customer_id": [1001, 1002, 1003],
        }
    )


def test_valid_phone_numbers_pass_validation():
    logger.info("Running the valid phone validation test.")
    df = build_valid_dataframe()

    result = PhoneValidator.validate_phone_quality(df)

    assert result["is_valid"] is True
    assert result["invalid_rows"] == []


def test_malformed_phone_numbers_fail_validation():
    logger.warning("Running the malformed phone validation scenario.")
    df = build_valid_dataframe().copy()
    df["phone"] = df["phone"].astype(object)
    df.loc[1, "phone"] = "300-100-0002"

    result = validate_phone_quality(df)

    assert result["is_valid"] is False
    assert 1 in result["invalid_rows"]
    assert "invalid" in result["message"].lower()


def test_blank_phone_numbers_are_rejected():
    logger.warning("Running the blank phone validation scenario.")
    df = build_valid_dataframe().copy()
    df["phone"] = df["phone"].astype(object)
    df.loc[2, "phone"] = " "

    result = PhoneValidator.validate_phone_quality(df)

    assert result["is_valid"] is False
    assert 2 in result["invalid_rows"]
    assert "blank" in result["message"].lower()


def test_missing_phone_column_fails_validation():
    logger.warning("Running the missing phone column validation scenario.")
    df = pd.DataFrame({"phone_number": ["3001000001", "3001000002"]})

    result = PhoneValidator.validate_phone_quality(df)

    assert result["is_valid"] is False
    assert result["message"] == "Missing required column: phone"
