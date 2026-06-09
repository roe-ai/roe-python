"""Command-line interface for the Roe SDK."""

from __future__ import annotations

import argparse
import getpass
import json
import os
import stat
import sys
import tempfile
from pathlib import Path
from typing import Any

from roe.client import RoeClient
from roe.api.table_upload_helpers import FAILED_UPLOAD_STATUSES
from roe.exceptions import RoeAPIException

DEFAULT_BASE_URL = "https://api.roe-ai.com"


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args) or 0)
    except (RoeAPIException, FileNotFoundError, TimeoutError, ValueError) as exc:
        _print_error(exc)
        return 1
    except KeyboardInterrupt:
        print("Interrupted", file=sys.stderr)
        return 130


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="roe",
        description="Roe AI command-line tools.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    auth = subparsers.add_parser("auth", help="Manage Roe CLI authentication.")
    auth_subparsers = auth.add_subparsers(dest="auth_command", required=True)

    login = auth_subparsers.add_parser(
        "login",
        help="Store Roe API credentials for CLI commands.",
    )
    _add_connection_options(login)
    login.set_defaults(func=_cmd_auth_login)

    whoami = auth_subparsers.add_parser(
        "whoami",
        help="Show the authenticated Roe user.",
    )
    _add_connection_options(whoami)
    whoami.add_argument("--json", action="store_true", help="Print JSON output.")
    whoami.set_defaults(func=_cmd_auth_whoami)

    table = subparsers.add_parser("table", help="Manage Roe tables.")
    table_subparsers = table.add_subparsers(dest="table_command", required=True)

    upload = table_subparsers.add_parser(
        "upload",
        help="Upload a local CSV as a Roe table.",
    )
    _add_connection_options(upload)
    upload.add_argument("path", help="Local CSV file path.")
    upload.add_argument(
        "--table",
        required=True,
        dest="table_name",
        help="Roe table name to create.",
    )
    upload.add_argument(
        "--no-headers",
        action="store_false",
        dest="with_headers",
        help="Treat every CSV row as data and generate column_1, column_2, etc.",
    )
    upload.add_argument(
        "--wait", action="store_true", help="Poll until import finishes."
    )
    upload.add_argument(
        "--poll-interval",
        type=float,
        default=2.0,
        help="Seconds between status checks when --wait is used.",
    )
    upload.add_argument(
        "--upload-timeout",
        type=float,
        default=None,
        help="Maximum seconds to wait for import completion.",
    )
    upload.add_argument("--json", action="store_true", help="Print JSON output.")
    upload.set_defaults(func=_cmd_table_upload)

    status_cmd = table_subparsers.add_parser(
        "status",
        help="Show a table upload/import status.",
    )
    _add_connection_options(status_cmd)
    status_cmd.add_argument("upload_id", help="Upload session ID.")
    status_cmd.add_argument("--json", action="store_true", help="Print JSON output.")
    status_cmd.set_defaults(func=_cmd_table_status)

    return parser


def _add_connection_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--api-key", help="Roe API key. Defaults to ROE_API_KEY/config."
    )
    parser.add_argument(
        "--organization-id",
        help="Roe organization ID. Defaults to ROE_ORGANIZATION_ID/config.",
    )
    parser.add_argument(
        "--base-url",
        help=f"Roe API base URL. Defaults to ROE_BASE_URL/config or {DEFAULT_BASE_URL}.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        help="HTTP timeout in seconds. Defaults to ROE_TIMEOUT/config.",
    )


def _cmd_auth_login(args: argparse.Namespace) -> int:
    config = _load_cli_config()
    api_key = _first_present(
        args.api_key, os.getenv("ROE_API_KEY"), config.get("api_key")
    )
    organization_id = _first_present(
        args.organization_id,
        os.getenv("ROE_ORGANIZATION_ID"),
        config.get("organization_id"),
    )
    base_url = _first_present(
        args.base_url,
        os.getenv("ROE_BASE_URL"),
        config.get("base_url"),
        DEFAULT_BASE_URL,
    )

    if not api_key:
        api_key = _prompt_secret("Roe API key: ")
    if not organization_id:
        organization_id = _prompt_text("Roe organization ID: ")

    next_config = {
        "api_key": api_key,
        "organization_id": organization_id,
        "base_url": base_url,
    }
    if args.timeout is not None:
        next_config["timeout"] = args.timeout
    elif config.get("timeout") is not None:
        next_config["timeout"] = config["timeout"]
    _save_cli_config(next_config)
    print(f"Saved Roe credentials to {_config_path()}")
    return 0


def _cmd_auth_whoami(args: argparse.Namespace) -> int:
    with _new_client(args) as client:
        result = client.users.me()
    _print_result(result, as_json=args.json)
    return 0


