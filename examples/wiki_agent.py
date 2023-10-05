from typing import Any
from src.roe_ai.agent import RoeAgent, AgentSchema
from src.roe_ai.agent_input import TextInput
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper


class WikiAgent(RoeAgent):
    """
    Wikipedia agent.
    """

    @classmethod
    def schema(cls) -> AgentSchema:
        return AgentSchema(
            agent_input={"query": TextInput},
            agent_config={},
        )

    def run_impl(self, input: Any) -> Any:
        wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

        return wikipedia.run(input["query"].get())


# wiki_agent = WikiAgent()
# wiki_agent.setup_cli()
# res = wiki_agent.run(
#     {
#         "query": TextInput(
#             "Can you tell me if Kevin McCarthy is still in the house?"
#         ),
#     }
# )
# print(res)
