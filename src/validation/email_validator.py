from __future__ import annotations

import re
from typing import Any

import pandas as pd

from src.common.logger import get_logger, log_section

logger = get_logger("validation")


class EmailValidator:
    """Validate email addresses for the US-004 data quality rule."""

    REQUIRED_COLUMN = "email"
    EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    @classmethod
    def validate_email_column(cls, dataframe: pd.DataFrame) -> None:
        """Raise a validation error when the email column is missing."""
        logger.info("Checking email column presence.")
        if dataframe is None or cls.REQUIRED_COLUMN not in dataframe.columns:
            logger.warning("Missing required column: %s", cls.REQUIRED_COLUMN)
            raise ValueError(f"Missing required column: {cls.REQUIRED_COLUMN}")

    @classmethod
    def identify_invalid_rows(cls, dataframe: pd.DataFrame) -> dict[int, str]:
        """Return invalid email rows and the reason for each invalid row."""
        invalid_rows: dict[int, str] = {}

        for idx, value in dataframe[cls.REQUIRED_COLUMN].items():
            if pd.isna(value):
                invalid_rows[idx] = "blank"
                continue

            normalized = str(value).strip()
            if normalized == "":
                invalid_rows[idx] = "blank"
                continue

            if not cls.EMAIL_PATTERN.fullmatch(normalized):
                invalid_rows[idx] = "invalid"

        if invalid_rows:
            logger.warning("Email validation found invalid rows: %s", invalid_rows)
        return invalid_rows

    @classmethod
    def validate_email_quality(cls, dataframe: pd.DataFrame) -> dict[str, Any]:
        """Return a structured validation result for email quality."""
        log_section(logger, "EMAIL VALIDATION")
        logger.info("Validating email quality.")
        result: dict[str, Any] = {
            "is_valid": True,
            "invalid_rows": [],
            "message": "Email quality is valid.",
        }

        try:
            cls.validate_email_column(dataframe)
        except ValueError as exc:
            result["is_valid"] = False
            result["message"] = str(exc)
            logger.warning("Email validation failed: %s", result["message"])
            return result

        invalid_rows = cls.identify_invalid_rows(dataframe)
        result["invalid_rows"] = sorted(invalid_rows)

        if invalid_rows:
            result["is_valid"] = False

            reasons = sorted(set(invalid_rows.values()))
            if "blank" in reasons and "invalid" in reasons:
                result["message"] = "Email values contain blank and invalid entries."
            elif "blank" in reasons:
                result["message"] = "Email values contain blank entries."
            else:
                result["message"] = "Email values contain invalid format entries."
            logger.warning("Email validation failed: %s", result["message"])
        else:
            logger.info("Email quality validation passed.")

        return result


def validate_email_quality(dataframe: pd.DataFrame) -> dict[str, Any]:
    """Project-level entry point for email validation."""
    return EmailValidator.validate_email_quality(dataframe)


__all__ = ["EmailValidator", "validate_email_quality"]
