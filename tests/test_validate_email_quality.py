import pandas as pd

from src.common.logger import get_logger
from src.validation.email_validator import EmailValidator, validate_email_quality

logger = get_logger("execution")


VALID_EMAILS = [
    "user1@example.com",
    "user2@example.org",
    "user3@sub.example.net",
]


def build_valid_dataframe():
    return pd.DataFrame(
        {
            "email": VALID_EMAILS,
            "customer_id": [1001, 1002, 1003],
        }
    )


def test_valid_emails_pass_validation():
    logger.info("Running the valid email validation test.")
    df = build_valid_dataframe()

    result = EmailValidator.validate_email_quality(df)

    assert result["is_valid"] is True
    assert result["invalid_rows"] == []


def test_malformed_emails_fail_validation():
    logger.warning("Running the malformed email validation scenario.")
    df = build_valid_dataframe().copy()
    df["email"] = df["email"].astype(object)
    df.loc[1, "email"] = "not-an-email"

    result = validate_email_quality(df)

    assert result["is_valid"] is False
    assert 1 in result["invalid_rows"]
    assert "invalid" in result["message"].lower()


def test_blank_emails_are_rejected():
    logger.warning("Running the blank email validation scenario.")
    df = build_valid_dataframe().copy()
    df["email"] = df["email"].astype(object)
    df.loc[2, "email"] = " "

    result = EmailValidator.validate_email_quality(df)

    assert result["is_valid"] is False
    assert 2 in result["invalid_rows"]
    assert "blank" in result["message"].lower()


def test_missing_email_column_fails_validation():
    logger.warning("Running the missing email column validation scenario.")
    df = pd.DataFrame({"user_email": ["a@example.com", "b@example.com"]})

    result = EmailValidator.validate_email_quality(df)

    assert result["is_valid"] is False
    assert result["message"] == "Missing required column: email"
