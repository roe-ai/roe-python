import roe
from roe.auth import RoeAuth
from roe.config import RoeConfig


def test_user_agent_uses_package_version():
    auth = RoeAuth(RoeConfig(api_key="key", organization_id="org"))

    assert auth.get_headers()["User-Agent"] == f"roe-python/{roe.__version__}"
