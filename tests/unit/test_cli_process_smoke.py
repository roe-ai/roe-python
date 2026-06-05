"""Subprocess-level CLI smoke tests against a local HTTP server."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
from threading import Thread
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

ORG_ID = "00000000-0000-0000-0000-000000000123"
AGENT_ID = "00000000-0000-0000-0000-000000000111"
VERSION_ID = "00000000-0000-0000-0000-000000000222"
JOB_ID = "00000000-0000-0000-0000-000000000333"
UPLOAD_ID = "00000000-0000-0000-0000-000000000444"
LARGE_DOCX_SIZE = 6 * 1024 * 1024


def _write_config(path: Path, base_url: str) -> None:
    path.write_text(
        json.dumps(
            {
                "api_key": "test-key",
                "organization_id": ORG_ID,
                "base_url": base_url,
            }
        ),
        encoding="utf-8",
    )


def _run_cli(
    tmp_path: Path, config_path: Path, *args: str
) -> subprocess.CompletedProcess:
    env = os.environ.copy()
    env["ROE_CONFIG_FILE"] = str(config_path)
    env["PYTHONPATH"] = os.pathsep.join(
        item
        for item in [
            str(Path(__file__).resolve().parents[2] / "src"),
            env.get("PYTHONPATH", ""),
        ]
        if item
    )
    return subprocess.run(
        [sys.executable, "-m", "roe.cli", *args],
        cwd=tmp_path,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def test_cli_process_agent_pdf_run_and_table_upload_round_trip(tmp_path):
    events: list[dict[str, object]] = []

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, format, *args):  # noqa: A002
            return

        def _body(self) -> bytes:
            length = int(self.headers.get("Content-Length") or "0")
            return self.rfile.read(length)

        def _send_json(self, status: int, payload: object) -> None:
            body = json.dumps(payload).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _send_empty(self, status: int) -> None:
            self.send_response(status)
            self.send_header("Content-Length", "0")
            self.end_headers()

        def _assert_roe_headers(self) -> None:
            assert self.headers["Authorization"] == "Bearer test-key"
            assert self.headers["X-Organization-Id"] == ORG_ID
            assert self.headers["X-Roe-Organization-Id"] == ORG_ID

        def do_POST(self) -> None:
            parsed = urlparse(self.path)
            query = parse_qs(parsed.query)
            self._assert_roe_headers()

            if parsed.path == f"/v1/agents/run/{AGENT_ID}/async/":
                assert query == {"organization_id": [ORG_ID]}
                assert self.headers["Idempotency-Key"] == "idem-process"
                assert self.headers["x-roe-skip-retry"] == "1"
                content_type = self.headers["Content-Type"]
                assert content_type.startswith("multipart/form-data; boundary=")
                body = self._body()
                assert body.count(b'name="pdf_files"') == 2
                assert b'filename="first.pdf"' in body
                assert b'filename="second.pdf"' in body
                assert body.count(b"Content-Type: application/pdf") == 2
                assert body.count(b'name="documents"') == 1
                assert b'filename="handbook.docx"' in body
                assert (
                    b"Content-Type: application/vnd.openxmlformats-officedocument."
                    b"wordprocessingml.document"
                ) in body
                assert b"large-docx-marker" in body
                assert b'name="prompt"' in body
                assert b"Summarize these PDFs" in body
                assert b'name="source_url"' in body
                assert b"https://example.com/manual.pdf" in body
                assert b'name="metadata"' in body
                assert b'"flow": "process"' in body
                assert b'"source": "cli"' in body
                events.append({"kind": "agent_run", "bytes": len(body)})
                self._send_json(200, JOB_ID)
                return

            if parsed.path == "/v1/tables/upload/presigned-url/":
                payload = json.loads(self._body())
                assert payload == {
                    "content_type": "text/csv",
                    "filename": "flights.csv",
                    "organization_id": ORG_ID,
                    "table_name": "flights",
                    "with_headers": False,
                }
                events.append({"kind": "table_create"})
                self._send_json(
                    201,
                    {
                        "upload_id": UPLOAD_ID,
                        "upload_url": f"http://{self.server.server_address[0]}:{self.server.server_address[1]}/presigned/flights.csv",
                        "headers": {
                            "Authorization": "Bearer should-not-leak",
                            "X-Organization-Id": "should-not-leak",
                            "X-Roe-Organization-Id": "should-not-leak",
                            "x-amz-meta-test": "ok",
                        },
                    },
                )
                return

            if parsed.path == f"/v1/tables/upload/{UPLOAD_ID}/complete/":
                assert self._body() == b""
                events.append({"kind": "table_complete"})
                self._send_json(202, {"upload_id": UPLOAD_ID, "status": "COMPLETED"})
                return

            self._send_json(404, {"detail": f"unexpected POST {self.path}"})

        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            query = parse_qs(parsed.query)
            self._assert_roe_headers()
            assert query == {"organization_id": [ORG_ID]}

            if parsed.path == f"/v1/agents/jobs/{JOB_ID}/status/":
                events.append({"kind": "agent_status"})
                self._send_json(200, {"status": 3, "timestamp": 123})
                return

            if parsed.path == f"/v1/agents/jobs/{JOB_ID}/result/":
                events.append({"kind": "agent_result"})
                self._send_json(
                    200,
                    {
                        "agent_id": AGENT_ID,
                        "agent_version_id": VERSION_ID,
                        "inputs": [],
                        "input_tokens": None,
                        "output_tokens": None,
                        "outputs": [
                            {
                                "key": "answer",
                                "data_type": "text/plain",
                                "value": "done",
                            }
                        ],
                    },
                )
                return

            self._send_json(404, {"detail": f"unexpected GET {self.path}"})

        def do_PUT(self) -> None:
            parsed = urlparse(self.path)
            assert parsed.path == "/presigned/flights.csv"
            lower_headers = {key.lower(): value for key, value in self.headers.items()}
            assert "authorization" not in lower_headers
            assert "x-organization-id" not in lower_headers
            assert "x-roe-organization-id" not in lower_headers
            assert lower_headers["x-amz-meta-test"] == "ok"
            body = self._body()
            assert body == b"origin,dest\nSFO,JFK\n"
            events.append({"kind": "presigned_put", "bytes": len(body)})
            self._send_empty(200)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    config_path = tmp_path / "config.json"
    _write_config(
        config_path,
        f"http://{server.server_address[0]}:{server.server_address[1]}",
    )

    try:
        first_pdf = tmp_path / "first.pdf"
        second_pdf = tmp_path / "second.pdf"
        handbook = tmp_path / "handbook.docx"
        first_pdf.write_bytes(b"%PDF-1.4\nfirst\n")
        second_pdf.write_bytes(b"%PDF-1.4\nsecond\n")
        handbook.write_bytes(
            b"PK\x03\x04large-docx-marker\n"
            + (b"x" * (LARGE_DOCX_SIZE - len(b"PK\x03\x04large-docx-marker\n")))
        )
        agent = _run_cli(
            tmp_path,
            config_path,
            "agent",
            "run",
            AGENT_ID,
            "--input",
            "prompt=Summarize these PDFs",
            "--input",
            "source_url=https://example.com/manual.pdf",
            "--file",
            f"pdf_files={first_pdf}",
            "--file",
            f"pdf_files={second_pdf}",
            "--file",
            f"documents={handbook}",
            "--metadata-json",
            '{"flow":"process"}',
            "--metadata",
            "source=cli",
            "--idempotency-key",
            "idem-process",
            "--wait",
            "--poll-interval",
            "0.01",
            "--job-timeout",
            "2",
            "--json",
        )
        assert agent.returncode == 0, agent.stderr
        agent_payload = json.loads(agent.stdout)
        assert agent_payload["status"] == 3
        assert agent_payload["outputs"][0]["value"] == "done"

        csv_path = tmp_path / "flights.csv"
        csv_path.write_bytes(b"origin,dest\nSFO,JFK\n")
        table = _run_cli(
            tmp_path,
            config_path,
            "table",
            "upload",
            str(csv_path),
            "--table",
            "flights",
            "--no-headers",
            "--json",
        )
        assert table.returncode == 0, table.stderr
        assert json.loads(table.stdout) == {
            "upload_id": UPLOAD_ID,
            "status": "COMPLETED",
        }
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    assert events == [
        {"kind": "agent_run", "bytes": events[0]["bytes"]},
        {"kind": "agent_status"},
        {"kind": "agent_result"},
        {"kind": "table_create"},
        {"kind": "presigned_put", "bytes": 20},
        {"kind": "table_complete"},
    ]
    assert events[0]["bytes"] > LARGE_DOCX_SIZE
