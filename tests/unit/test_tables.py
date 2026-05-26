"""Unit tests for the generated ``roe.api.tables.TablesAPI`` facade."""

from __future__ import annotations

import json
from http import HTTPStatus
from unittest.mock import MagicMock, patch

from roe._generated.models.table_upload_response import TableUploadResponse
from roe._generated.types import UNSET, Response
from roe.api.tables import TablesAPI


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
