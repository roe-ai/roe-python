"""CLI coverage for agent file/PDF execution commands."""

from __future__ import annotations

import json
from types import SimpleNamespace

from roe import cli
from roe.models import FileUpload

ORG_ID = "00000000-0000-0000-0000-000000000123"
AGENT_ID = "00000000-0000-0000-0000-000000000111"
JOB_ID = "00000000-0000-0000-0000-000000000333"


def _write_config(path):
    path.write_text(
        json.dumps(
            {
                "api_key": "test-key",
                "organization_id": ORG_ID,
                "base_url": "http://backend",
            }
        ),
        encoding="utf-8",
    )


def test_cli_agent_run_help_exposes_pdf_file_inputs(capsys):
    try:
        cli.main(["agent", "run", "--help"])
    except SystemExit as exc:
        assert exc.code == 0

    output = capsys.readouterr().out
    assert "roe agent run" in output
    assert "--file" in output
    assert "pdf_files=./document.pdf" in output


def test_cli_agent_run_uploads_multiple_pdf_files(tmp_path, monkeypatch, capsys):
    config_path = tmp_path / "config.json"
    _write_config(config_path)
    first_pdf = tmp_path / "first.pdf"
    second_pdf = tmp_path / "second.pdf"
    first_pdf.write_bytes(b"%PDF-1.4\nfirst\n")
    second_pdf.write_bytes(b"%PDF-1.4\nsecond\n")
    monkeypatch.setenv("ROE_CONFIG_FILE", str(config_path))
    calls = []

    class FakeJob:
        id = JOB_ID

    class FakeClient:
        def __init__(self, **kwargs):
            calls.append({"client": kwargs})
            self.agents = SimpleNamespace(run=self.run)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def run(self, *args, **kwargs):
            calls.append({"run": {"args": args, "kwargs": kwargs}})
            return FakeJob()

    monkeypatch.setattr(cli, "RoeClient", FakeClient)

    result = cli.main(
        [
            "agent",
            "run",
            AGENT_ID,
            "--input",
            "prompt=Summarize these PDFs",
            "--file",
            f"pdf_files={first_pdf}",
            "--file",
            f"pdf_files={second_pdf}",
            "--metadata",
            "source=cli-test",
            "--json",
        ]
    )

    assert result == 0
    assert calls[0] == {
        "client": {
            "api_key": "test-key",
            "organization_id": ORG_ID,
            "base_url": "http://backend",
            "timeout": None,
        }
    }
    assert calls[1]["run"]["args"] == (AGENT_ID,)
    kwargs = calls[1]["run"]["kwargs"]
    assert kwargs["prompt"] == "Summarize these PDFs"
    assert kwargs["metadata"] == {"source": "cli-test"}
    assert kwargs["idempotency_key"] is None
    assert [item.path for item in kwargs["pdf_files"]] == [
        str(first_pdf),
        str(second_pdf),
    ]
    assert all(isinstance(item, FileUpload) for item in kwargs["pdf_files"])
    assert json.loads(capsys.readouterr().out) == {"job_id": JOB_ID}


def test_cli_agent_run_wait_prints_result(tmp_path, monkeypatch, capsys):
    config_path = tmp_path / "config.json"
    _write_config(config_path)
    pdf_path = tmp_path / "document.pdf"
    pdf_path.write_bytes(b"%PDF-1.4\n")
    monkeypatch.setenv("ROE_CONFIG_FILE", str(config_path))
    calls = []

    class FakeJob:
        id = JOB_ID

        def wait(self, *args, **kwargs):
            calls.append({"wait": {"args": args, "kwargs": kwargs}})
            return {"job_id": JOB_ID, "status": 3}

    class FakeClient:
        def __init__(self, **kwargs):
            self.agents = SimpleNamespace(run=self.run)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def run(self, *args, **kwargs):
            return FakeJob()

    monkeypatch.setattr(cli, "RoeClient", FakeClient)

    result = cli.main(
        [
            "agent",
            "run",
            AGENT_ID,
            "--file",
            f"pdf_files={pdf_path}",
            "--wait",
            "--poll-interval",
            "0.5",
            "--job-timeout",
            "30",
            "--json",
        ]
    )

    assert result == 0
    assert calls == [
        {"wait": {"args": (), "kwargs": {"interval": 0.5, "timeout": 30.0}}}
    ]
    assert json.loads(capsys.readouterr().out) == {"job_id": JOB_ID, "status": 3}


def test_cli_agent_run_rejects_missing_file(tmp_path, monkeypatch, capsys):
    config_path = tmp_path / "config.json"
    _write_config(config_path)
    monkeypatch.setenv("ROE_CONFIG_FILE", str(config_path))

    result = cli.main(
        [
            "agent",
            "run",
            AGENT_ID,
            "--file",
            f"pdf_files={tmp_path / 'missing.pdf'}",
        ]
    )

    assert result == 1
    assert "Agent input file not found" in capsys.readouterr().err


def test_cli_agent_status_and_result_route_to_jobs_api(tmp_path, monkeypatch, capsys):
    config_path = tmp_path / "config.json"
    _write_config(config_path)
    monkeypatch.setenv("ROE_CONFIG_FILE", str(config_path))
    calls = []

    class FakeJobs:
        def retrieve_status(self, job_id):
            calls.append(("status", job_id))
            return {"job_id": job_id, "status": 1}

        def retrieve_result(self, job_id):
            calls.append(("result", job_id))
            return {"job_id": job_id, "outputs": [{"value": "done"}]}

    class FakeClient:
        def __init__(self, **kwargs):
            self.agents = SimpleNamespace(jobs=FakeJobs())

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    monkeypatch.setattr(cli, "RoeClient", FakeClient)

    status_result = cli.main(["agent", "status", JOB_ID, "--json"])
    result_out = json.loads(capsys.readouterr().out)
    result_result = cli.main(["agent", "result", JOB_ID, "--json"])
    final_out = json.loads(capsys.readouterr().out)

    assert status_result == 0
    assert result_result == 0
    assert calls == [("status", JOB_ID), ("result", JOB_ID)]
    assert result_out == {"job_id": JOB_ID, "status": 1}
    assert final_out == {"job_id": JOB_ID, "outputs": [{"value": "done"}]}
