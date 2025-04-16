from typing import Any

from app.factories.prompt_factory import PromptBuilder
from app.models.llm.enums import LLMTaskType
from app.services.abstract.llm.llm_service import LLMService
from app.services.abstract.llm.task_handler import TaskHandler


class SummarizationTaskHandler(TaskHandler):
    def __init__(self, llm_service: LLMService):
        """Initialize the task handler with a specific LLM service."""
        self.llm_service: LLMService = llm_service

    def handle(self, context: Any, query: str) -> str:
        """Handle the summarization task by building a prompt and asking the LLM service."""
        prompt = PromptBuilder.build(LLMTaskType.SUMMARIZATION, context, query)
        return self.llm_service.ask(prompt)
