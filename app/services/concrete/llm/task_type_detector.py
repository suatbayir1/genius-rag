from app.models.llm.enums import LLMTaskType


class TaskTypeDetector:
    @staticmethod
    def detect(question: str) -> LLMTaskType:
        question = question.lower()

        if any(keyword in question for keyword in ["what does", "explain", "describe", "meaning"]):
            return LLMTaskType.EXPLAIN
        elif any(keyword in question for keyword in ["summarize", "summary", "shorten"]):
            return LLMTaskType.SUMMARIZATION
        else:
            return LLMTaskType.QA
