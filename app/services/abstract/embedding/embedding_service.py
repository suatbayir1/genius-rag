from abc import ABC, abstractmethod
from typing import List


class EmbeddingService(ABC):
    """Abstract base class for a embedding service."""

    @abstractmethod
    def encode(self, text: str) -> List[float]:
        """Convert text into an embedding vector.

        Args:
            text (str): The text to convert into an embedding vector.

        Returns:
            List[float]: The embedding vector representation of the text.
        """
