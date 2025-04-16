from enum import Enum
from typing import Callable, Optional

from app.services.abstract.embedding.embedding import Embedding
from app.services.concrete.embedding.code_embedding import CodeEmbedding
from app.services.concrete.embedding.text_embedding import TextEmbedding


class LLMTaskType(str, Enum):
    QA = "QA"
    SUMMARIZATION = "SUMMARIZATION"
    EXPLAIN = "EXPLAIN"
    DETECT_QUERY_TYPE = "DETECT_QUERY_TYPE"

    @property
    def embedding_model_class(self) -> type[Embedding]:
        mapping = {
            LLMTaskType.QA: TextEmbedding,
            LLMTaskType.SUMMARIZATION: TextEmbedding,
            LLMTaskType.EXPLAIN: CodeEmbedding,
        }

        return mapping[self]

    @classmethod
    def to_prompt_list(
        cls,
        exclude: Optional[set["LLMTaskType"]] = None,
        formatter: Optional[Callable[[str], str]] = None,
    ) -> str:
        exclude = exclude or set()
        formatter = formatter or (lambda val: f"-{val}")

        return "\n".join(formatter(member.value) for member in cls if member not in exclude)

    @classmethod
    def from_llm_output(cls, output: str) -> Optional["LLMTaskType"]:
        normalized = output.strip().upper()

        for member in cls:
            if member.value in normalized:
                return member
        return None
