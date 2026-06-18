from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import types


def _load_generate_wrappers_module():
    ruamel = types.ModuleType("ruamel")
    ruamel_yaml = types.ModuleType("ruamel.yaml")
    ruamel_yaml.YAML = object
    sys.modules.setdefault("ruamel", ruamel)
    sys.modules.setdefault("ruamel.yaml", ruamel_yaml)

    path = Path(__file__).resolve().parents[2] / "scripts" / "generate_wrappers.py"
    spec = importlib.util.spec_from_file_location("generate_wrappers", path)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_main_deletes_stale_partial_modules_for_hand_maintained_apis(
    tmp_path, monkeypatch
):
    module = _load_generate_wrappers_module()
    stale = tmp_path / "_agents_generated.py"
    stale.write_text("# stale\n")

    monkeypatch.setattr(module, "API_DIR", tmp_path)
    monkeypatch.setattr(module, "REGISTRY_PATH", tmp_path / "_generated_registry.py")
    monkeypatch.setattr(
        module,
        "_load_contract",
        lambda: {
            "apis": {
                "agents": {
                    "class_name": "AgentsAPI",
                    "docstring": "API for agents.",
                    "operations": [
                        {
                            "kind": "manual",
                            "method_name": "run",
                            "docstring": "Run an agent.",
                        }
                    ],
                }
            }
        },
    )
    monkeypatch.setattr(module, "_sync_readme_release_banner", lambda: None)
    monkeypatch.setattr(module, "_sync_readme_block", lambda: None)

    module.main()

    assert not stale.exists()
