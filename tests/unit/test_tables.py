"""Unit tests for the generated ``roe.api.tables.TablesAPI`` facade."""

from __future__ import annotations

import json
import stat
from http import HTTPStatus
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import httpx
import pytest

from roe import cli
from roe._generated.models.table_upload_response import TableUploadResponse
from roe._generated.types import UNSET, Response
from roe.api import table_upload_helpers
from roe.api.tables import TablesAPI
from roe.client import RoeClient


ORG_ID = "323e4567-e89b-12d3-a456-426614174002"


def _fake_response(status: int, payload: dict) -> Response:
    body = json.dumps(payload).encode("utf-8")
    return Response(
        status_code=HTTPStatus(status),
        content=body,
        headers={},
        parsed=TableUploadResponse.from_dict(payload),
    )


def test_tables_upload_builds_multipart_request_from_bytes():
    raw_client = MagicMock()
    config = MagicMock(organization_id=ORG_ID)
    api = TablesAPI(config, raw_client)

    with patch(
        "roe.api.tables.upload_table.sync_detailed",
        return_value=_fake_response(
            201,
            {
                "table_name": "customers",
                "organization_id": ORG_ID,
                "summary": {"written_rows": 1},
            },
        ),
    ) as mocked:
        result = api.upload(
            table_name="customers",
            file=b"name\nAda\n",
            with_headers=True,
        )

    mocked.assert_called_once()
    body = mocked.call_args.kwargs["body"]
    assert body.table_name == "customers"
    assert body.with_headers is True
    assert str(body.organization_id) == ORG_ID
    assert body.file.file_name == "upload.csv"
    assert body.file.mime_type == "text/csv"
    assert result.table_name == "customers"
    assert str(result.organization_id) == ORG_ID


def test_tables_upload_omits_organization_id_when_not_configured():
    raw_client = MagicMock()
    config = MagicMock(organization_id=None)
    api = TablesAPI(config, raw_client)

    with patch(
        "roe.api.tables.upload_table.sync_detailed",
        return_value=_fake_response(
            201,
            {
                "table_name": "customers",
                "organization_id": ORG_ID,
                "summary": {"written_rows": 1},
            },
        ),
    ) as mocked:
        api.upload(
            table_name="customers",
            file=b"name\nAda\n",
        )

    body = mocked.call_args.kwargs["body"]
    assert body.organization_id is UNSET


def test_tables_upload_via_roe_client_generated_registry():
    with patch(
        "roe.api.tables.upload_table.sync_detailed",
        return_value=_fake_response(
            201,
            {
                "table_name": "events",
                "organization_id": ORG_ID,
                "summary": {"written_rows": 2},
            },
        ),
    ):
        from roe import RoeClient

        client = RoeClient(
            api_key="test-key",
            organization_id=ORG_ID,
            base_url="https://example.invalid",
        )
        try:
            result = client.tables.upload(
                table_name="events",
                file=b"id\n1\n2\n",
                with_headers=True,
            )
        finally:
            client.close()

    assert result.table_name == "events"


def test_roe_client_sets_organization_headers_for_raw_table_helpers():
    client = RoeClient(
        api_key="test-key",
        organization_id=ORG_ID,
        base_url="https://example.invalid",
    )
    try:
        headers = client.raw.get_httpx_client().headers
        assert headers["X-Organization-Id"] == ORG_ID
        assert headers["X-Roe-Organization-Id"] == ORG_ID
    finally:
        client.close()


