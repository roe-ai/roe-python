from roe.config import RoeConfig


def test_max_retries_zero_is_respected(monkeypatch):
    monkeypatch.setenv("ROE_MAX_RETRIES", "5")
    config = RoeConfig.from_env(api_key="key", organization_id="org", max_retries=0)
    assert config.max_retries == 0
