from __future__ import annotations

from pathlib import Path
from typing import Union

import pandas as pd


PathLike = Union[str, Path]


class OrdersExtractor:
    """Load and validate the raw orders dataset for the US-001 ETL flow."""

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
    EXPECTED_ROW_COUNT = 50

    @staticmethod
    def validate_path(file_path: PathLike) -> Path:
        """Resolve and validate the dataset path."""
        path = Path(file_path)

        if not path.is_absolute():
            project_root = Path(__file__).resolve().parents[2]
            path = (project_root / path).resolve()

        if not path.exists():
            raise FileNotFoundError(f"Dataset not found: {file_path}")

        if not path.is_file():
            raise FileNotFoundError(f"Expected a file path, received directory: {file_path}")

        if path.stat().st_size == 0:
            raise ValueError(f"Dataset is empty: {file_path}")

        return path

    @classmethod
    def validate_columns(cls, dataframe: pd.DataFrame) -> None:
        """Ensure the raw dataset contains the expected minimum schema."""
        missing_columns = [column for column in cls.REQUIRED_COLUMNS if column not in dataframe.columns]

        if missing_columns:
            raise ValueError(
                "Dataset is missing required columns: "
                + ", ".join(missing_columns)
            )

    @classmethod
    def validate_row_count(cls, dataframe: pd.DataFrame) -> None:
        """Ensure the dataset matches the expected number of records."""
        if len(dataframe) != cls.EXPECTED_ROW_COUNT:
            raise ValueError(
                "Dataset row count mismatch. "
                f"Expected {cls.EXPECTED_ROW_COUNT} rows, received {len(dataframe)}."
            )

    @classmethod
    def extract(cls, file_path: PathLike) -> pd.DataFrame:
        """Read and validate the orders dataset from disk."""
        path = cls.validate_path(file_path)

        try:
            dataframe = pd.read_csv(path)
        except UnicodeDecodeError as exc:
            raise ValueError(f"Invalid encoding in dataset: {path}") from exc
        except pd.errors.EmptyDataError as exc:
            raise ValueError(f"Dataset is empty: {path}") from exc

        if dataframe.empty:
            raise ValueError(f"Dataset is empty: {path}")

        cls.validate_columns(dataframe)
        cls.validate_row_count(dataframe)

        return dataframe


def extract_orders(file_path: PathLike) -> pd.DataFrame:
    """Project-level entry point for extracting the raw orders dataset."""
    return OrdersExtractor.extract(file_path)


__all__ = ["OrdersExtractor", "extract_orders"]