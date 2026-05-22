"""API modules for the Roe AI SDK."""

from roe.api._generated_registry import GENERATED_API_CLASSES
from roe.api.agents import AgentsAPI
from roe.api.policies import PoliciesAPI
from roe.api.users import UsersAPI

globals().update(
    {api_class.__name__: api_class for api_class in GENERATED_API_CLASSES.values()}
)
_generated_api_names = [
    api_class.__name__ for api_class in GENERATED_API_CLASSES.values()
]

__all__ = ["AgentsAPI", "PoliciesAPI", "UsersAPI", *_generated_api_names]

del _generated_api_names
