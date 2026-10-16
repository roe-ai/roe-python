from types import SimpleNamespace
from uuid import UUID

import pytest

from roe.exceptions import NotFoundError
from roe.models import job as job_module
from roe.models.job import Job, JobBatch, JobStatus


class FakeClock:
    def __init__(self):
        self.now = 0.0

    def monotonic(self):
        return self.now

    def sleep(self, seconds):
        self.now += seconds


@pytest.fixture
def clock(monkeypatch):
    fake = FakeClock()
    monkeypatch.setattr(job_module, "time", fake)
    return fake


def test_job_wait_does_not_sleep_past_timeout(clock):
    jobs = SimpleNamespace(
        retrieve_status=lambda job_id: SimpleNamespace(
            status=JobStatus.STARTED, error_message=None
        )
    )
    job = Job(SimpleNamespace(jobs=jobs), "job-1")

    with pytest.raises(TimeoutError):
        job.wait(interval=60, timeout=1)

    assert clock.now == 1


def test_job_batch_wait_does_not_sleep_past_timeout(clock):
    jobs = SimpleNamespace(
        retrieve_status_many=lambda job_ids: [
            SimpleNamespace(id=UUID(job_id), status=JobStatus.STARTED)
            for job_id in job_ids
        ]
    )
    batch = JobBatch(
        SimpleNamespace(jobs=jobs), ["00000000-0000-0000-0000-000000000001"]
    )

    with pytest.raises(TimeoutError):
        batch.wait(interval=60, timeout=1)

    assert clock.now == 1


def test_job_batch_wait_raises_when_status_response_omits_a_job(clock):
    present = "00000000-0000-0000-0000-000000000001"
    missing = "00000000-0000-0000-0000-000000000002"
    jobs = SimpleNamespace(
        retrieve_status_many=lambda job_ids: [
            SimpleNamespace(id=UUID(present), status=JobStatus.STARTED)
        ]
    )
    batch = JobBatch(SimpleNamespace(jobs=jobs), [present, missing])

    with pytest.raises(NotFoundError, match=missing):
        batch.wait(interval=5, timeout=60)

    assert clock.now == 0
