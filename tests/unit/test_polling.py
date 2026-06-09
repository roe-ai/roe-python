"""Unit tests for the shared poll_until helper."""

import pytest

from roe.utils import polling
from roe.utils.polling import poll_until


class FakeClock:
    """Deterministic monotonic clock; sleeping advances time."""

    def __init__(self):
        self.now = 0.0
        self.sleeps: list[float] = []

    def monotonic(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


@pytest.fixture
def clock(monkeypatch):
    fake = FakeClock()
    monkeypatch.setattr(polling.time, "monotonic", fake.monotonic)
    monkeypatch.setattr(polling.time, "sleep", fake.sleep)
    return fake


def test_poll_until_returns_first_truthy_result_without_sleeping(clock):
    result = poll_until(lambda: {"status": "COMPLETED"}, interval=2.0, timeout=30.0)

    assert result == {"status": "COMPLETED"}
    assert clock.sleeps == []


def test_poll_until_applies_capped_exponential_backoff(clock):
    results = iter([None, None, None, None, None, "done"])

    result = poll_until(
        lambda: next(results),
        interval=4.0,
        timeout=None,
        backoff_factor=2.0,
        max_interval=10.0,
        jitter=0.0,
    )

    assert result == "done"
    assert clock.sleeps == [4.0, 8.0, 10.0, 10.0, 10.0]


def test_poll_until_jitter_stays_within_bounds(clock):
    results = iter([None, None, None, "done"])

    poll_until(
        lambda: next(results),
        interval=10.0,
        timeout=None,
        backoff_factor=1.0,
        jitter=0.1,
    )

    assert len(clock.sleeps) == 3
    for sleep in clock.sleeps:
        assert 9.0 <= sleep <= 11.0


def test_poll_until_clamps_final_sleep_to_deadline_and_times_out(clock):
    calls = []

    def check():
        calls.append(clock.now)
        return None

    with pytest.raises(TimeoutError, match="upload abc"):
        poll_until(
            check,
            interval=4.0,
            timeout=10.0,
            backoff_factor=2.0,
            jitter=0.0,
            timeout_message="Timed out waiting for upload abc",
        )

    # Sleeps: 4.0, then 8.0 clamped to the 6.0 remaining before the deadline.
    assert clock.sleeps == [4.0, 6.0]
    assert len(calls) == 3


def test_poll_until_timeout_zero_checks_once_then_raises(clock):
    calls = []

    def check():
        calls.append(clock.now)
        return None

    with pytest.raises(TimeoutError):
        poll_until(check, interval=1.0, timeout=0.0)

    assert len(calls) == 1
    assert clock.sleeps == []


def test_poll_until_returns_empty_container_results(clock):
    # Falsy-but-not-None results (e.g. an empty batch list) terminate polling.
    result = poll_until(lambda: [], interval=1.0, timeout=5.0)

    assert result == []
    assert clock.sleeps == []


def test_poll_until_rejects_non_positive_interval(clock):
    with pytest.raises(ValueError, match="interval"):
        poll_until(lambda: None, interval=0, timeout=5.0)

    assert clock.sleeps == []
