from abc import ABC, abstractmethod
from typing import Any


class RoeAgentConfig:
    """
    Standard configuration class for RoeAgent.

    Users should derive from this class to provide their specific configuration
    properties for their agents.
    """
    def __init__(self):
        # Common configuration properties for all agents can be defined here
        pass


class RoeAgent(ABC):
    """
    Base interface for AI agents to be wrapped for the Roe platform.
    """

    def __init__(self, config: RoeAgentConfig):
        """
        Initializes the RoeAgent with the provided configuration.

        :param config: Configuration for the agent.
        """
        if not isinstance(config, RoeAgentConfig):
            raise ValueError("config must be an instance of RoeAgentConfig or its derivative.")
        self.config = config

    @abstractmethod
    def run_agent(self, input_data: Any) -> Any:
        """
        Abstract method that derived agents must implement.

        :param input_data: Input data for the agent.
        :return: Agent's output.
        """
        pass

    def run(self, input_data: Any) -> Any:
        """
        Uniform method to run any AI agent. Calls `run_agent`.

        :param input_data: Input data for the agent.
        :return: Agent's output.
        """
        return self.run_agent(input_data)
