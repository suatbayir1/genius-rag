from abc import ABC, abstractmethod


class LLMService(ABC):
    @abstractmethod
    def ask(self, prompt: str) -> str:
        pass