def test_tables_presigned_helpers_use_path_upload_id_endpoints():
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if request.url.path == "/v1/tables/upload/presigned-url/":
            return httpx.Response(
                201,
                json={
                    "upload_id": "00000000-0000-0000-0000-000000000555",
                    "upload_url": "https://uploads.example.com/customers.csv",
                    "upload_method": "PUT",
                    "headers": {"Content-Type": "text/csv"},
                    "expires_at": "2026-06-05T00:00:00Z",
                    "max_bytes": 2147483648,
                },
            )
        if (
            request.url.path
            == "/v1/tables/upload/00000000-0000-0000-0000-000000000555/complete/"
        ):
            return httpx.Response(
                202,
                json={
                    "upload_id": "00000000-0000-0000-0000-000000000555",
                    "status": "IMPORTING",
                    "table_name": "customers",
                    "organization_id": ORG_ID,
                    "summary": None,
                },
            )
        if (
            request.url.path
            == "/v1/tables/upload/00000000-0000-0000-0000-000000000555/status/"
        ):
            return httpx.Response(
                200,
                json={
                    "upload_id": "00000000-0000-0000-0000-000000000555",
                    "status": "COMPLETED",
                    "table_name": "customers",
                    "organization_id": ORG_ID,
                    "summary": {"written_rows": 1},
                },
            )
        return httpx.Response(404, json={"detail": "not found"})

    httpx_client = httpx.Client(
        base_url="http://backend",
        transport=httpx.MockTransport(handler),
    )
    raw_client = MagicMock()
    raw_client.get_httpx_client.return_value = httpx_client
    api = TablesAPI(MagicMock(organization_id=ORG_ID), raw_client)

    created = api.create_upload(
        table_name="customers",
        filename="customers.csv",
        content_type="text/csv",
        with_headers=False,
    )
    completed = api.complete_upload(upload_id=created["upload_id"])
    status = api.upload_status(upload_id=created["upload_id"])

    assert created["upload_method"] == "PUT"
    assert completed["status"] == "IMPORTING"
    assert status["status"] == "COMPLETED"
    assert json.loads(requests[0].content) == {
        "table_name": "customers",
        "filename": "customers.csv",
        "content_type": "text/csv",
        "with_headers": False,
        "organization_id": ORG_ID,
    }
    assert requests[1].method == "POST"
    assert requests[1].content == b""
    assert requests[2].method == "GET"
    assert requests[2].content == b""


def test_tables_presigned_helpers_reject_invalid_upload_id_before_http():
    raw_client = MagicMock()
    raw_client.get_httpx_client.return_value = MagicMock()
    api = TablesAPI(MagicMock(organization_id=ORG_ID), raw_client)

    with pytest.raises(ValueError):
        api.upload_status(upload_id="../not-a-uuid")

    raw_client.get_httpx_client.return_value.request.assert_not_called()


def test_tables_upload_large_uses_presigned_storage_path(tmp_path):
    path = tmp_path / "customers.csv"
    path.write_text("name,age\nAda,37\n")
    api = TablesAPI(MagicMock(organization_id=ORG_ID), MagicMock())
    put_calls = []

    with (
        patch.object(
            api,
            "create_upload",
            return_value={
                "upload_id": "00000000-0000-0000-0000-000000000555",
                "upload_url": "https://uploads.example.com/customers.csv",
                "headers": {"Content-Type": "text/csv"},
            },
        ) as create_upload,
        patch(
            "roe.api.table_upload_helpers._put_presigned_upload",
            side_effect=lambda **kwargs: put_calls.append(kwargs),
        ) as put,
        patch.object(
            api,
            "complete_upload",
            return_value={
                "upload_id": "00000000-0000-0000-0000-000000000555",
                "status": "COMPLETED",
                "table_name": "customers",
            },
        ) as complete_upload,
    ):
        result = api.upload_large(path, table_name="customers", with_headers=False)

    create_upload.assert_called_once_with(
        table_name="customers",
        filename="customers.csv",
        content_type="text/csv",
        with_headers=False,
        organization_id=None,
    )
    put.assert_called_once()
    assert put_calls == [
        {
            "upload_url": "https://uploads.example.com/customers.csv",
            "headers": {"Content-Type": "text/csv"},
            "file_path": path,
        }
    ]
    complete_upload.assert_called_once_with(
        upload_id="00000000-0000-0000-0000-000000000555"
    )
    assert result["status"] == "COMPLETED"


def test_put_presigned_upload_retries_and_does_not_forward_roe_auth_headers(
    tmp_path,
    monkeypatch,
):
    path = tmp_path / "customers.csv"
    path.write_text("name,age\nAda,37\n")
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if len(requests) == 1:
            return httpx.Response(503, json={"detail": "retry later"})
        return httpx.Response(200)

    real_client = httpx.Client

    def fake_client(**kwargs):
        assert kwargs["trust_env"] is False
        return real_client(transport=httpx.MockTransport(handler))

    monkeypatch.setattr(table_upload_helpers.httpx, "Client", fake_client)
    monkeypatch.setattr(table_upload_helpers.time, "sleep", lambda _: None)

    table_upload_helpers._put_presigned_upload(
        upload_url="https://uploads.example.com/customers.csv",
        headers={
            "Content-Type": "text/csv",
            "Authorization": "Bearer roe-token",
            "X-Organization-Id": ORG_ID,
            "X-Roe-Organization-Id": ORG_ID,
        },
        file_path=path,
    )

    assert len(requests) == 2
    assert requests[0].headers["content-type"] == "text/csv"
    assert requests[0].headers["content-length"] == str(path.stat().st_size)
    assert "authorization" not in requests[0].headers
    assert "x-organization-id" not in requests[0].headers
    assert "x-roe-organization-id" not in requests[0].headers


