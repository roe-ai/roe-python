import httpx
import pytest

from roe.utils import transport
from roe.utils.transport import RoeRetryTransport


@pytest.mark.parametrize(
    ("status", "retry_after", "expected_sleep"),
    [(429, "5", 5), (503, "120", 60), (429, "Wed, 21 Oct 2025 07:28:00 GMT", 1)],
)
def test_retry_waits_for_retry_after_seconds(
    monkeypatch, status, retry_after, expected_sleep
):
    responses = [
        httpx.Response(status, headers={"Retry-After": retry_after}),
        httpx.Response(200),
    ]
    sleeps = []
    monkeypatch.setattr(
        httpx.HTTPTransport, "handle_request", lambda self, req: responses.pop(0)
    )
    monkeypatch.setattr(transport.time, "sleep", sleeps.append)

    response = RoeRetryTransport().handle_request(
        httpx.Request("GET", "https://example.com")
    )

    assert response.status_code == 200
    assert sleeps == [expected_sleep]
