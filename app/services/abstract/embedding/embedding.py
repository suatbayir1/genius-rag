from abc import ABC, abstractmethod
from typing import List


class Embedding(ABC):
    """Abstract base class for a embedding service."""

    @abstractmethod
    def encode(self, chunks: List[str]) -> List[float]:
        """Convert chunks into an embedding vector.

        Args:
            chunks (List[str]): The chunks to convert into an embedding vector.

        Returns:
            List[float]: The embedding vector representation of the text.
        """
