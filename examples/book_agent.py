from typing import Any
from src.roe_ai.agent import RoeAgent, AgentSchema
from src.roe_ai.agent_config import OpenAIConfig
from src.roe_ai.agent_input import PineconeInput, TextInput
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo


class BookAgent(RoeAgent):
    """
    Book agent for the Roe platform.
    """

    def schema(self) -> AgentSchema:
        """
        Returns the BookAgent's configuration.

        :return: Agent's configuration.
        """
        return AgentSchema(
            agent_input={"pinecone": PineconeInput, "query": TextInput},
            agent_config={"openai": OpenAIConfig},
        )

    def run_impl(self, input: Any) -> Any:
        """
        Runs the BookAgent with the provided input data.

        :param input_data: Input data for the agent.
        :return: Agent's output.
        """
        embed = OpenAIEmbeddings(
            openai_api_key=self.config["openai"].api_key,
        )
        vectorstore = Pinecone(
            input["pinecone"].get(), embed.embed_query, "text"
        )
        metadata_field_info = [
            AttributeInfo(
                name="Text#",
                description="A unique identifier representing the index number of the document within the Gutenberg library.",
                type="integer",
            ),
            AttributeInfo(
                name="Type",
                description="Specifies the format or category of the document, such as 'Text', 'Audio', etc.",
                type="string",
            ),
            AttributeInfo(
                name="Issued",
                description="The publication date of the document, presented in the 'YYYY-MM-DD' format.",
                type="string",
            ),
            AttributeInfo(
                name="Title",
                description="The full title of the document, including any subtitles or additional descriptive information.",
                type="string",
            ),
            AttributeInfo(
                name="Language",
                description="The primary language in which the document is written, represented by its two-letter language code (e.g., 'en' for English).",
                type="string",
            ),
            AttributeInfo(
                name="Authors",
                description="The names of individuals or entities credited as authors of the document, listed in a standardized format.",
                type="string",
            ),
            AttributeInfo(
                name="Subjects",
                description="A list of topics, themes, or subjects addressed in the document, separated by semicolons.",
                type="string",
            ),
            AttributeInfo(
                name="LoCC",
                description="Library of Congress Classification (LoCC) codes associated with the document, providing a hint about its thematic categorization.",
                type="string",
            ),
            AttributeInfo(
                name="Bookshelves",
                description="Identifies the thematic bookshelves or collections within the Gutenberg library to which the document belongs.",
                type="string",
            ),
        ]

        document_content_description = "Books of the Gutenberg library."
        llm = OpenAI(openai_api_key=self.config["openai"].api_key, temperature=0)
        retriever = SelfQueryRetriever.from_llm(
            llm,
            vectorstore,
            document_content_description,
            metadata_field_info,
            verbose=True,
        )
        return retriever.get_relevant_documents(input["query"].get())


book_agent = BookAgent()
book_agent.setup_cli()
res = book_agent.run(
    {
        "pinecone": PineconeInput(
            "<secret>", "gcp-starter", "gutenburg"
        ),
        "query": TextInput("First paragraph of the Declaration of Independence of the U.S."),
    }
)
print(res)
