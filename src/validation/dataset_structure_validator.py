from __future__ import annotations

from typing import Any

import pandas as pd

from src.common.logger import get_logger

logger = get_logger("validation")


class DatasetStructureValidator:
    """Validate that a dataset matches the approved schema."""

    REQUIRED_COLUMNS = [
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

    @classmethod
    def validate_not_empty(cls, dataframe: pd.DataFrame) -> bool:
        """Return True when the dataset contains at least one row."""
        is_not_empty = dataframe is not None and not dataframe.empty
        logger.info("Checking whether the dataset is empty.")
        if not is_not_empty:
            logger.warning("Dataset is empty.")
        return is_not_empty

    @classmethod
    def validate_required_columns(cls, dataframe: pd.DataFrame) -> list[str]:
        """Return the subset of required columns that is currently missing."""
        if dataframe is None:
            logger.warning("Dataset reference is None when checking required columns.")
            return list(cls.REQUIRED_COLUMNS)

        missing_columns = [
            column for column in cls.REQUIRED_COLUMNS if column not in dataframe.columns
        ]
        if missing_columns:
            logger.warning("Missing required columns: %s", ", ".join(missing_columns))
        return missing_columns

    @classmethod
    def identify_extra_columns(cls, dataframe: pd.DataFrame) -> list[str]:
        """Return columns that are present but not part of the approved schema."""
        if dataframe is None:
            logger.warning("Dataset reference is None when checking extra columns.")
            return []

        extra_columns = sorted(set(dataframe.columns) - set(cls.REQUIRED_COLUMNS))
        if extra_columns:
            logger.warning("Unexpected columns detected: %s", ", ".join(extra_columns))
        return extra_columns

    @classmethod
    def validate_structure(cls, dataframe: pd.DataFrame) -> dict[str, Any]:
        """Return a structured validation result for the dataset schema."""
        logger.info("Validating dataset structure.")
        result: dict[str, Any] = {
            "is_valid": True,
            "missing_columns": [],
            "extra_columns": [],
            "message": "Dataset structure is valid.",
        }

        if dataframe is None or dataframe.empty:
            result["is_valid"] = False
            result["message"] = "Dataset is empty."
            logger.warning("Dataset structure validation failed: dataset is empty.")
            return result

        result["missing_columns"] = cls.validate_required_columns(dataframe)
        result["extra_columns"] = cls.identify_extra_columns(dataframe)

        if result["missing_columns"] or result["extra_columns"]:
            result["is_valid"] = False

            issues = []
            if result["missing_columns"]:
                issues.append(
                    "Missing required columns: " + ", ".join(result["missing_columns"])
                )
            if result["extra_columns"]:
                issues.append(
                    "Unexpected columns: " + ", ".join(result["extra_columns"])
                )
            result["message"] = "; ".join(issues)
            logger.warning("Dataset structure validation failed: %s", result["message"])
        else:
            logger.info("Dataset structure validation passed.")

        return result


def validate_dataset_structure(dataframe: pd.DataFrame) -> dict[str, Any]:
    """Project-level routine for validating dataset structure."""
    return DatasetStructureValidator.validate_structure(dataframe)


__all__ = ["DatasetStructureValidator", "validate_dataset_structure"]
