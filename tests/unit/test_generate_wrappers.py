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


def test_partial_module_imports_uuid_without_unset_usage():
    module = _load_generate_wrappers_module()

    rendered = module._render_partial_api_module(
        "widgets",
        {
            "class_name": "WidgetsAPI",
            "docstring": "API for widgets.",
            "operations": [
                {
                    "method_name": "list",
                    "endpoint_module": "roe._generated.api.widgets.widgets_list",
                    "return_import": "roe._generated.models.widget.Widget",
                    "return_type": "Widget",
                    "empty_response_message": "widgets list returned no data",
                },
                {
                    "method_name": "patch",
                    "endpoint_module": "roe._generated.api.widgets.widgets_patch",
                    "return_type": "Any",
                    "empty_response_message": "widgets patch returned no data",
                }
            ],
        },
    )

    assert "from typing import Any" in rendered
    assert "from uuid import UUID" in rendered
    assert "from roe._generated.types import UNSET" not in rendered
    assert "config: RoeConfig" in rendered
    assert "_raw: AuthenticatedClient" in rendered
