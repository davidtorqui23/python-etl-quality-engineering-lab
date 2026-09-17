from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import pandas as pd

from src.common.logger import get_logger

logger = get_logger("validation")


COUNTRY_MAP = {
    "CO": "Colombia",
    "COLOMBIA": "Colombia",
    "USA": "United States",
    "US": "United States",
    "UNITED STATES": "United States",
    "UNITED STATES OF AMERICA": "United States",
    "MEXICO": "Mexico",
    "CANADA": "Canada",
    "SPAIN": "Spain",
}


def _normalize_country(value: Any) -> str:
    if pd.isna(value):
        return ""

    normalized = str(value).strip()
    if not normalized:
        return ""

    country_key = normalized.upper().replace(".", "").replace("-", " ").strip()
    country_key = " ".join(country_key.split())
    return COUNTRY_MAP.get(country_key, normalized.title())


def _normalize_phone(value: Any) -> str:
    if pd.isna(value):
        return ""

    digits = re.sub(r"\D+", "", str(value).strip())
    return digits


def normalize_customer_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Normalize fields so customer records are standardized for downstream ETL use."""
    logger.info("Starting customer data normalization.")
    if dataframe is None:
        raise ValueError("Input dataframe cannot be None.")

    normalized = dataframe.copy()
    for column in normalized.columns:
        if normalized[column].dtype == "object":
            normalized[column] = normalized[column].map(lambda value: value.strip() if isinstance(value, str) else value)

    normalized["email"] = normalized["email"].map(
        lambda value: str(value).strip().lower() if isinstance(value, str) else value
    )

    if "country" in normalized.columns:
        normalized["country"] = normalized["country"].map(_normalize_country)

    if "phone" in normalized.columns:
        normalized["phone"] = normalized["phone"].map(_normalize_phone)

    if "full_name" in normalized.columns:
        normalized["full_name"] = normalized["full_name"].map(
            lambda value: str(value).strip() if isinstance(value, str) else value
        )

    statistics = {
        "rows": int(len(normalized)),
        "email_lowercase_count": int(normalized["email"].astype(str).str.count("@").sum()) if "email" in normalized.columns else 0,
        "country_normalized_count": int((normalized["country"].astype(str).str.len() > 0).sum()) if "country" in normalized.columns else 0,
        "phone_digits_count": int((normalized["phone"].astype(str).str.len() > 0).sum()) if "phone" in normalized.columns else 0,
    }
    logger.info("Customer data normalization completed with statistics: %s", statistics)
    return normalized


def main() -> None:
    """Generate the normalized orders dataset in the processed output directory."""
    logger.info("Preparing normalized dataset output.")
    source_path = Path("data/raw/orders_raw.csv")
    output_path = Path("data/processed/orders_normalized.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    dataframe = pd.read_csv(source_path)
    normalized = normalize_customer_data(dataframe)
    normalized.to_csv(output_path, index=False)
    logger.info("Normalized dataset saved to %s", output_path)


if __name__ == "__main__":
    main()
