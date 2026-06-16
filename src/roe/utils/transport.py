"""Custom httpx transport with retry policy for the Roe SDK.

Retries failed requests with exponential backoff (capped at ~10 seconds):

- Transport errors: ``httpx.TransportError`` (disconnects, timeouts, etc.).
- HTTP statuses: ``5xx``, ``408``, ``429``.
- Applies to **all** HTTP methods, including POST (replay is handled by httpx /
  rewindable buffers for JSON-encoded bodies).

Multipart agent-run helpers opt out via the ``x-roe-skip-retry`` header so
those POSTs are not retried (non-idempotent streamed bodies).

See TS ``retryMiddleware`` / ``dynamicInputs.postDynamicInputs`` and Go
``doRetried`` for the analogous contract across SDKs.
"""

from __future__ import annotations

import logging
from typing import Any

import time

import httpx

logger = logging.getLogger(__name__)

_BYPASS_HEADER = "x-roe-skip-retry"


def _should_retry_status(status_code: int) -> bool:
    return status_code >= 500 or status_code in (408, 429)


class RoeRetryTransport(httpx.HTTPTransport):
    """httpx transport with configurable retries aligned with TS and Go SDKs."""

    def __init__(self, *, max_retries: int = 3, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.max_retries = max_retries

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        if request.headers.get(_BYPASS_HEADER):
            return super().handle_request(request)

        for attempt in range(self.max_retries + 1):
            try:
                response = super().handle_request(request)
            except httpx.TransportError as exc:
                if attempt >= self.max_retries:
                    raise
                wait_time = min(2**attempt, 10)
                logger.warning(
                    "Transport error on %s %s (%s), retrying in %ds (attempt %d/%d)",
                    request.method,
                    request.url,
                    exc,
                    wait_time,
                    attempt + 1,
                    self.max_retries,
                )
                time.sleep(wait_time)
                continue

            if (
                not _should_retry_status(response.status_code)
                or attempt >= self.max_retries
            ):
                return response

            wait_time = min(2**attempt, 10)
            logger.warning(
                "Roe API returned %d for %s %s, retrying in %ds (attempt %d/%d)",
                response.status_code,
                request.method,
                request.url,
                wait_time,
                attempt + 1,
                self.max_retries,
            )
            response.close()
            time.sleep(wait_time)
