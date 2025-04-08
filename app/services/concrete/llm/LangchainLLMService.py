from typing import Any

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

from app.models.llm.enums import LLMTaskType
from app.models.llm.prompt_templates import PROMPT_TEMPLATES
from app.services.abstract.llm.LLMService import LLMService
from app.services.concrete.llm.task_type_detector import TaskTypeDetector


class LangchainLLMService(LLMService):
    def __init__(self, model_name: str = "llama3.2"):
        """Initialize the LangchainLLMService with a specific model.

        Args:
            model_name (str): The name of the model to use.
        """
        self.model = OllamaLLM(model=model_name)

    def answer(self, context: Any, question: str) -> str:
        task_type: LLMTaskType = TaskTypeDetector.detect(question)
        prompt: ChatPromptTemplate = ChatPromptTemplate.from_template(PROMPT_TEMPLATES[task_type])

        chain = prompt | self.model
        result = chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        return result
