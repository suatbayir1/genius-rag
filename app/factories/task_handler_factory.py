from app.exceptions.unsupported_task_exception import UnsupportedTaskError
from app.models.llm.enums import LLMTaskType
from app.services.abstract.llm.llm_service import LLMService
from app.services.abstract.llm.task_handler import TaskHandler
from app.services.concrete.llm.detect_query_task_handler import DetectQueryTaskHandler
from app.services.concrete.llm.explain_task_handler import ExplainTaskHandler
from app.services.concrete.llm.qa_task_handler import QATaskHandler
from app.services.concrete.llm.summarization_task_handler import (
    SummarizationTaskHandler,
)


class TaskHandlerFactory:
    def __init__(self, llm_service: LLMService):
        """Initialize the factory with a specific LLM service."""
        self.handlers = {
            LLMTaskType.QA: QATaskHandler(llm_service),
            LLMTaskType.SUMMARIZATION: SummarizationTaskHandler(llm_service),
            LLMTaskType.EXPLAIN: ExplainTaskHandler(llm_service),
            LLMTaskType.DETECT_QUERY_TYPE: DetectQueryTaskHandler(llm_service),
        }

    def get_handler(self, task_type: LLMTaskType) -> TaskHandler:
        """Get the appropriate task handler based on the task type."""
        if task_type not in self.handlers:
            raise UnsupportedTaskError(task_type)
        return self.handlers[task_type]
