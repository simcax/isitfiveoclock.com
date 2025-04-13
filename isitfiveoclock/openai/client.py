"""OpenAI Client implementing fast"""

from os import environ

from loguru import logger
from openai import OpenAI


class OpenAIClient:
    def __init__(self):
        self.api_key = environ.get("OPENAI_API_KEY")
        self.client()
        if self.api_key is None:
            logger.error(
                "OpenAI API key not found in environment variables. Set secret OPENAI_API_KEY"
            )
            raise ValueError("OpenAI API key not found in environment variables.")

    def client(self) -> OpenAI:
        """
        Create an OpenAI client with the given API key and base URL.

        Args:
            api_key (str): The OpenAI API key.
            api_base (str): The base URL for the OpenAI API.

        Returns:
            OpenAI: An instance of the OpenAI client.
        """
        self.oa_client = OpenAI(api_key=self.api_key)

    def query(self, question: str):
        response = self.oa_client.responses.create(
            model="gpt-4o",
            instructions="You are a travel guide, a bit drunk, but know your stuff and can give interesting unique information about locations",
            input=question,
        )
        return response.output_text
