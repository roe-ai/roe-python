"""Shared poll-until-terminal loop for SDK wait helpers."""

from __future__ import annotations

import random
import time
from typing import Callable, TypeVar

T = TypeVar("T")

DEFAULT_BACKOFF_FACTOR = 1.5
DEFAULT_MAX_INTERVAL = 15.0
DEFAULT_JITTER = 0.1


def poll_until(
    check: Callable[[], T | None],
    *,
    interval: float,
    timeout: float | None,
    backoff_factor: float = DEFAULT_BACKOFF_FACTOR,
    max_interval: float = DEFAULT_MAX_INTERVAL,
    jitter: float = DEFAULT_JITTER,
    timeout_message: str = "Timed out while polling",
) -> T:
    """Call ``check`` until it returns non-``None``, with capped backoff between calls.

    ``interval`` is the first sleep; later sleeps grow by ``backoff_factor`` up
    to ``max_interval``, each randomized by +/- ``jitter`` fraction. Sleeps are
    clamped to the remaining ``timeout`` (measured from before the first
    check); when the deadline passes without a result, ``TimeoutError`` is
    raised with ``timeout_message``. ``timeout=None`` polls forever;
    ``timeout=0`` checks exactly once. Callers validate ``timeout`` semantics
    of their own public APIs.
    """
    if interval <= 0:
        raise ValueError("interval must be greater than 0")
    deadline = time.monotonic() + timeout if timeout is not None else None
    sleep_for = interval
    while True:
        result = check()
        if result is not None:
            return result
        if deadline is not None and time.monotonic() >= deadline:
            raise TimeoutError(timeout_message)
        delay = sleep_for
        if jitter:
            delay *= 1.0 + random.uniform(-jitter, jitter)
        if deadline is not None:
            delay = min(delay, max(0.0, deadline - time.monotonic()))
        time.sleep(delay)
        sleep_for = min(sleep_for * backoff_factor, max_interval)
