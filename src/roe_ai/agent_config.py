from abc import ABC, abstractmethod
from typing import Any
import inspect


class AgentConfig(ABC):
    @classmethod
    def get_constructor_args(cls) -> dict[str, type]:
        # Get the signature of the constructor
        sig = inspect.signature(cls.__init__)

        # Get a mapping of parameter names to their annotations
        param_types = {
            k: v.annotation
            for k, v in sig.parameters.items()
            if v.annotation is not inspect.Parameter.empty
        }

        # Remove 'self' from the mapping, as it's not an argument passed by the user
        param_types.pop("self", None)

        return param_types


class OpenAIConfig(AgentConfig):
    def __init__(
        self,
        api_key: str,
    ):
        super().__init__()
        self.api_key = api_key
