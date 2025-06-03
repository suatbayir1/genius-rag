from abc import ABC, abstractmethod


class GuardService(ABC):
    @abstractmethod
    def is_safe_prompt(self, prompt: str) -> bool:
        """Check user prompt is safe.

        Args:
            prompt (str): User prompt

        Returns:
            bool: safe or unsafe
        """