def test_tables_upload_large_waits_for_import_when_requested(tmp_path):
    path = tmp_path / "customers.csv"
    path.write_text("name,age\nAda,37\n")
    api = TablesAPI(MagicMock(organization_id=ORG_ID), MagicMock())

    with (
        patch.object(
            api,
            "create_upload",
            return_value={
                "upload_id": "00000000-0000-0000-0000-000000000555",
                "upload_url": "https://uploads.example.com/customers.csv",
                "headers": {},
            },
        ),
        patch("roe.api.table_upload_helpers._put_presigned_upload"),
        patch.object(
            api,
            "complete_upload",
            return_value={
                "upload_id": "00000000-0000-0000-0000-000000000555",
                "status": "IMPORTING",
            },
        ),
        patch.object(
            api,
            "wait_for_upload",
            return_value={
                "upload_id": "00000000-0000-0000-0000-000000000555",
                "status": "COMPLETED",
            },
        ) as wait_for_upload,
    ):
        result = api.upload_large(
            path,
            table_name="customers",
            wait=True,
            interval=0.5,
            timeout=30,
        )

    wait_for_upload.assert_called_once_with(
        upload_id="00000000-0000-0000-0000-000000000555",
        interval=0.5,
        timeout=30,
    )
    assert result["status"] == "COMPLETED"


def test_tables_wait_for_upload_rejects_invalid_interval():
    api = TablesAPI(MagicMock(organization_id=ORG_ID), MagicMock())

    with pytest.raises(ValueError, match="interval"):
        api.wait_for_upload(
            upload_id="00000000-0000-0000-0000-000000000555",
            interval=0,
        )


def test_tables_upload_large_validates_interval_before_uploading(tmp_path):
    # A bad wait interval must fail before any bytes are uploaded or the
    # import is started.
    path = tmp_path / "customers.csv"
    path.write_text("name,age\nAda,37\n")
    api = TablesAPI(MagicMock(organization_id=ORG_ID), MagicMock())

    with (
        patch.object(api, "create_upload") as create_upload,
        patch("roe.api.table_upload_helpers._put_presigned_upload") as put_upload,
    ):
        with pytest.raises(ValueError, match="interval"):
            api.upload_large(
                path,
                table_name="customers",
                wait=True,
                interval=0,
            )

    create_upload.assert_not_called()
    put_upload.assert_not_called()


def test_tables_wait_for_upload_times_out():
    api = TablesAPI(MagicMock(organization_id=ORG_ID), MagicMock())

    with patch.object(api, "upload_status", return_value={"status": "IMPORTING"}):
        with pytest.raises(TimeoutError, match="Timed out"):
            api.wait_for_upload(
                upload_id="00000000-0000-0000-0000-000000000555",
                interval=0.01,
                timeout=0,
            )


def test_cli_auth_login_writes_config(tmp_path, monkeypatch, capsys):
    config_path = tmp_path / "config.json"
    monkeypatch.setenv("ROE_CONFIG_FILE", str(config_path))

    result = cli.main(
        [
            "auth",
            "login",
            "--api-key",
            "test-key",
            "--organization-id",
            ORG_ID,
            "--base-url",
            "http://backend",
            "--timeout",
            "12",
        ]
    )

    assert result == 0
    assert "Saved Roe credentials" in capsys.readouterr().out
    assert stat.S_IMODE(config_path.stat().st_mode) == 0o600
    assert json.loads(config_path.read_text(encoding="utf-8")) == {
        "api_key": "test-key",
        "base_url": "http://backend",
        "organization_id": ORG_ID,
        "timeout": 12.0,
    }


def test_cli_auth_login_restricts_existing_config_permissions(
    tmp_path, monkeypatch, capsys
):
    config_path = tmp_path / "config.json"
    config_path.write_text("{}", encoding="utf-8")
    config_path.chmod(0o644)
    monkeypatch.setenv("ROE_CONFIG_FILE", str(config_path))

    result = cli.main(
        [
            "auth",
            "login",
            "--api-key",
            "test-key",
            "--organization-id",
            ORG_ID,
        ]
    )

    assert result == 0
    assert "Saved Roe credentials" in capsys.readouterr().out
    assert stat.S_IMODE(config_path.stat().st_mode) == 0o600


