import io
import subprocess
import sys

from roe.models.file import FileUpload


def test_file_upload_import_emits_no_deprecation_warning():
    result = subprocess.run(
        [
            sys.executable,
            "-W",
            "error::DeprecationWarning",
            "-c",
            "import roe.models.file",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr


def test_file_upload_accepts_file_object():
    buf = io.BytesIO(b"data")
    upload = FileUpload(file_obj=buf, filename="a.txt")

    assert upload.to_multipart_tuple() == ("a.txt", buf, "text/plain")
