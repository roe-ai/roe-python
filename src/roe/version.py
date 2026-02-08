"""Version information for the Roe AI SDK.

Reads the canonical version from package metadata (set by pyproject.toml)
so there is only one place to bump the version number.
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__: str = version("roe-ai")
except PackageNotFoundError:
    # Fallback when the package is not installed (e.g. editable dev mode
    # before the first `uv sync` / `pip install -e .`).
    __version__ = "0.0.0-dev"
