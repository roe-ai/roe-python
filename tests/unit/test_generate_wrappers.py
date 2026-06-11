"""Tests for the body/manual/namespace paths in scripts/generate_wrappers.py."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

pytest.importorskip("ruamel.yaml", reason="requires the codegen dependency group")
from ruamel.yaml import YAML  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import generate_wrappers as gw  # noqa: E402

FIXTURE = ROOT / "scripts" / "fixtures" / "candidate_wrappers.yml"
API_DIR = ROOT / "src" / "roe" / "api"


def _fixture_apis() -> dict:
    return YAML(typ="safe").load(FIXTURE.read_text())["apis"]


def test_candidate_fixture_passes_manual_parity() -> None:
    gw._check_manual_parity(_fixture_apis(), API_DIR)


def test_manual_parity_fails_loudly_on_missing_method() -> None:
    apis = _fixture_apis()
    apis["agents"]["operations"].append(
        {"kind": "manual", "method_name": "definitely_missing", "docstring": ""}
    )
    with pytest.raises(gw.ManualWrapperParityError, match="definitely_missing"):
        gw._check_manual_parity(apis, API_DIR)


def test_split_module_renders_body_methods_and_namespaces() -> None:
    apis = _fixture_apis()
    module = gw._render_module("agents", apis["agents"], split=True)
    assert "class AgentsAPIGenerated:" in module
    assert "class AgentVersionsAPIGenerated:" in module
    assert "class AgentJobsAPIGenerated:" in module
    # body conventions
    assert "return PaginatedBaseAgentList.from_dict(response.json())" in module
    assert "organization_id=self._org_id" in module
    assert "UUID(str(agent_id))" in module
    assert "input_definitions=input_definitions or []" in module
    # refetch-with-retrieve (versions.create)
    assert "return self.retrieve(agent_id, str(version_id))" in module
    # manual methods never generated
    assert "def run(" not in module
    assert "def retrieve_status_many(" not in module


def test_all_manual_api_emits_nothing(tmp_path: Path) -> None:
    apis = {
        "users": {
            "class_name": "UsersAPI",
            "docstring": "API for users.",
            "operations": [{"kind": "manual", "method_name": "me", "docstring": ""}],
        }
    }
    (tmp_path / "users.py").write_text("def me(self):\n    pass\n")
    whole, split = gw._generate_modules(apis, tmp_path)
    assert whole == {}
    assert split == []
    assert not (tmp_path / "_users_generated.py").exists()
