from enum import Enum


class LLMTaskType(str, Enum):
    QA = "qa"
    SUMMARIZATION = "summarization"
    EXPLAIN = "explain"
