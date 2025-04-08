from abc import ABC, abstractmethod
from typing import Any


class LLMService(ABC):
    @abstractmethod
    def answer(self, context: Any, question: str) -> str:
        pass