def test_cli_table_upload_help_exposes_agent_friendly_command(capsys):
    with pytest.raises(SystemExit) as exc:
        cli.main(["table", "upload", "--help"])

    assert exc.value.code == 0
    output = capsys.readouterr().out
    assert "roe table upload" in output
    assert "--table" in output
    assert "--wait" in output


def test_cli_table_upload_uses_large_upload_helper(tmp_path, monkeypatch, capsys):
    config_path = tmp_path / "config.json"
    config_path.write_text(
        json.dumps(
            {
                "api_key": "test-key",
                "organization_id": ORG_ID,
                "base_url": "http://backend",
            }
        ),
        encoding="utf-8",
    )
    csv_path = tmp_path / "customers.csv"
    csv_path.write_text("name,age\nAda,37\n", encoding="utf-8")
    monkeypatch.setenv("ROE_CONFIG_FILE", str(config_path))
    calls = []

    class FakeClient:
        def __init__(self, **kwargs):
            calls.append({"client": kwargs})
            self.tables = SimpleNamespace(upload_large=self.upload_large)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def upload_large(self, *args, **kwargs):
            calls.append({"upload_large": {"args": args, "kwargs": kwargs}})
            return {
                "upload_id": "00000000-0000-0000-0000-000000000555",
                "status": "IMPORTING",
                "table_name": "customers",
            }

    monkeypatch.setattr(cli, "RoeClient", FakeClient)

    result = cli.main(
        [
            "table",
            "upload",
            str(csv_path),
            "--table",
            "customers",
            "--no-headers",
            "--wait",
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
    assert calls[1]["upload_large"]["args"] == (str(csv_path),)
    assert calls[1]["upload_large"]["kwargs"] == {
        "table_name": "customers",
        "with_headers": False,
        "wait": True,
        "interval": 2.0,
        "timeout": None,
    }
    assert json.loads(capsys.readouterr().out)["status"] == "IMPORTING"


def test_cli_table_upload_wait_returns_nonzero_for_terminal_failure(
    tmp_path, monkeypatch, capsys
):
    config_path = tmp_path / "config.json"
    config_path.write_text(
        json.dumps(
            {
                "api_key": "test-key",
                "organization_id": ORG_ID,
                "base_url": "http://backend",
            }
        ),
        encoding="utf-8",
    )
    csv_path = tmp_path / "customers.csv"
    csv_path.write_text("name,age\nAda,37\n", encoding="utf-8")
    monkeypatch.setenv("ROE_CONFIG_FILE", str(config_path))

    class FakeClient:
        def __init__(self, **kwargs):
            self.tables = SimpleNamespace(upload_large=self.upload_large)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def upload_large(self, *args, **kwargs):
            return {
                "upload_id": "00000000-0000-0000-0000-000000000555",
                "status": "FAILED",
                "table_name": "customers",
                "error": "bad csv",
            }

    monkeypatch.setattr(cli, "RoeClient", FakeClient)

    result = cli.main(
        [
            "table",
            "upload",
            str(csv_path),
            "--table",
            "customers",
            "--wait",
            "--json",
        ]
    )

    assert result == 1
    captured = capsys.readouterr()
    assert json.loads(captured.out)["status"] == "FAILED"
    assert "Table upload failed: bad csv" in captured.err


def test_cli_table_status_routes_to_upload_status(monkeypatch, tmp_path, capsys):
    config_path = tmp_path / "config.json"
    config_path.write_text(
        json.dumps(
            {
                "api_key": "test-key",
                "organization_id": ORG_ID,
                "base_url": "http://backend",
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setenv("ROE_CONFIG_FILE", str(config_path))
    calls = []

    class FakeClient:
        def __init__(self, **kwargs):
            calls.append({"client": kwargs})
            self.tables = SimpleNamespace(upload_status=self.upload_status)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def upload_status(self, *, upload_id):
            calls.append({"upload_status": upload_id})
            return {"upload_id": upload_id, "status": "COMPLETED"}

    monkeypatch.setattr(cli, "RoeClient", FakeClient)

    result = cli.main(
        [
            "table",
            "status",
            "00000000-0000-0000-0000-000000000555",
            "--json",
        ]
    )

    assert result == 0
    assert calls[1] == {"upload_status": "00000000-0000-0000-0000-000000000555"}
    assert json.loads(capsys.readouterr().out)["status"] == "COMPLETED"