def _cmd_table_upload(args: argparse.Namespace) -> int:
    with _new_client(args) as client:
        result = client.tables.upload_large(
            args.path,
            table_name=args.table_name,
            with_headers=args.with_headers,
            wait=args.wait,
            interval=args.poll_interval,
            timeout=args.upload_timeout,
        )
    _print_result(result, as_json=args.json)
    upload_id = result.get("upload_id")
    if not args.json and result.get("status") == "IMPORTING" and upload_id:
        print(f"Status: roe table status {upload_id} --json")
    if result.get("status") in FAILED_UPLOAD_STATUSES:
        _print_terminal_failure("Table upload", result.get("error"))
        return 1
    return 0


def _cmd_table_status(args: argparse.Namespace) -> int:
    with _new_client(args) as client:
        result = client.tables.upload_status(upload_id=args.upload_id)
    _print_result(result, as_json=args.json)
    return 0


def _new_client(args: argparse.Namespace) -> RoeClient:
    config = _connection_config(args)
    return RoeClient(
        api_key=config["api_key"],
        organization_id=config["organization_id"],
        base_url=config["base_url"],
        timeout=config.get("timeout"),
    )


def _connection_config(args: argparse.Namespace) -> dict[str, Any]:
    config = _load_cli_config()
    api_key = _first_present(
        args.api_key, os.getenv("ROE_API_KEY"), config.get("api_key")
    )
    organization_id = _first_present(
        args.organization_id,
        os.getenv("ROE_ORGANIZATION_ID"),
        config.get("organization_id"),
    )
    base_url = _first_present(
        args.base_url,
        os.getenv("ROE_BASE_URL"),
        config.get("base_url"),
        DEFAULT_BASE_URL,
    )
    timeout = _first_present(
        args.timeout,
        _parse_float_env("ROE_TIMEOUT"),
        config.get("timeout"),
    )
    if not api_key:
        raise ValueError(
            "Missing Roe API key. Run `roe auth login` or set ROE_API_KEY."
        )
    if not organization_id:
        raise ValueError(
            "Missing Roe organization ID. Run `roe auth login` or set ROE_ORGANIZATION_ID."
        )
    return {
        "api_key": api_key,
        "organization_id": organization_id,
        "base_url": base_url,
        "timeout": timeout,
    }


def _config_path() -> Path:
    override = os.getenv("ROE_CONFIG_FILE")
    if override:
        return Path(override).expanduser()
    config_home = os.getenv("XDG_CONFIG_HOME")
    base = Path(config_home).expanduser() if config_home else Path.home() / ".config"
    return base / "roe" / "config.json"


def _load_cli_config() -> dict[str, Any]:
    path = _config_path()
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Roe config file is not valid JSON: {path}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"Roe config file must contain a JSON object: {path}")
    return data


def _save_cli_config(data: dict[str, Any]) -> None:
    path = _config_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as out:
            out.write(json.dumps(data, indent=2, sort_keys=True) + "\n")
        os.chmod(temp_path, stat.S_IRUSR | stat.S_IWUSR)
        os.replace(temp_path, path)
        os.chmod(path, stat.S_IRUSR | stat.S_IWUSR)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def _prompt_secret(prompt: str) -> str:
    if not sys.stdin.isatty():
        raise ValueError("Missing API key and stdin is not interactive.")
    value = getpass.getpass(prompt).strip()
    if not value:
        raise ValueError("API key is required.")
    return value


def _prompt_text(prompt: str) -> str:
    if not sys.stdin.isatty():
        raise ValueError("Missing organization ID and stdin is not interactive.")
    value = input(prompt).strip()
    if not value:
        raise ValueError("Organization ID is required.")
    return value


def _first_present(*values: Any) -> Any:
    for value in values:
        if value not in (None, ""):
            return value
    return None


def _parse_float_env(name: str) -> float | None:
    value = os.getenv(name)
    return float(value) if value else None


def _print_result(value: Any, *, as_json: bool) -> None:
    payload = _to_jsonable(value)
    if as_json:
        print(json.dumps(payload, default=str, sort_keys=True))
        return
    if isinstance(payload, dict):
        for key, item in payload.items():
            print(f"{key}: {item}")
    else:
        print(payload)


def _to_jsonable(value: Any) -> Any:
    if hasattr(value, "to_dict"):
        return value.to_dict()
    if isinstance(value, dict):
        return {key: _to_jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_to_jsonable(item) for item in value]
    return value


def _print_error(exc: Exception) -> None:
    if isinstance(exc, RoeAPIException):
        prefix = (
            f"Roe API error {exc.status_code}" if exc.status_code else "Roe API error"
        )
        print(f"{prefix}: {exc.message}", file=sys.stderr)
        return
    print(str(exc), file=sys.stderr)


def _print_terminal_failure(label: str, error: Any) -> None:
    message = str(error) if error else "reached a failed terminal status"
    print(f"{label} failed: {message}", file=sys.stderr)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
