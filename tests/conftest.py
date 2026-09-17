from __future__ import annotations

import pytest

from src.common.logger import get_logger

logger = get_logger("execution")


@pytest.fixture(autouse=True)
def log_test_lifecycle(request):
    """Log the start, completion, and failure state of each test."""
    test_name = request.node.name
    separator = "=" * 65
    logger.info("\n%s\nSTART TEST: %s\n%s", separator, test_name, separator)
    yield

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        logger.warning("FAILED TEST: %s", test_name)

    logger.info("\n%s\nEND TEST: %s\n%s", separator, test_name, separator)
