from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, List, Optional

from src.roe_ai.agent_input import AgentInput
from src.roe_ai.agent_config import AgentConfig


@dataclass
class AgentSchema:
    """
    Standard configuration class for RoeAgent.

    Users should derive from this class to provide their specific configuration
    properties for their agents.
    """

    agent_input: dict[str, AgentInput]
    agent_config: dict[str, AgentConfig]

    @classmethod
    def from_agents(
        cls,
        agent_classes: List["RoeAgent"],
        agent_input: Optional[dict[str, AgentInput]] = None,
        agent_config: Optional[dict[str, AgentConfig]] = None,
    ) -> "AgentSchema":
        """
        Combines the schemas of multiple agents into a single schema.

        :param agents: List of agents to combine schemas.
        :return: Combined schema of the agents.
        """
        agent_input = agent_input or {}
        agent_config = agent_config or {}
        for agent_classes in agent_classes:
            agent_config.update(agent_classes.schema().agent_config)
        return AgentSchema(agent_input=agent_input, agent_config=agent_config)


class RoeAgent(ABC):
    """
    Base interface for AI agents to be wrapped for the Roe platform.
    """

    def __init__(self) -> None:
        self.config: dict[str, Any] = {}

    @classmethod
    @abstractmethod
    def schema(cls) -> AgentSchema:
        """
        Abstract method that derived agents must implement.

        :return: Agent's schema of inputs and configurations.
        """
        pass

    @abstractmethod
    def run_impl(self, input: Any) -> Any:
        """
        Abstract method that derived agents must implement.

        :param input: Input data for the agent.
        :return: Agent's output.
        """
        pass

    def _validate_schema(self) -> None:
        """
        Validates the agent's schema.

        :return: None
        """
        schema = self.schema()
        if schema is None:
            raise ValueError("Agent schema cannot be None.")
        assert isinstance(
            schema, AgentSchema
        ), "Agent schema implementation return must be of type AgentSchema."
        assert isinstance(
            schema.agent_input, dict
        ), "Agent input must be a dict."
        assert isinstance(
            schema.agent_config, dict
        ), "Agent config must be a dict."

        for input_name, input_type in schema.agent_input.items():
            assert issubclass(
                input_type, AgentInput
            ), f"Agent input {input_name} must be of type AgentInput."

        for config_name, config_type in schema.agent_config.items():
            assert issubclass(
                config_type, AgentConfig
            ), f"Agent config {config_name} must be of type AgentConfig."

    def _validate_input(self, input: Any) -> None:
        """
        Validates the agent's input.

        :param input: Input data for the agent.
        :return: None
        """
        schema = self.schema()
        assert isinstance(input, dict), "Agent input must be a dict."
        for input_name, input_type in schema.agent_input.items():
            assert (
                input_name in input
            ), f"Agent input {input_name} not found in input."
            assert isinstance(
                input[input_name], input_type
            ), f"Agent input {input_name} must be of type {input_type}."

    def setup_cli(self) -> None:
        """
        Use cli input to initialize self.config
        """
        self._validate_schema()
        schema = self.schema()
        for config_name, config_type in schema.agent_config.items():
            print(f"Please enter config for {config_name}")
            arg_type_map = config_type.get_constructor_args()
            arg_dict = {}
            for arg_name, arg_type in arg_type_map.items():
                arg_dict[arg_name] = arg_type(input(f"{arg_name}: "))

            self.config[config_name] = config_type(**arg_dict)

    def run(self, input: Any) -> Any:
        self._validate_input(input)

        return self.run_impl(input)
