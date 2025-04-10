from abc import ABC, abstractmethod
from typing import List


class Chunker(ABC):
    """Abstract base class for a chunker."""

    @abstractmethod
    def chunk(self, file_path: str) -> List[str]:
        """Chunk text into smaller parts.

        Args:
            file_path (str): The path of the file to chunk.

        Returns:
            List[str]: The chunked text.
        """
