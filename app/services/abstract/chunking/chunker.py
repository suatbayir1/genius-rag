from abc import ABC, abstractmethod
from typing import List


class Chunker(ABC):
    """Abstract base class for a chunker."""

    @abstractmethod
    def chunk(self, text: str) -> List[str]:
        """Chunk text into smaller parts.

        Args:
            text (str): The text to chunk.

        Returns:
            List[str]: The chunked text.
        """
