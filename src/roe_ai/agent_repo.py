from examples.book_agent import BookAgent
from examples.wiki_agent import WikiAgent
from src.roe_ai.agent import RoeAgent

REPO = {
    "book": BookAgent,
    "wiki": WikiAgent,
}


class RoeAgentRepo:
    def get(self, agent_id: str) -> RoeAgent:
        """
        Get an agent by its ID.

        :param agent_id: Agent ID.
        :return: Agent.
        """
        return REPO[agent_id]
