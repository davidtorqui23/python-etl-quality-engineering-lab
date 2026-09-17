from __future__ import annotations

import re
from typing import Any

import pandas as pd

from src.common.logger import get_logger, log_section

logger = get_logger("validation")


class PhoneValidator:
    """Validate phone number quality for the US-005 data quality rule."""

    REQUIRED_COLUMN = "phone"
    PHONE_PATTERN = re.compile(r"^\d{10,15}$")

    @classmethod
    def validate_phone_column(cls, dataframe: pd.DataFrame) -> None:
        """Raise a validation error when the phone column is missing."""
        logger.info("Checking phone column presence.")
        if dataframe is None or cls.REQUIRED_COLUMN not in dataframe.columns:
            logger.warning("Missing required column: %s", cls.REQUIRED_COLUMN)
            raise ValueError(f"Missing required column: {cls.REQUIRED_COLUMN}")

    @classmethod
    def identify_invalid_rows(cls, dataframe: pd.DataFrame) -> dict[int, str]:
        """Return invalid phone rows and the reason for each invalid row."""
        invalid_rows: dict[int, str] = {}

        for idx, value in dataframe[cls.REQUIRED_COLUMN].items():
            if pd.isna(value):
                invalid_rows[idx] = "blank"
                continue

            normalized = str(value).strip()
            if normalized == "":
                invalid_rows[idx] = "blank"
                continue

            if not cls.PHONE_PATTERN.fullmatch(normalized):
                invalid_rows[idx] = "invalid"

        if invalid_rows:
            logger.warning("Phone validation found invalid rows: %s", invalid_rows)
        return invalid_rows

    @classmethod
    def validate_phone_quality(cls, dataframe: pd.DataFrame) -> dict[str, Any]:
        """Return a structured validation result for phone number quality."""
        log_section(logger, "PHONE VALIDATION")
        logger.info("Validating phone number quality.")
        result: dict[str, Any] = {
            "is_valid": True,
            "invalid_rows": [],
            "message": "Phone number quality is valid.",
        }

        try:
            cls.validate_phone_column(dataframe)
        except ValueError as exc:
            result["is_valid"] = False
            result["message"] = str(exc)
            logger.warning("Phone validation failed: %s", result["message"])
            return result

        invalid_rows = cls.identify_invalid_rows(dataframe)
        result["invalid_rows"] = sorted(invalid_rows)

        if invalid_rows:
            result["is_valid"] = False

            reasons = sorted(set(invalid_rows.values()))
            if "blank" in reasons and "invalid" in reasons:
                result["message"] = "Phone values contain blank and invalid entries."
            elif "blank" in reasons:
                result["message"] = "Phone values contain blank entries."
            else:
                result["message"] = "Phone values contain invalid format entries."
            logger.warning("Phone validation failed: %s", result["message"])
        else:
            logger.info("Phone number quality validation passed.")

        return result


def validate_phone_quality(dataframe: pd.DataFrame) -> dict[str, Any]:
    """Project-level entry point for phone validation."""
    return PhoneValidator.validate_phone_quality(dataframe)


__all__ = ["PhoneValidator", "validate_phone_quality"]
