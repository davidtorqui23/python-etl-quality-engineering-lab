from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
LOGS_DIR = PROJECT_ROOT / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)
RUN_TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
SEPARATOR = "=" * 60


def log_section(logger: logging.Logger, title: str) -> None:
    """Write a readable section header to the active logger."""
    logger.info("\n%s\n%s\n%s", SEPARATOR, title, SEPARATOR)


def get_logger(name: str) -> logging.Logger:
    """Return a logger that writes to a timestamped file for the current execution."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        if name == "execution":
            file_name = f"execution_{RUN_TIMESTAMP}.log"
        elif name == "validation":
            file_name = f"validation_{RUN_TIMESTAMP}.log"
        else:
            file_name = f"etl_{RUN_TIMESTAMP}.log"

        handler = logging.FileHandler(LOGS_DIR / file_name, encoding="utf-8")
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(handler)

    return logger


__all__ = ["get_logger", "log_section"]
