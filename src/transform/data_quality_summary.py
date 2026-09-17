from __future__ import annotations

import re
from typing import Any

import pandas as pd

from src.common.logger import get_logger

logger = get_logger("validation")

EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def _is_valid_email(value: Any) -> bool:
    if pd.isna(value):
        return False
    normalized = str(value).strip()
    return bool(normalized) and bool(EMAIL_PATTERN.fullmatch(normalized))


def _is_valid_phone(value: Any) -> bool:
    if pd.isna(value):
        return False
    normalized = str(value).strip()
    return bool(normalized) and bool(re.fullmatch(r"\d+", normalized))


def _is_valid_customer_id(value: Any) -> bool:
    if pd.isna(value):
        return False
    normalized = str(value).strip()
    return bool(normalized) and normalized.isdigit()


def _is_valid_row(row: pd.Series) -> bool:
    email_ok = True
    phone_ok = True
    customer_id_ok = True

    if "email" in row.index:
        email_ok = _is_valid_email(row["email"])
    if "phone" in row.index:
        phone_ok = _is_valid_phone(row["phone"])
    if "customer_id" in row.index:
        customer_id_ok = _is_valid_customer_id(row["customer_id"])

    return email_ok and phone_ok and customer_id_ok


def generate_data_quality_summary(dataframe: pd.DataFrame) -> dict[str, Any]:
    """Generate a summary of the dataset quality for downstream review and load decisions."""
    logger.info("Starting data quality summary generation.")
    if dataframe is None:
        raise ValueError("Input dataframe cannot be None.")

    total_records = int(len(dataframe))

    invalid_emails = 0
    if "email" in dataframe.columns:
        invalid_emails = int(dataframe["email"].map(lambda value: not _is_valid_email(value)).sum())

    invalid_phone_numbers = 0
    if "phone" in dataframe.columns:
        invalid_phone_numbers = int(dataframe["phone"].map(lambda value: not _is_valid_phone(value)).sum())

    invalid_customer_ids = 0
    if "customer_id" in dataframe.columns:
        invalid_customer_ids = int(dataframe["customer_id"].map(lambda value: not _is_valid_customer_id(value)).sum())

    valid_records = int(dataframe.apply(_is_valid_row, axis=1).sum())
    invalid_records = total_records - valid_records

    summary = {
        "total_records": total_records,
        "valid_records": valid_records,
        "invalid_records": invalid_records,
        "invalid_emails": invalid_emails,
        "invalid_phone_numbers": invalid_phone_numbers,
        "invalid_customer_ids": invalid_customer_ids,
    }

    logger.info("Data quality summary generated: %s", summary)
    return summary


__all__ = ["generate_data_quality_summary"]
