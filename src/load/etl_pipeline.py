from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

from src.common.logger import get_logger, log_section
from src.load.load_valid_orders import load_valid_orders
from src.transform.data_quality_summary import generate_data_quality_summary
from src.transform.normalize_customer_data import normalize_customer_data
from src.validation.customer_id_validator import validate_customer_id_quality
from src.validation.dataset_structure_validator import validate_dataset_structure
from src.validation.email_validator import validate_email_quality
from src.validation.phone_validator import validate_phone_quality

logger = get_logger("execution")


def _collect_invalid_row_indexes(*validation_results: dict[str, Any]) -> set[int]:
    """Collect invalid row indexes from validation result dictionaries."""
    invalid_rows: set[int] = set()
    for result in validation_results:
        if not isinstance(result, dict):
            continue
        for row_index in result.get("invalid_rows", []):
            try:
                invalid_rows.add(int(row_index))
            except (TypeError, ValueError):
                continue
    return invalid_rows


def execute_etl_pipeline(
    raw_path: str | Path = "data/raw/orders_raw.csv",
    summary_path: str | Path = "data/output/data_quality_summary.json",
    db_path: str | Path = "data/output/orders.db",
) -> dict[str, Any]:
    """Run the end-to-end ETL flow from raw data to normalized and loaded trusted records."""
    log_section(logger, "ETL PIPELINE START")
    logger.info("Starting ETL pipeline execution.")
    source_path = Path(raw_path)
    dataframe = pd.read_csv(source_path)
    logger.info("Raw dataset loaded from %s", source_path)

    structure_result = validate_dataset_structure(dataframe)
    if not structure_result.get("is_valid"):
        logger.critical("ETL pipeline stopped because the dataset structure is invalid: %s", structure_result.get("message"))
        raise ValueError(structure_result.get("message", "Dataset structure is invalid."))
    logger.info("Dataset structure validation passed.")

    customer_id_result = validate_customer_id_quality(dataframe)
    email_result = validate_email_quality(dataframe)
    phone_result = validate_phone_quality(dataframe)

    invalid_indexes = _collect_invalid_row_indexes(
        customer_id_result,
        email_result,
        phone_result,
    )
    logger.warning("Invalid rows identified before transformation: %s", sorted(invalid_indexes))

    valid_dataframe = dataframe.drop(index=sorted(invalid_indexes)).copy()
    logger.info("Valid rows retained for transformation: %s", len(valid_dataframe))

    normalized_dataframe = normalize_customer_data(valid_dataframe)
    logger.info("Data normalization completed.")

    quality_summary = generate_data_quality_summary(normalized_dataframe)
    quality_summary["total_records"] = int(len(normalized_dataframe))
    quality_summary["valid_records"] = int(len(normalized_dataframe))
    quality_summary["invalid_records"] = int(len(invalid_indexes))
    summary_file = Path(summary_path)
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    summary_file.write_text(json.dumps(quality_summary, indent=2), encoding="utf-8")
    logger.info("Data quality summary written to %s", summary_file)

    load_stats = load_valid_orders(normalized_dataframe, db_path)
    logger.info("SQLite load completed. Inserted records: %s; rejected records: %s", load_stats["inserted_records"], load_stats["rejected_records"])

    final_summary = {
        "source_path": str(source_path),
        "database_path": load_stats["database_path"],
        "summary_path": str(summary_file),
        "total_records": int(len(dataframe)),
        "valid_records": int(len(normalized_dataframe)),
        "invalid_records": int(len(dataframe) - len(normalized_dataframe)),
        "inserted_records": load_stats["inserted_records"],
        "rejected_records": load_stats["rejected_records"],
        "quality_summary": quality_summary,
    }

    log_section(logger, "ETL PIPELINE COMPLETED")
    logger.info("ETL pipeline completed with final summary: %s", final_summary)
    return final_summary


__all__ = ["execute_etl_pipeline"]
