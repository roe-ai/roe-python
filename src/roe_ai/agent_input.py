from abc import ABC, abstractmethod
from typing import Any, List, Iterator, Optional
import boto3
import pinecone
import os


class AgentInput(ABC):
    """
    Base interface for AI agent inputs to be wrapped for the Roe platform.
    """

    @abstractmethod
    def get(self) -> Any:
        """
        Abstract method that derived inputs must implement.

        :return: Input data for the agent.
        """
        pass


class TextInput(AgentInput):
    """
    Text input for AI agents.
    """

    def __init__(self, text: str):
        """
        Initializes the TextInput with the provided text.

        :param text: Input text for the agent.
        """
        self.text = text

    def get(self) -> str:
        return self.text


class TwilioTextInput(TextInput):
    """
    Twilio voice input for AI agents.
    """

    pass


class S3Input(AgentInput):
    """
    S3 input for AI agents.
    """

    def __init__(
        self,
        access_key: str,
        secret_key: str,
        session_token: str,
        bucket: str,
        object: Optional[str] = None,
    ):
        """
        Initialize AWS boto3 client.
        """
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token,
        )
        self.bucket = bucket
        self.object = object

    def get(self) -> Any:
        pass


class PineconeInput(AgentInput):
    """
    Pinecone input for AI agents.
    """

    def __init__(self, api_key: str, env: str, index: str):
        """
        Initialize Pinecone client.
        """
        pinecone.init(
            api_key=api_key,
            environment=env,
        )
        self.pinecone_index = pinecone.Index(index)

    def get(self) -> pinecone.Index:
        return self.pinecone_index
