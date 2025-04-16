from langchain_ollama.llms import OllamaLLM

from app.services.abstract.llm.llm_service import LLMService


class LangchainLLMService(LLMService):
    def __init__(self, model_name: str = "llama3.2"):
        """Initialize the LangchainLLMService with a specific model.

        Args:
            model_name (str): The name of the model to use.
        """
        self.model = OllamaLLM(model=model_name)

    def ask(self, prompt: str) -> str:
        return self.model.invoke(prompt)
