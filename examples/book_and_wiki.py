from typing import Any
from src.roe_ai.agent_repo import RoeAgentRepo
from src.roe_ai.agent import RoeAgent, AgentSchema
from src.roe_ai.agent_input import PineconeInput, TextInput
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain.chat_models import ChatOpenAI


class KnowledgeableAgent(RoeAgent):
    """
    A knowledgeable agent that answers questions based on books and wikipedia.
    """

    def schema(cls) -> AgentSchema:
        agent_repo = RoeAgentRepo()
        return AgentSchema.from_agents(
            agent_classes=[agent_repo.get("book"), agent_repo.get("wiki")],
            agent_input={"pinecone": PineconeInput, "query": TextInput},
        )

    def run_impl(self, input: Any) -> Any:
        wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

        agent_repo = RoeAgentRepo()
        book_agent = agent_repo.get("book")()
        book_agent.config = self.config
        summaries = book_agent.run({
            "pinecone": input["pinecone"],
            "query": input["query"],
        })

        wiki_agent = agent_repo.get("wiki")()
        wiki_agent.config = self.config
        wiki_page = wiki_agent.run({"query": input["query"]})

        qsummary = "\n".join(
            f"Book segment {i}: {summary}"
            for i, summary in enumerate(summaries)
        )
        prompt = f"""
        Book summaries:
        {qsummary}

        Wikipedia page:
        {wiki_page}

        Given information above, answer the following qestions.

        Question: {input["query"].get()}
        """
        llm = ChatOpenAI(openai_api_key=self.config["openai"].api_key, model="gpt-3.5-turbo-16k", temperature=0)
        response = llm.call_as_llm(
            prompt,
        )

        return response


knowledgeable_agent = KnowledgeableAgent()
knowledgeable_agent.setup_cli()
res = knowledgeable_agent.run(
    {  
        "pinecone": PineconeInput(
            "cc4c64ff-e33a-4ab1-b54a-5a47505910ce", "gcp-starter", "gutenburg"
        ),
        "query": TextInput(
            "What caused the world war one?"
        ),
    }
)
print(res)


