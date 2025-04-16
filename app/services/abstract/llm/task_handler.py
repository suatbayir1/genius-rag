from abc import ABC, abstractmethod
from typing import Any


class TaskHandler(ABC):
    @abstractmethod
    def handle(self, context: Any, query: str) -> str:
        pass
