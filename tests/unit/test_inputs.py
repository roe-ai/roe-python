import pytest

from roe.models.file import FileUpload
from roe.utils.inputs import build_execution_multipart


def test_file_upload_path_is_read_not_left_open(tmp_path):
    path = tmp_path / "invoice.pdf"
    path.write_bytes(b"%PDF-1.4")

    _, files = build_execution_multipart({"document": FileUpload(path=str(path))})

    assert files["document"] == ("invoice.pdf", b"%PDF-1.4", "application/pdf")


@pytest.mark.parametrize(
    ("value", "expected"),
    [({"a": "b"}, '{"a": "b"}'), (["x", 1], '["x", 1]'), (3, "3"), (True, "True")],
)
def test_non_string_inputs_are_sent_as_form_values(value, expected):
    form_data, _ = build_execution_multipart({"field": value})

    assert form_data == {"field": expected}
