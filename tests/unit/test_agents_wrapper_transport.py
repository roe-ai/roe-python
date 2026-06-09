"""Regression tests for public SDK wrapper transport behavior."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

import httpx
import pytest

from roe.api.agents import AgentsAPI
from roe.exceptions import NotFoundError
from roe.models import FileUpload

ORG_ID = "00000000-0000-0000-0000-000000000123"
AGENT_ID = "00000000-0000-0000-0000-000000000111"
VERSION_ID = "00000000-0000-0000-0000-000000000222"
JOB_ID = "00000000-0000-0000-0000-000000000333"


def _api(response: httpx.Response) -> tuple[AgentsAPI, MagicMock]:
    request = MagicMock(return_value=response)
    raw_client = MagicMock()
    raw_client.get_httpx_client.return_value = SimpleNamespace(request=request)
    config = SimpleNamespace(organization_id=ORG_ID, batch_chunk_delay=0)
    return AgentsAPI(config, raw_client), request


def test_agent_version_retrieve_404_uses_sdk_error_not_generated_error_parser():
    api, _ = _api(
        httpx.Response(404, json={"detail": "No Agent matches the given query."})
    )

    with pytest.raises(NotFoundError) as exc_info:
        api.versions.retrieve(AGENT_ID, VERSION_ID)

    assert exc_info.value.message == "No Agent matches the given query."


def test_job_cancel_404_uses_sdk_error_not_generated_error_parser():
    api, _ = _api(httpx.Response(404, json={"detail": "No AgentJob found."}))

    with pytest.raises(NotFoundError) as exc_info:
        api.jobs.cancel(JOB_ID)

    assert exc_info.value.message == "No AgentJob found."


def test_run_passes_idempotency_key_through_dynamic_wrapper():
    api, request = _api(httpx.Response(200, json=JOB_ID))

    job = api.run(AGENT_ID, idempotency_key="idem-123", prompt="hello")

    kwargs = request.call_args.kwargs
    assert kwargs["headers"]["Idempotency-Key"] == "idem-123"
    assert kwargs["headers"]["x-roe-skip-retry"] == "1"
    assert job.id == JOB_ID


def test_run_sends_repeated_file_fields_for_multiple_pdf_inputs(tmp_path):
    first = tmp_path / "first.pdf"
    second = tmp_path / "second.pdf"
    first.write_bytes(b"%PDF-1.4\nfirst\n")
    second.write_bytes(b"%PDF-1.4\nsecond\n")
    api, request = _api(httpx.Response(200, json=JOB_ID))

    api.run(
        AGENT_ID,
        prompt="summarize",
        pdf_files=[
            FileUpload(path=str(first)),
            FileUpload(path=str(second)),
        ],
    )

    kwargs = request.call_args.kwargs
    assert kwargs["data"] == {"prompt": "summarize"}
    pdf_parts = [part for key, part in kwargs["files"] if key == "pdf_files"]
    assert [part[0] for part in pdf_parts] == ["first.pdf", "second.pdf"]
    assert [part[2] for part in pdf_parts] == ["application/pdf", "application/pdf"]
    assert all(part[1].closed for part in pdf_parts)


def test_run_sends_bytes_upload_with_explicit_pdf_metadata():
    api, request = _api(httpx.Response(200, json=JOB_ID))

    api.run(
        AGENT_ID,
        prompt="segment this policy",
        pdf_file=FileUpload.from_bytes(
            b"%PDF-1.4\nbytes\n",
            filename="policy.pdf",
            mime_type="application/pdf",
        ),
    )

    kwargs = request.call_args.kwargs
    assert kwargs["data"] == {"prompt": "segment this policy"}
    assert len(kwargs["files"]) == 1
    key, part = kwargs["files"][0]
    assert key == "pdf_file"
    assert part[0] == "policy.pdf"
    assert part[1].getvalue() == b"%PDF-1.4\nbytes\n"
    assert part[2] == "application/pdf"


def test_run_sends_docx_path_with_office_mime_type(tmp_path):
    document = tmp_path / "contract.docx"
    document.write_bytes(b"PK\x03\x04docx")
    api, request = _api(httpx.Response(200, json=JOB_ID))

    api.run(AGENT_ID, documents=FileUpload(path=str(document)))

    key, part = request.call_args.kwargs["files"][0]
    assert key == "documents"
    assert part[0] == "contract.docx"
    assert part[2] == (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    assert part[1].closed


def test_run_streams_existing_string_path_instead_of_reading_into_memory(tmp_path):
    document = tmp_path / "policy.pdf"
    document.write_bytes(b"%PDF-1.4\nlocal path\n")
    api, request = _api(httpx.Response(200, json=JOB_ID))

    api.run(AGENT_ID, pdf_file=str(document))

    key, part = request.call_args.kwargs["files"][0]
    assert key == "pdf_file"
    assert part[0] == "policy.pdf"
    assert part[1].name == str(document)
    assert part[1].closed
    assert part[2] == "application/pdf"


def test_run_sends_path_string_list_as_repeated_file_fields(tmp_path):
    first = tmp_path / "first.pdf"
    second = tmp_path / "second.pdf"
    first.write_bytes(b"%PDF-1.4\nfirst\n")
    second.write_bytes(b"%PDF-1.4\nsecond\n")
    api, request = _api(httpx.Response(200, json=JOB_ID))

    api.run(AGENT_ID, pdf_files=[str(first), str(second)])

    parts = [
        part for key, part in request.call_args.kwargs["files"] if key == "pdf_files"
    ]
    assert [part[0] for part in parts] == ["first.pdf", "second.pdf"]
    assert all(part[1].closed for part in parts)
    assert [part[2] for part in parts] == ["application/pdf", "application/pdf"]


def test_run_rejects_raw_bytes_without_filename():
    api, _ = _api(httpx.Response(200, json=JOB_ID))

    with pytest.raises(ValueError, match="FileUpload.from_bytes"):
        api.run(AGENT_ID, pdf_file=b"%PDF-1.4\nraw\n")


def test_run_rejects_mixed_file_and_scalar_list(tmp_path):
    document = tmp_path / "policy.pdf"
    document.write_bytes(b"%PDF-1.4\nlocal\n")
    api, _ = _api(httpx.Response(200, json=JOB_ID))

    with pytest.raises(ValueError, match="mixes local file uploads"):
        api.run(AGENT_ID, pdf_files=[str(document), "https://example.com/policy.pdf"])


def test_run_keeps_urls_and_roe_file_ids_as_scalar_inputs():
    api, request = _api(httpx.Response(200, json=JOB_ID))

    api.run(
        AGENT_ID,
        pdf_file="https://example.com/policy.pdf",
        existing_file="00000000-0000-0000-0000-000000000999",
    )

    kwargs = request.call_args.kwargs
    assert kwargs["data"] == {
        "pdf_file": "https://example.com/policy.pdf",
        "existing_file": "00000000-0000-0000-0000-000000000999",
    }
    assert kwargs["files"] == []
