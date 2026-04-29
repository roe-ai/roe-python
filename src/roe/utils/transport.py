"""Custom httpx transport with retry policy for the Roe SDK.

Retries 502/503/504 responses for GET/PUT/PATCH/DELETE with exponential
backoff. POST is never retried — POSTs may carry non-rewindable multipart
bodies and may not be idempotent on the server side. PATCH is included
because the SDK's only PATCH calls are partial-field updates on
``agents.update()`` / ``policies.update()`` (replacing prior PUT calls)
that the Roe backend implements idempotently — the same partial body
yields the same end state.
"""

from __future__ import annotations

import logging
import time

import httpx

logger = logging.getLogger(__name__)

_RETRYABLE_STATUS_CODES = frozenset({502, 503, 504})
_IDEMPOTENT_METHODS = frozenset({"GET", "PUT", "PATCH", "DELETE"})


class RoeRetryTransport(httpx.HTTPTransport):
    """httpx transport that retries 502/503/504 on idempotent methods."""

    def __init__(self, *, max_retries: int = 3, **kwargs):
        super().__init__(**kwargs)
        self.max_retries = max_retries

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        response = super().handle_request(request)

        if request.method.upper() not in _IDEMPOTENT_METHODS:
            return response

        if response.status_code not in _RETRYABLE_STATUS_CODES:
            return response

        for attempt in range(self.max_retries):
            wait_time = 2 ** attempt  # 1s, 2s, 4s, ...
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
            response = super().handle_request(request)
            if response.status_code not in _RETRYABLE_STATUS_CODES:
                return response

        return response
