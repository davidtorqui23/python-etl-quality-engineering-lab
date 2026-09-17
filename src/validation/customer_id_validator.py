from __future__ import annotations

from typing import Any

import pandas as pd

from src.common.logger import get_logger, log_section

logger = get_logger("validation")


class CustomerIDValidator:
    """Validate customer_id quality for the US-003 required data quality rule."""

    REQUIRED_COLUMN = "customer_id"

    @classmethod
    def validate_customer_id_column(cls, dataframe: pd.DataFrame) -> None:
        """Raise a validation error when the customer ID column is missing."""
        logger.info("Checking customer_id column presence.")
        if dataframe is None or cls.REQUIRED_COLUMN not in dataframe.columns:
            logger.warning("Missing required column: %s", cls.REQUIRED_COLUMN)
            raise ValueError(f"Missing required column: {cls.REQUIRED_COLUMN}")

    @classmethod
    def identify_invalid_rows(cls, dataframe: pd.DataFrame) -> dict[int, str]:
        """Return row numbers and reason codes for invalid customer IDs."""
        invalid_rows: dict[int, str] = {}

        for idx, value in dataframe[cls.REQUIRED_COLUMN].items():
            if pd.isna(value):
                invalid_rows[idx] = "blank"
                continue

            normalized = str(value).strip()
            if normalized == "":
                invalid_rows[idx] = "blank"
                continue

            if not normalized.isdigit():
                invalid_rows[idx] = "non-numeric"

        if invalid_rows:
            logger.warning("Customer_id validation found invalid rows: %s", invalid_rows)
        return invalid_rows

    @classmethod
    def validate_customer_id_quality(cls, dataframe: pd.DataFrame) -> dict[str, Any]:
        """Return a structured validation result for customer ID quality."""
        log_section(logger, "CUSTOMER ID VALIDATION")
        logger.info("Validating customer_id quality.")
        result: dict[str, Any] = {
            "is_valid": True,
            "invalid_rows": [],
            "message": "Customer ID quality is valid.",
        }

        try:
            cls.validate_customer_id_column(dataframe)
        except ValueError as exc:
            result["is_valid"] = False
            result["message"] = str(exc)
            logger.warning("Customer_id validation failed: %s", result["message"])
            return result

        invalid_rows = cls.identify_invalid_rows(dataframe)
        result["invalid_rows"] = sorted(invalid_rows)

        if invalid_rows:
            result["is_valid"] = False

            reasons = sorted(set(invalid_rows.values()))
            if "blank" in reasons and "non-numeric" in reasons:
                result["message"] = "Customer IDs contain blank and non-numeric values."
            elif "blank" in reasons:
                result["message"] = "Customer IDs contain blank values."
            else:
                result["message"] = "Customer IDs contain non-numeric values."
            logger.warning("Customer_id validation failed: %s", result["message"])
        else:
            logger.info("Customer_id quality validation passed.")

        return result


def validate_customer_id_quality(dataframe: pd.DataFrame) -> dict[str, Any]:
    """Project-level entry point for customer ID validation."""
    return CustomerIDValidator.validate_customer_id_quality(dataframe)


__all__ = ["CustomerIDValidator", "validate_customer_id_quality"]
