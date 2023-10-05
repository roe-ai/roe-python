from typing import Any
from src.roe_ai.agent import RoeAgent, AgentSchema
from src.roe_ai.agent_config import OpenAIConfig
from src.roe_ai.agent_input import PineconeInput, TextInput
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import concurrent.futures


class BookAgent(RoeAgent):
    """
    Book agent for the Roe platform.
    """

    @classmethod
    def schema(cls) -> AgentSchema:
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
        openai_api_key = self.config["openai"].api_key
        embed = OpenAIEmbeddings(
            openai_api_key=openai_api_key,
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

        document_content_description = "Book segments of the Gutenberg library."
        llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)
        retriever = SelfQueryRetriever.from_llm(
            llm,
            vectorstore,
            document_content_description,
            metadata_field_info,
            verbose=True,
        )
        docs = vectorstore.similarity_search(query=input["query"].get(), k=8)
        summaries = []

        

        def summarize_doc(doc, query):
            qdoc = f"Book {i}:\nMetadata:\n```{doc.metadata}```\nSegment:\n```{doc.page_content}```"
            prompt = f"""
                {qdoc}

                Given related segment above from a book in the Gutenberg library:
                Provide one long and detailed summary for the book segments without losing any information.
                Include the book title and author in the summary.
                The summary should take into account the query below.

                Query: {query}
            """
            return llm.call_as_llm(prompt)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for i, doc in enumerate(docs):
                futures.append(executor.submit(summarize_doc, doc, input["query"].get()))
            summaries = [f.result() for f in futures]

        
        return summaries


# book_agent = BookAgent()
# book_agent.setup_cli()
# res = book_agent.run(
#     {
#         "pinecone": PineconeInput(
#             "cc4c64ff-e33a-4ab1-b54a-5a47505910ce", "gcp-starter", "gutenburg"
#         ),
#         "query": TextInput("What caused the world war one?"),
#     }
# )
# print(res)
