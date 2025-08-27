"""File detection utilities."""

import os
import re
from typing import Any


def is_uuid_string(value: Any) -> bool:
    """Check if a value is a UUID string.

    Args:
        value: Value to check.

    Returns:
        True if the value is a UUID string, False otherwise.
    """
    if not isinstance(value, str):
        return False

    # UUID regex pattern (with or without hyphens)
    uuid_pattern = re.compile(
        r"^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$",
        re.IGNORECASE,
    )

    return bool(uuid_pattern.match(value))


def is_file_path(value: Any) -> bool:
    """Check if a value is a valid file path that exists.

    Args:
        value: Value to check.

    Returns:
        True if the value is a string path to an existing file, False otherwise.
    """
    if not isinstance(value, str):
        return False

    # Don't treat UUID strings as file paths
    if is_uuid_string(value):
        return False

    return os.path.isfile(value)
